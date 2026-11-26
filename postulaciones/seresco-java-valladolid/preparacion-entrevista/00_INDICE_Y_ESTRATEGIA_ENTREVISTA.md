# 00 — ÍNDICE MAESTRO Y ESTRATEGIA DE ENTREVISTA: SERESCO (VALLADOLID)

> **Candidato:** Diego de la Fuente Alonso  
> **Puesto:** Desarrollador/a Java (Perfil Desarrollador JEE) — Área Técnica de Producción de Software  
> **Ubicación y Modalidad:** Valladolid (Híbrido hasta 50% teletrabajo | Jornada continua L-V de 08:00 a 15:00h todo el año)  
> **Enlaces de referencia de la vacante:**  
> - Oferta oficial: https://empleo.seresco.es/desarrollador-a-java-valladolid-9E5tVln_-5yB/  
> - Portal Viterbit: https://seresco.viterbit.site/desarrollador-a-java-valladolid-9E5tVln_-5yB/  

---

## 1. MAPA DEL REPOSITORIO DE PREPARACIÓN

| Bloque | Carpeta / Archivo | Objetivo de Estudio |
| :--- | :--- | :--- |
| **00. Estrategia** | `00_INDICE_Y_ESTRATEGIA_ENTREVISTA.md` | Guiones palabra por palabra, defensa del CV, salario, cambio desde HORSE y 12 competencias blandas de Seresco. |
| **01. Java / JEE & Spring** | `01_java_jee_y_spring_boot/01_teoria_y_preguntas_entrevista_java_jee.md` | Equivalencias Jakarta EE (JEE) vs Spring Boot, POO, Colecciones, Streams, CDI/EJB, JPA/Hibernate, N+1, Transacciones y 15 preguntas de entrevista. |
| **01. Código Java** | `ExpedienteAgrarioEntity.java` / `ExpedienteRepository.java` / `ExpedienteService.java` | Código productivo comentado línea a línea (Entidad JPA, Repositorio con JPQL + SQL Nativo + JDBC `PreparedStatement`, Servicio transaccional). |
| **02. SQL & BBDD** | `02_sql_bases_de_datos/02_teoria_optimizacion_y_preguntas_sql.md` | Teoría avanzada de JOINs, `GROUP BY`/`HAVING`, CTEs, Funciones Ventana (`OVER`), Índices, Planes de ejecución, Triggers y ACID. |
| **02. Scripts SQL** | `esquema_catastro_y_parcelas_rusticas.sql` / `consultas_avanzadas_entrevista.sql` | Modelo relacional agrario/catastral completo (SIGPAC, polígonos, parcelas, titulares, expedientes) + 10 consultas de prueba técnica comentadas. |
| **03. JSF & PrimeFaces** | `03_jsf_javaserver_faces/03_arquitectura_ciclo_vida_y_preguntas_jsf.md` | Arquitectura `FacesServlet`, las 6 fases del ciclo de vida JSF, Scopes (`@RequestScoped`, `@ViewScoped`, `@SessionScoped`), AJAX y PrimeFaces. |
| **03. Código JSF** | `ExpedienteManagedBean.java` / `gestion_expedientes_agricolas.xhtml` | Controlador `@ViewScoped` y pantalla XHTML con JSF estándar (`h:`) y PrimeFaces (`p:dataTable`, `p:dialog`, descarga PDF Jasper). |
| **04. Jasper Reports** | `04_jasper_reports/04_flujo_jrxml_y_preguntas_jasper.md` | Flujo Jaspersoft Studio, estructura XML `.jrxml`, bandas, `$P{}`, `$F{}`, `$V{}`, compilación `.jasper` y orígenes JDBC vs `JRBeanCollectionDataSource`. |
| **04. Código Jasper** | `informe_parcelas_titular.jrxml` / `JasperReportGeneratorService.java` | Plantilla `.jrxml` oficial del Certificado Municipal de Parcelas Rústicas + Servicio Java de compilación, relleno y exportación a PDF. |
| **05. Caso de Éxito Real** | `05_proyecto_ayuntamiento_roperuelos_del_paramo/*` | Documentación arquitectónica, narrativa, código end-to-end integrado y las 15 repreguntas de tribunal sobre tu proyecto en el Ayuntamiento de Roperuelos del Páramo. |

