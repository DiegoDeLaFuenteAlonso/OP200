#!/usr/bin/env python3
import os
import json
import subprocess

BASE_DIR = r"C:\Users\DELAFUENTEALONSODieg\empleo\postulaciones"
DOCX_CREATE = r"C:\Users\DELAFUENTEALONSODieg\AppData\Local\hermes\skills\productivity\docx\scripts\docx_create.py"
DOCX_VAL = r"C:\Users\DELAFUENTEALONSODieg\AppData\Local\hermes\skills\productivity\docx\scripts\docx_validate.py"

pepper_dir = os.path.join(BASE_DIR, "pepper-data-analyst")
os.makedirs(pepper_dir, exist_ok=True)

with open(os.path.join(pepper_dir, "oferta_analizada.md"), "w", encoding="utf-8") as f:
    f.write("""# ANÁLISIS DE OFERTA — PEPPER

**Puesto:** Data Analyst – Jr Data Scientist  
**Empresa:** PEPPER (Servicios de financiación al consumo)  
**Modalidad:** Híbrido (Madrid, 3 días oficina / 2 remoto, viernes de 9:00 a 15:00)  
**Salario:** 30.000 € – 40.000 € Bruto/año (+ 10% variable anual)  
**Fecha de publicación:** Activa (hace 1-2 días)  
**Enlace directo:** [Ver en InfoJobs](https://www.infojobs.net/ofertas-trabajo/analista-de-datos-jr)  
**Encaje estimado:** 96%

---

## Puntos Fuertes de Encaje:
- **SQL Server & Consultas analíticas:** Experiencia demostrable en Craftelier y HORSE.
- **Visualización y Cuadros de Mando:** Experiencia creando dashboards operativos y de negocio en Looker.
- **Uso de LLMs e IA Generativa como parte del flujo:** Diego trabaja directamente en HORSE con arquitecturas de agentes, loop engineering y MCP.
- **Prototipado rápido de MVPs:** Desarrollo ágil con Python, Go y APIs REST.
""")

with open(os.path.join(pepper_dir, "carta_presentacion.md"), "w", encoding="utf-8") as f:
    f.write("""# CARTA DE PRESENTACIÓN — PEPPER

**Empresa:** PEPPER (Área de Data & Advanced Analytics)  
**Posición:** Data Analyst – Jr Data Scientist  
**Candidato:** Diego de la Fuente Alonso  

---

Estimado equipo de selección de PEPPER,

Les escribo para presentar mi candidatura al puesto de Data Analyst – Jr Data Scientist en su sede de Madrid. Me apasiona su enfoque de situar los datos y la IA en el núcleo de las decisiones de negocio, combinando la exploración analítica con el uso nativo de LLMs e inteligencia artificial generativa.

En mi trayectoria profesional:
- **Analítica de datos y reporting:** En HORSE Technologies diseño y mantengo dashboards de reporting corporativo con Looker, explotando datos analíticos en Google BigQuery y automatizando pipelines con Python.
- **SQL avanzado y bases de datos:** Cuento con experiencia sólida en optimización y consultas sobre SQL Server (SSMS en Craftelier) y entornos relacionales/cloud.
- **Integración de IA y LLMs:** Desarrollo activamente soluciones con agentes de IA, agent harnesses, loop engineering e integraciones mediante Model Context Protocol (MCP), lo que me permite aplicar modelos de lenguaje de forma natural y eficaz para acelerar la exploración y el prototipado de datos.
- **Formación técnica integral:** Graduado en DAM, DAW y con Especialización Superior en Inteligencia Artificial y Big Data.

La propuesta de valor de PEPPER —un entorno ágil donde se fomenta la curiosidad, el prototipado rápido de MVPs y el aprendizaje continuo— encaja exactamente con mi forma de trabajar. Además, tengo total disponibilidad para el modelo híbrido en Madrid.

Agradezco su tiempo y quedo a su entera disposición para mantener una entrevista.

Atentamente,  
Diego de la Fuente Alonso  
diegodelafuentealonso@gmail.com | (+34) 626 68 71 79
""")

with open(os.path.join(pepper_dir, "respuestas_formulario.md"), "w", encoding="utf-8") as f:
    f.write("""# RESPUESTAS PARA FORMULARIO INFOJOBS — PEPPER

### 1. Experiencia en análisis de datos y SQL Server:
Experiencia consolidada en consultas SQL complejas sobre SQL Server y BigQuery, modelado y diseño de dashboards analíticos en Looker para reporting corporativo en HORSE Technologies y proyectos previos en Craftelier.

### 2. Experiencia con herramientas de IA y LLMs:
Trabajo habitualmente integrando modelos de lenguaje y sistemas agénticos con Python, aplicando agent harnesses y MCP. Cuento además con el Curso de Especialización en Inteligencia Artificial y Big Data.

### 3. Disponibilidad y modelo de trabajo:
Preaviso estándar de 15 días laborables. Total disponibilidad para el modelo híbrido (3 días oficina en Madrid / 2 días remoto).

### 4. Pretensiones salariales:
Acorde al rango ofrecido: 34.000 € – 38.000 € brutos/año (+ variable).
""")

