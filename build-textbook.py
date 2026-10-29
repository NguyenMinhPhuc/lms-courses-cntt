"""
Ghép giáo trình nội bộ (Markdown) của một học phần thành một file Word (.docx) có trang bìa và mục lục.

Cách dùng:
    uv run --with python-docx python build-textbook.py lap-trinh-ung-dung-mobile
    uv run --with python-docx python build-textbook.py lap-trinh-ung-dung-mobile --srs

Giáo trình:  <hoc-phan>/giao-trinh/00-loi-noi-dau.md, chuong-01.md, ...  → giao-trinh/Giao-trinh-<hoc-phan>.docx
             (giao-trinh/bai-tap-huong-dan/bt-XX.md, nếu có, được chèn vào chương XX trước "Tài liệu tham khảo")
SRS (--srs): <hoc-phan>/srs/01-*.md, 02-*.md, ...  → srs/SRS-<srsProject>.docx
             (tên dự án lấy từ "srsProject" trong course.json)

Hỗ trợ phần Markdown dùng trong giáo trình: tiêu đề #..####, đoạn văn, **đậm**, *nghiêng*, `code`,
danh sách - và 1. (lồng 2 cấp), bảng |...|, khối ``` code ```, trích dẫn >.
Mục lục là trường TOC của Word: mở file trong Word rồi chọn Update Field (hoặc F9) để cập nhật số trang.
"""
import re
import sys
import json
import argparse
from datetime import date
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

# Fix Windows console encoding for Vietnamese unicode characters
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROOT_DIR = Path(__file__).resolve().parent
BODY_FONT = "Times New Roman"
HEADING_FONT = "Arial"
CODE_FONT = "Consolas"
LHU_BLUE = RGBColor(0x01, 0x3D, 0x88)
CODE_BG = "F1F3F5"
TABLE_HEADER_BG = "E7F1FF"


# ---------------------------------------------------------------- helpers
def set_cell_shading(cell, color: str):
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), color)
    cell._tc.get_or_add_tcPr().append(shd)


def set_paragraph_shading(paragraph, color: str):
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), color)
    paragraph._p.get_or_add_pPr().append(shd)


def set_paragraph_left_border(paragraph, color: str = "013D88"):
    borders = OxmlElement("w:pBdr")
    left = OxmlElement("w:left")
    for key, value in (("val", "single"), ("sz", "18"), ("space", "8"), ("color", color)):
        left.set(qn(f"w:{key}"), value)
    borders.append(left)
    paragraph._p.get_or_add_pPr().append(borders)


def add_field(paragraph, instruction: str, placeholder: str = ""):
    """Chèn một trường Word (TOC, PAGE...) vào paragraph."""
    run = paragraph.add_run()
    begin = OxmlElement("w:fldChar")
    begin.set(qn("w:fldCharType"), "begin")
    begin.set(qn("w:dirty"), "true")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = instruction
    sep = OxmlElement("w:fldChar")
    sep.set(qn("w:fldCharType"), "separate")
    text = OxmlElement("w:t")
    text.text = placeholder
    end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end")
    for element in (begin, instr, sep, text, end):
        run._r.append(element)


