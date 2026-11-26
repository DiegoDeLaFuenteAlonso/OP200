# ARQUITECTURA DEL SISTEMA Y DECISIONES TÉCNICAS — PROYECTO AYUNTAMIENTO DE ROPERUELOS DEL PÁRAMO

> **Cómo usar este documento en la entrevista:** Cuando el arquitecto o jefe de proyecto de Seresco te pregunte *«¿Cómo estructuraste por dentro la aplicación del Ayuntamiento y por qué tomaste esas decisiones?»*, apóyate en este diseño en capas.

---

## 1. DIAGRAMA ASCII DE LA ARQUITECTURA COMPLETA

```text
+-----------------------------------------------------------------------------------+
|                     NAVEGADOR WEB DEL PERSONAL DEL AYUNTAMIENTO                   |
|    (Secretaría-Intervención / Ventanilla Administrativa — Red Local Municipal)    |
+-----------------------------------------+-----------------------------------------+
                                          |
                 Peticiones HTTP / AJAX   |   Descarga Stream Binario
               (Postback JSF ViewState)   |   (Content-Type: application/pdf)
                                          v
+-----------------------------------------------------------------------------------+
|                 SERVIDOR DE APLICACIONES JAVA (WildFly / Tomcat)                  |
|                                                                                   |
|  +-----------------------------------------------------------------------------+  |
|  | 1. CAPA DE PRESENTACIÓN (JSF 2.3 Facelets + PrimeFaces)                     |  |
|  |    - Controlador Frontal: FacesServlet (Ciclo de vida de 6 fases)           |  |
|  |    - Vista XHTML: gestion_expedientes_agricolas.xhtml (<p:dataTable>)       |  |
|  |    - Backing Bean: ExpedienteManagedBean (@Named + @ViewScoped)             |  |
|  +----------------------+-----------------------------------+------------------+  |
|                         | @Inject                           | @Inject             |
|                         v                                   v                     |
|  +--------------------------------------+  +-----------------------------------+  |
|  | 2. CAPA DE SERVICIO / NEGOCIO        |  | 3. MOTOR DE INFORMES DOCUMENTALES |  |
|  |    - ExpedienteService               |  |    - JasperReportGeneratorService |  |
|  |    - @Transactional (ACID)           |  |    - Caché ConcurrentHashMap de   |  |
|  |    - Validación SIGPAC y cálculo     |  |      plantillas .jasper compiladas|  |
|  |      exacto con BigDecimal (scale 4) |  |    - JasperFillManager +          |  |
|  |                                      |  |      JasperExportManager (PDF/XLS)|  |
|  +----------------------+---------------+  +-----------------+-----------------+  |
|                         | @Inject                            |                    |
|                         v                                    |                    |
|  +-----------------------------------------------------------+-----------------+  |
|  | 4. CAPA DE ACCESO A DATOS Y PERSISTENCIA (ExpedienteRepository)             |  |
|  |    - JPA / Hibernate (EntityManager): JPQL con JOIN FETCH (Sin N+1 queries) |  |
|  |    - JDBC Puro (DataSource Pool + PreparedStatement): Consultas masivas     |  |
|  |      para alimentar JRBeanCollectionDataSource o Connection directa         |  |
|  +--------------------------------------+--------------------------------------+  |
+-----------------------------------------|-----------------------------------------+
                                          |
                           Pool JDBC      |      (Evolutivo 2024: Script/API Python
                         (Puerto 5432)    |       para carga y limpieza CSV Catastro)
                                          v
+-----------------------------------------------------------------------------------+
|                   BASE DE DATOS RELACIONAL SQL (PostgreSQL / MySQL)               |
|  - Tablas: titulares, parcelas_rusticas, expedientes_municipales,                 |
|            expediente_parcelas, certificados_emitidos, auditoria_cambios          |
|  - Vista de Reporting: v_certificado_parcelas_titular                             |
|  - Índices B-Tree: idx_exp_campania_estado, uq_sigpac_municipio_pol_par_rec       |
+-----------------------------------------------------------------------------------+
```

---

## 2. LAS 5 DECISIONES TÉCNICAS DE ARQUITECTURA Y SU JUSTIFICACIÓN

### Decisión 1: Uso de `@ViewScoped` en `ExpedienteManagedBean` en lugar de `@RequestScoped` o `@SessionScoped`
- **Problema:** La pantalla principal (`gestion_expedientes_agricolas.xhtml`) combina tres interacciones sin cambiar de página: filtrar expedientes con AJAX, paginar/ordenar la tabla `<p:dataTable>` y abrir un diálogo modal `<p:dialog>` para revisar observaciones, aprobar el expediente o descargar el PDF.
- **Por qué descarté `@RequestScoped`:** Con `@RequestScoped`, al pulsar el botón *"Aprobar Expediente"* dentro del diálogo modal, JSF reconstruiría el Bean desde cero antes de invocar la acción, perdiendo la referencia a `expedienteSeleccionado` o re-ejecutando innecesariamente la consulta SQL de toda la tabla en cada petición AJAX.
- **Por qué descarté `@SessionScoped`:** Guardar listas de entidades y resultados de búsqueda en la sesión HTTP consume memoria Heap durante toda la jornada del administrativo y provoca conflictos de estado si el funcionario abre dos pestañas del navegador a la vez para consultar dos agricultores distintos.
- **Solución adoptada (`@ViewScoped`):** Mantiene vivos en memoria los filtros, la lista de la tabla y el `expedienteSeleccionado` única y exclusivamente mientras el usuario sigue en esa vista XHTML, liberando la memoria automáticamente al cambiar de pantalla.

