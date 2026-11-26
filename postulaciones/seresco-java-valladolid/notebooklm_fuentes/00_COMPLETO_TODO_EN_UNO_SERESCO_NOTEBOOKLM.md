# DOSSIER MAESTRO COMPLETO PARA NOTEBOOKLM — ENTREVISTA SERESCO VALLADOLID (DIEGO DE LA FUENTE ALONSO)

---
## ARCHIVO: 00_INDICE_Y_ESTRATEGIA_ENTREVISTA.md

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

---
## ARCHIVO: oferta_analizada.md

# Análisis de Oferta y Match Técnico — Seresco (Desarrollador/a Java en Valladolid)

## 1. Datos de la Vacante
- **Empresa:** Seresco (Área Técnica de Producción de Software — Valladolid)
- **Rol:** Desarrollador/a Java (Perfil Desarrollador JEE)
- **Ubicación y Modalidad:** **Valladolid** (Híbrido con hasta un 50% de teletrabajo)
- **Horario:** **De Lunes a Viernes de 08:00 a 15:00h** todo el año (Jornada completa continua + Contrato indefinido + 22 días laborables + Nochebuena/Nochevieja)
- **Experiencia requerida:** 1 año de experiencia
- **URL Oferta (Viterbit):** https://seresco.viterbit.site/desarrollador-a-java-valladolid-9E5tVln_-5yB/
- **URL Formulario Directo:** https://seresco.viterbit.site/desarrollador-a-java-valladolid-9E5tVln_-5yB/apply/

---

## 2. Requisitos Clave y Keywords ATS
1. **Formación en Informática:** Doble Grado Superior en Desarrollo de Aplicaciones Multiplataforma (**DAM**) y Desarrollo de Aplicaciones Web (**DAW**) + Curso de Especialización en **IA y Big Data**.
2. **Experiencia de al menos 1 año en proyectos de desarrollo de software con Java.**
3. **Programación en entornos web Java/JEE:** **Java / JEE**, **SQL**, **JSF (JavaServer Faces / JSP)**, **Spring Boot** y generación de informes con **Jasper Reports**.
4. **Valorable — Experiencia o adecuación en proyectos de Agricultura / Administración Pública / Medio Rural:** Experiencia directa en el **Ayuntamiento de Roperuelos del Páramo** desarrollando software de gestión municipal, territorial/agrícola y administrativa en entorno rural.

---

## 3. Evaluación de Match (Match Score: **98%**)

| Requisito de Seresco (Valladolid) | Experiencia Real de Diego (CV Maestro) | Nivel de Coincidencia |
|---|---|---|
| **Ubicación en Valladolid (Híbrido 50%)** | Residencia actual en **Valladolid**, con disponibilidad inmediata para acudir a la oficina de Seresco en Valladolid en horario de 08:00 a 15:00h. | **100% (Exact Hit)** |
| **Formación en Informática** | Doble titulación oficial en **DAM** y **DAW** + Especialización en **IA y Big Data**. | **100% (Exact Hit)** |
| **Al menos 1 año en desarrollo Java, SQL, JSF y Jasper Reports** | Desarrollo de aplicaciones web y empresariales en **Java / JEE (Spring Boot, JSF/JSP, Hibernate/JPA, JDBC)**, dominio de **SQL** y generación de informes corporativos (**Jasper Reports** / reporting estructurado). | **98% (Exact Hit)** |
| **Valorable: Proyectos de Agricultura / Gestión Territorial y Pública** | Dos etapas desarrollando software y bases de datos en el **Ayuntamiento de Roperuelos del Páramo** (gestión municipal, censo y ámbito rural/agrícola). | **100% (Diferenciador único)** |

---
## ARCHIVO: carta_presentacion.md

# Carta de Presentación — Seresco (Desarrollador/a Java en Valladolid)

Asunto: Candidatura a Desarrollador/a Java en Valladolid — Diego de la Fuente Alonso

Estimado equipo de Selección de Seresco,

Les escribo para presentar mi candidatura a la posición de Desarrollador/a Java para su Área Técnica de Producción de Software en Valladolid. Resido actualmente en Valladolid y cuento con doble titulación oficial en Informática (Grado Superior en Desarrollo de Aplicaciones Web y Grado Superior en Desarrollo de Aplicaciones Multiplataforma, además de la Especialización en IA y Big Data) y más de un año de experiencia práctica desarrollando software en entornos web con Java, SQL y generación de informes.

Mi trayectoria técnica se alinea directamente con los requisitos y valores de Seresco para este puesto:

- Experiencia en proyectos de desarrollo web con Java, SQL, JSF y Jasper Reports: He trabajado en el desarrollo y mantenimiento de aplicaciones web utilizando el ecosistema Java/JEE (JSF, JSP, Spring Boot, Hibernate y JDBC), diseñando y optimizando consultas sobre bases de datos relacionales SQL (PostgreSQL, MySQL y SQL Server) e implementando la generación de informes y documentos parametrizados con Jasper Reports.
- Experiencia en proyectos vinculados al ámbito rural, agrícola y de gestión pública: Durante mis dos etapas como desarrollador en el Ayuntamiento de Roperuelos del Páramo, construí soluciones web y de bases de datos orientadas a la gestión municipal, territorial y de expedientes del entorno rural y agrícola, experiencia que complementé con mi etapa en consultoría tecnológica en FDS (DXC Technology) y mi puesto actual en HORSE Technologies en Valladolid.
- Residencia en Valladolid y compromiso a largo plazo: Busco integrarme de forma estable en el equipo de Seresco en Valladolid, donde la modalidad híbrida y la jornada continua de 08:00 a 15:00h encajan de manera inmejorable con mi planificación profesional y personal.

Mi disponibilidad de incorporación es de 15 días naturales. Agradezco de antemano su tiempo y consideración, y quedo a su entera disposición para mantener una entrevista personal en sus oficinas de Valladolid o por videollamada.

Atentamente,

Diego de la Fuente Alonso
Desarrollador de Software Java / JEE & SQL (JSF / Spring Boot / Jasper Reports)
Valladolid | (+34) 626 68 71 79 | diegodelafuentealonso@gmail.com

---
## ARCHIVO: respuestas_formulario.md

# Respuestas Exactas para el Formulario de Seresco (Viterbit) — Desarrollador/a Java (Valladolid)

## Enlace Directo al Formulario de Inscripción de Seresco
👉 **https://seresco.viterbit.site/desarrollador-a-java-valladolid-9E5tVln_-5yB/apply/**

---

## 1. Datos Personales y Archivos a Subir
- **Nombre \*:** `Diego`
- **Apellido(s) \*:** `de la Fuente Alonso`
- **Email \*:** `diegodelafuentealonso@gmail.com`
- **Teléfono \*:** `+34 626 68 71 79`
- **País \*:** `España`
- **Ciudad \*:** `Valladolid`
- **Código Postal:** `47001` *(o el código postal exacto de tu domicilio en Valladolid)*
- **Curriculum \*:** Sube `Diego_de_la_Fuente_Alonso_CV_Seresco_Java_Valladolid.pdf`
- **Carta de presentación:** Sube `Diego_de_la_Fuente_Alonso_Carta_Presentacion_Seresco_Java_Valladolid.pdf`

---

## 2. Respuestas Exactas a las 2 Preguntas Obligatorias del Cuestionario

### Pregunta 1: ¿Cuánta experiencia tienes como desarrollador en proyectos Java? \* *(Selector desplegable)*
- Selecciona la opción: **`Más de 12 meses`** *(también puedes marcar `Entre 6 y 12 meses` si prefieres, pero como el selector permite elegir `Más de 12 meses` y la oferta pide "al menos 1 año", **`Más de 12 meses`** garantiza pasar el filtro automático de Viterbit al 100%)*.

### Pregunta 2: ¿Cuáles son tus expectativas económicas? \* *(Campo de texto libre)*
> `Entre 23.000 € y 27.000 € brutos anuales, totalmente flexible y negociable según las tablas salariales de Seresco en Valladolid y el programa de retribución flexible Serflex.`

---
## ARCHIVO: cv_spec.json

```json
{
  "page": {
    "width_mm": 210,
    "height_mm": 297,
    "margins_mm": {
      "top": 15,
      "bottom": 15,
      "left": 18,
      "right": 18
    }
  },
  "styles": [
    {
      "name": "CVTitle",
      "base": "Normal",
      "font": "Calibri",
      "size_pt": 19.5,
      "bold": true,
      "color": "111827"
    },
    {
      "name": "CVSubtitle",
      "base": "Normal",
      "font": "Calibri",
      "size_pt": 10.8,
      "bold": true,
      "color": "1F2937"
    },
    {
      "name": "CVContact",
      "base": "Normal",
      "font": "Calibri",
      "size_pt": 9.5,
      "color": "4B5563"
    },
    {
      "name": "CVHeading",
      "base": "Normal",
      "font": "Calibri",
      "size_pt": 11.5,
      "bold": true,
      "color": "111827"
    },
    {
      "name": "CVJobHeader",
      "base": "Normal",
      "font": "Calibri",
      "size_pt": 10.5,
      "bold": true,
      "color": "111827"
    },
    {
      "name": "CVJobDate",
      "base": "Normal",
      "font": "Calibri",
      "size_pt": 9.5,
      "italic": true,
      "color": "4B5563"
    },
    {
      "name": "CVBody",
      "base": "Normal",
      "font": "Calibri",
      "size_pt": 9.8,
      "color": "1F2937"
    }
  ],
  "blocks": [
    {
      "type": "paragraph",
      "style": "CVTitle",
      "text": "DIEGO DE LA FUENTE ALONSO"
    },
    {
      "type": "paragraph",
      "style": "CVSubtitle",
      "text": "Desarrollador de Software Java / JEE & SQL | Entornos Web (JSF, Spring Boot, Hibernate/JDBC) & Reporting (Jasper Reports)"
    },
    {
      "type": "paragraph",
      "style": "CVContact",
      "text": "Valladolid, España | (+34) 626 68 71 79 | diegodelafuentealonso@gmail.com"
    },
    {
      "type": "paragraph",
      "style": "CVHeading",
      "text": "PERFIL PROFESIONAL"
    },
    {
      "type": "paragraph",
      "style": "CVBody",
      "text": "Desarrollador de Software Java / JEE residente en Valladolid con más de 1 año de experiencia profesional acumulada en proyectos de desarrollo web, integración de sistemas y explotación de bases de datos relacionales SQL. Doble titulación oficial en Informática: Técnico Superior en Desarrollo de Aplicaciones Web (DAW) y Técnico Superior en Desarrollo de Aplicaciones Multiplataforma (DAM), más Curso de Especialización en Inteligencia Artificial y Big Data. Experiencia práctica en programación en entornos web con Java (JEE, JSF/JSP, Spring Boot, Hibernate/JPA y JDBC), optimización de consultas SQL complejas y generación de informes y plantillas documentales (Jasper Reports y herramientas de reporting). Experiencia previa desarrollando aplicaciones de gestión para la administración local y el ámbito rural/agrícola."
    },
    {
      "type": "paragraph",
      "style": "CVHeading",
      "text": "COMPETENCIAS TÉCNICAS (JAVA / JEE, SQL, JSF & JASPER REPORTS)"
    },
    {
      "type": "bullet_list",
      "items": [
        "Desarrollo en Entornos Web Java / JEE: Más de 1 año de experiencia trabajando con Java (Java SE / Jakarta EE / JEE), desarrollo de interfaces y componentes web con JSF (JavaServer Faces), JSP/Servlets y Spring Boot, capa de persistencia con Hibernate (JPA) y JDBC, servicios web REST/SOAP y construcción con Maven/Gradle.",
        "Bases de Datos Relacionales & Dominio de SQL: Diseño de modelos relacionales, escritura y optimización de consultas SQL avanzadas (joins complejos, vistas, funciones analíticas, triggers y procedimientos almacenados) sobre PostgreSQL, MySQL, Microsoft SQL Server, Oracle/SAP y Google BigQuery.",
        "Generación de Informes & Jasper Reports: Diseño y parametrización de informes corporativos, listados oficiales y exportación documental (PDF/Excel/CSV) mediante Jasper Reports (Jaspersoft Studio / JRXML) y herramientas de reporting conectadas a orígenes SQL y beans de Java.",
        "Calidad de Software, Control de Versiones & Sector Público/Agrícola: Uso diario de Git, gestión estructurada del ciclo de vida del software y despliegues entre entornos (DEV, QAS, PRD), y conocimiento funcional de aplicaciones de gestión administrativa, territorial y del sector rural/agrícola."
      ]
    },
    {
      "type": "paragraph",
      "style": "CVHeading",
      "text": "EXPERIENCIA PROFESIONAL"
    },
    {
      "type": "paragraph",
      "style": "CVJobHeader",
      "text": "HORSE Technologies — Desarrollador de Software, Datos SQL & Reporting Corporativo"
    },
    {
      "type": "paragraph",
      "style": "CVJobDate",
      "text": "Julio 2026 – Actualidad | Valladolid, España"
    },
    {
      "type": "bullet_list",
      "items": [
        "Desarrollo y mantengo aplicaciones de software, servicios backend y procesos de integración de datos, aplicando buenas prácticas de ingeniería de software, orientación a la calidad y control de versiones con Git.",
        "Diseño y optimizo consultas SQL complejas sobre bases de datos corporativas (SQL Server, PostgreSQL y BigQuery) y automatizo la generación de informes técnicos y operativos para las distintas áreas de negocio."
      ]
    },
    {
      "type": "paragraph",
      "style": "CVJobHeader",
      "text": "FDS, a DXC Technology Company — Consultor Técnico de Desarrollo y Sistemas Empresariales"
    },
    {
      "type": "paragraph",
      "style": "CVJobDate",
      "text": "Febrero 2026 – Junio 2026 | España"
    },
    {
      "type": "bullet_list",
      "items": [
        "Desarrollé y mantuve lógica de negocio empresarial, consultas SQL de alto rendimiento y módulos de generación de listados e informes corporativos dentro de equipos de producción de software orientados al cliente.",
        "Participé en el análisis funcional y técnico, resolución de incidencias evolutivas y correctivas, y gestión rigurosa del paso entre entornos de Desarrollo, Calidad y Producción (DEV, QAS, PRD)."
      ]
    },
    {
      "type": "paragraph",
      "style": "CVJobHeader",
      "text": "Ayuntamiento de Roperuelos del Páramo — Desarrollador Web Java / JEE (JSF, Spring Boot, SQL & Jasper Reports)"
    },
    {
      "type": "paragraph",
      "style": "CVJobDate",
      "text": "Junio 2024 – Octubre 2024 | Junio 2023 – Septiembre 2023 | León, España"
    },
    {
      "type": "bullet_list",
      "items": [
        "Desarrollé y evolucioné aplicaciones en entorno web utilizando Java / JEE (vistas con JSF/JSP, servicios en Spring Boot y acceso a datos con Hibernate/JDBC) conectadas a bases de datos relacionales SQL (PostgreSQL y MySQL).",
        "Implementé módulos de generación automática de informes, certificados y listados con Jasper Reports a partir de consultas SQL parametrizadas para la gestión administrativa, catastral y de expedientes del ámbito rural y agrícola del municipio."
      ]
    },
    {
      "type": "paragraph",
      "style": "CVJobHeader",
      "text": "Craftelier — Desarrollador de Software & Bases de Datos SQL"
    },
    {
      "type": "paragraph",
      "style": "CVJobDate",
      "text": "Marzo 2024 – Mayo 2024 | España"
    },
    {
      "type": "bullet_list",
      "items": [
        "Desarrollé funcionalidades de software orientado a objetos y optimicé consultas SQL, vistas y generación de reportes operativos sobre bases de datos relacionales Microsoft SQL Server."
      ]
    },
    {
      "type": "paragraph",
      "style": "CVHeading",
      "text": "FORMACIÓN EN INFORMÁTICA"
    },
    {
      "type": "bullet_list",
      "items": [
        "Técnico Superior en Desarrollo de Aplicaciones Web (DAW) — IES San Andrés (2025 – 2026) — Programación en entornos web con Java/JEE, JSF, JSP, Spring Boot, SQL y despliegue en servidores de aplicaciones.",
        "Curso de Especialización en Inteligencia Artificial y Big Data — (2024 – 2025).",
        "Técnico Superior en Desarrollo de Aplicaciones Multiplataforma (DAM) — IES San Andrés (2022 – 2024) — Desarrollo de software con Java, JDBC, Hibernate, diseño de informes con Jasper Reports y bases de datos SQL."
      ]
    },
    {
      "type": "paragraph",
      "style": "CVHeading",
      "text": "IDIOMAS Y DISPONIBILIDAD EN VALLADOLID"
    },
    {
      "type": "bullet_list",
      "items": [
        "Español: Nativo | Inglés: Nivel técnico y profesional.",
        "Residencia actual en Valladolid capital | Disponibilidad para incorporación en 15 días naturales en modalidad híbrida en Valladolid (horario de 08:00 a 15:00h)."
      ]
    }
  ]
}
```

---
## ARCHIVO: 01_teoria_y_preguntas_entrevista_java_jee.md

# 01 — TEORÍA AVANZADA Y PREGUNTAS DE ENTREVISTA: JAVA, JAKARTA EE (JEE) Y SPRING BOOT

> **Objetivo de este documento:** Dominar tanto la arquitectura **Java EE / Jakarta EE (JEE)** clásica que Seresco utiliza en aplicaciones institucionales (JSF, CDI/EJB, JPA/Hibernate, JDBC, desplegadas en WildFly/JBoss o Tomcat) como su equivalencia directa con **Spring Boot**, para responder con precisión de arquitecto a cualquier pregunta técnica.

---

## 1. TABLA DE EQUIVALENCIAS DIRECTAS: JAVA EE / JAKARTA EE vs. SPRING BOOT

En entrevistas para consultoras como Seresco, muchos proyectos históricos están construidos sobre **Java EE 7/8 o Jakarta EE** desplegados en servidores de aplicaciones (**JBoss EAP / WildFly**, **WebLogic** o **Apache Tomcat**), mientras que los módulos más nuevos usan **Spring Boot**. Si conoces esta tabla de memoria, demostrarás que dominas ambos mundos:

| Capa / Concepto | Ecosistema Java EE / Jakarta EE (Clásico Seresco) | Ecosistema Spring Boot (Moderno) |
| :--- | :--- | :--- |
| **Contenedor de Inversión de Control (IoC)** | **CDI** (*Contexts and Dependency Injection*) / Contenedor **EJB** | **Spring IoC Container** (`ApplicationContext`) |
| **Inyección de Dependencias** | `@Inject` (estándar JSR-330 / CDI) o `@EJB` | `@Autowired` o inyección por constructor (recomendada) |
| **Componente de Vista / Controlador Web** | `FacesServlet` + **Managed Bean / CDI Bean** (`@Named` + `@ViewScoped`) con vistas `.xhtml` (JSF / PrimeFaces) | `DispatcherServlet` + `@Controller` / `@RestController` |
| **Servicios REST (si aplica)** | **JAX-RS** (`@Path`, `@GET`, `@POST`, `@Produces`, `@Consumes`) | **Spring Web MVC** (`@RequestMapping`, `@GetMapping`, `@PostMapping`) |
| **Capa de Negocio / Servicios** | `@Stateless` (EJB sin estado) o `@ApplicationScoped` (CDI) | `@Service` (Singleton por defecto en Spring) |
| **Gestión de Transacciones** | `@Transactional` (`javax.transaction.Transactional`) o JTA implícito en EJB (`@TransactionAttribute`) | `@Transactional` (`org.springframework.transaction.annotation.Transactional`) |
| **Capa de Persistencia (ORM)** | **JPA (Hibernate)** inyectando `@PersistenceContext EntityManager em;` | **Spring Data JPA (`JpaRepository`)** o `@PersistenceContext EntityManager em;` |
| **Acceso Directo SQL / Reporting** | `DataSource` inyectado con `@Resource(lookup="jdbc/AgroDS")` + JDBC `Connection` | `DataSource` autoconfigurado + `JdbcTemplate` o `DataSourceUtils.getConnection()` |
| **Empaquetado y Despliegue** | Fichero **`.war`** o **`.ear`** desplegado en un servidor externo (**WildFly / JBoss / Tomcat**) | **`.jar`** ejecutable con Tomcat embebido o **`.war`** para servidor externo |

---

## 2. FUNDAMENTOS CLAVE DE JAVA QUE SIEMPRE PREGUNTAN EN SERESCO

### 2.1. Programación Orientada a Objetos (POO) y Contratos `equals()` / `hashCode()`
1. **Los 4 pilares aplicados al proyecto agrícola:**
   - **Encapsulamiento:** Ocultar el estado interno de `ExpedienteAgrarioEntity` con atributos `private` y exponer métodos de negocio controlados (ej. `aprobarExpediente()` en lugar de cambiar el estado sin validar).
   - **Abstacción:** Definir interfaces como `InformeExportador` o `ExpedienteRepository` desacoplando el *qué hace* del *cómo lo hace*.
   - **Herencia:** Clase base `@MappedSuperclass AuditableEntity` con `fechaCreacion`, `usuarioCreacion`, `fechaModificacion` heredada por todas las tablas administrativas.
   - **Polimorfismo:** Procesar una lista de `List<DocumentoOficial>` donde cada subclase (`CertificadoCatastral`, `ResolucionAyudaPac`) implementa su propia plantilla `.jrxml` e invocamos `doc.generarPdf()`.
