"""
Sinh bai-XX.html từ bai-XX.md cho một hoặc nhiều học phần.
Nếu course.json có "coursePages": true thì sinh thêm thong-tin-hoc-phan.html và danh-gia-hoc-phan.html từ .md tương ứng.
Nếu có quiz/quiz-bai-XX-aiken.txt thì trang bài học có thêm khung "Luyện tập trắc nghiệm" làm bài trực tiếp
(chỉ báo số câu đúng/sai, không lưu kết quả, không hiển thị đáp án).

Cách dùng:
    uv run python build-lessons.py                  # build mọi học phần có course.json
    uv run python build-lessons.py nhap-mon-nganh   # build một học phần
    uv run python build-lessons.py --check ...      # chỉ kiểm tra, không ghi file (exit 1 nếu lệch)
"""
import re
import sys
import json
import html
import argparse
import importlib.util
from datetime import date
from pathlib import Path
from urllib.parse import quote

# Fix Windows console encoding for Vietnamese unicode characters
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if sys.stderr and hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

ROOT_DIR = Path(__file__).resolve().parent
TEMPLATE_FILE = ROOT_DIR / "templates" / "lesson-page.html"
PRACTICE_TEMPLATE_FILE = ROOT_DIR / "templates" / "practice-quiz.html"
DEFAULT_LOGO = "nhap-mon-nganh/LHU_ASU_VI_Small_Ngang.png"

LESSON_RE = re.compile(r"^bai-(\d{2})\.md$")
NAV_CLASS = ('class="px-4 py-2.5 bg-white border border-slate-200 hover:border-lhu-blue '
             'text-slate-700 hover:text-lhu-blue rounded-xl shadow-sm transition-all flex items-center gap-2"')


def load_course_config(course_dir: Path) -> dict:
    config_file = course_dir / "course.json"
    if not config_file.is_file():
        raise FileNotFoundError(f"Thiếu {config_file.relative_to(ROOT_DIR)} (xem templates/course.example.json)")
    config = json.loads(config_file.read_text(encoding="utf-8"))
    for key in ("name", "code", "credits"):
        if not config.get(key):
            raise ValueError(f"{config_file.relative_to(ROOT_DIR)}: thiếu trường bắt buộc '{key}'")
    return config


def list_lessons(course_dir: Path) -> list[str]:
    """Trả về danh sách số bài ('01', '02', ...) theo thứ tự."""
    return sorted(m.group(1) for f in course_dir.iterdir() if (m := LESSON_RE.match(f.name)))


def extract_lesson_title(md_content: str, number: str) -> str:
    """Lấy tên bài từ dòng <strong>BÀI XX - Tên bài (5 tiết)</strong> trong khối Tổng quan."""
    match = re.search(r"<strong>\s*BÀI\s*\d+\s*[-–:]\s*(.+?)</strong>", md_content, re.IGNORECASE | re.DOTALL)
    if not match:
        return f"Bài {number}"
    title = html.unescape(re.sub(r"\s+", " ", match.group(1))).strip()
    return re.sub(r"\s*\(\d+\s*tiết\)\s*$", "", title, flags=re.IGNORECASE)


def nav_link(href: str | None, label_html: str) -> str:
    if not href:
        return "<div></div>"
    return f'<a href="{href}" {NAV_CLASS}>{label_html}</a>'


def resolve_logo(config: dict) -> str:
    return config.get("logo") or "../" + DEFAULT_LOGO


def resolve_landing(course_dir: Path, config: dict) -> str:
    if config.get("landingPage"):
        return config["landingPage"]
    return "course-landingpage.html" if (course_dir / "course-landingpage.html").is_file() else "index.html"


def has_page(course_dir: Path, config: dict, name: str) -> bool:
    """Trang đề cương/đánh giá có tồn tại (hoặc sẽ được build từ .md) hay không."""
    if (course_dir / f"{name}.html").is_file():
        return True
    return bool(config.get("coursePages")) and (course_dir / f"{name}.md").is_file()


