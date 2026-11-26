#!/usr/bin/env python3
import os
import json
import subprocess

BASE_DIR = r"C:\Users\DELAFUENTEALONSODieg\empleo\postulaciones"
DOCX_CREATE = r"C:\Users\DELAFUENTEALONSODieg\AppData\Local\hermes\skills\productivity\docx\scripts\docx_create.py"
DOCX_VAL = r"C:\Users\DELAFUENTEALONSODieg\AppData\Local\hermes\skills\productivity\docx\scripts\docx_validate.py"

factum_dir = os.path.join(BASE_DIR, "factum-data-engineer")
os.makedirs(factum_dir, exist_ok=True)

# 1. Oferta analizada
with open(os.path.join(factum_dir, "oferta_analizada.md"), "w", encoding="utf-8") as f:
    f.write("""# ANÁLISIS DE OFERTA Y ENCAJE — FACTUM IT

**Puesto:** Data Engineer / MLOps Engineer  
**Empresa:** Factum IT  
**Modalidad:** Solo teletrabajo (100% Remoto España)  
**Contrato:** Indefinido, Jornada Completa  
**Enlace directo:** [Oferta en InfoJobs](https://www.infojobs.net/madrid/data-engineer/of-i4ec868ae6d42e584edbd1372e9ad49)  
**Encaje estimado:** 92%

---

## 1. Requisitos Clave de la Vacante vs. Perfil de Diego

| Requisito de Factum IT | Importancia | Encaje Diego | Estrategia de Justificación en el CV |
|---|---|---|---|
| **Python sólido** | Imprescindible | 🟢 100% | Desarrollo diario en HORSE, automatización ETL, scripts y utilidades en Python. |
| **APIs y servicios con FastAPI / REST** | Imprescindible | 🟢 100% | Desarrollo backend de APIs REST en Python y Java (Spring Boot) en proyectos reales. |
| **MLflow & Ciclo de Vida ML** | Imprescindible | 🟢 90% | Dominio adquirido en el Curso de Especialización en IA y Big Data y puesto en práctica en pipelines de IA. |
| **Azure Databricks / Cloud & Datos** | Imprescindible | 🟢 85% | Experiencia en grandes plataformas de datos (BigQuery, Dataform), procesamiento distribuido y SQL Server. |
| **Docker, Kubernetes / AKS, CI/CD** | Imprescindible | 🟢 85% | Contenedores, despliegue continuo y control de versiones Git en proyectos backend. |
| **SQL Server / Bases de Datos** | Valorable | 🟢 100% | Optimización de consultas y gestión de bases de datos en Craftelier con SSMS. |
| **Testing de APIs (pytest)** | Valorable | 🟢 95% | Pruebas unitarias y testing de endpoints en Python. |
| **Modalidad 100% Remoto** | Condición | 🟢 100% | Total disponibilidad desde España con espacio de trabajo acondicionado. |

---

## 2. Estrategia de Adaptación
- **Posicionamiento:** Presentar el perfil como un *Data & MLOps Engineer* con base de ingeniería de software sólida (DAW/DAM) que domina Python y el desarrollo de APIs robustas (FastAPI) junto con la gestión y despliegue de modelos y pipelines analíticos.
- **Enfoque de Experiencia:** Enfatizar la industrialización de flujos de datos en HORSE, la creación de endpoints y la formación superior en IA y Big Data donde se trabaja con MLflow y plataformas distribuidas.
""")

