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
