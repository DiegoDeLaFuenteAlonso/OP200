# 04 — FLUJO COMPLETO DE JASPER REPORTS, ARQUITECTURA `.JRXML` Y 15 PREGUNTAS DE ENTREVISTA

> **Objetivo de este documento:** Dominar al 100% **Jasper Reports (`net.sf.jasperreports`)** y **Jaspersoft Studio**, requisito explícito de la vacante de **Seresco Valladolid** y herramienta con la que desarrollaste los módulos de certificados y listados en el **Ayuntamiento de Roperuelos del Páramo**.

---

## 1. FLUJO DE ARQUITECTURA DE PRINCIPIO A FIN EN JASPER REPORTS

Cuando en la entrevista de Seresco te pregunten *«Explícanos cómo trabajas con Jasper Reports desde el diseño hasta que el usuario descarga el PDF»*, descríbelo en **4 pasos claros**:

```text
[1. DISEÑO (.jrxml)]           [2. COMPILACIÓN (.jasper)]        [3. RELLENO (.jrprint)]             [4. EXPORTACIÓN (PDF/XLSX)]
Jaspersoft Studio (Eclipse) -> JasperCompileManager           -> JasperFillManager.fillReport()   -> JasperExportManager
Fichero XML legible en Git     Bytecode serializado (JasperReport) Cruza Plantilla + Map<$P> + Datos  Genera byte[] application/pdf
                               (Se compila en el build Maven      (vía JDBC Connection o             y lo envía por HttpServletResponse
                                o se cachea en memoria al inicio)  JRBeanCollectionDataSource)
```

1. **Fase 1 — Diseño visual (`.jrxml`):**
   - Diseñamos la plantilla en **Jaspersoft Studio** (o iReport en proyectos antiguos), lo que genera un archivo XML estándar con extensión **`.jrxml`** que versionamos en Git dentro de `src/main/resources/reports/`.
2. **Fase 2 — Compilación (`.jrxml` → `.jasper`):**
   - El XML se compila a un fichero binario serializado **`.jasper`** (que representa un objeto `JasperReport` en Java) mediante `JasperCompileManager.compileReport(...)` o precompilándolo en tiempo de construcción con el plugin de Maven (`jasperreports-maven-plugin`) para ahorrar CPU en Producción.
3. **Fase 3 — Relleno de datos (`fillReport` → `JasperPrint`):**
   - En nuestro servicio Java (`JasperReportGeneratorService`), invocamos **`JasperFillManager.fillReport(jasperReport, mapaParametros, origenDatos)`**, que inyecta el `Map<String, Object>` de parámetros (`$P{}`) y recorre las filas devueltas por la base de datos o colección de Beans (`$F{}`), calculando las variables (`$V{}`) y devolviendo un documento paginado en memoria llamado **`JasperPrint`**.
4. **Fase 4 — Exportación (`exportReportToPdf` → `byte[]` / `OutputStream`):**
   - Con **`JasperExportManager.exportReportToPdf(jasperPrint)`** convertimos el documento en un array de bytes PDF (`application/pdf`) que devolvemos al navegador desde el Managed Bean de JSF o controlador Spring.

---

## 2. ESTRUCTURA INTERNA DE UN FICHERO `.JRXML`: LAS BANDAS (*BANDS*)

Un informe `.jrxml` divide verticalmente la página en **bandas**, cada una con un comportamiento específico respecto a la paginación:

