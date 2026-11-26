---
name: empleo-kit-ats
description: >-
  Use this skill whenever generating or updating a job application package (Kit ATS) for a specific job offer
  inside postulaciones/<slug>/, including oferta_analizada.md, cv_spec.json, 1-page justified CV (.pdf and .docx),
  1-page justified Cover Letter (.pdf without bold text in body), and respuestas_formulario.md.
---

# Generación de Paquete de Postulación ATS Completo (`empleo-kit-ats`)

Estándar oficial de 2.ª generación para crear candidaturas de alto impacto en `postulaciones/<slug>/` dentro de este proyecto.

## 1. Fuentes Obligatorias y Reglas Anti-Invención

Antes de redactar cualquier archivo del kit:
1. Lee `perfil/master_cv.md` y `perfil/preferencias.json`.
2. Lee la descripción completa y las preguntas reales del formulario de la oferta (navegando o inspeccionando la URL de inscripción si está disponible).
3. **Regla de Oro de Veracidad**:
   - **Inmutables**: Empresas (`HORSE Technologies`, `FDS, a DXC Technology Company`, `Ayuntamiento de Roperuelos del Páramo`, `Craftelier`), periodos y titulaciones oficiales (`Especialización IA y Big Data`, `DAW`, `DAM` en IES San Andrés).
   - **Adaptables**: El subtítulo del CV, el orden de competencias, las palabras clave exactas del ATS y las equivalencias técnicas reales (ej. `Dataform <-> dbt`, `Agent Harness / Loop Engineering <-> LangGraph / flujos con estado`, `Spring Boot <-> JEE / MVC`). Nunca inventes experiencias en empresas inexistentes ni certificaciones no cursadas.

## 2. Los 8 Artefactos Requeridos en `postulaciones/<slug>/`

Cada carpeta de candidatura debe quedar autocontenida con estos archivos:

1. **`oferta_analizada.md`**:
   - Datos clave (empresa, rol, modalidad, salario si consta, URL de la oferta y URL directa del formulario, `% Match`).
   - Desglose de *Must-Have Hard Skills*, *Puntos Fuertes (Exact Hits)* y *Estrategia Honesta de Mitigación de Gaps*.
2. **`cv_spec.json`**:
   - Especificación estructurada con bloques `CVTitle`, `CVSubtitle`, `CVContact`, `CVHeading`, `CVJobHeader`, `CVJobDate`, `CVBody` y `bullet_list`.
   - Idioma: Español por defecto, o **Inglés** si la oferta y el formulario están íntegramente en inglés (ej. `aircall-software-engineer-graduate`, `elevenlabs-data-engineer`).
3. **`carta_spec.json`** *(o definición equivalente en `build_pdfs.py`)* + **`carta_presentacion.md`**:
   - Versión Markdown legible (`carta_presentacion.md`) y especificación para el PDF formal.
   - **Regla Tipográfica Estricta de la Carta**: Texto justificado (`TA_JUSTIFY`) y **CERO negritas (`<b>` / `**`) dentro de los párrafos del cuerpo ni en las viñetas** (solo el nombre superior en cabecera va en negrita). Esto evita el aspecto artificial típico de textos generados por IA.
4. **`Diego_de_la_Fuente_Alonso_CV_<Empresa>_<Rol>.pdf`**:
   - Exactamente **1 página A4**, texto de perfil y viñetas completamente justificados (`TA_JUSTIFY`).
5. **`Diego_de_la_Fuente_Alonso_CV_<Empresa>_<Rol>.docx`**:
   - Documento Word ATS limpio generado desde el mismo `cv_spec.json` con texto justificado.
6. **`Diego_de_la_Fuente_Alonso_Carta_Presentacion_<Empresa>.pdf`** *(o `_Cover_Letter_` en inglés)*:
   - Exactamente **1 página A4**, justificada, sin negritas en el cuerpo.
7. **`respuestas_formulario.md`**:
   - Respuestas listas para copiar y pegar (`Copy-paste answer`) a cada pregunta obligatoria y opcional del portal (*Teamtailor, Greenhouse, Viterbit, Bizneo, InfoJobs, Tecnoempleo, Workday*).
   - Incluye horquilla salarial calibrada al rol/ubicación y disponibilidad estándar (`15 días naturales / laborables`).
   - Si es una autocandidatura sin formulario, genera además `estrategia_autocandidatura.md` (email en frío, nota de LinkedIn y seguimiento Día +5).
8. **`build_pdfs.py`** *(o invocación reproducible a `render_ats_kit.py`)*:
   - Script para regenerar los PDFs/DOCX localmente en cualquier momento.

## 3. Renderizado y Validación Automática de 1 Página (`uv run`)

`reportlab` y `python-docx` se ejecutan siempre mediante **`uv run`** (no uses `pip install` global). Usa el motor incluido en esta skill: [render_ats_kit.py](./scripts/render_ats_kit.py).

### Formato de `carta_spec.json` soportado por `render_ats_kit.py`

```json
{
  "output_pdf": "Diego_de_la_Fuente_Alonso_Carta_Presentacion_Empresa.pdf",
  "output_cv_pdf": "Diego_de_la_Fuente_Alonso_CV_Empresa_Rol.pdf",
  "output_cv_docx": "Diego_de_la_Fuente_Alonso_CV_Empresa_Rol.docx",
  "role_header": "Analista Programador Java | Java 11+ · Spring Boot · SQL · APIs REST",
  "contact_header": "España (100% Teletrabajo / Valladolid)  |  (+34) 626 68 71 79  |  diegodelafuentealonso@gmail.com",
  "date": "16 de noviembre de 2026",
  "recipient": "Para: Equipo de Selección — Empresa",
  "subject": "Asunto: Candidatura a Puesto",
  "salutation": "Estimado equipo de Selección,",
  "opening_paragraphs": ["Párrafo inicial...", "Segundo párrafo introductorio..."],
  "bullets": ["Punto clave 1 sin negritas...", "Punto clave 2 sin negritas..."],
  "closing_paragraphs": ["Disponibilidad de 15 días naturales..."],
  "signoff": "Atentamente,",
  "signature_role": "Desarrollador Backend / Data & AI Engineer"
}
```

### Comando de Ejecución y Verificación

```powershell
uv run --with reportlab --with python-docx --with pypdf python .agents/skills/empleo-kit-ats/scripts/render_ats_kit.py postulaciones/<slug>
```

El script:
1. Genera el CV en `.pdf` y `.docx` y la Carta en `.pdf` (limpiando automáticamente cualquier negrita accidental del cuerpo de la carta).
2. Comprueba con `pypdf` que **ambos PDFs tienen exactamente `1` página**. Si alguno ocupa 2 páginas, devuelve código de error indicando cuál ajustar (`cv_spec.json` o `carta_spec.json`).

## 4. Cierre del Flujo

Una vez validado el Kit ATS:
1. Actualiza la vacante en `ofertas/tracker.json` poniendo `"estado": "preparada_para_postular"` y detallando la ruta `postulaciones/<slug>/` en `"notas"`.
2. Sincroniza el dashboard ejecutando:
   ```powershell
   python .agents/skills/empleo-radar-tracker/scripts/sync_tracker_dashboard.py --sync
   ```
