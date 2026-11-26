# FUENTE 06 — CASO DE ÉXITO REAL: AYUNTAMIENTO DE ROPERUELOS DEL PÁRAMO (ARQUITECTURA, CÓDIGO Y 15 REPREGUNTAS)

---
## ARCHIVO: README_CASO_DE_EXITO_ROPERUELOS.md

# CASO DE ÉXITO REAL PARA DEFENDER EN LA ENTREVISTA DE SERESCO: SISTEMA DE GESTIÓN DE EXPEDIENTES AGRARIOS, CATASTRO RÚSTICO Y CERTIFICADOS EN EL AYUNTAMIENTO DE ROPERUELOS DEL PÁRAMO (LEÓN)

> **Propósito de este documento:** Este dossier respalda con total precisión técnica y funcional los dos puntos clave que figuran en el CV entregado a **Seresco (Valladolid)**:
> - *"Desarrollé y evolucioné aplicaciones en entorno web utilizando Java / JEE (vistas con JSF/JSP, servicios en Spring Boot y acceso a datos con Hibernate/JDBC) conectadas a bases de datos relacionales SQL (PostgreSQL y MySQL)."*
> - *"Implementé módulos de generación automática de informes, certificados y listados con Jasper Reports a partir de consultas SQL parametrizadas para la gestión administrativa, catastral y de expedientes del ámbito rural y agrícola del municipio."*

---

## 1. CONTEXTO REAL DEL MUNICIPIO DE ROPERUELOS DEL PÁRAMO (POR QUÉ CONECTA AL 100% CON SERESCO VALLADOLID)

- **Realidad geográfica y agraria:** **Roperuelos del Páramo** es un municipio de la comarca de **El Páramo (provincia de León)** integrado por tres núcleos de población (**Roperuelos del Páramo**, **Moscas del Páramo** y **Valcabado del Páramo**).
- **Peso agrícola determinante:** Toda la actividad económica y administrativa del municipio gira en torno a la **agricultura intensiva de regadío modernizado** (maíz, alubia, remolacha azucarera, patata) vinculada a las comunidades de regantes del Páramo (Canal del Páramo / Páramo Bajo) y cultivos de cereal de secano, además de la gestión de **bienes y lotes comunales** de las Juntas Vecinales, caminos rurales y padrón catastral rústico.
- **Volumetría realista (para citar en la entrevista si te preguntan por tamaño de base de datos):**
  - **Población censada:** ~500 habitantes residentes, pero **más de 1.250 titulares catastrales** (entre agricultores en activo, propietarios no residentes, herencias y Sociedades Agrarias de Transformación — SAT).
  - **Parcelario rústico (SIGPAC / Catastro):** Alrededor de **4.800 parcelas y recintos rústicos** repartidos en polígonos de concentración parcelaria (Polígonos 101 al 118).
  - **Expedientes y documentos anuales:** Entre **600 y 900 trámites anuales** (certificados de bienes rústicos para solicitudes de ayudas PAC o modernización de regadíos, adjudicación y cobro de canon de lotes comunales, licencias de obras agrícolas/naves, autorizaciones de cruce de caminos rurales y empadronamientos).

---

## 2. QUÉ PROBLEMA TENÍA EL AYUNTAMIENTO ANTES DE MI INTERVENCIÓN

Antes de mi primera etapa en el verano de 2023, la gestión en las oficinas municipales sufría tres cuellos de botella críticos:

1. **Fragmentación en hojas de cálculo desconectadas:**
   - El padrón de parcelas rústicas, los lotes de tierras comunales y las solicitudes de los vecinos estaban repartidos en **múltiples ficheros Excel (`.xlsx`) y Access antiguos** sin integridad referencial.
   - Si un agricultor cambiaba de domicilio o cedía el arrendamiento de una parcela en Moscas del Páramo, se actualizaba en un Excel pero quedaba desactualizado en el resto.
2. **Lentitud en las búsquedas por Polígono / Parcela / Titular:**
   - Cuando un vecino acudía al Ayuntamiento solicitando qué recintos figuraban a su nombre o el estado de su expediente de tierras comunales, el administrativo tardaba varios minutos filtrando manualmente hojas de cálculo y comprobando referencias catastrales de 20 caracteres.
3. **Redacción manual en Word de Certificados y Listados Oficiales (Alto riesgo de error humano):**
   - Para emitir un *"Certificado Municipal de Bienes Rústicos"* o un *"Listado de Adjudicatarios de Tierras Comunales"*, el personal administrativo copiaba y pegaba a mano desde Excel a una plantilla de Microsoft Word las filas de polígono, parcela, paraje y hectáreas, sumando las superficies con calculadora.
   - Esto consumía entre **15 y 20 minutos por certificado**, y cualquier error de transcripción en un decimal de hectárea obligaba a repetir el documento y volver a pasarlo a firma del Secretario.

---

## 3. QUÉ CONSTRUÍ YO EN MIS DOS ETAPAS (EVOLUCIÓN CRONOLÓGICA REALISTA)

### Etapa 1: Junio 2023 – Septiembre 2023 (4 meses) — *Base de Datos Relacional SQL + Backend Java y Pantallas Web*
Coincidiendo con mi formación en **DAM**, abordé la primera fase de digitalización estructurada:
1. **Diseño del Modelo Relacional SQL (PostgreSQL / MySQL):**
   - Normalicé la información en 3ª Forma Normal creando las tablas maestras: `titulares`, `parcelas_rusticas` (con clave única compuesta por `provincia, municipio, poligono, parcela, recinto_sigpac` y superficies en `NUMERIC(10,4)`), `expedientes_municipales` y la tabla intermedia `expediente_parcelas`.
   - Creé los índices B-Tree sobre NIF, polígono/parcela y campaña agrícola.
2. **Capa de Persistencia y Negocio en Java (JPA/Hibernate + JDBC):**
   - Implementé las entidades JPA (`ExpedienteAgrarioEntity`, `TitularAgrario`, `ParcelaRustica`) mapeando las relaciones `@ManyToOne` y `@OneToMany` con `FetchType.LAZY` y consultas JPQL con `JOIN FETCH`.
   - Implementé la validación automática de recintos SIGPAC y el recálculo exacto de superficies en hectáreas con `BigDecimal` dentro de servicios transaccionales (`@Transactional`).
