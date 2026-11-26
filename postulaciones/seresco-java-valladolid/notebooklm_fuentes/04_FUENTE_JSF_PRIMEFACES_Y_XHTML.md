# FUENTE 04 — JSF (JAVASERVER FACES), PRIMEFACES, MANAGED BEAN Y VISTA XHTML

---
## ARCHIVO: 03_arquitectura_ciclo_vida_y_preguntas_jsf.md

# 03 — ARQUITECTURA, CICLO DE VIDA, SCOPES Y 15 PREGUNTAS DE ENTREVISTA: JSF (JAVASERVER FACES) Y PRIMEFACES

> **Objetivo de este documento:** Dominar **JSF (JavaServer Faces 2.2 / 2.3 / Jakarta Faces)** y **PrimeFaces**, que es el framework de interfaz web institucional exigido explícitamente en la vacante de **Seresco Valladolid** para los aplicativos de gestión agraria y administración pública.

---

## 1. ARQUITECTURA MVC BASADA EN COMPONENTES EN JSF

A diferencia de Spring MVC o JSP clásico (que son frameworks orientados a peticiones HTTP/acciones donde tú manejas manualmente los parámetros del `HttpServletRequest`), **JSF es un framework MVC orientado a componentes en el servidor y guiado por eventos**:

1. **Controlador Frontal (*Front Controller*) — `FacesServlet`:**
   - Configurado en `web.xml` (mapeado a `*.xhtml` o `/faces/*`).
   - Intercepta todas las peticiones HTTP, construye el contexto **`FacesContext`** (que envuelve el `HttpServletRequest` y `HttpServletResponse`) y coordina las 6 fases del ciclo de vida.
2. **Vista (*View*) — Plantillas Facelets (`.xhtml`):**
   - Archivos XML/XHTML con espacios de nombres (`xmlns:h`, `xmlns:f`, `xmlns:ui`, `xmlns:p` de PrimeFaces).
   - En el servidor, cada etiqueta (`<h:inputText>`, `<p:dataTable>`) se transforma en un nodo Java dentro de un **Árbol de Componentes (`UIViewRoot`)** que guarda su estado entre peticiones.
3. **Modelo y Controlador de Vista (*Backing Bean*) — CDI Bean (`@Named`) / Managed Bean:**
   - Clase Java anotada con `@Named("expedienteManagedBean")` y un ámbito como `@ViewScoped`.
   - Expone propiedades (atributos con *getters* y *setters*) enlazadas a los campos del XHTML mediante **Expression Language (`#{expedienteManagedBean.filtroNifTitular}`)** y métodos de acción (`#{expedienteManagedBean.buscarExpedientes()}`) invocados al pulsar botones.

---

## 2. LAS 6 FASES DEL CICLO DE VIDA DE JSF (PREGUNTA ESTRELLA DE ENTREVISTA)

Cuando un administrativo pulsa un botón `<h:commandButton>` o `<p:commandButton>` en una pantalla JSF, la petición atraviesa **6 fases ordenadas**:

```text
[Petición HTTP / AJAX]
       │
       ▼
1. RESTORE VIEW (Restaurar Vista)
   └─ Si es la primera vez (GET), construye el árbol UIViewRoot vacío.
   └─ Si es un Postback (POST del formulario), recupera el árbol UIViewRoot guardado en servidor/cliente.
       │
       ▼
2. APPLY REQUEST VALUES (Aplicar Valores de la Petición)
   └─ Cada componente del árbol lee su valor bruto (String) del request HTTP y lo guarda en su "submittedValue".
   └─ Si el botón pulsado tiene immediate="true" (ej. botón Cancelar), salta directamente a Render Response.
       │
       ▼
3. PROCESS VALIDATIONS (Procesar Conversores y Validadores)
   └─ Convierte los Strings a tipos Java (ej. String -> LocalDate o BigDecimal mediante Converters).
   └─ Ejecuta las validaciones (required="true", <f:validateLongRange>, Bean Validation @NotNull).
   └─ ¡IMPORTANTE!: Si falla una conversión o validación, añade un FacesMessage de error y SALTA DIRECTAMENTE
      a la Fase 6 (Render Response) sin tocar el Bean ni ejecutar la base de datos.
       │
       ▼
4. UPDATE MODEL VALUES (Actualizar Valores del Modelo)
   └─ Como los datos ya son válidos, JSF invoca los métodos SETTERS de nuestro Bean Java
      (ej. expedienteManagedBean.setFiltroNifTitular(...)) volcando los valores limpios al modelo.
       │
       ▼
5. INVOKE APPLICATION (Invocar a la Aplicación)
   └─ Ejecuta el método de negocio asociado al botón pulsado (action="#{expedienteManagedBean.aprobarExpedienteSeleccionado()}")
      que a su vez llama a nuestro ExpedienteService (@Transactional) o genera el PDF de Jasper Reports.
       │
       ▼
6. RENDER RESPONSE (Renderizar Respuesta)
   └─ JSF invoca los métodos GETTERS del Bean, guarda el estado de la vista (ViewState) y genera el HTML
      (o el fragmento XML parcial si fue una petición AJAX) de vuelta al navegador.
```

