#!/usr/bin/env python3
"""
Motor ATS de renderizado y validación (PDF + DOCX) para postulaciones/<slug>/.
Ejecutar con:
  uv run --with reportlab --with python-docx --with pypdf python .agents/skills/empleo-kit-ats/scripts/render_ats_kit.py postulaciones/<slug>
"""
import argparse
import json
import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Mm, Pt, RGBColor
from pypdf import PdfReader
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer


def xml_escape(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def strip_bold_markup(text: str) -> str:
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"</?b>", "", text, flags=re.I)
    text = re.sub(r"</?strong>", "", text, flags=re.I)
    return text


def build_cv_pdf(spec: dict, out_pdf: Path, scale: float = 1.0) -> None:
    styles = getSampleStyleSheet()
    margin_h = 15.5 * mm
    margin_v = (12.5 * scale) * mm
    doc = SimpleDocTemplate(
        str(out_pdf),
        pagesize=A4,
        leftMargin=margin_h,
        rightMargin=margin_h,
        topMargin=margin_v,
        bottomMargin=margin_v,
        title=f"CV - Diego de la Fuente Alonso ({out_pdf.stem})",
        author="Diego de la Fuente Alonso",
    )

    s_title = ParagraphStyle("CVT", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=15.8 * scale, leading=18.8 * scale, textColor=colors.HexColor("#111827"), spaceAfter=2 * scale)
    s_sub = ParagraphStyle("CVS", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=9.2 * scale, leading=12.0 * scale, textColor=colors.HexColor("#1F2937"), spaceAfter=2 * scale)
    s_con = ParagraphStyle("CVC", parent=styles["Normal"], fontName="Helvetica", fontSize=8.6 * scale, leading=11.2 * scale, textColor=colors.HexColor("#4B5563"), spaceAfter=5 * scale)
    s_head = ParagraphStyle("CVH", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=9.8 * scale, leading=12.5 * scale, textColor=colors.HexColor("#111827"), spaceBefore=4.8 * scale, spaceAfter=2 * scale)
    s_job = ParagraphStyle("CVJ", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=9.0 * scale, leading=11.5 * scale, textColor=colors.HexColor("#111827"), spaceBefore=3.0 * scale, spaceAfter=0.8 * scale)
    s_date = ParagraphStyle("CVD", parent=styles["Normal"], fontName="Helvetica-Oblique", fontSize=8.3 * scale, leading=10.8 * scale, textColor=colors.HexColor("#4B5563"), spaceAfter=1.8 * scale)
    s_body = ParagraphStyle("CVB", parent=styles["Normal"], fontName="Helvetica", fontSize=8.5 * scale, leading=11.4 * scale, alignment=TA_JUSTIFY, textColor=colors.HexColor("#1F2937"), spaceAfter=2.8 * scale)
    s_bul = ParagraphStyle("CVBul", parent=styles["Normal"], fontName="Helvetica", fontSize=8.4 * scale, leading=11.1 * scale, alignment=TA_JUSTIFY, leftIndent=10, firstLineIndent=-6, textColor=colors.HexColor("#1F2937"), spaceAfter=1.8 * scale)

    story = []
    for b in spec["blocks"]:
        if b["type"] == "paragraph":
            st = b.get("style", "CVBody")
            txt = xml_escape(b["text"])
            if st == "CVTitle":
                story.append(Paragraph(txt, s_title))
            elif st == "CVSubtitle":
                story.append(Paragraph(txt, s_sub))
            elif st == "CVContact":
                story.append(Paragraph(txt, s_con))
                story.append(HRFlowable(width="100%", thickness=0.6, color=colors.HexColor("#D1D5DB"), spaceBefore=1, spaceAfter=3.5 * scale))
            elif st == "CVHeading":
                story.append(Paragraph(txt, s_head))
            elif st == "CVJobHeader":
                story.append(Paragraph(txt, s_job))
            elif st == "CVJobDate":
                story.append(Paragraph(txt, s_date))
            else:
                story.append(Paragraph(txt, s_body))
        elif b["type"] == "bullet_list":
            for it in b["items"]:
                clean_it = strip_bold_markup(it)
                story.append(Paragraph("• " + xml_escape(clean_it), s_bul))

    doc.build(story)


