from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable

# 1. Cover Letter PDF (NO BOLD in body text)
cl_path = "C:/Users/DELAFUENTEALONSODieg/empleo/postulaciones/infortec-java-junior-teletrabajo/Diego_de_la_Fuente_Alonso_Carta_Presentacion_Infortec_Java_Junior.pdf"

doc = SimpleDocTemplate(
    cl_path,
    pagesize=A4,
    leftMargin=22*mm,
    rightMargin=22*mm,
    topMargin=18*mm,
    bottomMargin=18*mm,
    title="Carta de Presentación - Diego de la Fuente Alonso - Infortec Consultores Java Junior",
    author="Diego de la Fuente Alonso"
)

styles = getSampleStyleSheet()
name_style = ParagraphStyle("NameHeader", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=16, leading=20, textColor=colors.HexColor("#111827"), spaceAfter=2)
role_style = ParagraphStyle("RoleHeader", parent=styles["Normal"], fontName="Helvetica", fontSize=9.8, leading=13.5, textColor=colors.HexColor("#1F2937"), spaceAfter=3)
contact_style = ParagraphStyle("ContactHeader", parent=styles["Normal"], fontName="Helvetica", fontSize=9.5, leading=13, textColor=colors.HexColor("#4B5563"), spaceAfter=8)
meta_style = ParagraphStyle("MetaText", parent=styles["Normal"], fontName="Helvetica", fontSize=9.8, leading=13.5, textColor=colors.HexColor("#1F2937"), spaceAfter=5)
subject_style = ParagraphStyle("SubjectText", parent=styles["Normal"], fontName="Helvetica", fontSize=10, leading=14.5, textColor=colors.HexColor("#111827"), spaceBefore=4, spaceAfter=10)
body_style = ParagraphStyle("BodyJustified", parent=styles["Normal"], fontName="Helvetica", fontSize=9.8, leading=14.4, alignment=TA_JUSTIFY, textColor=colors.HexColor("#1F2937"), spaceAfter=8)
bullet_style = ParagraphStyle("BulletItem", parent=styles["Normal"], fontName="Helvetica", fontSize=9.6, leading=13.8, alignment=TA_JUSTIFY, leftIndent=12, firstLineIndent=-8, textColor=colors.HexColor("#1F2937"), spaceAfter=5.5)
sign_style = ParagraphStyle("Signature", parent=styles["Normal"], fontName="Helvetica", fontSize=9.8, leading=13.5, textColor=colors.HexColor("#111827"), spaceBefore=8)

story = [
    Paragraph("DIEGO DE LA FUENTE ALONSO", name_style),
    Paragraph("Programador Java &amp; Especialista en Integración de Datos (ETL / SQL) | Spring Boot · Hibernate · JDBC · JSP/JSTL · JavaScript · Docker", role_style),
    Paragraph("España (100% Teletrabajo / Valladolid)  |  (+34) 626 68 71 79  |  diegodelafuentealonso@gmail.com", contact_style),
    HRFlowable(width="100%", thickness=0.8, color=colors.HexColor("#D1D5DB"), spaceBefore=2, spaceAfter=12),
    Paragraph("3 de noviembre de 2026", meta_style),
    Paragraph("Para: Equipo de Selección de Talento IT — Infortec Consultores", meta_style),
    Paragraph("Asunto: Candidatura a Programador/a Java Junior 100% Teletrabajo", subject_style),
    Paragraph("Estimado equipo de Selección de Infortec Consultores,", body_style),
    Paragraph(
        "Les escribo para presentar mi candidatura a la posición de Programador/a Java Junior en modalidad 100% teletrabajo publicada en su portal de empleo. "
        "Al revisar los requisitos tanto obligatorios como valorables de la vacante, comprobé una coincidencia total con mi formación de Grado Superior y con mi "
        "experiencia práctica combinando desarrollo en el ecosistema Java con ingeniería de procesos ETL y optimización SQL.",
        body_style
    ),
    Paragraph(
        "Aporto a su equipo una combinación poco habitual en un perfil Junior, al unir el desarrollo web en Java con el tratamiento avanzado de datos en producción:",
        body_style
    ),
    Paragraph(
        "• Doble Grado Superior y dominio del ecosistema Java Web: Poseo doble titulación de Grado Superior en Desarrollo de Aplicaciones Multiplataforma (DAM) "
        "y Desarrollo de Aplicaciones Web (DAW). He desarrollado aplicaciones backend y frontend utilizando Java, Spring Boot, Hibernate (JPA), JDBC, vistas "
        "JSP/JSTL y JavaScript, cuidando la seguridad de las sesiones, el cifrado y la trazabilidad de cada operación.",
        bullet_style
    ),
    Paragraph(
        "• Procesos ETL, optimización SQL y múltiples orígenes y formatos de datos: Actualmente en HORSE Technologies diseño y mantengo procesos ETL y flujos de "
        "integración que conectan bases de datos relacionales (PostgreSQL, MySQL, SQL Server), hojas de cálculo y APIs REST, transformando y validando datos en "
        "formatos CSV, XML, JSON y YAML mediante consultas SQL optimizadas.",
        bullet_style
    ),
    Paragraph(
        "• Entornos Linux, Git, Docker y cultura de calidad: Trabajo a diario con control de versiones en Git, despliegue en contenedores Docker sobre sistemas "
        "Linux y metodologías estructuradas de gestión de cambios y servicios TI (ITIL) adquiridas en entornos de consultoría tecnológica como FDS (DXC Technology).",
        bullet_style
    ),
    Spacer(1, 2),
    Paragraph(
        "Me motiva enormemente incorporarme a un proyecto donde el objetivo no sea solo mantener lo existente, sino transformar, optimizar consultas y construir "
        "soluciones más rápidas y seguras en modalidad 100% teletrabajo. Resido en Valladolid y cuento con disponibilidad de incorporación en 15 días naturales.",
        body_style
    ),
    Paragraph(
        "Agradezco de antemano su tiempo y consideración. Quedo a su entera disposición para mantener una entrevista técnica y profundizar en mi perfil.",
        body_style
    ),
    Paragraph(
        "Atentamente,<br/><br/>"
        "Diego de la Fuente Alonso<br/>"
        "Programador Java &amp; Especialista en Integración de Datos (Spring Boot / Hibernate / SQL / ETL)<br/>"
        "(+34) 626 68 71 79  |  diegodelafuentealonso@gmail.com",
        sign_style
    )
]

