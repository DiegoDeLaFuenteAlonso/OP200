import json
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable

styles = getSampleStyleSheet()

# 1. Generate the 1-page CV PDF with fully justified text (TA_JUSTIFY)
with open("C:/Users/DELAFUENTEALONSODieg/empleo/postulaciones/logicalis-backend-python-junior/cv_spec.json", "r", encoding="utf-8") as f:
    spec = json.load(f)

cv_pdf_path = "C:/Users/DELAFUENTEALONSODieg/empleo/postulaciones/logicalis-backend-python-junior/Diego_de_la_Fuente_Alonso_CV_Logicalis_Backend_Python_Junior.pdf"
cv_doc = SimpleDocTemplate(
    cv_pdf_path,
    pagesize=A4,
    leftMargin=16*mm,
    rightMargin=16*mm,
    topMargin=13*mm,
    bottomMargin=13*mm,
    title="CV - Diego de la Fuente Alonso - Jr Python Backend Developer (Logicalis Spain)",
    author="Diego de la Fuente Alonso"
)

s_title = ParagraphStyle("CVT", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=16, leading=19, textColor=colors.HexColor("#111827"), spaceAfter=2)
s_sub = ParagraphStyle("CVS", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=9.0, leading=12.0, textColor=colors.HexColor("#1F2937"), spaceAfter=2)
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
cl_path = "C:/Users/DELAFUENTEALONSODieg/empleo/postulaciones/logicalis-backend-python-junior/Diego_de_la_Fuente_Alonso_Carta_Presentacion_Logicalis_Backend_Python.pdf"
cl_doc = SimpleDocTemplate(
    cl_path,
    pagesize=A4,
    leftMargin=22*mm,
    rightMargin=22*mm,
    topMargin=18*mm,
    bottomMargin=18*mm,
    title="Carta de Presentación - Diego de la Fuente Alonso - Logicalis Spain Jr Python Developer",
    author="Diego de la Fuente Alonso"
)

name_style = ParagraphStyle("NameHeader", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=16, leading=20, textColor=colors.HexColor("#111827"), spaceAfter=2)
role_style = ParagraphStyle("RoleHeader", parent=styles["Normal"], fontName="Helvetica", fontSize=9.4, leading=13.2, textColor=colors.HexColor("#1F2937"), spaceAfter=3)
contact_style = ParagraphStyle("ContactHeader", parent=styles["Normal"], fontName="Helvetica", fontSize=9.5, leading=13, textColor=colors.HexColor("#4B5563"), spaceAfter=8)
meta_style = ParagraphStyle("MetaText", parent=styles["Normal"], fontName="Helvetica", fontSize=9.8, leading=13.5, textColor=colors.HexColor("#1F2937"), spaceAfter=5)
subject_style = ParagraphStyle("SubjectText", parent=styles["Normal"], fontName="Helvetica", fontSize=10, leading=14.5, textColor=colors.HexColor("#111827"), spaceBefore=4, spaceAfter=10)
body_style = ParagraphStyle("BodyJustified", parent=styles["Normal"], fontName="Helvetica", fontSize=9.8, leading=14.3, alignment=TA_JUSTIFY, textColor=colors.HexColor("#1F2937"), spaceAfter=8)
bullet_style = ParagraphStyle("BulletItem", parent=styles["Normal"], fontName="Helvetica", fontSize=9.6, leading=13.7, alignment=TA_JUSTIFY, leftIndent=12, firstLineIndent=-8, textColor=colors.HexColor("#1F2937"), spaceAfter=5.5)
sign_style = ParagraphStyle("Signature", parent=styles["Normal"], fontName="Helvetica", fontSize=9.8, leading=13.5, textColor=colors.HexColor("#111827"), spaceBefore=8)