2. **Contrato `equals()` y `hashCode()` (Crítico en JPA y Colecciones `Set`/`Map`):**
   - Si dos objetos son iguales según `equals(Object o)`, **obligatoriamente deben devolver el mismo `hashCode()`**.
   - En entidades JPA (`@Entity`), **nunca uses todos los campos ni relaciones `@OneToMany` en `equals`/`hashCode`** (provocaría `LazyInitializationException` o bucles infinitos). Usa una **clave de negocio natural inmutable (`@NaturalId`, como el `codigoExpediente` o el `referenciaSigpac`)** o el `id` controlando el estado transitorio (`id != null && id.equals(other.id)`).

### 2.2. Colecciones (`List`, `Set`, `Map`) y Complejidad
- **`List` (`ArrayList` vs `LinkedList`):** Colección ordenada que **permite duplicados**. `ArrayList` usa un array dinámico en memoria contigua (acceso por índice $O(1)$, excelente para mostrar resultados en un `<p:dataTable>`).
- **`Set` (`HashSet`, `LinkedHashSet`, `TreeSet`):** Colección que **no permite duplicados**. `HashSet` se apoya internamente en una tabla hash ($O(1)$ en búsqueda/inserción usando `hashCode()` y `equals()`). Muy útil en JPA para mapear colecciones `@OneToMany` cuando quieres evitar el error `MultipleBagFetchException` de Hibernate al hacer múltiples `JOIN FETCH`.
- **`Map` (`HashMap`, `LinkedHashMap`):** Diccionario de pares `Clave -> Valor` sin claves duplicadas. En **Jasper Reports** es el objeto estándar (`Map<String, Object> parametros = new HashMap<>()`) que pasamos a `JasperFillManager.fillReport(reporte, parametros, conexion)` para inyectar los parámetros `$P{...}`.

### 2.3. Java Streams y Expresiones Lambda (Java 8+)
En aplicaciones de gestión agraria, usamos `Stream` para transformar, filtrar o agrupar datos en memoria de forma declarativa sin mutar la colección original:
```java
// Ejemplo real: Calcular la superficie total de REGADÍO de las parcelas válidas agrupadas por polígono
Map<Integer, BigDecimal> hectareasRegadioPorPoligono = parcelas.stream()
    .filter(p -> "REGADIO".equalsIgnoreCase(p.getTipoCultivo()))
    .filter(p -> p.isActiva())
    .collect(Collectors.groupingBy(
        ParcelaRustica::getPoligono,
        Collectors.reducing(BigDecimal.ZERO, ParcelaRustica::getSuperficieHa, BigDecimal::add)
    ));
```

---

## 3. PERSISTENCIA AVANZADA CON JPA / HIBERNATE

### 3.1. Los 4 Estados del Ciclo de Vida de una Entidad JPA
1. **Transient (Nuevo / Transitorio):** El objeto se acaba de instanciar con `new ExpedienteAgrarioEntity()`, no tiene `id` en base de datos ni está asociado al contexto de persistencia (`EntityManager`).
2. **Managed (Gestionado / Persistente):** El objeto está asociado al `EntityManager` actual (porque llamamos a `em.persist(entidad)` o porque lo recuperamos con `em.find(...)` / consulta JPQL dentro de una transacción `@Transactional`). **Cualquier cambio con un `.setEstado(...)` en un objeto *Managed* se sincroniza automáticamente a la base de datos (`UPDATE`) al hacer *flush/commit* de la transacción (*Dirty Checking*) sin necesidad de llamar explícitamente a `save()`**.
3. **Detached (Desasociado / Separado):** La transacción o el `EntityManager` se cerró, pero el objeto sigue vivo en memoria (por ejemplo, guardado en un Bean `@ViewScoped` de JSF entre peticiones del usuario). Si intentas acceder a una relación `LAZY` no inicializada sobre un objeto *Detached*, salta la famosa **`LazyInitializationException`**. Para volver a unirlo al contexto de persistencia se usa `em.merge(entidad)`.
4. **Removed (Eliminado):** Se ha invocado `em.remove(entidad)` y será borrado con un `DELETE` al confirmar la transacción.

### 3.2. `FetchType.LAZY` vs `FetchType.EAGER` y el Problema de las `N+1 Queries`
- **Valores por defecto en JPA:**
  - `@ManyToOne` y `@OneToOne` son **`EAGER`** por defecto *(¡Mala práctica dejarlo en `EAGER`! Conviene forzar siempre `fetch = FetchType.LAZY`)*.
  - `@OneToMany` y `@ManyToMany` son **`LAZY`** por defecto.
- **¿En qué consiste el problema `N+1`?**
  Imagina que ejecutas una consulta JPQL para listar 100 expedientes agrarios:
  `SELECT e FROM ExpedienteAgrarioEntity e WHERE e.campania = 2026` (1 consulta SQL).
  Luego, al renderizar la tabla en JSF o construir el DTO para Jasper Reports, por cada expediente accedes a `e.getTitular().getNombreCompleto()`. Si la relación `titular` no se trajo en la consulta inicial, Hibernate lanza **100 consultas SQL adicionales** (`SELECT * FROM titulares WHERE id = ?`), sumando **1 + 100 = 101 consultas** contra la base de datos y hundiendo el rendimiento.
- **¿Cómo se soluciona profesionalmente?**
  1. **`JOIN FETCH` en JPQL:**
     ```sql
     SELECT DISTINCT e FROM ExpedienteAgrarioEntity e
     JOIN FETCH e.titular t
     LEFT JOIN FETCH e.lineasParcela lp
     WHERE e.campania = :campania
     ```
     Esto obliga a Hibernate a traer el expediente, su titular y sus parcelas en **una única consulta SQL** con `INNER JOIN` y `LEFT OUTER JOIN`.
  2. **`@EntityGraph`:** Definir qué relaciones grafo cargar dinámicamente sin ensuciar la query JPQL base.
  3. **Proyecciones DTO (`SELECT new es.seresco...ExpedienteResumenDTO(...)`) o Consultas SQL Nativas:** Cuando es un listado de búsqueda en JSF o un informe de Jasper Reports con miles de filas, proyectar directamente solo las columnas necesarias evita cargar entidades pesadas en la caché de primer nivel de Hibernate.

### 3.3. Gestión de Transacciones (`@Transactional`)
- **Ubicación correcta:** Siempre en la **capa de Servicio (`ExpedienteService`)**, nunca en el Managed Bean de JSF ni en el Repositorio individual, porque un caso de negocio suele abarcar varias operaciones de base de datos que deben ser atómicas (ACID).
- **`readOnly = true` (en Spring) / consultas sin bloqueo:** En métodos de solo lectura (búsquedas para tablas JSF o lectura de datos para Jasper Reports), desactivar el *Dirty Checking* de Hibernate ahorra memoria y CPU.
- **Trampa clásica de entrevista sobre `rollbackFor`:**
  Por defecto, tanto en JEE (JTA) como en Spring, `@Transactional` **solo hace rollback automático ante excepciones no comprobadas (`RuntimeException` y `Error`)**, pero **NO hace rollback ante excepciones comprobadas (*Checked Exceptions* como `IOException`, `SQLException` o `JRException` de Jasper Reports)**. Por eso, cuando un método transaccional puede lanzar una excepción *checked*, siempre declaramos explícitamente:
  `@Transactional(rollbackFor = Exception.class)` (en Spring) o `@Transactional(rollbackOn = Exception.class)` (en Jakarta EE).

---

## 4. LAS 15 PREGUNTAS REALES DE ENTREVISTA TÉCNICA JAVA/JEE EN SERESCO (Y SUS RESPUESTAS EN VOZ ALTA)

### Pregunta 1: ¿Cuál es la diferencia entre `JDK`, `JRE` y `JVM`?
> **Respuesta:** "La **JVM** (*Java Virtual Machine*) es la máquina virtual que ejecuta el bytecode (`.class`) y gestiona la memoria (Heap, Stack y Garbage Collector). El **JRE** (*Java Runtime Environment*) incluye la JVM más las librerías estándar necesarias para ejecutar una aplicación. Y el **JDK** (*Java Development Kit*) añade sobre el JRE las herramientas de desarrollo como el compilador `javac`, el depurador y utilidades de diagnóstico."

### Pregunta 2: ¿Por qué en entidades monetarias o de superficies agrarias (hectáreas SIGPAC) nunca debemos usar `double` o `float`, sino `BigDecimal`?
> **Respuesta:** "Porque `double` y `float` usan aritmética de coma flotante binaria IEEE 754 y producen errores de precisión decimal (por ejemplo, `0.1 + 0.2` da `0.30000000000000004`). En proyectos agrarios o administrativos, donde una diferencia de 0,01 hectáreas o un céntimo en una ayuda de la PAC puede invalidar un expediente oficial, siempre utilizo **`BigDecimal`** inicializado con `String` o `BigDecimal.valueOf(...)` y definiendo explícitamente la escala y el modo de redondeo (`RoundingMode.HALF_UP`), mapeándolo en SQL como `NUMERIC(10,4)` o `DECIMAL(12,2)`."

### Pregunta 3: ¿Qué diferencia hay entre `==` y `.equals()` en Java, y qué es el *String Pool*?
> **Respuesta:** "El operador `==` compara referencias de memoria (si dos variables apuntan exactamente a la misma dirección en el Heap, o el valor en tipos primitivos), mientras que `.equals()` compara la igualdad lógica del contenido del objeto. Con los `String`, Java mantiene un *String Pool* para reutilizar literales idénticos, pero si un `String` viene de un formulario JSF o de un `ResultSet` de JDBC se instancia fuera del pool, por lo que comparar cadenas con `==` fallará; siempre hay que usar `.equals()` o `Objects.equals(a, b)` para evitar `NullPointerException`."

### Pregunta 4: ¿Cuál es la diferencia entre `String`, `StringBuilder` y `StringBuffer`?
> **Respuesta:** "`String` es inmutable: cada vez que concatenas con `+` dentro de un bucle creas objetos nuevos en memoria. `StringBuilder` es mutable y muy rápido porque modifica un buffer interno sin crear objetos intermedios, siendo el ideal para construir consultas SQL dinámicas con filtros opcionales dentro de un método local. `StringBuffer` también es mutable pero tiene sus métodos sincronizados (`synchronized`), por lo que es *thread-safe* pero más lento."

### Pregunta 5: ¿Qué diferencia hay entre una interfaz (`interface`) y una clase abstracta (`abstract class`)?
> **Respuesta:** "Una clase abstracta puede tener estado (atributos de instancia no finales) y constructores, y permite compartir código base entre clases estrechamente relacionadas (relación *ES-UN*, con herencia simple `extends`). Una interfaz define un contrato de comportamiento (que desde Java 8 puede incluir métodos `default` y `static`, pero sin estado de instancia) y una clase puede implementar múltiples interfaces (`implements`), lo que es clave para la inyección de dependencias y el bajo acoplamiento."

### Pregunta 6: ¿Qué es la Inyección de Dependencias (IoC) y por qué es preferible frente a hacer `new ExpedienteService()`?
> **Respuesta:** "La Inversión de Control delega en el contenedor (sea CDI/EJB en Jakarta EE con `@Inject` o Spring con `@Autowired`) la creación y el ciclo de vida de las dependencias. Si hiciera `new ExpedienteService()` acoplaría el controlador a una implementación concreta, perdería los proxies dinámicos que gestionan las transacciones (`@Transactional`) y la seguridad, y no podría inyectar un *mock* al hacer pruebas unitarias con JUnit y Mockito."

### Pregunta 7: ¿Cómo funciona `@Transactional` por debajo en Java EE / Spring y qué pasa si llamas a un método `@Transactional` desde otro método de la misma clase?
> **Respuesta:** "Funciona mediante el patrón **Proxy Dinámico (AOP)**: el contenedor envuelve nuestra clase de servicio en un proxy que abre la transacción antes de entrar al método y hace `commit` o `rollback` al salir. Si desde un método `A()` de la clase `ExpedienteService` llamo directamente a `this.metodoB()` que tiene `@Transactional`, la llamada no pasa por el proxy externo sino por la referencia interna `this`, por lo que la anotación `@Transactional` de `metodoB()` se ignora."

### Pregunta 8: ¿Qué es una `LazyInitializationException` en Hibernate/JPA y cómo la evitas en una aplicación web con JSF?
> **Respuesta:** "Ocurre cuando la vista XHTML de JSF o el Managed Bean intenta acceder a una colección o relación configurada como `FetchType.LAZY` después de que la sesión de Hibernate (`EntityManager`) y la transacción del servicio ya se han cerrado. En lugar de usar el antipatrón *Open Session in View* o cambiar la entidad a `EAGER` (que penaliza todas las consultas), lo soluciono cargando en la capa de servicio exactamente los datos que necesita la vista mediante una consulta JPQL con `JOIN FETCH` o devolviendo un DTO ya poblado antes de cerrar la transacción."

### Pregunta 9: ¿Cuál es la diferencia entre `Statement` y `PreparedStatement` en JDBC?
> **Respuesta:** "Dos diferencias críticas: **seguridad** y **rendimiento**. `Statement` concatena cadenas de texto, lo que abre la puerta a ataques de **Inyección SQL**. `PreparedStatement` utiliza parámetros posicionales (`?`) cuyos valores se envían separados de la estructura sintáctica del SQL, neutralizando al 100% la inyección SQL. Además, la base de datos precompila y cachea el plan de ejecución del `PreparedStatement`, acelerando ejecuciones repetidas."

### Pregunta 10: ¿Cómo gestionas el cierre de recursos (`Connection`, `PreparedStatement`, `ResultSet` o flujos de bytes de un PDF de Jasper Reports)?
> **Respuesta:** "Utilizando siempre el bloque **`try-with-resources`** introducido en Java 7 (`try (Connection conn = dataSource.getConnection(); PreparedStatement ps = ...) { ... }`). Al implementar la interfaz `AutoCloseable`, Java garantiza que la conexión se devuelve al pool de conexiones (como HikariCP o el pool JNDI de WildFly/JBoss) incluso si salta una excepción en mitad de la consulta, evitando fugas de conexiones (*Connection Leaks*) que bloquearían el servidor de aplicaciones."

### Pregunta 11: ¿Qué diferencia hay entre excepciones *Checked* y *Unchecked* en Java, y cómo diseñas el manejo de errores en una aplicación web empresarial?
> **Respuesta:** "Las excepciones *Checked* heredan de `Exception` (pero no de `RuntimeException`) y el compilador obliga a capturarlas o declararlas con `throws` (ej. `SQLException`, `JRException`). Las *Unchecked* heredan de `RuntimeException` (ej. `NullPointerException`, `IllegalArgumentException` o nuestras propias excepciones de negocio como `ExpedienteInvalidoException`). En mis proyectos defino excepciones de negocio *Unchecked* para que fuercen automáticamente el rollback de `@Transactional`, las capturo en la capa de controlador/Managed Bean, registro el detalle técnico en el log con SLF4J/Logback y muestro al usuario en JSF un `FacesMessage` claro y amigable."

### Pregunta 12: ¿Qué diferencia hay entre `em.persist()`, `em.merge()` y `em.flush()` en el `EntityManager` de JPA?
> **Respuesta:** "`persist(entity)` toma una instancia nueva (*Transient*) y la convierte en *Managed* para insertarla en base de datos. `merge(entity)` toma una instancia desasociada (*Detached*, como un objeto editado por el usuario en un formulario `@ViewScoped` de JSF), copia su estado a una instancia *Managed* y devuelve esa copia gestionada para hacer el `UPDATE`. Y `flush()` fuerza a que los comandos SQL pendientes en memoria (`INSERT`, `UPDATE`, `DELETE`) se envíen inmediatamente a la base de datos dentro de la misma transacción sin esperar al `commit` final."

### Pregunta 13: ¿Qué diferencia hay entre una consulta JPQL (`createQuery`) y una consulta SQL Nativa (`createNativeQuery`)? ¿Cuándo eliges cada una?
> **Respuesta:** "JPQL consulta sobre el modelo orientado a objetos (clases `@Entity` y sus atributos), es portable entre motores de base de datos y aprovecha el ciclo de vida de JPA. Uso JPQL para el 85% de las operaciones CRUD y búsquedas de negocio. En cambio, uso SQL Nativo (o JDBC directo) cuando necesito exprimir funciones analíticas específicas del motor SQL (como funciones ventana `ROW_NUMBER() OVER(...)`, CTEs recursivas, cruces espaciales/catastrales complejos o alimentar informes masivos de Jasper Reports con máximo rendimiento)."

### Pregunta 14: ¿Qué es un Pool de Conexiones (como el DataSource JNDI en WildFly/Tomcat o HikariCP) y por qué es vital?
> **Respuesta:** "Abrir una conexión física TCP/IP y autenticar contra PostgreSQL, Oracle o SQL Server es una operación muy costosa (puede tardar decenas de milisegundos). Un Pool de Conexiones mantiene un conjunto de conexiones físicas ya abiertas y listas en memoria. Cuando nuestra aplicación o Jasper Reports pide `dataSource.getConnection()`, el pool le presta una al instante, y al hacer `conn.close()` no se cierra la conexión física, sino que regresa al pool para el siguiente usuario."

### Pregunta 15: En tu etapa en FDS (DXC Technology) y en el Ayuntamiento, ¿cómo garantizabas que un cambio en Java o SQL no rompiera Producción?
> **Respuesta:** "Siguiendo de forma estricta el ciclo **`DEV -> QAS -> PRD`**:
> 1. En **DEV (Desarrollo)** implemento el cambio en una rama Git, externalizo cualquier ruta o credencial en ficheros de configuración por entorno, verifico con pruebas unitarias y compruebo que las consultas SQL usen los índices correctos.
> 2. En **QAS (Calidad / Preproducción)** desplegamos el artefacto (`.war` / `.jar`) y ejecutamos los scripts SQL de migración sobre una copia anonimizada de datos reales, probando también la generación de los PDFs de Jasper Reports con casos límite.
> 3. Solo tras la validación funcional pasamos a **PRD (Producción)** llevando siempre preparado el script de *rollback* por si hubiera cualquier incidencia."

---
## ARCHIVO: ExpedienteAgrarioEntity.java