---

### Decisión 2: Prevención del problema `N+1` y de `LazyInitializationException` combinando `FetchType.LAZY` con `JOIN FETCH`
- **Problema:** Un `ExpedienteAgrarioEntity` está relacionado con un `Titular` (`@ManyToOne`) y con múltiples `Parcelas` (`@OneToMany`). Si dejáramos `@ManyToOne` en su valor por defecto (`EAGER`), cualquier consulta simple cargaría tablas innecesarias; pero si lo ponemos en `LAZY` y la vista JSF evalúa `#{exp.titular.nombreCompleto}` fuera de la transacción, salta `LazyInitializationException`.
- **Solución adoptada:**
  1. Declarar **todas** las relaciones JPA como **`FetchType.LAZY`** en las clases `@Entity`.
  2. Crear consultas JPQL específicas en `ExpedienteRepository` según lo que necesita cada caso de uso:
     - Para la bandeja de búsqueda JSF: `SELECT e FROM ExpedienteAgrarioEntity e JOIN FETCH e.titular t WHERE ...` (trae expediente + titular en 1 sola query SQL, sin cargar todavía las 40 parcelas de cada fila).
     - Para abrir el detalle o aprobar el expediente: `SELECT DISTINCT e FROM ExpedienteAgrarioEntity e JOIN FETCH e.titular LEFT JOIN FETCH e.parcelasAsociadas WHERE e.codigoExpediente = :codigo` (trae cabecera, titular y todas sus parcelas en 1 sola query SQL).

---

### Decisión 3: Caché en memoria de plantillas compiladas `.jasper` (`ConcurrentHashMap`) para no bloquear la CPU
- **Problema:** Compilar un archivo XML `.jrxml` con `JasperCompileManager.compileReport(...)` parsea el XML, valida el esquema XSD y genera bytecode de expresiones internamente, lo que puede tardar entre 400 ms y 1,5 segundos y consumir mucha CPU si se ejecuta en cada clic del usuario.
- **Solución adoptada:**
  1. Precompilar los `.jrxml` a `.jasper` en el empaquetado Maven y además mantener en `JasperReportGeneratorService` (`@ApplicationScoped`) un **`ConcurrentHashMap<String, JasperReport>`**.
  2. La primera vez que se solicita un informe se carga el objeto `JasperReport` en el mapa concurrente (que es *thread-safe* y puede ser reutilizado simultáneamente por múltiples hilos), y en las siguientes peticiones se pasa directamente a `JasperFillManager.fillReport(...)`, bajando el tiempo de generación del PDF a **30–80 milisegundos**.

---

### Decisión 4: Elección de `JRBeanCollectionDataSource` alimentado por DTOs JDBC (`PreparedStatement`) para informes complejos
- **Problema:** Algunos certificados requerían verificar reglas de negocio en Java antes de emitir el PDF (comprobar que el expediente estuviera en estado `APROBADO`, formatear advertencias de regadío y registrar en la tabla `certificados_emitidos` el Código Seguro de Verificación `CSV`).
- **Solución adoptada:**
  - En lugar de acoplar toda esa lógica dentro del XML de la plantilla, creé en el repositorio una consulta JDBC ultrarrápida con `PreparedStatement` y `try-with-resources` que proyecta los datos ya limpios en una lista de `ResumenCertificadoCatastralDTO`.
  - El servicio valida la lista, genera el código `CSV`, inyecta los metadatos en el `Map<String, Object>` de parámetros (`$P{}`) y pasa la colección envuelta en `new JRBeanCollectionDataSource(filasParcelas)` a `JasperFillManager`, logrando máxima velocidad, seguridad contra Inyección SQL y facilidad de pruebas unitarias.

---

### Decisión 5: Aritmética exacta con `BigDecimal` (`NUMERIC(10,4)`) en Java, SQL y Jasper Reports
- **Problema:** En el ámbito catastral y SIGPAC, las superficies se expresan en hectáreas con 4 decimales (`0.0001 ha = 1 centiárea = 1 m²`). Usar `Double` producía redondeos inexactos donde la suma de las filas del certificado no cuadraba por una diezmilésima con el total de la cabecera.
- **Solución adoptada:** Unificar el tipo de dato en las tres capas:
  - **Base de datos SQL:** `NUMERIC(10,4)` para hectáreas y `NUMERIC(12,2)` para importes en euros.
  - **Entidades y Servicios Java:** `java.math.BigDecimal` con `RoundingMode.HALF_UP`.
  - **Plantilla `.jrxml` de Jasper Reports:** `<field name="superficieHa" class="java.math.BigDecimal"/>` y `<variable name="TOTAL_HECTAREAS_TITULAR" class="java.math.BigDecimal" calculation="Sum"/>` con máscara `pattern="#,##0.0000"`.
