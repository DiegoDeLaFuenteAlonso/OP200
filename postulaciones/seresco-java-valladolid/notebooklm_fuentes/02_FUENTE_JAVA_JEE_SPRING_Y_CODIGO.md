# FUENTE 02 — JAVA, JAKARTA EE (JEE), SPRING BOOT, JPA/HIBERNATE Y CÓDIGO COMENTADO

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