```java
package es.seresco.agro.roperuelos.model; // Paquete estructurado por dominio agrario/municipal

import java.io.Serializable; // Necesario en entidades JEE/JSF que viajan en ámbitos de vista o sesión
import java.math.BigDecimal; // Tipo obligatorio para superficies en hectáreas (SIGPAC) e importes sin pérdida de precisión
import java.time.LocalDate; // API moderna de fechas Java 8+ (java.time) para fechas sin hora
import java.time.LocalDateTime; // Fecha y hora exacta para auditoría de creación/modificación
import java.util.ArrayList; // Implementación de lista dinámica en memoria para inicializar relaciones @OneToMany
import java.util.List; // Interfaz estándar de colección ordenada
import java.util.Objects; // Utilidad null-safe para implementar equals() y hashCode()

import javax.persistence.CascadeType; // Define cómo se propagan las operaciones (PERSIST, MERGE, REMOVE) a entidades hijas
import javax.persistence.Column; // Mapea un atributo Java a su columna exacta en la tabla SQL
import javax.persistence.Entity; // Marca la clase como una Entidad gestionada por el contenedor JPA (Hibernate)
import javax.persistence.EnumType; // Permite indicar que los Enum se guarden como texto (STRING) y no como número (ORDINAL)
import javax.persistence.Enumerated; // Anotación para persistir tipos enumerados en base de datos
import javax.persistence.FetchType; // Controla la estrategia de carga de relaciones: LAZY (perezosa) vs EAGER (ansiosa)
import javax.persistence.GeneratedValue; // Indica que la clave primaria se genera automáticamente en la base de datos
import javax.persistence.GenerationType; // Estrategia de generación de ID (IDENTITY para PostgreSQL/MySQL/SQL Server o SEQUENCE)
import javax.persistence.Id; // Identifica el atributo que actúa como Primary Key (PK) de la tabla
import javax.persistence.Index; // Permite declarar índices SQL desde el modelo JPA para optimizar búsquedas frecuentes
import javax.persistence.JoinColumn; // Especifica la columna Foreign Key (FK) en relaciones @ManyToOne
import javax.persistence.ManyToOne; // Relación Muchos-a-Uno (Muchos expedientes pertenecen a Un Titular agrario)
import javax.persistence.OneToMany; // Relación Uno-a-Muchos (Un expediente agrupa Muchas parcelas rústicas asociadas)
import javax.persistence.PrePersist; // Callback del ciclo de vida JPA que se ejecuta automáticamente antes del INSERT SQL
import javax.persistence.PreUpdate; // Callback del ciclo de vida JPA que se ejecuta automáticamente antes del UPDATE SQL
import javax.persistence.Table; // Especifica el nombre real de la tabla en la base de datos relacional y sus restricciones
import javax.persistence.Version; // Control de concurrencia optimista: evita que dos administrativos pisen el mismo expediente

/**
 * Entidad JPA que representa un Expediente Administrativo Agrario / Catastral
 * tramitado en el Ayuntamiento de Roperuelos del Páramo (y extrapolable a sistemas PAC/ITACyL de Seresco).
 */
@Entity // Indica a Hibernate/JPA que esta clase está vinculada a una tabla de base de datos
@Table(
    name = "expedientes_municipales", // Nombre físico de la tabla en PostgreSQL / MySQL
    indexes = {
        // Índice compuesto por campaña y estado para acelerar los filtros de la bandeja JSF (p:dataTable)
        @Index(name = "idx_exp_campania_estado", columnList = "campania_agricola, estado_expediente"),
        // Índice único sobre el código oficial del expediente (ej. EXP-2024-00145)
        @Index(name = "idx_exp_codigo_unico", columnList = "codigo_expediente", unique = true)
    }
)
public class ExpedienteAgrarioEntity implements Serializable { // Implementa Serializable por estándar Java EE

    // Identificador de versión para serialización binaria en contenedores JEE (WildFly / JBoss / Tomcat)
    private static final long serialVersionUID = 1L;

    /**
     * Enumerado interno que define la máquina de estados del expediente agrario.
     */
    public enum EstadoExpediente {
        BORRADOR,           // Registrado en ventanilla pero pendiente de aportar documentación catastral
        EN_REVISION_TECNICA,// En revisión de recintos SIGPAC y cruce de titularidad en base de datos
        APROBADO,           // Validado por secretaría municipal; habilita la emisión del Certificado PDF con Jasper Reports
        SUBSANACION,        // Requiere corrección por parte del agricultor/titular (discrepancia de hectáreas o lindes)
        DENEGADO            // Rechazado con resolución motivada
    }

    @Id // Clave primaria de la tabla expedientes_municipales
    @GeneratedValue(strategy = GenerationType.IDENTITY) // Usa columna autoincremental (SERIAL/BIGSERIAL en PostgreSQL, AUTO_INCREMENT en MySQL)
    @Column(name = "id_expediente") // Nombre exacto de la columna PK en SQL
    private Long id; // Usamos Long (objeto envolvente) en lugar de long primitivo para distinguir entidades Transient (id == null)

    @Column(
        name = "codigo_expediente", // Columna de clave de negocio natural (ej. "EXP-ROP-2024-0089")
        nullable = false,           // Genera restricción NOT NULL en el DDL SQL
        unique = true,              // Genera restricción UNIQUE en base de datos
        length = 30                 // VARCHAR(30)
    )
    private String codigoExpediente; // Clave natural inmutable que usamos en equals() y hashCode()

    @Column(name = "campania_agricola", nullable = false) // Año de la campaña agraria/catastral (ej. 2023, 2024, 2026)
    private Integer campaniaAgricola; // Permite filtrar expedientes por ejercicio anual

    @Column(name = "tipo_tramite", nullable = false, length = 80) // Ej: "CERTIFICADO_BIENES_RUSTICOS", "APROVECHAMIENTO_COMUNAL", "DECLARACION_REGADIO"
    private String tipoTramite; // Tipología del expediente municipal o agrario

    @Enumerated(EnumType.STRING) // CRÍTICO: Guarda "APROBADO" como VARCHAR en lugar de un número (0,1,2) que se rompería al reordenar el Enum
    @Column(name = "estado_expediente", nullable = false, length = 30) // Columna de estado actual
    private EstadoExpediente estado; // Estado administrativo del expediente

    @Column(
        name = "superficie_total_declarada_ha", // Superficie total en hectáreas declarada en el expediente
        nullable = false,                       // Siempre debe tener valor (mínimo 0.0000)
        precision = 10,                         // Hasta 10 dígitos en total
        scale = 4                               // 4 decimales de precisión (estándar SIGPAC: hasta centiáreas, 0.0001 ha = 1 m2)
    )
    private BigDecimal superficieTotalDeclaradaHa = BigDecimal.ZERO; // Inicializado a 0 para evitar NullPointerException en sumatorios

    @Column(
        name = "importe_tasa_o_ayuda_eur", // Importe económico asociado (tasa municipal o subvención/ayuda agraria)
        precision = 12,                    // 12 dígitos totales
        scale = 2                          // 2 decimales para céntimos de euro
    )
    private BigDecimal importeEconomicoEur = BigDecimal.ZERO; // Valor monetario exacto con BigDecimal

    @Column(name = "fecha_solicitud", nullable = false) // Fecha oficial de registro de entrada
    private LocalDate fechaSolicitud; // Mapeado automáticamente por JPA 2.2+ a tipo DATE de SQL

    @Column(name = "fecha_resolucion") // Puede ser NULL mientras el expediente está en trámite
    private LocalDate fechaResolucion; // Fecha en que se aprueba o deniega el expediente

    @Column(name = "observaciones_tecnicas", length = 1000) // Comentarios del técnico o secretario municipal
    private String observacionesTecnicas; // Texto descriptivo que se imprimirá también en el pie del informe Jasper Reports

    // =========================================================================
    // RELACIONES JPA (@ManyToOne y @OneToMany) OPTIMIZADAS CONTRA N+1 QUERIES
    // =========================================================================

    @ManyToOne(fetch = FetchType.LAZY, optional = false) // SIEMPRE FetchType.LAZY para no cargar el titular si no se necesita; optional=false impone FK NOT NULL
    @JoinColumn(name = "id_titular", nullable = false)   // Columna Foreign Key en expedientes_municipales que apunta a titulares(id_titular)
    private TitularAgrarioStub titular;                  // Agricultor, vecino o entidad titular del expediente

    @OneToMany(
        mappedBy = "expediente",         // Indica que la relación es bidireccional y la FK está en el atributo "expediente" de la clase hija
        fetch = FetchType.LAZY,          // Carga perezosa: las parcelas solo se traen cuando hacemos JOIN FETCH en el repositorio
        cascade = CascadeType.ALL,       // Al guardar o actualizar el expediente, se persisten/actualizan sus líneas de parcela en cascada
        orphanRemoval = true             // Si quitamos una parcela de la colección en memoria, JPA ejecuta el DELETE correspondiente en BD
    )
    private List<ParcelaExpedienteStub> parcelasAsociadas = new ArrayList<>(); // Inicializada siempre para evitar NullPointerException

    // =========================================================================
    // CAMPOS DE AUDITORÍA Y CONTROL DE CONCURRENCIA OPTIMISTA
    // =========================================================================

    @Version // Hibernate incrementa este número automáticamente en cada UPDATE: UPDATE ... SET version = version + 1 WHERE id = ? AND version = ?
    @Column(name = "version_concurrencia", nullable = false)
    private Long version; // Si otro usuario modificó el registro antes, JPA lanza OptimisticLockException evitando pérdida de datos

    @Column(name = "fecha_creacion", nullable = false, updatable = false) // updatable = false impide que un UPDATE modifique la fecha de alta original
    private LocalDateTime fechaCreacion; // Timestamp de auditoría de alta

    @Column(name = "fecha_ultima_modificacion", nullable = false) // Se actualiza automáticamente en cada cambio
    private LocalDateTime fechaUltimaModificacion; // Timestamp de auditoría de última edición

    // Constructor vacío obligatorio por especificación JPA (Hibernate lo usa por reflexión al hidratar resultados SQL)
    public ExpedienteAgrarioEntity() {
    }

    // Constructor de conveniencia para instanciar nuevos expedientes desde la capa de servicio
    public ExpedienteAgrarioEntity(String codigoExpediente, Integer campaniaAgricola, String tipoTramite, TitularAgrarioStub titular) {
        this.codigoExpediente = codigoExpediente; // Asigna el código único
        this.campaniaAgricola = campaniaAgricola; // Asigna la campaña (ej. 2024)
        this.tipoTramite = tipoTramite;           // Asigna el tipo de trámite municipal/agrario
        this.titular = titular;                   // Vincula con el titular solicitante
        this.estado = EstadoExpediente.BORRADOR;  // Todo expediente nace en estado BORRADOR
        this.fechaSolicitud = LocalDate.now();    // Fecha de registro por defecto hoy
    }

    // =========================================================================
    // CALLBACKS DE CICLO DE VIDA JPA (@PrePersist y @PreUpdate)
    // =========================================================================

    @PrePersist // Se dispara justo antes de que el EntityManager ejecute el INSERT INTO expedientes_municipales
    protected void alCrearRegistro() {
        LocalDateTime ahora = LocalDateTime.now(); // Captura el instante actual del servidor
        this.fechaCreacion = ahora;                // Fija fecha de creación
        this.fechaUltimaModificacion = ahora;      // Iguala fecha de última modificación
        if (this.estado == null) {                 // Garantiza defensivamente que nunca se inserte un estado nulo
            this.estado = EstadoExpediente.BORRADOR;
        }
        if (this.fechaSolicitud == null) {         // Garantiza que la fecha de solicitud nunca quede nula
            this.fechaSolicitud = LocalDate.now();
        }
    }

    @PreUpdate // Se dispara justo antes de que el EntityManager ejecute un UPDATE sobre la fila
    protected void alActualizarRegistro() {
        this.fechaUltimaModificacion = LocalDateTime.now(); // Refresca automáticamente el sello de tiempo de auditoría
    }

    // =========================================================================
    // MÉTODOS HELPER DE NEGOCIO Y SINCRONIZACIÓN BIDIRECCIONAL JPA
    // =========================================================================

    /**
     * Método helper para añadir una parcela al expediente manteniendo sincronizados ambos lados
     * de la relación bidireccional en memoria y recalculando la superficie total en hectáreas.
     */
    public void agregarParcela(ParcelaExpedienteStub parcela) {
        this.parcelasAsociadas.add(parcela);       // Añade la parcela a la colección del padre
        parcela.setExpediente(this);               // Vincula la referencia inversa (@ManyToOne) en el hijo
        recalcularSuperficieTotal();               // Actualiza el sumatorio de hectáreas con precisión BigDecimal
    }

    /**
     * Método helper para desvincular una parcela del expediente y recalcular las hectáreas totales.
     */
    public void eliminarParcela(ParcelaExpedienteStub parcela) {
        this.parcelasAsociadas.remove(parcela);    // Elimina de la lista (disparará el DELETE por orphanRemoval = true)
        parcela.setExpediente(null);               // Limpia la referencia al padre
        recalcularSuperficieTotal();               // Recalcula la superficie total declarada
    }

    /**
     * Recalcula la superficie total sumando las hectáreas de todas las parcelas asociadas usando Streams y BigDecimal.
     */
    public void recalcularSuperficieTotal() {
        this.superficieTotalDeclaradaHa = this.parcelasAsociadas.stream() // Abre un flujo sobre la lista de parcelas
            .map(ParcelaExpedienteStub::getSuperficieDeclaradaHa)         // Extrae el BigDecimal de hectáreas de cada parcela
            .filter(Objects::nonNull)                                     // Descarta posibles nulos defensivamente
            .reduce(BigDecimal.ZERO, BigDecimal::add);                    // Suma con precisión exacta partiendo de 0
    }

    // =========================================================================
    // GETTERS Y SETTERS ESTÁNDAR (REQUERIDOS POR JPA, JSF EL Y JASPER REPORTS)
    // =========================================================================

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getCodigoExpediente() { return codigoExpediente; }
    public void setCodigoExpediente(String codigoExpediente) { this.codigoExpediente = codigoExpediente; }

    public Integer getCampaniaAgricola() { return campaniaAgricola; }
    public void setCampaniaAgricola(Integer campaniaAgricola) { this.campaniaAgricola = campaniaAgricola; }

    public String getTipoTramite() { return tipoTramite; }
    public void setTipoTramite(String tipoTramite) { this.tipoTramite = tipoTramite; }

    public EstadoExpediente getEstado() { return estado; }
    public void setEstado(EstadoExpediente estado) { this.estado = estado; }

    public BigDecimal getSuperficieTotalDeclaradaHa() { return superficieTotalDeclaradaHa; }
    public void setSuperficieTotalDeclaradaHa(BigDecimal superficieTotalDeclaradaHa) { this.superficieTotalDeclaradaHa = superficieTotalDeclaradaHa; }

    public BigDecimal getImporteEconomicoEur() { return importeEconomicoEur; }
    public void setImporteEconomicoEur(BigDecimal importeEconomicoEur) { this.importeEconomicoEur = importeEconomicoEur; }

    public LocalDate getFechaSolicitud() { return fechaSolicitud; }
    public void setFechaSolicitud(LocalDate fechaSolicitud) { this.fechaSolicitud = fechaSolicitud; }

    public LocalDate getFechaResolucion() { return fechaResolucion; }
    public void setFechaResolucion(LocalDate fechaResolucion) { this.fechaResolucion = fechaResolucion; }

    public String getObservacionesTecnicas() { return observacionesTecnicas; }
    public void setObservacionesTecnicas(String observacionesTecnicas) { this.observacionesTecnicas = observacionesTecnicas; }

    public TitularAgrarioStub getTitular() { return titular; }
    public void setTitular(TitularAgrarioStub titular) { this.titular = titular; }

    public List<ParcelaExpedienteStub> getParcelasAsociadas() { return parcelasAsociadas; }
    public void setParcelasAsociadas(List<ParcelaExpedienteStub> parcelasAsociadas) { this.parcelasAsociadas = parcelasAsociadas; }

    public Long getVersion() { return version; }
    public LocalDateTime getFechaCreacion() { return fechaCreacion; }
    public LocalDateTime getFechaUltimaModificacion() { return fechaUltimaModificacion; }

    // =========================================================================
    // EQUALS Y HASHCODE BASADOS EN CLAVE DE NEGOCIO NATURAL (BUENA PRÁCTICA JPA)
    // =========================================================================

    @Override
    public boolean equals(Object o) {
        if (this == o) return true; // Si apuntan a la misma dirección de memoria, son iguales
        if (!(o instanceof ExpedienteAgrarioEntity)) return false; // Verifica compatibilidad de tipo soportando proxies de Hibernate
        ExpedienteAgrarioEntity other = (ExpedienteAgrarioEntity) o;
        // Comparamos por codigoExpediente (clave natural inmutable y única), funcionando tanto antes como después de persistir
        return codigoExpediente != null && Objects.equals(codigoExpediente, other.getCodigoExpediente());
    }

    @Override
    public int hashCode() {
        // Devuelve el hash de la clave de negocio natural
        return Objects.hashCode(codigoExpediente);
    }

    @Override
    public String toString() {
        // IMPORTANTE: Nunca incluir relaciones FetchType.LAZY en toString() para evitar LazyInitializationException en logs
        return "ExpedienteAgrarioEntity{" +
                "id=" + id +
                ", codigoExpediente='" + codigoExpediente + '\'' +
                ", campaniaAgricola=" + campaniaAgricola +
                ", estado=" + estado +
                ", superficieTotalDeclaradaHa=" + superficieTotalDeclaradaHa +
                '}';
    }

    // =========================================================================
    // CLASES AUXILIARES CONEXAS PARA COMPILACIÓN AUTOCONTENIDA DEL MODELO
    // =========================================================================

    @Entity
    @Table(name = "titulares")
    public static class TitularAgrarioStub implements Serializable {
        private static final long serialVersionUID = 1L;
        @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
        @Column(name = "id_titular")
        private Long id;
        @Column(name = "nif_cif", nullable = false, unique = true, length = 15)
        private String nifCif;
        @Column(name = "nombre_completo", nullable = false, length = 150)
        private String nombreCompleto;
        @Column(name = "municipio_residencia", length = 100)
        private String municipioResidencia;

        public Long getId() { return id; }
        public void setId(Long id) { this.id = id; }
        public String getNifCif() { return nifCif; }
        public void setNifCif(String nifCif) { this.nifCif = nifCif; }
        public String getNombreCompleto() { return nombreCompleto; }
        public void setNombreCompleto(String nombreCompleto) { this.nombreCompleto = nombreCompleto; }
        public String getMunicipioResidencia() { return municipioResidencia; }
        public void setMunicipioResidencia(String municipioResidencia) { this.municipioResidencia = municipioResidencia; }
    }

    @Entity
    @Table(name = "parcelas_expediente")
    public static class ParcelaExpedienteStub implements Serializable {
        private static final long serialVersionUID = 1L;
        @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
        @Column(name = "id_parcela_exp")
        private Long id;
        @Column(name = "poligono", nullable = false)
        private Integer poligono;
        @Column(name = "parcela", nullable = false)
        private Integer parcela;
        @Column(name = "recinto_sigpac", nullable = false)
        private Integer recintoSigpac;
        @Column(name = "tipo_cultivo", nullable = false, length = 30) // "REGADIO" o "SECANO"
        private String tipoCultivo;
        @Column(name = "superficie_declarada_ha", nullable = false, precision = 10, scale = 4)
        private BigDecimal superficieDeclaradaHa;
        @ManyToOne(fetch = FetchType.LAZY)
        @JoinColumn(name = "id_expediente", nullable = false)
        private ExpedienteAgrarioEntity expediente;

        public Long getId() { return id; }
        public Integer getPoligono() { return poligono; }
        public void setPoligono(Integer poligono) { this.poligono = poligono; }
        public Integer getParcela() { return parcela; }
        public void setParcela(Integer parcela) { this.parcela = parcela; }
        public Integer getRecintoSigpac() { return recintoSigpac; }
        public void setRecintoSigpac(Integer recintoSigpac) { this.recintoSigpac = recintoSigpac; }
        public String getTipoCultivo() { return tipoCultivo; }
        public void setTipoCultivo(String tipoCultivo) { this.tipoCultivo = tipoCultivo; }
        public BigDecimal getSuperficieDeclaradaHa() { return superficieDeclaradaHa; }
        public void setSuperficieDeclaradaHa(BigDecimal superficieDeclaradaHa) { this.superficieDeclaradaHa = superficieDeclaradaHa; }
        public ExpedienteAgrarioEntity getExpediente() { return expediente; }
        public void setExpediente(ExpedienteAgrarioEntity expediente) { this.expediente = expediente; }
    }
}
```

---
## ARCHIVO: ExpedienteRepository.java

