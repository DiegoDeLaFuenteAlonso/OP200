import json
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable

styles = getSampleStyleSheet()

# 1. Generate the 1-page CV PDF with fully justified text (TA_JUSTIFY)
with open("C:/Users/DELAFUENTEALONSODieg/empleo/postulaciones/michael-page-migracion-datos-sql-junior/cv_spec.json", "r", encoding="utf-8") as f:
    spec = json.load(f)

cv_pdf_path = "C:/Users/DELAFUENTEALONSODieg/empleo/postulaciones/michael-page-migracion-datos-sql-junior/Diego_de_la_Fuente_Alonso_CV_Michael_Page_Migracion_Datos_SQL.pdf"
cv_doc = SimpleDocTemplate(
    cv_pdf_path,
    pagesize=A4,
    leftMargin=16*mm,
    rightMargin=16*mm,
    topMargin=13*mm,
    bottomMargin=13*mm,
    title="CV - Diego de la Fuente Alonso - Especialista en Migración de Datos Junior (SQL)",
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
cl_path = "C:/Users/DELAFUENTEALONSODieg/empleo/postulaciones/michael-page-migracion-datos-sql-junior/Diego_de_la_Fuente_Alonso_Carta_Presentacion_Michael_Page_Migracion_Datos.pdf"
cl_doc = SimpleDocTemplate(
    cl_path,
    pagesize=A4,
    leftMargin=22*mm,
    rightMargin=22*mm,
    topMargin=18*mm,
    bottomMargin=18*mm,
    title="Carta de Presentación - Diego de la Fuente Alonso - Michael Page Migración de Datos Junior",
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
    Paragraph("Especialista en Migración de Datos, SQL &amp; Calidad del Dato | Procesos ETL · Validación de Integridad · Documentación Técnica", role_style),
    Paragraph("España (Full-Remote / Valladolid)  |  (+34) 626 68 71 79  |  diegodelafuentealonso@gmail.com", contact_style),
    HRFlowable(width="100%", thickness=0.8, color=colors.HexColor("#D1D5DB"), spaceBefore=2, spaceAfter=12),
    Paragraph("3 de noviembre de 2026", meta_style),
    Paragraph("Para: Equipo de Selección de Tecnología — Michael Page (Ref. JN-092026-7115236)", meta_style),
    Paragraph("Asunto: Candidatura a Especialista en Migración de Datos Junior (Modalidad Full-Remote)", subject_style),
    Paragraph("Estimado equipo de Selección de Tecnología de Michael Page,", body_style),
    Paragraph(
        "Les escribo para presentar mi candidatura a la posición de Especialista en Migración de Datos Junior (Ref. JN-092026-7115236), acogiendo mi perfil a "
        "la modalidad full-remote indicada en la oferta para candidatos residentes fuera de Sevilla. Cuento con doble titulación oficial en Informática "
        "(DAM y DAW) más el Curso de Especialización en Inteligencia Artificial y Big Data, y más de un año de experiencia práctica planificando y ejecutando "
        "procesos de migración, integración y validación de calidad de datos en entornos SQL.",
        body_style
    ),
    Paragraph(
        "A lo largo de mi trayectoria actual en HORSE Technologies y en mis etapas previas en FDS (DXC Technology), el Ayuntamiento de Roperuelos del Páramo "
        "y Craftelier, he desempeñado de forma directa las responsabilidades clave del puesto:",
        body_style
    ),
    Paragraph(
        "• Planificación y ejecución de migraciones de datos con SQL: Poseo conocimientos sólidos en bases de datos relacionales SQL (Microsoft SQL Server, "
        "PostgreSQL, MySQL, sistemas corporativos SAP y Google BigQuery) y herramientas de migración y transformación (Dataform, Python ETL y utilidades "
        "nativas SQL) para traspasar y consolidar grandes volúmenes de información entre sistemas.",
        bullet_style
    ),
    Paragraph(
        "• Garantía de calidad, integridad y validación de resultados: Aplico controles sistemáticos de integridad referencial, limpieza de duplicados, "
        "reconciliación origen-destino y validación funcional en los pasos entre entornos (DEV, QAS, PRD) para asegurar que los datos migrados sean 100% "
        "precisos y fiables.",
        bullet_style
    ),
    Paragraph(
        "• Resolución de problemas, documentación técnica y soporte: Estoy habituado a diagnosticar y corregir incidencias durante las cargas, redactar "
        "documentación técnica clara sobre los mapeos y procesos realizados, y colaborar estrechamente con diferentes departamentos internos dando soporte "
        "sobre los datos migrados.",
        bullet_style
    ),
    Spacer(1, 2),
    Paragraph(
        "Resido en Valladolid, tengo total disponibilidad para trabajar en modalidad full-remote (así como para desplazarme puntualmente a la oficina de "
        "Sevilla cuando el proyecto lo requiera) y mi preaviso de incorporación es de 15 días naturales.",
        body_style
    ),
    Paragraph(
        "Agradezco de antemano su tiempo y consideración. Quedo a su entera disposición para mantener una entrevista y ampliar cualquier detalle técnico.",
        body_style
    ),
    Paragraph(
        "Atentamente,<br/><br/>"
        "Diego de la Fuente Alonso<br/>"
        "Especialista en Migración de Datos, SQL &amp; Calidad del Dato<br/>"
        "(+34) 626 68 71 79  |  diegodelafuentealonso@gmail.com",
        sign_style
    )
]

cl_doc.build(cl_story)
print("Created Cover Letter PDF:", cl_path)
