import json
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable

styles = getSampleStyleSheet()

# 1. Generate the 1-page CV PDF with fully justified text (TA_JUSTIFY)
with open("C:/Users/DELAFUENTEALONSODieg/empleo/postulaciones/mc-engineering-data-analyst/cv_spec.json", "r", encoding="utf-8") as f:
    spec = json.load(f)

cv_pdf_path = "C:/Users/DELAFUENTEALONSODieg/empleo/postulaciones/mc-engineering-data-analyst/Diego_de_la_Fuente_Alonso_CV_MCEng_Data_Analyst.pdf"
cv_doc = SimpleDocTemplate(
    cv_pdf_path,
    pagesize=A4,
    leftMargin=16*mm,
    rightMargin=16*mm,
    topMargin=13*mm,
    bottomMargin=13*mm,
    title="CV - Diego de la Fuente Alonso - Data Analyst (MCEng España)",
    author="Diego de la Fuente Alonso"
)

s_title = ParagraphStyle("CVT", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=16, leading=19, textColor=colors.HexColor("#111827"), spaceAfter=2)
s_sub = ParagraphStyle("CVS", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=9.4, leading=12.4, textColor=colors.HexColor("#1F2937"), spaceAfter=2)
s_con = ParagraphStyle("CVC", parent=styles["Normal"], fontName="Helvetica", fontSize=8.8, leading=11.5, textColor=colors.HexColor("#4B5563"), spaceAfter=6)
s_head = ParagraphStyle("CVH", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=10, leading=13, textColor=colors.HexColor("#111827"), spaceBefore=5.5, spaceAfter=2.5)
s_job = ParagraphStyle("CVJ", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=9.2, leading=12, textColor=colors.HexColor("#111827"), spaceBefore=3.8, spaceAfter=1)
s_date = ParagraphStyle("CVD", parent=styles["Normal"], fontName="Helvetica-Oblique", fontSize=8.5, leading=11, textColor=colors.HexColor("#4B5563"), spaceAfter=2)
s_body = ParagraphStyle("CVB", parent=styles["Normal"], fontName="Helvetica", fontSize=8.8, leading=12, alignment=TA_JUSTIFY, textColor=colors.HexColor("#1F2937"), spaceAfter=3.5)
s_bul = ParagraphStyle("CVBul", parent=styles["Normal"], fontName="Helvetica", fontSize=8.7, leading=11.7, alignment=TA_JUSTIFY, leftIndent=10, firstLineIndent=-6, textColor=colors.HexColor("#1F2937"), spaceAfter=2.2)

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
cl_path = "C:/Users/DELAFUENTEALONSODieg/empleo/postulaciones/mc-engineering-data-analyst/Diego_de_la_Fuente_Alonso_Carta_Presentacion_MCEng_Data_Analyst.pdf"
cl_doc = SimpleDocTemplate(
    cl_path,
    pagesize=A4,
    leftMargin=22*mm,
    rightMargin=22*mm,
    topMargin=18*mm,
    bottomMargin=18*mm,
    title="Carta de Presentación - Diego de la Fuente Alonso - MCEng España Data Analyst",
    author="Diego de la Fuente Alonso"
)

name_style = ParagraphStyle("NameHeader", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=16, leading=20, textColor=colors.HexColor("#111827"), spaceAfter=2)
role_style = ParagraphStyle("RoleHeader", parent=styles["Normal"], fontName="Helvetica", fontSize=9.8, leading=13.5, textColor=colors.HexColor("#1F2937"), spaceAfter=3)
contact_style = ParagraphStyle("ContactHeader", parent=styles["Normal"], fontName="Helvetica", fontSize=9.5, leading=13, textColor=colors.HexColor("#4B5563"), spaceAfter=8)
meta_style = ParagraphStyle("MetaText", parent=styles["Normal"], fontName="Helvetica", fontSize=9.8, leading=13.5, textColor=colors.HexColor("#1F2937"), spaceAfter=5)
subject_style = ParagraphStyle("SubjectText", parent=styles["Normal"], fontName="Helvetica", fontSize=10, leading=14.5, textColor=colors.HexColor("#111827"), spaceBefore=4, spaceAfter=10)
body_style = ParagraphStyle("BodyJustified", parent=styles["Normal"], fontName="Helvetica", fontSize=9.8, leading=14.4, alignment=TA_JUSTIFY, textColor=colors.HexColor("#1F2937"), spaceAfter=8)
bullet_style = ParagraphStyle("BulletItem", parent=styles["Normal"], fontName="Helvetica", fontSize=9.6, leading=13.8, alignment=TA_JUSTIFY, leftIndent=12, firstLineIndent=-8, textColor=colors.HexColor("#1F2937"), spaceAfter=5.5)
sign_style = ParagraphStyle("Signature", parent=styles["Normal"], fontName="Helvetica", fontSize=9.8, leading=13.5, textColor=colors.HexColor("#111827"), spaceBefore=8)