```java
package es.seresco.agro.roperuelos.repository; // Paquete de acceso a datos (Capa DAO / Repository)

import java.math.BigDecimal; // Para mapear sumatorios y superficies agrarias con precisión exacta
import java.sql.Connection; // Conexión JDBC estándar al motor relacional (PostgreSQL, MySQL, Oracle, SQL Server)
import java.sql.Date; // Tipo java.sql.Date para pasar fechas a PreparedStatement
import java.sql.PreparedStatement; // Sentencia SQL precompilada y parametrizada contra Inyección SQL
import java.sql.ResultSet; // Cursor de resultados devuelto por una consulta JDBC
import java.sql.SQLException; // Excepción comprobada (Checked Exception) propia de JDBC
import java.time.LocalDate; // Fecha Java 8+
import java.util.ArrayList; // Lista dinámica para poblar resultados de consultas
import java.util.List; // Interfaz List
import java.util.Optional; // Contenedor Java 8+ para expresar de forma segura que una búsqueda puede no devolver fila

import javax.annotation.Resource; // Inyección JEE de recursos del servidor de aplicaciones (como el DataSource JNDI)
import javax.enterprise.context.ApplicationScoped; // Bean CDI Singleton en Jakarta EE (equivalente a @Repository en Spring)
import javax.persistence.EntityManager; // Interfaz central de JPA para interactuar con el contexto de persistencia
import javax.persistence.PersistenceContext; // Inyecta el EntityManager gestionado por el contenedor JEE o Spring
import javax.persistence.TypedQuery; // Consulta JPQL fuertemente tipada en tiempo de compilación
import javax.sql.DataSource; // Pool de conexiones configurado en el servidor (WildFly/JBoss/Tomcat o HikariCP en Spring Boot)

import es.seresco.agro.roperuelos.model.ExpedienteAgrarioEntity; // Entidad principal del dominio
import es.seresco.agro.roperuelos.model.ExpedienteAgrarioEntity.EstadoExpediente; // Enumerado de estados

/**
 * Repositorio / DAO Híbrido que demuestra las 3 formas de acceso a datos que te pueden preguntar
 * en la entrevista técnica de Seresco:
 *  1) JPA / Hibernate con JPQL y JOIN FETCH (evitando el problema de las N+1 queries).
 *  2) Consultas SQL Nativas desde el EntityManager para agregaciones rápidas.
 *  3) JDBC puro con DataSource, try-with-resources y PreparedStatement (muy usado en módulos legacy y reporting).
 */
@ApplicationScoped // En JEE/CDI crea una única instancia compartida; en Spring Boot equivale exactamente a @Repository
public class ExpedienteRepository {

    // Inyección estándar JPA del EntityManager (funciona idéntico tanto en Jakarta EE / WildFly como en Spring Boot)
    @PersistenceContext(unitName = "AgroRoperuelosPU")
    private EntityManager em;

    // Inyección del Pool de Conexiones JNDI del servidor de aplicaciones (en Spring se puede inyectar con @Autowired DataSource)
    @Resource(lookup = "java:/jdbc/AgroRoperuelosDS")
    private DataSource dataSource;

    // =========================================================================
    // 1. OPERACIONES CRUD Y BÚSQUEDA OPTIMIZADA CON JPA / JPQL (SIN N+1 QUERIES)
    // =========================================================================

    /**
     * Guarda un expediente nuevo (INSERT) o actualiza uno existente (UPDATE) en el contexto de persistencia.
     */
    public ExpedienteAgrarioEntity guardar(ExpedienteAgrarioEntity expediente) {
        if (expediente.getId() == null) { // Si el ID es nulo, la entidad está en estado Transient (nueva)
            em.persist(expediente);       // Registra la entidad en el EntityManager para hacer INSERT
            return expediente;            // Devuelve la misma instancia (ahora en estado Managed)
        } else {                          // Si ya tiene ID, viene de una vista JSF (@ViewScoped) en estado Detached
            return em.merge(expediente);  // Une los cambios al contexto de persistencia para ejecutar el UPDATE
        }
    }

    /**
     * Recupera un expediente junto con su Titular y todas sus Parcelas en UNA SOLA CONSULTA SQL
     * utilizando JOIN FETCH para evitar el problema de las N+1 queries y la LazyInitializationException en JSF.
     */
    public Optional<ExpedienteAgrarioEntity> buscarPorCodigoConDetalleCompleto(String codigoExpediente) {
        // Usamos DISTINCT para que el producto cartesiano del LEFT JOIN con parcelas no duplique la referencia del padre en Java
        String jpql = "SELECT DISTINCT e " +
                      "FROM ExpedienteAgrarioEntity e " +
                      "JOIN FETCH e.titular t " +                 // Carga ansiosa controlada del Titular en el mismo SELECT
                      "LEFT JOIN FETCH e.parcelasAsociadas p " +  // LEFT JOIN FETCH porque un expediente en borrador podría tener 0 parcelas aún
                      "WHERE e.codigoExpediente = :codigo";       // Parámetro con nombre (:codigo) seguro frente a Inyección SQL

        List<ExpedienteAgrarioEntity> resultados = em.createQuery(jpql, ExpedienteAgrarioEntity.class)
                .setParameter("codigo", codigoExpediente) // Enlaza el valor del parámetro de forma segura
                .getResultList();                         // Ejecuta la consulta y devuelve la lista hidratada

        // Usamos stream().findFirst() en lugar de getSingleResult() para no lanzar NoResultException si no existe
        return resultados.stream().findFirst();
    }

    /**
     * Búsqueda multicriterio para alimentar la tabla paginada (<p:dataTable>) de la vista JSF.
     * Permite filtrar opcionalmente por campaña agrícola, NIF del agricultor y estado del expediente.
     */
    public List<ExpedienteAgrarioEntity> buscarPorFiltrosBandejaJsf(
            Integer campania,
            String nifTitular,
            EstadoExpediente estado) {

        // Construimos la consulta JPQL usando StringBuilder de forma limpia y eficiente
        StringBuilder jpql = new StringBuilder(
            "SELECT e FROM ExpedienteAgrarioEntity e " +
            "JOIN FETCH e.titular t " + // Traemos siempre los datos del titular para pintarlos en las columnas de la tabla JSF
            "WHERE 1 = 1 "              // Truco clásico para concatenar cláusulas AND dinámicas limpiamente
        );

        if (campania != null) {
            jpql.append("AND e.campaniaAgricola = :campania "); // Añade filtro por campaña si el usuario lo seleccionó
        }
        if (nifTitular != null && !nifTitular.trim().isEmpty()) {
            jpql.append("AND UPPER(t.nifCif) LIKE :nif ");      // Búsqueda insensible a mayúsculas/minúsculas
        }
        if (estado != null) {
            jpql.append("AND e.estado = :estado ");             // Filtro por estado del enumerado
        }
        jpql.append("ORDER BY e.fechaSolicitud DESC, e.id DESC"); // Orden cronológico inverso (los más recientes primero)

        // Creamos el TypedQuery a partir de la cadena JPQL construida
        TypedQuery<ExpedienteAgrarioEntity> query = em.createQuery(jpql.toString(), ExpedienteAgrarioEntity.class);

        // Asignamos únicamente los parámetros que estaban presentes en el filtro
        if (campania != null) {
            query.setParameter("campania", campania);
        }
        if (nifTitular != null && !nifTitular.trim().isEmpty()) {
            query.setParameter("nif", "%" + nifTitular.trim().toUpperCase() + "%");
        }
        if (estado != null) {
            query.setParameter("estado", estado);
        }

        return query.getResultList(); // Devuelve la lista lista para mostrarse en el Managed Bean de JSF
    }

    // =========================================================================
    // 2. CONSULTA SQL NATIVA CON JPA (PARA ESTADÍSTICAS Y AGREGACIONES COMPLEJAS)
    // =========================================================================

    /**
     * Calcula la suma total de hectáreas de REGADÍO frente a SECANO de un polígono catastral
     * usando SQL Nativo parametrizado sobre PostgreSQL / MySQL.
     */
    public BigDecimal calcularSuperficieAprobadaPorPoligonoYCultivo(int poligono, String tipoCultivo, int campania) {
        String sqlNativo =
            "SELECT COALESCE(SUM(pe.superficie_declarada_ha), 0) " + // COALESCE garantiza devolver 0 en vez de NULL si no hay filas
            "FROM parcelas_expediente pe " +
            "INNER JOIN expedientes_municipales em ON em.id_expediente = pe.id_expediente " +
            "WHERE pe.poligono = :poligono " +
            "  AND pe.tipo_cultivo = :tipoCultivo " +
            "  AND em.campania_agricola = :campania " +
            "  AND em.estado_expediente = 'APROBADO'";

        Object resultado = em.createNativeQuery(sqlNativo)
                .setParameter("poligono", poligono)       // Parámetro seguro en NativeQuery
                .setParameter("tipoCultivo", tipoCultivo) // "REGADIO" o "SECANO"
                .setParameter("campania", campania)       // Año de campaña
                .getSingleResult();                       // Siempre devuelve 1 fila gracias a SUM() + COALESCE()

        // Convertimos el Number devuelto por el driver SQL a BigDecimal
        return (resultado instanceof BigDecimal)
                ? (BigDecimal) resultado
                : new BigDecimal(resultado.toString());
    }

    // =========================================================================
    // 3. ACCESO CON JDBC PURO (PreparedStatement + try-with-resources)
    // =========================================================================

    /**
     * DTO ligero (Data Transfer Object) pensado para alimentar informes de Jasper Reports
     * mediante JRBeanCollectionDataSource o listados rápidos sin sobrecargar la memoria de Hibernate.
     */
    public static class ResumenCertificadoCatastralDTO {
        private final String codigoExpediente;
        private final String nifTitular;
        private final String nombreTitular;
        private final int poligono;
        private final int parcela;
        private final int recintoSigpac;
        private final String tipoCultivo;
        private final BigDecimal superficieHa;
        private final LocalDate fechaResolucion;

        public ResumenCertificadoCatastralDTO(String codigoExpediente, String nifTitular, String nombreTitular,
                int poligono, int parcela, int recintoSigpac, String tipoCultivo,
                BigDecimal superficieHa, LocalDate fechaResolucion) {
            this.codigoExpediente = codigoExpediente;
            this.nifTitular = nifTitular;
            this.nombreTitular = nombreTitular;
            this.poligono = poligono;
            this.parcela = parcela;
            this.recintoSigpac = recintoSigpac;
            this.tipoCultivo = tipoCultivo;
            this.superficieHa = superficieHa;
            this.fechaResolucion = fechaResolucion;
        }

        // Getters públicos requeridos por Jasper Reports (JRBeanCollectionDataSource accede por reflexión a getXxx())
        public String getCodigoExpediente() { return codigoExpediente; }
        public String getNifTitular() { return nifTitular; }
        public String getNombreTitular() { return nombreTitular; }
        public int getPoligono() { return poligono; }
        public int getParcela() { return parcela; }
        public int getRecintoSigpac() { return recintoSigpac; }
        public String getTipoCultivo() { return tipoCultivo; }
        public BigDecimal getSuperficieHa() { return superficieHa; }
        public LocalDate getFechaResolucion() { return fechaResolucion; }
    }

    /**
     * Ejemplo de consulta JDBC de alto rendimiento usando PreparedStatement y try-with-resources.
     * En Seresco valoran mucho que sepas escribir JDBC limpio porque muchas aplicaciones JEE
     * combinan Hibernate con consultas JDBC directas para informes de Jasper Reports.
     */
    public List<ResumenCertificadoCatastralDTO> obtenerDatosCertificadoPorTitularJdbc(
            String nifTitular,
            int campaniaAgricola) throws SQLException {

        // Consulta SQL parametrizada con marcadores '?' (impide cualquier intento de Inyección SQL)
        final String sql =
            "SELECT em.codigo_expediente, t.nif_cif, t.nombre_completo, " +
            "       pe.poligono, pe.parcela, pe.recinto_sigpac, pe.tipo_cultivo, " +
            "       pe.superficie_declarada_ha, em.fecha_resolucion " +
            "FROM expedientes_municipales em " +
            "INNER JOIN titulares t ON t.id_titular = em.id_titular " +
            "INNER JOIN parcelas_expediente pe ON pe.id_expediente = em.id_expediente " +
            "WHERE t.nif_cif = ? " +
            "  AND em.campania_agricola = ? " +
            "  AND em.estado_expediente = 'APROBADO' " +
            "ORDER BY pe.poligono ASC, pe.parcela ASC, pe.recinto_sigpac ASC";

        List<ResumenCertificadoCatastralDTO> filasInforme = new ArrayList<>();

        // Bloque try-with-resources: cierra automáticamente ResultSet, PreparedStatement y devuelve la Connection al Pool
        try (Connection conn = dataSource.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {

            // Asignación tipada de los parámetros posicionales (en JDBC los índices empiezan en 1)
            ps.setString(1, nifTitular.trim().toUpperCase()); // Parámetro 1: NIF del agricultor
            ps.setInt(2, campaniaAgricola);                   // Parámetro 2: Año de la campaña

            // Ejecutamos la consulta y abrimos el ResultSet dentro de otro try-with-resources anidado
            try (ResultSet rs = ps.executeQuery()) {
                while (rs.next()) { // Recorremos fila a fila el cursor de base de datos
                    Date sqlFechaRes = rs.getDate("fecha_resolucion"); // Puede ser NULL en base de datos
                    LocalDate fechaResolucion = (sqlFechaRes != null) ? sqlFechaRes.toLocalDate() : null;

                    ResumenCertificadoCatastralDTO dto = new ResumenCertificadoCatastralDTO(
                        rs.getString("codigo_expediente"),
                        rs.getString("nif_cif"),
                        rs.getString("nombre_completo"),
                        rs.getInt("poligono"),
                        rs.getInt("parcela"),
                        rs.getInt("recinto_sigpac"),
                        rs.getString("tipo_cultivo"),
                        rs.getBigDecimal("superficie_declarada_ha"),
                        fechaResolucion
                    );
                    filasInforme.add(dto); // Añadimos el DTO a la colección que alimentará Jasper Reports
                }
            }
        }
        return filasInforme;
    }
}
```

---
## ARCHIVO: ExpedienteService.java

```java
package es.seresco.agro.roperuelos.service; // Paquete de lógica de negocio y coordinación transaccional

import java.math.BigDecimal; // Precisión exacta para validaciones de hectáreas e importes
import java.math.RoundingMode; // Redondeo financiero/agrario estándar (HALF_UP)
import java.sql.SQLException; // Excepción de acceso a datos JDBC
import java.time.LocalDate; // Fecha de resolución y auditoría
import java.util.List; // Colecciones de expedientes y DTOs
import java.util.logging.Level; // Niveles de log estándar (INFO, WARNING, SEVERE)
import java.util.logging.Logger; // Logger estándar en servidores JEE (WildFly/JBoss)

import javax.enterprise.context.ApplicationScoped; // Bean CDI de negocio (equivalente a @Service en Spring Boot)
import javax.inject.Inject; // Inyección de dependencias estándar JSR-330 / CDI (equivalente a @Autowired en Spring)
import javax.transaction.Transactional; // Gestión declarativa de transacciones JTA/JEE (y equivalente directo en Spring)

import es.seresco.agro.roperuelos.model.ExpedienteAgrarioEntity; // Entidad de expediente
import es.seresco.agro.roperuelos.model.ExpedienteAgrarioEntity.EstadoExpediente; // Estados válidos
import es.seresco.agro.roperuelos.model.ExpedienteAgrarioEntity.ParcelaExpedienteStub; // Entidad hija de parcela
import es.seresco.agro.roperuelos.repository.ExpedienteRepository; // Capa de acceso a datos
import es.seresco.agro.roperuelos.repository.ExpedienteRepository.ResumenCertificadoCatastralDTO; // DTO para Jasper Reports

/**
 * Servicio de Negocio que encapsula las reglas de validación agraria/administrativa
 * del Ayuntamiento de Roperuelos del Páramo y delimita las transacciones ACID.
 */
@ApplicationScoped // Instancia única de servicio gestionada por el contenedor
public class ExpedienteService {

    // Logger para trazabilidad operativa en los ficheros server.log de WildFly/Tomcat
    private static final Logger LOG = Logger.getLogger(ExpedienteService.class.getName());

    // Constantes de negocio reales: coeficientes de cálculo por hectárea de secano y regadío en el Páramo
    private static final BigDecimal MODULO_EUR_POR_HA_REGADIO = new BigDecimal("245.50");
    private static final BigDecimal MODULO_EUR_POR_HA_SECANO  = new BigDecimal("110.00");

    // Inyección del repositorio de datos (en Spring se puede usar @Autowired o constructor)
    @Inject
    private ExpedienteRepository expedienteRepository;

    /**
     * Excepción de negocio personalizada (Unchecked) para rechazar operaciones inválidas
     * garantizando rollback automático de la transacción activa y mensaje claro en la vista JSF.
     */
    public static class ReglaNegocioAgrarioException extends RuntimeException {
        private static final long serialVersionUID = 1L;
        public ReglaNegocioAgrarioException(String mensaje) {
            super(mensaje);
        }
    }

    // =========================================================================
    // 1. CONSULTA PARA LA PANTALLA JSF (LECTURA OPTIMIZADA)
    // =========================================================================

    /**
     * Busca expedientes según los filtros introducidos por el administrativo en la pantalla JSF.
     */
    public List<ExpedienteAgrarioEntity> buscarExpedientesBandeja(
            Integer campania,
            String nifTitular,
            EstadoExpediente estado) {

        LOG.log(Level.INFO, "Buscando expedientes agrarios [campania={0}, nif={1}, estado={2}]",
                new Object[]{campania, nifTitular, estado});

        // Delega en la consulta JPQL con JOIN FETCH del repositorio para evitar N+1 queries
        return expedienteRepository.buscarPorFiltrosBandejaJsf(campania, nifTitular, estado);
    }

    // =========================================================================
    // 2. REGISTRO Y VALIDACIÓN TRANSACCIONAL DE UN EXPEDIENTE AGRARIO
    // =========================================================================

    /**
     * Registra o actualiza un expediente validando las parcelas rústicas declaradas y calculando
     * automáticamente la superficie total (ha) y el importe correspondiente según cultivo (Regadío/Secano).
     *
     * @Transactional(rollbackOn = Exception.class) asegura que ante CUALQUIER excepción (tanto RuntimeException
     * como Checked Exception) se deshagan todos los cambios en la base de datos manteniendo la atomicidad ACID.
     */
    @Transactional(rollbackOn = Exception.class)
    public ExpedienteAgrarioEntity registrarOActualizarExpediente(ExpedienteAgrarioEntity expediente) {
        // 1. Validaciones defensivas de integridad funcional
        if (expediente == null) {
            throw new ReglaNegocioAgrarioException("El expediente no puede ser nulo.");
        }
        if (expediente.getTitular() == null || expediente.getTitular().getNifCif() == null) {
            throw new ReglaNegocioAgrarioException("Todo expediente debe tener un titular agrario con NIF/CIF válido.");
        }
        if (expediente.getParcelasAsociadas() == null || expediente.getParcelasAsociadas().isEmpty()) {
            throw new ReglaNegocioAgrarioException("El expediente debe incluir al menos una parcela rústica (polígono/parcela/recinto SIGPAC).");
        }

        // 2. Validación de cada recinto SIGPAC y cálculo de superficie e importe económico
        BigDecimal sumaHectareas = BigDecimal.ZERO;
        BigDecimal importeCalculado = BigDecimal.ZERO;

        for (ParcelaExpedienteStub parcela : expediente.getParcelasAsociadas()) {
            // Verificamos que polígono, parcela y recinto sean estrictamente positivos
            if (parcela.getPoligono() == null || parcela.getPoligono() <= 0 ||
                parcela.getParcela() == null || parcela.getParcela() <= 0 ||
                parcela.getRecintoSigpac() == null || parcela.getRecintoSigpac() <= 0) {
                throw new ReglaNegocioAgrarioException(
                    "Referencia catastral/SIGPAC inválida: Polígono, Parcela y Recinto deben ser mayores que cero."
                );
            }

            // Verificamos que la superficie declarada sea mayor que 0.0000 ha
            BigDecimal supHa = parcela.getSuperficieDeclaradaHa();
            if (supHa == null || supHa.compareTo(BigDecimal.ZERO) <= 0) {
                throw new ReglaNegocioAgrarioException(
                    String.format("La superficie del Polígono %d - Parcela %d debe ser mayor que 0 hectáreas.",
                            parcela.getPoligono(), parcela.getParcela())
                );
            }

            // Acumulamos las hectáreas con precisión de 4 decimales
            sumaHectareas = sumaHectareas.add(supHa);

            // Aplicamos el módulo económico según sea cultivo de REGADÍO del Páramo o SECANO
            BigDecimal moduloAplicable = "REGADIO".equalsIgnoreCase(parcela.getTipoCultivo())
                    ? MODULO_EUR_POR_HA_REGADIO
                    : MODULO_EUR_POR_HA_SECANO;

            importeCalculado = importeCalculado.add(supHa.multiply(moduloAplicable));
        }

        // 3. Asignamos los totales calculados y redondeamos el importe a 2 decimales (HALF_UP)
        expediente.setSuperficieTotalDeclaradaHa(sumaHectareas.setScale(4, RoundingMode.HALF_UP));
        expediente.setImporteEconomicoEur(importeCalculado.setScale(2, RoundingMode.HALF_UP));

        // 4. Persistimos el expediente y sus líneas de parcela dentro de la transacción activa
        ExpedienteAgrarioEntity guardado = expedienteRepository.guardar(expediente);
        LOG.log(Level.INFO, "Expediente {0} guardado con éxito. Superficie total: {1} ha | Importe: {2} EUR",
                new Object[]{guardado.getCodigoExpediente(), guardado.getSuperficieTotalDeclaradaHa(), guardado.getImporteEconomicoEur()});

        return guardado;
    }

    // =========================================================================
    // 3. APROBACIÓN DE EXPEDIENTE PARA HABILITAR EMISIÓN DE CERTIFICADO JASPER
    // =========================================================================

    /**
     * Cambia el estado de un expediente a APROBADO tras la validación técnica del secretario/técnico municipal.
     * Como la entidad recuperada dentro del método @Transactional está en estado MANAGED,
     * el Dirty Checking de Hibernate ejecuta automáticamente el UPDATE al terminar el método.
     */
    @Transactional(rollbackOn = Exception.class)
    public ExpedienteAgrarioEntity aprobarExpediente(String codigoExpediente, String observacionesSecretaria) {
        // Buscamos el expediente con su detalle completo (JOIN FETCH)
        ExpedienteAgrarioEntity expediente = expedienteRepository
                .buscarPorCodigoConDetalleCompleto(codigoExpediente)
                .orElseThrow(() -> new ReglaNegocioAgrarioException(
                        "No existe ningún expediente con el código: " + codigoExpediente));

        // Regla de estado: Un expediente denegado no puede aprobarse directamente sin reabrirse antes
        if (expediente.getEstado() == EstadoExpediente.DENEGADO) {
            throw new ReglaNegocioAgrarioException(
                    "El expediente " + codigoExpediente + " está DENEGADO y requiere apertura de recurso antes de aprobarse.");
        }

        // Recalculamos defensivamente la superficie de sus parcelas
        expediente.recalcularSuperficieTotal();
        if (expediente.getSuperficieTotalDeclaradaHa().compareTo(BigDecimal.ZERO) <= 0) {
            throw new ReglaNegocioAgrarioException(
                    "No se puede aprobar un expediente con superficie total igual a 0 hectáreas.");
        }

        // Actualizamos el estado, la fecha oficial de resolución y las observaciones que saldrán en el PDF de Jasper Reports
        expediente.setEstado(EstadoExpediente.APROBADO);
        expediente.setFechaResolucion(LocalDate.now());
        expediente.setObservacionesTecnicas(observacionesSecretaria);

        LOG.log(Level.INFO, "Expediente {0} APROBADO en fecha {1}",
                new Object[]{codigoExpediente, expediente.getFechaResolucion()});

        return expediente; // Al cerrarse el método @Transactional, Hibernate hace flush y commit del UPDATE
    }

    // =========================================================================
    // 4. OBTENCIÓN DE DATOS PARA EL INFORME OFICIAL PDF DE JASPER REPORTS
    // =========================================================================

    /**
     * Obtiene las filas validadas mediante JDBC PreparedStatement para alimentar el Certificado
     * Municipal de Parcelas Rústicas en Jasper Reports.
     */
    public List<ResumenCertificadoCatastralDTO> obtenerDatosParaCertificadoJasper(String nifTitular, int campania) {
        try {
            List<ResumenCertificadoCatastralDTO> datos =
                    expedienteRepository.obtenerDatosCertificadoPorTitularJdbc(nifTitular, campania);

            if (datos.isEmpty()) {
                throw new ReglaNegocioAgrarioException(
                    String.format("El titular con NIF %s no tiene expedientes APROBADOS en la campaña %d para emitir certificado.",
                            nifTitular, campania)
                );
            }
            return datos;
        } catch (SQLException e) {
            LOG.log(Level.SEVERE, "Error SQL al extraer datos para el informe Jasper Reports del NIF " + nifTitular, e);
            throw new RuntimeException("Error técnico al consultar los datos catastrales para el certificado PDF.", e);
        }
    }
}
```

---
## ARCHIVO: 02_teoria_optimizacion_y_preguntas_sql.md

# 02 — TEORÍA, OPTIMIZACIÓN DE RENDIMIENTO Y 15 PREGUNTAS DE ENTREVISTA: SQL Y BASES DE DATOS RELACIONALES

> **Objetivo de este documento:** Dominar SQL de producción para entrevistas técnicas en Seresco (donde las aplicaciones Java/JEE y los informes de Jasper Reports dependen de consultas SQL complejas sobre PostgreSQL, Oracle, SQL Server y MySQL).

---

## 1. DOMINIO DE JOINS: `INNER JOIN`, `LEFT JOIN` Y CASOS REALES AGRARIOS

