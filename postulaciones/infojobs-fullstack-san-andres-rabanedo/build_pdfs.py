import json
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable

styles = getSampleStyleSheet()

# 1. Generate the 1-page CV PDF with fully justified text (TA_JUSTIFY)
with open("C:/Users/DELAFUENTEALONSODieg/empleo/postulaciones/infojobs-fullstack-san-andres-rabanedo/cv_spec.json", "r", encoding="utf-8") as f:
    spec = json.load(f)

cv_pdf_path = "C:/Users/DELAFUENTEALONSODieg/empleo/postulaciones/infojobs-fullstack-san-andres-rabanedo/Diego_de_la_Fuente_Alonso_CV_FullStack_Automatizacion.pdf"
cv_doc = SimpleDocTemplate(
    cv_pdf_path,
    pagesize=A4,
    leftMargin=16*mm,
    rightMargin=16*mm,
    topMargin=13*mm,
    bottomMargin=13*mm,
    title="CV - Diego de la Fuente Alonso - Desarrollador Full Stack & Automatizaciones",
    author="Diego de la Fuente Alonso"
)

s_title = ParagraphStyle("CVT", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=16, leading=19, textColor=colors.HexColor("#111827"), spaceAfter=2)
s_sub = ParagraphStyle("CVS", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=9.1, leading=12.1, textColor=colors.HexColor("#1F2937"), spaceAfter=2)
s_con = ParagraphStyle("CVC", parent=styles["Normal"], fontName="Helvetica", fontSize=8.8, leading=11.5, textColor=colors.HexColor("#4B5563"), spaceAfter=6)
s_head = ParagraphStyle("CVH", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=10, leading=13, textColor=colors.HexColor("#111827"), spaceBefore=5.2, spaceAfter=2.2)
s_job = ParagraphStyle("CVJ", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=9.2, leading=12, textColor=colors.HexColor("#111827"), spaceBefore=3.5, spaceAfter=1)
s_date = ParagraphStyle("CVD", parent=styles["Normal"], fontName="Helvetica-Oblique", fontSize=8.5, leading=11, textColor=colors.HexColor("#4B5563"), spaceAfter=2)
s_body = ParagraphStyle("CVB", parent=styles["Normal"], fontName="Helvetica", fontSize=8.7, leading=11.8, alignment=TA_JUSTIFY, textColor=colors.HexColor("#1F2937"), spaceAfter=3.2)
s_bul = ParagraphStyle("CVBul", parent=styles["Normal"], fontName="Helvetica", fontSize=8.6, leading=11.5, alignment=TA_JUSTIFY, leftIndent=10, firstLineIndent=-6, textColor=colors.HexColor("#1F2937"), spaceAfter=2)

cv_story = []
for b in spec["blocks"]:
    if b["type"] == "paragraph":
        st_name = b["style"]
        txt = b["text"].replace("&", "&amp;")
        if st_name == "CVTitle":
            cv_story.append(Paragraph(txt, s_title))
        elif st_name == "CVSubtitle":
            cv_story.append(Paragraph(txt, s_sub))
        elif st_name == "CVContact":
            cv_story.append(Paragraph(txt, s_con))
            cv_story.append(HRFlowable(width="100%", thickness=0.6, color=colors.HexColor("#D1D5DB"), spaceBefore=1, spaceAfter=4))
        elif st_name == "CVHeading":
            cv_story.append(Paragraph(txt, s_head))
        elif st_name == "CVJobHeader":
            cv_story.append(Paragraph(txt, s_job))
        elif st_name == "CVJobDate":
            cv_story.append(Paragraph(txt, s_date))
        else:
            cv_story.append(Paragraph(txt, s_body))
    elif b["type"] == "bullet_list":
        for it in b["items"]:
            cv_story.append(Paragraph("• " + it.replace("&", "&amp;"), s_bul))

cv_doc.build(cv_story)
print("Created CV PDF:", cv_pdf_path)

# 2. Generate the Cover Letter PDF (justified, no bold in body)
cl_path = "C:/Users/DELAFUENTEALONSODieg/empleo/postulaciones/infojobs-fullstack-san-andres-rabanedo/Diego_de_la_Fuente_Alonso_Carta_Presentacion_FullStack_Automatizacion.pdf"
cl_doc = SimpleDocTemplate(
    cl_path,
    pagesize=A4,
    leftMargin=22*mm,
    rightMargin=22*mm,
    topMargin=18*mm,
    bottomMargin=18*mm,
    title="Carta de Presentación - Diego de la Fuente Alonso - Desarrollador Full Stack",
    author="Diego de la Fuente Alonso"
)

