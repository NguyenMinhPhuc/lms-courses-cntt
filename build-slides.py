"""
Sinh slide PowerPoint (Slides/bai-XX.pptx) từ ghi chú slide Markdown (Slides/bai-XX.markdown).

Cách dùng:
    uv run --with python-pptx python build-slides.py nhap-mon-lap-trinh          # mọi bài của học phần
    uv run --with python-pptx python build-slides.py nhap-mon-lap-trinh 03       # chỉ bài 03

Định dạng Markdown đầu vào: xem .claude/skills/lms-lecture-builder/references/slides.md
"""
import re
import sys
import json
import argparse
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

# Fix Windows console encoding for Vietnamese unicode characters
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if sys.stderr and hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

ROOT_DIR = Path(__file__).resolve().parent
SLIDE_FILE_RE = re.compile(r"^bai-(\d{2})\.markdown$")

LHU_BLUE = RGBColor(0x01, 0x3D, 0x88)
LHU_DARK = RGBColor(0x01, 0x29, 0x5C)
GOLD = RGBColor(0xFF, 0xC6, 0x27)
TEXT = RGBColor(0x21, 0x25, 0x29)
MUTED = RGBColor(0x6C, 0x75, 0x7D)
CODE_BG = RGBColor(0xF1, 0xF3, 0xF5)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
FONT = "Arial"
CODE_FONT = "Consolas"

SLIDE_W, SLIDE_H = Inches(13.333), Inches(7.5)
NOTES_LABEL = "ghi chú giảng viên"


# ---------------------------------------------------------------- parse
def parse_markdown(text: str) -> tuple[str, str, list[dict]]:
    """Trả về (tiêu đề bài, phụ đề, danh sách slide). Mỗi slide: {title, blocks, notes}.
    block = ("para", level, text, is_label) hoặc ("code", text)."""
    deck_title, subtitle, slides = "", "", []
    current = None
    in_notes = in_code = False
    code_lines: list[str] = []

    for raw in text.replace("\r\n", "\n").split("\n"):
        line = raw.rstrip()
        if in_code:
            if line.strip().startswith("```"):
                current["blocks"].append(("code", "\n".join(code_lines)))
                in_code, code_lines = False, []
            else:
                code_lines.append(raw.rstrip("\n"))
            continue

        if line.startswith("# ") and not deck_title:
            deck_title = line[2:].strip()
            continue
        if line.startswith("## "):
            title = re.sub(r"^Slide\s*\d+\s*[:.\-–]\s*", "", line[3:].strip(), flags=re.IGNORECASE)
            current = {"title": title, "blocks": [], "notes": []}
            slides.append(current)
            in_notes = False
            continue
        if current is None:
            if line.strip() and not subtitle and line.strip() != "---":
                subtitle = line.strip()
            continue
        if line.strip() == "---":
            in_notes = False
            continue
        if line.strip().startswith("```") and not in_notes:
            in_code = True
            continue

        label = re.match(r"^\*\*(.+?)\*\*\s*:\s*(.*)$", line.strip())
        if label and label.group(1).strip().lower() == NOTES_LABEL:
            in_notes = True
            if label.group(2).strip():
                current["notes"].append(label.group(2).strip())
            continue
        if in_notes:
            if line.strip():
                current["notes"].append(re.sub(r"^\s*[-*]\s+", "", line).strip())
            continue
        if not line.strip():
            continue

        if label:
            content = f"**{label.group(1).strip()}**" + (f": {label.group(2).strip()}" if label.group(2).strip() else "")
            current["blocks"].append(("para", 0, content, True))
            continue
        bullet = re.match(r"^(\s*)[-*]\s+(.*)$", line)
        if bullet:
            level = len(bullet.group(1).replace("\t", "  ")) // 2
            current["blocks"].append(("para", level, bullet.group(2).strip(), False))
        else:
            current["blocks"].append(("para", 0, line.strip(), False))
    return deck_title, subtitle, slides


# ---------------------------------------------------------------- render
def add_runs(paragraph, text: str, size: int, color: RGBColor, bold_all: bool = False):
    """Ghi text vào paragraph, hỗ trợ **in đậm** và `code` trong dòng."""
    for part in re.split(r"(\*\*.+?\*\*|`[^`]+`)", text):
        if not part:
            continue
        run = paragraph.add_run()
        if part.startswith("**") and part.endswith("**"):
            run.text, run.font.bold = part[2:-2], True
        elif part.startswith("`") and part.endswith("`"):
            run.text, run.font.name = part[1:-1], CODE_FONT
        else:
            run.text, run.font.bold = part, bold_all
        run.font.size = Pt(size)
        run.font.color.rgb = color
        if run.font.name != CODE_FONT:
            run.font.name = FONT


def add_rect(slide, left, top, width, height, color):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    shape.shadow.inherit = False
    return shape


def add_text(slide, left, top, width, height, text, size, color, bold=False):
    box = slide.shapes.add_textbox(left, top, width, height)
    frame = box.text_frame
    frame.word_wrap = True
    add_runs(frame.paragraphs[0], text, size, color, bold_all=bold)
    return box


def title_slide(prs, deck_title, subtitle, course_line):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_rect(slide, 0, 0, SLIDE_W, SLIDE_H, LHU_BLUE)
    add_rect(slide, Inches(0.8), Inches(3.55), Inches(1.6), Inches(0.08), GOLD)
    add_text(slide, Inches(0.8), Inches(0.8), Inches(11.5), Inches(0.5), course_line, 16, GOLD, bold=True)
    box = add_text(slide, Inches(0.8), Inches(1.5), Inches(11.5), Inches(2.0), deck_title, 40, WHITE, bold=True)
    box.text_frame.vertical_anchor = MSO_ANCHOR.BOTTOM
    if subtitle:
        add_text(slide, Inches(0.8), Inches(3.85), Inches(11.5), Inches(1.0), subtitle, 20, WHITE)
    add_text(slide, Inches(0.8), Inches(6.6), Inches(11.5), Inches(0.4),
             "Khoa Công nghệ Thông tin - Trường Đại học Lạc Hồng", 12, WHITE)


