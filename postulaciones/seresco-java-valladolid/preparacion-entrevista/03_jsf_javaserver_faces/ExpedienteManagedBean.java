package es.seresco.agro.roperuelos.web; // Paquete de capa de presentación web JSF / PrimeFaces

import java.io.IOException; // Excepción de entrada/salida al escribir el flujo binario del PDF en el navegador
import java.io.OutputStream; // Flujo de salida HTTP para enviar el documento PDF generado por Jasper Reports
import java.io.Serializable; // Obligatorio para todo Bean @ViewScoped o @SessionScoped en Jakarta EE / JSF
import java.time.LocalDate; // Para obtener el año de la campaña agraria actual por defecto
import java.util.ArrayList; // Lista vacía inicializada defensivamente
import java.util.List; // Colección de expedientes mostrada en la tabla p:dataTable
import java.util.logging.Level; // Nivel de traza en el log del servidor
import java.util.logging.Logger; // Logger institucional

import javax.annotation.PostConstruct; // Se ejecuta una sola vez justo después de construir el Bean e inyectar dependencias
import javax.faces.application.FacesMessage; // Objeto estándar de JSF para mostrar alertas (INFO, WARN, ERROR) en pantalla
import javax.faces.context.ExternalContext; // Envoltorio JSF que da acceso seguro al HttpServletResponse para descargas
import javax.faces.context.FacesContext; // Contexto central de la petición JSF actual
import javax.faces.view.ViewScoped; // Ámbito de Vista: mantiene el estado mientras el usuario siga en la misma pantalla XHTML
import javax.inject.Inject; // Inyección CDI del servicio de negocio y del generador de informes Jasper Reports
import javax.inject.Named; // Expone este Bean al Expression Language del XHTML como #{expedienteManagedBean}

import es.seresco.agro.roperuelos.model.ExpedienteAgrarioEntity; // Entidad de expediente agrario
import es.seresco.agro.roperuelos.model.ExpedienteAgrarioEntity.EstadoExpediente; // Enumerado de estados para el desplegable
import es.seresco.agro.roperuelos.report.JasperReportGeneratorService; // Servicio que compila, rellena y exporta el .jrxml a PDF
import es.seresco.agro.roperuelos.service.ExpedienteService; // Servicio transaccional de negocio
import es.seresco.agro.roperuelos.service.ExpedienteService.ReglaNegocioAgrarioException; // Excepción controlada de negocio

/**
 * Controlador de Vista JSF (Backing Bean CDI) para la pantalla de Gestión de Expedientes
 * Agrícolas y Catastrales del Ayuntamiento de Roperuelos del Páramo.
 *
 * Está anotado con @ViewScoped para conservar los filtros, la lista paginada del <p:dataTable>
 * y el expediente seleccionado en el diálogo modal (<p:dialog>) durante las peticiones AJAX parciales.
 */
@Named("expedienteManagedBean") // Nombre accesible desde gestion_expedientes_agricolas.xhtml mediante #{expedienteManagedBean}
@ViewScoped                     // Vive mientras el administrativo permanezca en gestion_expedientes_agricolas.xhtml
public class ExpedienteManagedBean implements Serializable {

    private static final long serialVersionUID = 1L;
    private static final Logger LOG = Logger.getLogger(ExpedienteManagedBean.class.getName());

    // =========================================================================
    // INYECCIÓN DE SERVICIOS DE NEGOCIO Y DE REPORTING (JASPER REPORTS)
    // =========================================================================

    @Inject // Inyecta el servicio transaccional de expedientes
    private ExpedienteService expedienteService;

    @Inject // Inyecta el servicio generador de certificados PDF con Jasper Reports
    private JasperReportGeneratorService jasperReportService;

    // =========================================================================
    // ATRIBUTOS DE ESTADO DE LA VISTA (FILTROS, RESULTADOS Y SELECCIÓN)
    // =========================================================================

    private Integer filtroCampania;                            // Filtro por año de campaña agrícola (ej. 2024)
    private String filtroNifTitular;                           // Filtro por NIF/CIF del agricultor o titular catastral
    private EstadoExpediente filtroEstado;                     // Filtro por estado del expediente (BORRADOR, APROBADO, etc.)

    private List<ExpedienteAgrarioEntity> listaExpedientes;    // Colección que alimenta el <p:dataTable> de PrimeFaces
    private ExpedienteAgrarioEntity expedienteSeleccionado;    // Fila actualmente seleccionada para ver/editar en el <p:dialog>
    private String observacionesAprobacion;                    // Campo de texto del diálogo modal para que el secretario anote su informe

    // =========================================================================
    // INICIALIZACIÓN DEL BEAN (@PostConstruct)
    // =========================================================================

    /**
     * Se ejecuta automáticamente una única vez cuando el usuario entra en la página XHTML.
     * NUNCA ponemos consultas SQL en los getters; las ejecutamos aquí y en los métodos de acción.
     */
    @PostConstruct
    public void inicializarVista() {
        this.filtroCampania = 2024;                            // Campaña por defecto al abrir la bandeja
        this.listaExpedientes = new ArrayList<>();             // Inicialización defensiva
        buscarExpedientes();                                   // Carga inicial de datos desde base de datos
    }

