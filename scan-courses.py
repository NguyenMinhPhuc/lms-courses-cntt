import os
import re
import sys
import json
from pathlib import Path

# Fix Windows console encoding for Vietnamese unicode characters
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if sys.stderr and hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

ROOT_DIR = Path(__file__).resolve().parent

IGNORE_DIRS = {
    ".git", ".gemini", ".vscode", ".idea", "node_modules", 
    "__pycache__", "dist", "build", "scratch"
}

def clean_text(text: str) -> str:
    if not text:
        return ""
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def parse_course_folder(folder_path: Path):
    folder_name = folder_path.name
    index_file = folder_path / "index.html"
    if not index_file.is_file():
        return None

    try:
        content = index_file.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        content = ""

    # Check for course-landingpage or syllabus if available
    course_landing = "course-landingpage.html" if (folder_path / "course-landingpage.html").is_file() else None
    if not course_landing and (folder_path / "landingpage.html").is_file():
        course_landing = "landingpage.html"
    
    syllabus_file = "thong-tin-hoc-phan.html" if (folder_path / "thong-tin-hoc-phan.html").is_file() else None
    assessment_file = "danh-gia-hoc-phan.html" if (folder_path / "danh-gia-hoc-phan.html").is_file() else None

    # Title extraction
    title = ""
    # Try finding <title>
    title_match = re.search(r"<title>(.*?)</title>", content, re.IGNORECASE | re.DOTALL)
    if title_match:
        raw_title = clean_text(title_match.group(1))
        # Remove suffix like "| Khoa CNTT - Đại học Lạc Hồng"
        title = raw_title.split("|")[0].split("-")[0].strip()
    
    # Try finding h1 or specific course title if title is generic
    if not title or "Ngành" in title or len(title) > 60:
        h1_match = re.search(r"<h1[^>]*>(.*?)</h1>", content, re.IGNORECASE | re.DOTALL)
        if h1_match:
            cand = clean_text(h1_match.group(1))
            if cand and len(cand) < 60:
                title = cand

    if not title:
        # Fallback to humanized folder name
        title = folder_name.replace("-", " ").replace("_", " ").title()

    # Description extraction
    desc = ""
    desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE)
    if desc_match:
        desc = clean_text(desc_match.group(1))
    
    if not desc:
        # Try finding first paragraph
        p_match = re.search(r"<p[^>]*>(.*?)</p>", content, re.IGNORECASE | re.DOTALL)
        if p_match:
            desc = clean_text(p_match.group(1))
            if len(desc) > 220:
                desc = desc[:217] + "..."

    # Course code extraction
    code = ""
    code_match = re.search(r"(?:Mã\s*(?:môn|học\s*phần|HP)?[:\s]+)(\d{5,7})", content, re.IGNORECASE)
    if code_match:
        code = code_match.group(1)
    else:
        # Check in syllabus_file if present
        if syllabus_file:
            syl_content = (folder_path / syllabus_file).read_text(encoding="utf-8", errors="ignore")
            syl_code = re.search(r"(?:Mã\s*(?:môn|học\s*phần|HP)?[:\s]+)(\d{5,7})", syl_content, re.IGNORECASE)
            if syl_code:
                code = syl_code.group(1)

    if not code:
        code = "CNTT"

    # Credits extraction
    credits = 3
    cred_match = re.search(r"(\d+)\s*(?:Tín\s*chỉ|tín\s*chỉ|TC)", content, re.IGNORECASE)
    if cred_match:
        try:
            credits = int(cred_match.group(1))
        except ValueError:
            pass

    # Tags & Icons
    tags = ["CNTT", "LHU"]
    if "abet" in content.lower():
        tags.append("ABET")
    if "ai" in content.lower() or "genai" in content.lower():
        tags.append("AI-First")
    if "web" in content.lower():
        tags.append("Web Dev")

    icons = {
        "nhap-mon-nganh": "fa-solid fa-microchip",
        "web": "fa-solid fa-globe",
        "data": "fa-solid fa-database",
        "ai": "fa-solid fa-brain",
        "net": "fa-solid fa-network-wired",
        "sec": "fa-solid fa-shield-halved"
    }

    icon = "fa-solid fa-book-bookmark"
    for key, ic in icons.items():
        if key in folder_name.lower():
            icon = ic
            break

    return {
        "id": folder_name,
        "code": code,
        "title": title,
        "englishTitle": folder_name.replace("-", " ").title(),
        "credits": credits,
        "hours": f"{credits * 15} tiết",
        "semester": "Chương trình Đào tạo CNTT",
        "folder": folder_name,
        "entryFile": "index.html",
        "courseLanding": course_landing,
        "syllabusFile": syllabus_file,
        "assessmentFile": assessment_file,
        "description": desc or f"Học phần {title} thuộc chương trình đào tạo Khoa CNTT - Đại học Lạc Hồng.",
        "instructor": "Bộ môn CNTT - LHU",
        "tags": list(dict.fromkeys(tags)),
        "badgeColor": "blue",
        "icon": icon
    }

def main():
    print(f"Scanning directory: {ROOT_DIR}")
    courses = []

    for item in sorted(ROOT_DIR.iterdir()):
        if item.is_dir() and item.name not in IGNORE_DIRS and not item.name.startswith("."):
            course_data = parse_course_folder(item)
            if course_data:
                courses.append(course_data)
                print(f"  [+] Discovered course: {course_data['title']} ({course_data['folder']})")

    # If nhap-mon-nganh has customized metadata, preserve it
    for c in courses:
        if c["id"] == "nhap-mon-nganh":
            c["title"] = "Nhập Môn Công Nghệ Thông Tin"
            c["code"] = "111106"
            c["credits"] = 3
            c["hours"] = "45 tiết (9 buổi)"
            c["semester"] = "Học kỳ 1 • Năm 1"
            c["instructor"] = "ThS. Nguyễn Minh Phúc"
            c["tags"] = ["ABET", "AI-First", "Vibe Coding", "Cơ sở ngành"]
            c["courseLanding"] = "course-landingpage.html"
            c["syllabusFile"] = "thong-tin-hoc-phan.html"
            c["assessmentFile"] = "danh-gia-hoc-phan.html"

    # Write courses.json
    json_path = ROOT_DIR / "courses.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(courses, f, ensure_ascii=False, indent=2)
    print(f"Updated {json_path} with {len(courses)} course(s).")

    # Write courses-data.js
    js_path = ROOT_DIR / "courses-data.js"
    js_content = f"""/**
 * LMS Courses CNTT - Auto-generated Course Registry Data
 * Tự động đồng bộ bởi scan-courses.py
 */
window.DEFAULT_COURSES = {json.dumps(courses, ensure_ascii=False, indent=2)};
"""
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"Updated {js_path} successfully.")

if __name__ == "__main__":
    main()
