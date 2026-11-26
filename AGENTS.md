# Guía Operativa del Proyecto `empleo` — Diego de la Fuente Alonso

Este repositorio es el centro de operaciones de búsqueda de empleo, seguimiento de vacantes, generación de paquetes ATS y preparación técnica de entrevistas de **Diego de la Fuente Alonso**.

## 1. Fuentes Exclusivas de Verdad

Antes de evaluar cualquier vacante, adaptar un CV o redactar respuestas de formulario, consulta siempre:
- `perfil/master_cv.md` — Historial laboral real verificable, titulaciones oficiales y stack técnico.
- `perfil/preferencias.json` — Roles objetivo, modalidades preferidas (*100% Remoto* e *Híbrido Valladolid / Madrid / Castilla y León*), keywords clave y portales prioritarios.
- `ofertas/tracker.json` — Base de datos maestra de ofertas, estados y decisiones.

## 2. Reglas Inquebrantables

1. **Cero invención (`No Fabrication`)**: Jamás inventes empresas, fechas, títulos académicos ni autoría de herramientas externas. Adapta el enfoque, prioriza tecnologías reales del historial de Diego y explicita equivalencias arquitectónicas honestas (`Dataform <-> dbt`, `Agent Harness / Loop Engineering <-> LangGraph`, `Spring Boot <-> JEE/MVC`).
2. **Verificación de enlaces vivos (`Liveness Gate`)**: Toda oferta añadida a `ofertas/tracker.json` debe tener enlace directo a la vacante activa (nunca páginas de búsqueda genéricas ni ofertas cerradas/404).
3. **Sincronización doble obligatoria**: Cualquier cambio en `ofertas/tracker.json` debe sincronizarse con `ofertas/dashboard_ofertas.html` ejecutando `python .agents/skills/empleo-radar-tracker/scripts/sync_tracker_dashboard.py --sync`.
4. **Estándar tipográfico de Kits ATS (`postulaciones/<slug>/`)**:
   - CV en `.pdf` y `.docx` de **exactamente 1 página A4** con texto justificado.
   - Carta de presentación en `.pdf` de **exactamente 1 página A4**, texto justificado y **sin negritas en los párrafos del cuerpo ni en las viñetas**.
   - Ejecuta siempre `reportlab`, `python-docx` y `pypdf` mediante `uv run` (sin `pip install` global).
5. **Control humano de envíos**: Prepara todos los materiales listos para enviar, pero nunca pulses botones de envío final (*Submit / Inscribirme*) en portales externos sin autorización explícita del usuario.

## 3. Enrutamiento de Skills del Proyecto (`.agents/skills/`)

Activa bajo demanda la skill adecuada según la fase de la búsqueda de empleo (**44 skills activas**):

- **Descubrimiento de ofertas, ATS públicos, trabajo remoto internacional y sincronización del tracker**: `empleo-radar-tracker`, `hunter-scout` (APIs públicas Greenhouse/Lever/Ashby/Workday), `remote-international-jobs` (elegibilidad EMEA/España, EOR vs contractor, anti-estafas) y `career-ops`.
- **Investigación de empresas y evaluación de encaje (fit, red flags, ATS)**: `company-researcher` (negocio, salud financiera y test AI-native vs AI-washed), `job-description-analyzer`, `ats-detective` (reglas específicas por proveedor ATS: Workday, Greenhouse, Lever, Ashby, Teamtailor, SAP SuccessFactors, etc.) y `career-ops`.
- **CV, cuantificación, auditoría, minería de evidencia y control anti-invención**: `empleo-kit-ats` (render 1 página PDF/DOCX + Carta + Formulario), `claim-check` (verificación final anti-alucinación frente a `perfil/master_cv.md`), `resume-auditor` (crítica dura de reclutador en 30 s), `evidence-miner` (extracción read-only de logros reales desde git/PRs), `resume-tailor`, `tech-resume-optimizer`, `resume-ats-optimizer`, `resume-bullet-writer`, `resume-quantifier`, `resume-formatter`, `resume-section-builder`, `resume-version-manager`, `career-changer-translator`, `cover-letter-generator` y `application-form-filler`.
- **GitHub, portfolio y *proof-of-work* técnico**: `github-profile-optimization` (perfil y 6 repos fijados), `github-profile-readme` (README de perfil en 9 arquetipos), `readme-optimization` (READMEs de proyectos), `portfolio-case-study-writer` y `proof-asset-creator`.
- **LinkedIn, networking, referrals, bandeja de recruiters y seguimiento**: `linkedin-profile-optimizer`, `linkedin-360brew-planner` (publicaciones bajo algoritmo 360Brew), `networking-referral-outreach`, `cold-email-writer`, `hunter-connector` (localizar hiring manager y conseguir *coffee chats*), `hunter-followup` (seguimientos Día +10, *thank-you notes* y reglas de parada), `triage-inbox` (clasificación de correos de recruiters) y `draft-reply` (respuestas calibradas por intención).
- **Entrevistas (banco STAR, simulacros técnicos/IA, coaching y NotebookLM)**: `empleo-entrevista-notebooklm`, `interview-coach` (coaching adaptativo, análisis de transcripciones y *storybank*), `mock-interviewer` (simulacros Coding, Eval Design, Agent Debugging, LLM System Design, Architecture Defense y Behavioral con rúbrica 1–5), `star-story-extractor`, `interview-prep-generator` y los modos `es/interview/*` de `career-ops`.
- **Referencias, negociación, comparación de ofertas y hoja de ruta profesional**: `reference-list-builder`, `salary-negotiation-prep`, `offer-comparison-analyzer` y `map-career-path`.
