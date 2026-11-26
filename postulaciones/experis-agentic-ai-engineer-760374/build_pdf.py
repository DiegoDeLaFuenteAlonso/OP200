from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable

out_path = "C:/Users/DELAFUENTEALONSODieg/empleo/postulaciones/experis-agentic-ai-engineer-760374/Diego_de_la_Fuente_Alonso_Carta_Presentacion_Experis_Conjunta.pdf"

doc = SimpleDocTemplate(
    out_path,
    pagesize=A4,
    leftMargin=22*mm,
    rightMargin=22*mm,
    topMargin=18*mm,
    bottomMargin=18*mm,
    title="Carta de Presentación Conjunta - Diego de la Fuente Alonso - Experis (Refs. 760374 y 757310)",
    author="Diego de la Fuente Alonso"
)

styles = getSampleStyleSheet()

name_style = ParagraphStyle("NameHeader", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=16, leading=20, textColor=colors.HexColor("#111827"), spaceAfter=2)
role_style = ParagraphStyle("RoleHeader", parent=styles["Normal"], fontName="Helvetica", fontSize=10, leading=13.5, textColor=colors.HexColor("#1F2937"), spaceAfter=3)
contact_style = ParagraphStyle("ContactHeader", parent=styles["Normal"], fontName="Helvetica", fontSize=9.5, leading=13, textColor=colors.HexColor("#4B5563"), spaceAfter=8)
meta_style = ParagraphStyle("MetaText", parent=styles["Normal"], fontName="Helvetica", fontSize=9.8, leading=13.5, textColor=colors.HexColor("#1F2937"), spaceAfter=5)
subject_style = ParagraphStyle("SubjectText", parent=styles["Normal"], fontName="Helvetica", fontSize=10, leading=14.5, textColor=colors.HexColor("#111827"), spaceBefore=4, spaceAfter=10)
body_style = ParagraphStyle("BodyJustified", parent=styles["Normal"], fontName="Helvetica", fontSize=9.8, leading=14.5, alignment=TA_JUSTIFY, textColor=colors.HexColor("#1F2937"), spaceAfter=8)
bullet_style = ParagraphStyle("BulletItem", parent=styles["Normal"], fontName="Helvetica", fontSize=9.6, leading=14, alignment=TA_JUSTIFY, leftIndent=12, firstLineIndent=-8, textColor=colors.HexColor("#1F2937"), spaceAfter=5.5)
sign_style = ParagraphStyle("Signature", parent=styles["Normal"], fontName="Helvetica", fontSize=9.8, leading=13.5, textColor=colors.HexColor("#111827"), spaceBefore=8)

story = [
    Paragraph("DIEGO DE LA FUENTE ALONSO", name_style),
    Paragraph("AI Developer &amp; Agentic AI Specialist (GCP) | Python · LangGraph/LangChain · Gemini · BigQuery · MCP · APIs REST", role_style),
    Paragraph("España (100% Remoto / Valladolid - Madrid)  |  (+34) 626 68 71 79  |  diegodelafuentealonso@gmail.com", contact_style),
    HRFlowable(width="100%", thickness=0.8, color=colors.HexColor("#D1D5DB"), spaceBefore=2, spaceAfter=12),
    Paragraph("3 de noviembre de 2026", meta_style),
    Paragraph("Para: Equipo de Selección IT e Innovación — Experis España", meta_style),
    Paragraph("Asunto: Candidatura conjunta a AI Developer / Agentic AI Engineer (Ref. 760374) y Especialista en IA Generativa – Agentes Multimodales sobre GCP (Ref. 757310)", subject_style),
    Paragraph("Estimado equipo de Selección IT e Innovación de Experis España,", body_style),
    Paragraph(
        "Les escribo para presentar mi candidatura a las dos posiciones de Inteligencia Artificial Generativa y Sistemas de Agentes en modalidad 100% remota "
        "que tienen actualmente abiertas: AI Developer / Agentic AI Engineer (Ref. 760374) y Especialista en IA Generativa – Agentes Multimodales sobre GCP "
        "(Ref. 757310). Mi experiencia técnica actual une exactamente ambos perfiles, ya que desarrollo sistemas de agentes e integraciones backend en Python "
        "directamente conectados con Google Cloud Platform (GCP) y Google BigQuery.",
        body_style
    ),
    Paragraph(
        "En mi puesto actual en HORSE Technologies, mi trabajo diario en producción abarca de forma integral los requisitos técnicos de ambas vacantes:",
        body_style
    ),
    Paragraph(
        "• Desarrollo de agentes, orquestadores y flujos con estado (LangGraph / LangChain y Gemini): Diseño, desarrollo y evoluciono agentes inteligentes "
        "y sistemas multiagente en Python y Go utilizando Google Gemini, Claude y OpenAI. Defino instrucciones, herramientas (tools), workflows y gestión "
        "de estado (mediante arquitecturas agent harness y loop engineering equivalentes a LangGraph) capaces de procesar tanto datos estructurados como "
        "documentación técnica.",
        bullet_style
    ),
    Paragraph(
        "• Ecosistema Google Cloud Platform (GCP), BigQuery y validación automatizada: Integro directamente los agentes y pipelines ETL/ELT con Google BigQuery "
        "y Dataform sobre GCP. Diseño flujos que cruzan múltiples fuentes de datos y documentación para automatizar validaciones de calidad y generar informes "
        "de discrepancias y cuadros de mando en Looker.",
        bullet_style
    ),
    Paragraph(
        "• Model Context Protocol (MCP), APIs REST y microservicios: Implemento servidores y conectores bajo el estándar Model Context Protocol (MCP) "
        "para conectar de forma segura y modular los agentes de IA con APIs REST, microservicios y bases de datos corporativas, aplicando buenas prácticas "
        "de Arquitectura Hexagonal, Domain-Driven Design (DDD), control de versiones con Git y despliegues en Cloud.",
        bullet_style
    ),
    Paragraph(
        "• Lógica determinista, evaluación de LLMs y observabilidad: Combino las capacidades de la IA generativa con reglas de negocio deterministas "
        "para asegurar la consistencia de los procesos, realizando una evaluación y optimización continua de los modelos mediante prompt engineering "
        "y el análisis de logs, trazas y métricas de rendimiento.",
        bullet_style
    ),
    Spacer(1, 2),
    Paragraph(
        "Asimismo, cuento con el Curso de Especialización en Inteligencia Artificial y Big Data (donde también he trabajado técnicas de visión artificial, "
        "análisis de imágenes y evaluación de modelos) y con la doble titulación superior en Desarrollo de Aplicaciones Multiplataforma (DAM) y Web (DAW).",
        body_style
    ),
    Paragraph(
        "Resido en España con disponibilidad total para modalidad 100% remota y un preaviso de incorporación de 15 días naturales.",
        body_style
    ),
    Paragraph(
        "Agradezco de antemano su tiempo y consideración. Quedo a su entera disposición para mantener una entrevista y valorar en cuál de los dos proyectos "
        "(Ref. 760374 o Ref. 757310) o en ambos puedo aportar mayor impacto inmediato.",
        body_style
    ),
    Paragraph(
        "Atentamente,<br/><br/>"
        "Diego de la Fuente Alonso<br/>"
        "AI Developer &amp; Agentic AI Specialist (Python / GCP / BigQuery / MCP)<br/>"
        "(+34) 626 68 71 79  |  diegodelafuentealonso@gmail.com",
        sign_style
    )
]

doc.build(story)
print("Joint PDF created:", out_path)