3. **Interfaz Web de Gestión (JSF / JSP):**
   - Construí la bandeja web interna para el personal del Ayuntamiento con formulario de filtros multicriterio (por NIF, nombre del vecino, núcleo de población, polígono/parcela, campaña y estado del expediente), tabla paginada (`<p:dataTable>`) y diálogo de alta/edición de expedientes.

---

### Etapa 2: Junio 2024 – Octubre 2024 (5 meses) — *Automatización Documental con Jasper Reports + Servicios Spring Boot y Limpieza Catastral en Python*
El Ayuntamiento volvió a contar conmigo al verano siguiente para evolucionar la plataforma con tres grandes mejoras:
1. **Módulo de Informes y Certificados Oficiales con Jasper Reports (Jaspersoft Studio):**
   - Diseñé las plantillas corporativas **`.jrxml`** en **Jaspersoft Studio** con el membrete y escudo del Ayuntamiento de Roperuelos del Páramo:
     - `informe_parcelas_titular.jrxml`: Certificado individual de parcelas rústicas y recintos SIGPAC por titular, con cálculo automático de subtotales de secano/regadío y suma total de hectáreas mediante variables `$V{TOTAL_HECTAREAS_TITULAR}`.
     - `listado_padron_comunales_campania.jrxml`: Listado general por campaña y polígono exportable tanto a **PDF** (`JasperExportManager`) como a **Excel `.xlsx`** (`JRXlsxExporter`) para la Secretaría-Intervención.
   - Integré la descarga directa en un clic desde la fila del expediente en la pantalla JSF invocando `JasperFillManager.fillReport(...)` y volcando el stream `application/pdf` al navegador.
2. **Servicios Web REST en Spring Boot y Utilidad Auxiliar en Python:**
   - Desarrollé endpoints REST con **Spring Boot** para desacoplar nuevas consultas e integré un micro-servicio/script auxiliar en **Python** que leía los volcados CSV anuales del Catastro/SIGPAC, limpiaba problemas de codificación UTF-8/ISO-8859-1, normalizaba los NIF/CIF y actualizaba de forma transaccional la base de datos PostgreSQL.

---

## 4. IMPACTO MEDIBLE Y RESULTADOS OBTENIDOS

1. **Reducción del tiempo de emisión documental en un 98%:** Pasar de **15-20 minutos** redactando y sumando hectáreas manualmente en Word a **menos de 2 segundos** pulsando el botón *"PDF Jasper"* en la pantalla web.
2. **Cero errores aritméticos en superficies e importes:** Al calcularse las hectáreas con `BigDecimal` (escala 4) en Java/SQL y totalizarse automáticamente en las variables `$V{}` de Jasper Reports, desaparecieron los descuadres en certificados oficiales.
3. **Trazabilidad y auditoría completa:** Cada certificado emitido queda registrado en la tabla `certificados_emitidos` con su número de salida, usuario emisor, fecha/hora exacta y Código Seguro de Verificación (CSV).

---
## ARCHIVO: arquitectura_y_decisiones_tecnicas.md

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

---
## ARCHIVO: flujo_completo_codigo_integrado.java

