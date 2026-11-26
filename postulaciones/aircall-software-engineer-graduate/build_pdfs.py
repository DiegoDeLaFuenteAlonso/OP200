import json
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable

styles = getSampleStyleSheet()
base_dir = "C:/Users/DELAFUENTEALONSODieg/empleo/postulaciones/aircall-software-engineer-graduate"

# 1. Generate 1-page CV PDF with fully justified body & bullet text (TA_JUSTIFY)
with open(f"{base_dir}/cv_spec.json", "r", encoding="utf-8") as f:
    spec = json.load(f)

cv_pdf_path = f"{base_dir}/Diego_de_la_Fuente_Alonso_CV_Aircall_Software_Engineer_Graduate.pdf"
cv_doc = SimpleDocTemplate(
    cv_pdf_path,
    pagesize=A4,
    leftMargin=15*mm,
    rightMargin=15*mm,
    topMargin=12*mm,
    bottomMargin=12*mm,
    title="CV - Diego de la Fuente Alonso - Software Engineer Graduate (Aircall)",
    author="Diego de la Fuente Alonso"
)

s_title = ParagraphStyle("CVT", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=15.5, leading=18.5, textColor=colors.HexColor("#111827"), spaceAfter=2)
s_sub = ParagraphStyle("CVS", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=9.2, leading=12.0, textColor=colors.HexColor("#1F2937"), spaceAfter=2)
s_con = ParagraphStyle("CVC", parent=styles["Normal"], fontName="Helvetica", fontSize=8.6, leading=11.2, textColor=colors.HexColor("#4B5563"), spaceAfter=5)
s_head = ParagraphStyle("CVH", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=9.8, leading=12.5, textColor=colors.HexColor("#111827"), spaceBefore=4.8, spaceAfter=2)
s_job = ParagraphStyle("CVJ", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=9.0, leading=11.5, textColor=colors.HexColor("#111827"), spaceBefore=3.0, spaceAfter=0.8)
s_date = ParagraphStyle("CVD", parent=styles["Normal"], fontName="Helvetica-Oblique", fontSize=8.3, leading=10.8, textColor=colors.HexColor("#4B5563"), spaceAfter=1.8)
s_body = ParagraphStyle("CVB", parent=styles["Normal"], fontName="Helvetica", fontSize=8.5, leading=11.4, alignment=TA_JUSTIFY, textColor=colors.HexColor("#1F2937"), spaceAfter=2.8)
s_bul = ParagraphStyle("CVBul", parent=styles["Normal"], fontName="Helvetica", fontSize=8.4, leading=11.1, alignment=TA_JUSTIFY, leftIndent=10, firstLineIndent=-6, textColor=colors.HexColor("#1F2937"), spaceAfter=1.8)

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
            cv_story.append(HRFlowable(width="100%", thickness=0.6, color=colors.HexColor("#D1D5DB"), spaceBefore=1, spaceAfter=3.5))
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
cl_path = f"{base_dir}/Diego_de_la_Fuente_Alonso_Cover_Letter_Aircall_Software_Engineer_Graduate.pdf"
cl_doc = SimpleDocTemplate(
    cl_path,
    pagesize=A4,
    leftMargin=22*mm,
    rightMargin=22*mm,
    topMargin=17*mm,
    bottomMargin=17*mm,
    title="Cover Letter - Diego de la Fuente Alonso - Aircall Software Engineer Graduate",
    author="Diego de la Fuente Alonso"
)

name_style = ParagraphStyle("NameHeader", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=16, leading=20, textColor=colors.HexColor("#111827"), spaceAfter=2)
role_style = ParagraphStyle("RoleHeader", parent=styles["Normal"], fontName="Helvetica", fontSize=9.6, leading=13.2, textColor=colors.HexColor("#1F2937"), spaceAfter=3)
contact_style = ParagraphStyle("ContactHeader", parent=styles["Normal"], fontName="Helvetica", fontSize=9.4, leading=13, textColor=colors.HexColor("#4B5563"), spaceAfter=8)
meta_style = ParagraphStyle("MetaText", parent=styles["Normal"], fontName="Helvetica", fontSize=9.8, leading=13.5, textColor=colors.HexColor("#1F2937"), spaceAfter=4.5)
subject_style = ParagraphStyle("SubjectText", parent=styles["Normal"], fontName="Helvetica", fontSize=9.8, leading=14.2, textColor=colors.HexColor("#111827"), spaceBefore=4, spaceAfter=10)
body_style = ParagraphStyle("BodyJustified", parent=styles["Normal"], fontName="Helvetica", fontSize=9.7, leading=14.0, alignment=TA_JUSTIFY, textColor=colors.HexColor("#1F2937"), spaceAfter=7.5)
bullet_style = ParagraphStyle("BulletItem", parent=styles["Normal"], fontName="Helvetica", fontSize=9.5, leading=13.5, alignment=TA_JUSTIFY, leftIndent=12, firstLineIndent=-8, textColor=colors.HexColor("#1F2937"), spaceAfter=5.5)
sign_style = ParagraphStyle("Signature", parent=styles["Normal"], fontName="Helvetica", fontSize=9.8, leading=13.5, textColor=colors.HexColor("#111827"), spaceBefore=8)