    // =========================================================================
    // ACCIONES INVOCADAS DESDE EL XHTML (FASE 5: INVOKE APPLICATION)
    // =========================================================================

    /**
     * Acción invocada por el botón "Buscar / Filtrar" mediante AJAX parcial.
     */
    public void buscarExpedientes() {
        try {
            this.listaExpedientes = expedienteService.buscarExpedientesBandeja(
                    this.filtroCampania,
                    this.filtroNifTitular,
                    this.filtroEstado
            );
            agregarMensajeJsf(FacesMessage.SEVERITY_INFO,
                    "Consulta completada",
                    "Se han recuperado " + this.listaExpedientes.size() + " expedientes agrarios.");
        } catch (Exception e) {
            LOG.log(Level.SEVERE, "Error al consultar la bandeja de expedientes en JSF", e);
            agregarMensajeJsf(FacesMessage.SEVERITY_ERROR,
                    "Error en la consulta",
                    "No se pudieron recuperar los expedientes. Revise el log del servidor.");
        }
    }

    /**
     * Limpia los filtros de búsqueda y recarga la bandeja completa de la campaña actual.
     */
    public void limpiarFiltros() {
        this.filtroCampania = LocalDate.now().getYear();
        this.filtroNifTitular = null;
        this.filtroEstado = null;
        this.expedienteSeleccionado = null;
        buscarExpedientes();
    }

    /**
     * Prepara el expediente seleccionado en la fila del <p:dataTable> antes de abrir el diálogo modal <p:dialog>.
     */
    public void prepararEdicionModal(ExpedienteAgrarioEntity fila) {
        this.expedienteSeleccionado = fila;
        this.observacionesAprobacion = (fila != null) ? fila.getObservacionesTecnicas() : "";
    }

    /**
     * Guarda los cambios realizados sobre el expediente en el diálogo modal de PrimeFaces.
     */
    public void guardarCambiosModal() {
        if (this.expedienteSeleccionado == null) {
            return;
        }
        try {
            this.expedienteSeleccionado.setObservacionesTecnicas(this.observacionesAprobacion);
            expedienteService.registrarOActualizarExpediente(this.expedienteSeleccionado);
            buscarExpedientes(); // Refresca la tabla principal
            agregarMensajeJsf(FacesMessage.SEVERITY_INFO,
                    "Expediente actualizado",
                    "Se han guardado correctamente los datos del expediente " + this.expedienteSeleccionado.getCodigoExpediente());
        } catch (ReglaNegocioAgrarioException rne) {
            agregarMensajeJsf(FacesMessage.SEVERITY_WARN, "Validación de negocio", rne.getMessage());
        } catch (Exception e) {
            LOG.log(Level.SEVERE, "Error al guardar expediente desde modal JSF", e);
            agregarMensajeJsf(FacesMessage.SEVERITY_ERROR, "Error técnico", "No se pudo guardar el expediente.");
        }
    }

    /**
     * Aprueba oficialmente un expediente desde la pantalla JSF para habilitar la emisión de su Certificado PDF.
     */
    public void aprobarExpedienteSeleccionado() {
        if (this.expedienteSeleccionado == null) {
            agregarMensajeJsf(FacesMessage.SEVERITY_WARN, "Atención", "Debe seleccionar un expediente primero.");
            return;
        }
        try {
            expedienteService.aprobarExpediente(
                    this.expedienteSeleccionado.getCodigoExpediente(),
                    this.observacionesAprobacion
            );
            buscarExpedientes(); // Refresca los estados en la tabla p:dataTable
            agregarMensajeJsf(FacesMessage.SEVERITY_INFO,
                    "Expediente Aprobado",
                    "El expediente " + this.expedienteSeleccionado.getCodigoExpediente() + " ha quedado APROBADO y listo para emitir certificado PDF.");
        } catch (ReglaNegocioAgrarioException rne) {
            agregarMensajeJsf(FacesMessage.SEVERITY_WARN, "No se puede aprobar", rne.getMessage());
        } catch (Exception e) {
            LOG.log(Level.SEVERE, "Error al aprobar el expediente", e);
            agregarMensajeJsf(FacesMessage.SEVERITY_ERROR, "Error del sistema", "Fallo inesperado al aprobar el expediente.");
        }
    }

    // =========================================================================
    // DESCARGA DEL CERTIFICADO PDF GENERADO CON JASPER REPORTS DESDE JSF
    // =========================================================================

