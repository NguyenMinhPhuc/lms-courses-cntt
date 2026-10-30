"""
Sinh rubric chấm điểm theo CLO từ một nguồn duy nhất: <hoc-phan>/rubric/rubric.json

Cách dùng:
    uv run --with openpyxl python build-rubric.py lap-trinh-ung-dung-mobile

Đầu ra:
    <hoc-phan>/rubric/Rubric-<mã học phần>.xlsx   rubric + bảng điểm có công thức + mức đạt CLO
    <hoc-phan>/cham-diem.html                      công cụ chấm điểm trên web (từ templates/rubric-grading.html),
                                                   xuất điểm theo tiêu chí và CLO ra Excel

Kiểm tra: tổng điểm tiêu chí của mỗi CLO bằng điểm tối đa của CLO, tổng các CLO bằng thang điểm,
mỗi tiêu chí có đủ mô tả các mức, gợi ý chấm và minh chứng.

Hai dạng rubric.json:
- "clos": một bài đánh giá cuối kỳ, tiêu chí nhóm theo CLO, điểm tiêu chí = điểm tối đa × tỷ lệ mức
  (ví dụ lap-trinh-ung-dung-mobile).
- "components": nhiều thành phần đánh giá (A1, A2, A3…) có tỷ trọng; mỗi thành phần thang 10, điểm tiêu chí
  = hệ số mức (0–1) × trọng số; mỗi tiêu chí chia trọng số cho một hoặc nhiều CLO; "rules" giới hạn hệ số
  của một số tiêu chí khi có vi phạm (ví dụ co-so-van-hoa-viet-nam). Trang chấm dùng
  templates/rubric-components.html.
"""
import argparse
import json
import sys
from pathlib import Path

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT_DIR = Path(__file__).resolve().parent
TEMPLATE = ROOT_DIR / "templates" / "rubric-grading.html"
TEMPLATE_COMPONENTS = ROOT_DIR / "templates" / "rubric-components.html"
DATA_ROWS = 60  # số dòng sinh viên sẵn trong bảng điểm Excel


# ---------------------------------------------------------------- kiểm tra dữ liệu
def validate(rubric: dict) -> list[str]:
    errors = []
    level_codes = [lv["code"] for lv in rubric["levels"]]
    described = [c for c in level_codes if c != "0"]
    total = 0.0
    seen = set()
    for clo in rubric["clos"]:
        s = round(sum(c["max"] for c in clo["criteria"]), 4)
        total += clo["max"]
        if abs(s - clo["max"]) > 1e-9:
            errors.append(f"{clo['id']}: tổng tiêu chí {s} khác điểm tối đa {clo['max']}")
        for c in clo["criteria"]:
            if c["id"] in seen:
                errors.append(f"Trùng mã tiêu chí {c['id']}")
            seen.add(c["id"])
            if c["scope"] not in ("group", "individual"):
                errors.append(f"{c['id']}: scope phải là group hoặc individual")
            missing = [code for code in described if not c.get("levels", {}).get(code)]
            if missing:
                errors.append(f"{c['id']}: thiếu mô tả mức {', '.join(missing)}")
            for key in ("guide", "evidence"):
                if not c.get(key):
                    errors.append(f"{c['id']}: thiếu {key}")
    if abs(total - rubric["course"]["scale"]) > 1e-9:
        errors.append(f"Tổng điểm các CLO {total} khác thang điểm {rubric['course']['scale']}")
    return errors