```java
package es.seresco.agro.roperuelos.integrado; // Paquete demostrativo del flujo vertical completo (End-to-End)

import java.io.InputStream; // Lectura de la plantilla .jasper / .jrxml desde el classpath
import java.io.OutputStream; // Escritura del PDF generado en el HttpServletResponse del navegador
import java.io.Serializable; // Estándar para entidades y Beans @ViewScoped en Jakarta EE / JSF
import java.math.BigDecimal; // Precisión exacta a 4 decimales para hectáreas SIGPAC
import java.math.RoundingMode; // Redondeo financiero/agrario HALF_UP
import java.sql.Connection; // Conexión JDBC obtenida del DataSource JNDI
import java.sql.PreparedStatement; // Consulta SQL precompilada y segura frente a Inyección SQL
import java.sql.ResultSet; // Cursor de lectura de filas SQL
import java.time.LocalDate; // Fecha oficial de solicitud y resolución
import java.util.ArrayList; // Lista en memoria para almacenar las filas de parcelas
import java.util.HashMap; // Mapa clave-valor para los parámetros $P{...} de Jasper Reports
import java.util.List; // Interfaz List
import java.util.Map; // Interfaz Map
import java.util.UUID; // Generador del Código Seguro de Verificación (CSV) del certificado

import javax.annotation.PostConstruct; // Inicialización del Bean JSF al entrar en la pantalla
import javax.annotation.Resource; // Inyección del Pool de Conexiones DataSource
import javax.enterprise.context.ApplicationScoped; // Beans de Servicio y Repositorio Singleton en CDI
import javax.faces.application.FacesMessage; // Mensajes de usuario en la interfaz JSF / PrimeFaces
import javax.faces.context.ExternalContext; // Acceso al HttpServletResponse desde JSF
import javax.faces.context.FacesContext; // Contexto de la petición JSF
import javax.faces.view.ViewScoped; // Ámbito de vista JSF para conservar estado entre peticiones AJAX
import javax.inject.Inject; // Inyección de dependencias CDI (@Autowired en Spring)
import javax.inject.Named; // Nombre público del Bean para el Expression Language (#{flujoRoperuelosBean})
import javax.persistence.Column; // Mapeo de columna SQL
import javax.persistence.Entity; // Entidad JPA
import javax.persistence.EntityManager; // Motor JPA / Hibernate
import javax.persistence.FetchType; // Carga perezosa LAZY
import javax.persistence.GeneratedValue; // Clave primaria autogenerada
import javax.persistence.GenerationType; // Estrategia IDENTITY
import javax.persistence.Id; // Primary Key
import javax.persistence.JoinColumn; // Foreign Key
import javax.persistence.ManyToOne; // Relación Muchos-a-Uno
import javax.persistence.OneToMany; // Relación Uno-a-Muchos
import javax.persistence.PersistenceContext; // Inyección del EntityManager JPA
import javax.persistence.Table; // Nombre de tabla SQL
import javax.sql.DataSource; // Pool de conexiones JDBC
import javax.transaction.Transactional; // Transacción declarativa ACID

import net.sf.jasperreports.engine.JasperCompileManager; // Compilador de .jrxml a .jasper
import net.sf.jasperreports.engine.JasperExportManager; // Exportador de JasperPrint a PDF (byte[])
import net.sf.jasperreports.engine.JasperFillManager; // Motor de relleno (Plantilla + $P + $F -> JasperPrint)
import net.sf.jasperreports.engine.JasperPrint; // Documento paginado en memoria
import net.sf.jasperreports.engine.JasperReport; // Plantilla compilada
import net.sf.jasperreports.engine.data.JRBeanCollectionDataSource; // Origen de datos basado en colección de Beans Java

/**
 * =============================================================================
 * FLUJO VERTICAL COMPLETO E INTEGRADO — PROYECTO AYUNTAMIENTO DE ROPERUELOS DEL PÁRAMO
 * =============================================================================
 * Caso estrella para defender en la entrevista técnica de Seresco (Valladolid):
 * "Búsqueda de expedientes y parcelas de un agricultor por NIF y Polígono Catastral
 *  y emisión en un clic del Certificado Oficial Municipal en PDF con Jasper Reports".
 *
 * Este archivo unifica en una sola vista de estudio las 5 capas que interactúan:
 *   [PASO 1] Entidad JPA y DTO de Parcela Rústica (Modelo de Datos).
 *   [PASO 2] Repositorio JPA (JPQL con JOIN FETCH) + JDBC (PreparedStatement).
 *   [PASO 3] Servicio Transaccional de Negocio (@Transactional + validación BigDecimal).
 *   [PASO 4] Servicio de Jasper Reports (Compilación + Parámetros $P + JRBeanCollectionDataSource + PDF).
 *   [PASO 5] Managed Bean JSF (@ViewScoped) + Equivalente Spring Boot REST Controller.
 */
public class flujo_completo_codigo_integrado {

    // =========================================================================
    // [PASO 1] MODELO DE DATOS: ENTIDAD JPA + DTO PARA JASPER REPORTS
    // =========================================================================

    @Entity
    @Table(name = "expedientes_municipales")
    public static class ExpedienteMunicipalEntity implements Serializable {
        private static final long serialVersionUID = 1L;

        @Id
        @GeneratedValue(strategy = GenerationType.IDENTITY)
        @Column(name = "id_expediente")
        private Long id;

        @Column(name = "codigo_expediente", nullable = false, unique = true, length = 30)
        private String codigoExpediente;

        @Column(name = "campania_agricola", nullable = false)
        private Integer campaniaAgricola;

        @Column(name = "estado_expediente", nullable = false, length = 30)
        private String estadoExpediente; // 'BORRADOR', 'EN_REVISION_TECNICA', 'APROBADO'

        @Column(name = "superficie_total_declarada_ha", nullable = false, precision = 10, scale = 4)
        private BigDecimal superficieTotalHa = BigDecimal.ZERO;

        @ManyToOne(fetch = FetchType.LAZY, optional = false) // LAZY siempre para evitar consultas ocultas
        @JoinColumn(name = "id_titular", nullable = false)
        private TitularEntity titular;

        @OneToMany(mappedBy = "expediente", fetch = FetchType.LAZY)
        private List<ParcelaRusticaEntity> parcelas = new ArrayList<>();

        public Long getId() { return id; }
        public String getCodigoExpediente() { return codigoExpediente; }
        public Integer getCampaniaAgricola() { return campaniaAgricola; }
        public String getEstadoExpediente() { return estadoExpediente; }
        public void setEstadoExpediente(String estadoExpediente) { this.estadoExpediente = estadoExpediente; }
        public BigDecimal getSuperficieTotalHa() { return superficieTotalHa; }
        public void setSuperficieTotalHa(BigDecimal superficieTotalHa) { this.superficieTotalHa = superficieTotalHa; }
        public TitularEntity getTitular() { return titular; }
        public List<ParcelaRusticaEntity> getParcelas() { return parcelas; }
    }

    @Entity
    @Table(name = "titulares")
    public static class TitularEntity implements Serializable {
        private static final long serialVersionUID = 1L;
        @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
        @Column(name = "id_titular")
        private Long id;
        @Column(name = "nif_cif", nullable = false, unique = true)
        private String nifCif;
        @Column(name = "nombre_completo", nullable = false)
        private String nombreCompleto;

        public Long getId() { return id; }
        public String getNifCif() { return nifCif; }
        public String getNombreCompleto() { return nombreCompleto; }
    }

    @Entity
    @Table(name = "parcelas_rusticas")
    public static class ParcelaRusticaEntity implements Serializable {
        private static final long serialVersionUID = 1L;
        @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
        @Column(name = "id_parcela")
        private Long id;
        @Column(name = "poligono", nullable = false)
        private Integer poligono;
        @Column(name = "parcela", nullable = false)
        private Integer parcela;
        @Column(name = "recinto_sigpac", nullable = false)
        private Integer recintoSigpac;
        @Column(name = "tipo_cultivo", nullable = false)
        private String tipoCultivo; // 'REGADIO' o 'SECANO'
        @Column(name = "superficie_ha", nullable = false, precision = 10, scale = 4)
        private BigDecimal superficieHa;
        @ManyToOne(fetch = FetchType.LAZY)
        @JoinColumn(name = "id_expediente")
        private ExpedienteMunicipalEntity expediente;

        public Integer getPoligono() { return poligono; }
        public Integer getParcela() { return parcela; }
        public Integer getRecintoSigpac() { return recintoSigpac; }
        public String getTipoCultivo() { return tipoCultivo; }
        public BigDecimal getSuperficieHa() { return superficieHa; }
    }

    /**
     * DTO cuyos getters coinciden exactamente con los campos <field name="...">
     * declarados en la plantilla informe_parcelas_titular.jrxml de Jasper Reports.
     */
    public static class FilaCertificadoJasperDTO implements Serializable {
        private static final long serialVersionUID = 1L;
        private final String codigoExpediente;
        private final String nifTitular;
        private final String nombreTitular;
        private final Integer poligono;
        private final Integer parcela;
        private final Integer recintoSigpac;
        private final String tipoCultivo;
        private final BigDecimal superficieHa;

        public FilaCertificadoJasperDTO(String codigoExpediente, String nifTitular, String nombreTitular,
                Integer poligono, Integer parcela, Integer recintoSigpac, String tipoCultivo, BigDecimal superficieHa) {
            this.codigoExpediente = codigoExpediente;
            this.nifTitular = nifTitular;
            this.nombreTitular = nombreTitular;
            this.poligono = poligono;
            this.parcela = parcela;
            this.recintoSigpac = recintoSigpac;
            this.tipoCultivo = tipoCultivo;
            this.superficieHa = superficieHa;
        }

        // Jasper Reports invoca estos getters por reflexión al iterar la banda <detail>
        public String getCodigoExpediente() { return codigoExpediente; }
        public String getNifTitular() { return nifTitular; }
        public String getNombreTitular() { return nombreTitular; }
        public Integer getPoligono() { return poligono; }
        public Integer getParcela() { return parcela; }
        public Integer getRecintoSigpac() { return recintoSigpac; }
        public String getTipoCultivo() { return tipoCultivo; }
        public BigDecimal getSuperficieHa() { return superficieHa; }
    }

    // =========================================================================
    // [PASO 2] CAPA DE REPOSITORIO: JPQL (JOIN FETCH) + JDBC (PreparedStatement)
    // =========================================================================

    @ApplicationScoped
    public static class RoperuelosAgrarioRepository {

        @PersistenceContext(unitName = "AgroRoperuelosPU")
        private EntityManager em;

        @Resource(lookup = "java:/jdbc/AgroRoperuelosDS")
        private DataSource dataSource;

        /**
         * Consulta JPQL optimizada con JOIN FETCH para buscar expedientes de un agricultor
         * por NIF y opcionalmente por Polígono rústico, trayendo Titular y Parcelas en 1 sola consulta SQL.
         */
        public List<ExpedienteMunicipalEntity> buscarExpedientesPorNifYPoligono(
                String nifAgricultor,
                Integer poligonoFiltro,
                Integer campania) {

            String jpql =
                "SELECT DISTINCT e " +
                "FROM flujo_completo_codigo_integrado$ExpedienteMunicipalEntity e " +
                "JOIN FETCH e.titular t " +
                "LEFT JOIN FETCH e.parcelas p " +
                "WHERE UPPER(t.nifCif) = :nif " +
                "  AND e.campaniaAgricola = :campania " +
                (poligonoFiltro != null ? " AND p.poligono = :poligono " : "") +
                "ORDER BY e.codigoExpediente DESC";

            var query = em.createQuery(jpql, ExpedienteMunicipalEntity.class)
                    .setParameter("nif", nifAgricultor.trim().toUpperCase())
                    .setParameter("campania", campania);

            if (poligonoFiltro != null) {
                query.setParameter("poligono", poligonoFiltro);
            }
            return query.getResultList();
        }

        /**
         * Consulta JDBC parametrizada (PreparedStatement + try-with-resources) para extraer
         * los recintos SIGPAC aprobados que se imprimirán en el Certificado PDF de Jasper Reports.
         */
        public List<FilaCertificadoJasperDTO> obtenerFilasParaJasperJdbc(
                Long idExpediente,
                Integer poligonoOpcional) throws Exception {

            String sql =
                "SELECT em.codigo_expediente, t.nif_cif, t.nombre_completo, " +
                "       pr.poligono, pr.parcela, pr.recinto_sigpac, pr.tipo_cultivo, " +
                "       ep.superficie_computada_ha AS superficie_ha " +
                "FROM expedientes_municipales em " +
                "INNER JOIN titulares t            ON t.id_titular = em.id_titular " +
                "INNER JOIN expediente_parcelas ep ON ep.id_expediente = em.id_expediente " +
                "INNER JOIN parcelas_rusticas pr   ON pr.id_parcela = ep.id_parcela " +
                "WHERE em.id_expediente = ? " +
                "  AND em.estado_expediente = 'APROBADO' " +
                (poligonoOpcional != null ? " AND pr.poligono = ? " : "") +
                "ORDER BY pr.poligono ASC, pr.parcela ASC, pr.recinto_sigpac ASC";

            List<FilaCertificadoJasperDTO> lista = new ArrayList<>();

            // try-with-resources: garantiza devolver la conexión al Pool aunque ocurra una SQLException
            try (Connection conn = dataSource.getConnection();
                 PreparedStatement ps = conn.prepareStatement(sql)) {

                ps.setLong(1, idExpediente);
                if (poligonoOpcional != null) {
                    ps.setInt(2, poligonoOpcional);
                }

                try (ResultSet rs = ps.executeQuery()) {
                    while (rs.next()) {
                        lista.add(new FilaCertificadoJasperDTO(
                            rs.getString("codigo_expediente"),
                            rs.getString("nif_cif"),
                            rs.getString("nombre_completo"),
                            rs.getInt("poligono"),
                            rs.getInt("parcela"),
                            rs.getInt("recinto_sigpac"),
                            rs.getString("tipo_cultivo"),
                            rs.getBigDecimal("superficie_ha")
                        ));
                    }
                }
            }
            return lista;
        }

        /**
         * Registra en la tabla de auditoría 'certificados_emitidos' cada vez que se genera un PDF oficial.
         */
        public void registrarAuditoriaCertificado(
                Long idExpediente, Long idTitular, String csvVerificacion, int numParcelas, BigDecimal totalHa) throws Exception {

            String sqlInsert =
                "INSERT INTO certificados_emitidos " +
                "(numero_registro_salida, id_expediente, id_titular, codigo_csv_verificacion, " +
                " usuario_emisor, total_parcelas_incluidas, total_hectareas_certif) " +
                "VALUES (?, ?, ?, ?, ?, ?, ?)";

            try (Connection conn = dataSource.getConnection();
                 PreparedStatement ps = conn.prepareStatement(sqlInsert)) {

                ps.setString(1, "CERT-ROP-" + LocalDate.now().getYear() + "-" + System.currentTimeMillis() % 100000);
                ps.setLong(2, idExpediente);
                ps.setLong(3, idTitular);
                ps.setString(4, csvVerificacion);
                ps.setString(5, "secretaria.roperuelos");
                ps.setInt(6, numParcelas);
                ps.setBigDecimal(7, totalHa.setScale(4, RoundingMode.HALF_UP));
                ps.executeUpdate();
            }
        }
    }

    // =========================================================================
    // [PASO 3 Y 4] SERVICIO TRANSACCIONAL + GENERACIÓN PDF CON JASPER REPORTS
    // =========================================================================

    @ApplicationScoped
    public static class RoperuelosCertificadoService {

        @Inject
        private RoperuelosAgrarioRepository repository;

        /**
         * Orquesta de forma transaccional:
         * 1) La consulta de parcelas del expediente en SQL.
         * 2) El cálculo de verificación con BigDecimal.
         * 3) El registro de auditoría del Certificado y su CSV en base de datos.
         * 4) El relleno y exportación del PDF con JasperFillManager y JasperExportManager.
         */
        @Transactional(rollbackOn = Exception.class)
        public byte[] emitirCertificadoOficialPdf(
                ExpedienteMunicipalEntity expediente,
                Integer poligonoOpcional) throws Exception {

            // 1. Validamos que el expediente esté APROBADO antes de permitir emitir certificado oficial
            if (!"APROBADO".equalsIgnoreCase(expediente.getEstadoExpediente())) {
                throw new IllegalStateException("Solo se pueden emitir certificados oficiales de expedientes en estado APROBADO.");
            }

            // 2. Obtenemos las filas validadas mediante JDBC PreparedStatement
            List<FilaCertificadoJasperDTO> filas = repository.obtenerFilasParaJasperJdbc(
                    expediente.getId(), poligonoOpcional);

            if (filas.isEmpty()) {
                throw new IllegalStateException("No existen parcelas aprobadas para incluir en el certificado.");
            }

            // 3. Sumamos las hectáreas en Java con BigDecimal para guardarlas en el registro de salida
            BigDecimal totalHectareas = filas.stream()
                    .map(FilaCertificadoJasperDTO::getSuperficieHa)
                    .reduce(BigDecimal.ZERO, BigDecimal::add)
                    .setScale(4, RoundingMode.HALF_UP);

            // 4. Generamos el Código Seguro de Verificación (CSV) y registramos la emisión en base de datos
            String codigoCsv = "CSV-24136-" + expediente.getCampaniaAgricola() + "-"
                    + UUID.randomUUID().toString().substring(0, 8).toUpperCase();

            repository.registrarAuditoriaCertificado(
                    expediente.getId(),
                    expediente.getTitular().getId(),
                    codigoCsv,
                    filas.size(),
                    totalHectareas
            );

            // 5. Preparamos los Parámetros ($P{...}) para la plantilla informe_parcelas_titular.jrxml
            Map<String, Object> parametrosJasper = new HashMap<>();
            parametrosJasper.put("ID_TITULAR", expediente.getTitular().getId());
            parametrosJasper.put("CAMPANIA_AGRICOLA", expediente.getCampaniaAgricola());
            parametrosJasper.put("CODIGO_EXPEDIENTE", expediente.getCodigoExpediente());
            parametrosJasper.put("NOMBRE_AYUNTAMIENTO", "EXCMO. AYUNTAMIENTO DE ROPERUELOS DEL PÁRAMO (LEÓN)");
            parametrosJasper.put("CODIGO_CSV", codigoCsv);

            // 6. Cargamos y compilamos la plantilla .jrxml y la rellenamos con JRBeanCollectionDataSource
            try (InputStream jrxmlStream = getClass().getResourceAsStream("/reports/informe_parcelas_titular.jrxml")) {
                JasperReport plantillaCompilada = JasperCompileManager.compileReport(jrxmlStream);
                JRBeanCollectionDataSource dataSourceBeans = new JRBeanCollectionDataSource(filas);

                JasperPrint jasperPrint = JasperFillManager.fillReport(
                        plantillaCompilada,
                        parametrosJasper,
                        dataSourceBeans
                );

                // 7. Exportamos a formato binario PDF (byte[])
                return JasperExportManager.exportReportToPdf(jasperPrint);
            }
        }
    }

    // =========================================================================
    // [PASO 5] MANAGED BEAN JSF (@ViewScoped) PARA LA PANTALLA WEB XHTML
    // =========================================================================

    @Named("flujoRoperuelosBean")
    @ViewScoped
    public static class FlujoRoperuelosManagedBean implements Serializable {
        private static final long serialVersionUID = 1L;

        @Inject
        private RoperuelosAgrarioRepository repository;

        @Inject
        private RoperuelosCertificadoService certificadoService;

        // Criterios de búsqueda enlazados a los <h:inputText> de la vista XHTML
        private String nifBusqueda;
        private Integer poligonoBusqueda;
        private Integer campaniaBusqueda;

        // Resultados mostrados en el <p:dataTable>
        private List<ExpedienteMunicipalEntity> expedientesEncontrados;

        @PostConstruct
        public void init() {
            this.campaniaBusqueda = 2024;
            this.expedientesEncontrados = new ArrayList<>();
        }

        /**
         * Acción AJAX del botón "Buscar Agricultor / Polígono".
         */
        public void buscarPorNifYPoligono() {
            this.expedientesEncontrados = repository.buscarExpedientesPorNifYPoligono(
                    this.nifBusqueda, this.poligonoBusqueda, this.campaniaBusqueda);
        }

        /**
         * Acción no-AJAX (ajax="false") del botón "Emitir Certificado Oficial PDF (Jasper Reports)".
         */
        public void emitirYDescargarPdf(ExpedienteMunicipalEntity expedienteFila) {
            FacesContext fc = FacesContext.getCurrentInstance();
            ExternalContext ec = fc.getExternalContext();

            try {
                // Llama al servicio transaccional + Jasper Reports
                byte[] pdfBytes = certificadoService.emitirCertificadoOficialPdf(
                        expedienteFila, this.poligonoBusqueda);

                String nombrePdf = "Certificado_Roperuelos_" + expedienteFila.getCodigoExpediente() + ".pdf";

                // Configura las cabeceras HTTP para descarga limpia en el navegador
                ec.responseReset();
                ec.setResponseContentType("application/pdf");
                ec.setResponseContentLength(pdfBytes.length);
                ec.setResponseHeader("Content-Disposition", "attachment; filename=\"" + nombrePdf + "\"");

                try (OutputStream out = ec.getResponseOutputStream()) {
                    out.write(pdfBytes);
                    out.flush();
                }

                // Detiene el ciclo de vida JSF en Fase 5 para no renderizar HTML sobre el stream del PDF
                fc.responseComplete();

            } catch (Exception e) {
                fc.addMessage(null, new FacesMessage(
                        FacesMessage.SEVERITY_ERROR,
                        "No se pudo emitir el Certificado PDF",
                        e.getMessage()));
            }
        }

        public String getNifBusqueda() { return nifBusqueda; }
        public void setNifBusqueda(String nifBusqueda) { this.nifBusqueda = nifBusqueda; }
        public Integer getPoligonoBusqueda() { return poligonoBusqueda; }
        public void setPoligonoBusqueda(Integer poligonoBusqueda) { this.poligonoBusqueda = poligonoBusqueda; }
        public Integer getCampaniaBusqueda() { return campaniaBusqueda; }
        public void setCampaniaBusqueda(Integer campaniaBusqueda) { this.campaniaBusqueda = campaniaBusqueda; }
        public List<ExpedienteMunicipalEntity> getExpedientesEncontrados() { return expedientesEncontrados; }
    }
}
```

