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