# ---------------------------------------------------------------- Excel
def build_excel(rubric: dict, out: Path):
    from openpyxl import Workbook
    from openpyxl.formatting.rule import CellIsRule, FormulaRule
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter as col
    from openpyxl.worksheet.datavalidation import DataValidation

    course = rubric["course"]
    levels = rubric["levels"]
    described = [lv for lv in levels if lv["code"] != "0"]
    clos = rubric["clos"]
    criteria = [(clo, c) for clo in clos for c in clo["criteria"]]

    BLUE, DARK, LIGHT = "013D88", "01295C", "EEF5FC"
    CLO_FILL = ["E7F1FF", "EAFAF1", "FFF5EB", "F3E5F5"]
    thin = Side(style="thin", color="B8C4D6")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    wrap = Alignment(wrap_text=True, vertical="top")
    center = Alignment(horizontal="center", vertical="center", wrap_text=True)
    head_font = Font(bold=True, color="FFFFFF")
    head_fill = PatternFill("solid", fgColor=BLUE)
    scope_text = {"group": "Nhóm", "individual": "Cá nhân"}

    def header(ws, row, values, fill=head_fill, font=head_font):
        for i, v in enumerate(values, start=1):
            cell = ws.cell(row=row, column=i, value=v)
            cell.fill, cell.font, cell.alignment, cell.border = fill, font, center, border

    wb = Workbook()

    # ----- Hướng dẫn
    ws = wb.active
    ws.title = "Hướng dẫn"
    ws.column_dimensions["A"].width = 120
    lines = [
        (f"RUBRIC CHẤM ĐIỂM CUỐI KỲ - {course['name'].upper()} ({course['code']})", Font(bold=True, size=14, color=BLUE)),
        (course["assessment"], Font(italic=True)),
        ("", None),
        ("Cấu trúc", Font(bold=True, color=DARK)),
        (f"- {len(clos)} CLO, {len(criteria)} tiêu chí; mỗi tiêu chí chỉ chấm một vấn đề. Tổng điểm: {course['scale']}.", None),
        ("- " + "; ".join(f"{clo['id']} ({clo['plo']}): {clo['max']} điểm, {len(clo['criteria'])} tiêu chí" for clo in clos) + ".", None),
        ("- Mức chấm: " + "; ".join(f"{lv['code']} {lv['name']} = {int(lv['ratio'] * 100)}% điểm tối đa" for lv in levels) + ".", None),
        ("- Có thể cho điểm lẻ giữa hai mức (bước 0,05) khi minh chứng nằm giữa hai mô tả.", None),
        ("- Phạm vi 'Nhóm': chấm trên sản phẩm chung, mặc định cùng điểm cho cả nhóm; hạ riêng cho sinh viên không giải thích được phần mã liên quan.", None),
        ("- Phạm vi 'Cá nhân': chấm riêng từng sinh viên dựa trên minh chứng của chính sinh viên đó.", None),
        ("", None),
        ("Ngưỡng đạt", Font(bold=True, color=DARK)),
        (f"- {course['note']}", None),
        ("", None),
        ("Cách dùng file", Font(bold=True, color=DARK)),
        ("1. Sheet 'Rubric': mô tả mức, gợi ý chấm, minh chứng cần có của từng tiêu chí.", None),
        (f"2. Sheet 'Bảng điểm': nhập MSSV, họ tên, nhóm và điểm từng tiêu chí (0 đến điểm tối đa, có kiểm tra dữ liệu). Điểm CLO, tổng, Đạt/Chưa đạt tự tính. Sẵn {DATA_ROWS} dòng.", None),
        ("3. Sheet 'Mức đạt CLO': tỷ lệ sinh viên đạt từng CLO và kết luận đạt ở cấp lớp; điểm trung bình theo tiêu chí.", None),
        ("4. Có thể chấm trên trang web cham-diem.html của học phần rồi xuất Excel; file xuất có cùng cấu trúc cột.", None),
    ]
    for r, (text, font) in enumerate(lines, start=1):
        cell = ws.cell(row=r, column=1, value=text)
        cell.alignment = Alignment(wrap_text=True)
        if font:
            cell.font = font

    # ----- Rubric
    ws = wb.create_sheet("Rubric")
    cols = ["Mã", "Tiêu chí", "Phạm vi", "Điểm tối đa"] + [f"{lv['code']} - {lv['name']} ({int(lv['ratio'] * 100)}%)" for lv in described] + ["Gợi ý chấm", "Minh chứng cần có"]
    widths = [7, 26, 10, 9] + [34] * len(described) + [40, 34]
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[col(i)].width = w
    header(ws, 1, cols)
    r = 2
    for k, clo in enumerate(clos):
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=len(cols))
        cell = ws.cell(row=r, column=1, value=f"{clo['id']} ({clo['plo']}) - {clo['name']} - {clo['max']} điểm (đạt khi ≥ {clo['max'] * course['studentThreshold']:g})")
        cell.font = Font(bold=True, color=DARK)
        cell.fill = PatternFill("solid", fgColor=CLO_FILL[k % 4])
        cell.alignment = Alignment(vertical="center", wrap_text=True)
        ws.row_dimensions[r].height = 30
        r += 1
        for c in clo["criteria"]:
            values = [c["id"], c["name"], scope_text[c["scope"]], c["max"]] + [c["levels"][lv["code"]] for lv in described] + [c["guide"], c["evidence"]]
            for i, v in enumerate(values, start=1):
                cell = ws.cell(row=r, column=i, value=v)
                cell.alignment, cell.border = (center if i in (1, 3, 4) else wrap), border
            ws.cell(row=r, column=2).font = Font(bold=True)
            r += 1
    ws.freeze_panes = "C2"

    # ----- Bảng điểm
    ws = wb.create_sheet("Bảng điểm")
    info_cols = ["STT", "MSSV", "Họ và tên", "Nhóm"]
    first_crit = len(info_cols) + 1
    crit_col = {}
    c_idx = first_crit
    for clo, c in criteria:
        crit_col[c["id"]] = c_idx
        c_idx += 1
    clo_col = {clo["id"]: c_idx + i for i, clo in enumerate(clos)}
    total_col = c_idx + len(clos)
    pass_col = {clo["id"]: total_col + 1 + i for i, clo in enumerate(clos)}
    note_col = total_col + 1 + len(clos)
    last_col = note_col

    # Hàng 1: nhóm CLO; hàng 2: tiêu chí; hàng 3: điểm tối đa
    for i, name in enumerate(info_cols, start=1):
        ws.merge_cells(start_row=1, start_column=i, end_row=3, end_column=i)
    header(ws, 1, info_cols)
    for k, clo in enumerate(clos):
        ids = [c["id"] for c in clo["criteria"]]
        a, b = crit_col[ids[0]], crit_col[ids[-1]]
        ws.merge_cells(start_row=1, start_column=a, end_row=1, end_column=b)
        cell = ws.cell(row=1, column=a, value=f"{clo['id']} ({clo['max']} điểm)")
        for cc in range(a, b + 1):
            ws.cell(row=1, column=cc).fill = PatternFill("solid", fgColor=CLO_FILL[k % 4])
            ws.cell(row=1, column=cc).border = border
        cell.font, cell.alignment = Font(bold=True, color=DARK), center
        for c in clo["criteria"]:
            x = crit_col[c["id"]]
            h = ws.cell(row=2, column=x, value=f"{c['id']} {c['name']}" + (" (CN)" if c["scope"] == "individual" else ""))
            h.alignment, h.border, h.font = center, border, Font(bold=True, size=9)
            h.fill = PatternFill("solid", fgColor=CLO_FILL[k % 4])
            m = ws.cell(row=3, column=x, value=c["max"])
            m.alignment, m.border, m.font = center, border, Font(italic=True, size=9)
            ws.column_dimensions[col(x)].width = 11
    for title, colmap, fill in (("Điểm CLO", clo_col, "D6E4F5"), ("Đạt CLO", pass_col, "FCE8C8")):
        a, b = min(colmap.values()), max(colmap.values())
        ws.merge_cells(start_row=1, start_column=a, end_row=1, end_column=b)
        cell = ws.cell(row=1, column=a, value=title)
        cell.font, cell.alignment = Font(bold=True, color=DARK), center
        for clo in clos:
            x = colmap[clo["id"]]
            ws.cell(row=1, column=x).fill = PatternFill("solid", fgColor=fill)
            ws.cell(row=1, column=x).border = border
            h = ws.cell(row=2, column=x, value=clo["id"])
            h.font, h.alignment, h.border, h.fill = Font(bold=True), center, border, PatternFill("solid", fgColor=fill)
            m = ws.cell(row=3, column=x, value=clo["max"] if colmap is clo_col else f"≥ {clo['max'] * course['studentThreshold']:g}")
            m.alignment, m.border, m.font = center, border, Font(italic=True, size=9)
            ws.column_dimensions[col(x)].width = 10
    for x, title, sub in ((total_col, f"Tổng ({course['scale']})", course["scale"]), (note_col, "Ghi chú", "")):
        ws.merge_cells(start_row=1, start_column=x, end_row=2, end_column=x)
        cell = ws.cell(row=1, column=x, value=title)
        cell.fill, cell.font, cell.alignment, cell.border = head_fill, head_font, center, border
        m = ws.cell(row=3, column=x, value=sub)
        m.alignment, m.border = center, border
    ws.column_dimensions[col(total_col)].width = 10
    ws.column_dimensions[col(note_col)].width = 30
    for i, w in enumerate([5, 12, 24, 8], start=1):
        ws.column_dimensions[col(i)].width = w
    ws.row_dimensions[2].height = 75

    first, last = 4, 3 + DATA_ROWS
    for r in range(first, last + 1):
        ws.cell(row=r, column=1, value=r - first + 1).alignment = center
        for x in range(1, last_col + 1):
            ws.cell(row=r, column=x).border = border
        for clo in clos:
            ids = [c["id"] for c in clo["criteria"]]
            rng = f"{col(crit_col[ids[0]])}{r}:{col(crit_col[ids[-1]])}{r}"
            # Chỉ tính điểm CLO khi đã chấm đủ mọi tiêu chí của CLO
            ws.cell(row=r, column=clo_col[clo["id"]], value=f'=IF(COUNT({rng})={len(ids)},ROUND(SUM({rng}),2),"")')
            cref = f"{col(clo_col[clo['id']])}{r}"
            ws.cell(row=r, column=pass_col[clo["id"]], value=f'=IF({cref}="","",IF({cref}>={clo["max"] * course["studentThreshold"]},"Đạt","Chưa đạt"))')
        crng = f"{col(min(clo_col.values()))}{r}:{col(max(clo_col.values()))}{r}"
        ws.cell(row=r, column=total_col, value=f'=IF(COUNT({crng})={len(clos)},ROUND(SUM({crng}),2),"")').font = Font(bold=True)
        for x in list(clo_col.values()) + list(pass_col.values()) + [total_col]:
            ws.cell(row=r, column=x).alignment = center

    for clo, c in criteria:
        letter = col(crit_col[c["id"]])
        dv = DataValidation(type="decimal", operator="between", formula1="0", formula2=str(c["max"]), allow_blank=True,
                            showErrorMessage=True, errorTitle="Điểm không hợp lệ",
                            error=f"Tiêu chí {c['id']}: nhập từ 0 đến {c['max']}")
        ws.add_data_validation(dv)
        dv.add(f"{letter}{first}:{letter}{last}")
    red = PatternFill("solid", fgColor="FDE2E1")
    green = PatternFill("solid", fgColor="E3F6E8")
    prng = f"{col(min(pass_col.values()))}{first}:{col(max(pass_col.values()))}{last}"
    ws.conditional_formatting.add(prng, CellIsRule(operator="equal", formula=['"Chưa đạt"'], fill=red, font=Font(color="B42318", bold=True)))
    ws.conditional_formatting.add(prng, CellIsRule(operator="equal", formula=['"Đạt"'], fill=green, font=Font(color="067647")))
    ws.freeze_panes = ws.cell(row=first, column=first_crit)

    # ----- Mức đạt CLO
    ws2 = wb.create_sheet("Mức đạt CLO")
    for i, w in enumerate([10, 50, 12, 14, 14, 14, 12, 14, 18], start=1):
        ws2.column_dimensions[col(i)].width = w
    ws2.cell(row=1, column=1, value=f"MỨC ĐẠT CLO - {course['name']} ({course['code']})").font = Font(bold=True, size=13, color=BLUE)
    ws2.cell(row=2, column=1, value=course["note"]).font = Font(italic=True)
    header(ws2, 4, ["CLO", "Nội dung", "Điểm tối đa", "Ngưỡng SV đạt", "Số SV có điểm", "Số SV đạt", "Tỷ lệ đạt", "Điểm TB", "Kết luận cấp lớp"])
    sheet = "'Bảng điểm'"
    for i, clo in enumerate(clos):
        r = 5 + i
        sc = f"{sheet}!{col(clo_col[clo['id']])}{first}:{col(clo_col[clo['id']])}{last}"
        pc = f"{sheet}!{col(pass_col[clo['id']])}{first}:{col(pass_col[clo['id']])}{last}"
        values = [clo["id"], clo["name"], clo["max"], clo["max"] * course["studentThreshold"], f"=COUNT({sc})", f'=COUNTIF({pc},"Đạt")',
                  f'=IF(E{r}=0,"",F{r}/E{r})', f'=IF(E{r}=0,"",ROUND(AVERAGE({sc}),2))',
                  f'=IF(E{r}=0,"",IF(G{r}>={course["classThreshold"]},"Đạt","Chưa đạt"))']
        for x, v in enumerate(values, start=1):
            cell = ws2.cell(row=r, column=x, value=v)
            cell.border, cell.alignment = border, (wrap if x == 2 else center)
        ws2.cell(row=r, column=7).number_format = "0.0%"
    concl = f"I5:I{4 + len(clos)}"
    ws2.conditional_formatting.add(concl, CellIsRule(operator="equal", formula=['"Chưa đạt"'], fill=red, font=Font(color="B42318", bold=True)))
    ws2.conditional_formatting.add(concl, CellIsRule(operator="equal", formula=['"Đạt"'], fill=green, font=Font(color="067647", bold=True)))

    r0 = 7 + len(clos)
    ws2.cell(row=r0 - 1, column=1, value="Điểm trung bình theo tiêu chí").font = Font(bold=True, color=DARK)
    header(ws2, r0, ["Mã", "Tiêu chí", "Điểm tối đa", "Phạm vi", "Số SV có điểm", "Điểm TB", "TB / tối đa"])
    for i, (clo, c) in enumerate(criteria):
        r = r0 + 1 + i
        rng = f"{sheet}!{col(crit_col[c['id']])}{first}:{col(crit_col[c['id']])}{last}"
        values = [c["id"], c["name"], c["max"], scope_text[c["scope"]], f"=COUNT({rng})",
                  f'=IF(E{r}=0,"",ROUND(AVERAGE({rng}),2))', f'=IF(E{r}=0,"",F{r}/C{r})']
        for x, v in enumerate(values, start=1):
            cell = ws2.cell(row=r, column=x, value=v)
            cell.border, cell.alignment = border, (wrap if x == 2 else center)
        ws2.cell(row=r, column=7).number_format = "0%"
    low = f"G{r0 + 1}:G{r0 + len(criteria)}"
    ws2.conditional_formatting.add(low, FormulaRule(formula=[f'AND(ISNUMBER(G{r0 + 1}),G{r0 + 1}<{course["studentThreshold"]})'], fill=red))

    wb.active = wb.sheetnames.index("Bảng điểm")
    wb.save(out)