---

## 3. DIFERENCIA CRÍTICA ENTRE SCOPES: `@RequestScoped` vs. `@ViewScoped` vs. `@SessionScoped`

| Ámbito (Scope) | Cuánto vive la instancia del Bean | Cuándo usarlo (y cuándo NO usarlo) |
| :--- | :--- | :--- |
| **`@RequestScoped`** | Vive **una única petición HTTP** (desde que entra al `FacesServlet` hasta que termina la Fase 6). Se destruye inmediatamente después. | Útil para páginas estáticas de solo consulta sin AJAX. **Cuidado:** si tienes una tabla con un diálogo modal o botones dentro de un `<p:dataTable>`, con `@RequestScoped` el bean se recrea desde cero en cada clic y se pierde la fila seleccionada. |
| **`@ViewScoped`** *(El estándar de oro en JSF / PrimeFaces)* | Vive **mientras el usuario permanezca interactuando con la misma pantalla XHTML** (haciendo búsquedas AJAX, paginando la tabla, abriendo diálogos `p:dialog`, validando formularios). Se destruye automáticamente en cuanto el usuario navega a otra URL distinta. | **Obligatorio en el 90% de las pantallas CRUD de Seresco** (como `gestion_expedientes_agricolas.xhtml`). Requiere que la clase implemente `Serializable`. Mantiene la lista de resultados y el expediente seleccionado en memoria de vista sin ensuciar la sesión global. |
| **`@SessionScoped`** | Vive durante **toda la sesión HTTP del usuario** (desde que hace login hasta que cierra sesión o expira el timeout) y se comparte entre todas las pestañas del navegador. | Usar **exclusivamente** para datos globales ligeros del usuario autenticado (`UsuarioSesionBean`: login, rol, municipio activo, preferencias de idioma). **Nunca guardar listas de expedientes pesadas aquí**, o saturarás la memoria Heap del servidor. |
| **`@ApplicationScoped`** | Una única instancia (*Singleton*) compartida por todos los usuarios mientras el servidor esté encendido. | Para servicios sin estado (`ExpedienteService`, `JasperReportGeneratorService`) o cachés de catálogos estáticos (lista de provincias, tipos de cultivo SIGPAC). |

---

## 4. AJAX PARCIAL EN JSF ESTÁNDAR (`<f:ajax>`) vs. PRIMEFACES (`process` / `update`)

| Acción | En JSF Estándar (`<f:ajax>`) | En PrimeFaces (`<p:commandButton>` / `<p:ajax>`) |
| :--- | :--- | :--- |
| **Qué componentes se envían y validan en el servidor** (Fases 2, 3 y 4) | Atributo **`execute`** (ej. `execute="@form"` o `execute="gridFiltros @this"`) | Atributo **`process`** (por defecto `@form` en `p:commandButton`) |
| **Qué componentes se repintan en el navegador** (Fase 6) | Atributo **`render`** (ej. `render="tablaExpedientes mensajesGlobales"`) | Atributo **`update`** (ej. `update=":formBandejaExpedientes:tablaExpedientes"`) |

---

## 5. LAS 15 PREGUNTAS TÉCNICAS DE ENTREVISTA JSF / PRIMEFACES (CON RESPUESTAS LISTAS PARA DECIR EN VOZ ALTA)

1. **¿Cuál es la diferencia entre `@ManagedBean` (`javax.faces.bean`) y `@Named` (`javax.inject`)?**
   > "`@ManagedBean` era el mecanismo antiguo de JSF 2.0 y está *deprecated* desde JSF 2.3. Hoy siempre usamos **`@Named`** de CDI junto con `@ViewScoped` de `javax.faces.view.ViewScoped` para integrar los Backing Beans con el contenedor CDI de Jakarta EE e inyectar servicios con `@Inject`."