| Tipo de JOIN | Qué devuelve exactamente | Caso de uso real en Gestión Agraria / Catastral |
| :--- | :--- | :--- |
| **`INNER JOIN`** | Devuelve **solo las filas que tienen coincidencia en ambas tablas** según la condición `ON`. | Obtener los expedientes que tienen un titular asignado y al menos una parcela vinculada. |
| **`LEFT JOIN`** (`LEFT OUTER JOIN`) | Devuelve **todas las filas de la tabla izquierda** y las coincidencias de la derecha; si no hay coincidencia en la derecha, rellena sus columnas con `NULL`. | Listar **todos los agricultores del censo municipal** aunque todavía no hayan presentado ningún expediente en la campaña 2026. |
| **`LEFT JOIN ... WHERE derecha.id IS NULL`** (*Anti-Join*) | Devuelve **únicamente las filas de la tabla izquierda que NO tienen correspondencia** en la tabla derecha. | Detectar qué titulares rústicos con parcelas de regadío **NO** han solicitado aún la ayuda o certificado anual. |
| **`FULL OUTER JOIN`** | Devuelve todas las filas de ambas tablas, coincidan o no. | Cruzar el volcado externo del Catastro/SIGPAC contra el padrón interno del Ayuntamiento para detectar altas y bajas en ambos lados. |

> **Trampa de entrevista sobre `LEFT JOIN`:**  
> Si haces `LEFT JOIN expedientes_municipales e ON e.id_titular = t.id_titular` y pones el filtro `WHERE e.campania_agricola = 2026`, **conviertes accidentalmente el `LEFT JOIN` en un `INNER JOIN`**, porque para los titulares sin expediente `e.campania_agricola` vale `NULL` y el `WHERE` los elimina.  
> **Solución correcta:** Poner la condición dentro de la cláusula **`ON`** del `LEFT JOIN`:  
> `LEFT JOIN expedientes_municipales e ON e.id_titular = t.id_titular AND e.campania_agricola = 2026`.

---

## 2. AGREGACIONES: `WHERE` vs. `GROUP BY` vs. `HAVING`

El orden lógico en el que el motor SQL ejecuta una consulta (que **no** es el orden en que se escribe) es una pregunta fija de entrevista:
1. **`FROM` / `JOIN`**: Construye el conjunto de tablas origen y filtra por las condiciones `ON`.
2. **`WHERE`**: Filtra **filas individuales ANTES de agrupar**. *(Aquí NO se pueden usar funciones de agregación como `SUM()`, `COUNT()`, `AVG()`)*.
3. **`GROUP BY`**: Agrupa las filas supervivientes en cubos según las columnas indicadas.
4. **`HAVING`**: Filtra **grupos enteros DESPUÉS de haber ejecutado el `GROUP BY`**. *(Aquí SÍ se usan `HAVING SUM(superficie_ha) > 10.0000` o `HAVING COUNT(*) > 1`)*.
5. **`SELECT`**: Calcula las expresiones de salida y las funciones ventana (`OVER(...)`).
6. **`DISTINCT`**: Elimina filas duplicadas de la proyección.
7. **`ORDER BY`**: Ordena el resultado final (aquí ya puedes usar los alias definidos en el `SELECT`).
8. **`LIMIT` / `OFFSET` (`FETCH FIRST n ROWS ONLY`)**: Paginación del resultado.

---

## 3. SUBCONSULTAS vs. CTEs (`WITH`) Y FUNCIONES VENTANA (`OVER`)

### 3.1. Por qué preferir CTEs (`WITH`) frente a subconsultas anidadas
- **Subconsulta Correlacionada (Mala práctica en tablas grandes):** Es una subconsulta en el `SELECT` o `WHERE` que depende de una columna de la fila externa y se re-ejecuta fila por fila (comportamiento $O(N^2)$ similar al N+1).
- **CTE (*Common Table Expression* — `WITH nombre_cte AS (...)`):**
  - Divide una consulta compleja (por ejemplo, el origen de datos de un informe de **Jasper Reports**) en bloques lógicos legibles, reutilizables y fáciles de depurar paso a paso.
  - Permite además hacer consultas jerárquicas con `WITH RECURSIVE`.

### 3.2. Funciones Ventana (*Window Functions*): `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `SUM() OVER()`
A diferencia de `GROUP BY` (que colapsa varias filas en una sola fila resumen), las **funciones ventana calculan agregados o rankings manteniendo intactas todas las filas originales de detalle**:
- **`ROW_NUMBER() OVER (PARTITION BY id_titular ORDER BY superficie_ha DESC)`**: Numera las parcelas de cada agricultor de mayor a menor superficie (1, 2, 3...) sin repetir número en caso de empate. Ideal para sacar "la parcela más grande de cada titular" filtrando luego `WHERE rn = 1`.
- **`RANK()` vs `DENSE_RANK()`**: Si dos parcelas empatan en el primer puesto con `5.0000 ha`, `RANK()` asigna `1, 1, 3` (salta el 2), mientras que `DENSE_RANK()` asigna `1, 1, 2` (sin huecos).
- **`SUM(superficie_ha) OVER (PARTITION BY poligono)`**: Muestra en cada fila de una parcela su superficie individual y, al lado, la superficie total del polígono al que pertenece, permitiendo calcular el `% de participación` de esa parcela dentro del polígono en una sola pasada de lectura.

---

## 4. ÍNDICES Y OPTIMIZACIÓN DE CONSULTAS SQL (CÓMO RESPONDER «¿QUÉ HACES SI UNA QUERY VA LENTA?»)

### 4.1. Cuándo crear un Índice B-Tree (y cuándo NO)
Se deben indexar:
1. Todas las **Claves Primarias (`PRIMARY KEY`)** y restricciones **`UNIQUE`** (el motor las indexa automáticamente).
2. Todas las **Claves Foráneas (`FOREIGN KEY`)** como `id_titular` o `id_expediente` *(ojo: PostgreSQL, Oracle y SQL Server NO crean índices automáticos en las Foreign Keys; si no los creas tú, los `JOIN` y los `DELETE` en la tabla padre harán un *Full Table Scan*)*.
3. Las columnas con **alta selectividad (alta cardinalidad)** más utilizadas en filtros **`WHERE`**, agrupaciones **`GROUP BY`** y ordenaciones **`ORDER BY`** (creando índices compuestos con la columna de igualdad más selectiva primero).
- **Cuándo NO abusar de los índices:** Cada índice adicional ralentiza las operaciones de escritura (`INSERT`, `UPDATE`, `DELETE`) porque el motor debe actualizar tanto la tabla como todos sus árboles B-Tree. Tampoco son útiles en tablas diminutas o en columnas booleanas con distribución 50%/50%.

### 4.2. Los 5 Errores Clásicos que ROMPEN el uso de un Índice en un `WHERE` (Consultas *Non-SARGable*)
Si un entrevistador de Seresco te pregunta *«La columna `fecha_solicitud` o `nif_cif` tiene índice, pero la consulta sigue haciendo un *Seq Scan / Full Table Scan*, ¿por qué?»*, estas son las 5 causas:
1. **Aplicar funciones sobre la columna indexada en el `WHERE`:**
   - ❌ Mal (rompe el índice): `WHERE EXTRACT(YEAR FROM fecha_solicitud) = 2024`
   - ✅ Bien (usa el índice B-Tree por rango): `WHERE fecha_solicitud >= '2024-01-01' AND fecha_solicitud < '2025-01-01'`
   - ❌ Mal (sin índice funcional): `WHERE UPPER(nif_cif) = '12345678Z'` (salvo que crees un índice funcional `CREATE INDEX idx_nif_upper ON titulares(UPPER(nif_cif))`).
2. **Usar comodín inicial `%` en un `LIKE`:**
   - ❌ Mal: `WHERE codigo_expediente LIKE '%0089'` (no puede usar el árbol B-Tree porque no sabe por qué letra empieza).
   - ✅ Bien: `WHERE codigo_expediente LIKE 'EXP-2024-%'` (búsqueda por prefijo: sí recorre el árbol B-Tree).
3. **Conversiones implícitas de tipos de datos:**
   - Comparar una columna `VARCHAR` (como un código catastral) contra un número entero `WHERE codigo_catastral = 47001` obliga al motor a aplicar `CAST` a cada fila de la tabla, inutilizando el índice.
4. **Operadores negativos (`<>`, `!=`, `NOT IN`):**
   - Suelen forzar escaneo completo; `NOT EXISTS` es mucho más eficiente y seguro frente a valores `NULL` que `NOT IN`.
5. **Realizar operaciones aritméticas en el lado de la columna:**
   - ❌ Mal: `WHERE superficie_ha * 2 > 10`
   - ✅ Bien: `WHERE superficie_ha > 5`

---

## 5. VISTAS, TRIGGERS, PROCEDIMIENTOS ALMACENADOS Y TRANSACCIONES ACID

### 5.1. Vistas (`VIEW`) vs. Vistas Materializadas (`MATERIALIZED VIEW`)
- **Vista estándar (`CREATE VIEW v_certificado_parcelas_titular AS SELECT ...`):** Es una consulta almacenada que no ocupa espacio físico en disco; cada vez que la consultas desde Java o desde **Jasper Reports**, ejecuta el `SELECT` subyacente en tiempo real. Muy útil para desacoplar las plantillas `.jrxml` de cambios internos en las tablas.
- **Vista Materializada (`CREATE MATERIALIZED VIEW`):** Guarda físicamente en disco el resultado precalculado de una consulta pesada (y permite crear índices sobre ella), refrescándose periódicamente (`REFRESH MATERIALIZED VIEW`). Ideal para cuadros de mando por campaña agraria.

### 5.2. Ejemplo de Procedimiento Almacenado (`PROCEDURE`) de Cierre/Actualización Masiva por Campaña
```sql
CREATE OR REPLACE PROCEDURE sp_recalcular_importes_campania(
    p_campania INTEGER,
    p_modulo_regadio NUMERIC(12,2),
    p_modulo_secano  NUMERIC(12,2)
)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE expedientes_municipales em
    SET importe_tasa_o_ayuda_eur = ROUND(sub.importe_calculado, 2),
        superficie_total_declarada_ha = sub.hectareas_totales,
        fecha_ultima_modificacion = CURRENT_TIMESTAMP
    FROM (
        SELECT
            ep.id_expediente,
            SUM(ep.superficie_computada_ha) AS hectareas_totales,
            SUM(
                CASE
                    WHEN pr.tipo_cultivo = 'REGADIO' THEN ep.superficie_computada_ha * p_modulo_regadio
                    ELSE ep.superficie_computada_ha * p_modulo_secano
                END
            ) AS importe_calculado
        FROM expediente_parcelas ep
        INNER JOIN parcelas_rusticas pr ON pr.id_parcela = ep.id_parcela
        GROUP BY ep.id_expediente
    ) sub
    WHERE em.id_expediente = sub.id_expediente
      AND em.campania_agricola = p_campania
      AND em.estado_expediente <> 'DENEGADO';
END;
$$;
```

### 5.3. Las 4 Propiedades ACID de una Transacción
1. **Atomicidad (*Atomicity*):** Todo o nada. Si al aprobar un expediente se inserta el certificado emitido pero falla la actualización del estado, toda la transacción hace `ROLLBACK`.
2. **Consistencia (*Consistency*):** La base de datos pasa de un estado válido a otro estado válido respetando todas las `FOREIGN KEY`, `UNIQUE` y restricciones `CHECK (superficie_ha > 0)`.
3. **Aislamiento (*Isolation*):** Dos transacciones concurrentes no se interfieren (niveles `READ COMMITTED`, `REPEATABLE READ`, `SERIALIZABLE`).
4. **Durabilidad (*Durability*):** Una vez ejecutado el `COMMIT`, los datos quedan persistidos en el log transaccional (WAL / Redo Log) aunque se apague el servidor un milisegundo después.

---

## 6. LAS 15 PREGUNTAS DE ENTREVISTA SQL EN SERESCO (CON RESPUESTAS LISTAS PARA DECIR EN VOZ ALTA)

1. **¿Cuál es la diferencia entre `WHERE` y `HAVING`?**
   > "`WHERE` filtra filas individuales antes de agrupar con `GROUP BY` y no admite funciones de agregación; `HAVING` filtra los grupos ya formados después del `GROUP BY` usando funciones como `SUM()`, `COUNT()` o `AVG()`."
2. **¿Cuál es la diferencia entre `UNION` y `UNION ALL`?**
   > "`UNION` combina los resultados de dos consultas y además ordena/compara todas las filas para eliminar duplicados (lo que es costoso en CPU y memoria); `UNION ALL` concatena directamente ambos conjuntos sin eliminar duplicados, siendo mucho más rápido cuando sabemos que los conjuntos son disjuntos (por ejemplo, expedientes de 2023 y expedientes de 2024)."
3. **¿Por qué `NOT IN` es peligroso si la subconsulta puede devolver algún `NULL`, y por qué es mejor `NOT EXISTS`?**
   > "En lógica trivalente SQL, `valor NOT IN (10, 20, NULL)` equivale a `valor <> 10 AND valor <> 20 AND valor <> NULL`. Como cualquier comparación con `NULL` da `UNKNOWN`, **toda la consulta devuelve 0 filas**. En cambio, `NOT EXISTS` evalúa la existencia de filas de forma segura frente a nulos y aprovecha mejor los índices haciendo cortocircuito."
4. **¿Qué diferencia hay entre `DELETE`, `TRUNCATE` y `DROP`?**
   > "`DELETE` es DML, borra filas pudiendo filtrar con `WHERE`, dispara triggers `ON DELETE` y registra cada fila borrada en el log transaccional. `TRUNCATE` vacía toda la tabla de golpe liberando las páginas de datos sin recorrer fila a fila (muchísimo más rápido para tablas temporales de carga). `DROP` es DDL y elimina la tabla completa, su estructura, índices y permisos."
5. **¿Para qué sirve `COALESCE(col, valor_defecto)` y por qué es indispensable en informes de Jasper Reports?**
   > "`COALESCE` devuelve el primer argumento que no sea `NULL`. En consultas para informes o cálculos (`SUM(superficie_ha)`), si no hay filas coincidentes en un `LEFT JOIN`, `SUM` devuelve `NULL`; con `COALESCE(SUM(superficie_ha), 0)` garantizamos que siempre devuelva `0.0000` evitando celdas vacías o `NullPointerException` en Java."
6. **¿Qué diferencia hay entre `COUNT(*)` y `COUNT(columna)`?**
   > "`COUNT(*)` cuenta el número total de filas del grupo (incluyendo aquellas que tengan columnas en `NULL`), mientras que `COUNT(columna)` cuenta únicamente las filas donde esa columna concreta **no es `NULL`**; y `COUNT(DISTINCT columna)` cuenta valores únicos no nulos."
7. **¿Qué es una Clave Primaria Compuesta vs una Clave Subrogada (`id BIGSERIAL`) con restricción `UNIQUE`?**
   > "En el proyecto catastral preferí usar una clave primaria subrogada numérica (`id_parcela BIGSERIAL`) porque simplifica enormemente las relaciones `@ManyToOne` en JPA/Hibernate y ocupa solo 8 bytes en los índices de las tablas hijas, añadiendo además una restricción **`UNIQUE (codigo_provincia, codigo_municipio, poligono, parcela, recinto_sigpac)`** para garantizar la integridad de la clave natural de negocio."
8. **¿Qué significa `ON DELETE RESTRICT` vs `ON DELETE CASCADE` en una Foreign Key?**
   > "Con `ON DELETE RESTRICT` (el que puse entre `titulares` y `expedientes_municipales`), la base de datos impide borrar por error un titular si tiene expedientes históricos asociados. Con `ON DELETE CASCADE` (entre `expedientes_municipales` y sus líneas en `expediente_parcelas`), al borrar un expediente en borrador se borran automáticamente sus líneas de detalle."
9. **¿Cómo paginas una consulta SQL que devuelve 50.000 expedientes para un `<p:dataTable>` de PrimeFaces?**
   > "Siempre con ordenación determinista (`ORDER BY fecha_solicitud DESC, id_expediente DESC`) añadiendo `LIMIT :tamanoPagina OFFSET :desplazamiento` (en PostgreSQL/MySQL) o `OFFSET :desplazamiento ROWS FETCH NEXT :tamanoPagina ROWS ONLY` (estándar ANSI SQL / Oracle / SQL Server)."
10. **¿Qué miras dentro del resultado de un `EXPLAIN ANALYZE` para saber dónde está el cuello de botella?**
    > "Busco tres indicadores: primero, si aparecen nodos **`Seq Scan` (Full Table Scan)** sobre tablas grandes donde debería haber un **`Index Scan`** o `Bitmap Index Scan`; segundo, si el número de filas estimadas por el optimizador difiere mucho de las filas reales (`rows`), lo que indica estadísticas desactualizadas (`ANALYZE`); y tercero, si un `Sort` o `Hash Join` está volcando a disco temporal por falta de memoria (`work_mem`)."
11. **¿En qué orden debes colocar las columnas al crear un Índice Compuesto `CREATE INDEX idx ON tabla (colA, colB)`?**
    > "Sigue la regla **Igualdad primero, Rango después**: primero van las columnas por las que filtramos con igualdad exacta (`WHERE campania_agricola = 2024 AND estado_expediente = 'APROBADO'`) y al final la columna por la que filtramos por rango o fecha (`AND fecha_solicitud >= '2024-06-01'`) o por la que hacemos `ORDER BY`."
12. **¿Qué es un `Deadlock` (interbloqueo) en base de datos y cómo se previene desde Java?**
    > "Un *deadlock* ocurre cuando la Transacción 1 bloquea la Fila A y espera por la Fila B, mientras que la Transacción 2 bloquea la Fila B y espera por la Fila A. Se previene haciendo las transacciones `@Transactional` lo más cortas posible (sin llamadas HTTP ni generación pesada de ficheros en medio de escrituras) y actualizando las tablas y filas siempre en el mismo orden canónico (por ejemplo, ordenadas por `id ASC`)."
13. **¿Qué es la 3ª Forma Normal (3FN) y cuándo tiene sentido desnormalizar un dato?**
    > "Una base de datos está en 3FN cuando no hay grupos repetitivos (1FN), cada atributo depende de toda la clave primaria (2FN) y no existen dependencias transitivas entre columnas que no son clave (3FN). Sin embargo, en la tabla `expedientes_municipales` guardamos la columna calculada `superficie_total_declarada_ha` (una desnormalización controlada y auditada) para poder pintar y ordenar la bandeja JSF de miles de expedientes al instante sin hacer un `SUM()` con `GROUP BY` en cada recarga."
14. **¿Cómo evitas el error de división por cero (`Division by zero`) al calcular porcentajes en SQL?**
    > "Envolviendo siempre el divisor en **`NULLIF(divisor, 0)`**, por ejemplo: `ROUND((ha_regadio * 100.0) / NULLIF(ha_totales, 0), 2)`. Si `ha_totales` vale `0`, `NULLIF` devuelve `NULL`, la división devuelve `NULL` limpiamente sin romper la consulta, y con `COALESCE(..., 0)` mostramos `0.00%`."
15. **¿Qué nivel de aislamiento transaccional usan por defecto PostgreSQL, Oracle y SQL Server, y qué anomalía evita?**
    > "Usan **`READ COMMITTED`** por defecto: garantiza que ninguna consulta pueda leer datos sucios no confirmados por otra transacción (*Dirty Reads*), de modo que un informe de Jasper Reports nunca imprimirá datos de un expediente cuya transacción aún no ha hecho `COMMIT`."

---
## ARCHIVO: esquema_catastro_y_parcelas_rusticas.sql

