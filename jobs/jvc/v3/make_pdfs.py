#!/usr/bin/env python3
from pathlib import Path
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
    KeepTogether,
)


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "pdf"
def register_fonts():
    pdfmetrics.registerFont(UnicodeCIDFont("HeiseiKakuGo-W5"))
    pdfmetrics.registerFont(UnicodeCIDFont("HeiseiMin-W3"))


def styles():
    base = getSampleStyleSheet()
    for style in base.byName.values():
        style.fontName = "JP"
        style.wordWrap = "CJK"

    return {
        "title": ParagraphStyle(
            "TitleJP",
            parent=base["Title"],
            fontName="HeiseiKakuGo-W5",
            fontSize=20,
            leading=26,
            textColor=colors.HexColor("#1f3a5f"),
            alignment=TA_CENTER,
            spaceAfter=7 * mm,
            wordWrap="CJK",
        ),
        "meta": ParagraphStyle(
            "MetaJP",
            parent=base["Normal"],
            fontName="HeiseiMin-W3",
            fontSize=9,
            leading=13,
            textColor=colors.HexColor("#4b5563"),
            alignment=TA_CENTER,
            spaceAfter=5 * mm,
            wordWrap="CJK",
        ),
        "h2": ParagraphStyle(
            "H2JP",
            parent=base["Heading2"],
            fontName="HeiseiKakuGo-W5",
            fontSize=13,
            leading=18,
            textColor=colors.HexColor("#1f3a5f"),
            spaceBefore=4 * mm,
            spaceAfter=2 * mm,
            wordWrap="CJK",
        ),
        "h3": ParagraphStyle(
            "H3JP",
            parent=base["Heading3"],
            fontName="HeiseiKakuGo-W5",
            fontSize=11,
            leading=15,
            textColor=colors.HexColor("#1f2937"),
            spaceBefore=3 * mm,
            spaceAfter=1.5 * mm,
            wordWrap="CJK",
        ),
        "body": ParagraphStyle(
            "BodyJP",
            parent=base["BodyText"],
            fontName="HeiseiMin-W3",
            fontSize=9.7,
            leading=15,
            textColor=colors.HexColor("#111827"),
            spaceAfter=2.2 * mm,
            alignment=TA_LEFT,
            wordWrap="CJK",
        ),
        "small": ParagraphStyle(
            "SmallJP",
            parent=base["BodyText"],
            fontName="HeiseiMin-W3",
            fontSize=8.4,
            leading=12,
            textColor=colors.HexColor("#111827"),
            wordWrap="CJK",
        ),
        "bullet": ParagraphStyle(
            "BulletJP",
            parent=base["BodyText"],
            fontName="HeiseiMin-W3",
            fontSize=9.4,
            leading=14,
            leftIndent=5 * mm,
            firstLineIndent=-3.5 * mm,
            spaceAfter=1.2 * mm,
            wordWrap="CJK",
        ),
    }


def clean_inline(text: str) -> str:
    text = text.strip()
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", text)
    return text


def parse_table(lines, idx):
    table_lines = []
    while idx < len(lines) and lines[idx].strip().startswith("|"):
        table_lines.append(lines[idx].strip())
        idx += 1

    rows = []
    for line in table_lines:
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            continue
        rows.append(cells)
    return rows, idx


def table_flowable(rows, st, available_width):
    max_cols = max(len(row) for row in rows)
    rows = [row + [""] * (max_cols - len(row)) for row in rows]

    if max_cols == 2:
        widths = [available_width * 0.32, available_width * 0.68]
    elif max_cols == 3:
        widths = [available_width * 0.20, available_width * 0.25, available_width * 0.55]
    elif max_cols == 4:
        widths = [available_width * 0.23, available_width * 0.25, available_width * 0.25, available_width * 0.27]
    else:
        widths = [available_width / max_cols] * max_cols

    data = []
    for r, row in enumerate(rows):
        style = st["small"]
        data.append([Paragraph(clean_inline(cell).replace("<br>", "<br/>"), style) for cell in row])

    table = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("FONTNAME", (0, 0), (-1, -1), "HeiseiMin-W3"),
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e8eef6")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#1f3a5f")),
                ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#c8d2df")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
            ]
        )
    )
    return table


def md_to_flowables(md_text: str, st, available_width):
    lines = md_text.splitlines()
    story = []
    para = []
    i = 0
    saw_title = False

    def flush_para():
        if para:
            story.append(Paragraph(clean_inline("".join(para)), st["body"]))
            para.clear()

    while i < len(lines):
        raw = lines[i].rstrip()
        line = raw.strip()

        if not line:
            flush_para()
            i += 1
            continue

        if line.startswith("|"):
            flush_para()
            rows, i = parse_table(lines, i)
            story.append(table_flowable(rows, st, available_width))
            story.append(Spacer(1, 2.5 * mm))
            continue

        if line.startswith("# "):
            flush_para()
            if saw_title:
                story.append(PageBreak())
            story.append(Paragraph(clean_inline(line[2:]), st["title"]))
            saw_title = True
            i += 1
            continue

        if line.startswith("## "):
            flush_para()
            story.append(Paragraph(clean_inline(line[3:]), st["h2"]))
            i += 1
            continue

        if line.startswith("### "):
            flush_para()
            story.append(Paragraph(clean_inline(line[4:]), st["h3"]))
            i += 1
            continue

        if line.startswith("- "):
            flush_para()
            story.append(Paragraph("・" + clean_inline(line[2:]), st["bullet"]))
            i += 1
            continue

        if re.match(r"^[^:：]{1,18}[:：]\s*", line):
            flush_para()
            label, value = re.split(r"[:：]\s*", line, maxsplit=1)
            story.append(Paragraph(f"<b>{clean_inline(label)}:</b> {clean_inline(value)}", st["body"]))
            i += 1
            continue

        if para:
            para.append("<br/>" + line)
        else:
            para.append(line)
        i += 1

    flush_para()
    return story


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("HeiseiMin-W3", 8)
    canvas.setFillColor(colors.HexColor("#6b7280"))
    canvas.drawRightString(A4[0] - 18 * mm, 12 * mm, f"{doc.page}")
    canvas.restoreState()


def build_pdf(src_name, out_name):
    register_fonts()
    st = styles()
    OUT.mkdir(exist_ok=True)
    src = ROOT / src_name
    out = OUT / out_name

    doc = SimpleDocTemplate(
        str(out),
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=17 * mm,
        bottomMargin=18 * mm,
        title=out_name,
        author="宇野 拓磨",
    )
    available_width = A4[0] - doc.leftMargin - doc.rightMargin
    story = md_to_flowables(src.read_text(encoding="utf-8"), st, available_width)
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    return out


def main():
    outputs = [
        build_pdf("職務経歴書_JVCラオス事業向け_v3.md", "職務経歴書_宇野拓磨_JVCラオス事業.pdf"),
        build_pdf("応募動機作文_JVCラオス事業_v3.md", "応募動機作文_宇野拓磨_JVCラオス事業.pdf"),
    ]
    for out in outputs:
        print(out)


if __name__ == "__main__":
    main()
