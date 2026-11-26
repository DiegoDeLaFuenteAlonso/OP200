import json
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable

styles = getSampleStyleSheet()

# 1. Generate the 1-page CV PDF with fully justified text (TA_JUSTIFY)
with open("C:/Users/DELAFUENTEALONSODieg/empleo/postulaciones/grupo-digital-devsecops-junior/cv_spec.json", "r", encoding="utf-8") as f:
    spec = json.load(f)

cv_pdf_path = "C:/Users/DELAFUENTEALONSODieg/empleo/postulaciones/grupo-digital-devsecops-junior/Diego_de_la_Fuente_Alonso_CV_Grupo_Digital_DevSecOps_Junior.pdf"
cv_doc = SimpleDocTemplate(
    cv_pdf_path,
    pagesize=A4,
    leftMargin=16*mm,
    rightMargin=16*mm,
    topMargin=13*mm,
    bottomMargin=13*mm,
    title="CV - Diego de la Fuente Alonso - Técnico DevSecOps Junior (Grupo Digital)",
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
cl_path = "C:/Users/DELAFUENTEALONSODieg/empleo/postulaciones/grupo-digital-devsecops-junior/Diego_de_la_Fuente_Alonso_Carta_Presentacion_Grupo_Digital_DevSecOps.pdf"
cl_doc = SimpleDocTemplate(
    cl_path,
    pagesize=A4,
    leftMargin=22*mm,
    rightMargin=22*mm,
    topMargin=18*mm,
    bottomMargin=18*mm,
    title="Carta de Presentación - Diego de la Fuente Alonso - Grupo Digital DevSecOps Junior",
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
    Paragraph("Técnico DevSecOps &amp; Automatización Junior | Pipelines CI/CD (GitHub Actions) · Python/Bash/PowerShell · Docker · APIs · PostgreSQL", role_style),
    Paragraph("España (100% Remoto / Horario 7:30–15:30h)  |  (+34) 626 68 71 79  |  diegodelafuentealonso@gmail.com", contact_style),
    HRFlowable(width="100%", thickness=0.8, color=colors.HexColor("#D1D5DB"), spaceBefore=2, spaceAfter=12),
    Paragraph("3 de noviembre de 2026", meta_style),
    Paragraph("Para: Equipo de Selección de Talento IT — Grupo Digital", meta_style),
    Paragraph("Asunto: Candidatura a Técnico/a DevSecOps Junior 7:30–15:30h (100% Remoto)", subject_style),
    Paragraph("Estimado equipo de Selección de Grupo Digital,", body_style),
    Paragraph(
        "Les escribo para presentar mi candidatura a la posición de Técnico/a DevSecOps Junior en modalidad 100% remota (horario de 7:30 a 15:30h) publicada "
        "en Tecnoempleo. Cuento con más de un año de experiencia práctica en entornos técnicos de automatización, desarrollo de scripts, administración de "
        "APIs REST, bases de datos SQL/PostgreSQL y gestión de despliegues, encajando de lleno en la franja de 6 meses a 1,5 años que solicitan para esta vacante.",
        body_style
    ),
    Paragraph(
        "A lo largo de mi trayectoria actual en HORSE Technologies y en mis etapas previas en FDS (DXC Technology), el Ayuntamiento de Roperuelos del Páramo "
        "y Craftelier, he trabajado de forma directa con las tecnologías y responsabilidades descritas en la oferta:",
        body_style
    ),
    Paragraph(
        "• Automatización con Python, Bash, PowerShell y pipelines CI/CD con GitHub Actions: Desarrollo scripts y herramientas de automatización en Python, Go, "
        "Bash y PowerShell sobre sistemas Linux y Windows, colaborando en el mantenimiento de repositorios en GitHub, flujos de integración y despliegue continuo "
        "con GitHub Actions y contenedores Docker.",
        bullet_style
    ),
    Paragraph(
        "• Uso y administración de APIs REST, SQL y PostgreSQL: Poseo experiencia práctica integrando herramientas y procesos mediante APIs RESTful y trabajando "
        "directamente con bases de datos relacionales SQL y PostgreSQL.",
        bullet_style
    ),
    Paragraph(
        "• Gestión de credenciales, secretos, mínimo privilegio y resolución de incidencias: En FDS (DXC Technology) gestioné y validé el ciclo de despliegues "
        "entre entornos (DEV, QAS, PRD), y en mis desarrollos actuales aplico buenas prácticas de gestión de secretos, principio de mínimo privilegio, hardening "
        "básico y análisis de logs para resolver incidencias técnicas con rapidez.",
        bullet_style
    ),
    Spacer(1, 2),
    Paragraph(
        "Cuento con doble titulación de Grado Superior en Desarrollo de Aplicaciones Web (DAW) y Multiplataforma (DAM), además del Curso de Especialización en "
        "Inteligencia Artificial y Big Data. Resido en Valladolid (España), me adapto al 100% al horario continuo de 7:30 a 15:30h (y a la jornada especial "
        "bimensual) y mi disponibilidad de incorporación es de 15 días naturales.",
        body_style
    ),
    Paragraph(
        "Agradezco de antemano su tiempo y consideración. Quedo a su entera disposición para mantener una entrevista técnica.",
        body_style
    ),
    Paragraph(
        "Atentamente,<br/><br/>"
        "Diego de la Fuente Alonso<br/>"
        "Técnico DevSecOps &amp; Automatización Junior (Python / GitHub Actions / Docker / APIs / PostgreSQL)<br/>"
        "(+34) 626 68 71 79  |  diegodelafuentealonso@gmail.com",
        sign_style
    )
]

cl_doc.build(cl_story)
print("Created Cover Letter PDF:", cl_path)
