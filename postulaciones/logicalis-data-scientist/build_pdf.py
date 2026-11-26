from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable

out_path = "C:/Users/DELAFUENTEALONSODieg/empleo/postulaciones/logicalis-data-scientist/Diego_de_la_Fuente_Alonso_Carta_Presentacion_Logicalis_Data_Scientist.pdf"

doc = SimpleDocTemplate(
    out_path,
    pagesize=A4,
    leftMargin=22*mm,
    rightMargin=22*mm,
    topMargin=20*mm,
    bottomMargin=20*mm,
    title="Carta de Presentación - Diego de la Fuente Alonso - Logicalis Spain Data Scientist",
    author="Diego de la Fuente Alonso"
)

styles = getSampleStyleSheet()

name_style = ParagraphStyle("NameHeader", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=16, leading=20, textColor=colors.HexColor("#111827"), spaceAfter=2)
role_style = ParagraphStyle("RoleHeader", parent=styles["Normal"], fontName="Helvetica", fontSize=10.2, leading=14, textColor=colors.HexColor("#1F2937"), spaceAfter=3)
contact_style = ParagraphStyle("ContactHeader", parent=styles["Normal"], fontName="Helvetica", fontSize=9.5, leading=13, textColor=colors.HexColor("#4B5563"), spaceAfter=8)
meta_style = ParagraphStyle("MetaText", parent=styles["Normal"], fontName="Helvetica", fontSize=10, leading=14, textColor=colors.HexColor("#1F2937"), spaceAfter=6)
subject_style = ParagraphStyle("SubjectText", parent=styles["Normal"], fontName="Helvetica", fontSize=10.5, leading=15, textColor=colors.HexColor("#111827"), spaceBefore=6, spaceAfter=10)
body_style = ParagraphStyle("BodyJustified", parent=styles["Normal"], fontName="Helvetica", fontSize=10, leading=15, alignment=TA_JUSTIFY, textColor=colors.HexColor("#1F2937"), spaceAfter=9)
bullet_style = ParagraphStyle("BulletItem", parent=styles["Normal"], fontName="Helvetica", fontSize=9.8, leading=14.5, alignment=TA_JUSTIFY, leftIndent=12, firstLineIndent=-8, textColor=colors.HexColor("#1F2937"), spaceAfter=6)
sign_style = ParagraphStyle("Signature", parent=styles["Normal"], fontName="Helvetica", fontSize=10, leading=14, textColor=colors.HexColor("#111827"), spaceBefore=10)

story = [
    Paragraph("DIEGO DE LA FUENTE ALONSO", name_style),
    Paragraph("Data Scientist &amp; Data Analyst | Python (Pandas, NumPy, scikit-learn) · Machine Learning · SQL · BigQuery", role_style),
    Paragraph("España (100% Remoto / Valladolid - Madrid)  |  (+34) 626 68 71 79  |  diegodelafuentealonso@gmail.com", contact_style),
    HRFlowable(width="100%", thickness=0.8, color=colors.HexColor("#D1D5DB"), spaceBefore=2, spaceAfter=14),
    Paragraph("3 de noviembre de 2026", meta_style),
    Paragraph("Para: Equipo de Selección y Área de Data &amp; Analytics — Logicalis Spain", meta_style),
    Paragraph("Asunto: Candidatura a la vacante de Data Scientist (100% Remoto)", subject_style),
    Paragraph("Estimado equipo de Selección y área de Data &amp; Analytics de Logicalis Spain,", body_style),
    Paragraph(
        "Les escribo para presentar mi candidatura a la posición de Data Scientist (100% Remoto) publicada en su portal de empleo. "
        "Mi perfil combina una base específica en Ciencia de Datos e Inteligencia Artificial con experiencia práctica en producción tratando, "
        "transformando y explotando datos con Python y SQL para dar respuesta a necesidades reales de negocio.",
        body_style
    ),
    Paragraph(
        "En mi puesto actual en HORSE Technologies y a través de mi Especialización en Inteligencia Artificial y Big Data, trabajo directamente "
        "con las herramientas y metodologías que solicitan para su equipo de Data &amp; AI:",
        body_style
    ),
    Paragraph(
        "• Desarrollo y evaluación de modelos de Machine Learning con Python: Utilizo Python junto con librerías científicas como Pandas, NumPy "
        "y scikit-learn para el análisis exploratorio de datos (EDA), ingeniería de características, entrenamiento de modelos predictivos "
        "y validación mediante métricas estadísticas rigurosas.",
        bullet_style
    ),
    Paragraph(
        "• Análisis, transformación y tratamiento de datos multi-fuente (SQL y Cloud): En HORSE Technologies preparo, limpio y transformo grandes "
        "volúmenes de información procedentes de distintas fuentes mediante Python, SQL avanzado sobre Google BigQuery y pipelines declarativos en Dataform, "
        "asegurando la calidad del dato antes de su explotación analítica o modelado.",
        bullet_style
    ),
    Paragraph(
        "• Ciclo de vida completo, buenas prácticas y versionado con Git: Participo en todas las fases del ciclo de vida del dato y de los modelos "
        "—desde la exploración y diseño hasta su integración en producción y visualización en Looker—, trabajando de forma colaborativa con equipos "
        "de Data &amp; AI mediante Git (GitFlow) y estándares de código limpio.",
        bullet_style
    ),
    Spacer(1, 3),
    Paragraph(
        "Cuento con el Curso de Especialización en Inteligencia Artificial y Big Data y doble titulación superior en desarrollo de software (DAM y DAW), "
        "lo que me permite no solo construir y evaluar modelos en notebooks, sino también empaquetarlos y llevarlos a producción con solvencia técnica.",
        body_style
    ),
    Paragraph(
        "Resido en Valladolid, con disponibilidad total para trabajar en modalidad 100% remota desde España y cercanía directa a las oficinas de Madrid "
        "(a menos de una hora en AVE). Mi disponibilidad de incorporación es de 15 días naturales (preaviso legal estándar).",
        body_style
    ),
    Paragraph(
        "Agradezco de antemano su tiempo y consideración. Quedo a su entera disposición para ampliar cualquier detalle técnico en una entrevista.",
        body_style
    ),
    Paragraph(
        "Atentamente,<br/><br/>"
        "Diego de la Fuente Alonso<br/>"
        "Data Scientist &amp; Data / AI Developer<br/>"
        "(+34) 626 68 71 79  |  diegodelafuentealonso@gmail.com",
        sign_style
    )
]

doc.build(story)
print("Created PDF:", out_path)