2. **¿Por qué nunca debes hacer consultas SQL dentro de un método `getter` de un Bean JSF?**
   > "Porque JSF invoca los `getters` múltiples veces durante el ciclo de vida y el renderizado del árbol de componentes. Si pones una consulta SQL en `getListaExpedientes()`, se ejecutará varias veces por cada petición. La consulta debe hacerse una sola vez en `@PostConstruct` o en el método de acción del botón Buscar."
3. **¿Por qué todo Bean `@ViewScoped` o `@SessionScoped` debe implementar `Serializable`?**
   > "Porque el servidor de aplicaciones (WildFly/JBoss o Tomcat) puede necesitar serializar el estado de la vista o de la sesión a disco (pasivación) o replicarlo en un clúster. Si no implementa `Serializable`, el despliegue falla o lanza `NotSerializableException`."
4. **¿Qué diferencia hay entre Expression Language inmediato `${...}` y diferido `#{...}` en JSF?**
   > "`#{bean.propiedad}` es evaluación diferida (*Deferred EL*): funciona en ambos sentidos, permitiendo a JSF **leer** el valor con el `getter` en la Fase 6 (*Render Response*) y **escribir** el valor con el `setter` en la Fase 4 (*Update Model Values*). En cambio `${...}` es evaluación inmediata de solo lectura heredada de JSP."
5. **¿Para qué sirven los `Converters` y `Validators` en JSF y en qué fase se ejecutan?**
   > "Se ejecutan en la **Fase 3 (*Process Validations*)**. El `Converter` transforma el `String` del formulario HTML en un objeto Java (`LocalDate`, `BigDecimal`, o una entidad JPA mediante `getAsObject`/`getAsString`), y el `Validator` comprueba que ese objeto cumpla las reglas de negocio antes de tocar el modelo."
6. **¿Para qué sirve `immediate="true"` en un botón Cancelar de un formulario JSF?**
   > "Hace que la acción del botón se ejecute al final de la Fase 2 (*Apply Request Values*) y salte directamente a la Fase 6 (*Render Response*), evitando que la Fase 3 (*Process Validations*) bloquee el cierre del formulario por culpa de campos obligatorios (`required="true"`) vacíos."
7. **¿Por qué el botón que descarga un PDF de Jasper Reports necesita `ajax="false"` y `facesContext.responseComplete()`?**
   > "`ajax="false"` es necesario porque una respuesta AJAX de JSF devuelve un XML `<partial-response>` que no puede abrir directamente un archivo binario `application/pdf` en el navegador; y `facesContext.responseComplete()` le dice a JSF en la Fase 5 que ya hemos escrito los bytes del PDF en el `HttpServletResponse` para que no ejecute la Fase 6 ni corrompa el flujo binario."
8. **¿Qué diferencia hay entre `action` y `actionListener` en un `<h:commandButton>` o `<p:commandButton>`?**
   > "`actionListener` está pensado para lógica de interfaz previa (por ejemplo, recibir un evento o fijar qué fila de la tabla se ha seleccionado antes de abrir un diálogo modal) y siempre devuelve `void`. `action` ejecuta la operación principal de negocio y puede devolver un `String` con la regla de navegación hacia otra página (o `null`/`void` para permanecer en la misma vista)."
9. **¿Por qué en PrimeFaces no se deben anidar un `<h:form>` dentro de otro `<h:form>`, especialmente al usar `<p:dialog>`?**
   > "El estándar HTML prohíbe formularios `<form>` anidados y en JSF corrompe el campo oculto `javax.faces.ViewState` haciendo que los botones del diálogo dejen de funcionar. La buena práctica es colocar el `<p:dialog>` fuera del formulario de la tabla principal y darle su propio `<h:form id="formDialogoEdicion">` independiente."
10. **¿Cómo actualizas desde el formulario del `<p:dialog>` la tabla que está en otro `<h:form>` distinto?**
    > "Usando una ruta absoluta de cliente precedida por dos puntos (`:`) en el atributo `update` de PrimeFaces, por ejemplo: `update=":formBandejaExpedientes:tablaExpedientes :formBandejaExpedientes:mensajesGlobales"`."