def build_cv_docx(spec: dict, out_docx: Path) -> None:
    doc = Document()
    section = doc.sections[0]
    section.page_width = Mm(210)
    section.page_height = Mm(297)
    section.top_margin = Mm(14)
    section.bottom_margin = Mm(14)
    section.left_margin = Mm(16)
    section.right_margin = Mm(16)

    for b in spec["blocks"]:
        if b["type"] == "paragraph":
            st = b.get("style", "CVBody")
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(2)
            run = p.add_run(strip_bold_markup(b["text"]))
            run.font.name = "Calibri"
            if st == "CVTitle":
                run.bold = True
                run.font.size = Pt(17)
                run.font.color.rgb = RGBColor(0x11, 0x18, 0x27)
            elif st == "CVSubtitle":
                run.bold = True
                run.font.size = Pt(10.5)
                run.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)
            elif st == "CVContact":
                run.font.size = Pt(9)
                run.font.color.rgb = RGBColor(0x4B, 0x55, 0x63)
                p.paragraph_format.space_after = Pt(5)
            elif st == "CVHeading":
                run.bold = True
                run.font.size = Pt(11)
                run.font.color.rgb = RGBColor(0x00, 0x33, 0x66)
                p.paragraph_format.space_before = Pt(5)
                p.paragraph_format.space_after = Pt(2)
            elif st == "CVJobHeader":
                run.bold = True
                run.font.size = Pt(10)
                run.font.color.rgb = RGBColor(0x11, 0x18, 0x27)
                p.paragraph_format.space_before = Pt(3.5)
                p.paragraph_format.space_after = Pt(0.5)
            elif st == "CVJobDate":
                run.italic = True
                run.font.size = Pt(8.8)
                run.font.color.rgb = RGBColor(0x4B, 0x55, 0x63)
                p.paragraph_format.space_after = Pt(1.5)
            else:
                run.font.size = Pt(9.3)
                run.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)
                p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                p.paragraph_format.space_after = Pt(3)
        elif b["type"] == "bullet_list":
            for it in b["items"]:
                p = doc.add_paragraph(style="List Bullet")
                p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                p.paragraph_format.space_before = Pt(0)
                p.paragraph_format.space_after = Pt(1.5)
                run = p.add_run(strip_bold_markup(it))
                run.font.name = "Calibri"
                run.font.size = Pt(9.2)
                run.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)

    doc.save(str(out_docx))


def build_cover_letter_pdf(cl: dict, out_pdf: Path, scale: float = 1.0) -> None:
    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(
        str(out_pdf),
        pagesize=A4,
        leftMargin=22 * mm,
        rightMargin=22 * mm,
        topMargin=(17.5 * scale) * mm,
        bottomMargin=(17.5 * scale) * mm,
        title=f"Carta de Presentación - Diego de la Fuente Alonso ({out_pdf.stem})",
        author="Diego de la Fuente Alonso",
    )

    name_st = ParagraphStyle("NH", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=16 * scale, leading=20 * scale, textColor=colors.HexColor("#111827"), spaceAfter=2 * scale)
    role_st = ParagraphStyle("RH", parent=styles["Normal"], fontName="Helvetica", fontSize=9.6 * scale, leading=13.2 * scale, textColor=colors.HexColor("#1F2937"), spaceAfter=3 * scale)
    con_st = ParagraphStyle("CH", parent=styles["Normal"], fontName="Helvetica", fontSize=9.4 * scale, leading=13 * scale, textColor=colors.HexColor("#4B5563"), spaceAfter=8 * scale)
    meta_st = ParagraphStyle("MT", parent=styles["Normal"], fontName="Helvetica", fontSize=9.8 * scale, leading=13.5 * scale, textColor=colors.HexColor("#1F2937"), spaceAfter=4.5 * scale)
    subj_st = ParagraphStyle("ST", parent=styles["Normal"], fontName="Helvetica", fontSize=9.9 * scale, leading=14.2 * scale, textColor=colors.HexColor("#111827"), spaceBefore=4 * scale, spaceAfter=10 * scale)
    body_st = ParagraphStyle("BJ", parent=styles["Normal"], fontName="Helvetica", fontSize=9.7 * scale, leading=14.1 * scale, alignment=TA_JUSTIFY, textColor=colors.HexColor("#1F2937"), spaceAfter=7.5 * scale)
    bul_st = ParagraphStyle("BI", parent=styles["Normal"], fontName="Helvetica", fontSize=9.5 * scale, leading=13.6 * scale, alignment=TA_JUSTIFY, leftIndent=12, firstLineIndent=-8, textColor=colors.HexColor("#1F2937"), spaceAfter=5.5 * scale)
    sign_st = ParagraphStyle("SG", parent=styles["Normal"], fontName="Helvetica", fontSize=9.8 * scale, leading=13.5 * scale, textColor=colors.HexColor("#111827"), spaceBefore=8 * scale)

    story = [
        Paragraph("DIEGO DE LA FUENTE ALONSO", name_st),
        Paragraph(xml_escape(strip_bold_markup(cl["role_header"])), role_st),
        Paragraph(xml_escape(strip_bold_markup(cl["contact_header"])), con_st),
        HRFlowable(width="100%", thickness=0.8, color=colors.HexColor("#D1D5DB"), spaceBefore=2, spaceAfter=11 * scale),
        Paragraph(xml_escape(strip_bold_markup(cl["date"])), meta_st),
        Paragraph(xml_escape(strip_bold_markup(cl["recipient"])), meta_st),
        Paragraph(xml_escape(strip_bold_markup(cl["subject"])), subj_st),
        Paragraph(xml_escape(strip_bold_markup(cl["salutation"])), body_st),
    ]
    for p in cl.get("opening_paragraphs", []):
        story.append(Paragraph(xml_escape(strip_bold_markup(p)), body_st))
    for b in cl.get("bullets", []):
        clean_b = strip_bold_markup(b).lstrip("•*- ").strip()
        story.append(Paragraph("• " + xml_escape(clean_b), bul_st))
    if cl.get("bullets"):
        story.append(Spacer(1, 2))
    for p in cl.get("closing_paragraphs", []):
        story.append(Paragraph(xml_escape(strip_bold_markup(p)), body_st))

    signoff = xml_escape(strip_bold_markup(cl.get("signoff", "Atentamente,")))
    sig_role = xml_escape(strip_bold_markup(cl.get("signature_role", cl["role_header"].split("|")[0].strip())))
    sig_contact = "(+34) 626 68 71 79  |  diegodelafuentealonso@gmail.com"
    story.append(Paragraph(f"{signoff}<br/><br/>Diego de la Fuente Alonso<br/>{sig_role}<br/>{sig_contact}", sign_st))

    doc.build(story)


