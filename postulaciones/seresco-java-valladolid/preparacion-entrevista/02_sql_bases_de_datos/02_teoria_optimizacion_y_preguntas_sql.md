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
