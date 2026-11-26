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