def page_count(pdf_path: Path) -> int:
    return len(PdfReader(str(pdf_path)).pages)


def render_one_page(builder_fn, data: dict, out_pdf: Path) -> int:
    for scale in (1.0, 0.96, 0.92, 0.88):
        builder_fn(data, out_pdf, scale=scale)
        pages = page_count(out_pdf)
        if pages == 1:
            return 1
    return page_count(out_pdf)


def main() -> int:
    parser = argparse.ArgumentParser(description="Renderiza y valida un Kit ATS de 1 página (PDF + DOCX)")
    parser.add_argument("target_dir", type=str, help="Carpeta postulaciones/<slug>")
    parser.add_argument("--verify-only", action="store_true", help="Solo valida conteo de páginas de los PDFs existentes")
    args = parser.parse_args()

    target = Path(args.target_dir).resolve()
    if not target.exists():
        print(f"[ERROR] No existe el directorio: {target}", file=sys.stderr)
        return 1

    if args.verify_only:
        pdfs = sorted(target.glob("*.pdf"))
        if not pdfs:
            print(f"[WARN] No hay archivos PDF en {target}")
            return 1
        ok = True
        for p in pdfs:
            n = page_count(p)
            status = "OK (1 pág)" if n == 1 else f"EXCEDE ({n} págs)"
            print(f"  {p.name}: {status}")
            if n != 1:
                ok = False
        return 0 if ok else 2

    cv_spec_path = target / "cv_spec.json"
    carta_spec_path = target / "carta_spec.json"
    if not cv_spec_path.exists():
        print(f"[ERROR] Falta {cv_spec_path}", file=sys.stderr)
        return 1

    cv_spec = json.loads(cv_spec_path.read_text(encoding="utf-8"))
    carta_spec = json.loads(carta_spec_path.read_text(encoding="utf-8")) if carta_spec_path.exists() else {}

    slug_clean = re.sub(r"[^A-Za-z0-9]+", "_", target.name).strip("_")
    cv_pdf = target / carta_spec.get("output_cv_pdf", f"Diego_de_la_Fuente_Alonso_CV_{slug_clean}.pdf")
    cv_docx = target / carta_spec.get("output_cv_docx", f"Diego_de_la_Fuente_Alonso_CV_{slug_clean}.docx")

    cv_pages = render_one_page(build_cv_pdf, cv_spec, cv_pdf)
    build_cv_docx(cv_spec, cv_docx)
    print(f"[CV]    {cv_pdf.name} ({cv_pages} pág) + {cv_docx.name}")

    cl_pages = 1
    if carta_spec:
        cl_pdf = target / carta_spec.get("output_pdf", f"Diego_de_la_Fuente_Alonso_Carta_Presentacion_{slug_clean}.pdf")
        cl_pages = render_one_page(build_cover_letter_pdf, carta_spec, cl_pdf)
        print(f"[CARTA] {cl_pdf.name} ({cl_pages} pág)")

    if cv_pages != 1 or cl_pages != 1:
        print("[ERROR] Algún documento supera 1 página incluso tras auto-ajuste; recorta texto en el JSON.", file=sys.stderr)
        return 2

    return 0


if __name__ == "__main__":
    sys.exit(main())
