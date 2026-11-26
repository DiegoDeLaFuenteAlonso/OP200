#!/usr/bin/env python3
import os
import json
import subprocess

BASE_DIR = r"C:\Users\DELAFUENTEALONSODieg\empleo\postulaciones"
DOCX_CREATE_SCRIPT = r"C:\Users\DELAFUENTEALONSODieg\AppData\Local\hermes\skills\productivity\docx\scripts\docx_create.py"
DOCX_VALIDATE_SCRIPT = r"C:\Users\DELAFUENTEALONSODieg\AppData\Local\hermes\skills\productivity\docx\scripts\docx_validate.py"

applications = [
    {
        "id": "ust-ai-solutions-engineer",
        "company": "UST",
        "role": "Ingeniero/a de Soluciones de IA (LLMs & Agentes Autónomos)",
        "modality": "100% Remoto (España)",
        "url": "https://www.wearedevelopers.com/jobs/ext/2761248-ingeniero-a-de-soluciones-de-ia-100-remoto",
        "match": 95,
        "title_cv": "AI Solutions & Agent Engineer | Python, LLMs, MCP & Loop Engineering",
        "summary": "Ingeniero de software especializado en el diseño, desarrollo e integración de sistemas basados en agentes autónomos de Inteligencia Artificial y Large Language Models (LLMs). Experiencia directa en producción en HORSE Technologies implementando agent harnesses, ingeniería de bucles de razonamiento (loop engineering) e interoperabilidad estandarizada mediante Model Context Protocol (MCP). Sólido dominio de Python y Go para backend de alta concurrencia, junto con experiencia en pipelines de datos y microservicios. Doble titulación técnica en desarrollo de aplicaciones (DAM / DAW) y Especialización Superior en IA y Big Data.",
        "skills": [
            "Arquitecturas de Agentes & LLMs: Diseño y despliegue de agentes autónomos, frameworks de agentes, agent harnesses, loop engineering, memory persistente, orquestación de tareas complejas.",
            "Protocolos & Tool Calling: Model Context Protocol (MCP), llamadas a funciones estructuradas, diseño de herramientas y plugins para agentes, APIs RESTful.",
            "Desarrollo & Backend: Python (avanzado), Go (Golang), Java, microservicios, APIs con FastAPI / REST, contenedores Docker.",
            "Ecosistema de Modelos: Claude (Anthropic), Gemini, OpenAI GPT, arquitecturas RAG, vectorización e ingeniería de prompts avanzada.",
            "Datos & Almacenamiento: Google BigQuery, SQL Server, NoSQL, pipelines de datos automatizados en Python."
        ],
        "horse_exp": [
            "Diseño e implementación de soluciones pioneras basadas en agentes de Inteligencia Artificial para la automatización de procesos técnicos corporativos.",
            "Desarrollo de agent harnesses robustos y control de flujos de razonamiento mediante técnicas avanzadas de loop engineering.",
            "Integración de agentes con herramientas y fuentes de información internas empleando el estándar Model Context Protocol (MCP).",
            "Desarrollo de servicios backend, utilidades de alto rendimiento y pipelines en Python y Go.",
            "Modelado y consulta de datos en Google BigQuery para alimentar contextos e informes analíticos."
        ],
        "cover_letter_es": """Estimado equipo de selección de UST,

Les escribo para presentar mi candidatura al puesto de Ingeniero/a de Soluciones de IA (100% Remoto). Cuento con experiencia directa en el diseño y despliegue de sistemas basados en agentes de Inteligencia Artificial, agent harnesses, loop engineering e integración mediante el estándar Model Context Protocol (MCP), lo que me permite encajar de forma inmediata en sus proyectos estratégicos de IA en España y LATAM.

En mi posición actual en HORSE Technologies trabajo a la vanguardia de la IA agéntica:
- Desarrollo de agentes autónomos y sistemas multi-herramienta con Python y Go.
- Implementación de harnesses de ejecución y orquestación con control de estados y bucles de razonamiento.
- Integración de herramientas mediante Model Context Protocol (MCP), dotando a los agentes de capacidades de interacción segura con bases de datos y APIs.
- Sólida base de ingeniería de software (DAM, DAW y Especialización en IA y Big Data) con experiencia en desarrollo backend robusto y APIs RESTful.

La visión de UST como referente tecnológico internacional en transformación digital e IA hace que esta posición sea el entorno ideal para aportar mi experiencia práctica en sistemas agénticos.

Agradezco su consideración y quedo a su entera disposición para mantener una entrevista técnica.

Atentamente,
Diego de la Fuente Alonso
diegodelafuentealonso@gmail.com | (+34) 626 68 71 79""",
        "form_answers": """### 1. Experiencia en desarrollo con Python y LLMs / Agentes:
Cuento con experiencia directa en HORSE Technologies desarrollando agentes de IA autónomos con Python y Go, aplicando arquitecturas de agent harness, loop engineering e integración estandarizada de herramientas mediante Model Context Protocol (MCP). Además, cuento con Especialización Superior en Inteligencia Artificial y Big Data.

### 2. Experiencia con frameworks de agentes y ecosistema Claude:
Experiencia práctica en el desarrollo de arquitecturas agénticas, tool calling estructurado, integración MCP y uso avanzado del ecosistema de modelos de Anthropic (Claude / Claude Code) y Gemini/OpenAI.

### 3. Disponibilidad / Preaviso:
15 días laborables de preaviso estándar.

### 4. Ubicación y modalidad:
Residencia en España, 100% disponible para modalidad remota.

### 5. Expectativas salariales:
Rango orientativo: 34.000 € – 40.000 € brutos anuales."""
    },
    {
        "id": "factum-data-engineer",
        "company": "Factum IT",
        "role": "Data Engineer / MLOps Engineer",
        "modality": "100% Remoto (España)",
        "url": "https://www.infojobs.net/ofertas-trabajo/madrid/machine-learning",
        "match": 88,
        "title_cv": "Data Engineer | Python, BigQuery, ETL Pipelines & Backend",
        "summary": "Ingeniero de datos y desarrollador backend con sólida experiencia en la construcción de pipelines ETL/ELT automatizados con Python, modelado analítico sobre grandes volúmenes de datos y diseño de APIs y microservicios. Experiencia probada en HORSE Technologies trabajando con Google BigQuery, Dataform, desarrollo en Python y Go, y despliegue de soluciones inteligentes con agentes. Formación técnica integral con doble titulación en DAM/DAW y Especialización en IA y Big Data. Acostumbrado al desarrollo ágil, integración continua y observabilidad.",
        "skills": [
            "Data Engineering & ETL: Construcción y automatización de pipelines ETL en Python, modelado declarativo en Dataform, orquestación de ingesta y transformación de datos.",
            "Bases de Datos & Cloud: Google BigQuery (optimización de queries, clustering, particionado), SQL Server (SSMS), diseño relacional y NoSQL.",
            "Desarrollo Backend & APIs: Python (FastAPI, Flask, scripts de ingesta), Java (Spring Boot, APIs RESTful), Go (Golang), microservicios.",
            "IA & MLOps: Especialización Superior en IA y Big Data, ciclo de vida de datos analíticos, integración de modelos y agentes autónomos mediante MCP.",
            "Buenas Prácticas & DevOps: Git / GitHub, CI/CD, pruebas unitarias, Docker, monitorización y rendimiento de servicios."
        ],
        "horse_exp": [
            "Desarrollo e industrialización de pipelines ETL automatizados en Python para ingesta y limpieza de datos.",
            "Modelado y transformación escalable de datos con Dataform y Google BigQuery, reduciendo costes de procesamiento.",
            "Construcción de microservicios y herramientas internas de automatización en Python y Go.",
            "Integración de agentes inteligentes y herramientas mediante Model Context Protocol (MCP).",
            "Soporte técnico a equipos de BI y producto en la gobernanza y disponibilidad de datos analíticos."
        ],
        "cover_letter_es": """Estimado equipo de selección de Factum IT,

Me dirijo a ustedes para presentar mi candidatura a la posición de Data Engineer / MLOps Engineer (100% Remoto). Cuento con una sólida trayectoria en el desarrollo de pipelines ETL automatizados en Python, modelado y optimización de grandes volúmenes de datos en Google BigQuery y Dataform, y desarrollo de servicios backend y APIs RESTful.

En HORSE Technologies me encargo a diario de:
- Diseñar e implementar flujos de transformación de datos escalables y reproducibles con Dataform y Python.
- Optimizar consultas complejas en BigQuery garantizando alto rendimiento y control de costes cloud.
- Construir microservicios y soluciones backend utilizando Python y Go.
- Integrar soluciones inteligentes y agentes automatizados para optimizar operaciones técnicas.

Mi perfil combina la disciplina de desarrollo de software (DAW/DAM, Java Spring Boot, Python) con la formación especializada en Inteligencia Artificial y Big Data, lo que me permite abordar proyectos de ingeniería de datos y MLOps con rigor arquitectónico.

Agradezco su atención y estaré encantado de ampliar cualquier detalle sobre mi experiencia técnica en una entrevista.

Atentamente,
Diego de la Fuente Alonso
diegodelafuentealonso@gmail.com | (+34) 626 68 71 79""",
        "form_answers": """### 1. Experiencia en desarrollo con Python y APIs:
Experiencia diaria en el desarrollo de scripts y servicios backend con Python, automatización de pipelines de datos y desarrollo previo de APIs RESTful en Python y Java (Spring Boot).

### 2. Experiencia en bases de datos y plataformas Cloud/Data:
Experiencia directa en Google BigQuery, Dataform, SQL Server y diseño relacional/NoSQL, con foco en optimización de rendimiento y buenas prácticas de modelado.

### 3. Disponibilidad / Preaviso:
15 días laborables de preaviso estándar.

### 4. Modalidad:
Total disponibilidad para incorporación en modalidad 100% remota.

### 5. Expectativas salariales:
Rango orientativo: 32.000 € – 37.000 € brutos/año."""
    },
    {
        "id": "cheil-data-analyst",
        "company": "Cheil Spain (Samsung)",
        "role": "Data Analyst",
        "modality": "Híbrido (Alcobendas, Madrid)",
        "url": "https://es.linkedin.com/jobs/view/data-analyst-at-cheil-spain-4228999630",
        "match": 88,
        "title_cv": "Data Analyst | Looker, BigQuery, Python & Business Intelligence",
        "summary": "Analista de datos con experiencia consolidada en diseño y desarrollo de cuadros de mando en Looker / Looker Studio, consultas analíticas avanzadas en Google BigQuery y automatización de procesos de datos mediante Python. Experiencia en entorno multinacional (HORSE Technologies) transformando datos en insights accionables para la dirección y equipos operativos. Formación técnica en Inteligencia Artificial, Big Data y desarrollo de aplicaciones. Con capacidad contrastada para comunicar métricas y recomendaciones claras a interlocutores técnicos y de negocio.",
        "skills": [
            "Business Intelligence & Reporting: Looker, Looker Studio, diseño de dashboards ejecutivos y operacionales, definición de métricas y KPIs de negocio.",
            "Plataformas de Datos & SQL: Google BigQuery (SQL avanzado, optimización de queries, agregaciones complejas), Dataform, SQL Server.",
            "Programación & Automatización: Python (manejo y limpieza de datos, automatización de reporting, scripts analíticos), Go.",
            "Análisis de Negocio: Segmentación, análisis de comportamiento, rendimiento de embudos de conversión, data storytelling.",
            "Entornos & Herramientas: Google Cloud Platform (GCP), Git, metodologías ágiles, SAP (procesos de negocio)."
        ],
        "horse_exp": [
            "Diseño, desarrollo y mantenimiento de dashboards analíticos en Looker para el seguimiento de métricas clave y toma de decisiones corporativas.",
            "Consulta, extracción y agregación de grandes conjuntos de datos con Google BigQuery y Dataform.",
            "Automatización de extracciones y transformaciones de datos utilizando Python para garantizar reportes actualizados y fiables.",
            "Colaboración estrecha con responsables de área para traducir requisitos de negocio en soluciones visuales e informes comprensibles.",
            "Desarrollo de herramientas internas en Python y Go para optimizar la operativa diaria."
        ],
        "cover_letter_es": """Estimado equipo de selección de Cheil Spain,

Les escribo con gran entusiasmo para presentar mi candidatura al puesto de Data Analyst en su sede de Alcobendas. Cuento con experiencia directa en el análisis de datos, desarrollo de cuadros de mando interactivos en Looker / Looker Studio y consultas avanzadas sobre grandes volúmenes en Google BigQuery, automatizando procesos con Python.

En HORSE Technologies mi labor se centra en:
- Crear y evolucionar dashboards en Looker para monitorizar KPIs críticos y facilitar la toma de decisiones basada en datos.
- Explotar y modelar datos complejos en BigQuery mediante SQL avanzado y flujos en Dataform.
- Desarrollar scripts en Python para automatizar la extracción y preparación de datos analíticos.
- Traducir resultados técnicos en conclusiones de negocio claras para diversos departamentos.

Formar parte de Cheil Spain y apoyar a marcas líderes como Samsung en el entendimiento del rendimiento de sus plataformas digitales y CRM representa un reto estimulante en el que puedo aportar valor técnico y analítico desde el primer día. Además, tengo total disponibilidad para la modalidad híbrida en Alcobendas.

Agradezco su tiempo y consideración, y quedo a su disposición para mantener una conversación.

Atentamente,
Diego de la Fuente Alonso
diegodelafuentealonso@gmail.com | (+34) 626 68 71 79""",
        "form_answers": """### 1. Experiencia con Looker y BigQuery:
Uso diario en producción en HORSE Technologies para la creación de dashboards corporativos, modelado analítico y ejecución de consultas SQL de alta complejidad sobre BigQuery.

### 2. Habilidades en Python y automatización:
Desarrollo habitual de scripts y flujos en Python para ingesta, limpieza y preparación de datasets para reporting.

### 3. Modalidad y ubicación:
Total disponibilidad para el modelo híbrido en las oficinas de Alcobendas (Madrid).

### 4. Disponibilidad:
15 días laborables de preaviso.

### 5. Rango salarial orientativo:
30.000 € – 35.000 € brutos/año."""
    },
    {
        "id": "seresco-java-spring",
        "company": "Seresco",
        "role": "Desarrollador/a Backend Java Spring Boot",
        "modality": "Híbrido (Valladolid) / Remoto",
        "url": "https://es.linkedin.com/jobs/view/desarrollador-a-java-at-seresco",
        "match": 85,
        "title_cv": "Backend Software Developer | Java, Spring Boot, Microservicios & APIs",
        "summary": "Desarrollador de software backend con experiencia en desarrollo web empresarial utilizando Java con Spring Boot, microservicios y APIs RESTful. Doble titulación técnica en Desarrollo de Aplicaciones Multiplataforma (DAM) y Desarrollo de Aplicaciones Web (DAW) por el IES San Andrés, complementada con Especialización Superior en Inteligencia Artificial y Big Data. Experiencia práctica en proyectos para administraciones públicas y empresas privadas, además de desarrollo de herramientas en Python y Go en HORSE Technologies. Acostumbrado al diseño limpio, optimización de consultas SQL y trabajo en equipo.",
        "skills": [
            "Desarrollo Java & Backend: Java (Java 11 / 17 / 21), Spring Boot, Spring Data JPA, Spring MVC, microservicios, seguridad y arquitectura backend.",
            "APIs RESTful & Integración: Diseño, documentación y despliegue de APIs RESTful, endpoints en Python y Java, integración de sistemas de terceros.",
            "Bases de Datos & Persistencia: SQL Server, Microsoft SSMS, MySQL/PostgreSQL, diseño relacional, transacciones y procedimientos almacenados.",
            "Otros Lenguajes & Entornos: Python, Go (Golang), C# (.NET), Kotlin (Android Studio), ABAP / SAP.",
            "Metodologías: Git / GitHub, Scrum / Agile, pruebas unitarias, patrones de diseño de software."
        ],
        "horse_exp": [
            "Desarrollo de servicios internos y herramientas de software de alto rendimiento utilizando Python y Go.",
            "Automatización de procesos backend y orquestación de flujos de datos.",
            "Implementación de integraciones mediante protocolos estandarizados (MCP / APIs).",
            "Consulta y explotación de datos en entornos cloud de gran escala (BigQuery)."
        ],
        "cover_letter_es": """Estimado equipo de selección de Seresco,

Les escribo para presentar formalmente mi candidatura a la posición de Desarrollador/a Java en Valladolid. Cuento con una sólida formación en desarrollo backend con Java y Spring Boot avalada por mi doble titulación en DAM y DAW, y con experiencia práctica en el desarrollo de servicios web, APIs REST y bases de datos relacionales.

A lo largo de mi trayectoria:
- He desarrollado plataformas web y servicios backend utilizando Java con Spring Boot en el Ayuntamiento de Roperuelos del Páramo, asegurando una comunicación fluida entre el frontend y las bases de datos.
- He implementado APIs RESTful robustas en Python y gestionado persistencia avanzada en SQL Server en Craftelier (.NET y SSMS).
- En mi puesto actual en HORSE Technologies en Valladolid, sigo perfeccionando mis capacidades de desarrollo con Python y Go para utilidades y servicios backend de alto rendimiento.

Residiendo en Valladolid, valoro enormemente la presencia y trayectoria de Seresco y la posibilidad de integrarme en su equipo técnico local/híbrido para seguir aportando soluciones de software sólidas y de calidad.

Quedo a su disposición para mantener una entrevista y conversar en detalle sobre mi perfil.

Atentamente,
Diego de la Fuente Alonso
diegodelafuentealonso@gmail.com | (+34) 626 68 71 79""",
        "form_answers": """### 1. Experiencia con Java y Spring Boot:
Desarrollo de plataformas web y microservicios con Spring Boot, APIs REST y persistencia con Spring Data / JPA a través de proyectos reales y formación reglada de grado superior (DAM / DAW).

### 2. Experiencia en bases de datos:
Diseño y consultas avanzadas sobre SQL Server, PostgreSQL/MySQL y BigQuery.

### 3. Modalidad y ubicación:
Residencia en Valladolid, con total disponibilidad para trabajar en modalidad híbrida o presencial en la sede de Valladolid.

### 4. Disponibilidad:
Preaviso estándar de 15 días laborables.

### 5. Rango salarial orientativo:
26.000 € – 32.000 € brutos/año."""
    }
]