def render_lesson(course_dir: Path, config: dict, lessons: list[str], number: str, template: str) -> str:
    md_content = (course_dir / f"bai-{number}.md").read_text(encoding="utf-8")
    title = config.get("lessonTitles", {}).get(number) or extract_lesson_title(md_content, number)

    idx = lessons.index(number)
    if idx > 0:
        prev_href = f"bai-{lessons[idx - 1]}.html"
    elif has_page(course_dir, config, "thong-tin-hoc-phan"):
        prev_href = "thong-tin-hoc-phan.html"
    else:
        prev_href = None
    next_href = f"bai-{lessons[idx + 1]}.html" if idx + 1 < len(lessons) else None
    return render_page(course_dir, config, template, f"Bài {number} - {title}", md_content, prev_href, next_href,
                       practice=render_practice_quiz(course_dir, number))


def local_links(course_dir: Path, config: dict) -> dict:
    """Placeholder link → file có thật trong học phần, dùng cho trang web của portal.

    File .md (bản dán Moodle) vẫn giữ placeholder để giảng viên thay bằng link Moodle; trang .html
    sinh ra thì trỏ thẳng tới file trong repo:
    - "documents" trong course.json: {"LINK_GIAO_TRINH": "giao-trinh/....docx", ...}
    - {{LINK_SLIDE_BAI_XX}} → Slides/bai-XX.pptx nếu file tồn tại.
    """
    links = {}
    for key, rel in (config.get("documents") or {}).items():
        if (course_dir / rel).is_file():
            links[key] = quote(rel)
    for pptx in sorted((course_dir / "Slides").glob("bai-*.pptx")):
        links[f"LINK_SLIDE_BAI_{pptx.stem[4:]}"] = f"Slides/{quote(pptx.name)}"
    return links


def resolve_local_links(content: str, links: dict) -> str:
    return re.sub(r"\{\{([A-Z][A-Z0-9_]*)\}\}", lambda m: links.get(m.group(1), m.group(0)), content)


def fill(template: str, values: dict) -> str:
    # Thay một lượt bằng regex để nội dung có chứa "{{...}}" (placeholder link) không bị thay nhầm
    return re.sub(r"\{\{([A-Z_]+)\}\}", lambda m: values.get(m.group(1), m.group(0)), template)


_quiz_module = None


def load_quiz_module():
    """Dùng lại bộ đọc Aiken của build-quiz.py để hai script luôn hiểu file quiz giống nhau."""
    global _quiz_module
    if _quiz_module is None:
        spec = importlib.util.spec_from_file_location("build_quiz", ROOT_DIR / "build-quiz.py")
        _quiz_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(_quiz_module)
    return _quiz_module


def render_practice_quiz(course_dir: Path, number: str) -> str:
    quiz_file = course_dir / "quiz" / f"quiz-bai-{number}-aiken.txt"
    if not quiz_file.is_file():
        return ""
    quiz = load_quiz_module()
    questions = quiz.parse_questions(quiz.read_text(quiz_file), quiz_file.name)
    # Mã hóa nhẹ vị trí đáp án (giải mã trong templates/practice-quiz.html) để không lộ khi xem nhanh mã nguồn
    data = [{"q": q["question"], "o": q["options"], "k": (q["answer"] + i * 3 + 5) % len(q["options"])}
            for i, q in enumerate(questions)]
    quiz_json = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    fragment = PRACTICE_TEMPLATE_FILE.read_text(encoding="utf-8")
    return fill(fragment, {"LESSON_NUMBER": number, "QUESTION_COUNT": str(len(data)), "QUIZ_JSON": quiz_json}) + "\n"


def render_course_page(course_dir: Path, config: dict, lessons: list[str], name: str, template: str) -> str:
    """Trang đề cương (thong-tin-hoc-phan) và trang đánh giá (danh-gia-hoc-phan)."""
    md_content = (course_dir / f"{name}.md").read_text(encoding="utf-8")
    first = f"bai-{lessons[0]}.html" if lessons else None
    last = f"bai-{lessons[-1]}.html" if lessons else None
    if name == "thong-tin-hoc-phan":
        title = f'Thông tin học phần & Đề cương chi tiết ({config["code"]})'
        prev_href, next_href = None, first
    else:
        title = f'Đánh giá học phần & Rubric ({config["code"]})'
        prev_href, next_href = last, None
    return render_page(course_dir, config, template, title, md_content, prev_href, next_href)