---
## ARCHIVO: posibles_repreguntas_del_tribunal_seresco.md

# 15 POSIBLES REPREGUNTAS DEL TRIBUNAL TÉCNICO DE SERESCO SOBRE MI PROYECTO EN EL AYUNTAMIENTO DE ROPERUELOS DEL PÁRAMO

> **Objetivo de este documento:** Cuando en la entrevista de Seresco Valladolid cuentes tu experiencia en el **Ayuntamiento de Roperuelos del Páramo**, un Arquitecto Java/JEE o Jefe de Proyecto de su área agroalimentaria te hará repreguntas concretas para comprobar que **de verdad hiciste el proyecto** y conoces los detalles del día a día. Aquí tienes las **15 repreguntas de profundización** con respuestas en primera persona naturales, honestas y técnicamente impecables.

---

### 1. «¿Qué volumen real de datos manejabais en la base de datos del Ayuntamiento de Roperuelos del Páramo?»
> **Respuesta en primera persona:**  
> *"Aunque Roperuelos del Páramo tiene unos 500 habitantes empadronados, al ser un municipio agrícola de la comarca del Páramo con tres núcleos (Roperuelos, Moscas del Páramo y Valcabado del Páramo) y mucha fragmentación parcelaria, el padrón rústico era bastante más grande que el padrón de habitantes: manejábamos unos **1.250 titulares catastrales** (incluyendo propietarios no residentes, herencias y SATs), alrededor de **4.800 parcelas y recintos rústicos SIGPAC** repartidos en unos 18 polígonos, y entre **600 y 900 expedientes y certificados al año** acumulados por campañas."*