cl_story = [
    Paragraph("DIEGO DE LA FUENTE ALONSO", name_style),
    Paragraph("Software Engineer – Graduate | Python · Java · Go · TypeScript/JS · REST APIs · SQL · AI/LLM Systems", role_style),
    Paragraph("Spain (Available Hybrid in Madrid)  |  (+34) 626 68 71 79  |  diegodelafuentealonso@gmail.com", contact_style),
    HRFlowable(width="100%", thickness=0.8, color=colors.HexColor("#D1D5DB"), spaceBefore=2, spaceAfter=11),
    Paragraph("November 16, 2026", meta_style),
    Paragraph("To: Aircall Talent Acquisition &amp; Engineering Team (Madrid Office)", meta_style),
    Paragraph("Subject: Application for Software Engineer – Graduate (6-month Professional Practice Contract)", subject_style),
    Paragraph("Dear Aircall Engineering &amp; Talent Team,", body_style),
    Paragraph(
        "I am writing to apply for the Software Engineer – Graduate (6-month Professional Practice Contract) position in your Madrid office. "
        "Having recently completed my Higher VET (FP Grado Superior) in Web Application Development (DAW, 2026), following my Specialization "
        "in Artificial Intelligence &amp; Big Data (2025) and Higher VET in Multi-Platform Application Development (DAM, 2024), I meet all formal "
        "eligibility requirements for the Spanish contrato formativo para la obtención de la práctica profesional and am excited by the "
        "opportunity to contribute to a product-driven team with a clear path toward a permanent role.",
        body_style
    ),
    Paragraph(
        "What draws me most to Aircall is the intersection of reliable backend engineering, real-time customer communications, and practical "
        "AI features—particularly across teams such as Conversational Intelligence, Agent Productivity, and Data Platform. Across my recent "
        "professional and academic experience, I have worked directly across these layers:",
        body_style
    ),
    Paragraph(
        "• Backend &amp; Multi-Language Engineering Fundamentals: Across my roles at HORSE Technologies, Ayuntamiento de Roperuelos del Páramo, "
        "and Craftelier, I have built backend services, RESTful APIs, and internal tooling in Python, Go, Java (Spring Boot), and C# (.NET), "
        "alongside web development in JavaScript/TypeScript, HTML5, CSS3, and Angular. I am eager to ramp up quickly on Aircall's "
        "TypeScript/Node.js and AWS stack while contributing immediately through Python, clean APIs, testing, and Git workflows.",
        bullet_style
    ),
    Paragraph(
        "• Hands-On Experience with Data Platform &amp; AI/LLM Systems: At HORSE Technologies, I engineered automated Python ETL pipelines, "
        "declarative SQL data models in Google BigQuery and Dataform, and Looker analytics, while building AI agent harnesses, deterministic "
        "loop engineering patterns, and Model Context Protocol (MCP) integrations. Having also explored speech synthesis and LLM workflows "
        "in side projects, Aircall's focus on AI Voice Agents and Conversational Intelligence strongly aligns with my interests.",
        bullet_style
    ),
    Paragraph(
        "• Production Discipline &amp; Hybrid Collaboration: Working in enterprise delivery teams at DXC Technology (FDS) and HORSE Technologies "
        "has trained me in code quality, structured DEV/QAS/PRD release cycles, observability, and clear technical communication in English "
        "and Spanish. I am fully comfortable working hybrid 3 days per week in Aircall's Madrid office and hold full EU work authorization.",
        bullet_style
    ),
    Spacer(1, 2),
    Paragraph(
        "Thank you very much for your time and consideration. I would welcome the opportunity to discuss how my software engineering "
        "background, AI/data curiosity, and eagerness to learn can add value to Aircall's engineering teams.",
        body_style
    ),
    Paragraph(
        "Sincerely,<br/><br/>"
        "Diego de la Fuente Alonso<br/>"
        "Software Engineer – Graduate (Python / Java / Go / TypeScript / SQL / AI &amp; Data)<br/>"
        "(+34) 626 68 71 79  |  diegodelafuentealonso@gmail.com",
        sign_style
    )
]

cl_doc.build(cl_story)
print("Created Cover Letter PDF:", cl_path)
