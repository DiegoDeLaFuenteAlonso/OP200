import json
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable

styles = getSampleStyleSheet()

# 1. Generate the 1-page CV PDF with fully justified text (TA_JUSTIFY)
with open("C:/Users/DELAFUENTEALONSODieg/empleo/postulaciones/seresco-java-valladolid/cv_spec.json", "r", encoding="utf-8") as f:
    spec = json.load(f)

cv_pdf_path = "C:/Users/DELAFUENTEALONSODieg/empleo/postulaciones/seresco-java-valladolid/Diego_de_la_Fuente_Alonso_CV_Seresco_Java_Valladolid.pdf"
cv_doc = SimpleDocTemplate(
    cv_pdf_path,
    pagesize=A4,
    leftMargin=16*mm,
    rightMargin=16*mm,
    topMargin=13*mm,
    bottomMargin=13*mm,
    title="CV - Diego de la Fuente Alonso - Desarrollador Java / JEE (Seresco Valladolid)",
    author="Diego de la Fuente Alonso"
)

s_title = ParagraphStyle("CVT", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=16, leading=19, textColor=colors.HexColor("#111827"), spaceAfter=2)
s_sub = ParagraphStyle("CVS", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=9.3, leading=12.2, textColor=colors.HexColor("#1F2937"), spaceAfter=2)
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
cl_path = "C:/Users/DELAFUENTEALONSODieg/empleo/postulaciones/seresco-java-valladolid/Diego_de_la_Fuente_Alonso_Carta_Presentacion_Seresco_Java_Valladolid.pdf"
cl_doc = SimpleDocTemplate(
    cl_path,
    pagesize=A4,
    leftMargin=22*mm,
    rightMargin=22*mm,
    topMargin=18*mm,
    bottomMargin=18*mm,
    title="Carta de Presentación - Diego de la Fuente Alonso - Seresco Valladolid",
    author="Diego de la Fuente Alonso"
)

name_style = ParagraphStyle("NameHeader", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=16, leading=20, textColor=colors.HexColor("#111827"), spaceAfter=2)
role_style = ParagraphStyle("RoleHeader", parent=styles["Normal"], fontName="Helvetica", fontSize=9.6, leading=13.2, textColor=colors.HexColor("#1F2937"), spaceAfter=3)
contact_style = ParagraphStyle("ContactHeader", parent=styles["Normal"], fontName="Helvetica", fontSize=9.5, leading=13, textColor=colors.HexColor("#4B5563"), spaceAfter=8)
meta_style = ParagraphStyle("MetaText", parent=styles["Normal"], fontName="Helvetica", fontSize=9.8, leading=13.5, textColor=colors.HexColor("#1F2937"), spaceAfter=5)
subject_style = ParagraphStyle("SubjectText", parent=styles["Normal"], fontName="Helvetica", fontSize=10, leading=14.5, textColor=colors.HexColor("#111827"), spaceBefore=4, spaceAfter=10)
body_style = ParagraphStyle("BodyJustified", parent=styles["Normal"], fontName="Helvetica", fontSize=9.8, leading=14.3, alignment=TA_JUSTIFY, textColor=colors.HexColor("#1F2937"), spaceAfter=8)
bullet_style = ParagraphStyle("BulletItem", parent=styles["Normal"], fontName="Helvetica", fontSize=9.6, leading=13.7, alignment=TA_JUSTIFY, leftIndent=12, firstLineIndent=-8, textColor=colors.HexColor("#1F2937"), spaceAfter=5.5)
sign_style = ParagraphStyle("Signature", parent=styles["Normal"], fontName="Helvetica", fontSize=9.8, leading=13.5, textColor=colors.HexColor("#111827"), spaceBefore=8)

cl_story = [
    Paragraph("DIEGO DE LA FUENTE ALONSO", name_style),
    Paragraph("Desarrollador de Software Java / JEE &amp; SQL | Entornos Web (JSF, Spring Boot, Hibernate/JDBC) &amp; Jasper Reports", role_style),
    Paragraph("Valladolid, España  |  (+34) 626 68 71 79  |  diegodelafuentealonso@gmail.com", contact_style),
    HRFlowable(width="100%", thickness=0.8, color=colors.HexColor("#D1D5DB"), spaceBefore=2, spaceAfter=12),
    Paragraph("3 de noviembre de 2026", meta_style),
    Paragraph("Para: Equipo de Selección y Área Técnica de Producción de Software — Seresco (Valladolid)", meta_style),
    Paragraph("Asunto: Candidatura a Desarrollador/a Java en Valladolid", subject_style),
    Paragraph("Estimado equipo de Selección de Seresco,", body_style),
    Paragraph(
        "Les escribo para presentar mi candidatura a la posición de Desarrollador/a Java para su Área Técnica de Producción de Software en Valladolid. Resido "
        "actualmente en Valladolid y cuento con doble titulación oficial en Informática (Grado Superior en Desarrollo de Aplicaciones Web y Grado Superior en "
        "Desarrollo de Aplicaciones Multiplataforma, además de la Especialización en IA y Big Data) y más de un año de experiencia práctica desarrollando "
        "software en entornos web con Java, SQL y generación de informes.",
        body_style
    ),
    Paragraph(
        "Mi trayectoria técnica se alinea directamente con los requisitos y valores de Seresco para este puesto:",
        body_style
    ),
    Paragraph(
        "• Experiencia en proyectos de desarrollo web con Java, SQL, JSF y Jasper Reports: He trabajado en el desarrollo y mantenimiento de aplicaciones web "
        "utilizando el ecosistema Java/JEE (JSF, JSP, Spring Boot, Hibernate y JDBC), diseñando y optimizando consultas sobre bases de datos relacionales SQL "
        "(PostgreSQL, MySQL y SQL Server) e implementando la generación de informes y documentos parametrizados con Jasper Reports.",
        bullet_style
    ),
    Paragraph(
        "• Experiencia en proyectos vinculados al ámbito rural, agrícola y de gestión pública: Durante mis dos etapas como desarrollador en el Ayuntamiento de "
        "Roperuelos del Páramo, construí soluciones web y de bases de datos orientadas a la gestión municipal, territorial y de expedientes del entorno rural y "
        "agrícola, experiencia que complementé con mi etapa en consultoría tecnológica en FDS (DXC Technology) y mi puesto actual en HORSE Technologies en Valladolid.",
        bullet_style
    ),
    Paragraph(
        "• Residencia en Valladolid y compromiso a largo plazo: Busco integrarme de forma estable en el equipo de Seresco en Valladolid, donde la modalidad "
        "híbrida y la jornada continua de 08:00 a 15:00h encajan de manera inmejorable con mi planificación profesional y personal.",
        bullet_style
    ),
    Spacer(1, 2),
    Paragraph(
        "Mi disponibilidad de incorporación es de 15 días naturales. Agradezco de antemano su tiempo y consideración, y quedo a su entera disposición para "
        "mantener una entrevista personal en sus oficinas de Valladolid o por videollamada.",
        body_style
    ),
    Paragraph(
        "Atentamente,<br/><br/>"
        "Diego de la Fuente Alonso<br/>"
        "Desarrollador de Software Java / JEE &amp; SQL (JSF / Spring Boot / Jasper Reports)<br/>"
        "Valladolid  |  (+34) 626 68 71 79  |  diegodelafuentealonso@gmail.com",
        sign_style
    )
]

cl_doc.build(cl_story)
print("Created Cover Letter PDF:", cl_path)