    /**
     * Genera en vivo el "Certificado Municipal de Parcelas Rústicas y Explotación Agraria"
     * utilizando Jasper Reports y lo envía como descarga directa (application/pdf) al navegador.
     *
     * PREGUNTA DE ENTREVISTA: ¿Por qué llamamos a facesContext.responseComplete()?
     * Porque ya hemos volcado los bytes binarios del PDF en el OutputStream del HttpServletResponse;
     * si no llamáramos a responseComplete(), JSF intentaría ejecutar la Fase 6 (Render Response)
     * escribiendo el HTML de la página detrás del PDF y corrompiendo el archivo o lanzando IllegalStateException.
     */
    public void descargarCertificadoPdfJasper(ExpedienteAgrarioEntity expediente) {
        if (expediente == null || expediente.getTitular() == null) {
            agregarMensajeJsf(FacesMessage.SEVERITY_WARN, "Atención", "Expediente o titular no válido para emitir certificado.");
            return;
        }

        FacesContext facesContext = FacesContext.getCurrentInstance();
        ExternalContext externalContext = facesContext.getExternalContext();

        try {
            // 1. Invocamos al servicio de Jasper Reports pasando el ID del titular, NIF y el expediente
            byte[] pdfBytes = jasperReportService.generarCertificadoParcelasPdf(
                    expediente.getTitular().getId(),
                    expediente.getTitular().getNifCif(),
                    expediente.getCampaniaAgricola(),
                    expediente.getCodigoExpediente()
            );

            // 2. Construimos un nombre de fichero oficial limpio (ej. Certificado_Parcelas_09784512A_2024.pdf)
            String nombreArchivoPdf = String.format("Certificado_Parcelas_%s_%d.pdf",
                    expediente.getTitular().getNifCif(),
                    expediente.getCampaniaAgricola());

            // 3. Limpiamos cualquier buffer previo y configuramos las cabeceras HTTP de descarga PDF
            externalContext.responseReset(); // Limpia cabeceras y buffers previos del response
            externalContext.setResponseContentType("application/pdf"); // MIME Type oficial de Adobe PDF
            externalContext.setResponseContentLength(pdfBytes.length); // Tamaño exacto en bytes para barra de progreso del navegador
            externalContext.setResponseHeader("Content-Disposition",
                    "attachment; filename=\"" + nombreArchivoPdf + "\""); // Fuerza descarga con nombre oficial

            // 4. Escribimos el array de bytes del PDF en el flujo de salida HTTP y hacemos flush
            try (OutputStream out = externalContext.getResponseOutputStream()) {
                out.write(pdfBytes);
                out.flush();
            }

            // 5. CRÍTICO EN JSF: Notificamos al ciclo de vida que la respuesta HTTP ya ha finalizado
            facesContext.responseComplete();

        } catch (ReglaNegocioAgrarioException rne) {
            agregarMensajeJsf(FacesMessage.SEVERITY_WARN, "Certificado no disponible", rne.getMessage());
        } catch (IOException e) {
            LOG.log(Level.SEVERE, "Error de E/S enviando el PDF de Jasper Reports al navegador", e);
            agregarMensajeJsf(FacesMessage.SEVERITY_ERROR, "Error de descarga", "No se pudo transmitir el archivo PDF al navegador.");
        } catch (Exception e) {
            LOG.log(Level.SEVERE, "Error generando el informe Jasper Reports", e);
            agregarMensajeJsf(FacesMessage.SEVERITY_ERROR, "Error en Jasper Reports", "Fallo al compilar o rellenar la plantilla JRXML.");
        }
    }

    // =========================================================================
    // MÉTODOS AUXILIARES PARA LA VISTA Y GETTERS / SETTERS
    // =========================================================================

    /**
     * Devuelve todos los valores del enumerado EstadoExpediente para poblar el <h:selectOneMenu> del filtro.
     */
    public EstadoExpediente[] getEstadosDisponibles() {
        return EstadoExpediente.values();
    }

    /**
     * Método helper para encolar mensajes FacesMessage en el contexto actual de JSF.
     */
    private void agregarMensajeJsf(FacesMessage.Severity severidad, String resumen, String detalle) {
        FacesContext.getCurrentInstance().addMessage(null, new FacesMessage(severidad, resumen, detalle));
    }

    public Integer getFiltroCampania() { return filtroCampania; }
    public void setFiltroCampania(Integer filtroCampania) { this.filtroCampania = filtroCampania; }

    public String getFiltroNifTitular() { return filtroNifTitular; }
    public void setFiltroNifTitular(String filtroNifTitular) { this.filtroNifTitular = filtroNifTitular; }

    public EstadoExpediente getFiltroEstado() { return filtroEstado; }
    public void setFiltroEstado(EstadoExpediente filtroEstado) { this.filtroEstado = filtroEstado; }

    public List<ExpedienteAgrarioEntity> getListaExpedientes() { return listaExpedientes; }
    public ExpedienteAgrarioEntity getExpedienteSeleccionado() { return expedienteSeleccionado; }
    public void setExpedienteSeleccionado(ExpedienteAgrarioEntity expedienteSeleccionado) { this.expedienteSeleccionado = expedienteSeleccionado; }

    public String getObservacionesAprobacion() { return observacionesAprobacion; }
    public void setObservacionesAprobacion(String observacionesAprobacion) { this.observacionesAprobacion = observacionesAprobacion; }
}