pepper_spec = {
    "page": {"width_mm": 210, "height_mm": 297, "margins_mm": {"top": 20, "bottom": 20, "left": 20, "right": 20}},
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
        {"type": "paragraph", "style": "CVSubtitle", "text": "Data Analyst & Jr. Data Scientist | SQL Server, BI Dashboards & LLM Integration"},
        {"type": "paragraph", "style": "CVContact", "text": "Valladolid / Madrid, España | (+34) 626 68 71 79 | diegodelafuentealonso@gmail.com | LinkedIn | GitHub"},
        {"type": "paragraph", "style": "CVHeading", "text": "PERFIL PROFESIONAL"},
        {"type": "paragraph", "style": "CVBody", "text": "Analista de datos con perfil híbrido orientado a analítica avanzada, visualización y desarrollo de soluciones impulsadas por IA. Experiencia práctica en HORSE Technologies gestionando cuadros de mando analíticos en Looker, consultas SQL complejas sobre petabytes y desarrollo de agentes de Inteligencia Artificial mediante agent harnesses e integración MCP. Dominio de SQL Server, Python y modelado de datos para negocio. Sólida formación con doble grado superior en DAM/DAW y Especialización en Inteligencia Artificial y Big Data. Mentalidad proactiva para el prototipado rápido de MVPs y optimización de procesos."},
        {"type": "paragraph", "style": "CVHeading", "text": "COMPETENCIAS TÉCNICAS"},
        {"type": "bullet_list", "items": [
            "Analítica de Datos & Business Intelligence: Looker / Looker Studio, diseño de paneles y dashboards ejecutivos, visualización de métricas de negocio, data storytelling.",
            "Bases de Datos & SQL: SQL Server (SSMS, consultas complejas, optimización, procedimientos), Google BigQuery, Dataform, bases de datos relacionales y NoSQL.",
            "Inteligencia Artificial & LLMs: Integración nativa de LLMs (Claude, Gemini, OpenAI) en workflows de análisis, desarrollo de agentes autónomos, loop engineering, Model Context Protocol (MCP).",
            "Programación & ETL: Python (procesamiento de datos, automatización, scripting avanzado), Go, Java (Spring Boot, APIs RESTful), .NET / C#.",
            "Metodologías: Prototipado ágil de MVPs, trabajo autónomo orientado a negocio, Git/GitHub, control de versiones."
        ]},
        {"type": "paragraph", "style": "CVHeading", "text": "EXPERIENCIA LABORAL"},
        {"type": "paragraph", "style": "CVJobHeader", "text": "HORSE Technologies — Data Analyst & Software / AI Developer"},
        {"type": "paragraph", "style": "CVJobDate", "text": "Valladolid | Julio 2026 – Actualidad"},
        {"type": "bullet_list", "items": [
            "Diseño, despliegue y mantenimiento de cuadros de mando analíticos en Looker para seguimiento de indicadores estratégicos.",
            "Consultas analíticas avanzadas y transformación de grandes conjuntos de datos con Google BigQuery y Dataform.",
            "Automatización de pipelines ETL y tareas de preparación de datos con Python.",
            "Investigación e integración de agentes de Inteligencia Artificial para automatización y análisis asistido por LLMs (agent harness, MCP).",
            "Desarrollo de herramientas internas de software en Python y Go."
        ]},
        {"type": "paragraph", "style": "CVJobHeader", "text": "Craftelier — Desarrollador de Software & Bases de Datos"},
        {"type": "paragraph", "style": "CVJobDate", "text": "Marzo 2024 – Mayo 2024"},
        {"type": "bullet_list", "items": [
            "Optimización de consultas y creación de scripts SQL en SQL Server Management Studio (SSMS).",
            "Desarrollo de aplicaciones de escritorio en entorno .NET / C# sobre Visual Studio.",
            "Desarrollo de módulos móviles en Android con Kotlin."
        ]},
        {"type": "paragraph", "style": "CVJobHeader", "text": "Ayuntamiento de Roperuelos del Páramo — Desarrollador Backend & APIs"},
        {"type": "paragraph", "style": "CVJobDate", "text": "Junio 2024 – Octubre 2024 | Junio 2023 – Septiembre 2023"},
        {"type": "bullet_list", "items": [
            "Desarrollo de plataformas web y microservicios con Java y Spring Boot.",
            "Diseño de APIs REST en Python y optimización de flujos de datos relacionales."
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
            "Inglés: Nivel B1 técnico (documentación, lectura y entornos ágiles)."
        ]}
    ]
}

spec_path = os.path.join(pepper_dir, "cv_spec.json")
with open(spec_path, "w", encoding="utf-8") as f:
    json.dump(pepper_spec, f, indent=2, ensure_ascii=False)

docx_out = os.path.join(pepper_dir, "cv_adaptado_diego_de_la_fuente.docx")
subprocess.run(["uv", "run", "--with", "python-docx", "python", DOCX_CREATE, spec_path, docx_out], check=True)
subprocess.run(["uv", "run", "--with", "python-docx", "python", DOCX_VAL, docx_out], check=True)

print("PEPPER package generated and verified successfully.")