def render_page(course_dir: Path, config: dict, template: str, page_title: str, md_content: str,
                prev_href: str | None, next_href: str | None, practice: str = "") -> str:
    values = {
        "PAGE_TITLE": page_title,
        "COURSE_NAME": config["name"],
        "COURSE_CODE": config["code"],
        "CREDITS": config["credits"],
        "HEADER_LABEL": config.get("headerLabel") or f'{config["name"].upper()} ({config["code"]})',
        "SUBTITLE_TAG": config.get("subtitleTag", "Chuẩn ABET Hoa Kỳ"),
        "YEAR": str(config.get("year", date.today().year)),
        "LANDING_PAGE": resolve_landing(course_dir, config),
        "LOGO": resolve_logo(config),
        "PREV_NAV": nav_link(prev_href, '<i class="fa-solid fa-chevron-left"></i> Bài trước'),
        "NEXT_NAV": nav_link(next_href, 'Bài tiếp theo <i class="fa-solid fa-chevron-right"></i>'),
        "CONTENT": resolve_local_links(md_content, local_links(course_dir, config)).rstrip("\n") + "\n",
        "PRACTICE_QUIZ": practice,
    }
    return fill(template, values)


def build_course(course_dir: Path, check_only: bool = False) -> list[str]:
    """Build (hoặc kiểm tra) các trang bài học. Trả về danh sách file bị thay đổi / lệch."""
    config = load_course_config(course_dir)
    template = TEMPLATE_FILE.read_text(encoding="utf-8")
    lessons = list_lessons(course_dir)
    changed = []

    pages = [(f"bai-{n}.html", lambda n=n: render_lesson(course_dir, config, lessons, n, template)) for n in lessons]
    if config.get("coursePages"):
        # Trang đề cương & đánh giá chỉ được build khi course.json bật coursePages
        pages += [(f"{name}.html", lambda name=name: render_course_page(course_dir, config, lessons, name, template))
                  for name in ("thong-tin-hoc-phan", "danh-gia-hoc-phan") if (course_dir / f"{name}.md").is_file()]

    for filename, render in pages:
        out_file = course_dir / filename
        rendered = render()
        current = out_file.read_text(encoding="utf-8") if out_file.is_file() else None
        if current is not None and current.replace("\r\n", "\n") == rendered:
            continue
        changed.append(out_file.name)
        if not check_only:
            out_file.write_text(rendered, encoding="utf-8", newline="\n")
    return changed


def discover_courses() -> list[Path]:
    return sorted(d for d in ROOT_DIR.iterdir() if d.is_dir() and (d / "course.json").is_file())


def main():
    parser = argparse.ArgumentParser(description="Sinh bai-XX.html từ bai-XX.md")
    parser.add_argument("courses", nargs="*", help="Thư mục học phần (mặc định: mọi thư mục có course.json)")
    parser.add_argument("--check", action="store_true", help="Chỉ kiểm tra, không ghi file")
    args = parser.parse_args()

    course_dirs = [ROOT_DIR / c.strip("/\\") for c in args.courses] or discover_courses()
    if not course_dirs:
        print("Không tìm thấy học phần nào có course.json.")
        return 1

    exit_code = 0
    for course_dir in course_dirs:
        try:
            changed = build_course(course_dir, check_only=args.check)
        except (FileNotFoundError, ValueError) as e:
            print(f"[LỖI] {course_dir.name}: {e}")
            exit_code = 1
            continue

        total = len(list_lessons(course_dir))
        if args.check:
            if changed:
                exit_code = 1
                print(f"[LỆCH] {course_dir.name}: {', '.join(changed)} chưa khớp với file .md")
            else:
                print(f"[OK] {course_dir.name}: {total} bài đã đồng bộ")
        else:
            print(f"[+] {course_dir.name}: {len(changed)} trang được cập nhật"
                  + (f" ({', '.join(changed)})" if changed else ""))
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
