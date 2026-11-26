# FUENTE 05 — JASPER REPORTS, PLANTILLA JRXML Y SERVICIO GENERADOR PDF/EXCEL

---
## ARCHIVO: 04_flujo_jrxml_y_preguntas_jasper.md

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

---
## ARCHIVO: informe_parcelas_titular.jrxml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!--
  ARCHIVO: informe_parcelas_titular.jrxml
  DOCUMENTO OFICIAL: Certificado Municipal de Parcelas Rústicas y Explotación Agraria
  ENTIDAD: Ayuntamiento de Roperuelos del Páramo (León)
  HERRAMIENTA: Jaspersoft Studio / JasperReports 6.x
  AUTOR: Diego de la Fuente Alonso
-->
<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports"
              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
              xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd"
              name="Certificado_Parcelas_Rusticas_Roperuelos"
              pageWidth="595"
              pageHeight="842"
              columnWidth="535"
              leftMargin="30"
              rightMargin="30"
              topMargin="25"
              bottomMargin="25"
              whenNoDataType="AllSectionsNoDetail"
              uuid="7b382f10-8155-4f9a-9a14-002413600001">

    <!-- =====================================================================
         1. DEFINICIÓN DE PARÁMETROS DE ENTRADA ($P{...})
            Recibidos desde Java mediante Map<String, Object> en JasperFillManager.
         ===================================================================== -->
    <!-- Clave primaria del Titular Agrario para filtrar la consulta SQL -->
    <parameter name="ID_TITULAR" class="java.lang.Long">
        <defaultValueExpression><![CDATA[1L]]></defaultValueExpression>
    </parameter>

    <!-- Año de la Campaña Agrícola / Catastral -->
    <parameter name="CAMPANIA_AGRICOLA" class="java.lang.Integer">
        <defaultValueExpression><![CDATA[2024]]></defaultValueExpression>
    </parameter>

    <!-- Código oficial del expediente aprobado (ej. EXP-ROP-2024-0001) -->
    <parameter name="CODIGO_EXPEDIENTE" class="java.lang.String">
        <defaultValueExpression><![CDATA["EXP-ROP-2024-0001"]]></defaultValueExpression>
    </parameter>

    <!-- Nombre oficial de la Administración que emite el certificado -->
    <parameter name="NOMBRE_AYUNTAMIENTO" class="java.lang.String">
        <defaultValueExpression><![CDATA["EXCMO. AYUNTAMIENTO DE ROPERUELOS DEL PÁRAMO (LEÓN)"]]></defaultValueExpression>
    </parameter>

    <!-- Código Seguro de Verificación (CSV) generado en el backend Java -->
    <parameter name="CODIGO_CSV" class="java.lang.String">
        <defaultValueExpression><![CDATA["CSV-24136-2024-VERIFICADO"]]></defaultValueExpression>
    </parameter>

    <!-- Flujo de imagen (InputStream) opcional con el escudo institucional -->
    <parameter name="LOGO_STREAM" class="java.io.InputStream" isForPrompting="false"/>

    <!-- =====================================================================
         2. CONSULTA SQL PARAMETRIZADA (<queryString>)
            Jasper Reports transforma automáticamente $P{ID_TITULAR} y
            $P{CAMPANIA_AGRICOLA} en parámetros '?' de un PreparedStatement JDBC.
         ===================================================================== -->
    <queryString language="SQL">
        <![CDATA[
        SELECT
            em.codigo_expediente      AS codigoExpediente,
            t.nif_cif                 AS nifTitular,
            t.nombre_completo         AS nombreTitular,
            pr.poligono               AS poligono,
            pr.parcela                AS parcela,
            pr.recinto_sigpac         AS recintoSigpac,
            pr.paraje_nombre          AS parajeNombre,
            pr.referencia_catastral   AS referenciaCatastral,
            pr.tipo_cultivo           AS tipoCultivo,
            ep.cultivo_campania       AS cultivoDeclarado,
            pr.regimen_tenencia       AS regimenTenencia,
            ep.superficie_computada_ha AS superficieHa,
            em.fecha_resolucion       AS fechaResolucion
        FROM expedientes_municipales em
        INNER JOIN titulares t            ON t.id_titular = em.id_titular
        INNER JOIN expediente_parcelas ep ON ep.id_expediente = em.id_expediente
        INNER JOIN parcelas_rusticas pr   ON pr.id_parcela = ep.id_parcela
        WHERE t.id_titular = $P{ID_TITULAR}
          AND em.campania_agricola = $P{CAMPANIA_AGRICOLA}
          AND em.estado_expediente = 'APROBADO'
        ORDER BY
            pr.poligono ASC,
            pr.parcela ASC,
            pr.recinto_sigpac ASC
        ]]>
    </queryString>

    <!-- =====================================================================
         3. DEFINICIÓN DE CAMPOS ($F{...})
            Los nombres coinciden tanto con los alias del SELECT SQL como con
            los getters del DTO Java para soportar JDBC y JRBeanCollectionDataSource.
         ===================================================================== -->
    <field name="codigoExpediente"    class="java.lang.String"/>
    <field name="nifTitular"          class="java.lang.String"/>
    <field name="nombreTitular"       class="java.lang.String"/>
    <field name="poligono"            class="java.lang.Integer"/>
    <field name="parcela"             class="java.lang.Integer"/>
    <field name="recintoSigpac"       class="java.lang.Integer"/>
    <field name="parajeNombre"        class="java.lang.String"/>
    <field name="referenciaCatastral" class="java.lang.String"/>
    <field name="tipoCultivo"         class="java.lang.String"/>
    <field name="cultivoDeclarado"    class="java.lang.String"/>
    <field name="regimenTenencia"     class="java.lang.String"/>
    <field name="superficieHa"        class="java.math.BigDecimal"/>
    <field name="fechaResolucion"     class="java.time.LocalDate"/>

    <!-- =====================================================================
         4. VARIABLES DE CÁLCULO AUTOMÁTICO ($V{...})
            Calculan en tiempo de ejecución el sumatorio de hectáreas y el
            conteo total de recintos SIGPAC del titular.
         ===================================================================== -->
    <!-- Variable 1: Suma total de hectáreas (BigDecimal) en todo el informe -->
    <variable name="TOTAL_HECTAREAS_TITULAR" class="java.math.BigDecimal" calculation="Sum">
        <variableExpression><![CDATA[$F{superficieHa}]]></variableExpression>
        <initialValueExpression><![CDATA[java.math.BigDecimal.ZERO]]></initialValueExpression>
    </variable>

    <!-- Variable 2: Contador total de parcelas/recintos certificados -->
    <variable name="TOTAL_PARCELAS_CERTIFICADAS" class="java.lang.Integer" calculation="Count">
        <variableExpression><![CDATA[$F{parcela}]]></variableExpression>
        <initialValueExpression><![CDATA[0]]></initialValueExpression>
    </variable>

    <!-- Variable 3: Suma parcial de hectáreas de REGADÍO usando expresión ternaria -->
    <variable name="TOTAL_HECTAREAS_REGADIO" class="java.math.BigDecimal" calculation="Sum">
        <variableExpression><![CDATA["REGADIO".equalsIgnoreCase($F{tipoCultivo}) ? $F{superficieHa} : java.math.BigDecimal.ZERO]]></variableExpression>
        <initialValueExpression><![CDATA[java.math.BigDecimal.ZERO]]></initialValueExpression>
    </variable>

    <!-- =====================================================================
         5. BANDA TITLE (Se imprime una única vez en la primera página)
         ===================================================================== -->
    <title>
        <band height="115" splitType="Stretch">
            <!-- Nombre oficial del Ayuntamiento -->
            <textField>
                <reportElement x="0" y="0" width="535" height="22" uuid="10000001-0000-0000-0000-000000000001"/>
                <textElement textAlignment="Center" verticalAlignment="Middle">
                    <font fontName="SansSerif" size="13" isBold="true"/>
                </textElement>
                <textFieldExpression><![CDATA[$P{NOMBRE_AYUNTAMIENTO}]]></textFieldExpression>
            </textField>

            <!-- Subtítulo Oficial del Certificado -->
            <staticText>
                <reportElement x="0" y="24" width="535" height="20" uuid="10000001-0000-0000-0000-000000000002"/>
                <textElement textAlignment="Center" verticalAlignment="Middle">
                    <font fontName="SansSerif" size="11" isBold="true" isUnderline="true"/>
                </textElement>
                <text><![CDATA[CERTIFICADO MUNICIPAL DE PARCELAS RÚSTICAS Y EXPLOTACIÓN AGRARIA (SIGPAC)]]></text>
            </staticText>

            <!-- Bloque de datos del Expediente y del Titular Agrario -->
            <textField isBlankWhenNull="true">
                <reportElement x="0" y="52" width="535" height="55" uuid="10000001-0000-0000-0000-000000000003"/>
                <textElement textAlignment="Justified" verticalAlignment="Top">
                    <font fontName="SansSerif" size="9"/>
                </textElement>
                <textFieldExpression><![CDATA["La Secretaría-Intervención del " + $P{NOMBRE_AYUNTAMIENTO} + " CERTIFICA que, consultados los antecedentes obrantes en el Padrón Catastral de Rústica y el Registro Municipal de Expedientes Agrarios correspondientes a la Campaña " + $P{CAMPANIA_AGRICOLA} + " (Expediente Nº " + $P{CODIGO_EXPEDIENTE} + "), figuran a nombre del titular D./Dña./Entidad " + $F{nombreTitular} + " con NIF/CIF " + $F{nifTitular} + " las siguientes parcelas y recintos rústicos:"]]></textFieldExpression>
            </textField>
        </band>
    </title>

    <!-- =====================================================================
         6. BANDA PAGE HEADER (Se repite en la cabecera de todas las páginas)
         ===================================================================== -->
    <pageHeader>
        <band height="22" splitType="Stretch">
            <textField>
                <reportElement x="0" y="2" width="350" height="16" uuid="20000001-0000-0000-0000-000000000001"/>
                <textElement verticalAlignment="Middle">
                    <font fontName="SansSerif" size="8" isItalic="true"/>
                </textElement>
                <textFieldExpression><![CDATA["Expediente: " + $P{CODIGO_EXPEDIENTE} + " | Campaña Agrícola: " + $P{CAMPANIA_AGRICOLA} + " | NIF: " + $F{nifTitular}]]></textFieldExpression>
            </textField>
            <textField pattern="dd/MM/yyyy HH:mm">
                <reportElement x="350" y="2" width="185" height="16" uuid="20000001-0000-0000-0000-000000000002"/>
                <textElement textAlignment="Right" verticalAlignment="Middle">
                    <font fontName="SansSerif" size="8" isItalic="true"/>
                </textElement>
                <textFieldExpression><![CDATA[new java.util.Date()]]></textFieldExpression>
            </textField>
        </band>
    </pageHeader>

    <!-- =====================================================================
         7. BANDA COLUMN HEADER (Cabecera de la tabla de parcelas en cada página)
         ===================================================================== -->
    <columnHeader>
        <band height="24" splitType="Stretch">
            <staticText>
                <reportElement mode="Opaque" backcolor="#E2E8F0" x="0" y="0" width="55" height="22" uuid="30000001-0000-0000-0000-000000000001"/>
                <textElement textAlignment="Center" verticalAlignment="Middle"><font size="8" isBold="true"/></textElement>
                <text><![CDATA[POLÍGONO]]></text>
            </staticText>
            <staticText>
                <reportElement mode="Opaque" backcolor="#E2E8F0" x="55" y="0" width="55" height="22" uuid="30000001-0000-0000-0000-000000000002"/>
                <textElement textAlignment="Center" verticalAlignment="Middle"><font size="8" isBold="true"/></textElement>
                <text><![CDATA[PARCELA]]></text>
            </staticText>
            <staticText>
                <reportElement mode="Opaque" backcolor="#E2E8F0" x="110" y="0" width="55" height="22" uuid="30000001-0000-0000-0000-000000000003"/>
                <textElement textAlignment="Center" verticalAlignment="Middle"><font size="8" isBold="true"/></textElement>
                <text><![CDATA[RECINTO]]></text>
            </staticText>
            <staticText>
                <reportElement mode="Opaque" backcolor="#E2E8F0" x="165" y="0" width="160" height="22" uuid="30000001-0000-0000-0000-000000000004"/>
                <textElement textAlignment="Left" verticalAlignment="Middle"><font size="8" isBold="true"/></textElement>
                <text><![CDATA[ SISTEMA / TIPO EXPLOTACIÓN]]></text>
            </staticText>
            <staticText>
                <reportElement mode="Opaque" backcolor="#E2E8F0" x="325" y="0" width="110" height="22" uuid="30000001-0000-0000-0000-000000000005"/>
                <textElement textAlignment="Center" verticalAlignment="Middle"><font size="8" isBold="true"/></textElement>
                <text><![CDATA[EXPEDIENTE]]></text>
            </staticText>
            <staticText>
                <reportElement mode="Opaque" backcolor="#E2E8F0" x="435" y="0" width="100" height="22" uuid="30000001-0000-0000-0000-000000000006"/>
                <textElement textAlignment="Right" verticalAlignment="Middle"><font size="8" isBold="true"/></textElement>
                <text><![CDATA[SUPERFICIE (ha) ]]></text>
            </staticText>
        </band>
    </columnHeader>

    <!-- =====================================================================
         8. BANDA DETAIL (Se itera 1 vez por cada recinto rústico del titular)
         ===================================================================== -->
    <detail>
        <band height="20" splitType="Prevent">
            <!-- Polígono -->
            <textField>
                <reportElement x="0" y="0" width="55" height="18" uuid="40000001-0000-0000-0000-000000000001"/>
                <textElement textAlignment="Center" verticalAlignment="Middle"><font size="8"/></textElement>
                <textFieldExpression><![CDATA[$F{poligono}]]></textFieldExpression>
            </textField>

            <!-- Parcela -->
            <textField>
                <reportElement x="55" y="0" width="55" height="18" uuid="40000001-0000-0000-0000-000000000002"/>
                <textElement textAlignment="Center" verticalAlignment="Middle"><font size="8"/></textElement>
                <textFieldExpression><![CDATA[$F{parcela}]]></textFieldExpression>
            </textField>

            <!-- Recinto SIGPAC -->
            <textField>
                <reportElement x="110" y="0" width="55" height="18" uuid="40000001-0000-0000-0000-000000000003"/>
                <textElement textAlignment="Center" verticalAlignment="Middle"><font size="8"/></textElement>
                <textFieldExpression><![CDATA[$F{recintoSigpac}]]></textFieldExpression>
            </textField>

            <!-- Sistema de Cultivo (REGADIO / SECANO) con ajuste dinámico de altura si el texto es largo -->
            <textField textAdjust="StretchHeight" isBlankWhenNull="true">
                <reportElement x="165" y="0" width="160" height="18" uuid="40000001-0000-0000-0000-000000000004"/>
                <textElement textAlignment="Left" verticalAlignment="Middle"><font size="8"/></textElement>
                <textFieldExpression><![CDATA[" " + $F{tipoCultivo}]]></textFieldExpression>
            </textField>

            <!-- Código de Expediente -->
            <textField isBlankWhenNull="true">
                <reportElement x="325" y="0" width="110" height="18" uuid="40000001-0000-0000-0000-000000000005"/>
                <textElement textAlignment="Center" verticalAlignment="Middle"><font size="8"/></textElement>
                <textFieldExpression><![CDATA[$F{codigoExpediente}]]></textFieldExpression>
            </textField>

            <!-- Superficie en hectáreas formateada con 4 decimales exactos (#,##0.0000) -->
            <textField pattern="#,##0.0000">
                <reportElement x="435" y="0" width="100" height="18" uuid="40000001-0000-0000-0000-000000000006"/>
                <textElement textAlignment="Right" verticalAlignment="Middle"><font size="8" isBold="true"/></textElement>
                <textFieldExpression><![CDATA[$F{superficieHa}]]></textFieldExpression>
            </textField>
        </band>
    </detail>

    <!-- =====================================================================
         9. BANDA PAGE FOOTER (CSV de verificación y "Página X de Y")
         ===================================================================== -->
    <pageFooter>
        <band height="25" splitType="Stretch">
            <!-- Código Seguro de Verificación (CSV) a la izquierda -->
            <textField>
                <reportElement x="0" y="5" width="350" height="15" uuid="50000001-0000-0000-0000-000000000001"/>
                <textElement verticalAlignment="Middle"><font size="7" isItalic="true"/></textElement>
                <textFieldExpression><![CDATA["Documento verificable en Sede Electrónica — CSV: " + $P{CODIGO_CSV}]]></textFieldExpression>
            </textField>

            <!-- "Página X de" evaluado en tiempo actual (evaluationTime="Now") -->
            <textField evaluationTime="Now">
                <reportElement x="350" y="5" width="145" height="15" uuid="50000001-0000-0000-0000-000000000002"/>
                <textElement textAlignment="Right" verticalAlignment="Middle"><font size="8"/></textElement>
                <textFieldExpression><![CDATA["Página " + $V{PAGE_NUMBER} + " de "]]></textFieldExpression>
            </textField>

            <!-- "Y" (total de páginas) evaluado al finalizar todo el reporte (evaluationTime="Report") -->
            <textField evaluationTime="Report">
                <reportElement x="495" y="5" width="40" height="15" uuid="50000001-0000-0000-0000-000000000003"/>
                <textElement textAlignment="Left" verticalAlignment="Middle"><font size="8"/></textElement>
                <textFieldExpression><![CDATA[" " + $V{PAGE_NUMBER}]]></textFieldExpression>
            </textField>
        </band>
    </pageFooter>

    <!-- =====================================================================
         10. BANDA SUMMARY (Totales calculados por las variables $V{...} y firma)
         ===================================================================== -->
    <summary>
        <band height="95" splitType="Stretch">
            <!-- Total de recintos y suma de hectáreas de regadío + total general -->
            <textField>
                <reportElement mode="Opaque" backcolor="#F1F5F9" x="0" y="8" width="335" height="22" uuid="60000001-0000-0000-0000-000000000001"/>
                <textElement verticalAlignment="Middle"><font size="9" isBold="true"/></textElement>
                <textFieldExpression><![CDATA[" TOTAL RECINTOS CERTIFICADOS: " + $V{TOTAL_PARCELAS_CERTIFICADAS} + " (Regadío: " + $V{TOTAL_HECTAREAS_REGADIO} + " ha)"]]></textFieldExpression>
            </textField>

            <textField pattern="#,##0.0000">
                <reportElement mode="Opaque" backcolor="#E2E8F0" x="335" y="8" width="200" height="22" uuid="60000001-0000-0000-0000-000000000002"/>
                <textElement textAlignment="Right" verticalAlignment="Middle"><font size="10" isBold="true"/></textElement>
                <textFieldExpression><![CDATA[$V{TOTAL_HECTAREAS_TITULAR}]]></textFieldExpression>
            </textField>

            <!-- Pie de firma institucional -->
            <staticText>
                <reportElement x="0" y="42" width="535" height="45" uuid="60000001-0000-0000-0000-000000000003"/>
                <textElement textAlignment="Center" verticalAlignment="Middle">
                    <font size="8"/>
                </textElement>
                <text><![CDATA[Y para que así conste y surta los efectos oportunos ante los organismos agrarios y catastrales competentes, se expide la presente certificación en Roperuelos del Páramo (León), firmada electrónicamente por la Secretaría-Intervención con el Vº Bº de la Alcaldía-Presidencia.]]></text>
            </staticText>
        </band>
    </summary>

</jasperReport>
```

---
## ARCHIVO: JasperReportGeneratorService.java

```java
package es.seresco.agro.roperuelos.report; // Paquete especializado en generación documental con Jasper Reports

import java.io.ByteArrayOutputStream; // Buffer en memoria para exportaciones a Excel (XLSX) o PDF
import java.io.InputStream; // Flujo de lectura para cargar el fichero .jasper o .jrxml desde el classpath
import java.sql.Connection; // Conexión JDBC para informes que ejecutan su propia <queryString> SQL
import java.util.HashMap; // Implementación de Map para inyectar los parámetros $P{...}
import java.util.List; // Lista de DTOs cuando usamos JRBeanCollectionDataSource
import java.util.Map; // Interfaz Map<String, Object>
import java.util.UUID; // Generación del Código Seguro de Verificación (CSV) único por certificado
import java.util.concurrent.ConcurrentHashMap; // Caché thread-safe en memoria para no recompilar el .jrxml en cada petición
import java.util.logging.Level; // Niveles de log
import java.util.logging.Logger; // Logger del servidor

import javax.annotation.Resource; // Inyección del pool de conexiones JNDI del servidor JEE
import javax.enterprise.context.ApplicationScoped; // Servicio Singleton en CDI (equivalente a @Service en Spring Boot)
import javax.inject.Inject; // Inyección del servicio de negocio
import javax.sql.DataSource; // Pool de conexiones SQL

import es.seresco.agro.roperuelos.repository.ExpedienteRepository.ResumenCertificadoCatastralDTO; // DTO de fila del informe
import es.seresco.agro.roperuelos.service.ExpedienteService; // Servicio que provee los datos validados
import net.sf.jasperreports.engine.JRException; // Excepción comprobada (Checked Exception) propia de Jasper Reports
import net.sf.jasperreports.engine.JasperCompileManager; // Compila plantillas XML .jrxml a objetos binarios JasperReport (.jasper)
import net.sf.jasperreports.engine.JasperExportManager; // Exporta directamente un objeto JasperPrint a PDF o XML/HTML
import net.sf.jasperreports.engine.JasperFillManager; // Rellena la plantilla compilada cruzándola con los parámetros y el DataSource
import net.sf.jasperreports.engine.JasperPrint; // Documento intermedio ya paginado y rellenado en memoria, listo para exportar
import net.sf.jasperreports.engine.JasperReport; // Representación compilada en memoria de la plantilla del informe
import net.sf.jasperreports.engine.data.JRBeanCollectionDataSource; // Adaptador para pasar una List<DTO> de Java a Jasper Reports
import net.sf.jasperreports.engine.export.ooxml.JRXlsxExporter; // Exportador oficial a Microsoft Excel (.xlsx)
import net.sf.jasperreports.engine.util.JRLoader; // Cargador de ficheros .jasper ya precompilados en disco/classpath
import net.sf.jasperreports.export.SimpleExporterInput; // Entrada del exportador XLSX
import net.sf.jasperreports.export.SimpleOutputStreamExporterOutput; // Salida del exportador XLSX
import net.sf.jasperreports.export.SimpleXlsxReportConfiguration; // Configuración de pestañas y tipos de celda en Excel

/**
 * Servicio Empresarial de Generación de Informes y Certificados con Jasper Reports.
 *
 * Cubre las dos arquitecturas que pueden preguntarte en la entrevista técnica de Seresco:
 *  1) Generación mediante JRBeanCollectionDataSource (pasando una colección de DTOs Java ya validados).
 *  2) Generación mediante java.sql.Connection directa (ejecutando el <queryString> SQL del .jrxml).
 *  3) Exportación tanto a PDF oficial (JasperExportManager) como a Excel .xlsx (JRXlsxExporter).
 */
@ApplicationScoped // Instancia única compartida; reutiliza la caché de plantillas compiladas
public class JasperReportGeneratorService {

    private static final Logger LOG = Logger.getLogger(JasperReportGeneratorService.class.getName());

    // Rutas de las plantillas dentro de src/main/resources/reports/
    private static final String RUTA_PLANTILLA_JRXML  = "/reports/informe_parcelas_titular.jrxml";
    private static final String RUTA_PLANTILLA_JASPER = "/reports/informe_parcelas_titular.jasper";
    private static final String RUTA_LOGO_ESCUDO      = "/reports/img/escudo_roperuelos.png";

    // Caché concurrente de plantillas compiladas: evita penalizar la CPU compilando el XML en cada clic del usuario
    private final Map<String, JasperReport> cachePlantillasCompiladas = new ConcurrentHashMap<>();

    @Inject // Servicio de negocio para la Opción A (JRBeanCollectionDataSource)
    private ExpedienteService expedienteService;

    @Resource(lookup = "java:/jdbc/AgroRoperuelosDS") // DataSource JNDI para la Opción B (Conexión JDBC directa)
    private DataSource dataSource;

    // =========================================================================
    // OPCIÓN A: GENERACIÓN DE PDF CON JRBeanCollectionDataSource (COLECCIÓN JAVA)
    // =========================================================================

    /**
     * Genera el "Certificado Municipal de Parcelas Rústicas y Explotación Agraria" en formato PDF
     * obteniendo los datos desde la capa de servicio Java y envolviéndolos en un JRBeanCollectionDataSource.
     */
    public byte[] generarCertificadoParcelasPdf(
            Long idTitular,
            String nifTitular,
            Integer campaniaAgricola,
            String codigoExpediente) {

        LOG.log(Level.INFO, "Iniciando generación de PDF Jasper Reports [Titular={0}, Expediente={1}]",
                new Object[]{nifTitular, codigoExpediente});

        try {
            // 1. Recuperamos la lista de DTOs validada desde el servicio de negocio
            List<ResumenCertificadoCatastralDTO> filasParcelas =
                    expedienteService.obtenerDatosParaCertificadoJasper(nifTitular, campaniaAgricola);

            // 2. Obtenemos la plantilla compilada (desde .jasper precompilado o compilando y cacheando el .jrxml)
            JasperReport reporteCompilado = obtenerOCargarPlantilla();

            // 3. Construimos el diccionario Map<String, Object> con los parámetros $P{...} definidos en el .jrxml
            Map<String, Object> parametros = construirMapaParametros(idTitular, campaniaAgricola, codigoExpediente);

            // 4. Envolvemos la lista de objetos Java en un JRBeanCollectionDataSource
            //    Jasper Reports leerá cada atributo $F{poligono}, $F{superficieHa} invocando getPoligono(), getSuperficieHa()
            JRBeanCollectionDataSource origenDatosBeans = new JRBeanCollectionDataSource(filasParcelas);

            // 5. Rellenamos el informe (Fase de Fill): combina Plantilla + Parámetros ($P) + Filas ($F) y calcula Variables ($V)
            JasperPrint documentoRelleno = JasperFillManager.fillReport(
                    reporteCompilado,
                    parametros,
                    origenDatosBeans
            );

            // 6. Exportamos el objeto JasperPrint a un array de bytes PDF listo para enviar por HTTP
            byte[] pdfBytes = JasperExportManager.exportReportToPdf(documentoRelleno);

            LOG.log(Level.INFO, "Certificado PDF generado correctamente ({0} bytes, {1} parcelas).",
                    new Object[]{pdfBytes.length, filasParcelas.size()});

            return pdfBytes;

        } catch (JRException jre) {
            LOG.log(Level.SEVERE, "Error de JasperReports al generar el certificado PDF del expediente " + codigoExpediente, jre);
            throw new RuntimeException("Error procesando la plantilla de Jasper Reports.", jre);
        }
    }

    // =========================================================================
    // OPCIÓN B: GENERACIÓN DE PDF PASANDO CONEXIÓN JDBC DIRECTA AL .JRXML
    // =========================================================================

    /**
     * Variante muy utilizada en Seresco cuando la consulta SQL reside directamente en la etiqueta
     * <queryString> del fichero .jrxml: le pasamos una Connection del Pool JDBC dentro de un try-with-resources.
     */
    public byte[] generarCertificadoConConexionJdbcDirecta(
            Long idTitular,
            Integer campaniaAgricola,
            String codigoExpediente) {

        // try-with-resources garantiza que la conexión JDBC se cierre (regrese al Pool) siempre al terminar fillReport
        try (Connection conexionJdbc = dataSource.getConnection()) {

            JasperReport reporteCompilado = obtenerOCargarPlantilla();
            Map<String, Object> parametros = construirMapaParametros(idTitular, campaniaAgricola, codigoExpediente);

            // En esta sobrecarga, el tercer argumento es la Connection JDBC; Jasper ejecuta el <queryString> del .jrxml
            JasperPrint documentoRelleno = JasperFillManager.fillReport(
                    reporteCompilado,
                    parametros,
                    conexionJdbc
            );

            return JasperExportManager.exportReportToPdf(documentoRelleno);

        } catch (Exception e) {
            LOG.log(Level.SEVERE, "Error generando informe Jasper con conexión JDBC directa", e);
            throw new RuntimeException("Fallo en la generación del informe PDF por conexión directa.", e);
        }
    }

    // =========================================================================
    // OPCIÓN C: EXPORTACIÓN DEL MISMO INFORME A EXCEL (.XLSX) CON JRXlsxExporter
    // =========================================================================

    /**
     * Muchos pliegos de la Administración Pública piden poder descargar los listados tanto en PDF
     * como en Excel (.xlsx). Con Jasper Reports reutilizamos el mismo JasperPrint cambiando el Exporter.
     */
    public byte[] exportarListadoParcelasAExcelXlsx(
            Long idTitular,
            String nifTitular,
            Integer campaniaAgricola,
            String codigoExpediente) {

        try (ByteArrayOutputStream baos = new ByteArrayOutputStream()) {
            List<ResumenCertificadoCatastralDTO> filas =
                    expedienteService.obtenerDatosParaCertificadoJasper(nifTitular, campaniaAgricola);

            JasperReport reporteCompilado = obtenerOCargarPlantilla();
            Map<String, Object> parametros = construirMapaParametros(idTitular, campaniaAgricola, codigoExpediente);
            JasperPrint jasperPrint = JasperFillManager.fillReport(
                    reporteCompilado, parametros, new JRBeanCollectionDataSource(filas));

            // Configuramos el exportador oficial de Excel OOXML (.xlsx)
            JRXlsxExporter exporter = new JRXlsxExporter();
            exporter.setExporterInput(new SimpleExporterInput(jasperPrint));
            exporter.setExporterOutput(new SimpleOutputStreamExporterOutput(baos));

            SimpleXlsxReportConfiguration configExcel = new SimpleXlsxReportConfiguration();
            configExcel.setOnePagePerSheet(false);        // Todas las filas en una sola hoja continua
            configExcel.setDetectCellType(true);          // Las hectáreas se exportan como celdas numéricas reales en Excel
            configExcel.setRemoveEmptySpaceBetweenRows(true);
            configExcel.setWhitePageBackground(false);
            exporter.setConfiguration(configExcel);

            exporter.exportReport(); // Ejecuta el volcado al ByteArrayOutputStream
            return baos.toByteArray();

        } catch (Exception e) {
            LOG.log(Level.SEVERE, "Error exportando informe Jasper Reports a Excel XLSX", e);
            throw new RuntimeException("No se pudo exportar el informe a formato Excel.", e);
        }
    }

    // =========================================================================
    // MÉTODOS PRIVADOS DE CARGA/COMPILACIÓN DE PLANTILLA Y PARÁMETROS
    // =========================================================================

    /**
     * Carga el fichero precompilado .jasper si existe en el classpath; en caso contrario,
     * carga el código fuente XML .jrxml, lo compila con JasperCompileManager y lo guarda en caché.
     */
    private JasperReport obtenerOCargarPlantilla() throws JRException {
        // Si ya fue compilado previamente en esta ejecución del servidor, lo devolvemos al instante desde memoria
        JasperReport enCache = cachePlantillasCompiladas.get(RUTA_PLANTILLA_JRXML);
        if (enCache != null) {
            return enCache;
        }

        // Intentamos primero cargar el binario .jasper precompilado por Maven
        try (InputStream jasperStream = getClass().getResourceAsStream(RUTA_PLANTILLA_JASPER)) {
            if (jasperStream != null) {
                JasperReport cargado = (JasperReport) JRLoader.loadObject(jasperStream);
                cachePlantillasCompiladas.put(RUTA_PLANTILLA_JRXML, cargado);
                return cargado;
            }
        } catch (Exception ignorada) {
            LOG.log(Level.FINE, "No se encontró .jasper precompilado; se procederá a compilar el .jrxml en vivo.");
        }

        // Si no hay .jasper, leemos el .jrxml del classpath y lo compilamos con JasperCompileManager
        try (InputStream jrxmlStream = getClass().getResourceAsStream(RUTA_PLANTILLA_JRXML)) {
            if (jrxmlStream == null) {
                throw new IllegalStateException("No se encuentra la plantilla en el classpath: " + RUTA_PLANTILLA_JRXML);
            }
            JasperReport compilado = JasperCompileManager.compileReport(jrxmlStream);
            cachePlantillasCompiladas.put(RUTA_PLANTILLA_JRXML, compilado);
            return compilado;
        } catch (Exception e) {
            throw new JRException("Error al leer o compilar la plantilla " + RUTA_PLANTILLA_JRXML, e);
        }
    }

    /**
     * Construye el mapa de parámetros $P{...} que se inyectan en la plantilla informe_parcelas_titular.jrxml.
     */
    private Map<String, Object> construirMapaParametros(Long idTitular, Integer campania, String codigoExpediente) {
        Map<String, Object> params = new HashMap<>();
        params.put("ID_TITULAR", idTitular);
        params.put("CAMPANIA_AGRICOLA", campania);
        params.put("CODIGO_EXPEDIENTE", codigoExpediente);
        params.put("NOMBRE_AYUNTAMIENTO", "EXCMO. AYUNTAMIENTO DE ROPERUELOS DEL PÁRAMO (LEÓN)");

        // Generamos un Código Seguro de Verificación (CSV) único para el pie de página del PDF
        String csvVerificacion = "CSV-24136-" + campania + "-"
                + UUID.randomUUID().toString().substring(0, 8).toUpperCase();
        params.put("CODIGO_CSV", csvVerificacion);

        // Si existe el escudo institucional en el classpath, lo pasamos como InputStream en $P{LOGO_STREAM}
        InputStream logoStream = getClass().getResourceAsStream(RUTA_LOGO_ESCUDO);
        if (logoStream != null) {
            params.put("LOGO_STREAM", logoStream);
        }
        return params;
    }
}
```

