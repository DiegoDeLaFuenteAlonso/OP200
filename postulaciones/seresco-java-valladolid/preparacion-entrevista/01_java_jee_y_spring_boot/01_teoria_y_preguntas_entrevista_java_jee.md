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
