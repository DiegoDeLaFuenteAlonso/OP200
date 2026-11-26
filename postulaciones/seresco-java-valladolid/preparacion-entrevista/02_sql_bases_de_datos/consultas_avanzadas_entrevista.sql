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