---

## 2. RESUMEN EJECUTIVO: QUÉ TIENE EL ENTREVISTADOR DELANTE Y QUÉ BUSCA SERESCO EN VALLADOLID

### 2.1. El contexto real del centro de Seresco en Valladolid
En la oferta de Seresco figura explícitamente un requisito valorable muy específico:
> *"Se valorará experiencia, adecuación y capacitación, en proyectos de agricultura."*

¿Por qué piden exactamente **`JAVA` + `SQL` + `JSF` + `Jasper Reports` + `Agricultura`** en Valladolid?
1. **Clientes Institucionales Agroalimentarios y Medio Rural:** Desde su sede en Valladolid, Seresco desarrolla, evoluciona y mantiene aplicaciones críticas para la **Administración Pública autonómica y nacional** (como la **Consejería de Agricultura, Ganadería y Desarrollo Rural de la Junta de Castilla y León**, el **ITACyL** —Instituto Tecnológico Agrario de Castilla y León—, gestión de ayudas de la **PAC**, cruces con recintos **SIGPAC**, registros de explotaciones agrarias, cuadernos de campo digitales y su plataforma propia de agricultura de precisión **Cultiva Decisiones**).
2. **Arquitectura Tecnológica de estos Sistemas:**
   - **Backend Java EE / Jakarta EE o Spring:** Lógica de validación de expedientes, cálculo de superficies elegibles, cruces de recintos y reglas de negocio complejas.
   - **SQL Intenso:** Bases de datos relacionales con millones de registros de titulares, polígonos, parcelas, recintos, cultivos (secano/regadío) e históricos por campaña agrícola.
   - **Frontend Institucional en JSF (JavaServer Faces / PrimeFaces):** Pantallas de tramitación para funcionarios y técnicos agrarios con tablas paginadas (`p:dataTable`), filtros multicriterio, diálogos modales y validaciones AJAX parciales.
   - **Documentación Oficial en Jasper Reports:** Emisión masiva e individual de PDFs con validez administrativa (resoluciones de ayudas, certificados de titularidad catastral/rústica, actas de inspección, cartas de pago).