11. **¿Cómo evitas que el `<p:dialog>` se cierre en el navegador si ha fallado la validación de un campo obligatorio en el servidor?**
    > "PrimeFaces inyecta automáticamente el argumento `args.validationFailed` en el callback JavaScript `oncomplete`. Escribiendo `oncomplete="if (!args.validationFailed) PF('widgetDialogoExpediente').hide();"` el diálogo permanece abierto mostrando los errores si la Fase 3 falló, y se cierra limpiamente si todo fue válido."
12. **¿Qué diferencia hay entre `rendered="#{...}"` en JSF y ocultar un elemento con CSS `display: none`?**
    > "Con `rendered="false"`, JSF **ni siquiera genera el HTML de ese componente en el servidor** ni procesa sus valores en un postback (lo cual es mucho más seguro para ocultar botones como el de Aprobar o Emitir Certificado si el expediente no está aprobado). Eso sí, para poder mostrar luego por AJAX un componente que tenía `rendered="false"`, hay que hacer `update` sobre su contenedor padre (`<h:panelGroup>`)."
13. **¿Qué es el sistema de plantillas Facelets (`<ui:composition>`, `<ui:insert>`, `<ui:define>`)?**
    > "Es el motor de maquetación nativo de JSF que sustituyó a JSP. Permite definir una plantilla maestra (`template.xhtml`) con la cabecera institucional, menú lateral y pie de página usando `<ui:insert name="contenido"/>`, mientras cada pantalla funcional usa `<ui:composition template="/WEB-INF/template.xhtml">` y `<ui:define name="contenido">` sin repetir código HTML."
14. **¿Qué es `ViewState` (`javax.faces.ViewState`) y qué es una `ViewExpiredException`?**
    > "El `ViewState` almacena el estado del árbol de componentes de la vista entre peticiones. Si el administrativo deja la pantalla abierta sin tocarla hasta que caduca su sesión HTTP y luego pulsa un botón AJAX, el servidor ya no encuentra ese `ViewState` y lanza `ViewExpiredException`, que capturamos con un `ExceptionHandler` para redirigirle amablemente a la página de inicio."
15. **¿Cuándo usarías `LazyDataModel<T>` en un `<p:dataTable>` de PrimeFaces?**
    > "Cuando la consulta puede devolver decenas de miles o millones de registros (como todo el censo SIGPAC de una provincia). Con `LazyDataModel` y `lazy="true"`, PrimeFaces pasa al método `load(first, pageSize, sortBy, filterBy)` únicamente la página actual, delegando la paginación y el filtrado en un `SELECT ... LIMIT pageSize OFFSET first` + `SELECT COUNT(*)` en base de datos."

---
## ARCHIVO: ExpedienteManagedBean.java

```java
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
```

---
## ARCHIVO: gestion_expedientes_agricolas.xhtml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!--
  ARCHIVO: gestion_expedientes_agricolas.xhtml
  PROYECTO: Gestión Administrativa, Catastral y de Parcelas Rústicas — Ayuntamiento de Roperuelos del Páramo
  TECNOLOGÍA: JSF 2.3 (Facelets) + PrimeFaces
  AUTOR: Diego de la Fuente Alonso
-->
<!DOCTYPE html>
<!-- Declaración de espacios de nombres XML (Namespaces) obligatorios en JSF y PrimeFaces:
     xmlns:h  -> Componentes HTML estándar de JSF (formularios, inputs, combos, botones, textos)
     xmlns:f  -> Núcleo de JSF (conversores, validadores, selectItems, etiquetas f:ajax)
     xmlns:ui -> Plantillas Facelets (composiciones, fragmentos, iteraciones)
     xmlns:p  -> Biblioteca de componentes ricos PrimeFaces (p:dataTable, p:dialog, p:growl) -->
<html xmlns="http://www.w3.org/1999/xhtml"
      xmlns:h="http://xmlns.jcp.org/jsf/html"
      xmlns:f="http://xmlns.jcp.org/jsf/core"
      xmlns:ui="http://xmlns.jcp.org/jsf/facelets"
      xmlns:p="http://primefaces.org/ui"
      lang="es">

<!-- <h:head> es obligatorio en lugar de <head> plano para que JSF y PrimeFaces inyecten automáticamente
     sus hojas de estilo CSS y librerías JavaScript (jQuery / PrimeFaces AJAX engine) -->
<h:head>
    <meta charset="UTF-8" />
    <title>Gestión de Expedientes Agrarios y Certificados Catastrales — Ayto. de Roperuelos del Páramo</title>
