from __future__ import annotations

import html
import re
import sys
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    LongTable,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


NAVY = colors.HexColor("#17365D")
BLUE = colors.HexColor("#DCE6F1")
PALE = colors.HexColor("#F3F6F9")
GRID = colors.HexColor("#AEB8C2")
TEXT = colors.HexColor("#20252A")


def esc(value: str) -> str:
    value = value.replace("  ", " ").strip()
    value = re.sub(r"`([^`]+)`", r"\1", value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"\1", value)
    return html.escape(value, quote=False)


def register_fonts() -> tuple[str, str]:
    regular = Path(r"C:\Windows\Fonts\NotoSansJP-VF.ttf")
    bold_candidates = [
        Path(r"C:\Windows\Fonts\YuGothB.ttc"),
        Path(r"C:\Windows\Fonts\meiryob.ttc"),
    ]
    pdfmetrics.registerFont(TTFont("JP", str(regular)))
    bold_name = "JP"
    for candidate in bold_candidates:
        if candidate.exists():
            try:
                pdfmetrics.registerFont(TTFont("JPBold", str(candidate)))
                bold_name = "JPBold"
                break
            except Exception:
                pass
    return "JP", bold_name


FONT, FONT_BOLD = register_fonts()


def styles():
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "TitleJP",
            parent=base["Title"],
            fontName=FONT_BOLD,
            fontSize=18,
            leading=23,
            alignment=TA_CENTER,
            textColor=NAVY,
            spaceAfter=5 * mm,
            wordWrap="CJK",
        ),
        "meta": ParagraphStyle(
            "MetaJP",
            fontName=FONT,
            fontSize=8.5,
            leading=12,
            alignment=TA_RIGHT,
            textColor=TEXT,
            wordWrap="CJK",
        ),
        "body": ParagraphStyle(
            "BodyJP",
            fontName=FONT,
            fontSize=8.5,
            leading=13,
            textColor=TEXT,
            spaceAfter=2.2 * mm,
            wordWrap="CJK",
            splitLongWords=True,
        ),
        "bullet": ParagraphStyle(
            "BulletJP",
            fontName=FONT,
            fontSize=8.3,
            leading=12.2,
            textColor=TEXT,
            leftIndent=4.5 * mm,
            firstLineIndent=-3.3 * mm,
            spaceAfter=0.8 * mm,
            wordWrap="CJK",
            splitLongWords=True,
        ),
        "label": ParagraphStyle(
            "LabelJP",
            fontName=FONT_BOLD,
            fontSize=8.8,
            leading=12,
            textColor=NAVY,
            spaceBefore=1.5 * mm,
            spaceAfter=1.2 * mm,
            keepWithNext=True,
            wordWrap="CJK",
        ),
        "h3": ParagraphStyle(
            "H3JP",
            fontName=FONT_BOLD,
            fontSize=10.1,
            leading=14,
            textColor=NAVY,
            wordWrap="CJK",
        ),
        "cell": ParagraphStyle(
            "CellJP",
            fontName=FONT,
            fontSize=7.3,
            leading=10.2,
            textColor=TEXT,
            wordWrap="CJK",
            splitLongWords=True,
        ),
        "cell_bold": ParagraphStyle(
            "CellBoldJP",
            fontName=FONT_BOLD,
            fontSize=7.3,
            leading=10.2,
            textColor=TEXT,
            wordWrap="CJK",
            splitLongWords=True,
        ),
        "cell_head": ParagraphStyle(
            "CellHeadJP",
            fontName=FONT_BOLD,
            fontSize=7.5,
            leading=10.5,
            textColor=colors.white,
            alignment=TA_CENTER,
            wordWrap="CJK",
        ),
    }


S = styles()


def section_header(text: str) -> Table:
    t = Table([[Paragraph(esc(text), S["h3"])]], colWidths=[184 * mm])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), BLUE),
                ("BOX", (0, 0), (-1, -1), 0.5, NAVY),
                ("LEFTPADDING", (0, 0), (-1, -1), 2.2 * mm),
                ("RIGHTPADDING", (0, 0), (-1, -1), 2 * mm),
                ("TOPPADDING", (0, 0), (-1, -1), 1.3 * mm),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5 * mm),
            ]
        )
    )
    t.spaceBefore = 2.3 * mm
    t.spaceAfter = 1.8 * mm
    t.keepWithNext = True
    return t


def major_header(text: str) -> Table:
    p = Paragraph(esc(text), ParagraphStyle(
        "MajorJP", fontName=FONT_BOLD, fontSize=11.2, leading=15,
        textColor=colors.white, wordWrap="CJK"
    ))
    t = Table([[p]], colWidths=[184 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("LEFTPADDING", (0, 0), (-1, -1), 2.5 * mm),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2 * mm),
        ("TOPPADDING", (0, 0), (-1, -1), 1.5 * mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1.7 * mm),
    ]))
    t.spaceBefore = 3 * mm
    t.spaceAfter = 2 * mm
    t.keepWithNext = True
    return t