### 2.2. Coherencia total con los documentos que ya entregaste
En tu postulación a Seresco Valladolid (`seresco-java-valladolid`) entregaste una candidatura quirúrgicamente alineada con este stack (y en caso de que también vean tu versión previa `seresco-java-spring`, ambas cuentan la misma historia real sin ninguna contradicción):
- **Formación:** Doble Grado Superior en Informática (**DAM** 2022–2024 y **DAW** 2025–2026 en el IES San Andrés) + **Curso de Especialización en IA y Big Data** (2024–2025).
- **Ayuntamiento de Roperuelos del Páramo (Junio–Septiembre 2023 y Junio–Octubre 2024 | 9 meses acumulados en dos etapas):** Tu proyecto estrella para esta entrevista. Desarrollaste aplicaciones web con Java/JEE (JSF/JSP, Spring Boot, Hibernate/JPA y JDBC), bases de datos SQL (PostgreSQL y MySQL), APIs auxiliares en Python y módulos de generación automática de informes, certificados y listados en PDF con **Jasper Reports** para la gestión administrativa, catastral y de expedientes del ámbito rural y agrícola del municipio.
- **Craftelier (Marzo–Mayo 2024):** Desarrollo de software orientado a objetos (.NET/C# y Kotlin) y optimización de consultas SQL, vistas y reportes sobre **Microsoft SQL Server (SSMS)**.
- **FDS, a DXC Technology Company (Febrero–Junio 2026):** Consultoría técnica empresarial, lógica de negocio, consultas SQL de alto rendimiento, listados corporativos y disciplina rigurosa de paso entre entornos **DEV (Desarrollo) → QAS (Calidad) → PRD (Producción)**.
- **HORSE Technologies (Julio 2026–Actualidad | Valladolid):** Desarrollo de software, automatización backend (Python/Go), explotación de datos SQL (SQL Server, PostgreSQL, BigQuery) y reporting corporativo.

---

## 3. GUIONES PALABRA POR PALABRA PARA LA ENTREVISTA

### 3.1. Presentación Inicial de 90 Segundos («Háblame de ti / Cuéntanos tu trayectoria»)

> *"¡Hola! Muchas gracias por recibirme. Soy Diego de la Fuente, resido aquí en Valladolid capital y soy desarrollador de software especializado en entornos web con Java, bases de datos relacionales SQL y generación de informes.*
>
> *A nivel académico cuento con una base muy práctica en programación porque cursé la doble titulación superior en Informática en el IES San Andrés: primero **Desarrollo de Aplicaciones Multiplataforma (DAM)**, donde trabajé a fondo Java, JDBC, Hibernate, SQL y diseño de informes con **Jasper Reports**, después el **Curso de Especialización en IA y Big Data**, y finalmente **Desarrollo de Aplicaciones Web (DAW)**, profundizando en arquitecturas web Java/JEE, JSF, JSP, Spring Boot y despliegue en servidores de aplicaciones.*
>
> *En el plano profesional acumulo más de un año de experiencia combinando desarrollo web en el ámbito público/rural y consultoría tecnológica:*
> *1. Por un lado, trabajé durante dos etapas en el **Ayuntamiento de Roperuelos del Páramo**, un municipio eminentemente agrícola de la comarca del Páramo leonés. Allí desarrollé y evolucioné aplicaciones web internas con **Java (vistas en JSF/JSP y servicios en Spring Boot con Hibernate/JPA y JDBC)** sobre **PostgreSQL y MySQL**, e implementé la emisión automática de certificados e informes oficiales en PDF con **Jasper Reports** para la gestión de expedientes municipales, titulares y parcelas rústicas.*
> *2. Además, trabajé en **Craftelier** desarrollando software y optimizando consultas sobre **SQL Server**, y en **FDS (del grupo DXC Technology)**, donde adquirí una metodología muy sólida de producción de software empresarial, resolución de correctivos/evolutivos y gestión estricta del ciclo de despliegues entre entornos de **Desarrollo (DEV), Calidad (QAS) y Producción (PRD)**.*
> *3. Desde julio trabajo aquí en Valladolid en **HORSE Technologies**, donde desarrollo software, procesos de datos y consultas SQL complejas para reporting corporativo.*
>
> *En cuanto vi esta vacante de Seresco en Valladolid para el Área Técnica de Producción de Software, me identifiqué al 100%: tanto porque mi objetivo es consolidar mi carrera a largo plazo en el ecosistema **Java/JEE, SQL, JSF y Jasper Reports**, como porque ya conozco de primera mano la lógica de los proyectos de gestión territorial y agraria."*

---

### 3.2. Por qué cambio de HORSE Technologies a Seresco Valladolid (Si entré en julio de 2026)

Esta es la pregunta más importante de RRHH. Nunca hables mal de tu empresa actual; enfócalo como una **decisión vocacional hacia la ingeniería de software en Java/JEE y estabilidad a largo plazo en Seresco Valladolid**:

> *"En HORSE Technologies estoy muy contento con el trato y estoy aprendiendo mucho en la parte de ingeniería de datos, automatización con Python y Go y consultas analíticas en SQL y BigQuery. Sin embargo, mi verdadera vocación técnica —y para lo que me he formado con DAM y DAW y lo que más disfruté haciendo en el Ayuntamiento de Roperuelos del Páramo y en consultoría— es la **ingeniería y producción de software empresarial en Java y bases de datos relacionales SQL**.*
>
> *En HORSE mi rol actual tira cada vez más hacia la parte de datos y scripts en Python, mientras que yo quiero desarrollar mi carrera a largo plazo como **Desarrollador Java / JEE**. Además, Seresco es una compañía de referencia con un equipo técnico consolidado aquí en Valladolid, proyectos estables vinculados al sector público y agroalimentario que me resultan muy cercanos, y unas condiciones laborales (contrato indefinido, modelo híbrido en Valladolid y jornada continua de 8:00 a 15:00h todo el año) que encajan perfectamente con mi proyecto de vida en Valladolid."*

---

### 3.3. Defensa de Expectativas Salariales (23.000 € – 27.000 € + Serflex) y Disponibilidad (15 días)

En el formulario de Viterbit (`seresco-java-valladolid`) respondiste exactamente:
> `Entre 23.000 € y 27.000 € brutos anuales, totalmente flexible y negociable según las tablas salariales de Seresco en Valladolid y el programa de retribución flexible Serflex.`
*(Y si consultaran una inscripción previa de `seresco-java-spring`, figuraba `26.000 € – 32.000 €`).*

**Guion exacto si te preguntan «¿Cuáles son tus expectativas económicas?»:**

> *"En el formulario indiqué una horquilla orientativa de entre **23.000 € y 27.000 € brutos anuales** (moviéndome en torno a los **24.000 € – 26.000 €** según la responsabilidad del puesto). En cualquier caso, como reflejé en la solicitud, soy totalmente flexible para adaptarme a las tablas salariales que Seresco tenga establecidas en Valladolid para este perfil.*
>
> *Valoro el paquete en su conjunto: para mí el contrato indefinido, el programa de retribución flexible **Serflex** (especialmente el seguro médico y la tarjeta restaurante/Gourmet), el modelo híbrido al 50% en Valladolid y la jornada intensiva de 08:00 a 15:00h durante todo el año tienen un valor altísimo."*

**Guion exacto si te preguntan «¿Cuál es tu disponibilidad de incorporación?»:**

> *"Resido ya en Valladolid capital, por lo que no necesito ningún traslado. Mi disponibilidad es de **15 días naturales**, que es únicamente el preaviso legal estándar para dejar mi puesto actual de forma ordenada y profesional."*

---

### 3.4. Cómo defender la transición entre `Spring Boot` y `Java EE / JSF` (Si te preguntan en cuál tienes más mano)

Si el entrevistador técnico ve tus dos versiones de CV o te pregunta *«¿Has trabajado más con Spring Boot o con JSF / Java EE puro?»*, responde con total naturalidad técnica:

> *"En el Ayuntamiento de Roperuelos del Páramo convivían ambos mundos: teníamos módulos web clásicos con vistas **JSF (Facelets `.xhtml`) y JSP** apoyadas en Managed Beans, y en la segunda etapa modernizamos nuevos servicios backend con **Spring Boot y Spring Data JPA**.*
>
> *A nivel de arquitectura, pasar de uno a otro me resulta completamente natural porque los fundamentos son idénticos: donde en Spring tengo un `@RestController` o `@Controller` con `@Autowired`, en JSF/JEE tengo el `FacesServlet` enrutando hacia un `@Named` / `@ManagedBean` con `@ViewScoped` e inyección `@Inject`; y por debajo la capa de negocio transaccional, el ORM con **Hibernate/JPA**, las consultas **SQL** y la generación de PDFs con **`JasperFillManager` / `JasperExportManager`** funcionan exactamente igual."*

---

## 4. CONEXIÓN CON LAS 12 COMPETENCIAS BLANDAS DE LA OFERTA DE SERESCO

La oferta de Seresco en Viterbit lista explícitamente **12 competencias corporativas**. Aquí tienes cómo demostrar cada una con un ejemplo real de tu CV si RRHH te hace preguntas situacionales (método STAR):

| # | Competencia Seresco | Cómo la demuestras con tu experiencia real (Ejemplo STAR) |
| :-: | :--- | :--- |
| **1** | **Orientación al cliente** | En el **Ayuntamiento de Roperuelos del Páramo** me senté directamente con el secretario municipal y los administrativos para entender cómo emitían los certificados de parcelas rústicas y diseñé las pantallas JSF y las plantillas de Jasper Reports adaptadas a su flujo real de ventanilla. |
| **2** | **Flexibilidad** | He demostrado capacidad para adaptarme rápidamente a distintos stacks según las necesidades del proyecto: Java/JEE/Spring + SQL + Jasper en el Ayuntamiento, C#/.NET + SQL Server en Craftelier, entornos corporativos en FDS (DXC) y Python/Go/BigQuery en HORSE. |
| **3** | **Trabajo en equipo** | En **FDS (DXC Technology)** y **HORSE Technologies** trabajo integrado en equipos multidisciplinares usando Git (ramas feature, Pull Requests, revisiones de código) y metodologías ágiles (Scrum/Kanban). |
| **4** | **Orientación al logro** | En el Ayuntamiento logré reducir de **15-20 minutos** (búsqueda manual en Excel y copia a Word) a **menos de 3 segundos** la emisión de un Certificado Municipal de Parcelas Rústicas en PDF listo para firma electrónica. |
| **5** | **Innovación** | Además de dominar el stack clásico empresarial (Java, SQL, JSF, Jasper), cuento con el Curso de Especialización en IA y Big Data y experiencia automatizando validación y limpieza de datos catastrales. |
| **6** | **Comunicación** | Capacidad para traducir requisitos administrativos o agrarios (polígonos, parcelas, recintos, estados de expediente) a modelos de datos SQL y reglas de negocio en Java, comunicándome tanto con perfiles técnicos como con usuarios funcionales. |
| **7** | **Aprendizaje** | Cursé de forma consecutiva DAM, la Especialización en IA/Big Data y DAW mientras acumulaba experiencia laboral real, aprendiendo de forma autónoma librerías como JasperReports y PrimeFaces. |
| **8** | **Análisis** | Antes de escribir código o modificar una consulta SQL, analizo el modelo relacional, los casos borde (ej. titulares sin parcelas, parcelas en copropiedad, valores `NULL`) y el plan de ejecución (`EXPLAIN`). |
| **9** | **Orden y calidad** | En **FDS (DXC Technology)** interioricé el rigor del paso por entornos (**DEV → QAS → PRD**), separando configuración por entorno, documentando cada cambio y verificando pruebas unitarias e integrales antes de subir a Producción. |
| **10** | **Iniciativa** | Cuando en el Ayuntamiento de Roperuelos encontramos que los volcados catastrales en CSV venían con errores de codificación y NIFs mal formateados, propuse y construí un script/servicio auxiliar de pre-validación para no ensuciar la base de datos PostgreSQL. |
| **11** | **Resolución de problemas** | Acostumbrado a depurar incidencias correctivas tanto en código Java (`NullPointerException`, `LazyInitializationException`, bloqueos de transacciones) como en consultas SQL lentas o descuadres de bandas en `.jrxml`. |
| **12** | **Mejora continua** | Refactorización constante de consultas SQL repetitivas hacia vistas indexadas y centralización de la lógica de generación de informes en un servicio reutilizable (`JasperReportGeneratorService`). |

---

## 5. CHECKLIST DE ÚLTIMO MINUTO ANTES DE ENTRAR A LA ENTREVISTA

1. **Repasa los números clave de tu CV:**
   - **Ayuntamiento de Roperuelos del Páramo (León):** 2 etapas (Verano 2023 y Verano-Otoño 2024). Unos ~500 vecinos, ~4.500 parcelas rústicas (alta fragmentación parcelaria de regadío y secano en el Páramo), ~1.200 titulares catastrales y cientos de expedientes anuales.
   - **FDS (DXC Technology):** Febrero 2026 – Junio 2026. Disciplina de consultoría `DEV -> QAS -> PRD`.
   - **HORSE Technologies (Valladolid):** Julio 2026 – Actualidad.
   - **Expectativa salarial:** `23.000 € – 27.000 €` brutos anuales (flexible a tablas Seresco Valladolid + Serflex).
   - **Disponibilidad:** `15 días naturales`.
2. **Prepara tus 3 preguntas finales para el entrevistador:**
   - *"En la oferta se menciona que se valora la adecuación a proyectos de agricultura. ¿El equipo de Valladolid en el que me integraría trabaja en aplicaciones de gestión agraria / PAC para la Administración o en plataformas propias como Cultiva Decisiones?"*
   - *"A nivel de stack técnico del proyecto, ¿con qué versión de Java, servidor de aplicaciones (WildFly/JBoss, Tomcat) y gestor de base de datos (Oracle, PostgreSQL, SQL Server) estáis trabajando actualmente?"*
   - *"¿Cómo organizáis la dinámica del equipo en Valladolid entre los días presenciales en la oficina y los días de teletrabajo?"*
