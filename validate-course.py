"""
Kiểm tra một học phần đã đủ thành phần và đúng định dạng chưa.

Cách dùng:
    uv run python validate-course.py nhap-mon-nganh
    uv run python validate-course.py                # kiểm tra mọi thư mục học phần có index.html

Exit code 1 nếu có LỖI; CẢNH BÁO không làm thất bại.
"""
import re
import sys
import json
import argparse
import importlib.util
from collections import Counter
from pathlib import Path

# Fix Windows console encoding for Vietnamese unicode characters
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if sys.stderr and hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

ROOT_DIR = Path(__file__).resolve().parent
IGNORE_DIRS = {"templates", "node_modules", "__pycache__", "dist", "build", "scratch"}
MIN_QUIZ_QUESTIONS = 10

# 4 khối accordion bắt buộc theo template-lesson.md
LESSON_SECTIONS = [
    "📘 1. Tổng quan bài học",
    "📚 2. Học liệu chính",
    "💡 3. Hoạt động",
    "🆘 4. Góc trợ giúp",
]
REQUIRED_FILES = ["README.md", "index.html", "course.json",
                  "thong-tin-hoc-phan.md", "thong-tin-hoc-phan.html",
                  "danh-gia-hoc-phan.md", "danh-gia-hoc-phan.html"]
# Link mẫu trong template-lesson.md thuộc các domain này là link riêng của học phần khác
SAMPLE_LINK_DOMAINS = ("gamma.app", "youtube.com", "youtu.be", "forms.gle", "learn.lhu.edu.vn", "forum.fitlhu.com")

# Chỉ placeholder dạng {{TEN_IN_HOA}}; tránh báo nhầm JSX như style={{ width: 100 }} trong ví dụ code
PLACEHOLDER_RE = re.compile(r"\{\{[A-Z][A-Z0-9_]*\}\}")
OPTION_RE = re.compile(r"^([A-Z])\.\s+\S")
ANSWER_RE = re.compile(r"^ANSWER:\s*([A-Z])\s*$")


