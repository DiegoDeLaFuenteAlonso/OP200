
Esta guía de preparación está construida **exactamente sobre lo que ya les entregaste** (tu CV, tu carta de presentación y tus respuestas del formulario) y sobre el **proyecto real que tiene Seresco en su sede de Valladolid**.

---

## 1. Información Privilegiada: ¿Qué hace exactamente Seresco en Valladolid?
Si en la entrevista demuestras que sabes qué hacen en Valladolid, ganarás muchísimos puntos frente al resto de candidatos:
1. **Sector Agricultura / Cartografía / PAC y Administración Pública:** En la oferta pone *"Se valorará experiencia, adecuación y capacitación en proyectos de agricultura"*. Esto se debe a que el centro de **Seresco en Valladolid** trabaja estrechamente con la **Junta de Castilla y León (Consejería de Agricultura, Ganadería y Desarrollo Rural / ITACyL)**, el **FEGA / SIGPAC** y su propia plataforma de agricultura de precisión (**Cultiva Decisiones**).
2. **Por qué piden `Java JEE + SQL + JSF + Jasper Reports`:** Es el stack estándar de las aplicaciones de gestión agraria, ayudas de la PAC, registros de explotaciones y expedientes de la Junta de Castilla y León:
   - **Backend:** Java / Jakarta EE (JEE) o Spring, atacando bases de datos relacionales con **SQL** complejo.
   - **Frontend institucional:** **JSF (JavaServer Faces / PrimeFaces)** para formularios complejos de expedientes, tablas con filtros y validaciones.
   - **Documentación oficial:** **Jasper Reports** para generar los PDFs oficiales (resoluciones, certificados, informes de inspección, solicitudes firmadas).

---

## 2. Tu "Pitch" Inicial de 90 Segundos («Háblame de ti»)
Cuando te digan *«Cuéntanos quién eres y tu experiencia»*, sigue el orden exacto del CV y la carta que entregaste:

> *"Soy desarrollador de software y datos residente aquí en Valladolid. Tengo una base técnica muy enfocada en programación porque cursé los dos Grados Superiores de desarrollo (**DAM y DAW**) en el IES San Andrés y después el **Curso de Especialización en Inteligencia Artificial y Big Data**.*
>
> *A nivel profesional, mi experiencia combina el desarrollo web en **Java y bases de datos SQL** con entornos empresariales:*
> 1. *Por un lado, trabajé durante dos etapas en el **Ayuntamiento de Roperuelos del Páramo** (en una zona eminentemente agrícola del Páramo leonés), donde desarrollé aplicaciones web con **Java (Spring Boot / entorno JEE)**, consultas **SQL** y generación de informes y listados para la gestión de expedientes y registros municipales.*
> 2. *Después pasé por **Craftelier** trabajando con **.NET/C# y SQL Server (SSMS)**, y por **FDS (del grupo DXC Technology)**, donde adquirí mucha disciplina de consultoría gestionando evolutivos, correctivos y el paso riguroso entre entornos de **Desarrollo, Calidad y Producción (DEV, QAS, PRD)**.*
> 3. *Actualmente estoy en **HORSE Technologies** aquí en Valladolid desarrollando servicios backend, automatizaciones y procesos de datos con **Python, Go y SQL**.*
>
> *Me presenté a esta vacante de Seresco porque busco un proyecto estable y a largo plazo en Valladolid volviendo a centrarme en el ecosistema **Java y SQL**, y además el horario continuo de 8:00 a 15:00 y la modalidad híbrida encajan al 100% con lo que busco."*

---

## 3. Cómo Defender tus Respuestas del Formulario y cada Punto de tu CV

### A. Tu experiencia en el Ayuntamiento de Roperuelos del Páramo (Tu arma secreta para esta entrevista)
En tu CV y carta destacaste que desarrollaste servicios web y plataformas administrativas con **Java, Spring Boot y SQL** en el Ayuntamiento de Roperuelos del Páramo.
- **Qué te van a preguntar:** *«Cuéntanos qué hiciste exactamente con Java y SQL en el Ayuntamiento y cómo se relaciona con proyectos de agricultura o administración pública»*.
- **Qué debes responder:**
  > *"Roperuelos del Páramo es un municipio agrícola de León donde gran parte de la gestión municipal gira en torno al censo, parcelas rústicas, aguas/comunidades de regantes, licencias y expedientes administrativos. Desarrollé y mantuve servicios web en **Java (con Spring Boot, Spring Data JPA / Hibernate y MVC)** conectados a bases de datos relacionales **SQL (PostgreSQL / MySQL)**.*
  > *Mi trabajo consistía en crear los formularios de alta y consulta de expedientes, validar los datos en el backend, optimizar las consultas SQL para cruzar titulares con registros y generar los informes y documentos en PDF (usando plantillas tipo **Jasper Reports**). Por eso conozco muy bien la lógica de expedientes, estados administrativos y datos del medio rural."*