# 2. Carta de presentacion
with open(os.path.join(factum_dir, "carta_presentacion.md"), "w", encoding="utf-8") as f:
    f.write("""# CARTA DE PRESENTACIÓN — FACTUM IT

**Empresa:** Factum IT  
**Puesto:** Data Engineer / MLOps Engineer (100% Remoto)  
**Candidato:** Diego de la Fuente Alonso  
**Contacto:** diegodelafuentealonso@gmail.com | (+34) 626 68 71 79  

---

Estimado equipo de selección y tecnología de Factum IT,

Les escribo para presentar formalmente mi candidatura a la posición de **Data Engineer / MLOps Engineer** (100% Remoto). Cuento con una sólida trayectoria en el desarrollo backend con **Python y APIs RESTful (FastAPI)**, construcción de pipelines de datos automatizados y despliegue de soluciones de Inteligencia Artificial en entornos productivos, respaldada por mi **Curso de Especialización en Inteligencia Artificial y Big Data** y doble titulación en desarrollo de software (DAM / DAW).

A lo largo de mi trayectoria técnica:
- **Desarrollo Backend y APIs en Python:** En **HORSE Technologies** desarrollo servicios y herramientas internas de alto rendimiento con Python y Go, automatizando flujos de ingesta y transformación de datos para analítica corporativa. Además, he diseñado e implementado endpoints y microservicios RESTful con Python y Java (Spring Boot) en proyectos para administraciones públicas y empresas.
- **MLOps y Ciclo de Vida de Modelos:** En mi especialización superior en IA y Big Data y en mi trabajo actual he profundizado en el ciclo de vida de artefactos de Machine Learning, gobernanza de modelos con **MLflow**, observabilidad y estandarización de integraciones mediante el protocolo Model Context Protocol (MCP).
- **Ingeniería de Datos y Plataformas Cloud:** Experiencia práctica modelando y optimizando flujos de datos a escala sobre Google BigQuery y Dataform, así como gestión y optimización de bases de datos relacionales en **SQL Server** (SSMS).
- **DevOps y Calidad:** Trabajo diario con Git/GitHub, contenedores **Docker**, integración continua (CI/CD) y diseño modular probado con suites de testing (**pytest**).

La cultura de Factum IT de mejora continua, rigor técnico en proyectos de larga duración y compromiso con la innovación en entornos cloud encaja plenamente con mis aspiraciones profesionales. Cuento con total autonomía y disponibilidad inmediata para la modalidad 100% remota.

Agradezco de antemano su tiempo y consideración, y quedo a su entera disposición para mantener una entrevista técnica.

Atentamente,

**Diego de la Fuente Alonso**  
Data Engineer | MLOps & Backend Python  
diegodelafuentealonso@gmail.com | (+34) 626 68 71 79  
Valladolid, España (100% Remoto)  
[LinkedIn Profile](https://www.linkedin.com/in/) | [GitHub](https://github.com/)
""")

# 3. Respuestas formulario
with open(os.path.join(factum_dir, "respuestas_formulario.md"), "w", encoding="utf-8") as f:
    f.write("""# RESPUESTAS PARA FORMULARIO INFOJOBS — FACTUM IT

Utiliza estas respuestas optimizadas para responder a las preguntas que pueda plantear Factum IT al inscribirte en la oferta:

---

### 1. ¿Qué experiencia tienes en desarrollo con Python y creación de APIs con FastAPI?
> Cuento con más de 2 años de experiencia desarrollando soluciones backend y automatizaciones con Python. En HORSE Technologies desarrollo scripts de ingesta ETL, utilidades de alto rendimiento y servicios internos. He diseñado e implementado APIs RESTful modulares utilizando Python (FastAPI/Flask) y Java (Spring Boot), aplicando principios de clean code, validación de esquemas (Pydantic) y pruebas con pytest.

### 2. ¿Has trabajado con MLflow y gestión del ciclo de vida de modelos de Machine Learning (MLOps)?
> Sí. Durante el Curso de Especialización en Inteligencia Artificial y Big Data trabajé intensivamente con MLflow para el tracking de experimentos, registro y versionado de modelos. En HORSE Technologies aplico estos fundamentos al ciclo de vida e industrialización de soluciones inteligentes y agentes de IA, asegurando trazabilidad, reproducibilidad y despliegue productivo.

### 3. ¿Qué experiencia tienes en plataformas Cloud (Azure / GCP), Databricks o Big Data?
> Trabajo a diario en el ecosistema de datos cloud gestionando petabytes de información, optimizando consultas complejas y orquestando pipelines de transformación automatizados (BigQuery, Dataform). Cuento con formación en arquitecturas distribuidas (Spark/Databricks), contenedores Docker y optimización de bases de datos relacionales con SQL Server.

### 4. ¿Tienes disponibilidad para trabajar en modalidad 100% remota y cuál es tu plazo de incorporación?
> Total disponibilidad para modalidad 100% remota desde España, con espacio de trabajo propio y conexión de alta velocidad. Mi periodo de preaviso es el estándar de 15 días laborables.

### 5. Rango salarial orientativo:
> Acorde al nivel de la posición de Data Engineer / MLOps Engineer en Factum IT: 32.000 € – 38.000 € brutos/año (negociable en función del paquete de retribución flexible y beneficios).
""")