</h:head>

<h:body style="font-family: Arial, sans-serif; margin: 20px; background-color: #f8fafc;">

    <!-- =====================================================================
         FORMULARIO PRINCIPAL DE BÚSQUEDA Y LISTADO PAGINADO (<h:form>)
         Todo componente interactivo en JSF debe ir dentro de un <h:form> que
         gestiona automáticamente el campo oculto javax.faces.ViewState.
         ===================================================================== -->
    <h:form id="formBandejaExpedientes">

        <!-- <p:growl> muestra notificaciones flotantes con los FacesMessage añadidos desde ExpedienteManagedBean -->
        <p:growl id="mensajesGlobales" showDetail="true" life="4500" />

        <!-- Cabecera institucional de la pantalla -->
        <p:panel header="Ayuntamiento de Roperuelos del Páramo — Gestión de Expedientes Agrarios, Catastro Rústico y Emisión de Certificados"
                 style="margin-bottom: 16px;">

            <!-- 1. PANEL DE FILTROS CON COMPONENTES JSF ESTÁNDAR (h:inputText, h:selectOneMenu, h:commandButton + f:ajax) -->
            <h:panelGrid id="gridFiltros" columns="6" cellpadding="6" style="width: 100%;">

                <!-- Filtro 1: Año de Campaña Agrícola con conversor numérico -->
                <h:outputLabel for="txtCampania" value="Campaña Agrícola:" style="font-weight: bold;" />
                <h:inputText id="txtCampania"
                             value="#{expedienteManagedBean.filtroCampania}"
                             label="Campaña Agrícola"
                             maxlength="4"
                             style="width: 90px;">
                    <!-- Validador estándar JSF en Fase 3 (Process Validations) -->
                    <f:validateLongRange minimum="2020" maximum="2035" />
                </h:inputText>

                <!-- Filtro 2: NIF / CIF del Agricultor o Titular Catastral -->
                <h:outputLabel for="txtNif" value="NIF / CIF Titular:" style="font-weight: bold;" />
                <h:inputText id="txtNif"
                             value="#{expedienteManagedBean.filtroNifTitular}"
                             label="NIF/CIF del Titular"
                             maxlength="15"
                             style="width: 150px;" />

                <!-- Filtro 3: Desplegable (<h:selectOneMenu>) enlazado al Enum EstadoExpediente -->
                <h:outputLabel for="selEstado" value="Estado Expediente:" style="font-weight: bold;" />
                <h:selectOneMenu id="selEstado"
                                 value="#{expedienteManagedBean.filtroEstado}"
                                 style="width: 210px;">
                    <!-- Opción por defecto nula ("Todos los estados") -->
                    <f:selectItem itemLabel="-- Todos los estados --" itemValue="#{null}" noSelectionOption="true" />
                    <!-- Carga dinámica de los valores del Enum desde el Managed Bean -->
                    <f:selectItems value="#{expedienteManagedBean.estadosDisponibles}"
                                   var="est"
                                   itemLabel="#{est}"
                                   itemValue="#{est}" />
                </h:selectOneMenu>

            </h:panelGrid>

            <!-- Botonera de filtrado usando tanto JSF estándar con <f:ajax> como PrimeFaces -->
            <div style="margin-top: 10px; display: flex; gap: 10px;">
                <!-- <h:commandButton> con <f:ajax>:
                     execute="gridFiltros @this" -> envía y valida únicamente los 3 campos de filtro en Fases 2-4.
                     render="tablaExpedientes mensajesGlobales" -> repinta solo la tabla y los mensajes en Fase 6. -->
                <h:commandButton id="btnBuscar"
                                 value="Buscar Expedientes (JSF AJAX)"
                                 action="#{expedienteManagedBean.buscarExpedientes()}"
                                 style="padding: 6px 14px; font-weight: bold; cursor: pointer;">
                    <f:ajax execute="gridFiltros @this" render="tablaExpedientes mensajesGlobales" />
                </h:commandButton>

                <!-- Botón para limpiar criterios -->
                <h:commandButton id="btnLimpiar"
                                 value="Limpiar Filtros"
                                 action="#{expedienteManagedBean.limpiarFiltros()}"
                                 style="padding: 6px 14px; cursor: pointer;">
                    <f:ajax execute="@this" render="gridFiltros tablaExpedientes mensajesGlobales" />
                </h:commandButton>
            </div>
        </p:panel>

        <!-- =================================================================
             2. TABLA RICA DE PRIMEFACES (<p:dataTable>) CON PAGINACIÓN,
                ORDENACIÓN, FILTRADO POR COLUMNA Y DESCARGA PDF JASPER REPORTS
             ================================================================= -->
        <p:dataTable id="tablaExpedientes"
                     var="exp"
                     value="#{expedienteManagedBean.listaExpedientes}"
                     rowKey="#{exp.id}"
                     paginator="true"
                     rows="10"
                     paginatorPosition="bottom"
                     rowsPerPageTemplate="5,10,25,50"
                     emptyMessage="No se han encontrado expedientes agrarios para los criterios seleccionados."
                     stripedRows="true">

            <!-- Columna 1: Código Oficial del Expediente con ordenación y filtro integrado -->
            <p:column headerText="Código Expediente"
                      sortBy="#{exp.codigoExpediente}"
                      filterBy="#{exp.codigoExpediente}"
                      filterMatchMode="contains"
                      style="width: 160px; font-weight: bold;">
                <h:outputText value="#{exp.codigoExpediente}" />
            </p:column>

            <!-- Columna 2: Campaña Agrícola -->
            <p:column headerText="Campaña"
                      sortBy="#{exp.campaniaAgricola}"
                      style="width: 85px; text-align: center;">
                <h:outputText value="#{exp.campaniaAgricola}" />
            </p:column>

            <!-- Columna 3: NIF/CIF del Titular (cargado sin N+1 gracias al JOIN FETCH del repositorio) -->
            <p:column headerText="NIF / CIF"
                      sortBy="#{exp.titular.nifCif}"
                      filterBy="#{exp.titular.nifCif}"
                      filterMatchMode="contains"
                      style="width: 115px;">
                <h:outputText value="#{exp.titular.nifCif}" />
            </p:column>

            <!-- Columna 4: Nombre completo del Agricultor / Titular Catastral -->
            <p:column headerText="Titular Agrario / Solicitante"
                      sortBy="#{exp.titular.nombreCompleto}"
                      filterBy="#{exp.titular.nombreCompleto}"
                      filterMatchMode="contains">
                <h:outputText value="#{exp.titular.nombreCompleto}" />
            </p:column>

            <!-- Columna 5: Superficie Total Declarada (ha) formateada a 4 decimales exactos con <f:convertNumber> -->
            <p:column headerText="Superficie (ha)"
                      sortBy="#{exp.superficieTotalDeclaradaHa}"
                      style="width: 130px; text-align: right;">
                <h:outputText value="#{exp.superficieTotalDeclaradaHa}">
                    <f:convertNumber pattern="#,##0.0000" locale="es_ES" />
                </h:outputText>
                <h:outputText value=" ha" />
            </p:column>

            <!-- Columna 6: Importe Económico (EUR) formateado como moneda -->
            <p:column headerText="Importe (€)"
                      sortBy="#{exp.importeEconomicoEur}"
                      style="width: 120px; text-align: right;">
                <h:outputText value="#{exp.importeEconomicoEur}">
                    <f:convertNumber type="currency" currencySymbol="€" locale="es_ES" />
                </h:outputText>
            </p:column>

            <!-- Columna 7: Estado del Expediente -->
            <p:column headerText="Estado"
                      sortBy="#{exp.estado}"
                      style="width: 150px; text-align: center;">
                <h:outputText value="#{exp.estado}" style="font-weight: bold;" />
            </p:column>

            <!-- Columna 8: Acciones (Abrir Diálogo de Revisión/Aprobación + Descargar Certificado PDF de Jasper Reports) -->
            <p:column headerText="Acciones y Jasper Reports" style="width: 260px; text-align: center;">

                <!-- Botón 1: Abre el diálogo modal p:dialog mediante petición AJAX parcial -->
                <p:commandButton value="Revisar / Editar"
                                 icon="pi pi-pencil"
                                 actionListener="#{expedienteManagedBean.prepararEdicionModal(exp)}"
                                 process="@this"
                                 update=":formDialogoEdicion:panelContenidoModal"
                                 oncomplete="PF('widgetDialogoExpediente').show()"
                                 style="margin-right: 6px;" />

                <!-- Botón 2: Descarga el Certificado Oficial PDF generado con Jasper Reports.
                     ¡MUY IMPORTANTE EN ENTREVISTA!: Lleva ajax="false" porque devuelve un stream binario
                     application/pdf directo al navegador invocando facesContext.responseComplete(). -->
                <p:commandButton value="PDF Jasper"
                                 icon="pi pi-file-pdf"
                                 ajax="false"
                                 rendered="#{exp.estado eq 'APROBADO'}"
                                 action="#{expedienteManagedBean.descargarCertificadoPdfJasper(exp)}"
                                 title="Emitir y descargar Certificado Municipal de Parcelas Rústicas en PDF" />

            </p:column>

        </p:dataTable>

    </h:form>

    <!-- =====================================================================
         3. DIÁLOGO MODAL DE REVISIÓN Y APROBACIÓN (<p:dialog>)
            Se coloca en su propio <h:form> independiente (buena práctica en
            PrimeFaces para evitar formularios anidados y aislar validaciones).
         ===================================================================== -->
    <p:dialog id="dialogoEdicionExpediente"
              header="Revisión Técnica y Resolución de Expediente Agrario"
              widgetVar="widgetDialogoExpediente"
              modal="true"
              resizable="false"
              closable="true"
              width="620">

        <h:form id="formDialogoEdicion">
            <h:panelGroup id="panelContenidoModal">

                <!-- Solo se renderiza el interior si hay un expediente seleccionado en el Bean @ViewScoped -->
                <h:panelGrid columns="2" cellpadding="8" style="width: 100%;"
                             rendered="#{not empty expedienteManagedBean.expedienteSeleccionado}">

                    <h:outputLabel value="Código de Expediente:" style="font-weight: bold;" />
                    <h:outputText value="#{expedienteManagedBean.expedienteSeleccionado.codigoExpediente}" />

                    <h:outputLabel value="Titular Solicitante:" style="font-weight: bold;" />
                    <h:outputText value="#{expedienteManagedBean.expedienteSeleccionado.titular.nombreCompleto} (#{expedienteManagedBean.expedienteSeleccionado.titular.nifCif})" />

                    <h:outputLabel value="Superficie Total Computada:" style="font-weight: bold;" />
                    <h:outputText value="#{expedienteManagedBean.expedienteSeleccionado.superficieTotalDeclaradaHa} ha" />

                    <h:outputLabel value="Estado Actual:" style="font-weight: bold;" />
                    <h:outputText value="#{expedienteManagedBean.expedienteSeleccionado.estado}" />

                    <h:outputLabel for="txtObs" value="Informe / Observaciones Secretaría:" style="font-weight: bold;" />
                    <h:inputTextarea id="txtObs"
                                     value="#{expedienteManagedBean.observacionesAprobacion}"
                                     rows="4"
                                     cols="45"
                                     required="true"
                                     requiredMessage="Debe indicar las observaciones técnicas o de secretaría antes de guardar o aprobar." />
                </h:panelGrid>

                <!-- Botonera del Diálogo Modal -->
                <div style="margin-top: 14px; text-align: right;">
                    <!-- Guardar observaciones manteniendo el estado actual -->
                    <p:commandButton value="Guardar Observaciones"
                                     icon="pi pi-save"
                                     actionListener="#{expedienteManagedBean.guardarCambiosModal()}"
                                     process="@form"
                                     update=":formBandejaExpedientes:tablaExpedientes :formBandejaExpedientes:mensajesGlobales"
                                     oncomplete="if (!args.validationFailed) PF('widgetDialogoExpediente').hide();"
                                     style="margin-right: 8px;" />

                    <!-- Aprobar oficialmente el expediente para habilitar el botón PDF de Jasper Reports -->
                    <p:commandButton value="Aprobar Expediente y Habilitar Certificado"
                                     icon="pi pi-check"
                                     actionListener="#{expedienteManagedBean.aprobarExpedienteSeleccionado()}"
                                     process="@form"
                                     update=":formBandejaExpedientes:tablaExpedientes :formBandejaExpedientes:mensajesGlobales"
                                     oncomplete="if (!args.validationFailed) PF('widgetDialogoExpediente').hide();"
                                     style="margin-right: 8px;" />

                    <!-- Botón Cancelar con immediate="true" para cerrar el modal sin disparar validaciones de campos requeridos -->
                    <p:commandButton value="Cancelar"
                                     icon="pi pi-times"
                                     immediate="true"
                                     onclick="PF('widgetDialogoExpediente').hide(); return false;" />
                </div>

            </h:panelGroup>
        </h:form>
    </p:dialog>

</h:body>
</html>
```

