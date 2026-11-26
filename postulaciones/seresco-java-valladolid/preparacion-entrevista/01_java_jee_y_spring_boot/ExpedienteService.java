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
