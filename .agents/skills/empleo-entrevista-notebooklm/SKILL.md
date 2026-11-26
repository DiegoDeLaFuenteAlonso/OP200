---
name: empleo-entrevista-notebooklm
description: >-
  Use this skill when the user asks to prepare for a technical or HR job interview for a specific company,
  create word-for-word interview scripts, defend their CV or salary expectations, write annotated study code
  mapped to their past roles, or generate consolidated study sources for Google NotebookLM.
---

# Preparación Profunda de Entrevistas + Fuentes NotebookLM (`empleo-entrevista-notebooklm`)

Playbook modelado a partir del caso de referencia `postulaciones/seresco-java-valladolid/` para convertir cualquier candidatura en un repositorio de preparación técnica, defensa de CV y estudio asistido con **Google NotebookLM**.

## 1. Auditoría Previa de Coherencia Documental

Antes de escribir ni una sola línea de preparación:
1. Lee **exactamente** lo que Diego entregó o tiene generado en `postulaciones/<slug>/`:
   - `cv_spec.json` (y versiones previas si hubiera otra candidatura a la misma empresa, como ocurrió entre `seresco-java-spring` y `seresco-java-valladolid`).
   - `carta_presentacion.md`
   - `respuestas_formulario.md` (especialmente expectativa económica indicada, años declarados y preaviso).
   - `perfil/master_cv.md`
2. **Regla de Cero Contradicción**: Los guiones orales deben coincidir al 100% con las fechas, tecnologías, horquilla salarial y argumentos ya enviados a la empresa.

## 2. Inteligencia del Proyecto Real de la Empresa / Sede

Investiga en la web qué clientes, productos, licitaciones o arquitecturas reales maneja esa empresa **en la sede o equipo concreto de la oferta** (ej. clientes sector público/agrario/banca/automoción, stack legacy vs moderno). Demostrar conocimiento del contexto real del equipo diferencia radicalmente al candidato.

## 3. Estructura de Archivos a Generar en `postulaciones/<slug>/`

```text
postulaciones/<slug>/
├── preparacion.md                                      # Guía rápida de 5 minutos antes de entrar
├── preparacion-entrevista/
│   ├── 00_INDICE_Y_ESTRATEGIA_ENTREVISTA.md            # Guiones palabra por palabra, salario, cambio desde HORSE y tabla STAR
│   ├── 01_<stack_principal_1>/                         # Teoría + 15 preguntas trampa + código real comentado línea a línea
│   ├── 02_<stack_principal_2>/                         # Ej. SQL / BigQuery / Dataform con esquema y consultas resueltas
│   ├── 03_<stack_principal_3>/                         # Ej. Framework web / Agentes IA / MCP / CI-CD
│   ├── 04_<stack_principal_4>/                         # Ej. Testing / Reporting / Cloud / Arquitectura
│   └── 05_proyecto_estrella_<empresa_pasada>/          # Caso end-to-end defendible basado en un puesto real del CV + 15 repreguntas
└── notebooklm_fuentes/
    ├── 00_COMPLETO_TODO_EN_UNO_<EMPRESA>_NOTEBOOKLM.md # Compendio único si se quiere subir 1 sola fuente maestra
    ├── 01_FUENTE_ESTRATEGIA_CV_Y_CARTA.md
    ├── 02_FUENTE_<BLOQUE_1>.md
    ├── ...
    └── 06_FUENTE_PROYECTO_ESTRELLA.md
```

## 4. Elementos Obligatorios del Bloque Estratégico (`00_INDICE_Y_ESTRATEGIA_ENTREVISTA.md`)

1. **Pitch inicial de 90 segundos (*«Háblame de ti»*)**: Orden cronológico-lógico conectando DAM + Especialización IA/Big Data + DAW con Roperuelos del Páramo, Craftelier, FDS (DXC Technology: rigor `DEV -> QAS -> PRD`) y HORSE Technologies.
2. **Respuesta a *«¿Por qué quieres cambiar desde HORSE Technologies si entraste en julio de 2026?»***: Siempre positiva hacia HORSE, enfocada como decisión vocacional hacia el stack/producto de la empresa destino y estabilidad a largo plazo.
3. **Defensa de expectativas salariales y disponibilidad**: Alineada con lo escrito en `respuestas_formulario.md`, mostrando flexibilidad a tablas internas y retribución flexible, y preaviso estándar de `15 días`.
4. **Puentes técnicos honestos**: Si una tecnología de la oferta se tocó menos en el último puesto (ej. JSF frente a Spring Boot, o dbt frente a Dataform, o LangGraph frente a Agent Harnesses propios), redacta la equivalencia arquitectónica exacta para demostrar solvencia inmediata sin mentir.
5. **Tabla STAR de competencias blandas**: Mapea cada competencia mencionada en la oferta a una anécdota concreta y medible del CV de Diego.
6. **3 preguntas inteligentes para el final de la entrevista**: Específicas sobre el proyecto técnico, arquitectura y dinámica del equipo.

## 5. Reglas de Formato para `notebooklm_fuentes/`

Google NotebookLM rinde mejor cuando cada fuente `.md`:
- Es **completamente autocontenida** (incluye contexto en cabecera, teoría explicada en voz clara y los bloques de código incrustados directamente dentro del Markdown).
- Evita referencias rotas a rutas locales externas.
- Incluye bloques tipo *«Pregunta del entrevistador → Respuesta ideal en voz alta → Repregunta técnica y cómo salir airoso»*, ideales para generar el *Audio Overview* (podcast de repaso) o pedir a NotebookLM que actúe como tribunal técnico.

Consulta la referencia de un caso completo real en `postulaciones/seresco-java-valladolid/preparacion-entrevista/00_INDICE_Y_ESTRATEGIA_ENTREVISTA.md`.
