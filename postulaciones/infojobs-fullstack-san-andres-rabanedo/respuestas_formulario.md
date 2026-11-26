# Respuestas Exactas para el Cuestionario Previo de InfoJobs — Desarrollador/a Full Stack (San Andrés del Rabanedo)

Aquí tienes las respuestas listas para marcar y pegar en las **5 preguntas eliminatorias** de la oferta:

---

### 1. ¿Has desarrollado aplicaciones reales con React, Next.js o tecnologias equivalentes?
- Marca: **`SI`**

### 2. ¿Tienes experiencia profesional trabajando directamente con SQL y bases de datos como PostgreSQL, My SQL o similares?
- Marca: **`SI`**

### 3. ¿Has integrado aplicaciones o sistemas mediante APIs REST, Webhooks, N8N, Zapier o conexión directa con bases de datos?
- Marca: **`SI`**

### 4. ¿Has desarrollado automatizaciones que hayan funcionado en producción?
- Marca: **`SI`**

---

### 5. Describe una automatización o integración que hayas desarrollado de principio a fin. Indica el problema, las tecnologías utilizadas, que parte realizaste tu y cuanto tardaste en ponerla en funcionamiento.

*(Copia y pega este texto; responde de forma estructurada exactamente a los 5 puntos que pide la pregunta: Problema, Tecnologías, Tu rol end-to-end, Tiempo de puesta en marcha e Impacto en producción):*

> `Problema: En HORSE Technologies existía un proceso crítico de negocio donde la información operativa provenía de múltiples sistemas desconectados (bases de datos relacionales SQL, APIs externas y hojas de cálculo), lo que obligaba a cruzar datos manualmente cada día, generando retrasos y discrepancias entre plataformas.`
>
> `Tecnologías utilizadas: Python, Go, APIs REST, Webhooks, protocolo MCP (Model Context Protocol) / flujos de orquestación automatizados (equivalentes a n8n), conexión directa con bases de datos SQL (PostgreSQL, SQL Server y BigQuery), Dataform, Docker y un panel web en React/JavaScript para visualizar el estado de las ejecuciones.`
>
> `Qué parte realicé yo (100% de principio a fin): Tomé los requisitos directamente con el equipo, diseñé la arquitectura de integración, programé los conectores hacia las APIs REST y las consultas parametrizadas hacia las bases de datos SQL, implementé un motor automático de validación y reconciliación de discrepancias con reintentos y alertas por webhook, y lo desplegué en producción con Docker.`
>
> `Tiempo de puesta en funcionamiento: Tardé 2 semanas en tener la primera versión funcional (MVP) operando en producción y 1 semana adicional en añadir el panel de monitorización y el sistema de alertas automáticas, reduciendo un trabajo manual diario de varias horas a una ejecución 100% desatendida en pocos minutos.`
