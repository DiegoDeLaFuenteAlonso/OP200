import json
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable

styles = getSampleStyleSheet()
base_dir = "C:/Users/DELAFUENTEALONSODieg/empleo/postulaciones/knowmadmood-analista-programador-java-jsp-remoto"

# 1. Generate 1-page CV PDF with fully justified body & bullet text (TA_JUSTIFY)
with open(f"{base_dir}/cv_spec.json", "r", encoding="utf-8") as f:
    spec = json.load(f)

cv_pdf_path = f"{base_dir}/Diego_de_la_Fuente_Alonso_CV_Knowmad_Mood_Java_JSP.pdf"
cv_doc = SimpleDocTemplate(
    cv_pdf_path,
    pagesize=A4,
    leftMargin=16*mm,
    rightMargin=16*mm,
    topMargin=13*mm,
    bottomMargin=13*mm,
    title="CV - Diego de la Fuente Alonso - Analista Programador Java JSP Thymeleaf (knowmad mood)",
    author="Diego de la Fuente Alonso"
)

s_title = ParagraphStyle("CVT", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=16, leading=19, textColor=colors.HexColor("#111827"), spaceAfter=2)
s_sub = ParagraphStyle("CVS", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=9.3, leading=12.2, textColor=colors.HexColor("#1F2937"), spaceAfter=2)
s_con = ParagraphStyle("CVC", parent=styles["Normal"], fontName="Helvetica", fontSize=8.7, leading=11.4, textColor=colors.HexColor("#4B5563"), spaceAfter=5.5)
s_head = ParagraphStyle("CVH", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=10, leading=12.8, textColor=colors.HexColor("#111827"), spaceBefore=5.0, spaceAfter=2.0)
s_job = ParagraphStyle("CVJ", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=9.1, leading=11.8, textColor=colors.HexColor("#111827"), spaceBefore=3.2, spaceAfter=0.9)
s_date = ParagraphStyle("CVD", parent=styles["Normal"], fontName="Helvetica-Oblique", fontSize=8.4, leading=11, textColor=colors.HexColor("#4B5563"), spaceAfter=1.8)
s_body = ParagraphStyle("CVB", parent=styles["Normal"], fontName="Helvetica", fontSize=8.6, leading=11.6, alignment=TA_JUSTIFY, textColor=colors.HexColor("#1F2937"), spaceAfter=3.0)
s_bul = ParagraphStyle("CVBul", parent=styles["Normal"], fontName="Helvetica", fontSize=8.5, leading=11.3, alignment=TA_JUSTIFY, leftIndent=10, firstLineIndent=-6, textColor=colors.HexColor("#1F2937"), spaceAfter=1.9)

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

# 2. Generate 1-page Cover Letter PDF (justified, NO bold in body paragraphs or bullets)
cl_path = f"{base_dir}/Diego_de_la_Fuente_Alonso_Carta_Presentacion_Knowmad_Mood_Java.pdf"
cl_doc = SimpleDocTemplate(
    cl_path,
    pagesize=A4,
    leftMargin=22*mm,
    rightMargin=22*mm,
    topMargin=18*mm,
    bottomMargin=18*mm,
    title="Carta de Presentación - Diego de la Fuente Alonso - knowmad mood Java JSP Thymeleaf",
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
    Paragraph("Analista Programador Java | Java 11+ · Spring Boot · Microservicios · APIs REST · JSP/Thymeleaf · JUnit 5", role_style),
    Paragraph("España (100% Teletrabajo / Valladolid)  |  (+34) 626 68 71 79  |  diegodelafuentealonso@gmail.com", contact_style),
    HRFlowable(width="100%", thickness=0.8, color=colors.HexColor("#D1D5DB"), spaceBefore=2, spaceAfter=12),
    Paragraph("16 de noviembre de 2026", meta_style),
    Paragraph("Para: Equipo de Selección de Talento — knowmad mood", meta_style),
    Paragraph("Asunto: Candidatura a Analista Programador | Java + JSP/Thymeleaf | Remoto (Ref. 8700507)", subject_style),
    Paragraph("Estimado equipo de Selección de knowmad mood,", body_style),
    Paragraph(
        "Les escribo para presentar mi candidatura a la posición de Analista Programador | Java + JSP/Thymeleaf en modalidad 100% remota "
        "publicada en su portal de empleo. Sigo de cerca la trayectoria de knowmad mood como referente en transformación digital y me atrae "
        "especialmente la combinación de estabilidad, cultura técnica colaborativa y flexibilidad real en teletrabajo.",
        body_style
    ),
    Paragraph(
        "A lo largo de mi trayectoria profesional en el Ayuntamiento de Roperuelos del Páramo, Craftelier, FDS (DXC Technology) y actualmente "
        "en HORSE Technologies, así como en mi doble titulación superior en Desarrollo de Aplicaciones Web (DAW) y Multiplataforma (DAM), "
        "he trabajado directamente con las tecnologías clave que solicitan para esta vacante:",
        body_style
    ),
    Paragraph(
        "• Desarrollo Backend con Java 11+, Spring Boot, Microservicios y APIs REST: Cuento con experiencia práctica diseñando y manteniendo "
        "aplicaciones y servicios web en Java con Spring Boot, Hibernate/JPA y bases de datos relacionales (PostgreSQL, MySQL y SQL Server), "
        "exponiendo APIs REST limpias y desacopladas.",
        bullet_style
    ),
    Paragraph(
        "• Vistas en servidor y Front-End clásico (JSP/JSTL, Thymeleaf, JavaScript/jQuery, HTML5 y CSS3): He construido interfaces web dinámicas "
        "integradas con Spring MVC utilizando JSP/JSTL y Thymeleaf junto con JavaScript, jQuery, HTML5 y CSS3, además de trabajar con "
        "frameworks modernos como Angular.",
        bullet_style
    ),
    Paragraph(
        "• Calidad del código, testing y perfil de Analista Programador: Utilizo JUnit 5 y Mockito para pruebas unitarias, Git para control de "
        "versiones y cuento con experiencia realizando análisis técnico, desarrollo a medida y pases controlados entre entornos DEV, QAS y PRD "
        "en proyectos corporativos.",
        bullet_style
    ),
    Spacer(1, 2),
    Paragraph(
        "Mi disponibilidad de incorporación es de 15 días naturales, con total adaptación al trabajo 100% en remoto desde España. Agradezco de "
        "antemano su tiempo y consideración, y quedo a su disposición para ampliar cualquier detalle en una entrevista.",
        body_style
    ),
    Paragraph(
        "Atentamente,<br/><br/>"
        "Diego de la Fuente Alonso<br/>"
        "Analista Programador Java / Spring Boot / JSP / Thymeleaf<br/>"
        "(+34) 626 68 71 79  |  diegodelafuentealonso@gmail.com",
        sign_style
    )
]

cl_doc.build(cl_story)
print("Created Cover Letter PDF:", cl_path)
