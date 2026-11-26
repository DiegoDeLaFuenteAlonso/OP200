# RESPUESTAS PARA EL FORMULARIO DE POSTULACIÓN — ELEVENLABS (DATA ENGINEER)

**Vacante:** Data Engineer (Remote – Spain)  
**URL:** https://elevenlabs.io/careers/e53c5be6-5c1a-4870-ad85-8397a1f201de/data-engineer  

*(Las respuestas están redactadas en **inglés**, ya que el formulario y el proceso de selección de ElevenLabs son 100% en inglés, con la traducción/explicación debajo para tu referencia).*

---

### 1. Why ElevenLabs, and why now?

**Copy-paste answer (English):**
> Most data engineering roles treat AI as an afterthought, or treat data pipelines as purely static batch jobs for dashboards. What excites me about ElevenLabs right now is that you are scaling across three massive product lines (ElevenAgents, ElevenCreative, and ElevenAPI) while explicitly building a data stack where **declarative data modeling and AI agents converge**—specifically your goal of creating AI agents to serve data questions alongside a trusted transformation and metrics layer.
>
> "Why now" for me comes down to what I am currently building at HORSE Technologies: my daily work sits at the exact intersection of modern cloud data engineering (Python ETLs, Google BigQuery, declarative SQL transformations with Dataform, and Looker semantic layers) and production AI agent engineering (building agent harnesses, loop engineering, and connecting agents to enterprise systems via the Model Context Protocol - MCP). Joining ElevenLabs as an early Data Engineer allows me to bring both halves of my profile together in a high-velocity, AI-first team where clean data architecture directly powers autonomous agents and self-service analytics.

*(Resumen en español: Conecta el momento de hipercrecimiento de ElevenLabs —ElevenAgents, ElevenCreative, ElevenAPI— y su objetivo explícito en la oferta de "crear agentes de IA para responder preguntas de datos" con tu doble perfil exacto en HORSE Technologies: pipelines de datos en BigQuery/Dataform/Looker + desarrollo de agent harnesses e integraciones MCP).*

---

### 2. What's the most impactful thing you've built? What was your specific contribution?

**Copy-paste answer (English):**
> At HORSE Technologies, the most impactful system I built was an end-to-end analytical data pipeline and an MCP-enabled AI agent harness that connected our enterprise data warehouse to internal operational workflows. Before this, business and operations teams relied on fragmented data sources and manual ad-hoc requests to track key operational metrics, creating bottlenecks for the data team.
>
> **My specific contribution (end-to-end ownership):**
> 1. **Ingestion & Transformation Layer:** I wrote automated Python ETL services to ingest raw operational data into Google BigQuery and designed declarative transformation pipelines in Dataform (staging, intermediate, and mart models with dependency graphs, partitioning, clustering, and automated data quality assertions—following the same software engineering principles used in dbt).
> 2. **Semantic & BI Layer:** I modeled and maintained the semantic layer and executive dashboards in Looker (LookML) so stakeholders had a single source of truth for certified KPIs.
> 3. **AI Agent Integration (MCP):** I designed an AI agent execution harness in Python and Go using loop engineering patterns and integrated it with internal company tools and data sources through the **Model Context Protocol (MCP)**, enabling reliable, permissioned, and structured tool calling over our data without manual intervention.

*(Resumen en español: Presenta como hito principal tu arquitectura completa en HORSE Technologies, dividida en 3 capas que cubren el 100% de lo que pide la oferta de ElevenLabs: 1. Ingesta Python + modelado declarativo en Dataform/BigQuery, 2. Capa semántica en Looker, y 3. El agent harness con Loop Engineering y MCP para consultar/operar sobre sistemas internos).*

---

### 3. How did you know it worked? What did success actually look like?

**Copy-paste answer (English):**
> I measured success across three concrete dimensions: **data reliability, query/pipeline efficiency, and stakeholder self-service adoption**.
>
> 1. **Pipeline & Data Quality Reliability:** Schema changes and silent data drift were caught automatically by Dataform quality assertions before reaching downstream Looker dashboards or agent tools, eliminating broken morning reports and manual data-cleaning firefighting.
> 2. **Performance & Cost Efficiency:** By restructuring raw queries into incremental, partitioned, and clustered tables in BigQuery, query execution times for heavy operational reports dropped from minutes to seconds while significantly reducing bytes scanned per query.
> 3. **Real Self-Service & Agent Determinism:** For the MCP agent harness, success meant moving from brittle prompt-only prototypes to deterministic execution loops where tool calls returned grounded, verifiable data with zero schema hallucinations. In practice, success looked like business stakeholders answering their own recurring operational questions through Looker explores and automated workflows, freeing engineering time to build new data products rather than running ad-hoc SQL queries.

*(Resumen en español: Define el éxito con métricas de ingeniería reales que ElevenLabs valora: 1. Calidad del dato validada antes de llegar a BI/agentes gracias a tests declarativos, 2. Reducción de costes y latencia en BigQuery mediante particionado/clustering y modelos incrementales, y 3. Autoservicio real y determinismo en los agentes MCP sin alucinaciones de esquema).*

---

### 4. Have you used ElevenLabs - even in a personal or side project? What did you build or explore?

**Copy-paste answer (English):**
> Yes. While building and customizing my own local AI agent environment and multi-tool workflows (using Python and MCP-based agent tooling), I have explored and integrated TTS voice synthesis pipelines (`ElevenAPI` / low-latency audio generation) to give autonomous agents a natural voice output layer for voice-note summaries and hands-free technical briefings.
>
> What stood out to me from an engineering perspective was how ElevenLabs handles streaming latency, voice stability parameters, and multilingual pronunciation (especially switching between technical English terms and Spanish) without breaking conversational cadence. I have also been closely following the architecture of **ElevenAgents**—particularly how tool calling, sub-second turn-taking, and evaluation guardrails are orchestrated in production voice agents.

*(Resumen en español: Respuesta honesta y técnica: menciona tu exploración práctica integrando capacidades de síntesis de voz / TTS en tu propio entorno de agentes personales y flujos MCP para generar resúmenes de voz bilingües español/inglés, destacando aspectos técnicos reales de ElevenLabs como la latencia en streaming, estabilidad de voz en cambio de idioma y la arquitectura de tool-calling de ElevenAgents).*
