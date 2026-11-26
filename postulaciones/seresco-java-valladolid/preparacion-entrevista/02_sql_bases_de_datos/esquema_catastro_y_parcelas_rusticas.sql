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