---

### 2. «¿Por qué estuviste en dos etapas separadas (verano de 2023 y verano/otoño de 2024)? ¿Qué hiciste en cada una?»
> **Respuesta en primera persona:**  
> *"La primera etapa (de junio a septiembre de 2023, 4 meses) coincidió con el periodo estival mientras cursaba DAM. En esa primera fase el objetivo fue quitar las hojas de Excel desconectadas: diseñé el modelo de base de datos relacional en SQL, construí el backend Java con JPA/Hibernate y JDBC y levanté las pantallas web de alta y consulta de titulares, parcelas y expedientes.*  
> *Quedaron tan contentos con el resultado que al año siguiente (de junio a octubre de 2024, 5 meses) me volvieron a contratar para una segunda fase evolutiva: ahí fue donde implementé todo el módulo de generación automática de certificados y listados en PDF y Excel con **Jasper Reports**, añadí nuevos servicios en **Spring Boot** y creé una utilidad en **Python** para importar y limpiar automáticamente los ficheros CSV de actualización catastral."*

---

### 3. «En el Páramo hay grandes explotaciones de regadío. ¿Qué pasaba en tu plantilla `.jrxml` de Jasper Reports cuando un agricultor o una SAT tenía 40 o 60 parcelas y no cabían en un solo folio A4?»
> **Respuesta en primera persona:**  
> *"Ese fue precisamente uno de los casos que tuve que afinar en **Jaspersoft Studio**. Al principio, con agricultores de 3 o 4 parcelas todo cabía en una página, pero con titulares grandes o SATs de regadío de maíz y remolacha que tenían 40 o 50 recintos, el listado ocupaba 2 o 3 páginas.*  
> *Lo resolví estructurando bien las bandas del `.jrxml`:*
> - *Puse el membrete largo y el texto legal introductorio en la banda **`<title>`** para que solo saliera en la primera hoja.*
> - *En **`<pageHeader>`** y **`<columnHeader>`** coloqué el número de expediente, el NIF y las cabeceras de la tabla (*Polígono, Parcela, Recinto, Cultivo, Superficie*) para que se repitieran automáticamente al principio de las páginas 2 y 3.*
> - *En la banda **`<detail>`** configuré `splitType="Prevent"` para que ninguna fila de parcela quedara partida por la mitad en un salto de página.*
> - *En **`<pageFooter>`** puse la numeración `'Página X de Y'` combinando `evaluationTime="Now"` y `evaluationTime="Report"` junto con el código CSV.*
> - *Y el total general de hectáreas (`$V{TOTAL_HECTAREAS_TITULAR}`) y el bloque de firma del Secretario los coloqué en la banda **`<summary>`**, asegurando que solo aparecieran al final del todo."*

