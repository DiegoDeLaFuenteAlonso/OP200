---
name: empleo-radar-tracker
description: >-
  Use this skill whenever searching for new job openings, verifying whether job URLs are still active,
  adding or updating job offers in ofertas/tracker.json, importing user decisions (solicitado/descartado),
  or synchronizing ofertas/tracker.json with ofertas/dashboard_ofertas.html.
---

# Radar de Empleo y Sincronización `tracker.json` ↔ `dashboard_ofertas.html`

Skill específica del proyecto `empleo` para descubrir, verificar y mantener sincronizado el catálogo de ofertas de **Diego de la Fuente Alonso**.

## 1. Preparación Obligatoria

Antes de buscar o filtrar ofertas, lee:
- `perfil/master_cv.md`
- `perfil/preferencias.json`

### Criterios de Priorización del Candidato
1. **Experiencia**: Prioridad máxima a **Becas / Prácticas / Contratos Formativos (FP DAM/DAW < 3 años)** y puestos **0–1 año (Sin experiencia / Junior)** (`exp_min_anios` `0` o `1`), seguidos de `Hasta 2 años`.
2. **Modalidad y Ubicación**:
   - **100% Remoto / Teletrabajo desde España** (prioridad nº 1).
   - **Presencial o Híbrido en Valladolid / León / Castilla y León** o **Híbrido flexible en Madrid**.
3. **Roles y Stack Objetivo**:
   - *AI & Agent Engineer*: Agentes IA, LLMs (Gemini, Claude, OpenAI), MCP, LangGraph, n8n/automatización, Python, Go.
   - *Data Analyst / Data Engineer*: BigQuery, GCP, Dataform/dbt, Looker/Power BI, SQL/SQL Server, pipelines ETL en Python.
   - *Backend / Full-Stack Developer*: Java + Spring Boot / JEE / JSP / JSF, Python (FastAPI), Go, C#/.NET, SAP ABAP, DevSecOps Junior (CI/CD, Docker).

## 2. Reglas de Verificación de Enlaces (*Liveness Gate*)

1. **Nunca guardes enlaces genéricos de búsqueda** (ej. `/ofertas-trabajo/madrid` sin ID de oferta). Toda URL debe apuntar a una ficha concreta (`/of-i...` en InfoJobs, `/rf-...` en Tecnoempleo, `/jobs/<id>` en Greenhouse/Teamtailor/Bizneo/Ashby/Lever, slug único en Viterbit).
2. **Comprueba que la vacante sigue abierta**: Verifica mediante lectura/consulta web que la página muestra descripción real y botón de inscripción, y que no devuelve `404`, redirección a portada ni mensaje de *"proceso cerrado / ya no acepta candidaturas"*.
3. Si una oferta existente en `ofertas/tracker.json` ha expirado o cerrado, cambia su `"estado"` a `"cerrada"` o `"expirada"` (el script de sincronización la excluirá automáticamente de `dashboard_ofertas.html` conservando el histórico en `tracker.json`).

## 3. Esquema Requerido en `ofertas/tracker.json`

Cada entrada activa dentro de `"ofertas"` debe incluir:

```json
{
  "id": "empresa-rol-clave-modalidad",
  "empresa": "Nombre Empresa",
  "rol": "Título claro del puesto (Stack clave) – Modalidad",
  "categoria": "Data Engineering | Data Analytics | IA & Agentes | Backend Development | Becas & Prácticas / ...",
  "es_beca": false,
  "modalidad": "100% Remoto (España) | Híbrido (Valladolid) | Híbrido (Madrid)",
  "ubicacion": "España (100% Remoto) | Valladolid | Madrid",
  "salario": "25.000 € – 32.000 € Bruto/año",
  "stack_principal": ["Python", "SQL", "BigQuery"],
  "fecha_publicacion": "Publicada el DD/MM/YYYY (Activa en <Portal>)",
  "estado": "descubierta",
  "decision": "pendiente",
  "porcentaje_match_estimado": 94,
  "exp_min_anios": 1,
  "exp_rango": "0-1 años (Junior / Sin exp.)",
  "exp_detalle": "Detalle literal del requisito de experiencia y titulación (ej. FP Grado Superior)",
  "url": "https://...",
  "notas": "Resumen táctico de por qué encaja con el perfil de Diego."
}
```

Valores válidos de `"estado"`:
- `"descubierta"` / `"activa_fresca"` / `"activa_vigente"`: oferta activa sin kit o pendiente de empaquetar.
- `"preparada_para_postular"`: paquete ATS completo ya generado en `postulaciones/<carpeta>/` (activa el badge `★ KIT ATS LISTO` en el dashboard).
- `"cerrada"` / `"expirada"`: archivada en `tracker.json`, oculta en el dashboard activo.

Valores válidos de `"decision"`: `"pendiente"`, `"solicitado"`, `"descartado"`.

## 4. Sincronización y Auditoría Automática

Nunca edites a mano el bloque gigante `const OFFERS = [...]` de `ofertas/dashboard_ofertas.html` si puedes sincronizarlo de forma determinista con el script incluido en esta skill: [sync_tracker_dashboard.py](./scripts/sync_tracker_dashboard.py).

### Comandos del Script

1. **Auditar consistencia** (entre `tracker.json`, `dashboard_ofertas.html` y `postulaciones/`):
   ```powershell
   python .agents/skills/empleo-radar-tracker/scripts/sync_tracker_dashboard.py --check
   ```
2. **Sincronizar `tracker.json` → `dashboard_ofertas.html`** (actualiza `total_activas_verificadas`, fecha, `const OFFERS` y todos los contadores de botones/desplegables del HTML):
   ```powershell
   python .agents/skills/empleo-radar-tracker/scripts/sync_tracker_dashboard.py --sync
   ```
3. **Importar decisiones descargadas del navegador (`estados_ofertas.json`)** y sincronizar ambos archivos:
   ```powershell
   python .agents/skills/empleo-radar-tracker/scripts/sync_tracker_dashboard.py --import-decisions estados_ofertas.json --sync
   ```