def load_build_module():
    spec = importlib.util.spec_from_file_location("build_lessons", ROOT_DIR / "build-lessons.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Report:
    def __init__(self, course: str):
        self.course = course
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.info: list[str] = []

    def error(self, msg): self.errors.append(msg)
    def warn(self, msg): self.warnings.append(msg)
    def ok(self, msg): self.info.append(msg)

    def print(self):
        print("=" * 70)
        print(f"HỌC PHẦN: {self.course}")
        print("=" * 70)
        for m in self.info:
            print(f"  [OK]    {m}")
        for m in self.warnings:
            print(f"  [CẢNH BÁO] {m}")
        for m in self.errors:
            print(f"  [LỖI]   {m}")
        print(f"  => {len(self.errors)} lỗi, {len(self.warnings)} cảnh báo\n")


def sample_links() -> set[str]:
    template = ROOT_DIR / "template-lesson.md"
    if not template.is_file():
        return set()
    hrefs = re.findall(r'href="([^"]+)"', template.read_text(encoding="utf-8"))
    return {h for h in hrefs if any(d in h for d in SAMPLE_LINK_DOMAINS)}


def parse_aiken(text: str) -> tuple[int, list[str], Counter]:
    """Trả về (số câu hợp lệ, danh sách lỗi, thống kê đáp án)."""
    errors = []
    answers = Counter()
    count = 0
    blocks = [b for b in re.split(r"\n\s*\n", text.replace("\r\n", "\n").strip()) if b.strip()]
    for i, block in enumerate(blocks, 1):
        lines = [l.rstrip() for l in block.split("\n")]
        question, options, answer_line = lines[0], lines[1:-1], lines[-1]
        where = f"câu {i} (\"{question[:40]}...\")"
        if OPTION_RE.match(question) or ANSWER_RE.match(question):
            errors.append(f"{where}: thiếu dòng câu hỏi hoặc câu hỏi bị xuống dòng")
            continue
        if re.match(r"^\s*(Câu|Question)\s*\d+", question, re.IGNORECASE):
            errors.append(f"{where}: không được đánh số 'Câu N' ở đầu câu hỏi")
        bad = [o for o in options if not OPTION_RE.match(o)]
        if bad:
            errors.append(f"{where}: dòng không đúng dạng 'A. ...' hoặc câu hỏi nằm trên nhiều dòng: \"{bad[0][:40]}\"")
            continue
        letters = [OPTION_RE.match(o).group(1) for o in options]
        if len(letters) < 2:
            errors.append(f"{where}: cần ít nhất 2 phương án")
            continue
        if letters != [chr(ord("A") + k) for k in range(len(letters))]:
            errors.append(f"{where}: phương án phải theo thứ tự A, B, C, ...")
            continue
        m = ANSWER_RE.match(answer_line)
        if not m:
            errors.append(f"{where}: dòng cuối phải là 'ANSWER: X'")
            continue
        if m.group(1) not in letters:
            errors.append(f"{where}: đáp án {m.group(1)} không có trong các phương án")
            continue
        answers[m.group(1)] += 1
        count += 1
    return count, errors, answers


def check_required_files(course_dir: Path, r: Report):
    missing = [f for f in REQUIRED_FILES if not (course_dir / f).is_file()]
    if missing:
        r.error("Thiếu file: " + ", ".join(missing))
    else:
        r.ok("Đủ file bắt buộc (README, index, course.json, đề cương, đánh giá)")


def check_index(course_dir: Path, r: Report):
    index = course_dir / "index.html"
    if not index.is_file():
        return
    content = index.read_text(encoding="utf-8", errors="ignore")
    if not re.search(r"<title>.+?</title>", content, re.IGNORECASE | re.DOTALL):
        r.error("index.html thiếu thẻ <title> (portal không lấy được tên học phần)")
    if not re.search(r'<meta\s+name=["\']description["\']', content, re.IGNORECASE):
        r.warn("index.html thiếu <meta name=\"description\"> (portal sẽ đoán mô tả từ đoạn văn đầu)")


def check_lessons(course_dir: Path, r: Report, build) -> list[str]:
    lessons = build.list_lessons(course_dir)
    if not lessons:
        r.error("Chưa có file bài học bai-XX.md")
        return lessons

    expected = [f"{i:02d}" for i in range(1, len(lessons) + 1)]
    if lessons != expected:
        r.error(f"Số thứ tự bài không liên tục: {', '.join(lessons)}")

    structure_ok = True
    for n in lessons:
        md = (course_dir / f"bai-{n}.md").read_text(encoding="utf-8")
        summaries = [re.sub(r"<[^>]+>|\s+", " ", s).replace("&amp;", "&").strip()
                     for s in re.findall(r"<summary[^>]*>(.*?)</summary>", md, re.DOTALL)]
        for section in LESSON_SECTIONS:
            if not any(section in s for s in summaries):
                r.error(f"bai-{n}.md thiếu khối \"{section}\"")
                structure_ok = False
        if "<script" in md.lower():
            r.error(f"bai-{n}.md chứa <script> (Moodle sẽ chặn)")
            structure_ok = False
        if re.search(r'class="[^"]*\b(bg|text|px|py|flex|rounded)-', md):
            r.warn(f"bai-{n}.md dùng class Tailwind; Moodle không có Tailwind, hãy dùng inline style")
    if structure_ok:
        r.ok(f"{len(lessons)} bài học đủ 4 khối accordion")

    missing_html = [f"bai-{n}.html" for n in lessons if not (course_dir / f"bai-{n}.html").is_file()]
    if missing_html:
        r.error("Thiếu trang web: " + ", ".join(missing_html) + " (chạy build-lessons.py)")
    if (course_dir / "course.json").is_file():
        try:
            stale = build.build_course(course_dir, check_only=True)
        except ValueError as e:
            r.error(str(e))
        else:
            stale = [f for f in stale if f not in missing_html]
            if stale:
                r.error("Trang .html lệch với .md: " + ", ".join(stale) + " (chạy build-lessons.py)")
            elif not missing_html:
                r.ok("Mọi bai-XX.html đồng bộ với bai-XX.md")
    return lessons


def check_quizzes(course_dir: Path, lessons: list[str], r: Report):
    quiz_dir = course_dir / "quiz"
    total = 0
    all_ok = True
    for n in lessons:
        quiz = quiz_dir / f"quiz-bai-{n}-aiken.txt"
        if not quiz.is_file():
            r.error(f"Thiếu quiz/{quiz.name}")
            all_ok = False
            continue
        count, errors, answers = parse_aiken(quiz.read_text(encoding="utf-8"))
        total += count
        for e in errors:
            r.error(f"{quiz.name}: {e}")
            all_ok = False
        if count < MIN_QUIZ_QUESTIONS:
            r.error(f"{quiz.name}: chỉ có {count} câu hợp lệ (tối thiểu {MIN_QUIZ_QUESTIONS})")
            all_ok = False
        if count >= 4:
            letter, top = answers.most_common(1)[0]
            if top / count > 0.5:
                r.warn(f"{quiz.name}: {top}/{count} câu có đáp án {letter}; nên chia đều A/B/C/D")
    if lessons and all_ok:
        r.ok(f"Quiz đủ {len(lessons)} bài, {total} câu, đúng định dạng Aiken")

    summary_files = list(quiz_dir.glob("tong-hop-*-aiken.txt")) if quiz_dir.is_dir() else []
    if lessons and not summary_files:
        r.warn("Chưa có file quiz tổng hợp quiz/tong-hop-<N>-cau-quiz-aiken.txt")
    if lessons and quiz_dir.is_dir() and not (quiz_dir / "index.html").is_file():
        r.warn("Chưa có trang tải ngân hàng câu hỏi quiz/index.html (chạy build-quiz.py)")
    for f in summary_files:
        count, errors, _ = parse_aiken(f.read_text(encoding="utf-8"))
        if errors:
            r.error(f"{f.name}: {len(errors)} lỗi định dạng (ví dụ: {errors[0]})")
        elif count != total:
            r.warn(f"{f.name}: có {count} câu, trong khi tổng các bài là {total}; hãy ghép lại")


def check_slides(course_dir: Path, lessons: list[str], r: Report):
    """Chỉ kiểm tra khi course.json bật "slides": true."""
    config_file = course_dir / "course.json"
    try:
        enabled = json.loads(config_file.read_text(encoding="utf-8")).get("slides")
    except (OSError, ValueError):
        return
    if not enabled:
        return
    slides_dir = course_dir / "Slides"
    missing, stale = [], []
    for n in lessons:
        md, pptx = slides_dir / f"bai-{n}.markdown", slides_dir / f"bai-{n}.pptx"
        if not md.is_file():
            missing.append(md.name)
        elif not pptx.is_file() or pptx.stat().st_mtime < md.stat().st_mtime:
            stale.append(pptx.name)
    no_image = []
    for md in sorted(slides_dir.glob("bai-*.markdown")):
        text = re.sub(r"```.*?```", "", md.read_text(encoding="utf-8"), flags=re.DOTALL)
        for path in re.findall(r"^\s*!\[[^\]]*\]\(\s*<?([^)>]+?)>?\s*\)\s*$", text, re.MULTILINE):
            if re.match(r"^https?://", path, re.IGNORECASE) or not (slides_dir / path).is_file():
                no_image.append(f"{md.name} → {path}")
    if no_image:
        r.warn("Slide tham chiếu hình chưa có trong Slides/ (đang hiện khung chờ): " + "; ".join(no_image))
    if missing:
        r.error("Thiếu ghi chú slide: " + ", ".join(f"Slides/{m}" for m in missing))
    if stale:
        r.error("Slide .pptx chưa có hoặc cũ hơn .markdown: " + ", ".join(stale) + " (chạy build-slides.py)")
    if lessons and not missing and not stale:
        r.ok(f"Slide đủ {len(lessons)} bài (.markdown + .pptx)")


TEXTBOOK_SECTIONS = ["Mục tiêu chương", "Tóm tắt chương", "Câu hỏi ôn tập", "Bài tập", "Tài liệu tham khảo"]


def check_textbook(course_dir: Path, r: Report):
    """Giáo trình (giao-trinh/chuong-XX.md): đủ mục bắt buộc, trích dẫn [n] khớp danh mục tài liệu tham khảo.
    Xem skill giao-trinh-builder (Thông tư 62/2026/TT-BGDĐT, Điều 5)."""
    src = course_dir / "giao-trinh"
    chapters = sorted(src.glob("chuong-*.md")) if src.is_dir() else []
    if not chapters:
        return
    problems = []
    for ch in chapters:
        text = ch.read_text(encoding="utf-8")
        headings = re.findall(r"(?m)^##\s+(.+?)\s*$", text)
        missing = [s for s in TEXTBOOK_SECTIONS if not any(h.startswith(s) for h in headings)]
        if missing:
            problems.append(f"{ch.name} thiếu mục: {', '.join(missing)}")
        body, _, refs = text.partition("## Tài liệu tham khảo")
        body = re.sub(r"`[^`\n]*`", "", re.sub(r"```.*?```", "", body, flags=re.DOTALL))  # arr[0] trong code không phải trích dẫn
        listed = set(re.findall(r"(?m)^\[(\d+)\]", refs))
        cited = set(re.findall(r"\[(\d+)(?:,[^\]\n]*)?\]", body))  # [6] hoặc [6, Điều 32]
        if cited - listed:
            problems.append(f"{ch.name} trích dẫn không có trong danh mục: [{'], ['.join(sorted(cited - listed, key=int))}]")
        if listed - cited:
            problems.append(f"{ch.name} tài liệu không được trích dẫn: [{'], ['.join(sorted(listed - cited, key=int))}]")
    for p in problems:
        r.warn("Giáo trình: " + p)
    docx = list(src.glob("*.docx"))
    if docx and any(ch.stat().st_mtime > max(d.stat().st_mtime for d in docx) for ch in chapters):
        r.warn("Giáo trình .docx cũ hơn file chương .md (chạy build-textbook.py)")
    if not problems:
        r.ok(f"Giáo trình {len(chapters)} chương đủ mục bắt buộc, trích dẫn khớp tài liệu tham khảo")


def check_documents(course_dir: Path, r: Report):
    """"documents" trong course.json phải trỏ tới file có thật (dùng để thay placeholder trên trang web)."""
    config_file = course_dir / "course.json"
    docs = json.loads(config_file.read_text(encoding="utf-8")).get("documents") if config_file.is_file() else None
    if not docs:
        return
    missing = [f"{k} → {rel}" for k, rel in docs.items() if not (course_dir / rel).is_file()]
    if missing:
        r.error("documents trong course.json trỏ tới file không tồn tại: " + "; ".join(missing))
    else:
        r.ok(f"{len(docs)} tài liệu trong course.json đều có file ({', '.join(docs)})")


def check_links_and_placeholders(course_dir: Path, r: Report):
    samples = sample_links()
    reused = {}
    placeholders = {}
    for f in sorted(course_dir.rglob("*")):
        if f.suffix not in (".md", ".html", ".txt", ".json") or not f.is_file() or f.name == "template-lesson.md":
            continue
        if "node_modules" in f.parts:
            continue
        # Trang .html sinh từ .md đã được kiểm tra đồng bộ ở trên, không báo trùng
        if f.suffix == ".html" and f.with_suffix(".md").is_file():
            continue
        content = f.read_text(encoding="utf-8", errors="ignore")
        rel = f.relative_to(course_dir).as_posix()
        hits = sorted(h for h in samples if h in content)
        if hits:
            reused[rel] = hits
        found = sorted(set(PLACEHOLDER_RE.findall(content)))
        if found:
            placeholders[rel] = found
    for rel, hits in reused.items():
        r.warn(f"{rel} dùng link mẫu của template-lesson.md: {', '.join(hits)}")
    for rel, found in placeholders.items():
        r.warn(f"{rel} còn placeholder chưa điền: {', '.join(found)}")
    if not reused and not placeholders:
        r.ok("Không còn link mẫu hoặc placeholder chưa điền")


def validate(course_dir: Path, build) -> Report:
    r = Report(course_dir.name)
    check_required_files(course_dir, r)
    check_index(course_dir, r)
    lessons = check_lessons(course_dir, r, build)
    check_quizzes(course_dir, lessons, r)
    check_slides(course_dir, lessons, r)
    check_documents(course_dir, r)
    check_textbook(course_dir, r)
    check_links_and_placeholders(course_dir, r)
    return r


def discover_courses() -> list[Path]:
    return sorted(d for d in ROOT_DIR.iterdir()
                  if d.is_dir() and not d.name.startswith(".") and d.name not in IGNORE_DIRS
                  and (d / "index.html").is_file())


def main():
    parser = argparse.ArgumentParser(description="Kiểm tra học phần LMS")
    parser.add_argument("courses", nargs="*", help="Thư mục học phần (mặc định: mọi học phần có index.html)")
    args = parser.parse_args()

    build = load_build_module()
    course_dirs = [ROOT_DIR / c.strip("/\\") for c in args.courses] or discover_courses()
    exit_code = 0
    for course_dir in course_dirs:
        if not course_dir.is_dir():
            print(f"[LỖI] Không tìm thấy thư mục {course_dir.name}")
            exit_code = 1
            continue
        report = validate(course_dir, build)
        report.print()
        if report.errors:
            exit_code = 1
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
