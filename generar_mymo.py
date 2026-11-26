#!/usr/bin/env python3
import os
import json
import subprocess

BASE_DIR = r"C:\Users\DELAFUENTEALONSODieg\empleo\postulaciones"
DOCX_CREATE = r"C:\Users\DELAFUENTEALONSODieg\AppData\Local\hermes\skills\productivity\docx\scripts\docx_create.py"
DOCX_VAL = r"C:\Users\DELAFUENTEALONSODieg\AppData\Local\hermes\skills\productivity\docx\scripts\docx_validate.py"

mymo_dir = os.path.join(BASE_DIR, "mymo-backend-agentes")
os.makedirs(mymo_dir, exist_ok=True)

with open(os.path.join(mymo_dir, "oferta_analizada.md"), "w", encoding="utf-8") as f:
    f.write("""# ANÁLISIS DE OFERTA — PRESCRIPCIÓN MÉDICA UNIVERSAL (MyMO)

**Puesto:** Desarrollador/a Backend & IA (Orquestación de Agentes)  
**Empresa:** Prescripción Médica Universal SL (Plataforma MyMO - My Medical Order)  
**Modalidad:** 100% Remoto (Solo teletrabajo desde España)  
**Salario:** 30.000 € – 40.000 € Bruto/año (1.800€ - 2.200€ netos/mes + revisión a los 6 meses)  
**Vacantes:** 3 vacantes activas | Contrato Indefinido  
**Web de la empresa:** [discovermymedicalorder.es](https://discovermymedicalorder.es/)  
**Email corporativo:** infospain@mymedicalorder.com  
**Encaje estimado:** 98% (Match sobresaliente)

---

## 1. Misión del Puesto
Liderar la orquestación del cerebro de MyMO: un ecosistema de **19 agentes de IA** (6 C-Suite + 13 operativos) sobre **Claude API o similar**.
- Diseñar e implementar flujos de decisión y control: «agente propone -> humano aprueba -> ejecución con log de auditoría inmutable» (Loop Engineering / Human-in-the-loop).
- Conectar mediante backend REST la app, los agentes y el hardware.
- Stack: Python, C#/.NET, APIs de LLMs (Claude/OpenAI), arquitecturas de agentes, logs de auditoría inmutables.

## 2. Por qué encaja Diego de forma casi artesanal:
1. **Arquitecturas de Agentes y Loop Engineering:** Es exactamente lo que Diego implementa en HORSE Technologies (agent harnesses, control de bucles de razonamiento, integración mediante MCP).
2. **Backend Python & C# / .NET:** Combina desarrollo diario en Python con su experiencia profesional previa en .NET / C# en Craftelier.
3. **Inglés técnico:** Cumple el requisito de lectura fluida de documentación técnica.
""")

with open(os.path.join(mymo_dir, "carta_presentacion.md"), "w", encoding="utf-8") as f:
    f.write("""# CARTA DE PRESENTACIÓN — MyMO (Prescripción Médica Universal)

**Destinatario:** Coordinador de Proyecto & Equipo Técnico  
**Empresa:** Prescripción Médica Universal SL (MyMO)  
**Puesto:** Desarrollador/a Backend & IA (Orquestación de Agentes) — 100% Remoto  
**Candidato:** Diego de la Fuente Alonso  
**Email:** diegodelafuentealonso@gmail.com | (+34) 626 68 71 79  

---

Estimado equipo de MyMO y Prescripción Médica Universal,

Les escribo para presentar con gran entusiasmo mi candidatura a la posición de **Desarrollador/a Backend & IA (Orquestación de Agentes)** en modalidad 100% remota. Su proyecto me ha llamado profundamente la atención: la creación de un sistema de 19 agentes coordinados bajo el principio de «agente propone -> humano aprueba -> ejecución auditada» representa exactamente el tipo de arquitectura en la que trabajo a diario.

En mi posición actual en **HORSE Technologies**:
- **Ingeniería de Agentes & Loop Engineering:** Diseño e implemento soluciones basadas en agentes autónomos de Inteligencia Artificial utilizando Python y Go, aplicando arquitecturas de *agent harness*, control estricto de bucles de razonamiento e integración segura de herramientas mediante el protocolo **Model Context Protocol (MCP)**.
- **Modelos y APIs de LLMs:** Trabajo habitualmente con las APIs de vanguardia (**Claude / Anthropic**, OpenAI y Gemini), gestionando llamadas a funciones estructuradas, prompting contextual y control de estados.
- **Backend y experiencia en .NET / C#:** Además de construir microservicios y APIs REST en Python y Java, cuento con experiencia previa en desarrollo de software bajo el ecosistema **.NET y C#** (en Craftelier), lo que me permite comprender de inmediato la arquitectura de su aplicación y colaborar con fluidez en la integración entre la app y los agentes.
- **Formación técnica integral:** Especialización Superior en Inteligencia Artificial y Big Data, complementada con doble titulación técnica en desarrollo de aplicaciones (DAM y DAW).

Cuento con plena autonomía para el trabajo 100% remoto, comunicación proactiva y el nivel de inglés técnico requerido para documentación y especificaciones.

Me encantaría tener la oportunidad de conversar con el coordinador del proyecto y mostrarles cómo mis desarrollos en orquestación de agentes pueden aportar valor inmediato a la expansión de MyMO.

Atentamente,

**Diego de la Fuente Alonso**  
diegodelafuentealonso@gmail.com | (+34) 626 68 71 79  
Valladolid, España (100% Remoto)  
""")