# ---------------------------------------------------------------- HTML
def build_html(rubric: dict, out: Path):
    html = TEMPLATE.read_text(encoding="utf-8")
    data = json.dumps(rubric, ensure_ascii=False).replace("</", "<\\/")
    course = rubric["course"]
    html = (html.replace("__RUBRIC_JSON__", data)
                .replace("__COURSE_NAME__", course["name"])
                .replace("__COURSE_CODE__", course["code"]))
    out.write_text(html, encoding="utf-8")


# ================================================================ rubric nhiều thành phần
def validate_components(rubric: dict) -> list[str]:
    errors = []
    scale = rubric["course"]["scale"]
    level_codes = [lv["code"] for lv in rubric["levels"]]
    clo_ids = {clo["id"] for clo in rubric["clos"]}
    seen = set()
    total_weight = 0.0
    for comp in rubric["components"]:
        total_weight += comp["weight"]
        s = round(sum(c["weight"] for c in comp["criteria"]), 4)
        if abs(s - scale) > 1e-9:
            errors.append(f"{comp['id']}: tổng trọng số tiêu chí {s} khác thang điểm {scale}")
        for c in comp["criteria"]:
            if c["id"] in seen:
                errors.append(f"Trùng mã tiêu chí {c['id']}")
            seen.add(c["id"])
            if c["scope"] not in ("group", "individual"):
                errors.append(f"{c['id']}: scope phải là group hoặc individual")
            unknown = set(c.get("clo", {})) - clo_ids
            if unknown:
                errors.append(f"{c['id']}: CLO không có trong danh sách: {', '.join(sorted(unknown))}")
            if c.get("clo") and abs(sum(c["clo"].values()) - c["weight"]) > 1e-9:
                errors.append(f"{c['id']}: tổng trọng số CLO {sum(c['clo'].values())} khác trọng số tiêu chí {c['weight']}")
            missing = [code for code in level_codes if not c.get("levels", {}).get(code)]
            if missing:
                errors.append(f"{c['id']}: thiếu mô tả mức {', '.join(missing)}")
            for key in ("guide", "evidence"):
                if not c.get(key):
                    errors.append(f"{c['id']}: thiếu {key}")
    if abs(total_weight - 1) > 1e-9:
        errors.append(f"Tổng tỷ trọng các thành phần {total_weight} khác 1")
    comp_ids = {comp["id"] for comp in rubric["components"]}
    for rule in rubric.get("rules", []):
        if rule["component"] not in comp_ids:
            errors.append(f"Quy tắc {rule['id']}: không có thành phần {rule['component']}")
        for cid in rule["cap"]["criteria"]:
            if cid not in seen:
                errors.append(f"Quy tắc {rule['id']}: không có tiêu chí {cid}")
    return errors