| Banda del `.jrxml` | Cuándo se imprime | Uso real en el Certificado Catastral del Ayuntamiento / PAC |
| :--- | :--- | :--- |
| **`<background>`** | Detrás de todas las bandas en todas las páginas. | Marca de agua institucional (escudo difuminado o texto *"BORRADOR SIN VALIDEZ OFICIAL"*). |
| **`<title>`** | **Una sola vez al principio de la página 1** (no se repite en la página 2). | Escudo oficial del Ayuntamiento de Roperuelos del Páramo, título del Certificado, datos del Secretario y bloque identificativo del Titular agrario. |
| **`<pageHeader>`** | En la parte superior de **todas las páginas** (1, 2, 3...). | Código de expediente (`$P{CODIGO_EXPEDIENTE}`), NIF del titular y fecha de emisión para que las hojas sueltas nunca queden sin identificar. |
| **`<columnHeader>`** | Justo encima de la tabla de detalle al inicio de **cada página** que contenga filas. | Cabecera de las columnas de la tabla: *Polígono \| Parcela \| Recinto SIGPAC \| Sistema \| Expediente \| Superficie (ha)*. |
| **`<detail>`** | **Se repite una vez por cada fila ($N$ veces)** devuelta por la consulta SQL o por el `JRBeanCollectionDataSource`. | Imprime una fila por cada parcela rústica del agricultor (`$F{poligono}`, `$F{parcela}`, `$F{superficieHa}`). Si hay 45 parcelas, hace salto de página automático al llenarse el folio A4. |
| **`<columnFooter>`** | Al final de la tabla de columnas en cada página. | Subtotal de hectáreas acumuladas en la página actual. |
| **`<pageFooter>`** | En el borde inferior de **todas las páginas**. | Código Seguro de Verificación (`$P{CODIGO_CSV}`) y numeración *"Página X de Y"* combinando evaluationTime `Now` y `Report`. |
| **`<lastPageFooter>`** | Sustituye al `<pageFooter>` únicamente en la **última página**. | Recuadro de firma electrónica del Secretario y del Alcalde-Presidente con sello oficial. |
| **`<summary>`** | **Una sola vez al final del informe** (después de la última fila de `<detail>`). | Cuadro resumen final: **Total de Parcelas Computadas** (`$V{TOTAL_PARCELAS_CERTIFICADAS}`) y **Superficie Total Certificada en Hectáreas** (`$V{TOTAL_HECTAREAS_TITULAR}`). |
| **`<noData>`** | Se muestra cuando la consulta devuelve 0 filas (configurando `whenNoDataType="NoDataSection"`). | Mensaje controlado indicando que el titular no registra parcelas activas en esa campaña. |

---

## 3. DIFERENCIA EXACTA ENTRE PARÁMETROS (`$P{}`), CAMPOS (`$F{}`) Y VARIABLES (`$V{}`)

1. **Parámetros — `$P{NOMBRE_PARAMETRO}` (y `$P!{...}`):**
   - Valores de entrada que pasamos **desde nuestro código Java** dentro del diccionario `Map<String, Object> params = new HashMap<>()` antes de ejecutar el reporte.
   - Sirven para filtrar la consulta SQL interna (`WHERE id_titular = $P{ID_TITULAR}`) y para inyectar metadatos globales (`$P{NOMBRE_AYUNTAMIENTO}`, `$P{CODIGO_CSV}`, `$P{LOGO_STREAM}`).
   - **Diferencia entre `$P{...}` y `$P!{...}`:** `$P{ID_TITULAR}` se convierte en un parámetro seguro `?` de `PreparedStatement`, mientras que `$P!{...}` sustituye texto literal en la query antes de ejecutarla.
2. **Campos (*Fields*) — `$F{nombreCampo}`:**
   - Representan cada una de las **columnas de la fila actual** devuelta por el `ResultSet` SQL o cada propiedad `getNombreCampo()` del objeto Java dentro de un `JRBeanCollectionDataSource`.
3. **Variables — `$V{NOMBRE_VARIABLE}`:**
   - Cálculos dinámicos internos que Jasper Reports evalúa al recorrer el `<detail>`: sumatorios (`calculation="Sum"` sobre `$F{superficieHa}`), contadores (`Count`), subtotales por grupo o variables del motor como `$V{PAGE_NUMBER}` y `$V{REPORT_COUNT}`.

---

## 4. LAS DOS FORMAS DE PASAR DATOS A JASPER REPORTS: `Connection` JDBC vs. `JRBeanCollectionDataSource`

| Característica | Opción A: Pasar `java.sql.Connection` directa | Opción B: Pasar `JRBeanCollectionDataSource` (Lista de DTOs Java) |
| :--- | :--- | :--- |
| **Dónde está la consulta SQL** | Dentro de la etiqueta `<queryString>` del propio fichero `.jrxml`. | En el Repositorio/DAO Java (JPA, JPQL o JDBC `PreparedStatement`). |
| **Ventaja principal** | Muy rápido para informes tabulares y permite probar la query directamente desde el botón *Preview* de Jaspersoft Studio. | Permite aplicar validaciones de negocio complejas en Java antes de pintar el PDF, auditar la emisión y hacer tests unitarios sin BD. |
| **Precaución crítica** | **Obligatorio** obtener la `Connection` del `DataSource` dentro de un bloque **`try-with-resources`** para que regrese al pool nada más terminar `fillReport()`. | No cargar listas gigantes en memoria de golpe (para informes masivos por lotes usar `JRFileVirtualizer`). |

