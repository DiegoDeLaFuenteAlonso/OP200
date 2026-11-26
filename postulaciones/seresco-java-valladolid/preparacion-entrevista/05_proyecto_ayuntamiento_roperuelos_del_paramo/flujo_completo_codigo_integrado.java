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