def add_inline(paragraph, text: str, size: float | None = None, color: RGBColor | None = None):
    """Ghi text có **đậm**, *nghiêng*, `code` vào paragraph."""
    for part in re.split(r"(\*\*.+?\*\*|`[^`]+`|(?<![\w*])\*[^*\s][^*]*?\*(?![\w*]))", text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            run = paragraph.add_run(part[2:-2])
            run.bold = True
        elif part.startswith("`") and part.endswith("`"):
            run = paragraph.add_run(part[1:-1])
            run.font.name = CODE_FONT
            run._element.rPr.rFonts.set(qn("w:eastAsia"), CODE_FONT)
            run.font.size = Pt((size or 13) - 2)
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            run = paragraph.add_run(part[1:-1])
            run.italic = True
        else:
            run = paragraph.add_run(part)
        if size and not (part.startswith("`") and part.endswith("`")):
            run.font.size = Pt(size)
        if color:
            run.font.color.rgb = color


# ---------------------------------------------------------------- document setup
def setup_styles(doc: Document):
    normal = doc.styles["Normal"]
    normal.font.name = BODY_FONT
    normal.element.rPr.rFonts.set(qn("w:eastAsia"), BODY_FONT)
    normal.font.size = Pt(13)
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.2

    for level, size, before in ((1, 20, 0), (2, 16, 14), (3, 14, 10), (4, 13, 8)):
        style = doc.styles[f"Heading {level}"]
        style.font.name = HEADING_FONT
        rfonts = style.element.rPr.rFonts
        rfonts.set(qn("w:eastAsia"), HEADING_FONT)
        # Style tiêu đề mặc định trỏ tới font theme (Calibri Light); gỡ để Arial có hiệu lực
        for attr in ("w:asciiTheme", "w:hAnsiTheme", "w:eastAsiaTheme", "w:cstheme"):
            rfonts.attrib.pop(qn(attr), None)
        style.font.size = Pt(size)
        style.font.bold = True
        style.font.color.rgb = LHU_BLUE
        style.paragraph_format.space_before = Pt(before)
        style.paragraph_format.space_after = Pt(6)
        style.paragraph_format.keep_with_next = True

    section = doc.sections[0]
    section.page_height, section.page_width = Cm(29.7), Cm(21.0)
    section.left_margin = Cm(3.0)
    section.right_margin = Cm(2.0)
    section.top_margin = section.bottom_margin = Cm(2.5)


def add_cover(doc: Document, config: dict, course_dir: Path, kind: str = "GIÁO TRÌNH", title: str | None = None,
              subtitle_lines: list[str] | None = None):
    def centered(text: str, size: float, bold=False, color=None, space_after=6):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(space_after)
        run = p.add_run(text)
        run.font.size = Pt(size)
        run.bold = bold
        if color:
            run.font.color.rgb = color
        return p

    centered("TRƯỜNG ĐẠI HỌC LẠC HỒNG", 14, bold=True)
    centered("KHOA CÔNG NGHỆ THÔNG TIN", 14, bold=True, space_after=120)
    centered(kind, 22, bold=True, color=LHU_BLUE)
    centered((title or config.get("name", course_dir.name)).upper(), 26, bold=True, color=LHU_BLUE)
    centered(f"Mã học phần: {config.get('code', '')}", 14, space_after=24)
    lines = subtitle_lines if subtitle_lines is not None else config.get("textbookSubtitle", [])
    for line in lines:
        centered(line, 13)
    centered("", 13, space_after=120)
    author = config.get("textbookAuthor") or config.get("instructor")
    if author:
        centered(f"Biên soạn: {author}", 14, bold=True)
    centered("Bản thảo - Lưu hành nội bộ", 13)
    centered(f"Đồng Nai, {config.get('year', date.today().year)}", 13)
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def add_toc(doc: Document):
    heading = doc.add_paragraph()
    heading.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = heading.add_run("MỤC LỤC")
    run.bold = True
    run.font.size = Pt(18)
    run.font.color.rgb = LHU_BLUE
    add_field(doc.add_paragraph(), 'TOC \\o "1-2" \\h \\z \\u',
              "Nhấn chuột phải vào đây và chọn Update Field để tạo mục lục.")


def setup_header_footer(section, title: str):
    header = section.header.paragraphs[0]
    header.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = header.add_run(title)
    run.font.size = Pt(10)
    run.italic = True
    run.font.color.rgb = RGBColor(0x6C, 0x75, 0x7D)

    footer = section.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    add_field(footer, "PAGE", "1")


# ---------------------------------------------------------------- markdown → docx
def add_table(doc: Document, rows: list[list[str]]):
    header, body = rows[0], rows[1:]
    table = doc.add_table(rows=1 + len(body), cols=len(header))
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False

    # Chia độ rộng cột theo lượng chữ: cột mô tả dài được rộng hơn cột mã, cột ưu tiên
    section = doc.sections[-1]
    usable = section.page_width - section.left_margin - section.right_margin
    minimums, weights = [], []
    for c in range(len(header)):
        texts = [re.sub(r"[`*]", "", r[c]) for r in [header] + body if c < len(r)]
        lengths = [len(t) for t in texts]
        longest_word = max((len(w) for t in texts for w in t.split()), default=1)
        # mỗi cột tối thiểu đủ chứa từ dài nhất (khoảng 0,21 cm mỗi ký tự ở cỡ 11pt, cộng lề ô)
        minimums.append(Cm(min(longest_word * 0.21 + 0.5, 6)))
        weights.append(min(max(sum(lengths) / len(lengths), max(lengths) * 0.35), 60))
    spare = max(usable - sum(minimums), 0)
    widths = [int(m + spare * w / sum(weights)) for m, w in zip(minimums, weights)]
    if sum(widths) > usable:  # quá nhiều cột: thu nhỏ đều
        widths = [int(w * usable / sum(widths)) for w in widths]

    for r, cells in enumerate([header] + body):
        for c in range(len(header)):
            cell = table.cell(r, c)
            cell.width = widths[c]
            cell.paragraphs[0].paragraph_format.space_after = Pt(0)
            add_inline(cell.paragraphs[0], cells[c] if c < len(cells) else "", size=11)
            if r == 0:
                set_cell_shading(cell, TABLE_HEADER_BG)
                for run in cell.paragraphs[0].runs:
                    run.bold = True
    doc.add_paragraph().paragraph_format.space_after = Pt(0)


def add_code_block(doc: Document, lines: list[str]):
    for i, line in enumerate(lines or [""]):
        p = doc.add_paragraph()
        fmt = p.paragraph_format
        fmt.space_before = Pt(4 if i == 0 else 0)
        fmt.space_after = Pt(4 if i == len(lines) - 1 else 0)
        fmt.line_spacing = 1.0
        fmt.left_indent = Cm(0.3)
        fmt.keep_with_next = i < len(lines) - 1 and len(lines) <= 25
        set_paragraph_shading(p, CODE_BG)
        run = p.add_run(line.replace("\t", "    ") or " ")
        run.font.name = CODE_FONT
        run._element.rPr.rFonts.set(qn("w:eastAsia"), CODE_FONT)
        run.font.size = Pt(9.5)


def add_list_item(doc: Document, text: str, level: int, number: str | None):
    p = doc.add_paragraph()
    fmt = p.paragraph_format
    indent = Cm(0.8 + 0.8 * level)
    fmt.left_indent = indent
    fmt.first_line_indent = -Cm(0.6)
    fmt.space_after = Pt(3)
    bullet = f"{number}\t" if number else ("•\t" if level == 0 else "–\t")
    p.add_run(bullet)
    fmt.tab_stops.add_tab_stop(indent)
    add_inline(p, text)


def render_markdown(doc: Document, text: str, first_chapter: bool):
    lines = text.replace("\r\n", "\n").split("\n")
    i, para = 0, []

    def flush():
        if para:
            add_inline(doc.add_paragraph(), " ".join(s.strip() for s in para))
            para.clear()

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("```"):
            flush()
            block = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                block.append(lines[i])
                i += 1
            add_code_block(doc, block)
        elif m := re.match(r"^(#{1,4})\s+(.*)$", line):
            flush()
            level = len(m.group(1))
            heading = doc.add_heading(m.group(2).strip(), level=level)
            if level == 1 and not first_chapter:
                heading.paragraph_format.page_break_before = True
        elif stripped.startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|[\s:\-|]+\|\s*$", lines[i + 1]):
            flush()
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                if not re.match(r"^\s*\|[\s:\-|]+\|\s*$", lines[i]):
                    rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            add_table(doc, rows)
            continue
        elif m := re.match(r"^(\s*)[-*]\s+(.*)$", line):
            flush()
            add_list_item(doc, m.group(2), len(m.group(1)) // 2, None)
        elif m := re.match(r"^(\s*)(\d+)\.\s+(.*)$", line):
            flush()
            add_list_item(doc, m.group(3), len(m.group(1)) // 2, f"{m.group(2)}.")
        elif stripped.startswith(">"):
            flush()
            quote = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip()[1:].strip())
                i += 1
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.5)
            set_paragraph_left_border(p)
            add_inline(p, " ".join(quote))
            continue
        elif not stripped:
            flush()
        else:
            para.append(line)
        i += 1
    flush()


def chapter_text(f: Path) -> str:
    """Nội dung chương, kèm bài tập hướng dẫn bai-tap-huong-dan/bt-XX.md (nếu có) chèn trước Tài liệu tham khảo."""
    text = f.read_text(encoding="utf-8")
    m = re.match(r"chuong-(\d+)\.md$", f.name)
    extra = f.parent / "bai-tap-huong-dan" / f"bt-{m.group(1)}.md" if m else None
    if extra and extra.is_file():
        block = extra.read_text(encoding="utf-8").strip() + "\n\n"
        marker = "\n## Tài liệu tham khảo"
        text = text.replace(marker, "\n" + block + marker.lstrip("\n"), 1) if marker in text else text + "\n\n" + block
    return text


def render_document(files: list[Path], out: Path, header: str, cover) -> Path:
    doc = Document()
    setup_styles(doc)
    cover(doc)
    add_toc(doc)

    body = doc.add_section(WD_SECTION.NEW_PAGE)
    body.header.is_linked_to_previous = False
    body.footer.is_linked_to_previous = False
    setup_header_footer(body, header)

    for index, f in enumerate(files):
        render_markdown(doc, chapter_text(f), first_chapter=index == 0)

    doc.save(out)
    return out


def load_config(course_dir: Path) -> dict:
    config_file = course_dir / "course.json"
    return json.loads(config_file.read_text(encoding="utf-8")) if config_file.is_file() else {}


def build(course_dir: Path) -> Path:
    src = course_dir / "giao-trinh"
    files = sorted(src.glob("00-*.md")) + sorted(src.glob("chuong-*.md"))
    if not files:
        raise FileNotFoundError(f"Không có file Markdown trong {src.relative_to(ROOT_DIR)}")
    config = load_config(course_dir)
    return render_document(files, src / f"Giao-trinh-{course_dir.name}.docx",
                           f"Giáo trình {config.get('name', course_dir.name)}",
                           lambda doc: add_cover(doc, config, course_dir))


def build_srs(course_dir: Path) -> Path:
    src = course_dir / "srs"
    files = sorted(src.glob("[0-9][0-9]-*.md"))
    if not files:
        raise FileNotFoundError(f"Không có file Markdown trong {src.relative_to(ROOT_DIR)}")
    config = load_config(course_dir)
    project = config.get("srsProject", course_dir.name)
    subtitle = [f"Dự án mẫu của học phần {config.get('name', course_dir.name)}",
                "Phụ lục của giáo trình"]
    out = src / f"SRS-{project.replace(' ', '-')}.docx"
    return render_document(files, out, f"SRS {project} - {config.get('name', course_dir.name)}",
                           lambda doc: add_cover(doc, config, course_dir, kind="ĐẶC TẢ YÊU CẦU PHẦN MỀM (SRS)",
                                                 title=f"Dự án {project}", subtitle_lines=subtitle))


def main():
    parser = argparse.ArgumentParser(description="Ghép giáo trình Markdown thành file Word")
    parser.add_argument("course", help="Thư mục học phần")
    parser.add_argument("--srs", action="store_true", help="Ghép tài liệu SRS trong <hoc-phan>/srs/ thay cho giáo trình")
    args = parser.parse_args()
    course_dir = ROOT_DIR / args.course.strip("/\\")
    try:
        out = build_srs(course_dir) if args.srs else build(course_dir)
    except FileNotFoundError as e:
        print(f"[LỖI] {e}")
        return 1
    print(f"[+] Đã ghi {out.relative_to(ROOT_DIR)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
