#!/usr/bin/env python3
import argparse
import re
import zipfile
import xml.etree.ElementTree as ET

NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
}


def text_from_element(element):
    parts = []
    for node in element.iter():
        if node.tag == f"{{{NS['w']}}}t" and node.text:
            parts.append(node.text)
        elif node.tag == f"{{{NS['w']}}}tab":
            parts.append("\t")
        elif node.tag == f"{{{NS['w']}}}br":
            parts.append("\n")
    return "".join(parts)


def clean(text):
    text = text.replace("\u3000", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def para_to_md(paragraph):
    text = clean(text_from_element(paragraph))
    if not text:
        return ""

    style = paragraph.find(".//w:pStyle", NS)
    style_name = style.attrib.get(f"{{{NS['w']}}}val", "") if style is not None else ""
    if style_name.startswith("Heading"):
        level = re.sub(r"\D", "", style_name) or "2"
        return f"{'#' * min(int(level), 4)} {text}"

    if len(text) <= 35 and not text.endswith(("。", ".", "、", ",")):
        return f"## {text}"
    return text


def table_to_md(table):
    rows = []
    max_cols = 0
    for tr in table.findall("./w:tr", NS):
        row = []
        for tc in tr.findall("./w:tc", NS):
            cell_parts = []
            for p in tc.findall(".//w:p", NS):
                value = clean(text_from_element(p))
                if value:
                    cell_parts.append(value)
            row.append("<br>".join(cell_parts))
        if any(row):
            rows.append(row)
            max_cols = max(max_cols, len(row))

    if not rows:
        return ""

    normalized = [row + [""] * (max_cols - len(row)) for row in rows]
    escaped = [[cell.replace("|", "\\|") for cell in row] for row in normalized]
    header = escaped[0]
    divider = ["---"] * max_cols
    body = escaped[1:]

    lines = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join(divider) + " |",
    ]
    lines.extend("| " + " | ".join(row) + " |" for row in body)
    return "\n".join(lines)


def convert(docx_path):
    with zipfile.ZipFile(docx_path) as archive:
        xml = archive.read("word/document.xml")
    root = ET.fromstring(xml)
    body = root.find("w:body", NS)

    blocks = []
    for child in list(body):
        if child.tag == f"{{{NS['w']}}}p":
            md = para_to_md(child)
        elif child.tag == f"{{{NS['w']}}}tbl":
            md = table_to_md(child)
        else:
            md = ""
        if md:
            blocks.append(md)
    return "\n\n".join(blocks) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("docx")
    parser.add_argument("out")
    args = parser.parse_args()
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(convert(args.docx))


if __name__ == "__main__":
    main()