cl_story = [
    Paragraph("DIEGO DE LA FUENTE ALONSO", name_style),
    Paragraph("Jr Python Backend Developer | FastAPI · PyTest · Pandas &amp; NumPy · PostgreSQL/MySQL/MongoDB · Docker · Cloud (GCP)", role_style),
    Paragraph("España (100% Remoto / Valladolid)  |  (+34) 626 68 71 79  |  diegodelafuentealonso@gmail.com", contact_style),
    HRFlowable(width="100%", thickness=0.8, color=colors.HexColor("#D1D5DB"), spaceBefore=2, spaceAfter=12),
    Paragraph("3 de noviembre de 2026", meta_style),
    Paragraph("Para: Equipo de Selección y Desarrollo Cloud — Logicalis Spain", meta_style),
    Paragraph("Asunto: Candidatura a Desarrollador/a Backend Python (Jr Python Developer – Ref. 8747758)", subject_style),
    Paragraph("Estimado equipo de Selección de Logicalis Spain,", body_style),
    Paragraph(
        "Les escribo para presentar mi candidatura a la posición de Desarrollador/a Backend Python (Jr Python Developer) en modalidad 100% remota para su equipo "
        "de desarrollo en el Cloud. Al revisar las responsabilidades y el stack técnico de la vacante, comprobé una coincidencia directa y completa con las "
        "tecnologías que utilizo a diario en mi puesto actual y en mis proyectos de programación: Python, FastAPI, PyTest, Pandas, NumPy, bases de datos "
        "PostgreSQL/MySQL/MongoDB, Docker y entornos Cloud (GCP).",
        body_style
    ),
    Paragraph(
        "A lo largo de mi trayectoria en HORSE Technologies, FDS (DXC Technology), el Ayuntamiento de Roperuelos del Páramo y Craftelier, he consolidado cada "
        "uno de los pilares técnicos que buscan para este proyecto de larga duración:",
        body_style
    ),
    Paragraph(
        "• Desarrollo backend eficiente con Python y FastAPI en el Cloud: Diseño, construyo y mantengo servicios backend escalables, APIs RESTful y sistemas de "
        "mensajería y notificaciones de eventos utilizando Python y FastAPI (además de Flask/Django), desplegados en entornos Cloud (con experiencia diaria en "
        "producción sobre Google Cloud Platform y conocimientos de Azure e IBM Cloud).",
        bullet_style
    ),
    Paragraph(
        "• Calidad de código con PyTest y análisis de datos con Pandas y NumPy: Implemento pruebas automatizadas con PyTest, participo en revisiones de código "
        "con Git y utilizo Pandas y NumPy para el procesamiento, limpieza y optimización del rendimiento de procesos de datos.",
        bullet_style
    ),
    Paragraph(
        "• Bases de datos (PostgreSQL, MySQL y MongoDB), Docker/Kubernetes y monitoreo: Manejo con soltura tanto bases de datos relacionales (PostgreSQL y "
        "MySQL) como NoSQL (MongoDB), empaquetando servicios con Docker y aplicando herramientas de monitoreo y logging para asegurar la observabilidad en producción.",
        bullet_style
    ),
    Spacer(1, 2),
    Paragraph(
        "Cuento con doble titulación de Grado Superior en Desarrollo de Aplicaciones (DAM y DAW), el Curso de Especialización en Inteligencia Artificial y Big "
        "Data y una fuerte iniciativa desarrollando proyectos propios en Python. Resido en Valladolid, estoy totalmente conforme con la banda salarial de "
        "25.000 € a 28.000 € brutos anuales y cuento con plena disponibilidad para la rotación de turnos, guardias remuneradas futuras e incorporación en 15 días naturales.",
        body_style
    ),
    Paragraph(
        "Agradezco de antemano su tiempo y consideración. Quedo a su entera disposición para mantener una entrevista técnica.",
        body_style
    ),
    Paragraph(
        "Atentamente,<br/><br/>"
        "Diego de la Fuente Alonso<br/>"
        "Jr Python Backend Developer (FastAPI / PyTest / Pandas &amp; NumPy / PostgreSQL &amp; MongoDB / Cloud GCP)<br/>"
        "(+34) 626 68 71 79  |  diegodelafuentealonso@gmail.com",
        sign_style
    )
]

cl_doc.build(cl_story)
print("Created Cover Letter PDF:", cl_path)
