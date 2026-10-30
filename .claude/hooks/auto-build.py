"""
PostToolUse hook: sau khi Claude sửa bai-XX.md, quiz/quiz-bai-XX-aiken.txt, Slides/bai-XX.markdown hoặc rubric/rubric.json,
tự chạy build-lessons.py / build-quiz.py / build-slides.py / build-rubric.py cho đúng học phần đó.
"""
import re
import sys
import json
import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
LESSON_RE = re.compile(r"^([^/]+)/(bai-\d{2}|thong-tin-hoc-phan|danh-gia-hoc-phan)\.md$")
QUIZ_RE = re.compile(r"^([^/]+)/quiz/quiz-bai-\d{2}-aiken\.txt$")
SLIDES_RE = re.compile(r"^([^/]+)/Slides/bai-(\d{2})\.markdown$")
RUBRIC_RE = re.compile(r"^([^/]+)/rubric/rubric\.json$")


def main():
    try:
        payload = json.loads(sys.stdin.buffer.read().decode("utf-8"))
        file_path = Path(payload["tool_input"]["file_path"]).resolve()
        rel = file_path.relative_to(ROOT_DIR).as_posix()
    except (ValueError, KeyError, TypeError):
        return 0

    python = [sys.executable]
    # python-pptx không có sẵn trong môi trường của hook nên build slide chạy qua uv
    pptx_python = ["uv", "run", "--no-project", "--with", "python-pptx", "python"]
    if m := LESSON_RE.match(rel):
        commands = [(python, ["build-lessons.py", m.group(1)])]
    elif m := QUIZ_RE.match(rel):
        # Trang bài học nhúng đề luyện tập từ file quiz nên phải build lại cả trang
        commands = [(python, ["build-quiz.py", m.group(1)]), (python, ["build-lessons.py", m.group(1)])]
    elif m := SLIDES_RE.match(rel):
        commands = [(pptx_python, ["build-slides.py", m.group(1), m.group(2)])]
    elif m := RUBRIC_RE.match(rel):
        # rubric.json là nguồn của cả file Excel và trang cham-diem.html
        xlsx_python = ["uv", "run", "--no-project", "--with", "openpyxl", "python"]
        commands = [(xlsx_python, ["build-rubric.py", m.group(1)])]
    else:
        return 0

    messages = []
    for interpreter, command in commands:
        result = subprocess.run(interpreter + [str(ROOT_DIR / command[0]), *command[1:]],
                                cwd=ROOT_DIR, capture_output=True, encoding="utf-8", errors="replace")
        output = (result.stdout + result.stderr).strip()
        status = "OK" if result.returncode == 0 else "LỖI"
        messages.append(f"[auto-build {status}] {' '.join(command)}: {output}")
        if result.returncode != 0:
            break
    message = "\n".join(messages)
    print(json.dumps({
        "systemMessage": message,
        "hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": message},
    }))  # ensure_ascii mặc định: tránh lỗi encoding cp1252 của console Windows
    return 0


if __name__ == "__main__":
    sys.exit(main())