def parse_table(lines: list[str]) -> list[list[str]]:
    rows = []
    for line in lines:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells and all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in cells):
            continue
        rows.append(cells)
    return rows


def make_table(rows: list[list[str]]) -> LongTable:
    n = max(len(r) for r in rows)
    for row in rows:
        row.extend([""] * (n - len(row)))
    if n == 4:
        widths = [21 * mm, 43 * mm, 28 * mm, 92 * mm]
    elif n == 2:
        first_values = [r[0] for r in rows[1:]]
        if any("資格" in x or "年月" in x for x in rows[0]):
            widths = [35 * mm, 149 * mm]
        elif all(len(x) <= 12 for x in first_values):
            widths = [31 * mm, 153 * mm]
        else:
            widths = [42 * mm, 142 * mm]
    else:
        widths = [184 * mm / n] * n

    data = []
    for ri, row in enumerate(rows):
        formatted = []
        for ci, value in enumerate(row):
            style = S["cell_head"] if ri == 0 else (S["cell_bold"] if n == 2 and ci == 0 else S["cell"])
            formatted.append(Paragraph(esc(value), style))
        data.append(formatted)

    t = LongTable(data, colWidths=widths, repeatRows=1, splitByRow=1, hAlign="LEFT")
    commands = [
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("GRID", (0, 0), (-1, -1), 0.35, GRID),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 1.5 * mm),
        ("RIGHTPADDING", (0, 0), (-1, -1), 1.5 * mm),
        ("TOPPADDING", (0, 0), (-1, -1), 1.1 * mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1.2 * mm),
    ]
    for ri in range(1, len(data)):
        if ri % 2 == 0:
            commands.append(("BACKGROUND", (0, ri), (-1, ri), PALE))
    if n == 2:
        commands.append(("BACKGROUND", (0, 1), (0, -1), BLUE))
    t.setStyle(TableStyle(commands))
    t.spaceBefore = 0.8 * mm
    t.spaceAfter = 2.3 * mm
    return t


def markdown_to_story(text: str):
    lines = text.splitlines()
    story = []
    i = 0
    before_first_h2 = True
    paragraph_parts: list[str] = []

    def flush_paragraph():
        nonlocal paragraph_parts
        if not paragraph_parts:
            return
        value = " ".join(p.strip() for p in paragraph_parts if p.strip())
        if value:
            if before_first_h2:
                style = S["meta"]
            elif re.fullmatch(r"【[^】]+】", value):
                style = S["label"]
            else:
                style = S["body"]
            story.append(Paragraph(esc(value), style))
        paragraph_parts = []

    while i < len(lines):
        raw = lines[i].rstrip()
        stripped = raw.strip()
        if not stripped:
            flush_paragraph()
            i += 1
            continue
        if stripped.startswith("| ") or (stripped.startswith("|") and stripped.endswith("|")):
            flush_paragraph()
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i].strip())
                i += 1
            story.append(make_table(parse_table(table_lines)))
            continue
        if stripped.startswith("### "):
            flush_paragraph()
            story.append(section_header(stripped[4:]))
            i += 1
            continue
        if stripped.startswith("## "):
            flush_paragraph()
            before_first_h2 = False
            story.append(major_header(stripped[3:]))
            i += 1
            continue
        if stripped.startswith("# "):
            flush_paragraph()
            story.append(Paragraph(esc(stripped[2:]), S["title"]))
            i += 1
            continue
        if stripped.startswith("- "):
            flush_paragraph()
            story.append(Paragraph("・" + esc(stripped[2:]), S["bullet"]))
            i += 1
            continue
        if stripped.startswith("> "):
            flush_paragraph()
            story.append(Paragraph(esc(stripped[2:]), S["body"]))
            i += 1
            continue
        paragraph_parts.append(stripped)
        i += 1
    flush_paragraph()
    return story


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(GRID)
    canvas.setLineWidth(0.3)
    canvas.line(13 * mm, 10 * mm, 197 * mm, 10 * mm)
    canvas.setFont(FONT, 7)
    canvas.setFillColor(colors.HexColor("#5C6570"))
    canvas.drawString(13 * mm, 6.5 * mm, "職務経歴書 - 宇野 拓磨")
    canvas.drawRightString(197 * mm, 6.5 * mm, f"{doc.page}")
    canvas.restoreState()


def build(source: Path, output: Path):
    output.parent.mkdir(parents=True, exist_ok=True)
    doc = BaseDocTemplate(
        str(output),
        pagesize=A4,
        leftMargin=13 * mm,
        rightMargin=13 * mm,
        topMargin=12 * mm,
        bottomMargin=14 * mm,
        title="職務経歴書",
        author="宇野 拓磨",
        subject="職務経歴書",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
    doc.addPageTemplates([PageTemplate(id="career", frames=[frame], onPage=footer)])
    story = markdown_to_story(source.read_text(encoding="utf-8"))
    doc.build(story)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("usage: make_career_pdf.py INPUT.md OUTPUT.pdf")
    build(Path(sys.argv[1]), Path(sys.argv[2]))