cl_story = [
    Paragraph("DIEGO DE LA FUENTE ALONSO", name_style),
    Paragraph("Data Analyst &amp; BI Specialist | Python · SQL · Reporting &amp; Dashboards (Power BI / Looker / Qlik) · Excel · Big Data", role_style),
    Paragraph("España (100% Teletrabajo / Valladolid)  |  (+34) 626 68 71 79  |  diegodelafuentealonso@gmail.com", contact_style),
    HRFlowable(width="100%", thickness=0.8, color=colors.HexColor("#D1D5DB"), spaceBefore=2, spaceAfter=12),
    Paragraph("3 de noviembre de 2026", meta_style),
    Paragraph("Para: Equipo de Selección de Talento — MCEng España (MC Engineering)", meta_style),
    Paragraph("Asunto: Candidatura a Data Analyst (100% Teletrabajo)", subject_style),
    Paragraph("Estimado equipo de Selección de MCEng España,", body_style),
    Paragraph(
        "Les escribo para presentar mi candidatura a la posición de Data Analyst en modalidad de teletrabajo completo publicada en su portal de empleo "
        "(así como a sus vacantes afines de Data Engineer y Desarrollador Java/Python). Al revisar los requisitos de la oferta, comprobé una coincidencia "
        "directa entre lo que buscan y mi perfil técnico: cuento con doble titulación de Grado Técnico Superior (DAM y DAW), el Curso de Especialización en "
        "Inteligencia Artificial y Big Data y experiencia profesional desarrollando soluciones de reporting, diseño de dashboards y procesos analíticos con Python y SQL.",
        body_style
    ),
    Paragraph(
        "En mi puesto actual en HORSE Technologies y en mis etapas previas en FDS (DXC Technology), el Ayuntamiento de Roperuelos del Páramo y Craftelier, "
        "he aplicado de forma práctica las competencias principales solicitadas:",
        body_style
    ),
    Paragraph(
        "• Desarrollo de reporting, diseño de dashboards y herramientas de BI: Diseño y mantengo cuadros de mando interactivos e informes ejecutivos utilizando "
        "herramientas de Business Intelligence (Looker, Looker Studio y Power BI, con total facilidad de adaptación a MicroStrategy y Qlik) y manejo avanzado de "
        "Excel para traducir datos complejos en métricas claras de negocio.",
        bullet_style
    ),
    Paragraph(
        "• Dominio de Python, SQL y análisis estadístico (R): Trabajo a diario con Python (Pandas, NumPy, automatización ETL) y SQL avanzado para la extracción, "
        "limpieza, modelado y explotación de datos, apoyándome en una sólida base matemática y estadística (incluyendo fundamentos de R y análisis de datos).",
        bullet_style
    ),
    Paragraph(
        "• Conocimiento de tecnologías Big Data y Cloud: Combino experiencia en producción sobre plataformas de datos en la nube (Google BigQuery y Dataform) "
        "con formación técnica específica en el ecosistema Big Data distribuido (Apache Spark, Kafka, Hadoop, Hive, Impala y Kudu).",
        bullet_style
    ),
    Spacer(1, 2),
    Paragraph(
        "Me motiva especialmente incorporarme a una consultora tecnológica con proyección europea como MCEng España, aportando precisión analítica, proactividad "
        "y trabajo en equipo en modalidad de teletrabajo completo. Resido en Valladolid y cuento con disponibilidad de incorporación en 15 días naturales.",
        body_style
    ),
    Paragraph(
        "Agradezco de antemano su tiempo y consideración. Quedo a su entera disposición para mantener una entrevista y ampliar cualquier detalle sobre mi experiencia.",
        body_style
    ),
    Paragraph(
        "Atentamente,<br/><br/>"
        "Diego de la Fuente Alonso<br/>"
        "Data Analyst &amp; BI Specialist (Python / SQL / Dashboards BI / Big Data)<br/>"
        "(+34) 626 68 71 79  |  diegodelafuentealonso@gmail.com",
        sign_style
    )
]

cl_doc.build(cl_story)
print("Created Cover Letter PDF:", cl_path)