---

### 4. «¿Cómo pasabas los datos desde Java al informe de Jasper Reports: con una conexión JDBC directa o con `JRBeanCollectionDataSource`?»
> **Respuesta en primera persona:**  
> *"Utilicé ambos enfoques según el tipo de informe:*
> - *Para los **listados generales de padrón por polígono o campaña**, que eran consultas SQL puras sobre una vista (`v_certificado_parcelas_titular`), pasaba directamente una `Connection` obtenida del Pool `DataSource` dentro de un bloque `try-with-resources` a `JasperFillManager.fillReport(reporte, parametros, conexion)`, porque así el propio `.jrxml` ejecutaba su `<queryString>` parametrizado.*
> - *En cambio, para el **Certificado Oficial Individual de un Expediente**, preferí usar **`JRBeanCollectionDataSource`** alimentado por una lista de DTOs (`FilaCertificadoJasperDTO`): primero validaba en el servicio Java que el expediente estuviera en estado `APROBADO`, calculaba y auditaba el código CSV en la tabla `certificados_emitidos`, y le pasaba la colección ya validada a Jasper Reports."*

---

### 5. «¿Compilabas el archivo `.jrxml` cada vez que el administrativo pulsaba el botón de descargar PDF?»
> **Respuesta en primera persona:**  
> *"Al principio en entorno de desarrollo sí llamaba a `JasperCompileManager.compileReport(...)` en cada petición, pero enseguida vi que compilar el XML tardaba casi un segundo y consumía CPU innecesariamente. Lo optimicé de dos formas: precompilando las plantillas a ficheros binarios **`.jasper`** y guardando el objeto `JasperReport` cargado en memoria dentro de un **`ConcurrentHashMap`** en el servicio `@ApplicationScoped`. Así la compilación ocurre una sola vez y cada descarga de PDF tarda apenas 40 o 50 milisegundos."*