```sql
-- =============================================================================
-- ARCHIVO: esquema_catastro_y_parcelas_rusticas.sql
-- PROYECTO: Sistema de Gestión Catastral, Parcelas Rústicas (SIGPAC) y
--           Expedientes Agrarios — Ayuntamiento de Roperuelos del Páramo (León)
-- MOTOR:   PostgreSQL / Compatible con estándar ANSI SQL (MySQL / Oracle / SQL Server)
-- AUTOR:   Diego de la Fuente Alonso
-- =============================================================================

-- 1. LIMPIEZA PREVIA DE OBJETOS (IDEMPOTENCIA PARA ENTORNOS DEV / QAS)
DROP VIEW IF EXISTS v_certificado_parcelas_titular;
DROP TABLE IF EXISTS auditoria_cambios_expediente;
DROP TABLE IF EXISTS certificados_emitidos;
DROP TABLE IF EXISTS expediente_parcelas;
DROP TABLE IF EXISTS expedientes_municipales;
DROP TABLE IF EXISTS parcelas_rusticas;
DROP TABLE IF EXISTS titulares;

-- =============================================================================
-- 2. TABLA MAESTRA DE TITULARES AGRARIOS / VECINOS CATASTRALES
-- =============================================================================
CREATE TABLE titulares (
    id_titular            BIGSERIAL PRIMARY KEY,                     -- Identificador único autoincremental (PK)
    nif_cif               VARCHAR(15)  NOT NULL UNIQUE,              -- DNI/NIF (personas físicas) o CIF (cooperativas/SAT/Juntas Vecinales)
    nombre_completo       VARCHAR(150) NOT NULL,                     -- Nombre y apellidos o razón social
    tipo_persona          VARCHAR(20)  NOT NULL DEFAULT 'FISICA'     -- 'FISICA', 'JURIDICA_SAT', 'ENTIDAD_LOCAL_MENOR'
                          CHECK (tipo_persona IN ('FISICA', 'JURIDICA_SAT', 'ENTIDAD_LOCAL_MENOR')),
    nucleo_poblacion      VARCHAR(80)  NOT NULL DEFAULT 'Roperuelos del Páramo', -- Roperuelos del Páramo, Moscas del Páramo o Valcabado del Páramo
    direccion_postal      VARCHAR(200),                              -- Domicilio a efectos de notificaciones administrativas
    telefono_contacto     VARCHAR(20),                               -- Teléfono móvil/fijo
    email                 VARCHAR(120),                              -- Correo electrónico para sede electrónica
    activo                BOOLEAN      NOT NULL DEFAULT TRUE,        -- Baja lógica (nunca se borran titulares con histórico fiscal/catastral)
    fecha_alta_padron     DATE         NOT NULL DEFAULT CURRENT_DATE -- Fecha de alta en el registro municipal
);

-- Índice funcional sobre el NIF en mayúsculas y el nombre para búsquedas rápidas desde la pantalla JSF
CREATE INDEX idx_titulares_nombre ON titulares (nombre_completo);
CREATE INDEX idx_titulares_nucleo ON titulares (nucleo_poblacion);

-- =============================================================================
-- 3. TABLA DE PARCELAS RÚSTICAS Y RECINTOS SIGPAC DEL TÉRMINO MUNICIPAL
-- =============================================================================
CREATE TABLE parcelas_rusticas (
    id_parcela            BIGSERIAL PRIMARY KEY,                     -- PK interna de la parcela/recinto
    id_titular            BIGINT       NOT NULL,                     -- FK hacia el titular catastral o explotador actual
    codigo_provincia      INTEGER      NOT NULL DEFAULT 24,          -- 24 = León (47 = Valladolid en proyectos ITACyL/Junta)
    codigo_municipio      INTEGER      NOT NULL DEFAULT 136,         -- Código INE/Catastral del municipio
    poligono              INTEGER      NOT NULL CHECK (poligono > 0),-- Número de Polígono rústico (ej. Polígonos 101 a 118 de concentración parcelaria)
    parcela               INTEGER      NOT NULL CHECK (parcela > 0), -- Número de Parcela dentro del polígono
    recinto_sigpac        INTEGER      NOT NULL DEFAULT 1 CHECK (recinto_sigpac > 0), -- Subdivisión SIGPAC dentro de la parcela
    paraje_nombre         VARCHAR(100) NOT NULL,                     -- Nombre tradicional del paraje (ej. "El Páramo Alto", "La Vega", "Las Chanas")
    referencia_catastral  VARCHAR(20)  NOT NULL UNIQUE,              -- Referencia catastral oficial de 20 caracteres
    tipo_cultivo          VARCHAR(30)  NOT NULL                      -- Sistema de explotación: SECANO o REGADIO
                          CHECK (tipo_cultivo IN ('REGADIO', 'SECANO', 'PASTO_COMUNAL')),
    uso_sigpac            VARCHAR(10)  NOT NULL DEFAULT 'TA'         -- Código SIGPAC: 'TA' (Tierras Arables), 'PR' (Pasto Arbustivo), 'FO' (Forestal)
                          CHECK (uso_sigpac IN ('TA', 'TH', 'PR', 'PS', 'FO', 'IM')),
    cultivo_declarado     VARCHAR(60)  NOT NULL,                     -- Ej: 'MAIZ', 'ALUBIA', 'REMOLACHA', 'TRIGO_BLANDO', 'CEBADA'
    regimen_tenencia      VARCHAR(30)  NOT NULL DEFAULT 'PROPIEDAD'  -- 'PROPIEDAD', 'ARRENDAMIENTO', 'CESION_COMUNAL'
                          CHECK (regimen_tenencia IN ('PROPIEDAD', 'ARRENDAMIENTO', 'CESION_COMUNAL', 'APARCERIA')),
    superficie_ha         NUMERIC(10,4) NOT NULL CHECK (superficie_ha > 0), -- Precisión exacta a 4 decimales (1 centiárea = 0.0001 ha)
    comunidad_regantes    VARCHAR(100),                              -- Ej: 'Comunidad de Regantes del Páramo Bajo / Canal del Páramo'
    activa                BOOLEAN      NOT NULL DEFAULT TRUE,        -- Estado de vigencia catastral

    -- Restricción de integridad referencial hacia titulares
    CONSTRAINT fk_parcela_titular
        FOREIGN KEY (id_titular) REFERENCES titulares (id_titular)
        ON UPDATE CASCADE ON DELETE RESTRICT,

    -- Clave candidata natural única para evitar duplicar el mismo recinto SIGPAC en el municipio
    CONSTRAINT uq_sigpac_municipio_pol_par_rec
        UNIQUE (codigo_provincia, codigo_municipio, poligono, parcela, recinto_sigpac)
);

-- Índices críticos para cruces JOIN y filtros por polígono/cultivo
CREATE INDEX idx_parcelas_id_titular ON parcelas_rusticas (id_titular);
CREATE INDEX idx_parcelas_poligono_cultivo ON parcelas_rusticas (poligono, tipo_cultivo);

-- =============================================================================
-- 4. TABLA DE EXPEDIENTES ADMINISTRATIVOS MUNICIPALES / AGRARIOS
-- =============================================================================
CREATE TABLE expedientes_municipales (
    id_expediente                 BIGSERIAL PRIMARY KEY,             -- PK del expediente
    codigo_expediente             VARCHAR(30)   NOT NULL UNIQUE,     -- Clave natural visible (ej. 'EXP-ROP-2024-0001')
    id_titular                    BIGINT        NOT NULL,            -- FK al titular solicitante
    campania_agricola             INTEGER       NOT NULL CHECK (campania_agricola BETWEEN 2020 AND 2035),
    tipo_tramite                  VARCHAR(80)   NOT NULL,            -- 'CERTIFICADO_BIENES_RUSTICOS', 'ADJUDICACION_LOTES_COMUNALES', 'DECLARACION_REGADIO'
    estado_expediente             VARCHAR(30)   NOT NULL DEFAULT 'BORRADOR'
                                  CHECK (estado_expediente IN ('BORRADOR', 'EN_REVISION_TECNICA', 'SUBSANACION', 'APROBADO', 'DENEGADO')),
    superficie_total_declarada_ha NUMERIC(10,4) NOT NULL DEFAULT 0.0000 CHECK (superficie_total_declarada_ha >= 0),
    importe_tasa_o_ayuda_eur      NUMERIC(12,2) NOT NULL DEFAULT 0.00   CHECK (importe_tasa_o_ayuda_eur >= 0),
    fecha_solicitud               DATE          NOT NULL DEFAULT CURRENT_DATE,
    fecha_resolucion              DATE,                              -- Se rellena cuando pasa a APROBADO o DENEGADO
    observaciones_tecnicas        VARCHAR(1000),                     -- Informe del secretario o técnico agrario
    version_concurrencia          BIGINT        NOT NULL DEFAULT 0,  -- Columna @Version para bloqueo optimista en JPA/Hibernate
    fecha_creacion                TIMESTAMP     NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha_ultima_modificacion     TIMESTAMP     NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_expediente_titular
        FOREIGN KEY (id_titular) REFERENCES titulares (id_titular)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

-- Índices para acelerar la bandeja JSF (p:dataTable) y los informes por campaña/estado
CREATE INDEX idx_exp_titular ON expedientes_municipales (id_titular);
CREATE INDEX idx_exp_campania_estado ON expedientes_municipales (campania_agricola, estado_expediente);
CREATE INDEX idx_exp_fecha_solicitud ON expedientes_municipales (fecha_solicitud);

-- =============================================================================
-- 5. TABLA INTERMEDIA DE DETALLE: PARCELAS INCLUIDAS EN CADA EXPEDIENTE
-- =============================================================================
CREATE TABLE expediente_parcelas (
    id_expediente_parcela   BIGSERIAL PRIMARY KEY,
    id_expediente           BIGINT        NOT NULL,
    id_parcela              BIGINT        NOT NULL,
    superficie_computada_ha NUMERIC(10,4) NOT NULL CHECK (superficie_computada_ha > 0),
    cultivo_campania        VARCHAR(60)   NOT NULL,

    CONSTRAINT fk_exppar_expediente
        FOREIGN KEY (id_expediente) REFERENCES expedientes_municipales (id_expediente)
        ON DELETE CASCADE,
    CONSTRAINT fk_exppar_parcela
        FOREIGN KEY (id_parcela) REFERENCES parcelas_rusticas (id_parcela)
        ON DELETE RESTRICT,
    CONSTRAINT uq_expediente_parcela
        UNIQUE (id_expediente, id_parcela)
);

CREATE INDEX idx_exppar_expediente ON expediente_parcelas (id_expediente);
CREATE INDEX idx_exppar_parcela ON expediente_parcelas (id_parcela);

-- =============================================================================
-- 6. TABLA DE CERTIFICADOS OFICIALES EMITIDOS CON JASPER REPORTS
-- =============================================================================
CREATE TABLE certificados_emitidos (
    id_certificado          BIGSERIAL PRIMARY KEY,
    numero_registro_salida  VARCHAR(40)   NOT NULL UNIQUE,           -- Ej: 'CERT-ROP-2024-00128'
    id_expediente           BIGINT        NOT NULL,                  -- Expediente que origina el certificado PDF
    id_titular              BIGINT        NOT NULL,                  -- Titular certificado
    plantilla_jrxml         VARCHAR(100)  NOT NULL DEFAULT 'informe_parcelas_titular.jrxml',
    codigo_csv_verificacion VARCHAR(64)   NOT NULL UNIQUE,           -- Código Seguro de Verificación (CSV) impreso en el pie del PDF
    usuario_emisor          VARCHAR(60)   NOT NULL,                  -- Funcionario/secretario que generó el PDF desde la pantalla JSF
    fecha_hora_emision      TIMESTAMP     NOT NULL DEFAULT CURRENT_TIMESTAMP,
    total_parcelas_incluidas INTEGER      NOT NULL CHECK (total_parcelas_incluidas > 0),
    total_hectareas_certif  NUMERIC(10,4) NOT NULL CHECK (total_hectareas_certif > 0),

    CONSTRAINT fk_cert_expediente
        FOREIGN KEY (id_expediente) REFERENCES expedientes_municipales (id_expediente)
        ON DELETE RESTRICT,
    CONSTRAINT fk_cert_titular
        FOREIGN KEY (id_titular) REFERENCES titulares (id_titular)
        ON DELETE RESTRICT
);

CREATE INDEX idx_cert_expediente ON certificados_emitidos (id_expediente);
CREATE INDEX idx_cert_titular_fecha ON certificados_emitidos (id_titular, fecha_hora_emision DESC);

-- =============================================================================
-- 7. VISTA OFICIAL PARA ALIMENTAR LA PLANTILLA .JRXML DE JASPER REPORTS
-- =============================================================================
CREATE OR REPLACE VIEW v_certificado_parcelas_titular AS
SELECT
    em.id_expediente,
    em.codigo_expediente,
    em.campania_agricola,
    em.tipo_tramite,
    em.estado_expediente,
    em.fecha_solicitud,
    em.fecha_resolucion,
    t.id_titular,
    t.nif_cif,
    t.nombre_completo,
    t.nucleo_poblacion,
    t.direccion_postal,
    pr.poligono,
    pr.parcela,
    pr.recinto_sigpac,
    pr.paraje_nombre,
    pr.referencia_catastral,
    pr.tipo_cultivo,
    pr.uso_sigpac,
    ep.cultivo_campania,
    pr.regimen_tenencia,
    ep.superficie_computada_ha AS superficie_ha,
    COALESCE(pr.comunidad_regantes, 'Sin adscripción a riego') AS comunidad_regantes
FROM expedientes_municipales em
INNER JOIN titulares t            ON t.id_titular = em.id_titular
INNER JOIN expediente_parcelas ep ON ep.id_expediente = em.id_expediente
INNER JOIN parcelas_rusticas pr   ON pr.id_parcela = ep.id_parcela;

-- =============================================================================
-- 8. DATOS REALISTAS DE PRUEBA (MUNICIPIO DE ROPERUELOS DEL PÁRAMO, LEÓN)
-- =============================================================================

INSERT INTO titulares (id_titular, nif_cif, nombre_completo, tipo_persona, nucleo_poblacion, direccion_postal, telefono_contacto, email) VALUES
(1, '09784512A', 'Alejandro Martínez Huerga', 'FISICA', 'Roperuelos del Páramo', 'Calle Real 14, 24791 Roperuelos del Páramo', '618223344', 'alejandro.martinez@agroparamo.es'),
(2, '09812345B', 'María del Carmen Ferrero Fuertes', 'FISICA', 'Moscas del Páramo', 'Plaza Mayor 3, 24791 Moscas del Páramo', '629114455', 'mcarmen.ferrero@correo.es'),
(3, 'F24098765', 'SAT Regantes Vega del Órbigo y Páramo', 'JURIDICA_SAT', 'Valcabado del Páramo', 'Carretera La Bañeza km 4, Valcabado del Páramo', '987654321', 'administracion@satparamo.es'),
(4, '10045678C', 'Benito González Bécares', 'FISICA', 'Roperuelos del Páramo', 'Calle La Iglesia 8, 24791 Roperuelos del Páramo', '655889900', NULL);

INSERT INTO parcelas_rusticas (id_parcela, id_titular, poligono, parcela, recinto_sigpac, paraje_nombre, referencia_catastral, tipo_cultivo, uso_sigpac, cultivo_declarado, regimen_tenencia, superficie_ha, comunidad_regantes) VALUES
(101, 1, 104,  12, 1, 'El Páramo Alto', '24136A104000120000AB', 'REGADIO', 'TA', 'MAIZ',          'PROPIEDAD',       4.5250, 'Comunidad de Regantes del Páramo Bajo'),
(102, 1, 104,  13, 1, 'El Páramo Alto', '24136A104000130000CD', 'REGADIO', 'TA', 'ALUBIA',        'ARRENDAMIENTO',   2.1800, 'Comunidad de Regantes del Páramo Bajo'),
(103, 1, 108,  45, 2, 'Las Chanas',     '24136A108000450000EF', 'SECANO',  'TA', 'TRIGO_BLANDO',  'PROPIEDAD',       3.7500, NULL),
(104, 2, 102,  88, 1, 'La Vega',        '24136A102000880000GH', 'REGADIO', 'TA', 'REMOLACHA',     'PROPIEDAD',       6.4000, 'Comunidad de Regantes del Canal del Páramo'),
(105, 2, 105,  19, 1, 'Los Quiñones',   '24136A105000190000IJ', 'REGADIO', 'TA', 'MAIZ',          'CESION_COMUNAL',  1.8500, 'Comunidad de Regantes del Canal del Páramo'),
(106, 3, 110, 201, 1, 'El Soto',        '24136A110002010000KL', 'REGADIO', 'TA', 'MAIZ',          'PROPIEDAD',      18.9200, 'Comunidad de Regantes del Páramo Bajo'),
(107, 4, 112,   7, 1, 'Valdeiglesias',  '24136A112000070000MN', 'SECANO',  'TA', 'CEBADA',        'PROPIEDAD',       1.2000, NULL);

INSERT INTO expedientes_municipales (id_expediente, codigo_expediente, id_titular, campania_agricola, tipo_tramite, estado_expediente, superficie_total_declarada_ha, importe_tasa_o_ayuda_eur, fecha_solicitud, fecha_resolucion, observaciones_tecnicas) VALUES
(1001, 'EXP-ROP-2024-0001', 1, 2024, 'CERTIFICADO_BIENES_RUSTICOS',      'APROBADO',            10.4550, 2058.31, '2024-06-15', '2024-06-20', 'Verificada titularidad catastral y recintos SIGPAC de regadío y secano.'),
(1002, 'EXP-ROP-2024-0002', 2, 2024, 'ADJUDICACION_LOTES_COMUNALES',     'APROBADO',             8.2500, 2025.38, '2024-07-02', '2024-07-10', 'Lote comunal en Los Quiñones al corriente de pago de canon municipal.'),
(1003, 'EXP-ROP-2024-0003', 3, 2024, 'DECLARACION_REGADIO',              'EN_REVISION_TECNICA', 18.9200, 4644.86, '2024-08-12', NULL,         'Pendiente de cotejo de concesión de riego con la Comunidad de Regantes.');

INSERT INTO expediente_parcelas (id_expediente, id_parcela, superficie_computada_ha, cultivo_campania) VALUES
(1001, 101,  4.5250, 'MAIZ'),
(1001, 102,  2.1800, 'ALUBIA'),
(1001, 103,  3.7500, 'TRIGO_BLANDO'),
(1002, 104,  6.4000, 'REMOLACHA'),
(1002, 105,  1.8500, 'MAIZ'),
(1003, 106, 18.9200, 'MAIZ');

INSERT INTO certificados_emitidos (numero_registro_salida, id_expediente, id_titular, codigo_csv_verificacion, usuario_emisor, total_parcelas_incluidas, total_hectareas_certif) VALUES
('CERT-ROP-2024-0001', 1001, 1, 'CSV-24136-2024-98AF31B20C', 'secretaria.roperuelos', 3, 10.4550),
('CERT-ROP-2024-0002', 1002, 2, 'CSV-24136-2024-77BC19D44E', 'secretaria.roperuelos', 2,  8.2500);
```

---
## ARCHIVO: consultas_avanzadas_entrevista.sql

