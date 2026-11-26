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