---

### 6. «¿Con qué problema te encontraste al descargar el PDF de Jasper Reports desde un botón de JSF / PrimeFaces?»
> **Respuesta en primera persona:**  
> *"Me encontré con el clásico problema de que en PrimeFaces los `<p:commandButton>` hacen peticiones AJAX por defecto (`ajax="true"`). Cuando intentas devolver un flujo binario `application/pdf` por el `HttpServletResponse` dentro de una llamada AJAX, el motor JavaScript de JSF espera un XML `<partial-response>` y la descarga no se abre en el navegador.*  
> *Además, en el servidor, si no avisas a JSF de que ya has escrito la respuesta HTTP, al terminar la Fase 5 (*Invoke Application*) intenta ejecutar la Fase 6 (*Render Response*) y lanza un `IllegalStateException: Cannot call sendError() after the response has been committed`. Lo solucioné poniendo **`ajax="false"`** en el botón de descarga PDF, haciendo `externalContext.responseReset()`, configurando las cabeceras `Content-Type: application/pdf` y `Content-Disposition: attachment`, volcando los bytes al `OutputStream` y llamando al final a **`facesContext.responseComplete()`**."*

---

### 7. «¿Cómo probabas y optimizabas las consultas SQL antes de meterlas en el repositorio Java o en Jaspersoft Studio?»
> **Respuesta en primera persona:**  
> *"Primero escribía y probaba la consulta directamente contra PostgreSQL/MySQL en el cliente SQL (DBeaver / pgAdmin) con juegos de datos de prueba que incluían casos borde: titulares sin parcelas, parcelas con varios recintos SIGPAC, expedientes en borrador y expedientes aprobados.*  
> *Luego ejecutaba **`EXPLAIN ANALYZE`** sobre las consultas de filtrado y de agregación para comprobar que el motor utilizaba búsqueda por índice (*Index Scan*) sobre `id_titular`, `(campania_agricola, estado_expediente)` y `(poligono, tipo_cultivo)` en lugar de hacer barridos secuenciales (*Seq Scan*). Una vez afinada la query, si iba para un informe complejo creaba una **Vista SQL (`v_certificado_parcelas_titular`)** para mantener limpio el `.jrxml`."*

---

### 8. «¿Cómo modelaste en la base de datos la relación entre Titulares, Parcelas Rústicas y Expedientes?»
> **Respuesta en primera persona:**  
> *"Separé claramente el **inventario catastral permanente** de la **tramitación anual por campañas**:*
> - *Por un lado estaban `titulares` (1) y `parcelas_rusticas` (N), donde cada recinto tenía una restricción `UNIQUE (codigo_provincia, codigo_municipio, poligono, parcela, recinto_sigpac)`.*
> - *Por otro lado estaba `expedientes_municipales` (cabecera del trámite en una campaña concreta, ej. 2024).*
> - *Y como un expediente puede incluir varias parcelas de un titular, y una misma parcela pasa por distintos expedientes a lo largo de los años (2023, 2024...), creé la tabla intermedia **`expediente_parcelas`** con clave única `(id_expediente, id_parcela)` que guarda además la superficie computada y el cultivo declarado en esa campaña específica."*

---

### 9. «¿Por qué usaste `BigDecimal` y `NUMERIC(10,4)` para las superficies de las parcelas en lugar de `Double`?»
> **Respuesta en primera persona:**  
> *"Porque en gestión catastral y SIGPAC la unidad estándar es la hectárea con **4 decimales**, ya que `0,0001 ha` equivale exactamente a 1 centiárea ($1\text{ m}^2$). En las pruebas iniciales vi que al sumar 30 o 40 parcelas con `double`, la coma flotante binaria introducía residuos como `10.455000000000002`, y a veces el total impreso en el pie del certificado difería en una diezmilésima de la suma visual de la columna. Cambiando todas las columnas SQL a `NUMERIC(10,4)` y todos los atributos en Java y en Jasper Reports a `java.math.BigDecimal` con `RoundingMode.HALF_UP`, el cuadre contable y superficial pasó a ser exacto al 100%."*

