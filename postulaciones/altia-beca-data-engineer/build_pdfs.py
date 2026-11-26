import json
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable

styles = getSampleStyleSheet()

# 1. Generate the 1-page CV PDF with fully justified text (TA_JUSTIFY)
with open("C:/Users/DELAFUENTEALONSODieg/empleo/postulaciones/altia-beca-data-engineer/cv_spec.json", "r", encoding="utf-8") as f:
    spec = json.load(f)

cv_pdf_path = "C:/Users/DELAFUENTEALONSODieg/empleo/postulaciones/altia-beca-data-engineer/Diego_de_la_Fuente_Alonso_CV_Altia_Beca_Data_Engineer.pdf"
cv_doc = SimpleDocTemplate(
    cv_pdf_path,
    pagesize=A4,
    leftMargin=16*mm,
    rightMargin=16*mm,
    topMargin=13*mm,
    bottomMargin=13*mm,
    title="CV - Diego de la Fuente Alonso - Data Engineer IA-First (Altia)",
    author="Diego de la Fuente Alonso"
)

s_title = ParagraphStyle("CVT", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=16, leading=19, textColor=colors.HexColor("#111827"), spaceAfter=2)
s_sub = ParagraphStyle("CVS", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=9.2, leading=12.2, textColor=colors.HexColor("#1F2937"), spaceAfter=2)
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
cl_path = "C:/Users/DELAFUENTEALONSODieg/empleo/postulaciones/altia-beca-data-engineer/Diego_de_la_Fuente_Alonso_Carta_Presentacion_Altia_Beca_Data_Engineer.pdf"
cl_doc = SimpleDocTemplate(
    cl_path,
    pagesize=A4,
    leftMargin=22*mm,
    rightMargin=22*mm,
    topMargin=18*mm,
    bottomMargin=18*mm,
    title="Carta de Presentación - Diego de la Fuente Alonso - Altia Beca Data Engineer",
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
    Paragraph("Data Engineer IA-First (Junior / Early Career) | Python · SQL · DAX · ETL · dbt/Dataform · Power BI · CI/CD", role_style),
    Paragraph("Madrid / Valladolid (Híbrido / Teletrabajo)  |  (+34) 626 68 71 79  |  diegodelafuentealonso@gmail.com", contact_style),
    HRFlowable(width="100%", thickness=0.8, color=colors.HexColor("#D1D5DB"), spaceBefore=2, spaceAfter=12),
    Paragraph("3 de noviembre de 2026", meta_style),
    Paragraph("Para: Equipo de Selección y Área de Data &amp; Analytics — Altia", meta_style),
    Paragraph("Asunto: Candidatura a Beca Data Engineer (Ingeniería de Datos IA-First)", subject_style),
    Paragraph("Estimado equipo de Selección de Altia,", body_style),
    Paragraph(
        "Les escribo para presentar mi candidatura a la posición de Beca Data Engineer para sus equipos de Data &amp; Analytics. Me entusiasma especialmente el "
        "enfoque de este programa para formar ingenieros de datos IA-First, ya que une exactamente las dos áreas en las que me he especializado y trabajo a "
        "diario: la ingeniería de datos moderna (Python, SQL, ETL, modelado de datos, dbt/Dataform y Power BI) y el uso intensivo de herramientas de "
        "Inteligencia Artificial Generativa para construir y optimizar código.",
        body_style
    ),
    Paragraph(
        "Mi perfil encaja punto por punto con los requisitos técnicos del programa:",
        body_style
    ),
    Paragraph(
        "• Ingeniería de datos IA-First y herramientas de desarrollo: Utilizo a diario en VS Code herramientas de IA Generativa (modelos LLM, asistentes de "
        "código y protocolo MCP) para acelerar el desarrollo de pipelines, generar tests de calidad y optimizar consultas, integrando todo el flujo mediante "
        "control de versiones y pipelines CI/CD.",
        bullet_style
    ),
    Paragraph(
        "• Dominio de Python, SQL, DAX y transformación con dbt / Dataform: Tengo experiencia práctica diseñando procesos ETL/ELT, modelado dimensional de "
        "datos y transformaciones modulares con Dataform y dbt, trabajando con Python y SQL avanzado sobre plataformas cloud y relacionales.",
        bullet_style
    ),
    Paragraph(
        "• Reporting con Microsoft Power BI y plataformas Lakehouse (Fabric / Databricks): Cuento con formación específica en el Curso de Especialización en "
        "Inteligencia Artificial y Big Data y experiencia práctica creando modelos tabulares, medidas en DAX y cuadros de mando en Power BI Desktop, Looker "
        "y entornos Databricks / Microsoft Fabric.",
        bullet_style
    ),
    Spacer(1, 2),
    Paragraph(
        "Tengo total disponibilidad para incorporarme al programa formativo inicial y evolucionar a largo plazo dentro de los proyectos de Data &amp; Analytics "
        "de Altia. Agradezco de antemano su tiempo y consideración, y quedo a su entera disposición para mantener una entrevista.",
        body_style
    ),
    Paragraph(
        "Atentamente,<br/><br/>"
        "Diego de la Fuente Alonso<br/>"
        "Data Engineer IA-First (Python / SQL / DAX / ETL / dbt / Power BI)<br/>"
        "(+34) 626 68 71 79  |  diegodelafuentealonso@gmail.com",
        sign_style
    )
]

cl_doc.build(cl_story)
print("Created Cover Letter PDF:", cl_path)