---

## 5. LAS 15 PREGUNTAS TÉCNICAS DE ENTREVISTA SOBRE JASPER REPORTS (CON RESPUESTAS LISTAS PARA DECIR EN VOZ ALTA)

1. **¿Cuál es la diferencia entre un archivo `.jrxml`, un `.jasper` y un `.jrprint`?**
   > "El **`.jrxml`** es el código fuente XML del diseño del informe creado en Jaspersoft Studio; el **`.jasper`** es la plantilla ya compilada a bytecode binario (`JasperReport`); y el **`.jrprint`** (`JasperPrint`) es el documento ya rellenado con datos y paginado en memoria, listo para exportarse a PDF o Excel."
2. **¿Qué diferencia hay entre `$P{}`, `$F{}` y `$V{}` en Jasper Reports?**
   > "`$P{}` son los **Parámetros** que pasamos desde Java en un `Map<String, Object>` (como filtros de la query, título o logo); `$F{}` son los **Campos** de cada fila del `ResultSet` o DTO Java (`poligono`, `parcela`, `superficieHa`); y `$V{}` son las **Variables** calculadas por el motor durante la ejecución (como la suma total de hectáreas o `$V{PAGE_NUMBER}`)."
3. **¿Cómo haces en Jasper Reports el pie de página *"Página 1 de 5"* si ambas cajas leen `$V{PAGE_NUMBER}`?**
   > "Colocando dos `<textField>` con `$V{PAGE_NUMBER}` en la banda `<pageFooter>`: el primero con **`evaluationTime="Now"`** (imprime el número de la página actual) y el segundo con **`evaluationTime="Report"`** (espera a que termine todo el informe para imprimir el número total de páginas)."
4. **¿Qué pasa si un texto en la banda `<detail>` es más largo que el ancho de su celda y cómo evitas que se corte?**
   > "Activo la propiedad **`textAdjust="StretchHeight"`** (antes `isStretchWithOverflow="true"`) en el `<textField>` para que la caja crezca verticalmente hacia abajo, y configuro el resto de celdas de la fila con `stretchType="ElementGroupHeight"` para que todos los bordes de la fila estiren al unísono."
5. **¿Cómo evitas que aparezca la palabra literal `"null"` en el PDF cuando un campo de base de datos viene vacío?**
   > "Activando la propiedad **`isBlankWhenNull="true"`** en el elemento `<textField>` del `.jrxml` (o usando `COALESCE` en SQL / operadores ternarios en la expresión)."
6. **¿Cómo pasas el escudo del Ayuntamiento o una imagen dinámica al informe sin usar rutas absolutas `C:\...` que se rompen al desplegar en un servidor Linux?**
   > "Nunca uso rutas del sistema de ficheros local. Cargo la imagen desde el *classpath* en Java con `getClass().getResourceAsStream("/reports/img/escudo_roperuelos.png")` y la inyecto en el mapa de parámetros como un `java.io.InputStream` (`$P{LOGO_STREAM}`)."
7. **¿Cómo funcionan los Grupos (`<group>`) en Jasper Reports (por ejemplo, agrupar las parcelas de un informe por Polígono o por Secano/Regadío)?**
   > "Primero ordeno la consulta SQL por la columna de agrupación (`ORDER BY tipo_cultivo, poligono`). Luego defino en el `.jrxml` un `<group name="GrupoPoligono">` con `<groupExpression><![CDATA[$F{poligono}]]></groupExpression>`. Esto habilita las bandas `<groupHeader>` y `<groupFooter>`, y permite crear variables con `resetType="Group"` y `resetGroup="GrupoPoligono"` que calculan automáticamente el subtotal de hectáreas de cada polígono."