---

### 10. «¿Qué pasaba si dos administrativos del Ayuntamiento abrían a la vez el mismo expediente para editarlo?»
> **Respuesta en primera persona:**  
> *"Para evitar el problema de las actualizaciones perdidas (*Lost Updates*) sin bloquear registros en base de datos mientras un administrativo dejaba la pantalla abierta, implementé **bloqueo optimista (*Optimistic Locking*)** de JPA añadiendo el campo `@Version private Long version;` en la entidad `ExpedienteAgrarioEntity`.*  
> *De esa forma, cuando el primer administrativo guarda, Hibernate incrementa `version` de 0 a 1. Si el segundo administrativo intenta guardar sobre la versión 0 que tenía en su `@ViewScoped`, Hibernate detecta que la fila ya cambió, lanza `OptimisticLockException`, la capturamos en el Bean y le mostramos un `FacesMessage` avisándole de que otro usuario acaba de actualizar el expediente para que refresque los datos."*

---

### 11. «En tu CV mencionas que también usaste Python en el Ayuntamiento. ¿Para qué usabas Python y para qué Java?»
> **Respuesta en primera persona:**  
> *"El núcleo de la aplicación web, la lógica de negocio de expedientes, las vistas JSF y la generación de certificados con Jasper Reports estaban íntegramente en **Java y SQL**. Utilicé **Python** para construir un servicio/utilidad de ingesta y limpieza de datos catastrales: cuando llegaban volcados de datos externos en ficheros CSV o Excel antiguos de las Juntas Vecinales, venían con errores de codificación de tildes, espacios duplicados, NIFs sin ceros a la izquierda o decimales con coma en vez de punto. Con Python normalizaba y validaba esos ficheros en segundos antes de volcarlos de forma limpia a PostgreSQL."*

---

### 12. «¿Cómo gestionabas la seguridad, las sesiones y los permisos de quién podía aprobar un expediente o emitir un certificado?»
> **Respuesta en primera persona:**  
> *"Manejábamos autenticación con sesión HTTP y control basado en roles (RBAC) con dos perfiles principales en el Ayuntamiento:*
> - *El perfil **`ADMINISTRATIVO_TRAMITADOR`**, que podía dar de alta titulares, registrar expedientes en estado `BORRADOR` o `EN_REVISION_TECNICA`, asociar recintos rústicos y consultar el padrón.*
> - *Y el perfil **`SECRETARIA_INTERVENCION`**, que era el único autorizado para ejecutar la acción de pasar un expediente a estado `APROBADO` o `DENEGADO`. Además, en la vista XHTML el botón de descargar el Certificado Oficial PDF tenía la condición `rendered="#{exp.estado eq 'APROBADO'}"` y en la capa de servicio Java volvíamos a validar el estado y el rol antes de invocar a Jasper Reports, registrando en la tabla `certificados_emitidos` el login del usuario emisor."*

---

### 13. «¿Tuviste algún caso de `LazyInitializationException` o de lentitud por `N+1 queries` en la bandeja de expedientes?»
> **Respuesta en primera persona:**  
> *"Sí, me ocurrió al principio cuando configuré la relación `@ManyToOne` entre `Expediente` y `Titular` como `FetchType.LAZY`: al pintar el `<p:dataTable>` en JSF, cada fila llamaba a `#{exp.titular.nombreCompleto}` cuando la transacción del servicio ya había terminado, lanzando `LazyInitializationException` (o si la dejaba abierta, lanzando una query extra por cada fila de la tabla).*  
> *Lo solucioné escribiendo en el repositorio la consulta JPQL con **`JOIN FETCH e.titular t`**: así las relaciones siguen siendo `LAZY` por defecto en la entidad, pero cuando cargo la bandeja para JSF traigo los expedientes y sus titulares en un único `SELECT` con `INNER JOIN`."*

---

### 14. «¿Cómo desplegabas la aplicación y cómo gestionabas la configuración entre tu equipo de desarrollo y el servidor del Ayuntamiento?»
> **Respuesta en primera persona:**  
> *"Empaquetábamos la aplicación con **Maven** (`pom.xml`), separando los parámetros sensibles (URL JDBC de PostgreSQL/MySQL, credenciales, pool de conexiones y rutas) en perfiles/propiedades externas al código fuente y manteniendo todo versionado en **Git**.*  
> *Probaba primero cada cambio en mi entorno local de desarrollo (**DEV**) con una base de datos de pruebas, validaba la generación de los PDFs y los planes de ejecución SQL en preproducción (**QAS**) y, una vez verificado con el personal del Ayuntamiento, realizaba el despliegue ordenado a producción (**PRD**) haciendo backup previo de la base de datos —una disciplina que luego perfeccioné aún más en mi etapa en FDS (DXC Technology)."*

---

### 15. «Si te incorporas a Seresco en Valladolid en un proyecto grande de gestión agraria (tipo PAC / SIGPAC / ITACyL), ¿qué diferencia esperarías respecto a lo que hiciste en el Ayuntamiento y cómo te adaptarías?»
> **Respuesta en primera persona:**  
> *"La gran ventaja es que tanto el **dominio funcional** (titulares, polígonos, parcelas, recintos SIGPAC, secano/regadío, campañas anuales, estados de expediente y certificados oficiales) como el **stack tecnológico** (`Java / JEE`, `SQL`, `JSF` y `Jasper Reports`) son exactamente los mismos que ya he trabajado.*  
> *La diferencia principal en Seresco será la **escala y la arquitectura corporativa**: pasar de los ~5.000 recintos de un municipio a millones de recintos de toda una comunidad autónoma, trabajar con estándares estrictos de arquitectura JEE corporativa, integraciones con servicios web oficiales y un equipo grande de producción de software. Precisamente por haber combinado la experiencia del Ayuntamiento con el rigor de consultoría en **FDS (DXC Technology)** y el manejo de grandes volúmenes de datos SQL en **HORSE Technologies**, puedo adaptarme y ser productivo desde las primeras semanas."*