### B. Preguntas técnicas sobre `JSF (JavaServer Faces)` vs `Spring Boot / MVC`
En tu primer CV pusiste **Spring Boot / Spring MVC / Spring Data JPA**, y la oferta menciona **Java, SQL, JSF y Jasper Reports**.
- **Qué te pueden preguntar:** *«Vemos que has usado sobre todo Spring Boot. ¿Has tocado JSF (JavaServer Faces / PrimeFaces) o aplicaciones Java EE clásicas?»*
- **Qué debes responder (honesto y técnico):**
  > *"Mi experiencia más reciente en proyectos y en DAW ha sido con **Java y Spring Boot (Spring MVC + JPA/Hibernate)**, pero conozco perfectamente la arquitectura **Java EE / Jakarta EE y JSF**: sé cómo funciona el ciclo de vida de una vista XHTML/Facelets conectada a un **Managed Bean / CDI Bean** (`@ViewScoped`, `@RequestScoped`), el enlace de datos bidireccional con Expression Language (`#{bean.propiedad}`), las etiquetas de componentes (como `h:dataTable`, `f:ajax` o componentes de **PrimeFaces**) y cómo el Bean invoca a la capa de servicio y al DAO/Repositorio JPA. Al dominar Java, POO, Servlets/JSP y JPA, adaptarme al 100% a JSF me lleva días."*

### C. Preguntas técnicas sobre `Jasper Reports`
- **Qué te pueden preguntar:** *«¿Cómo funciona o cómo has trabajado con Jasper Reports?»*
- **Qué debes responder:**
  > *"Sé cómo es el flujo completo de **Jasper Reports**: se diseña la plantilla visual en **Jaspersoft Studio** (que genera un fichero XML llamado **`.jrxml`** con sus bandas: *Title, Page Header, Column Header, Detail, Summary*), se definen los parámetros (`$P{...}`) y los campos (`$F{...}`) que vienen o bien de una consulta **SQL** directa o de una colección de objetos Java (`JRBeanCollectionDataSource`), se compila a **`.jasper`** y desde Java se rellena con `JasperFillManager.fillReport(...)` y se exporta a PDF o Excel con `JasperExportManager`."*

### D. Preguntas técnicas de `Java y SQL` (Nivel 1–2 años)
Prepárate estas 5 preguntas cortas que siempre caen en entrevistas técnicas de Seresco:
1. **Diferencia entre `INNER JOIN` y `LEFT JOIN` en SQL:**
   - *Respuesta:* "`INNER JOIN` devuelve solo las filas que tienen coincidencia en ambas tablas; `LEFT JOIN` devuelve todas las filas de la tabla izquierda aunque no tengan correspondencia en la derecha (rellenando con `NULL`), muy útil por ejemplo para sacar todos los titulares o expedientes aunque aún no tengan documentos o pagos asociados."
2. **¿Cómo optimizas una consulta SQL que va lenta?**
   - *Respuesta:* "Primero miro el plan de ejecución (`EXPLAIN`), reviso que las columnas usadas en los `JOIN` y en el `WHERE` tengan **índices**, evito el `SELECT *` trayendo solo las columnas necesarias, evito funciones sobre columnas indexadas en el `WHERE` y sustituyo subconsultas correlacionadas por `JOIN` o CTEs."
3. **¿Qué es JPA / Hibernate y el problema de las `N+1 queries`?**
   - *Respuesta:* "JPA es la especificación de persistencia en Java e Hibernate es la implementación ORM. El problema `N+1` ocurre cuando cargas una lista de entidades padre (1 consulta) y al recorrer una relación `LAZY` hace 1 consulta adicional por cada fila ($N$ consultas). Se soluciona usando `JOIN FETCH` en JPQL o `@EntityGraph`."
