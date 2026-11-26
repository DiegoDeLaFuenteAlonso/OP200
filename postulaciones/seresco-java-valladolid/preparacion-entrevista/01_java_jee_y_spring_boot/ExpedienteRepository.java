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