def clo_max(rubric: dict) -> dict:
    """Điểm tối đa của từng CLO trên thang điểm học phần (đã nhân tỷ trọng thành phần)."""
    out = {clo["id"]: 0.0 for clo in rubric["clos"]}
    for comp in rubric["components"]:
        for c in comp["criteria"]:
            for k, w in c.get("clo", {}).items():
                out[k] += comp["weight"] * w
    return {k: round(v, 4) for k, v in out.items()}


def build_excel_components(rubric: dict, out: Path) -> int:
    from openpyxl import Workbook
    from openpyxl.formatting.rule import CellIsRule
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter as col
    from openpyxl.worksheet.datavalidation import DataValidation

    course = rubric["course"]
    levels = rubric["levels"]
    clos = rubric["clos"]
    comps = rubric["components"]
    rules = rubric.get("rules", [])
    cmax = clo_max(rubric)

    BLUE, DARK = "013D88", "01295C"
    FILLS = ["E7F1FF", "EAFAF1", "FFF5EB", "F3E5F5"]
    thin = Side(style="thin", color="B8C4D6")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    wrap = Alignment(wrap_text=True, vertical="top")
    center = Alignment(horizontal="center", vertical="center", wrap_text=True)
    head_font = Font(bold=True, color="FFFFFF")
    head_fill = PatternFill("solid", fgColor=BLUE)
    red = PatternFill("solid", fgColor="FDE2E1")
    green = PatternFill("solid", fgColor="E3F6E8")
    scope_text = {"group": "Nhóm", "individual": "Cá nhân"}

    def pct(w):
        return f"{w * 100:g}%"

    def clo_text(c):
        return " + ".join(f"{k} ({w:g})" for k, w in c.get("clo", {}).items()) or "Không gắn CLO"

    def header(ws, row, values):
        for i, v in enumerate(values, start=1):
            cell = ws.cell(row=row, column=i, value=v)
            cell.fill, cell.font, cell.alignment, cell.border = head_fill, head_font, center, border

    def head_block(ws, x, title, sub, width=12):
        ws.merge_cells(start_row=1, start_column=x, end_row=2, end_column=x)
        h = ws.cell(row=1, column=x, value=title)
        h.fill, h.font, h.alignment, h.border = head_fill, head_font, center, border
        m = ws.cell(row=3, column=x, value=sub)
        m.alignment, m.border, m.font = center, border, Font(italic=True, size=9)
        ws.column_dimensions[col(x)].width = width

    wb = Workbook()

    # ----- Hướng dẫn
    ws = wb.active
    ws.title = "Hướng dẫn"
    ws.column_dimensions["A"].width = 120
    lines = [
        (f"RUBRIC ĐÁNH GIÁ HỌC PHẦN - {course['name'].upper()} ({course['code']})", Font(bold=True, size=14, color=BLUE)),
        (course["assessment"], Font(italic=True)),
        ("", None),
        ("Cấu trúc", Font(bold=True, color=DARK)),
        *[(f"- {comp['id']} {comp['name']} ({pct(comp['weight'])}): {len(comp['criteria'])} tiêu chí, thang {course['scale']}. {comp.get('when', '')}", None) for comp in comps],
        ("- Mức chấm (hệ số): " + "; ".join(f"{lv['name']} {lv['min']:g}–{lv['max']:g}" for lv in levels) + ". Điểm tiêu chí = hệ số × trọng số.", None),
        *[(f"- Quy tắc: {r['label']} → tiêu chí {', '.join(r['cap']['criteria'])} tối đa hệ số {r['cap']['max']:g}. Ghi 'x' ở cột vi phạm của sheet {r['component']}.", None) for r in rules],
        ("- Phạm vi 'Nhóm': chấm trên sản phẩm chung, thường cùng hệ số cho cả nhóm; 'Cá nhân': chấm riêng từng sinh viên.", None),
        (f"- {course['aiNote']}" if course.get("aiNote") else "", None),
        ("", None),
        ("Điểm theo CLO và ngưỡng đạt", Font(bold=True, color=DARK)),
        ("- Điểm tối đa của CLO trên thang học phần (đã nhân tỷ trọng thành phần): " + "; ".join(f"{k} {v:g}" for k, v in cmax.items())
         + f". Phần còn lại ({course['scale'] - sum(cmax.values()):g}) thuộc các tiêu chí không gắn CLO.", None),
        (f"- {course['note']}", None),
        ("", None),
        ("Cách dùng file", Font(bold=True, color=DARK)),
        ("1. Sheet 'Danh sách': nhập MSSV, họ tên, nhóm một lần. Các sheet thành phần và 'Tổng hợp' tự lấy theo cùng dòng.", None),
        ("2. Sheet từng thành phần: nhập HỆ SỐ của mỗi tiêu chí (0 đến 1, ví dụ 0,8). Điểm thành phần chỉ hiện khi đã chấm đủ tiêu chí.", None),
        ("3. Sheet 'Tổng hợp': điểm từng thành phần, điểm học phần, điểm và kết luận Đạt/Chưa đạt từng CLO.", None),
        ("4. Sheet 'Mức đạt CLO': tỷ lệ sinh viên đạt và kết luận cấp lớp.", None),
        ("5. Có thể chấm trên trang web cham-diem.html của học phần rồi xuất Excel.", None),
    ]
    for r, (text, font) in enumerate(lines, start=1):
        cell = ws.cell(row=r, column=1, value=text)
        cell.alignment = Alignment(wrap_text=True)
        if font:
            cell.font = font

    # ----- Rubric
    ws = wb.create_sheet("Rubric")
    cols = ["Mã", "Tiêu chí", "CLO (trọng số)", "Phạm vi", "Trọng số"] + [f"{lv['name']} ({lv['min']:g}–{lv['max']:g})" for lv in levels] + ["Gợi ý chấm", "Minh chứng"]
    for i, w in enumerate([8, 30, 16, 9, 9] + [30] * len(levels) + [38, 30], start=1):
        ws.column_dimensions[col(i)].width = w
    header(ws, 1, cols)
    r = 2
    for k, comp in enumerate(comps):
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=len(cols))
        cell = ws.cell(row=r, column=1, value=f"{comp['id']}. {comp['name']} - {pct(comp['weight'])} điểm học phần, thang {course['scale']} · {comp.get('when', '')}")
        cell.font, cell.fill = Font(bold=True, color=DARK), PatternFill("solid", fgColor=FILLS[k % 4])
        r += 1
        for c in comp["criteria"]:
            values = [c["label"], c["name"], clo_text(c), scope_text[c["scope"]], c["weight"]] + [c["levels"][lv["code"]] for lv in levels] + [c["guide"], c["evidence"]]
            for i, v in enumerate(values, start=1):
                cell = ws.cell(row=r, column=i, value=v)
                cell.alignment, cell.border = (center if i in (1, 3, 4, 5) else wrap), border
            ws.cell(row=r, column=2).font = Font(bold=True)
            r += 1
        for rule in [x for x in rules if x["component"] == comp["id"]]:
            ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=len(cols))
            ws.cell(row=r, column=1, value=f"Lưu ý: {rule['label']} → {', '.join(rule['cap']['criteria'])} tối đa hệ số {rule['cap']['max']:g}.").font = Font(italic=True, color="B42318")
            r += 1
    ws.freeze_panes = "C2"

    # ----- Danh sách
    first, last = 4, 3 + DATA_ROWS
    ws = wb.create_sheet("Danh sách")
    ws.cell(row=1, column=1, value="Nhập danh sách sinh viên tại đây; các sheet khác lấy theo cùng dòng.").font = Font(italic=True)
    header(ws, 3, ["STT", "MSSV", "Họ và tên", "Nhóm"])
    for i, w in enumerate([5, 12, 26, 8], start=1):
        ws.column_dimensions[col(i)].width = w
    for r in range(first, last + 1):
        ws.cell(row=r, column=1, value=r - first + 1).alignment = center
        for x in range(1, 5):
            ws.cell(row=r, column=x).border = border
    ws.freeze_panes = "B4"

    def info_cols(ws):
        for x, (title, w) in enumerate((("STT", 5), ("MSSV", 12), ("Họ và tên", 24), ("Nhóm", 7)), start=1):
            ws.merge_cells(start_row=1, start_column=x, end_row=3, end_column=x)
            cell = ws.cell(row=1, column=x, value=title)
            cell.fill, cell.font, cell.alignment, cell.border = head_fill, head_font, center, border
            ws.column_dimensions[col(x)].width = w
        for r in range(first, last + 1):
            ws.cell(row=r, column=1, value=r - first + 1).alignment = center
            for x, letter in ((2, "B"), (3, "C"), (4, "D")):
                ws.cell(row=r, column=x, value=f"=IF('Danh sách'!{letter}{r}=\"\",\"\",'Danh sách'!{letter}{r})")

    # ----- Sheet từng thành phần: nhập hệ số, tính điểm thành phần và phần điểm của từng CLO
    comp_ref = {}
    for k, comp in enumerate(comps):
        name = f"{comp['id']} {comp['name']}".replace("(", "").replace(")", "")[:31]
        ws = wb.create_sheet(name)
        info_cols(ws)
        fill = PatternFill("solid", fgColor=FILLS[k % 4])
        x = 5
        crit_col = {}
        for c in comp["criteria"]:
            crit_col[c["id"]] = x
            h = ws.cell(row=2, column=x, value=f"{c['label']}. {c['name']}" + (" (CN)" if c["scope"] == "individual" else ""))
            h.alignment, h.border, h.font, h.fill = center, border, Font(bold=True, size=9), fill
            m = ws.cell(row=3, column=x, value=f"×{c['weight']:g} · {clo_text(c)}")
            m.alignment, m.border, m.font = center, border, Font(italic=True, size=8)
            ws.column_dimensions[col(x)].width = 13
            x += 1
        a, b = crit_col[comp["criteria"][0]["id"]], crit_col[comp["criteria"][-1]["id"]]
        ws.merge_cells(start_row=1, start_column=a, end_row=1, end_column=b)
        cell = ws.cell(row=1, column=a, value=f"{comp['id']}. {comp['name']} - nhập hệ số 0–1 ({pct(comp['weight'])} điểm học phần)")
        cell.font, cell.alignment = Font(bold=True, color=DARK), center
        for xx in range(a, b + 1):
            ws.cell(row=1, column=xx).fill = fill
        comp_rules = [rl for rl in rules if rl["component"] == comp["id"]]
        flag_col = {}
        for rl in comp_rules:
            flag_col[rl["id"]] = x
            ws.merge_cells(start_row=1, start_column=x, end_row=2, end_column=x)
            h = ws.cell(row=1, column=x, value=rl["label"])
            h.alignment, h.border, h.font, h.fill = center, border, Font(bold=True, size=8, color="B42318"), red
            ws.cell(row=3, column=x, value="x = có").alignment = center
            ws.column_dimensions[col(x)].width = 16
            x += 1
        total_col = x
        comp_clos = [clo["id"] for clo in clos if any(clo["id"] in c.get("clo", {}) for c in comp["criteria"])]
        clo_col = {cid: total_col + 1 + i for i, cid in enumerate(comp_clos)}
        note_col = total_col + 1 + len(comp_clos)
        head_block(ws, total_col, f"Điểm {comp['id']} (/{course['scale']})", course["scale"], 11)
        for cid in comp_clos:
            head_block(ws, clo_col[cid], f"{cid} trong {comp['id']}", round(sum(c.get("clo", {}).get(cid, 0) for c in comp["criteria"]), 4), 11)
        head_block(ws, note_col, "Ghi chú", "", 30)
        ws.row_dimensions[2].height = 80

        n = len(comp["criteria"])
        for r in range(first, last + 1):
            def eff(c):
                ref = f"{col(crit_col[c['id']])}{r}"
                caps = [f'IF({col(flag_col[rl["id"]])}{r}="x",{rl["cap"]["max"]},1)' for rl in comp_rules if c["id"] in rl["cap"]["criteria"]]
                return f"MIN({ref},{','.join(caps)})" if caps else ref
            rng = f"{col(a)}{r}:{col(b)}{r}"
            terms = "+".join(f"{c['weight']}*{eff(c)}" for c in comp["criteria"])
            ws.cell(row=r, column=total_col, value=f'=IF(COUNT({rng})={n},ROUND({terms},2),"")').font = Font(bold=True)
            for cid in comp_clos:
                t = "+".join(f"{c['clo'][cid]}*{eff(c)}" for c in comp["criteria"] if cid in c.get("clo", {}))
                ws.cell(row=r, column=clo_col[cid], value=f'=IF(COUNT({rng})={n},ROUND({t},2),"")')
            for xx in range(1, note_col + 1):
                ws.cell(row=r, column=xx).border = border
            for xx in [total_col] + list(clo_col.values()):
                ws.cell(row=r, column=xx).alignment = center
        dv = DataValidation(type="decimal", operator="between", formula1="0", formula2="1", allow_blank=True,
                            showErrorMessage=True, errorTitle="Hệ số không hợp lệ", error="Nhập hệ số từ 0 đến 1 (ví dụ 0,8)")
        ws.add_data_validation(dv)
        dv.add(f"{col(a)}{first}:{col(b)}{last}")
        for rl in comp_rules:
            fv = DataValidation(type="list", formula1='"x"', allow_blank=True)
            ws.add_data_validation(fv)
            letter = col(flag_col[rl["id"]])
            fv.add(f"{letter}{first}:{letter}{last}")
        ws.freeze_panes = ws.cell(row=first, column=5)
        comp_ref[comp["id"]] = {"sheet": name, "total": col(total_col), "clo": {cid: col(v) for cid, v in clo_col.items()}}

    # ----- Tổng hợp
    ws = wb.create_sheet("Tổng hợp")
    info_cols(ws)
    comp_col = {comp["id"]: 5 + i for i, comp in enumerate(comps)}
    final_col = 5 + len(comps)
    cs_col = {clo["id"]: final_col + 1 + i for i, clo in enumerate(clos)}
    pass_col = {clo["id"]: final_col + 1 + len(clos) + i for i, clo in enumerate(clos)}
    for comp in comps:
        head_block(ws, comp_col[comp["id"]], f"{comp['id']} {comp['name']}", pct(comp["weight"]))
    head_block(ws, final_col, f"Điểm học phần (/{course['scale']})", course["scale"])
    for clo in clos:
        head_block(ws, cs_col[clo["id"]], f"Điểm {clo['id']}", f"/{cmax[clo['id']]:g}")
        head_block(ws, pass_col[clo["id"]], f"Đạt {clo['id']}", f"≥ {cmax[clo['id']] * course['studentThreshold']:g}")
    ws.row_dimensions[2].height = 45
    for r in range(first, last + 1):
        for comp in comps:
            ref = f"'{comp_ref[comp['id']]['sheet']}'!{comp_ref[comp['id']]['total']}{r}"
            ws.cell(row=r, column=comp_col[comp["id"]], value=f'=IF({ref}="","",{ref})')
        crng = f"{col(comp_col[comps[0]['id']])}{r}:{col(comp_col[comps[-1]['id']])}{r}"
        all_ok = f"COUNT({crng})={len(comps)}"
        terms = "+".join(f"{comp['weight']}*{col(comp_col[comp['id']])}{r}" for comp in comps)
        ws.cell(row=r, column=final_col, value=f'=IF({all_ok},ROUND({terms},2),"")').font = Font(bold=True)
        for clo in clos:
            t = "+".join(f"{comp['weight']}*'{comp_ref[comp['id']]['sheet']}'!{comp_ref[comp['id']]['clo'][clo['id']]}{r}"
                         for comp in comps if clo["id"] in comp_ref[comp["id"]]["clo"])
            ws.cell(row=r, column=cs_col[clo["id"]], value=f'=IF({all_ok},ROUND({t},2),"")')
            cref = f"{col(cs_col[clo['id']])}{r}"
            ws.cell(row=r, column=pass_col[clo["id"]], value=f'=IF({cref}="","",IF({cref}>={cmax[clo["id"]] * course["studentThreshold"]:g},"Đạt","Chưa đạt"))')
        for xx in range(1, max(pass_col.values()) + 1):
            ws.cell(row=r, column=xx).border = border
            if xx > 4:
                ws.cell(row=r, column=xx).alignment = center
    prng = f"{col(min(pass_col.values()))}{first}:{col(max(pass_col.values()))}{last}"
    ws.conditional_formatting.add(prng, CellIsRule(operator="equal", formula=['"Chưa đạt"'], fill=red, font=Font(color="B42318", bold=True)))
    ws.conditional_formatting.add(prng, CellIsRule(operator="equal", formula=['"Đạt"'], fill=green, font=Font(color="067647")))
    ws.freeze_panes = ws.cell(row=first, column=5)

    # ----- Mức đạt CLO
    ws2 = wb.create_sheet("Mức đạt CLO")
    for i, w in enumerate([10, 60, 12, 14, 14, 12, 12, 12, 18], start=1):
        ws2.column_dimensions[col(i)].width = w
    ws2.cell(row=1, column=1, value=f"MỨC ĐẠT CLO - {course['name']} ({course['code']})").font = Font(bold=True, size=13, color=BLUE)
    ws2.cell(row=2, column=1, value=course["note"]).font = Font(italic=True)
    header(ws2, 4, ["CLO", "Nội dung", "Điểm tối đa", "Ngưỡng SV đạt", "Số SV có điểm", "Số SV đạt", "Tỷ lệ đạt", "Điểm TB", "Kết luận cấp lớp"])
    for i, clo in enumerate(clos):
        r = 5 + i
        sc = f"'Tổng hợp'!{col(cs_col[clo['id']])}{first}:{col(cs_col[clo['id']])}{last}"
        pc = f"'Tổng hợp'!{col(pass_col[clo['id']])}{first}:{col(pass_col[clo['id']])}{last}"
        values = [clo["id"], clo["name"], cmax[clo["id"]], round(cmax[clo["id"]] * course["studentThreshold"], 4), f"=COUNT({sc})", f'=COUNTIF({pc},"Đạt")',
                  f'=IF(E{r}=0,"",F{r}/E{r})', f'=IF(E{r}=0,"",ROUND(AVERAGE({sc}),2))',
                  f'=IF(E{r}=0,"",IF(G{r}>={course["classThreshold"]},"Đạt","Chưa đạt"))']
        for xx, v in enumerate(values, start=1):
            cell = ws2.cell(row=r, column=xx, value=v)
            cell.border, cell.alignment = border, (wrap if xx == 2 else center)
        ws2.cell(row=r, column=7).number_format = "0.0%"
    concl = f"I5:I{4 + len(clos)}"
    ws2.conditional_formatting.add(concl, CellIsRule(operator="equal", formula=['"Chưa đạt"'], fill=red, font=Font(color="B42318", bold=True)))
    ws2.conditional_formatting.add(concl, CellIsRule(operator="equal", formula=['"Đạt"'], fill=green, font=Font(color="067647", bold=True)))

    wb.active = wb.sheetnames.index("Danh sách")
    wb.save(out)
    return sum(len(comp["criteria"]) for comp in comps)