8. **¿Qué son los Subreportes (`<subreport>`) y cómo se comunican con el informe maestro?**
   > "Permiten anidar un informe `.jasper` secundario dentro de otro principal (por ejemplo, mostrar en un mismo certificado la tabla de parcelas rústicas y debajo otra tabla con las liquidaciones de tasas). El informe maestro le pasa al `<subreport>` los parámetros de enlace (`<subreportParameter name="ID_EXPEDIENTE">`) y bien la misma conexión `$P{REPORT_CONNECTION}` o una sub-colección `new JRBeanCollectionDataSource($F{subLista})`."
9. **¿Para qué sirve la propiedad `Print When Expression` (`<printWhenExpression>`)?**
   > "Es una expresión booleana que decide dinámicamente si un elemento o una banda entera debe imprimirse o no. Por ejemplo, la usé para mostrar un bloque de advertencia legal únicamente cuando el expediente incluía parcelas en régimen de `'CESION_COMUNAL'`."
10. **¿Qué ocurre si la consulta SQL de un informe devuelve 0 filas y el PDF sale completamente en blanco?**
    > "Por defecto `whenNoDataType` vale `NoPages` y genera un PDF vacío. Para solucionarlo configuro en la etiqueta raíz `<jasperReport>` el atributo **`whenNoDataType="AllSectionsNoDetail"`** (para que pinte la cabecera oficial aunque no haya filas) o **`whenNoDataType="NoDataSection"`** definiendo la banda `<noData>` con un texto explicativo."
11. **¿Cómo exportas el mismo informe tanto a PDF como a Excel (`.xlsx`) sin diseñar dos plantillas distintas?**
    > "El paso de compilación y de relleno (`JasperFillManager.fillReport(...)`) es exactamente el mismo y devuelve el objeto `JasperPrint`. Para PDF llamo a `JasperExportManager.exportReportToPdf(jasperPrint)`, y para Excel uso la clase **`JRXlsxExporter`** activando `setDetectCellType(true)` (para que Excel reconozca las hectáreas e importes como números sumables y no como texto) y `setRemoveEmptySpaceBetweenRows(true)`."
12. **¿Por qué en un entorno de producción en Linux a veces las negritas (`isBold="true"`) o tildes no se ven en el PDF exportado y cómo se soluciona?**
    > "Porque la librería de generación PDF (iText / OpenPDF) necesita tener empotradas las fuentes TrueType (`.ttf`). Si usas una fuente de Windows como `Calibri` o `Arial` que no está instalada en el contenedor Linux, no renderiza la negrita. Se soluciona usando **JasperReports Font Extensions** (`jasperreports-fonts` con DejaVu Sans) empaquetadas en un `.jar` dentro del classpath con `isPdfEmbedded="true"`."
13. **¿Cómo evitas un `OutOfMemoryError` en el servidor Java si un usuario solicita un listado de Jasper Reports de 200.000 páginas?**
    > "Inyectando en el mapa de parámetros el parámetro estándar **`JRParameter.REPORT_VIRTUALIZER`** con una instancia de **`JRFileVirtualizer`** (o `JRSwapFileVirtualizer`). Así Jasper Reports mantiene en memoria RAM solo un número máximo de páginas (ej. 100 páginas) y vuelca el resto temporalmente a disco duro mientras genera el informe."
14. **¿Cómo entregas el PDF generado por Jasper Reports si el proyecto usa un controlador REST de Spring Boot en lugar de JSF?**
    > "En un `@RestController` de Spring Boot devuelvo un `ResponseEntity<byte[]>` con las cabeceras `HttpHeaders.CONTENT_TYPE` a `MediaType.APPLICATION_PDF_VALUE` y `HttpHeaders.CONTENT_DISPOSITION` a `ContentDisposition.attachment().filename("Certificado.pdf").build()`, pasando en el `.body(pdfBytes)` el array devuelto por `JasperExportManager.exportReportToPdf(...)`."
15. **¿Por qué es importante cachear el objeto `JasperReport` o precompilar los `.jasper` con Maven?**
    > "Porque `JasperCompileManager.compileReport(...)` parsea el XML y compila internamente las expresiones Java/Groovy del reporte, siendo la operación más pesada en CPU. Precompilando a `.jasper` en el `pom.xml` y manteniendo un `ConcurrentHashMap<String, JasperReport>` en el servicio `@ApplicationScoped`, eliminamos ese coste en tiempo de ejecución."
