import json
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable

styles = getSampleStyleSheet()

# 1. Generate the 1-page CV PDF with fully justified text (TA_JUSTIFY)
with open("C:/Users/DELAFUENTEALONSODieg/empleo/postulaciones/metrica-desarrollador-back-junior/cv_spec.json", "r", encoding="utf-8") as f:
    spec = json.load(f)

cv_pdf_path = "C:/Users/DELAFUENTEALONSODieg/empleo/postulaciones/metrica-desarrollador-back-junior/Diego_de_la_Fuente_Alonso_CV_Metrica_Desarrollador_Back_Junior.pdf"
cv_doc = SimpleDocTemplate(
    cv_pdf_path,
    pagesize=A4,
    leftMargin=16*mm,
    rightMargin=16*mm,
    topMargin=13*mm,
    bottomMargin=13*mm,
    title="CV - Diego de la Fuente Alonso - Desarrollador Back Junior (Java & SQL)",
    author="Diego de la Fuente Alonso"
)

s_title = ParagraphStyle("CVT", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=16, leading=19, textColor=colors.HexColor("#111827"), spaceAfter=2)
s_sub = ParagraphStyle("CVS", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=9.6, leading=12.5, textColor=colors.HexColor("#1F2937"), spaceAfter=2)
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

# 2. Also generate the matching Cover Letter PDF (justified, no bold in body)
cl_path = "C:/Users/DELAFUENTEALONSODieg/empleo/postulaciones/metrica-desarrollador-back-junior/Diego_de_la_Fuente_Alonso_Carta_Presentacion_Metrica_Back_Junior.pdf"
cl_doc = SimpleDocTemplate(
    cl_path,
    pagesize=A4,
    leftMargin=22*mm,
    rightMargin=22*mm,
    topMargin=18*mm,
    bottomMargin=18*mm,
    title="Carta de Presentación - Diego de la Fuente Alonso - Métrica Desarrollador Back Junior",
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
    Paragraph("Desarrollador Back-End Junior | Java · Spring Boot · Maven/Gradle · APIs REST · SQL · Git", role_style),
    Paragraph("España (100% Remoto / Valladolid)  |  (+34) 626 68 71 79  |  diegodelafuentealonso@gmail.com", contact_style),
    HRFlowable(width="100%", thickness=0.8, color=colors.HexColor("#D1D5DB"), spaceBefore=2, spaceAfter=12),
    Paragraph("3 de noviembre de 2026", meta_style),
    Paragraph("Para: Equipo de Selección y Squad Santander — Métrica España", meta_style),
    Paragraph("Asunto: Candidatura a Desarrollador Back Junior (100% Remoto)", subject_style),
    Paragraph("Estimado equipo de Selección de Métrica España,", body_style),
    Paragraph(
        "Les escribo para presentar mi candidatura a la posición de Desarrollador Back Junior en modalidad 100% remota para el Squad Santander. Cuento con más "
        "de un año de experiencia práctica en el desarrollo de software backend e integración de bases de datos relacionales, además de doble titulación de Grado "
        "Superior en Desarrollo de Aplicaciones Multiplataforma (DAM) y Desarrollo de Aplicaciones Web (DAW).",
        body_style
    ),
    Paragraph(
        "A lo largo de mi trayectoria en HORSE Technologies, FDS (DXC Technology), el Ayuntamiento de Roperuelos del Páramo y Craftelier, he consolidado los "
        "pilares técnicos que solicitan para esta vacante:",
        body_style
    ),
    Paragraph(
        "• Sólidos fundamentos en Java y su ecosistema: He desarrollado servicios back-end y APIs RESTful utilizando Java, Spring Boot, Hibernate/JPA, JDBC y "
        "gestión de proyectos con Maven y Gradle, aplicando principios de diseño de software (SOLID, Clean Code) y patrones de arquitectura en capas.",
        bullet_style
    ),
    Paragraph(
        "• Dominio de SQL y bases de datos relacionales: Trabajo a diario diseñando esquemas, escribiendo consultas complejas y optimizando el acceso a datos "
        "sobre motores relacionales como PostgreSQL, MySQL y Microsoft SQL Server.",
        bullet_style
    ),
    Paragraph(
        "• Trabajo en equipo, control de versiones con Git y aprendizaje continuo: Estoy habituado a participar en el ciclo de vida completo del software bajo "
        "la supervisión de perfiles senior, utilizando Git para el control de versiones y siguiendo estándares rigurosos de pruebas y paso a producción.",
        bullet_style
    ),
    Spacer(1, 2),
    Paragraph(
        "Me entusiasma la oportunidad de integrarme en el equipo de desarrollo de Métrica España en modalidad 100% teletrabajo y seguir creciendo como "
        "Desarrollador Back-End en proyectos de primer nivel. Resido en Valladolid y mi disponibilidad de incorporación es de 15 días naturales.",
        body_style
    ),
    Paragraph(
        "Agradezco de antemano su tiempo y consideración. Quedo a su entera disposición para mantener una entrevista técnica.",
        body_style
    ),
    Paragraph(
        "Atentamente,<br/><br/>"
        "Diego de la Fuente Alonso<br/>"
        "Desarrollador Back-End Junior (Java / Spring Boot / SQL / Git)<br/>"
        "(+34) 626 68 71 79  |  diegodelafuentealonso@gmail.com",
        sign_style
    )
]

cl_doc.build(cl_story)
print("Created Cover Letter PDF:", cl_path)
