# FUENTE 03 — SQL, OPTIMIZACIÓN DE ÍNDICES, ESQUEMA CATASTRAL Y 10 CONSULTAS AVANZADAS

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

