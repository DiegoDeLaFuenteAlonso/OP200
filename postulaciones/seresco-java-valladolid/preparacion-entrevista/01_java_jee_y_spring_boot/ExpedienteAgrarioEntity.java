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