spec = {
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
        {"type": "paragraph", "style": "CVSubtitle", "text": "Backend & AI Agent Engineer | Loop Engineering, Agent Harness & LLM APIs"},
        {"type": "paragraph", "style": "CVContact", "text": "Valladolid / España (100% Remoto) | (+34) 626 68 71 79 | diegodelafuentealonso@gmail.com | LinkedIn | GitHub"},
        {"type": "paragraph", "style": "CVHeading", "text": "PERFIL PROFESIONAL"},
        {"type": "paragraph", "style": "CVBody", "text": "Ingeniero de software especializado en el diseño, desarrollo y orquestación de sistemas basados en agentes autónomos de Inteligencia Artificial y APIs de LLMs (Claude, OpenAI, Gemini). Experiencia práctica en HORSE Technologies construyendo agent harnesses, flujos de control de razonamiento (loop engineering, human-in-the-loop) e integración de herramientas mediante Model Context Protocol (MCP). Sólida formación con doble grado superior en DAM/DAW y Especialización en Inteligencia Artificial y Big Data. Dominio técnico de backend en Python y Go, junto con experiencia profesional previa en el ecosistema .NET / C# y bases de datos relacionales."},
        {"type": "paragraph", "style": "CVHeading", "text": "COMPETENCIAS TÉCNICAS CLAVE"},
        {"type": "bullet_list", "items": [
            "Sistemas Agénticos & Orquestación: Diseño de ecosistemas multi-agente, arquitecturas agent harness, loop engineering, patrones human-in-the-loop (propuesta, validación y auditoría), control de estados y memoria.",
            "APIs de Modelos LLM & Protocolos: Integración avanzada de Claude API (Anthropic), OpenAI y Gemini, tool calling estructurado, Model Context Protocol (MCP), validación de salidas.",
            "Desarrollo Backend & Lenguajes: Python (avanzado, APIs RESTful, frameworks de automatización), Go (Golang), .NET / C# (desarrollo previo en Craftelier), Java (Spring Boot), microservicios.",
            "Bases de Datos & Persistencia: SQL Server (SSMS, consultas complejas, integridad relacional), BigQuery, diseño de esquemas para trazabilidad y logs de auditoría.",
            "Entornos & Metodologías: Git / GitHub, Docker, APIs RESTful seguras, trabajo en remoto con comunicación proactiva y autonomía técnica."
        ]},
        {"type": "paragraph", "style": "CVHeading", "text": "EXPERIENCIA LABORAL"},
        {"type": "paragraph", "style": "CVJobHeader", "text": "HORSE Technologies — Data & Software / AI Developer"},
        {"type": "paragraph", "style": "CVJobDate", "text": "Valladolid | Julio 2026 – Actualidad"},
        {"type": "bullet_list", "items": [
            "Diseño, desarrollo y despliegue de soluciones basadas en agentes de Inteligencia Artificial para la automatización de procesos técnicos corporativos.",
            "Implementación de agent harnesses y bucles de razonamiento (loop engineering) con supervisión humana y registro de acciones.",
            "Integración de agentes con herramientas y sistemas de información utilizando el estándar Model Context Protocol (MCP).",
            "Desarrollo de servicios backend y utilidades internas de alto rendimiento con Python y Go.",
            "Automatización de pipelines ETL y consultas analíticas a gran escala sobre Google BigQuery."
        ]},
        {"type": "paragraph", "style": "CVJobHeader", "text": "Craftelier — Desarrollador de Software (.NET / C#) & SQL Server"},
        {"type": "paragraph", "style": "CVJobDate", "text": "Marzo 2024 – Mayo 2024"},
        {"type": "bullet_list", "items": [
            "Desarrollo y evolución de aplicaciones empresariales utilizando el ecosistema .NET y C# en Visual Studio.",
            "Consultas avanzadas, optimización de procedimientos y modelado relacional en SQL Server (SSMS).",
            "Desarrollo de módulos móviles en Android con Kotlin."
        ]},
        {"type": "paragraph", "style": "CVJobHeader", "text": "Ayuntamiento de Roperuelos del Páramo — Desarrollador Backend & APIs REST"},
        {"type": "paragraph", "style": "CVJobDate", "text": "Junio 2024 – Octubre 2024 | Junio 2023 – Septiembre 2023"},
        {"type": "bullet_list", "items": [
            "Desarrollo de endpoints y servicios backend de APIs REST en Python para gestión y tramitación de datos.",
            "Construcción de aplicaciones web administrativas y microservicios con Java y Spring Boot."
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
            "Inglés: Nivel B1 técnico (Capacidad para lectura fluida de documentación de APIs, especificaciones de arquitectura y comunicación escrita)."
        ]}
    ]
}

spec_path = os.path.join(mymo_dir, "cv_spec.json")
with open(spec_path, "w", encoding="utf-8") as f:
    json.dump(spec, f, indent=2, ensure_ascii=False)

docx_out = os.path.join(mymo_dir, "cv_adaptado_diego_de_la_fuente.docx")
subprocess.run(["uv", "run", "--with", "python-docx", "python", DOCX_CREATE, spec_path, docx_out], check=True)
subprocess.run(["uv", "run", "--with", "python-docx", "python", DOCX_VAL, docx_out], check=True)

print("Generated and validated MyMO package successfully.")