```sql
-- =============================================================================
-- ARCHIVO: consultas_avanzadas_entrevista.sql
-- OBJETIVO: 10 Consultas SQL de Nivel Entrevista Técnica (Seresco Valladolid)
--           comentadas paso a paso sobre el esquema agrario/catastral real.
-- =============================================================================

-- -----------------------------------------------------------------------------
-- CONSULTA 1: LEFT JOIN + IS NULL (Anti-Join)
-- Enunciado de prueba técnica:
-- "Obtén el listado de titulares activos que tienen parcelas rústicas en el
--  municipio pero que NO han presentado ningún expediente en la campaña 2024."
-- -----------------------------------------------------------------------------
SELECT
    t.id_titular,
    t.nif_cif,
    t.nombre_completo,
    t.nucleo_poblacion,
    COUNT(pr.id_parcela)    AS num_parcelas_catastrales,
    SUM(pr.superficie_ha)   AS superficie_catastral_total_ha
FROM titulares t
-- INNER JOIN con parcelas_rusticas porque el enunciado pide titulares que SÍ tengan parcelas
INNER JOIN parcelas_rusticas pr
    ON pr.id_titular = t.id_titular
   AND pr.activa = TRUE
-- LEFT JOIN con expedientes poniendo el filtro de campaña 2024 DENTRO del ON (¡clave para no romper el LEFT JOIN!)
LEFT JOIN expedientes_municipales em
    ON em.id_titular = t.id_titular
   AND em.campania_agricola = 2024
WHERE t.activo = TRUE
  AND em.id_expediente IS NULL -- Filtra solo los que no tuvieron coincidencia en expedientes 2024
GROUP BY
    t.id_titular,
    t.nif_cif,
    t.nombre_completo,
    t.nucleo_poblacion
ORDER BY superficie_catastral_total_ha DESC;


-- -----------------------------------------------------------------------------
-- CONSULTA 2: GROUP BY + HAVING + Agregación Condicional (CASE WHEN)
-- Enunciado de prueba técnica:
-- "Muestra por cada Polígono catastral el número de parcelas, las hectáreas de
--  REGADÍO, las hectáreas de SECANO y la superficie total, mostrando únicamente
--  aquellos polígonos cuya superficie de REGADÍO supere las 5.0000 hectáreas."
-- -----------------------------------------------------------------------------
SELECT
    pr.poligono,
    COUNT(pr.id_parcela) AS total_parcelas,
    -- Pivotado condicional con SUM(CASE WHEN ...): muy preguntado en entrevistas de SQL y reporting
    SUM(CASE WHEN pr.tipo_cultivo = 'REGADIO' THEN pr.superficie_ha ELSE 0 END) AS ha_regadio,
    SUM(CASE WHEN pr.tipo_cultivo = 'SECANO'  THEN pr.superficie_ha ELSE 0 END) AS ha_secano,
    SUM(pr.superficie_ha) AS ha_totales_poligono,
    ROUND(
        (SUM(CASE WHEN pr.tipo_cultivo = 'REGADIO' THEN pr.superficie_ha ELSE 0 END) * 100.0)
        / NULLIF(SUM(pr.superficie_ha), 0), -- NULLIF evita división por cero defensivamente
        2
    ) AS porcentaje_regadio
FROM parcelas_rusticas pr
WHERE pr.activa = TRUE
GROUP BY pr.poligono
-- HAVING filtra los grupos ya agregados (no se puede poner SUM() en el WHERE)
HAVING SUM(CASE WHEN pr.tipo_cultivo = 'REGADIO' THEN pr.superficie_ha ELSE 0 END) > 5.0000
ORDER BY ha_regadio DESC;


-- -----------------------------------------------------------------------------
-- CONSULTA 3: Función Ventana ROW_NUMBER() OVER (PARTITION BY ...)
-- Enunciado de prueba técnica:
-- "Para cada titular agrario, obtén los datos de su parcela rústica de MAYOR
--  superficie (Top 1 por titular). Si hay empate en hectáreas, prioriza REGADÍO."
-- -----------------------------------------------------------------------------
WITH ranking_parcelas_por_titular AS (
    SELECT
        t.nif_cif,
        t.nombre_completo,
        pr.poligono,
        pr.parcela,
        pr.recinto_sigpac,
        pr.paraje_nombre,
        pr.tipo_cultivo,
        pr.cultivo_declarado,
        pr.superficie_ha,
        -- Reinicia el contador a 1 para cada titular (PARTITION BY) ordenando por mayor superficie
        ROW_NUMBER() OVER (
            PARTITION BY t.id_titular
            ORDER BY pr.superficie_ha DESC,
                     CASE WHEN pr.tipo_cultivo = 'REGADIO' THEN 1 ELSE 2 END ASC
        ) AS posicion_ranking
    FROM titulares t
    INNER JOIN parcelas_rusticas pr ON pr.id_titular = t.id_titular
    WHERE pr.activa = TRUE
)
SELECT
    nif_cif,
    nombre_completo,
    poligono,
    parcela,
    recinto_sigpac,
    paraje_nombre,
    tipo_cultivo,
    cultivo_declarado,
    superficie_ha AS mayor_parcela_ha
FROM ranking_parcelas_por_titular
WHERE posicion_ranking = 1
ORDER BY mayor_parcela_ha DESC;


-- -----------------------------------------------------------------------------
-- CONSULTA 4: Función Ventana Analítica SUM() OVER() para Peso Porcentual
-- Enunciado de prueba técnica:
-- "Al generar un informe en Jasper Reports, necesitamos que cada fila de parcela
--  de un expediente muestre su superficie individual, la superficie acumulada
--  (running total) y qué porcentaje representa esa parcela sobre el total del
--  expediente, sin perder el detalle de las filas."
-- -----------------------------------------------------------------------------
SELECT
    em.codigo_expediente,
    t.nif_cif,
    pr.poligono,
    pr.parcela,
    pr.recinto_sigpac,
    ep.cultivo_campania,
    ep.superficie_computada_ha,
    -- Suma acumulada progresiva fila a fila dentro del expediente
    SUM(ep.superficie_computada_ha) OVER (
        PARTITION BY em.id_expediente
        ORDER BY pr.poligono, pr.parcela, pr.recinto_sigpac
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS superficie_acumulada_ha,
    -- Suma total del expediente calculada como ventana sin colapsar filas
    SUM(ep.superficie_computada_ha) OVER (
        PARTITION BY em.id_expediente
    ) AS total_expediente_ha,
    -- Peso porcentual de la parcela dentro del expediente
    ROUND(
        (ep.superficie_computada_ha * 100.0) /
        NULLIF(SUM(ep.superficie_computada_ha) OVER (PARTITION BY em.id_expediente), 0),
        2
    ) AS porcentaje_sobre_expediente
FROM expedientes_municipales em
INNER JOIN titulares t            ON t.id_titular = em.id_titular
INNER JOIN expediente_parcelas ep ON ep.id_expediente = em.id_expediente
INNER JOIN parcelas_rusticas pr   ON pr.id_parcela = ep.id_parcela
WHERE em.codigo_expediente = 'EXP-ROP-2024-0001'
ORDER BY pr.poligono, pr.parcela, pr.recinto_sigpac;


-- -----------------------------------------------------------------------------
-- CONSULTA 5: Detección de Duplicados o Inconsistencias Catastrales
-- Enunciado de prueba técnica:
-- "En una importación masiva de datos SIGPAC queremos detectar si una misma
--  parcela rústica ha sido declarada en MÁS DE UN expediente activo dentro de
--  la misma campaña agrícola (doble declaración de superficie)."
-- -----------------------------------------------------------------------------
SELECT
    em.campania_agricola,
    pr.poligono,
    pr.parcela,
    pr.recinto_sigpac,
    pr.referencia_catastral,
    COUNT(DISTINCT em.id_expediente) AS num_expedientes_en_conflicto,
    STRING_AGG(em.codigo_expediente || ' (' || t.nif_cif || ')', ', ') AS expedientes_implicados
FROM expediente_parcelas ep
INNER JOIN expedientes_municipales em ON em.id_expediente = ep.id_expediente
INNER JOIN parcelas_rusticas pr       ON pr.id_parcela = ep.id_parcela
INNER JOIN titulares t                ON t.id_titular = em.id_titular
WHERE em.estado_expediente <> 'DENEGADO'
GROUP BY
    em.campania_agricola,
    pr.poligono,
    pr.parcela,
    pr.recinto_sigpac,
    pr.referencia_catastral
HAVING COUNT(DISTINCT em.id_expediente) > 1;


-- -----------------------------------------------------------------------------
-- CONSULTA 6: CTEs Encadenadas (Auditoría de Discrepancias entre Cabecera y Líneas)
-- Enunciado de prueba técnica:
-- "Comprueba si existe algún expediente cuya columna resumen
--  'superficie_total_declarada_ha' en la tabla cabecera NO coincida exactamente
--  con la suma real de sus líneas en 'expediente_parcelas'."
-- -----------------------------------------------------------------------------
WITH suma_real_lineas AS (
    SELECT
        ep.id_expediente,
        COALESCE(SUM(ep.superficie_computada_ha), 0.0000) AS ha_calculadas_detalle,
        COUNT(ep.id_parcela) AS num_lineas
    FROM expediente_parcelas ep
    GROUP BY ep.id_expediente
)
SELECT
    em.id_expediente,
    em.codigo_expediente,
    em.estado_expediente,
    em.superficie_total_declarada_ha        AS ha_en_cabecera,
    COALESCE(srl.ha_calculadas_detalle, 0)  AS ha_en_lineas,
    (em.superficie_total_declarada_ha - COALESCE(srl.ha_calculadas_detalle, 0)) AS descuadre_ha
FROM expedientes_municipales em
LEFT JOIN suma_real_lineas srl ON srl.id_expediente = em.id_expediente
WHERE em.superficie_total_declarada_ha <> COALESCE(srl.ha_calculadas_detalle, 0);


-- -----------------------------------------------------------------------------
-- CONSULTA 7: Actualización Masiva Segura (UPDATE con Subconsulta / FROM)
-- Enunciado de prueba técnica:
-- "Recalcula y sincroniza automáticamente la columna 'superficie_total_declarada_ha'
--  de todos los expedientes de la campaña 2024 a partir de la suma real de sus
--  parcelas asociadas."
-- -----------------------------------------------------------------------------
UPDATE expedientes_municipales em
SET
    superficie_total_declarada_ha = COALESCE((
        SELECT SUM(ep.superficie_computada_ha)
        FROM expediente_parcelas ep
        WHERE ep.id_expediente = em.id_expediente
    ), 0.0000),
    fecha_ultima_modificacion = CURRENT_TIMESTAMP
WHERE em.campania_agricola = 2024;


-- -----------------------------------------------------------------------------
-- CONSULTA 8: Uso de EXISTS vs IN para Alto Rendimiento
-- Enunciado de prueba técnica:
-- "Obtén todos los titulares que tengan al menos un certificado PDF emitido en
--  el año actual y que además posean alguna parcela en régimen de 'CESION_COMUNAL'."
-- (Usamos EXISTS porque hace cortocircuito en cuanto encuentra la primera coincidencia
--  en el índice, sin materializar listas gigantes en memoria).
-- -----------------------------------------------------------------------------
SELECT
    t.id_titular,
    t.nif_cif,
    t.nombre_completo,
    t.nucleo_poblacion
FROM titulares t
WHERE t.activo = TRUE
  AND EXISTS (
      SELECT 1
      FROM certificados_emitidos ce
      WHERE ce.id_titular = t.id_titular
        AND ce.fecha_hora_emision >= DATE '2024-01-01'
  )
  AND EXISTS (
      SELECT 1
      FROM parcelas_rusticas pr
      WHERE pr.id_titular = t.id_titular
        AND pr.regimen_tenencia = 'CESION_COMUNAL'
        AND pr.activa = TRUE
  );


-- -----------------------------------------------------------------------------
-- CONSULTA 9: Consulta Parametrizada Exacta para Jasper Reports ($P{ID_EXPEDIENTE})
-- Enunciado de prueba técnica:
-- "Escribe la consulta SQL que pegamos dentro del bloque <queryString> del
--  fichero .jrxml de Jasper Reports para imprimir el Certificado Municipal de
--  Parcelas Rústicas de un expediente aprobado."
-- -----------------------------------------------------------------------------
SELECT
    v.codigo_expediente,
    v.campania_agricola,
    v.fecha_resolucion,
    v.nif_cif,
    v.nombre_completo,
    v.nucleo_poblacion,
    v.direccion_postal,
    v.poligono,
    v.parcela,
    v.recinto_sigpac,
    v.paraje_nombre,
    v.referencia_catastral,
    v.tipo_cultivo,
    v.cultivo_campania,
    v.regimen_tenencia,
    v.superficie_ha,
    v.comunidad_regantes
FROM v_certificado_parcelas_titular v
WHERE v.id_expediente = 1001 -- En el .jrxml se sustituye por: WHERE v.id_expediente = $P{ID_EXPEDIENTE}
  AND v.estado_expediente = 'APROBADO'
ORDER BY
    v.poligono ASC,
    v.parcela ASC,
    v.recinto_sigpac ASC;


-- -----------------------------------------------------------------------------
-- CONSULTA 10: Creación de Tabla y Trigger de Auditoría Automática
-- Enunciado de prueba técnica:
-- "¿Cómo garantizarías a nivel de base de datos que cualquier cambio de estado
--  en un expediente administrativo quede registrado en una tabla de auditoría?"
-- -----------------------------------------------------------------------------
CREATE TABLE auditoria_cambios_expediente (
    id_auditoria        BIGSERIAL PRIMARY KEY,
    id_expediente       BIGINT      NOT NULL,
    codigo_expediente   VARCHAR(30) NOT NULL,
    estado_anterior     VARCHAR(30),
    estado_nuevo        VARCHAR(30) NOT NULL,
    sup_anterior_ha     NUMERIC(10,4),
    sup_nueva_ha        NUMERIC(10,4),
    fecha_cambio        TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Función PL/pgSQL del Trigger (PostgreSQL)
CREATE OR REPLACE FUNCTION fn_auditar_cambio_estado_expediente()
RETURNS TRIGGER AS $$
BEGIN
    -- Solo insertamos traza si ha cambiado el estado o la superficie declarada
    IF (OLD.estado_expediente IS DISTINCT FROM NEW.estado_expediente)
       OR (OLD.superficie_total_declarada_ha IS DISTINCT FROM NEW.superficie_total_declarada_ha) THEN
        INSERT INTO auditoria_cambios_expediente (
            id_expediente, codigo_expediente, estado_anterior, estado_nuevo, sup_anterior_ha, sup_nueva_ha
        ) VALUES (
            NEW.id_expediente, NEW.codigo_expediente, OLD.estado_expediente, NEW.estado_expediente,
            OLD.superficie_total_declarada_ha, NEW.superficie_total_declarada_ha
        );
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_auditar_expediente_update
AFTER UPDATE ON expedientes_municipales
FOR EACH ROW
EXECUTE FUNCTION fn_auditar_cambio_estado_expediente();
```

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

---
## ARCHIVO: README_CASO_DE_EXITO_ROPERUELOS.md

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

---
## ARCHIVO: arquitectura_y_decisiones_tecnicas.md

# ARQUITECTURA DEL SISTEMA Y DECISIONES TÉCNICAS — PROYECTO AYUNTAMIENTO DE ROPERUELOS DEL PÁRAMO

> **Cómo usar este documento en la entrevista:** Cuando el arquitecto o jefe de proyecto de Seresco te pregunte *«¿Cómo estructuraste por dentro la aplicación del Ayuntamiento y por qué tomaste esas decisiones?»*, apóyate en este diseño en capas.

---

## 1. DIAGRAMA ASCII DE LA ARQUITECTURA COMPLETA

```text
+-----------------------------------------------------------------------------------+
|                     NAVEGADOR WEB DEL PERSONAL DEL AYUNTAMIENTO                   |
|    (Secretaría-Intervención / Ventanilla Administrativa — Red Local Municipal)    |
+-----------------------------------------+-----------------------------------------+
                                          |
                 Peticiones HTTP / AJAX   |   Descarga Stream Binario
               (Postback JSF ViewState)   |   (Content-Type: application/pdf)
                                          v
+-----------------------------------------------------------------------------------+
|                 SERVIDOR DE APLICACIONES JAVA (WildFly / Tomcat)                  |
|                                                                                   |
|  +-----------------------------------------------------------------------------+  |
|  | 1. CAPA DE PRESENTACIÓN (JSF 2.3 Facelets + PrimeFaces)                     |  |
|  |    - Controlador Frontal: FacesServlet (Ciclo de vida de 6 fases)           |  |
|  |    - Vista XHTML: gestion_expedientes_agricolas.xhtml (<p:dataTable>)       |  |
|  |    - Backing Bean: ExpedienteManagedBean (@Named + @ViewScoped)             |  |
|  +----------------------+-----------------------------------+------------------+  |
|                         | @Inject                           | @Inject             |
|                         v                                   v                     |
|  +--------------------------------------+  +-----------------------------------+  |
|  | 2. CAPA DE SERVICIO / NEGOCIO        |  | 3. MOTOR DE INFORMES DOCUMENTALES |  |
|  |    - ExpedienteService               |  |    - JasperReportGeneratorService |  |
|  |    - @Transactional (ACID)           |  |    - Caché ConcurrentHashMap de   |  |
|  |    - Validación SIGPAC y cálculo     |  |      plantillas .jasper compiladas|  |
|  |      exacto con BigDecimal (scale 4) |  |    - JasperFillManager +          |  |
|  |                                      |  |      JasperExportManager (PDF/XLS)|  |
|  +----------------------+---------------+  +-----------------+-----------------+  |
|                         | @Inject                            |                    |
|                         v                                    |                    |
|  +-----------------------------------------------------------+-----------------+  |
|  | 4. CAPA DE ACCESO A DATOS Y PERSISTENCIA (ExpedienteRepository)             |  |
|  |    - JPA / Hibernate (EntityManager): JPQL con JOIN FETCH (Sin N+1 queries) |  |
|  |    - JDBC Puro (DataSource Pool + PreparedStatement): Consultas masivas     |  |
|  |      para alimentar JRBeanCollectionDataSource o Connection directa         |  |
|  +--------------------------------------+--------------------------------------+  |
+-----------------------------------------|-----------------------------------------+
                                          |
                           Pool JDBC      |      (Evolutivo 2024: Script/API Python
                         (Puerto 5432)    |       para carga y limpieza CSV Catastro)
                                          v
+-----------------------------------------------------------------------------------+
|                   BASE DE DATOS RELACIONAL SQL (PostgreSQL / MySQL)               |
|  - Tablas: titulares, parcelas_rusticas, expedientes_municipales,                 |
|            expediente_parcelas, certificados_emitidos, auditoria_cambios          |
|  - Vista de Reporting: v_certificado_parcelas_titular                             |
|  - Índices B-Tree: idx_exp_campania_estado, uq_sigpac_municipio_pol_par_rec       |
+-----------------------------------------------------------------------------------+
```

---

## 2. LAS 5 DECISIONES TÉCNICAS DE ARQUITECTURA Y SU JUSTIFICACIÓN

### Decisión 1: Uso de `@ViewScoped` en `ExpedienteManagedBean` en lugar de `@RequestScoped` o `@SessionScoped`
- **Problema:** La pantalla principal (`gestion_expedientes_agricolas.xhtml`) combina tres interacciones sin cambiar de página: filtrar expedientes con AJAX, paginar/ordenar la tabla `<p:dataTable>` y abrir un diálogo modal `<p:dialog>` para revisar observaciones, aprobar el expediente o descargar el PDF.
- **Por qué descarté `@RequestScoped`:** Con `@RequestScoped`, al pulsar el botón *"Aprobar Expediente"* dentro del diálogo modal, JSF reconstruiría el Bean desde cero antes de invocar la acción, perdiendo la referencia a `expedienteSeleccionado` o re-ejecutando innecesariamente la consulta SQL de toda la tabla en cada petición AJAX.
- **Por qué descarté `@SessionScoped`:** Guardar listas de entidades y resultados de búsqueda en la sesión HTTP consume memoria Heap durante toda la jornada del administrativo y provoca conflictos de estado si el funcionario abre dos pestañas del navegador a la vez para consultar dos agricultores distintos.
- **Solución adoptada (`@ViewScoped`):** Mantiene vivos en memoria los filtros, la lista de la tabla y el `expedienteSeleccionado` única y exclusivamente mientras el usuario sigue en esa vista XHTML, liberando la memoria automáticamente al cambiar de pantalla.

---

### Decisión 2: Prevención del problema `N+1` y de `LazyInitializationException` combinando `FetchType.LAZY` con `JOIN FETCH`
- **Problema:** Un `ExpedienteAgrarioEntity` está relacionado con un `Titular` (`@ManyToOne`) y con múltiples `Parcelas` (`@OneToMany`). Si dejáramos `@ManyToOne` en su valor por defecto (`EAGER`), cualquier consulta simple cargaría tablas innecesarias; pero si lo ponemos en `LAZY` y la vista JSF evalúa `#{exp.titular.nombreCompleto}` fuera de la transacción, salta `LazyInitializationException`.
- **Solución adoptada:**
  1. Declarar **todas** las relaciones JPA como **`FetchType.LAZY`** en las clases `@Entity`.
  2. Crear consultas JPQL específicas en `ExpedienteRepository` según lo que necesita cada caso de uso:
     - Para la bandeja de búsqueda JSF: `SELECT e FROM ExpedienteAgrarioEntity e JOIN FETCH e.titular t WHERE ...` (trae expediente + titular en 1 sola query SQL, sin cargar todavía las 40 parcelas de cada fila).
     - Para abrir el detalle o aprobar el expediente: `SELECT DISTINCT e FROM ExpedienteAgrarioEntity e JOIN FETCH e.titular LEFT JOIN FETCH e.parcelasAsociadas WHERE e.codigoExpediente = :codigo` (trae cabecera, titular y todas sus parcelas en 1 sola query SQL).

---

### Decisión 3: Caché en memoria de plantillas compiladas `.jasper` (`ConcurrentHashMap`) para no bloquear la CPU
- **Problema:** Compilar un archivo XML `.jrxml` con `JasperCompileManager.compileReport(...)` parsea el XML, valida el esquema XSD y genera bytecode de expresiones internamente, lo que puede tardar entre 400 ms y 1,5 segundos y consumir mucha CPU si se ejecuta en cada clic del usuario.
- **Solución adoptada:**
  1. Precompilar los `.jrxml` a `.jasper` en el empaquetado Maven y además mantener en `JasperReportGeneratorService` (`@ApplicationScoped`) un **`ConcurrentHashMap<String, JasperReport>`**.
  2. La primera vez que se solicita un informe se carga el objeto `JasperReport` en el mapa concurrente (que es *thread-safe* y puede ser reutilizado simultáneamente por múltiples hilos), y en las siguientes peticiones se pasa directamente a `JasperFillManager.fillReport(...)`, bajando el tiempo de generación del PDF a **30–80 milisegundos**.

---

### Decisión 4: Elección de `JRBeanCollectionDataSource` alimentado por DTOs JDBC (`PreparedStatement`) para informes complejos
- **Problema:** Algunos certificados requerían verificar reglas de negocio en Java antes de emitir el PDF (comprobar que el expediente estuviera en estado `APROBADO`, formatear advertencias de regadío y registrar en la tabla `certificados_emitidos` el Código Seguro de Verificación `CSV`).
- **Solución adoptada:**
  - En lugar de acoplar toda esa lógica dentro del XML de la plantilla, creé en el repositorio una consulta JDBC ultrarrápida con `PreparedStatement` y `try-with-resources` que proyecta los datos ya limpios en una lista de `ResumenCertificadoCatastralDTO`.
  - El servicio valida la lista, genera el código `CSV`, inyecta los metadatos en el `Map<String, Object>` de parámetros (`$P{}`) y pasa la colección envuelta en `new JRBeanCollectionDataSource(filasParcelas)` a `JasperFillManager`, logrando máxima velocidad, seguridad contra Inyección SQL y facilidad de pruebas unitarias.

---

### Decisión 5: Aritmética exacta con `BigDecimal` (`NUMERIC(10,4)`) en Java, SQL y Jasper Reports
- **Problema:** En el ámbito catastral y SIGPAC, las superficies se expresan en hectáreas con 4 decimales (`0.0001 ha = 1 centiárea = 1 m²`). Usar `Double` producía redondeos inexactos donde la suma de las filas del certificado no cuadraba por una diezmilésima con el total de la cabecera.
- **Solución adoptada:** Unificar el tipo de dato en las tres capas:
  - **Base de datos SQL:** `NUMERIC(10,4)` para hectáreas y `NUMERIC(12,2)` para importes en euros.
  - **Entidades y Servicios Java:** `java.math.BigDecimal` con `RoundingMode.HALF_UP`.
  - **Plantilla `.jrxml` de Jasper Reports:** `<field name="superficieHa" class="java.math.BigDecimal"/>` y `<variable name="TOTAL_HECTAREAS_TITULAR" class="java.math.BigDecimal" calculation="Sum"/>` con máscara `pattern="#,##0.0000"`.

---
## ARCHIVO: flujo_completo_codigo_integrado.java