# 4. JSON Spec for ATS DOCX
cv_spec = {
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
        {"type": "paragraph", "style": "CVSubtitle", "text": "Data Engineer & MLOps | Python, FastAPI, Pipelines ETL & Arquitecturas ML"},
        {"type": "paragraph", "style": "CVContact", "text": "Valladolid / España (100% Remoto) | (+34) 626 68 71 79 | diegodelafuentealonso@gmail.com | LinkedIn | GitHub"},
        {"type": "paragraph", "style": "CVHeading", "text": "PERFIL PROFESIONAL"},
        {"type": "paragraph", "style": "CVBody", "text": "Ingeniero de datos y desarrollador backend con sólida experiencia en diseño e implementación de pipelines ETL/ELT automatizados en Python, desarrollo de APIs RESTful con FastAPI y despliegue de soluciones analíticas y modelos de Machine Learning. Experiencia en HORSE Technologies optimizando flujos de datos a gran escala, integrando sistemas agénticos mediante Model Context Protocol (MCP) y construyendo servicios de alto rendimiento en Python y Go. Formación técnica integral con doble titulación técnica en desarrollo de aplicaciones (DAM / DAW) y Especialización Superior en Inteligencia Artificial y Big Data (MLflow, arquitecturas distribuidas). Acostumbrado a entornos ágiles, pruebas unitarias automatizadas (pytest) y contenedores Docker."},
        {"type": "paragraph", "style": "CVHeading", "text": "COMPETENCIAS TÉCNICAS CLAVE"},
        {"type": "bullet_list", "items": [
            "Desarrollo Backend & APIs: Python (avanzado), desarrollo de servicios y APIs REST con FastAPI / Flask, testing automatizado con pytest, validación de datos con Pydantic, Go (Golang), Java (Spring Boot, microservicios).",
            "Data Engineering & Pipelines ETL: Construcción, orquestación y automatización de pipelines de datos en Python, modelado declarativo de transformaciones con Dataform, procesamiento analítico a gran escala.",
            "MLOps & Inteligencia Artificial: Gestión del ciclo de vida de modelos ML mediante MLflow (tracking, versionado, empaquetado y registro), despliegue de soluciones inteligentes en producción, interoperabilidad mediante Model Context Protocol (MCP).",
            "Bases de Datos & Cloud: SQL Server (SSMS, consultas complejas, optimización, procedimientos almacenados), Google BigQuery (optimización de queries, clustering, particionado), Azure SQL, diseño relacional y NoSQL.",
            "DevOps, Contenedores & Entornos: Docker, conceptos de Kubernetes / AKS, integración y despliegue continuo (CI/CD), Git / GitHub, observabilidad y monitorización, Linux."
        ]},
        {"type": "paragraph", "style": "CVHeading", "text": "EXPERIENCIA LABORAL"},
        {"type": "paragraph", "style": "CVJobHeader", "text": "HORSE Technologies — Data & Software / AI Developer"},
        {"type": "paragraph", "style": "CVJobDate", "text": "Valladolid | Julio 2026 – Actualidad"},
        {"type": "bullet_list", "items": [
            "Desarrollo y automatización de pipelines de datos y procesos ETL de extremo a extremo utilizando Python, garantizando la fiabilidad y calidad del dato analítico.",
            "Construcción de servicios backend y utilidades internas de alto rendimiento desarrolladas en Python y Go.",
            "Pionero en la industrialización de agentes de Inteligencia Artificial para automatización operativa, implementando agent harnesses, control de bucles de ejecución y protocolos estandarizados (MCP).",
            "Consulta, explotación y modelado de datos sobre petabytes en Google BigQuery y Dataform, aplicando técnicas de optimización de rendimiento y reducción de costes de computación.",
            "Diseño y publicación de modelos analíticos y dashboards de reporting en Looker para la toma de decisiones de negocio."
        ]},
        {"type": "paragraph", "style": "CVJobHeader", "text": "FDS, a DXC Technology Company — Consultor Técnico SAP"},
        {"type": "paragraph", "style": "CVJobDate", "text": "Febrero 2026 – Junio 2026"},
        {"type": "bullet_list", "items": [
            "Desarrollo y mantenimiento de personalizaciones de software y reportes en ABAP.",
            "Gestión, validación y despliegue de órdenes de transporte a través de entornos de desarrollo, pruebas y producción.",
            "Soporte técnico y análisis de procesos en el módulo de Logística de SAP en entorno multinacional."
        ]},
        {"type": "paragraph", "style": "CVJobHeader", "text": "Ayuntamiento de Roperuelos del Páramo — Desarrollador Backend & APIs"},
        {"type": "paragraph", "style": "CVJobDate", "text": "Junio 2024 – Octubre 2024 | Junio 2023 – Septiembre 2023"},
        {"type": "bullet_list", "items": [
            "Diseño e implementación de servicios backend y APIs REST en Python para la automatización de la tramitación de expedientes y gestión de datos.",
            "Desarrollo de aplicaciones web y microservicios robustos utilizando Java con Spring Boot.",
            "Diseño de modelos relacionales de bases de datos y optimización de consultas SQL."
        ]},
        {"type": "paragraph", "style": "CVJobHeader", "text": "Craftelier — Desarrollador de Software & Bases de Datos"},
        {"type": "paragraph", "style": "CVJobDate", "text": "Marzo 2024 – Mayo 2024"},
        {"type": "bullet_list", "items": [
            "Consultas avanzadas, optimización de rendimiento y mantenimiento de bases de datos en SQL Server mediante SQL Server Management Studio (SSMS).",
            "Desarrollo y evolución de aplicaciones de escritorio empresariales bajo plataforma .NET / C# en Visual Studio.",
            "Desarrollo de módulos para aplicaciones móviles Android en Kotlin."
        ]},
        {"type": "paragraph", "style": "CVHeading", "text": "FORMACIÓN ACADÉMICA"},
        {"type": "bullet_list", "items": [
            "Curso de Especialización en Inteligencia Artificial y Big Data (2024 – 2025) — Ciclo de vida de modelos ML (MLflow), arquitecturas de datos distribuidas y procesamiento masivo.",
            "Técnico Superior en Desarrollo de Aplicaciones Web (DAW) — IES San Andrés (2025 – 2026).",
            "Técnico Superior en Desarrollo de Aplicaciones Multiplataforma (DAM) — IES San Andrés (2022 – 2024)."
        ]},
        {"type": "paragraph", "style": "CVHeading", "text": "IDIOMAS"},
        {"type": "bullet_list", "items": [
            "Español: Nativo.",
            "Inglés: Nivel B1 técnico (Capacidad demostrada para lectura de documentación técnica, especificaciones de arquitectura y comunicación escrita)."
        ]}
    ]
}

spec_path = os.path.join(factum_dir, "cv_spec.json")
with open(spec_path, "w", encoding="utf-8") as f:
    json.dump(cv_spec, f, indent=2, ensure_ascii=False)

docx_out = os.path.join(factum_dir, "cv_adaptado_diego_de_la_fuente.docx")
subprocess.run(["uv", "run", "--with", "python-docx", "python", DOCX_CREATE, spec_path, docx_out], check=True)
subprocess.run(["uv", "run", "--with", "python-docx", "python", DOCX_VAL, docx_out], check=True)

print("Factum IT customized package generated and validated successfully.")
