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

Activa bajo demanda la skill adecuada según la tarea:

- **Buscar ofertas, verificar URLs o sincronizar tracker + dashboard**: `empleo-radar-tracker` (apoyada opcionalmente por `career-ops` para escaneo de portales ATS).
- **Evaluar a fondo si merece la pena postular (scoring A–G, red flags, match %)**: `career-ops` y `job-description-analyzer`.
- **Generar el paquete completo de candidatura en `postulaciones/<slug>/` (PDF + DOCX + Carta + Formulario)**: `empleo-kit-ats` (combinable con `resume-tailor`, `tech-resume-optimizer`, `resume-ats-optimizer`, `resume-bullet-writer`, `cover-letter-generator` y `application-form-filler`).
- **Preparar una entrevista técnica/RRHH con código comentado y fuentes para NotebookLM**: `empleo-entrevista-notebooklm` y `interview-prep-generator` (o los modos `es/interview/*` de `career-ops`).
- **Optimizar LinkedIn, redactar autocandidaturas en frío o negociar/comparar ofertas**: `linkedin-profile-optimizer`, `cold-email-writer`, `salary-negotiation-prep` y `offer-comparison-analyzer`.