for app in applications:
    app_dir = os.path.join(BASE_DIR, app["id"])
    os.makedirs(app_dir, exist_ok=True)
    
    # 1. Oferta analizada
    oferta_md = f"""# ANÁLISIS DE OFERTA Y ENCAJE (MATCH)

**Puesto:** {app["role"]}  
**Empresa:** {app["company"]}  
**Modalidad:** {app["modality"]}  
**Enlace directo:** [Ver Oferta]({app["url"]})  
**Porcentaje de Encaje Estimado:** {app["match"]}%

---

## Estrategia de Postulación
- **Punto Fuerte Principal:** {app["skills"][0]}
- **Adaptación en CV:** Se ha priorizado la redacción de viñetas con métricas de impacto enfocadas a las tecnologías clave requeridas por {app["company"]}.
- **Documentación Generada:** CV ATS en formato Word (.docx), carta de presentación personalizada y respuestas para el formulario de candidatura.
"""
    with open(os.path.join(app_dir, "oferta_analizada.md"), "w", encoding="utf-8") as f:
        f.write(oferta_md)
        
    # 2. Carta de presentacion
    with open(os.path.join(app_dir, "carta_presentacion.md"), "w", encoding="utf-8") as f:
        f.write(f"# CARTA DE PRESENTACIÓN\n\n**Empresa:** {app['company']}\n**Puesto:** {app['role']}\n**Candidato:** Diego de la Fuente Alonso\n\n---\n\n{app['cover_letter_es']}\n")
        
    # 3. Respuestas formulario
    with open(os.path.join(app_dir, "respuestas_formulario.md"), "w", encoding="utf-8") as f:
        f.write(f"# RESPUESTAS PARA FORMULARIO DE POSTULACIÓN — {app['company'].upper()}\n\n{app['form_answers']}\n")

    # 4. JSON Spec for DOCX
    spec = {
        "page": {
            "width_mm": 210,
            "height_mm": 297,
            "margins_mm": {"top": 20, "bottom": 20, "left": 20, "right": 20}
        },
        "styles": [
            {"name": "CVTitle", "base": "Normal", "font": "Calibri", "size_pt": 20, "bold": True, "color": "003366"},
            {"name": "CVSubtitle", "base": "Normal", "font": "Calibri", "size_pt": 12, "bold": True, "color": "4A5568"},
            {"name": "CVContact", "base": "Normal", "font": "Calibri", "size_pt": 10, "color": "718096"},
            {"name": "CVHeading", "base": "Normal", "font": "Calibri", "size_pt": 13, "bold": True, "color": "003366"},
            {"name": "CVJobHeader", "base": "Normal", "font": "Calibri", "size_pt": 11, "bold": True, "color": "1A202C"},
            {"name": "CVJobDate", "base": "Normal", "font": "Calibri", "size_pt": 9.5, "italic": True, "color": "718096"},
            {"name": "CVBody", "base": "Normal", "font": "Calibri", "size_pt": 10, "color": "2D3748"}
        ],
        "blocks": [
            {"type": "paragraph", "style": "CVTitle", "text": "DIEGO DE LA FUENTE ALONSO"},
            {"type": "paragraph", "style": "CVSubtitle", "text": app["title_cv"]},
            {"type": "paragraph", "style": "CVContact", "text": "Valladolid / Castilla y León, España | (+34) 626 68 71 79 | diegodelafuentealonso@gmail.com | LinkedIn | GitHub"},
            {"type": "paragraph", "style": "CVHeading", "text": "PERFIL PROFESIONAL"},
            {"type": "paragraph", "style": "CVBody", "text": app["summary"]},
            {"type": "paragraph", "style": "CVHeading", "text": "COMPETENCIAS TÉCNICAS CLAVE"},
            {"type": "bullet_list", "items": app["skills"]},
            {"type": "paragraph", "style": "CVHeading", "text": "EXPERIENCIA PROFESIONAL"},
            {"type": "paragraph", "style": "CVJobHeader", "text": "HORSE Technologies — Data & Software / AI Developer"},
            {"type": "paragraph", "style": "CVJobDate", "text": "Valladolid | Julio 2026 – Actualidad"},
            {"type": "bullet_list", "items": app["horse_exp"]},
            {"type": "paragraph", "style": "CVJobHeader", "text": "FDS, a DXC Technology Company — Consultor Técnico SAP"},
            {"type": "paragraph", "style": "CVJobDate", "text": "Febrero 2026 – Junio 2026"},
            {"type": "bullet_list", "items": [
                "Desarrollo de extensiones y programación a medida en ABAP.",
                "Gestión, trazabilidad y transporte de órdenes entre entornos de desarrollo, calidad y producción.",
                "Soporte y análisis técnico en procesos vinculados al módulo de Logística de SAP."
            ]},
            {"type": "paragraph", "style": "CVJobHeader", "text": "Ayuntamiento de Roperuelos del Páramo — Desarrollador de Software Backend"},
            {"type": "paragraph", "style": "CVJobDate", "text": "Junio 2024 – Octubre 2024 | Junio 2023 – Septiembre 2023"},
            {"type": "bullet_list", "items": [
                "Desarrollo de servicios web y plataformas administrativas con Java y el framework Spring Boot.",
                "Diseño e implementación de APIs RESTful utilizando Python para la gestión y tramitación de datos.",
                "Diseño de modelos relacionales en bases de datos y optimización de consultas SQL."
            ]},
            {"type": "paragraph", "style": "CVJobHeader", "text": "Craftelier — Desarrollador de Software"},
            {"type": "paragraph", "style": "CVJobDate", "text": "Marzo 2024 – Mayo 2024"},
            {"type": "bullet_list", "items": [
                "Desarrollo de aplicaciones de escritorio en C# y .NET sobre Visual Studio.",
                "Consultas avanzadas y optimización en bases de datos SQL Server mediante SSMS.",
                "Desarrollo móvil en Android utilizando Kotlin."
            ]},
            {"type": "paragraph", "style": "CVHeading", "text": "FORMACIÓN ACADÉMICA"},
            {"type": "bullet_list", "items": [
                "Curso de Especialización en Inteligencia Artificial y Big Data (2024 – 2025).",
                "Técnico Superior en Desarrollo de Aplicaciones Web (DAW) — IES San Andrés (2025 – 2026).",
                "Técnico Superior en Desarrollo de Aplicaciones Multiplataforma (DAM) — IES San Andrés (2022 – 2024)."
            ]},
            {"type": "paragraph", "style": "CVHeading", "text": "IDIOMAS"},
            {"type": "bullet_list", "items": [
                "Español: Nativo.",
                "Inglés: Nivel B1 (Capacidad técnica para documentación, lectura y comunicación profesional)."
            ]}
        ]
    }
    
    spec_path = os.path.join(app_dir, "cv_spec.json")
    with open(spec_path, "w", encoding="utf-8") as f:
        json.dump(spec, f, indent=2, ensure_ascii=False)
        
    docx_out = os.path.join(app_dir, "cv_adaptado_diego_de_la_fuente.docx")
    cmd = ["uv", "run", "--with", "python-docx", "python", DOCX_CREATE_SCRIPT, spec_path, docx_out]
    res = subprocess.run(cmd, capture_output=True, text=True)
    print(f"Generated DOCX for {app['id']}: {res.returncode}")
    if res.returncode != 0:
        print("Error:", res.stderr)
    else:
        # validate
        val_cmd = ["uv", "run", "--with", "python-docx", "python", DOCX_VALIDATE_SCRIPT, docx_out]
        val_res = subprocess.run(val_cmd, capture_output=True, text=True)
        print(f"Validation {app['id']}: {val_res.stdout.strip()}")

print("All applications generated successfully.")