4. **¿Cómo trabajabas el paso entre entornos en FDS (DXC Technology) y HORSE?**
   - *Respuesta:* "Trabajábamos con tres entornos separados: **Desarrollo (DEV)** donde programábamos y hacíamos pruebas unitarias, **Calidad/Preproducción (QAS)** donde se validaba con datos de prueba y pruebas de integración, y **Producción (PRD)**, manteniendo siempre trazabilidad con Git y órdenes de transporte para poder hacer *rollback* si algo fallaba."

---

## 4. Las Preguntas de RRHH y Condiciones (Basadas en tus Respuestas del Formulario)

### 1. «¿Por qué quieres cambiar de HORSE Technologies a Seresco si entraste en julio?»
- **Respuesta ganadora:**
  > *"En HORSE Technologies estoy muy agradecido y he aprendido muchísimo automatizando procesos de datos con Python, Go y BigQuery, pero mi vocación principal es el **desarrollo de software e ingeniería de aplicaciones en Java y SQL**. Cuando vi que Seresco abría esta posición estable en Valladolid en el Área Técnica de Producción de Software, con contrato indefinido, horario continuo de 8:00 a 15:00 y modelo híbrido, supe que era el sitio donde quería consolidar mi carrera como desarrollador Java a largo plazo."*

### 2. «¿Cuáles son tus expectativas salariales?»
*(En tu formulario anterior de `seresco-java-spring` tenías anotado 26k–32k y en el de hoy 23k–27k)*.
- **Cómo responder en vivo para no quedarte corto ni pasarte de la banda de 1 año en Valladolid:**
  > *"Busco ante todo un proyecto estable en Valladolid donde crecer técnicamente. Me muevo en una horquilla orientativa de entre **24.000 € y 28.000 € brutos anuales**, pero soy totalmente flexible para ajustarme a las tablas salariales de Seresco para este nivel en Valladolid y valoro muchísimo beneficios como la retribución flexible **Serflex** (seguro médico, tarjeta gourmet) y la jornada intensiva de 8:00 a 15:00 todo el año."*

### 3. «¿Cuál es tu disponibilidad de incorporación?»
- **Respuesta:**
  > *"Mi preaviso legal estándar es de **15 días naturales** desde la confirmación."*

---

## 5. Tres Preguntas Inteligentes para Hacerles Tú al Final de la Entrevista
Cuando te digan *«¿Tienes alguna pregunta para nosotros?»*, hazles estas dos o tres (les demostrarán que tienes interés real en su oficina de Valladolid):
1. *«En la oferta mencionáis que se valora la adecuación a proyectos de agricultura. ¿El equipo de Valladolid al que me incorporaría trabaja en proyectos para la administración agraria / PAC o en vuestra plataforma propia como Cultiva Decisiones?»*
2. *«A nivel técnico, ¿qué versiones de Java, servidor de aplicaciones (WildFly/JBoss, Tomcat) y motor de base de datos (Oracle, PostgreSQL, SQL Server) utilizáis actualmente en el proyecto?»*
3. *«¿Cómo se organiza el día a día del equipo en Valladolid entre los días presenciales y el 50% de teletrabajo?»*

Sí, te aconsejé poner exactamente esto en la casilla de **«¿Cuáles son tus expectativas económicas?»** del formulario de Seresco:

> **`Entre 23.000 € y 27.000 € brutos anuales, totalmente flexible y negociable según las tablas salariales de Seresco en Valladolid y el programa de retribución flexible Serflex.`**

*(Y si en la sesión anterior habías puesto el otro texto que tenías guardado en la carpeta antigua `seresco-java-spring`, aquel decía **`26.000 € – 32.000 € brutos/año`**).*

### ¿Por qué te aconsejé la horquilla de `23.000 € – 27.000 €` (y qué decir en la entrevista)?
- Porque para un puesto en **Valladolid** que pide **1 año de experiencia** en consultoría TIC (como Seresco), la banda real de mercado suele estar entre **22.000 € y 26.000 € brutos/año**.
- Si en la entrevista te preguntan *«Vimos lo que pusiste en el formulario, ¿esa sigue siendo tu expectativa?»*, mantenlo alineado diciendo:
  > *"Sí, indiqué esa horquilla orientativa de **23.000 € a 27.000 € brutos anuales** (o **26.000 €** si enviaste el primero), pero como comenté en el formulario, para mí la prioridad es incorporarme de forma estable al equipo de Seresco en Valladolid, así que me adapto sin problema a la banda salarial que tengáis estipulada para el puesto más el programa **Serflex**."*