def build_html_components(rubric: dict, out: Path):
    html = TEMPLATE_COMPONENTS.read_text(encoding="utf-8")
    data = json.dumps({**rubric, "cloMax": clo_max(rubric)}, ensure_ascii=False).replace("</", "<\\/")
    course = rubric["course"]
    html = (html.replace("__RUBRIC_JSON__", data)
                .replace("__COURSE_NAME__", course["name"])
                .replace("__COURSE_CODE__", course["code"]))
    out.write_text(html, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Sinh rubric Excel và công cụ chấm điểm HTML từ rubric.json")
    parser.add_argument("course", help="Thư mục học phần")
    args = parser.parse_args()
    course_dir = ROOT_DIR / args.course.strip("/\\")
    src = course_dir / "rubric" / "rubric.json"
    if not src.is_file():
        print(f"[LỖI] Không có {src.relative_to(ROOT_DIR)}")
        return 1
    rubric = json.loads(src.read_text(encoding="utf-8"))
    if "components" in rubric:
        return main_components(course_dir, rubric)
    errors = validate(rubric)
    if errors:
        for e in errors:
            print(f"[LỖI] {e}")
        return 1
    n = sum(len(clo["criteria"]) for clo in rubric["clos"])
    xlsx = course_dir / "rubric" / f"Rubric-{rubric['course']['code']}.xlsx"
    build_excel(rubric, xlsx)
    print(f"[+] Đã ghi {xlsx.relative_to(ROOT_DIR)} ({len(rubric['clos'])} CLO, {n} tiêu chí)")
    html = course_dir / "cham-diem.html"
    build_html(rubric, html)
    print(f"[+] Đã ghi {html.relative_to(ROOT_DIR)}")
    return 0



def main_components(course_dir: Path, rubric: dict) -> int:
    errors = validate_components(rubric)
    if errors:
        for e in errors:
            print(f"[LỖI] {e}")
        return 1
    xlsx = course_dir / "rubric" / f"Rubric-{rubric['course']['code']}.xlsx"
    n = build_excel_components(rubric, xlsx)
    print(f"[+] Đã ghi {xlsx.relative_to(ROOT_DIR)} ({len(rubric['components'])} thành phần, {n} tiêu chí)")
    html = course_dir / "cham-diem.html"
    build_html_components(rubric, html)
    print(f"[+] Đã ghi {html.relative_to(ROOT_DIR)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