name_style = ParagraphStyle("NameHeader", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=16, leading=20, textColor=colors.HexColor("#111827"), spaceAfter=2)
role_style = ParagraphStyle("RoleHeader", parent=styles["Normal"], fontName="Helvetica", fontSize=9.5, leading=13.2, textColor=colors.HexColor("#1F2937"), spaceAfter=3)
contact_style = ParagraphStyle("ContactHeader", parent=styles["Normal"], fontName="Helvetica", fontSize=9.5, leading=13, textColor=colors.HexColor("#4B5563"), spaceAfter=8)
meta_style = ParagraphStyle("MetaText", parent=styles["Normal"], fontName="Helvetica", fontSize=9.8, leading=13.5, textColor=colors.HexColor("#1F2937"), spaceAfter=5)
subject_style = ParagraphStyle("SubjectText", parent=styles["Normal"], fontName="Helvetica", fontSize=10, leading=14.5, textColor=colors.HexColor("#111827"), spaceBefore=4, spaceAfter=10)
body_style = ParagraphStyle("BodyJustified", parent=styles["Normal"], fontName="Helvetica", fontSize=9.8, leading=14.3, alignment=TA_JUSTIFY, textColor=colors.HexColor("#1F2937"), spaceAfter=8)
bullet_style = ParagraphStyle("BulletItem", parent=styles["Normal"], fontName="Helvetica", fontSize=9.6, leading=13.7, alignment=TA_JUSTIFY, leftIndent=12, firstLineIndent=-8, textColor=colors.HexColor("#1F2937"), spaceAfter=5.5)
sign_style = ParagraphStyle("Signature", parent=styles["Normal"], fontName="Helvetica", fontSize=9.8, leading=13.5, textColor=colors.HexColor("#111827"), spaceBefore=8)

cl_story = [
    Paragraph("DIEGO DE LA FUENTE ALONSO", name_style),
    Paragraph("Desarrollador Full Stack &amp; Especialista en Automatizaciones | React/Next.js · APIs REST · Webhooks · n8n · PostgreSQL/MySQL", role_style),
    Paragraph("San Andrés del Rabanedo (León) / Valladolid  |  (+34) 626 68 71 79  |  diegodelafuentealonso@gmail.com", contact_style),
    HRFlowable(width="100%", thickness=0.8, color=colors.HexColor("#D1D5DB"), spaceBefore=2, spaceAfter=12),
    Paragraph("3 de noviembre de 2026", meta_style),
    Paragraph("Para: Equipo de Selección — Vacante de Desarrollador/a Full Stack (San Andrés del Rabanedo)", meta_style),
    Paragraph("Asunto: Candidatura a Desarrollador/a Full Stack (React/Next.js, SQL, APIs REST y Automatizaciones)", subject_style),
    Paragraph("Estimado equipo de Selección,", body_style),
    Paragraph(
        "Les escribo para presentar mi candidatura a la posición de Desarrollador/a Full Stack en San Andrés del Rabanedo publicada en InfoJobs. Cuento con una "
        "vinculación directa con el municipio —donde cursé mis dos titulaciones de Grado Superior en Desarrollo de Aplicaciones Web (DAW) y Multiplataforma (DAM) "
        "en el IES San Andrés y donde trabajé como desarrollador en Craftelier—, además de experiencia profesional desarrollando aplicaciones web, gestionando bases "
        "de datos SQL (PostgreSQL, MySQL y SQL Server) y desplegando integraciones y automatizaciones reales en producción.",
        body_style
    ),
    Paragraph(
        "Mi perfil responde de forma directa a los cuatro pilares técnicos que plantean en su proceso de selección:",
        body_style
    ),
    Paragraph(
        "• Desarrollo de aplicaciones web reales (React, Next.js y Full Stack): He construido interfaces y aplicaciones completas combinando componentes frontend "
        "modernos (React, Next.js, JavaScript/TypeScript) con servicios backend robustos en Python, Java (Spring Boot) y .NET.",
        bullet_style
    ),
    Paragraph(
        "• Experiencia profesional con SQL, PostgreSQL y MySQL: Trabajo a diario escribiendo consultas SQL avanzadas, diseñando esquemas relacionales y conectando "
        "aplicaciones directamente a motores PostgreSQL, MySQL, Microsoft SQL Server y BigQuery.",
        bullet_style
    ),
    Paragraph(
        "• Integración de sistemas mediante APIs REST, Webhooks y flujos tipo n8n/Zapier: En mi puesto actual en HORSE Technologies y en mis etapas previas en el "
        "Ayuntamiento de Roperuelos del Páramo y Craftelier, he conectado aplicaciones, servicios cloud y bases de datos mediante APIs RESTful, Webhooks, protocolo "
        "MCP y flujos de orquestación automatizados.",
        bullet_style
    ),
    Paragraph(
        "• Automatizaciones funcionando en producción de principio a fin: Estoy habituado a tomar un problema operativo manual, diseñar la arquitectura de "
        "integración end-to-end, programarla, probarla y dejarla funcionando de forma autónoma y monitorizada en producción en plazos cortos.",
        bullet_style
    ),
    Spacer(1, 2),
    Paragraph(
        "Agradezco de antemano su tiempo y consideración. Quedo a su entera disposición para mantener una entrevista y mostrarles ejemplos concretos de las "
        "integraciones y aplicaciones que he puesto en marcha.",
        body_style
    ),
    Paragraph(
        "Atentamente,<br/><br/>"
        "Diego de la Fuente Alonso<br/>"
        "Desarrollador Full Stack &amp; Especialista en Integraciones y Automatización<br/>"
        "(+34) 626 68 71 79  |  diegodelafuentealonso@gmail.com",
        sign_style
    )
]

cl_doc.build(cl_story)
print("Created Cover Letter PDF:", cl_path)