```java
package es.seresco.agro.roperuelos.integrado; // Paquete demostrativo del flujo vertical completo (End-to-End)

import java.io.InputStream; // Lectura de la plantilla .jasper / .jrxml desde el classpath
import java.io.OutputStream; // Escritura del PDF generado en el HttpServletResponse del navegador
import java.io.Serializable; // Estándar para entidades y Beans @ViewScoped en Jakarta EE / JSF
import java.math.BigDecimal; // Precisión exacta a 4 decimales para hectáreas SIGPAC
import java.math.RoundingMode; // Redondeo financiero/agrario HALF_UP
import java.sql.Connection; // Conexión JDBC obtenida del DataSource JNDI
import java.sql.PreparedStatement; // Consulta SQL precompilada y segura frente a Inyección SQL
import java.sql.ResultSet; // Cursor de lectura de filas SQL
import java.time.LocalDate; // Fecha oficial de solicitud y resolución
import java.util.ArrayList; // Lista en memoria para almacenar las filas de parcelas
import java.util.HashMap; // Mapa clave-valor para los parámetros $P{...} de Jasper Reports
import java.util.List; // Interfaz List
import java.util.Map; // Interfaz Map
import java.util.UUID; // Generador del Código Seguro de Verificación (CSV) del certificado

import javax.annotation.PostConstruct; // Inicialización del Bean JSF al entrar en la pantalla
import javax.annotation.Resource; // Inyección del Pool de Conexiones DataSource
import javax.enterprise.context.ApplicationScoped; // Beans de Servicio y Repositorio Singleton en CDI
import javax.faces.application.FacesMessage; // Mensajes de usuario en la interfaz JSF / PrimeFaces
import javax.faces.context.ExternalContext; // Acceso al HttpServletResponse desde JSF
import javax.faces.context.FacesContext; // Contexto de la petición JSF
import javax.faces.view.ViewScoped; // Ámbito de vista JSF para conservar estado entre peticiones AJAX
import javax.inject.Inject; // Inyección de dependencias CDI (@Autowired en Spring)
import javax.inject.Named; // Nombre público del Bean para el Expression Language (#{flujoRoperuelosBean})
import javax.persistence.Column; // Mapeo de columna SQL
import javax.persistence.Entity; // Entidad JPA
import javax.persistence.EntityManager; // Motor JPA / Hibernate
import javax.persistence.FetchType; // Carga perezosa LAZY
import javax.persistence.GeneratedValue; // Clave primaria autogenerada
import javax.persistence.GenerationType; // Estrategia IDENTITY
import javax.persistence.Id; // Primary Key
import javax.persistence.JoinColumn; // Foreign Key
import javax.persistence.ManyToOne; // Relación Muchos-a-Uno
import javax.persistence.OneToMany; // Relación Uno-a-Muchos
import javax.persistence.PersistenceContext; // Inyección del EntityManager JPA
import javax.persistence.Table; // Nombre de tabla SQL
import javax.sql.DataSource; // Pool de conexiones JDBC
import javax.transaction.Transactional; // Transacción declarativa ACID

import net.sf.jasperreports.engine.JasperCompileManager; // Compilador de .jrxml a .jasper
import net.sf.jasperreports.engine.JasperExportManager; // Exportador de JasperPrint a PDF (byte[])
import net.sf.jasperreports.engine.JasperFillManager; // Motor de relleno (Plantilla + $P + $F -> JasperPrint)
import net.sf.jasperreports.engine.JasperPrint; // Documento paginado en memoria
import net.sf.jasperreports.engine.JasperReport; // Plantilla compilada
import net.sf.jasperreports.engine.data.JRBeanCollectionDataSource; // Origen de datos basado en colección de Beans Java

/**
 * =============================================================================
 * FLUJO VERTICAL COMPLETO E INTEGRADO — PROYECTO AYUNTAMIENTO DE ROPERUELOS DEL PÁRAMO
 * =============================================================================
 * Caso estrella para defender en la entrevista técnica de Seresco (Valladolid):
 * "Búsqueda de expedientes y parcelas de un agricultor por NIF y Polígono Catastral
 *  y emisión en un clic del Certificado Oficial Municipal en PDF con Jasper Reports".
 *
 * Este archivo unifica en una sola vista de estudio las 5 capas que interactúan:
 *   [PASO 1] Entidad JPA y DTO de Parcela Rústica (Modelo de Datos).
 *   [PASO 2] Repositorio JPA (JPQL con JOIN FETCH) + JDBC (PreparedStatement).
 *   [PASO 3] Servicio Transaccional de Negocio (@Transactional + validación BigDecimal).
 *   [PASO 4] Servicio de Jasper Reports (Compilación + Parámetros $P + JRBeanCollectionDataSource + PDF).
 *   [PASO 5] Managed Bean JSF (@ViewScoped) + Equivalente Spring Boot REST Controller.
 */
public class flujo_completo_codigo_integrado {

    // =========================================================================
    // [PASO 1] MODELO DE DATOS: ENTIDAD JPA + DTO PARA JASPER REPORTS
    // =========================================================================

    @Entity
    @Table(name = "expedientes_municipales")
    public static class ExpedienteMunicipalEntity implements Serializable {
        private static final long serialVersionUID = 1L;

        @Id
        @GeneratedValue(strategy = GenerationType.IDENTITY)
        @Column(name = "id_expediente")
        private Long id;

        @Column(name = "codigo_expediente", nullable = false, unique = true, length = 30)
        private String codigoExpediente;

        @Column(name = "campania_agricola", nullable = false)
        private Integer campaniaAgricola;

        @Column(name = "estado_expediente", nullable = false, length = 30)
        private String estadoExpediente; // 'BORRADOR', 'EN_REVISION_TECNICA', 'APROBADO'

        @Column(name = "superficie_total_declarada_ha", nullable = false, precision = 10, scale = 4)
        private BigDecimal superficieTotalHa = BigDecimal.ZERO;

        @ManyToOne(fetch = FetchType.LAZY, optional = false) // LAZY siempre para evitar consultas ocultas
        @JoinColumn(name = "id_titular", nullable = false)
        private TitularEntity titular;

        @OneToMany(mappedBy = "expediente", fetch = FetchType.LAZY)
        private List<ParcelaRusticaEntity> parcelas = new ArrayList<>();

        public Long getId() { return id; }
        public String getCodigoExpediente() { return codigoExpediente; }
        public Integer getCampaniaAgricola() { return campaniaAgricola; }
        public String getEstadoExpediente() { return estadoExpediente; }
        public void setEstadoExpediente(String estadoExpediente) { this.estadoExpediente = estadoExpediente; }
        public BigDecimal getSuperficieTotalHa() { return superficieTotalHa; }
        public void setSuperficieTotalHa(BigDecimal superficieTotalHa) { this.superficieTotalHa = superficieTotalHa; }
        public TitularEntity getTitular() { return titular; }
        public List<ParcelaRusticaEntity> getParcelas() { return parcelas; }
    }

    @Entity
    @Table(name = "titulares")
    public static class TitularEntity implements Serializable {
        private static final long serialVersionUID = 1L;
        @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
        @Column(name = "id_titular")
        private Long id;
        @Column(name = "nif_cif", nullable = false, unique = true)
        private String nifCif;
        @Column(name = "nombre_completo", nullable = false)
        private String nombreCompleto;

        public Long getId() { return id; }
        public String getNifCif() { return nifCif; }
        public String getNombreCompleto() { return nombreCompleto; }
    }

    @Entity
    @Table(name = "parcelas_rusticas")
    public static class ParcelaRusticaEntity implements Serializable {
        private static final long serialVersionUID = 1L;
        @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
        @Column(name = "id_parcela")
        private Long id;
        @Column(name = "poligono", nullable = false)
        private Integer poligono;
        @Column(name = "parcela", nullable = false)
        private Integer parcela;
        @Column(name = "recinto_sigpac", nullable = false)
        private Integer recintoSigpac;
        @Column(name = "tipo_cultivo", nullable = false)
        private String tipoCultivo; // 'REGADIO' o 'SECANO'
        @Column(name = "superficie_ha", nullable = false, precision = 10, scale = 4)
        private BigDecimal superficieHa;
        @ManyToOne(fetch = FetchType.LAZY)
        @JoinColumn(name = "id_expediente")
        private ExpedienteMunicipalEntity expediente;

        public Integer getPoligono() { return poligono; }
        public Integer getParcela() { return parcela; }
        public Integer getRecintoSigpac() { return recintoSigpac; }
        public String getTipoCultivo() { return tipoCultivo; }
        public BigDecimal getSuperficieHa() { return superficieHa; }
    }

    /**
     * DTO cuyos getters coinciden exactamente con los campos <field name="...">
     * declarados en la plantilla informe_parcelas_titular.jrxml de Jasper Reports.
     */
    public static class FilaCertificadoJasperDTO implements Serializable {
        private static final long serialVersionUID = 1L;
        private final String codigoExpediente;
        private final String nifTitular;
        private final String nombreTitular;
        private final Integer poligono;
        private final Integer parcela;
        private final Integer recintoSigpac;
        private final String tipoCultivo;
        private final BigDecimal superficieHa;

        public FilaCertificadoJasperDTO(String codigoExpediente, String nifTitular, String nombreTitular,
                Integer poligono, Integer parcela, Integer recintoSigpac, String tipoCultivo, BigDecimal superficieHa) {
            this.codigoExpediente = codigoExpediente;
            this.nifTitular = nifTitular;
            this.nombreTitular = nombreTitular;
            this.poligono = poligono;
            this.parcela = parcela;
            this.recintoSigpac = recintoSigpac;
            this.tipoCultivo = tipoCultivo;
            this.superficieHa = superficieHa;
        }

        // Jasper Reports invoca estos getters por reflexión al iterar la banda <detail>
        public String getCodigoExpediente() { return codigoExpediente; }
        public String getNifTitular() { return nifTitular; }
        public String getNombreTitular() { return nombreTitular; }
        public Integer getPoligono() { return poligono; }
        public Integer getParcela() { return parcela; }
        public Integer getRecintoSigpac() { return recintoSigpac; }
        public String getTipoCultivo() { return tipoCultivo; }
        public BigDecimal getSuperficieHa() { return superficieHa; }
    }

    // =========================================================================
    // [PASO 2] CAPA DE REPOSITORIO: JPQL (JOIN FETCH) + JDBC (PreparedStatement)
    // =========================================================================

    @ApplicationScoped
    public static class RoperuelosAgrarioRepository {

        @PersistenceContext(unitName = "AgroRoperuelosPU")
        private EntityManager em;

        @Resource(lookup = "java:/jdbc/AgroRoperuelosDS")
        private DataSource dataSource;

        /**
         * Consulta JPQL optimizada con JOIN FETCH para buscar expedientes de un agricultor
         * por NIF y opcionalmente por Polígono rústico, trayendo Titular y Parcelas en 1 sola consulta SQL.
         */
        public List<ExpedienteMunicipalEntity> buscarExpedientesPorNifYPoligono(
                String nifAgricultor,
                Integer poligonoFiltro,
                Integer campania) {

            String jpql =
                "SELECT DISTINCT e " +
                "FROM flujo_completo_codigo_integrado$ExpedienteMunicipalEntity e " +
                "JOIN FETCH e.titular t " +
                "LEFT JOIN FETCH e.parcelas p " +
                "WHERE UPPER(t.nifCif) = :nif " +
                "  AND e.campaniaAgricola = :campania " +
                (poligonoFiltro != null ? " AND p.poligono = :poligono " : "") +
                "ORDER BY e.codigoExpediente DESC";

            var query = em.createQuery(jpql, ExpedienteMunicipalEntity.class)
                    .setParameter("nif", nifAgricultor.trim().toUpperCase())
                    .setParameter("campania", campania);

            if (poligonoFiltro != null) {
                query.setParameter("poligono", poligonoFiltro);
            }
            return query.getResultList();
        }

        /**
         * Consulta JDBC parametrizada (PreparedStatement + try-with-resources) para extraer
         * los recintos SIGPAC aprobados que se imprimirán en el Certificado PDF de Jasper Reports.
         */
        public List<FilaCertificadoJasperDTO> obtenerFilasParaJasperJdbc(
                Long idExpediente,
                Integer poligonoOpcional) throws Exception {

            String sql =
                "SELECT em.codigo_expediente, t.nif_cif, t.nombre_completo, " +
                "       pr.poligono, pr.parcela, pr.recinto_sigpac, pr.tipo_cultivo, " +
                "       ep.superficie_computada_ha AS superficie_ha " +
                "FROM expedientes_municipales em " +
                "INNER JOIN titulares t            ON t.id_titular = em.id_titular " +
                "INNER JOIN expediente_parcelas ep ON ep.id_expediente = em.id_expediente " +
                "INNER JOIN parcelas_rusticas pr   ON pr.id_parcela = ep.id_parcela " +
                "WHERE em.id_expediente = ? " +
                "  AND em.estado_expediente = 'APROBADO' " +
                (poligonoOpcional != null ? " AND pr.poligono = ? " : "") +
                "ORDER BY pr.poligono ASC, pr.parcela ASC, pr.recinto_sigpac ASC";

            List<FilaCertificadoJasperDTO> lista = new ArrayList<>();

            // try-with-resources: garantiza devolver la conexión al Pool aunque ocurra una SQLException
            try (Connection conn = dataSource.getConnection();
                 PreparedStatement ps = conn.prepareStatement(sql)) {

                ps.setLong(1, idExpediente);
                if (poligonoOpcional != null) {
                    ps.setInt(2, poligonoOpcional);
                }

                try (ResultSet rs = ps.executeQuery()) {
                    while (rs.next()) {
                        lista.add(new FilaCertificadoJasperDTO(
                            rs.getString("codigo_expediente"),
                            rs.getString("nif_cif"),
                            rs.getString("nombre_completo"),
                            rs.getInt("poligono"),
                            rs.getInt("parcela"),
                            rs.getInt("recinto_sigpac"),
                            rs.getString("tipo_cultivo"),
                            rs.getBigDecimal("superficie_ha")
                        ));
                    }
                }
            }
            return lista;
        }

        /**
         * Registra en la tabla de auditoría 'certificados_emitidos' cada vez que se genera un PDF oficial.
         */
        public void registrarAuditoriaCertificado(
                Long idExpediente, Long idTitular, String csvVerificacion, int numParcelas, BigDecimal totalHa) throws Exception {

            String sqlInsert =
                "INSERT INTO certificados_emitidos " +
                "(numero_registro_salida, id_expediente, id_titular, codigo_csv_verificacion, " +
                " usuario_emisor, total_parcelas_incluidas, total_hectareas_certif) " +
                "VALUES (?, ?, ?, ?, ?, ?, ?)";

            try (Connection conn = dataSource.getConnection();
                 PreparedStatement ps = conn.prepareStatement(sqlInsert)) {

                ps.setString(1, "CERT-ROP-" + LocalDate.now().getYear() + "-" + System.currentTimeMillis() % 100000);
                ps.setLong(2, idExpediente);
                ps.setLong(3, idTitular);
                ps.setString(4, csvVerificacion);
                ps.setString(5, "secretaria.roperuelos");
                ps.setInt(6, numParcelas);
                ps.setBigDecimal(7, totalHa.setScale(4, RoundingMode.HALF_UP));
                ps.executeUpdate();
            }
        }
    }

    // =========================================================================
    // [PASO 3 Y 4] SERVICIO TRANSACCIONAL + GENERACIÓN PDF CON JASPER REPORTS
    // =========================================================================

    @ApplicationScoped
    public static class RoperuelosCertificadoService {

        @Inject
        private RoperuelosAgrarioRepository repository;

        /**
         * Orquesta de forma transaccional:
         * 1) La consulta de parcelas del expediente en SQL.
         * 2) El cálculo de verificación con BigDecimal.
         * 3) El registro de auditoría del Certificado y su CSV en base de datos.
         * 4) El relleno y exportación del PDF con JasperFillManager y JasperExportManager.
         */
        @Transactional(rollbackOn = Exception.class)
        public byte[] emitirCertificadoOficialPdf(
                ExpedienteMunicipalEntity expediente,
                Integer poligonoOpcional) throws Exception {

            // 1. Validamos que el expediente esté APROBADO antes de permitir emitir certificado oficial
            if (!"APROBADO".equalsIgnoreCase(expediente.getEstadoExpediente())) {
                throw new IllegalStateException("Solo se pueden emitir certificados oficiales de expedientes en estado APROBADO.");
            }

            // 2. Obtenemos las filas validadas mediante JDBC PreparedStatement
            List<FilaCertificadoJasperDTO> filas = repository.obtenerFilasParaJasperJdbc(
                    expediente.getId(), poligonoOpcional);

            if (filas.isEmpty()) {
                throw new IllegalStateException("No existen parcelas aprobadas para incluir en el certificado.");
            }

            // 3. Sumamos las hectáreas en Java con BigDecimal para guardarlas en el registro de salida
            BigDecimal totalHectareas = filas.stream()
                    .map(FilaCertificadoJasperDTO::getSuperficieHa)
                    .reduce(BigDecimal.ZERO, BigDecimal::add)
                    .setScale(4, RoundingMode.HALF_UP);

            // 4. Generamos el Código Seguro de Verificación (CSV) y registramos la emisión en base de datos
            String codigoCsv = "CSV-24136-" + expediente.getCampaniaAgricola() + "-"
                    + UUID.randomUUID().toString().substring(0, 8).toUpperCase();

            repository.registrarAuditoriaCertificado(
                    expediente.getId(),
                    expediente.getTitular().getId(),
                    codigoCsv,
                    filas.size(),
                    totalHectareas
            );

            // 5. Preparamos los Parámetros ($P{...}) para la plantilla informe_parcelas_titular.jrxml
            Map<String, Object> parametrosJasper = new HashMap<>();
            parametrosJasper.put("ID_TITULAR", expediente.getTitular().getId());
            parametrosJasper.put("CAMPANIA_AGRICOLA", expediente.getCampaniaAgricola());
            parametrosJasper.put("CODIGO_EXPEDIENTE", expediente.getCodigoExpediente());
            parametrosJasper.put("NOMBRE_AYUNTAMIENTO", "EXCMO. AYUNTAMIENTO DE ROPERUELOS DEL PÁRAMO (LEÓN)");
            parametrosJasper.put("CODIGO_CSV", codigoCsv);

            // 6. Cargamos y compilamos la plantilla .jrxml y la rellenamos con JRBeanCollectionDataSource
            try (InputStream jrxmlStream = getClass().getResourceAsStream("/reports/informe_parcelas_titular.jrxml")) {
                JasperReport plantillaCompilada = JasperCompileManager.compileReport(jrxmlStream);
                JRBeanCollectionDataSource dataSourceBeans = new JRBeanCollectionDataSource(filas);

                JasperPrint jasperPrint = JasperFillManager.fillReport(
                        plantillaCompilada,
                        parametrosJasper,
                        dataSourceBeans
                );

                // 7. Exportamos a formato binario PDF (byte[])
                return JasperExportManager.exportReportToPdf(jasperPrint);
            }
        }
    }

    // =========================================================================
    // [PASO 5] MANAGED BEAN JSF (@ViewScoped) PARA LA PANTALLA WEB XHTML
    // =========================================================================

    @Named("flujoRoperuelosBean")
    @ViewScoped
    public static class FlujoRoperuelosManagedBean implements Serializable {
        private static final long serialVersionUID = 1L;

        @Inject
        private RoperuelosAgrarioRepository repository;

        @Inject
        private RoperuelosCertificadoService certificadoService;

        // Criterios de búsqueda enlazados a los <h:inputText> de la vista XHTML
        private String nifBusqueda;
        private Integer poligonoBusqueda;
        private Integer campaniaBusqueda;

        // Resultados mostrados en el <p:dataTable>
        private List<ExpedienteMunicipalEntity> expedientesEncontrados;

        @PostConstruct
        public void init() {
            this.campaniaBusqueda = 2024;
            this.expedientesEncontrados = new ArrayList<>();
        }

        /**
         * Acción AJAX del botón "Buscar Agricultor / Polígono".
         */
        public void buscarPorNifYPoligono() {
            this.expedientesEncontrados = repository.buscarExpedientesPorNifYPoligono(
                    this.nifBusqueda, this.poligonoBusqueda, this.campaniaBusqueda);
        }

        /**
         * Acción no-AJAX (ajax="false") del botón "Emitir Certificado Oficial PDF (Jasper Reports)".
         */
        public void emitirYDescargarPdf(ExpedienteMunicipalEntity expedienteFila) {
            FacesContext fc = FacesContext.getCurrentInstance();
            ExternalContext ec = fc.getExternalContext();

            try {
                // Llama al servicio transaccional + Jasper Reports
                byte[] pdfBytes = certificadoService.emitirCertificadoOficialPdf(
                        expedienteFila, this.poligonoBusqueda);

                String nombrePdf = "Certificado_Roperuelos_" + expedienteFila.getCodigoExpediente() + ".pdf";

                // Configura las cabeceras HTTP para descarga limpia en el navegador
                ec.responseReset();
                ec.setResponseContentType("application/pdf");
                ec.setResponseContentLength(pdfBytes.length);
                ec.setResponseHeader("Content-Disposition", "attachment; filename=\"" + nombrePdf + "\"");

                try (OutputStream out = ec.getResponseOutputStream()) {
                    out.write(pdfBytes);
                    out.flush();
                }

                // Detiene el ciclo de vida JSF en Fase 5 para no renderizar HTML sobre el stream del PDF
                fc.responseComplete();

            } catch (Exception e) {
                fc.addMessage(null, new FacesMessage(
                        FacesMessage.SEVERITY_ERROR,
                        "No se pudo emitir el Certificado PDF",
                        e.getMessage()));
            }
        }

        public String getNifBusqueda() { return nifBusqueda; }
        public void setNifBusqueda(String nifBusqueda) { this.nifBusqueda = nifBusqueda; }
        public Integer getPoligonoBusqueda() { return poligonoBusqueda; }
        public void setPoligonoBusqueda(Integer poligonoBusqueda) { this.poligonoBusqueda = poligonoBusqueda; }
        public Integer getCampaniaBusqueda() { return campaniaBusqueda; }
        public void setCampaniaBusqueda(Integer campaniaBusqueda) { this.campaniaBusqueda = campaniaBusqueda; }
        public List<ExpedienteMunicipalEntity> getExpedientesEncontrados() { return expedientesEncontrados; }
    }
}
```

---
## ARCHIVO: posibles_repreguntas_del_tribunal_seresco.md

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

