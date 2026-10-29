"""
Ghép ngân hàng câu hỏi Aiken của từng bài thành file tổng hợp, có thể cân bằng vị trí đáp án đúng.

Cách dùng:
    uv run python build-quiz.py nhap-mon-nganh              # ghép quiz/quiz-bai-XX-aiken.txt -> quiz/tong-hop-N-cau-quiz-aiken.txt
    uv run python build-quiz.py nhap-mon-nganh --balance    # xáo vị trí đáp án đúng cho đều A/B/C/D rồi mới ghép

Đồng thời sinh quiz/index.html (trang cho giảng viên tải file Aiken để import vào Moodle).
--balance chỉ đổi chỗ đáp án đúng với một phương án khác trong cùng câu, không đổi nội dung.
Kết quả cố định (seed theo tên file) nên chạy lại nhiều lần không làm thay đổi gì thêm.
"""
import re
import sys
import json
import html
import random
import argparse
from pathlib import Path

# Fix Windows console encoding for Vietnamese unicode characters
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if sys.stderr and hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

ROOT_DIR = Path(__file__).resolve().parent
QUIZ_RE = re.compile(r"^quiz-bai-(\d{2})-aiken\.txt$")
OPTION_RE = re.compile(r"^([A-Z])\.\s+(.*)$")
ANSWER_RE = re.compile(r"^ANSWER:\s*([A-Z])\s*$")
# Phương án nhắc tới phương án khác ("Cả A và B đều đúng") thì không được đổi chỗ
CROSS_REF_RE = re.compile(r"\b(cả|tất cả|both|all)\b.*\b[A-D]\b|\b[A-D]\s*(và|hoặc|and|or)\s*[A-D]\b", re.IGNORECASE)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig").replace("\r\n", "\n")


def parse_questions(text: str, source: str) -> list[dict]:
    questions = []
    for block in re.split(r"\n\s*\n", text.strip()):
        lines = [l.rstrip() for l in block.strip().split("\n")]
        options = [OPTION_RE.match(l) for l in lines[1:-1]]
        answer = ANSWER_RE.match(lines[-1])
        if len(lines) < 4 or not all(options) or not answer:
            raise ValueError(f"{source}: câu sai định dạng Aiken (chạy validate-course.py để xem chi tiết):\n{block}")
        questions.append({
            "question": lines[0],
            "options": [m.group(2) for m in options],
            "answer": ord(answer.group(1)) - ord("A"),
        })
    return questions


def format_questions(questions: list[dict]) -> str:
    blocks = []
    for q in questions:
        lines = [q["question"]]
        lines += [f"{chr(ord('A') + i)}. {opt}" for i, opt in enumerate(q["options"])]
        lines.append(f"ANSWER: {chr(ord('A') + q['answer'])}")
        blocks.append("\n".join(lines))
    return "\n\n".join(blocks) + "\n"


def balance_answers(questions: list[dict], seed: str) -> int:
    """Đổi chỗ đáp án đúng để vị trí phân bố đều. Trả về số câu bị thay đổi."""
    rng = random.Random(seed)
    movable = [q for q in questions if not any(CROSS_REF_RE.search(o) for o in q["options"])]
    n_options = min((len(q["options"]) for q in movable), default=0)
    if n_options < 2:
        return 0
    offset = rng.randrange(n_options)
    targets = [(i + offset) % n_options for i in range(len(movable))]
    rng.shuffle(targets)

    changed = 0
    for q, target in zip(movable, targets):
        if q["answer"] == target:
            continue
        opts = q["options"]
        opts[q["answer"]], opts[target] = opts[target], opts[q["answer"]]
        q["answer"] = target
        changed += 1
    return changed


def build_quiz(course_dir: Path, balance: bool) -> Path:
    quiz_dir = course_dir / "quiz"
    files = sorted(f for f in quiz_dir.glob("quiz-bai-*-aiken.txt") if QUIZ_RE.match(f.name))
    if not files:
        raise FileNotFoundError(f"Không có file quiz-bai-XX-aiken.txt trong {quiz_dir.relative_to(ROOT_DIR)}")

    all_questions = []
    counts = []
    for f in files:
        questions = parse_questions(read_text(f), f.name)
        if balance:
            changed = balance_answers(questions, seed=f.name)
            if changed:
                f.write_text(format_questions(questions), encoding="utf-8", newline="\n")
            print(f"  [~] {f.name}: đổi vị trí đáp án {changed}/{len(questions)} câu")
        all_questions += questions
        counts.append((f, len(questions)))

    for old in quiz_dir.glob("tong-hop-*-aiken.txt"):
        old.unlink()
    summary = quiz_dir / f"tong-hop-{len(all_questions)}-cau-quiz-aiken.txt"
    summary.write_text(format_questions(all_questions), encoding="utf-8", newline="\n")
    write_bank_page(course_dir, counts, summary, len(all_questions))
    return summary


BANK_ROW = '''        <li class="px-6 py-3 flex items-center justify-between gap-3">
          <div class="min-w-0">
            <div class="font-bold text-slate-800 text-sm">Bài {number}</div>
            <div class="text-xs text-slate-500 font-mono truncate">{name} · {count} câu</div>
          </div>
          <a href="{name}" download class="px-3 py-2 bg-lhu-light hover:bg-blue-100 text-lhu-blue font-bold rounded-xl text-xs flex items-center gap-1.5 flex-shrink-0"><i class="fa-solid fa-download"></i> Tải file</a>
        </li>'''


def write_bank_page(course_dir: Path, counts: list[tuple[Path, int]], summary: Path, total: int):
    """Sinh quiz/index.html: trang cho giảng viên tải file Aiken để import vào Moodle."""
    config_file = course_dir / "course.json"
    config = json.loads(config_file.read_text(encoding="utf-8")) if config_file.is_file() else {}
    rows = "\n".join(BANK_ROW.format(number=QUIZ_RE.match(f.name).group(1), name=f.name, count=n) for f, n in counts)
    values = {
        "COURSE_NAME": html.escape(config.get("name", course_dir.name)),
        "COURSE_CODE": html.escape(config.get("code", "")),
        "LANDING_PAGE": config.get("landingPage", "index.html"),
        "TOTAL": str(total),
        "LESSON_COUNT": str(len(counts)),
        "SUMMARY_FILE": summary.name,
        "ROWS": rows,
    }
    template = (ROOT_DIR / "templates" / "quiz-bank.html").read_text(encoding="utf-8")
    page = re.sub(r"\{\{([A-Z_]+)\}\}", lambda m: values.get(m.group(1), m.group(0)), template)
    (course_dir / "quiz" / "index.html").write_text(page, encoding="utf-8", newline="\n")


def main():
    parser = argparse.ArgumentParser(description="Ghép và cân bằng ngân hàng câu hỏi Aiken")
    parser.add_argument("course", help="Thư mục học phần")
    parser.add_argument("--balance", action="store_true", help="Cân bằng vị trí đáp án đúng A/B/C/D")
    args = parser.parse_args()

    course_dir = ROOT_DIR / args.course.strip("/\\")
    try:
        summary = build_quiz(course_dir, args.balance)
    except (FileNotFoundError, ValueError) as e:
        print(f"[LỖI] {e}")
        return 1
    print(f"[+] Đã ghi {summary.relative_to(ROOT_DIR)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