def content_slide(prs, data, footer, number):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_rect(slide, 0, 0, Inches(0.18), SLIDE_H, LHU_BLUE)
    add_text(slide, Inches(0.6), Inches(0.35), Inches(12.2), Inches(0.9), data["title"], 30, LHU_BLUE, bold=True)
    add_rect(slide, Inches(0.6), Inches(1.2), Inches(1.2), Inches(0.06), GOLD)

    paras = [b for b in data["blocks"] if b[0] == "para"]
    codes = [b for b in data["blocks"] if b[0] == "code"]
    lines = len(paras) + sum(c[1].count("\n") + 1 for c in codes)
    base = 20 if lines <= 9 else 18 if lines <= 13 else 15

    body_top, body_bottom = Inches(1.5), Inches(6.7)
    code_height = Inches(0.32) * sum(c[1].count("\n") + 1 for c in codes) + Inches(0.3) * len(codes)
    text_height = max(Inches(1.0), body_bottom - body_top - code_height - (Inches(0.2) if codes else 0))
    if codes:
        # Ước lượng chiều cao phần chữ để khối code nằm ngay bên dưới thay vì dồn xuống cuối slide
        text_height = min(text_height, Inches(0.5) * len(paras) + Inches(0.2))

    if paras:
        box = slide.shapes.add_textbox(Inches(0.6), body_top, Inches(12.1), text_height)
        frame = box.text_frame
        frame.word_wrap = True
        for i, (_, level, text, is_label) in enumerate(paras):
            p = frame.paragraphs[0] if i == 0 else frame.add_paragraph()
            indent = "    " * level
            prefix = "" if is_label else ("•  " if level == 0 else "–  ")
            p.space_before = Pt(8 if is_label and i > 0 else 3)
            add_runs(p, indent + prefix + text, max(base - 2 * level, 12), LHU_DARK if is_label else TEXT)

    top = body_top + (text_height + Inches(0.2) if paras else 0)
    for _, code in codes:
        height = Inches(0.32) * (code.count("\n") + 1) + Inches(0.3)
        rect = add_rect(slide, Inches(0.6), top, Inches(12.1), height, CODE_BG)
        frame = rect.text_frame
        frame.word_wrap = True
        frame.vertical_anchor = MSO_ANCHOR.TOP
        frame.margin_left = frame.margin_top = Inches(0.15)
        for i, code_line in enumerate(code.split("\n")):
            p = frame.paragraphs[0] if i == 0 else frame.add_paragraph()
            p.alignment = PP_ALIGN.LEFT
            run = p.add_run()
            run.text = code_line or " "
            run.font.name, run.font.size, run.font.color.rgb = CODE_FONT, Pt(14), TEXT
        top += height + Inches(0.15)

    add_text(slide, Inches(0.6), Inches(6.95), Inches(10), Inches(0.35), footer, 11, MUTED)
    add_text(slide, Inches(12.0), Inches(6.95), Inches(0.8), Inches(0.35), str(number), 11, MUTED)
    if data["notes"]:
        slide.notes_slide.notes_text_frame.text = "\n".join(data["notes"])


def build_deck(md_file: Path, out_file: Path, config: dict) -> int:
    deck_title, subtitle, slides = parse_markdown(md_file.read_text(encoding="utf-8"))
    if not slides:
        raise ValueError(f"{md_file.name}: không tìm thấy slide nào (mỗi slide bắt đầu bằng '## ')")
    prs = Presentation()
    prs.slide_width, prs.slide_height = SLIDE_W, SLIDE_H
    name, code = config.get("name", ""), config.get("code", "")
    course_line = f"{name} ({code})" if name and code else name or code
    title_slide(prs, deck_title or md_file.stem, subtitle, course_line)
    for i, data in enumerate(slides, start=2):
        content_slide(prs, data, f"{course_line} • {deck_title}", i)
    prs.save(out_file)
    return len(slides) + 1


def main():
    parser = argparse.ArgumentParser(description="Sinh Slides/bai-XX.pptx từ Slides/bai-XX.markdown")
    parser.add_argument("course", help="Thư mục học phần")
    parser.add_argument("lessons", nargs="*", help="Số bài (01, 02...). Mặc định: mọi bài")
    args = parser.parse_args()

    course_dir = ROOT_DIR / args.course.strip("/\\")
    config_file = course_dir / "course.json"
    config = json.loads(config_file.read_text(encoding="utf-8")) if config_file.is_file() else {}
    slides_dir = course_dir / "Slides"
    files = sorted(f for f in slides_dir.glob("bai-*.markdown") if SLIDE_FILE_RE.match(f.name)) if slides_dir.is_dir() else []
    if args.lessons:
        files = [f for f in files if SLIDE_FILE_RE.match(f.name).group(1) in args.lessons]
    if not files:
        print(f"[LỖI] Không có file Slides/bai-XX.markdown trong {course_dir.name}")
        return 1

    exit_code = 0
    for md_file in files:
        try:
            count = build_deck(md_file, md_file.with_suffix(".pptx"), config)
            print(f"[+] {course_dir.name}/Slides/{md_file.with_suffix('.pptx').name}: {count} slide")
        except (ValueError, PermissionError) as e:
            print(f"[LỖI] {md_file.name}: {e}")
            exit_code = 1
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
