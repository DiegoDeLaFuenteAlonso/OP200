from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable

out_path = "C:/Users/DELAFUENTEALONSODieg/empleo/postulaciones/metrica-devsecops-junior/Diego_de_la_Fuente_Alonso_Carta_Presentacion_Metrica_DevSecOps_Junior.pdf"

doc = SimpleDocTemplate(
    out_path,
    pagesize=A4,
    leftMargin=22*mm,
    rightMargin=22*mm,
    topMargin=18*mm,
    bottomMargin=18*mm,
    title="Carta de Presentación - Diego de la Fuente Alonso - Métrica España DevSecOps Junior",
    author="Diego de la Fuente Alonso"
)

styles = getSampleStyleSheet()

name_style = ParagraphStyle("NameHeader", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=16, leading=20, textColor=colors.HexColor("#111827"), spaceAfter=2)
role_style = ParagraphStyle("RoleHeader", parent=styles["Normal"], fontName="Helvetica", fontSize=9.8, leading=13.5, textColor=colors.HexColor("#1F2937"), spaceAfter=3)
contact_style = ParagraphStyle("ContactHeader", parent=styles["Normal"], fontName="Helvetica", fontSize=9.5, leading=13, textColor=colors.HexColor("#4B5563"), spaceAfter=8)
meta_style = ParagraphStyle("MetaText", parent=styles["Normal"], fontName="Helvetica", fontSize=9.8, leading=13.5, textColor=colors.HexColor("#1F2937"), spaceAfter=5)
subject_style = ParagraphStyle("SubjectText", parent=styles["Normal"], fontName="Helvetica", fontSize=10, leading=14.5, textColor=colors.HexColor("#111827"), spaceBefore=4, spaceAfter=10)
body_style = ParagraphStyle("BodyJustified", parent=styles["Normal"], fontName="Helvetica", fontSize=9.8, leading=14.5, alignment=TA_JUSTIFY, textColor=colors.HexColor("#1F2937"), spaceAfter=8)
bullet_style = ParagraphStyle("BulletItem", parent=styles["Normal"], fontName="Helvetica", fontSize=9.6, leading=14, alignment=TA_JUSTIFY, leftIndent=12, firstLineIndent=-8, textColor=colors.HexColor("#1F2937"), spaceAfter=5.5)
sign_style = ParagraphStyle("Signature", parent=styles["Normal"], fontName="Helvetica", fontSize=9.8, leading=13.5, textColor=colors.HexColor("#111827"), spaceBefore=8)

story = [
    Paragraph("DIEGO DE LA FUENTE ALONSO", name_style),
    Paragraph("DevSecOps &amp; Backend Developer Junior | CI/CD (GitHub Actions) · Python/Bash/PowerShell · Docker · APIs REST · SQL/PostgreSQL", role_style),
    Paragraph("España (100% Remoto / Valladolid)  |  (+34) 626 68 71 79  |  diegodelafuentealonso@gmail.com", contact_style),
    HRFlowable(width="100%", thickness=0.8, color=colors.HexColor("#D1D5DB"), spaceBefore=2, spaceAfter=12),
    Paragraph("3 de noviembre de 2026", meta_style),
    Paragraph("Para: Equipo de Selección y Squad de Desarrollo — Métrica España", meta_style),
    Paragraph("Asunto: Candidatura a DevSecOps Junior 100% Remoto (y Desarrollador Back Junior)", subject_style),
    Paragraph("Estimado equipo de Selección de Métrica España,", body_style),
    Paragraph(
        "Les escribo para presentar mi candidatura a la posición de DevSecOps Junior 100% Remoto (así como a su vacante de Desarrollador Back Junior en remoto) "
        "publicada en su portal de empleo. Cuento con más de un año de experiencia práctica acumulada en desarrollo de software, automatización de procesos, "
        "gestión de pasos entre entornos y administración de APIs y bases de datos SQL, lo que encaja directamente con el perfil de 0,5 a 1 año que buscan "
        "para su Squad de Desarrollo.",
        body_style
    ),
    Paragraph(
        "A lo largo de mi trayectoria actual en HORSE Technologies y mis etapas previas en FDS (DXC Technology), el Ayuntamiento de Roperuelos del Páramo y Craftelier, "
        "he trabajado de forma práctica con las tecnologías clave del puesto:",
        body_style
    ),
    Paragraph(
        "• Automatización, scripting y CI/CD con GitHub Actions: Desarrollo scripts y utilidades de automatización en Python, Go, Bash y PowerShell sobre entornos "
        "tanto Linux como Windows, utilizando Git y GitHub (incluyendo flujos de integración continua con GitHub Actions y contenedores Docker) para estandarizar "
        "pruebas y despliegues.",
        bullet_style
    ),
    Paragraph(
        "• Gestión de despliegues, entornos y seguridad (DevSecOps): En FDS (DXC Technology) gestioné y validé el transporte de software entre entornos de Desarrollo, "
        "Calidad y Producción (DEV, QAS, PRD). Asimismo, en mis integraciones de servicios y agentes aplico buenas prácticas de gestión de credenciales y secretos, "
        "principio de mínimo privilegio y monitorización de logs y trazas.",
        bullet_style
    ),
    Paragraph(
        "• Uso y administración de APIs REST, SQL y PostgreSQL: Poseo sólida experiencia diseñando, consumiendo y asegurando APIs RESTful (en Python y Java Spring Boot) "
        "y trabajando con bases de datos relacionales SQL y PostgreSQL.",
        bullet_style
    ),
    Spacer(1, 2),
    Paragraph(
        "Cuento con doble titulación de Grado Superior en Desarrollo de Aplicaciones Web (DAW) y Multiplataforma (DAM), además del Curso de Especialización en "
        "Inteligencia Artificial y Big Data. Resido en Valladolid (España), me adapto perfectamente al horario de 7:30 a 15:30 en modalidad 100% remota y tengo "
        "disponibilidad para realizar guardias en caso de que el proyecto lo requiera en el futuro. Mi preaviso de incorporación es de 15 días naturales.",
        body_style
    ),
    Paragraph(
        "Agradezco de antemano su tiempo y consideración. Quedo a su entera disposición para mantener una entrevista técnica.",
        body_style
    ),
    Paragraph(
        "Atentamente,<br/><br/>"
        "Diego de la Fuente Alonso<br/>"
        "DevSecOps &amp; Backend Developer Junior (Python / CI-CD / Docker / SQL / Java)<br/>"
        "(+34) 626 68 71 79  |  diegodelafuentealonso@gmail.com",
        sign_style
    )
]

doc.build(story)
print("Created PDF:", out_path)