doc.build(story)
print("Created Cover Letter PDF:", cl_path)

# 2. Also generate a clean 1-page PDF version of the CV (since Bizneo's AI autofill requires PDF)
import json
with open("C:/Users/DELAFUENTEALONSODieg/empleo/postulaciones/infortec-java-junior-teletrabajo/cv_spec.json", "r", encoding="utf-8") as f:
    spec = json.load(f)

cv_pdf_path = "C:/Users/DELAFUENTEALONSODieg/empleo/postulaciones/infortec-java-junior-teletrabajo/Diego_de_la_Fuente_Alonso_CV_Infortec_Java_Junior.pdf"
cv_doc = SimpleDocTemplate(
    cv_pdf_path,
    pagesize=A4,
    leftMargin=16*mm,
    rightMargin=16*mm,
    topMargin=13*mm,
    bottomMargin=13*mm,
    title="CV - Diego de la Fuente Alonso - Programador Java Junior",
    author="Diego de la Fuente Alonso"
)

s_title = ParagraphStyle("CVT", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=16, leading=19, textColor=colors.HexColor("#111827"), spaceAfter=2)
s_sub = ParagraphStyle("CVS", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=9.5, leading=12.5, textColor=colors.HexColor("#1F2937"), spaceAfter=2)
s_con = ParagraphStyle("CVC", parent=styles["Normal"], fontName="Helvetica", fontSize=8.8, leading=11.5, textColor=colors.HexColor("#4B5563"), spaceAfter=6)
s_head = ParagraphStyle("CVH", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=10, leading=13, textColor=colors.HexColor("#111827"), spaceBefore=6, spaceAfter=3)
s_job = ParagraphStyle("CVJ", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=9.2, leading=12, textColor=colors.HexColor("#111827"), spaceBefore=4, spaceAfter=1)
s_date = ParagraphStyle("CVD", parent=styles["Normal"], fontName="Helvetica-Oblique", fontSize=8.5, leading=11, textColor=colors.HexColor("#4B5563"), spaceAfter=2)
s_body = ParagraphStyle("CVB", parent=styles["Normal"], fontName="Helvetica", fontSize=8.8, leading=12, alignment=TA_JUSTIFY, textColor=colors.HexColor("#1F2937"), spaceAfter=4)
s_bul = ParagraphStyle("CVBul", parent=styles["Normal"], fontName="Helvetica", fontSize=8.7, leading=11.8, alignment=TA_JUSTIFY, leftIndent=10, firstLineIndent=-6, textColor=colors.HexColor("#1F2937"), spaceAfter=2.2)

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
