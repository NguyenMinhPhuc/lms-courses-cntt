"""
Sinh hình minh họa cho slide (Slides/images/) của một học phần:
  - Sơ đồ vẽ từ mô tả trong Slides/images/diagrams.json (matplotlib, PNG nền trắng).
  - Ảnh có giấy phép mở tải từ Wikimedia Commons theo Slides/images/photos.json,
    tác giả và giấy phép được ghi vào Slides/images/NGUON.md.

Cách dùng:
    uv run --with matplotlib python build-images.py co-so-van-hoa-viet-nam            # mọi hình
    uv run --with matplotlib python build-images.py co-so-van-hoa-viet-nam bai-01     # chỉ hình có tên bắt đầu bằng bai-01

Định dạng hai file JSON: xem .claude/skills/lms-lecture-builder/references/slides.md
"""
import re
import sys
import json
import html
import math
import time
import textwrap
import argparse
import urllib.parse
import urllib.request
from pathlib import Path

if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROOT_DIR = Path(__file__).resolve().parent
USER_AGENT = "LHU-LMS-course-builder/1.0 (Khoa CNTT - Dai hoc Lac Hong; slide images)"

BLUE, NAVY, GOLD = "#0033CC", "#1F4E9C", "#F2A900"
BLUE_LIGHT, GOLD_LIGHT, GREY_LIGHT = "#E8EEFB", "#FFF4D6", "#F1F3F5"
TEXT, MUTED = "#212529", "#6C757D"
FILLS = [(BLUE, BLUE_LIGHT), (GOLD, GOLD_LIGHT), (NAVY, "#E3EAF5"), ("#2E8B57", "#E6F4EC"), ("#C0392B", "#FBEAE8")]
FONT_SIZE = 21


# ---------------------------------------------------------------- vẽ cơ bản
def wrap(text: str, width_in: float, size: float) -> str:
    chars = max(6, int(width_in * 72 / (size * 0.56)))
    return "\n".join(textwrap.fill(part, chars, break_long_words=False) for part in str(text).split("\n"))


def box(ax, x, y, w, h, text="", sub="", edge=BLUE, fill=BLUE_LIGHT, size=FONT_SIZE, bold=True, color=TEXT, round_=True):
    from matplotlib.patches import FancyBboxPatch
    style = "round,pad=0,rounding_size=0.12" if round_ else "square,pad=0"
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle=style, fc=fill, ec=edge, lw=2.2))
    if text and sub:
        ax.text(x, y + h * 0.17, wrap(text, w - 0.2, size), ha="center", va="center", fontsize=size,
                fontweight="bold" if bold else "normal", color=color, linespacing=1.15)
        ax.text(x, y - h * 0.22, wrap(sub, w - 0.2, size * 0.78), ha="center", va="center",
                fontsize=size * 0.78, color=MUTED, linespacing=1.15)
    elif text:
        ax.text(x, y, wrap(text, w - 0.2, size), ha="center", va="center", fontsize=size,
                fontweight="bold" if bold else "normal", color=color, linespacing=1.15)


def arrow(ax, x1, y1, x2, y2, color=NAVY, both=False, dashed=False, rad=0.0, lw=2.4):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="<|-|>" if both else "-|>", color=color, lw=lw, shrinkA=2, shrinkB=2,
                                mutation_scale=20, linestyle="--" if dashed else "-",
                                connectionstyle=f"arc3,rad={rad}"))


def split(item):
    """Một mục có thể là "chữ" hoặc ["tiêu đề", "chú thích"]."""
    if isinstance(item, (list, tuple)):
        return str(item[0]), str(item[1]) if len(item) > 1 else ""
    return str(item), ""


def title(ax, spec, W, H):
    if spec.get("title"):
        ax.text(W / 2, H - 0.35, spec["title"], ha="center", va="center", fontsize=FONT_SIZE * 1.15,
                fontweight="bold", color=BLUE)
        return H - 0.75
    return H - 0.15


# ---------------------------------------------------------------- các kiểu sơ đồ
def draw_flow(ax, spec, W, H):
    steps = spec["steps"]
    top = title(ax, spec, W, H)
    n = len(steps)
    horizontal = spec.get("direction", "h" if n <= 4 else "v") == "h"
    branch = spec.get("branch")  # {"from": [chỉ số bước], "to": "tên", "label": "..."}: nhánh rẽ phía dưới (chỉ khi ngang)
    xs = []
    for i, item in enumerate(steps):
        t, s = split(item)
        edge, fill = FILLS[i % 2] if spec.get("alternate", True) else FILLS[0]
        if horizontal:
            gap = 0.45
            w = (W - 0.4 - gap * (n - 1)) / n
            h = min(top - 0.4, 1.7) if not branch else 1.1
            x, y = 0.2 + w / 2 + i * (w + gap), (top + 0.15) / 2 if not branch else top - 0.75
            xs.append(x)
            box(ax, x, y, w, h, t, s, edge, fill)
            if i < n - 1:
                arrow(ax, x + w / 2, y, x + w / 2 + gap, y)
    if horizontal and branch:
        bx = sum(xs[j] for j in branch["from"]) / len(branch["from"])
        by = top - 0.75 - 2.4
        box(ax, bx, by, max(w, 4.6), 1.25, branch["to"], branch.get("label", ""), "#C0392B", "#FBEAE8")
        for j in branch["from"]:
            arrow(ax, xs[j], top - 0.75 - 0.55, bx, by + 0.5, color="#C0392B", dashed=True)
    for i, item in enumerate(steps):
        t, s = split(item)
        edge, fill = FILLS[i % 2] if spec.get("alternate", True) else FILLS[0]
        if horizontal:
            continue
        else:
            gap = 0.28
            h = min(1.2, (top - 0.2 - gap * (n - 1)) / n)
            w = min(W - 0.6, 6.5)
            y = top - h / 2 - i * (h + gap)
            box(ax, W / 2, y, w, h, t, s, edge, fill)
            if i < n - 1:
                arrow(ax, W / 2, y - h / 2, W / 2, y - h / 2 - gap)


def draw_cycle(ax, spec, W, H):
    steps = spec["steps"]
    top = title(ax, spec, W, H)
    n = len(steps)
    cx, cy = W / 2, top / 2
    rx, ry = W / 2 - 1.3, top / 2 - 0.6
    bw, bh = min(2.4, 2 * math.pi * rx / n * 0.75), 0.95
    pts = [(cx + rx * math.sin(2 * math.pi * i / n), cy + ry * math.cos(2 * math.pi * i / n)) for i in range(n)]
    delta = math.pi / n * 0.5  # mũi tên chạy trên đường elip, giữa hai hộp
    for i in range(n):
        a1, a2 = 2 * math.pi * i / n + delta, 2 * math.pi * (i + 1) / n - delta
        p1 = (cx + rx * math.sin(a1), cy + ry * math.cos(a1))
        p2 = (cx + rx * math.sin(a2), cy + ry * math.cos(a2))
        arrow(ax, *p1, *p2, rad=-0.2, color=GOLD, lw=3)
    for i, item in enumerate(steps):
        t, s = split(item)
        box(ax, *pts[i], bw, bh, t, s, *FILLS[i % 2])
    if spec.get("center"):
        ax.text(cx, cy, wrap(spec["center"], rx, FONT_SIZE * 1.05), ha="center", va="center",
                fontsize=FONT_SIZE * 1.05, fontweight="bold", color=NAVY)


def draw_hub(ax, spec, W, H):
    nodes = spec["nodes"]
    top = title(ax, spec, W, H)
    n = len(nodes)
    cx, cy = W / 2, top / 2
    rx, ry = W / 2 - 1.35, top / 2 - 0.65
    pts = [(cx + rx * math.sin(2 * math.pi * i / n + (math.pi / n if n % 2 == 0 and n != 4 else 0)),
            cy + ry * math.cos(2 * math.pi * i / n + (math.pi / n if n % 2 == 0 and n != 4 else 0))) for i in range(n)]
    for p in pts:
        ax.plot([cx, p[0]], [cy, p[1]], color=NAVY, lw=2, zorder=0)
    box(ax, cx, cy, 2.4, 1.1, spec["center"], "", NAVY, BLUE, size=FONT_SIZE * 1.05, color="white")
    for i, item in enumerate(nodes):
        t, s = split(item)
        box(ax, *pts[i], 2.5, 1.3 if not s else 1.5, t, s, *FILLS[i % 2])


def draw_layers(ax, spec, W, H):
    layers = spec["layers"]
    top = title(ax, spec, W, H)
    n = len(layers)
    gap = 0.35
    h = min(1.3, (top - 0.2 - gap * (n - 1)) / n)
    for i, layer in enumerate(layers):
        name = layer["name"] if isinstance(layer, dict) else split(layer)[0]
        items = layer.get("items", []) if isinstance(layer, dict) else []
        note = layer.get("note", "") if isinstance(layer, dict) else split(layer)[1]
        y = top - h / 2 - i * (h + gap)
        edge, fill = FILLS[i % len(FILLS)]
        box(ax, W / 2, y, W - 0.5, h, "", "", edge, fill)
        if items:
            box(ax, 0.25 + 1.2, y, 2.2, h - 0.25, name, "", edge, edge, size=FONT_SIZE * 0.95, color="white")
            cw = (W - 3.1 - 0.15 * (len(items) - 1)) / len(items)
            for j, it in enumerate(items):
                box(ax, 2.75 + cw / 2 + j * (cw + 0.15), y, cw, h - 0.4, it, "", edge, "white",
                    size=FONT_SIZE * 0.82, bold=False)
        else:
            ax.text(W / 2, y + (0.15 if note else 0), name, ha="center", va="center", fontsize=FONT_SIZE,
                    fontweight="bold", color=TEXT)
            if note:
                ax.text(W / 2, y - 0.25, wrap(note, W - 1, FONT_SIZE * 0.78), ha="center", va="center",
                        fontsize=FONT_SIZE * 0.78, color=MUTED)
        if i < n - 1 and spec.get("arrows", "down") != "none":
            arrow(ax, W / 2, y - h / 2, W / 2, y - h / 2 - gap, both=spec.get("arrows") == "both")


def draw_columns(ax, spec, W, H):
    cols = spec["columns"]
    top = title(ax, spec, W, H)
    n = len(cols)
    gap = 0.3
    w = (W - 0.4 - gap * (n - 1)) / n
    head_h = 0.8
    for i, col in enumerate(cols):
        x = 0.2 + w / 2 + i * (w + gap)
        edge, fill = FILLS[i % len(FILLS)]
        box(ax, x, top - head_h / 2, w, head_h, col["title"], "", edge, edge, color="white")
        body_top = top - head_h - 0.12
        size = FONT_SIZE * (0.95 if n <= 2 else 0.82)
        text = "\n".join(wrap("• " + str(it), w - 0.35, size) for it in col.get("items", []))
        body_h = min(body_top - 0.2, max(1.5, (text.count("\n") + 1) * size * 1.5 / 72 + 0.4))
        box(ax, x, body_top - body_h / 2, w, body_h, "", "", edge, fill)
        ax.text(x - w / 2 + 0.18, body_top - 0.2, text, ha="left", va="top", fontsize=size,
                color=TEXT, linespacing=1.45)


def draw_pairs(ax, spec, W, H):
    rows = spec["items"]
    top = title(ax, spec, W, H)
    if spec.get("headers"):
        for x, head in zip((W * 0.25, W * 0.75), spec["headers"]):
            ax.text(x, top - 0.25, head, ha="center", va="center", fontsize=FONT_SIZE, fontweight="bold", color=NAVY)
        top -= 0.6
    n = len(rows)
    gap = 0.22
    h = min(1.1, (top - 0.15 - gap * (n - 1)) / n)
    w = W * 0.4
    for i, (left, right) in enumerate(rows):
        y = top - h / 2 - i * (h + gap)
        box(ax, W * 0.25, y, w, h, left, "", BLUE, BLUE_LIGHT)
        box(ax, W * 0.75, y, w, h, right, "", GOLD, GOLD_LIGHT, bold=False)
        arrow(ax, W * 0.25 + w / 2, y, W * 0.75 - w / 2, y, both=spec.get("both", False))


def draw_timeline(ax, spec, W, H):
    events = spec["events"]
    top = title(ax, spec, W, H)
    n = len(events)
    y0 = top / 2
    ax.plot([0.3, W - 0.3], [y0, y0], color=NAVY, lw=4, zorder=0)
    step = (W - 0.6) / n
    for i, ev in enumerate(events):
        t, s = split(ev)
        x = 0.3 + step / 2 + i * step
        bw = min(step * 1.8, 2.6)
        ax.plot(x, y0, "o", ms=16, color=GOLD, mec=NAVY, mew=2.5)
        up = i % 2 == 0
        y = y0 + (1.05 if up else -1.05)
        ax.plot([x, x], [y0, y - (0.45 if up else -0.45)], color=MUTED, lw=1.2, zorder=0)
        box(ax, min(max(x, bw / 2 + 0.05), W - bw / 2 - 0.05), y, bw, 1.0 if s else 0.7, t, s, *FILLS[i % 2])


def draw_tree(ax, spec, W, H):
    top = title(ax, spec, W, H)
    kids = spec["children"]
    n = len(kids)
    box(ax, W / 2, top - 0.45, min(W - 1, 4.5), 0.8, spec["root"], "", NAVY, BLUE, color="white")
    gap = 0.25
    w = (W - 0.3 - gap * (n - 1)) / n
    yk = top - 1.9
    for i, kid in enumerate(kids):
        name = kid["name"] if isinstance(kid, dict) else str(kid)
        sub = kid.get("children", []) if isinstance(kid, dict) else []
        x = 0.15 + w / 2 + i * (w + gap)
        ax.plot([W / 2, W / 2, x, x], [top - 0.85, top - 1.2, top - 1.2, yk + 0.4], color=NAVY, lw=2, zorder=0)
        edge, fill = FILLS[i % len(FILLS)]
        box(ax, x, yk, w, 0.8, name, "", edge, fill, size=FONT_SIZE * 0.92)
        if sub:
            sh = min(0.75, (yk - 0.6 - 0.15 * len(sub)) / len(sub))
            for j, s in enumerate(sub):
                ys = yk - 0.6 - sh / 2 - j * (sh + 0.15)
                ax.plot([x, x], [yk - 0.4, ys], color=edge, lw=1.5, zorder=0)
                box(ax, x, ys, w - 0.2, sh, s, "", edge, "white", size=FONT_SIZE * 0.78, bold=False)


def draw_sequence(ax, spec, W, H):
    actors = spec["actors"]
    msgs = spec["messages"]
    top = title(ax, spec, W, H)
    n = len(actors)
    step = (W - 0.4) / n
    xs = {a: 0.2 + step / 2 + i * step for i, a in enumerate(actors)}
    for i, a in enumerate(actors):
        box(ax, xs[a], top - 0.4, min(step - 0.3, 2.8), 0.75, a, "", *FILLS[i % len(FILLS)])
        ax.plot([xs[a], xs[a]], [top - 0.8, 0.2], color=MUTED, lw=1.5, ls="--", zorder=0)
    dy = min(0.85, (top - 1.6) / max(len(msgs), 1))
    for i, m in enumerate(msgs):
        src, dst, label = m[0], m[1], m[2]
        dashed = len(m) > 3 and m[3] == "return"
        y = top - 1.6 - i * dy
        if src == dst:
            arrow(ax, xs[src], y + 0.12, xs[src], y - 0.2, rad=-1.2, color=NAVY)
            ax.text(xs[src] + 0.3, y, wrap(label, step * 1.4, FONT_SIZE * 0.78), ha="left", va="center",
                    fontsize=FONT_SIZE * 0.78, color=TEXT)
            continue
        arrow(ax, xs[src], y, xs[dst], y, dashed=dashed, color=GOLD if dashed else NAVY)
        ax.text((xs[src] + xs[dst]) / 2, y + 0.06, wrap(label, abs(xs[dst] - xs[src]) - 0.2, FONT_SIZE * 0.78),
                ha="center", va="bottom", fontsize=FONT_SIZE * 0.78, color=TEXT)


def draw_flowchart(ax, spec, W, H):
    """Lưu đồ thuật toán: nodes [{id, shape, text, pos: [cột, hàng]}], edges [[từ, đến, nhãn?, "left"|"right"?]].
    shape: terminal (bắt đầu/kết thúc), io (nhập/xuất), process (xử lý), decision (điều kiện)."""
    from matplotlib.patches import FancyBboxPatch, Polygon
    top = title(ax, spec, W, H)
    nodes = {n["id"]: n for n in spec["nodes"]}
    cols = max(n["pos"][0] for n in nodes.values()) + 1
    rows = max(n["pos"][1] for n in nodes.values()) + 1
    cw, rh = W / cols, (top - 0.1) / rows
    w = min(cw * 0.82, spec.get("node_width", 3.6))
    h = min(rh * 0.62, 0.95)
    size = FONT_SIZE * spec.get("font_scale", 0.78)
    geo = {}
    colors = {"terminal": ("#2E8B57", "#E6F4EC"), "io": (GOLD, GOLD_LIGHT), "process": (BLUE, BLUE_LIGHT),
              "decision": ("#C0392B", "#FBEAE8")}
    for nid, n in nodes.items():
        c, r = n["pos"]
        x, y = (c + 0.5) * cw, top - (r + 0.5) * rh
        shape = n.get("shape", "process")
        edge, fill = colors.get(shape, colors["process"])
        hw, hh = w / 2, h / 2
        if shape == "decision":
            hh = h * 0.68
            ax.add_patch(Polygon([(x, y + hh), (x + hw, y), (x, y - hh), (x - hw, y)], closed=True, fc=fill, ec=edge, lw=2.2))
        elif shape == "io":
            k = 0.22
            ax.add_patch(Polygon([(x - hw + k, y + hh), (x + hw, y + hh), (x + hw - k, y - hh), (x - hw, y - hh)],
                                 closed=True, fc=fill, ec=edge, lw=2.2))
        else:
            style = f"round,pad=0,rounding_size={hh if shape == 'terminal' else 0.04}"
            ax.add_patch(FancyBboxPatch((x - hw, y - hh), w, 2 * hh, boxstyle=style, fc=fill, ec=edge, lw=2.2))
        ax.text(x, y, wrap(n.get("text", ""), w * (0.72 if shape == "decision" else 0.92), size), ha="center", va="center",
                fontsize=size, color=TEXT, fontweight="bold" if shape in ("terminal", "decision") else "normal",
                linespacing=1.12, family="monospace" if n.get("code") else None)
        geo[nid] = (x, y, hw, hh)

    def label_at(px, py, text):
        if text:
            ax.text(px, py, text, ha="center", va="center", fontsize=size * 0.95, color="#C0392B", fontweight="bold",
                    bbox=dict(boxstyle="round,pad=0.12", fc="white", ec="none"))

    for e in spec.get("edges", []):
        a, b = e[0], e[1]
        lab = e[2] if len(e) > 2 else ""
        side = e[3] if len(e) > 3 else None
        ax_, ay, aw, ah = geo[a]
        bx, by, bw, bh = geo[b]
        if abs(ax_ - bx) < 1e-6 and by < ay:                       # cùng cột, đi xuống
            pts = [(ax_, ay - ah), (bx, by + bh)]
        elif abs(ay - by) < 1e-6:                                   # cùng hàng
            sgn = 1 if bx > ax_ else -1
            pts = [(ax_ + sgn * aw, ay), (bx - sgn * bw, by)]
        elif by < ay and side == "down":                            # xuống trước, gom vào đường chung phía trên đích
            ym = by + bh + min(0.35, (ay - ah - by - bh) / 2)
            pts = [(ax_, ay - ah), (ax_, ym), (bx, ym), (bx, by + bh)]
        elif by < ay:                                               # xuống, lệch cột: ra cạnh bên rồi xuống
            sgn = 1 if bx > ax_ else -1
            pts = [(ax_ + sgn * aw, ay), (bx, ay), (bx, by + bh)]
        else:                                                       # quay lại phía trên (vòng lặp)
            sgn = 1 if side == "right" else -1
            off = max(aw, bw) + 0.35
            xo = (max(ax_, bx) + off) if sgn > 0 else (min(ax_, bx) - off)
            pts = [(ax_ + sgn * aw, ay), (xo, ay), (xo, by), (bx + sgn * bw, by)]
        for (x1, y1), (x2, y2) in zip(pts[:-2], pts[1:-1]):
            ax.plot([x1, x2], [y1, y2], color=NAVY, lw=2.2, solid_capstyle="round")
        arrow(ax, *pts[-2], *pts[-1], lw=2.2)
        (x1, y1), (x2, y2) = pts[0], pts[1]
        label_at((x1 + x2) / 2 + (0.22 if abs(x1 - x2) < 1e-6 else 0), (y1 + y2) / 2 + (0.0 if abs(x1 - x2) < 1e-6 else 0.2), lab)


DRAWERS = {"flow": draw_flow, "cycle": draw_cycle, "hub": draw_hub, "layers": draw_layers, "columns": draw_columns,
           "pairs": draw_pairs, "timeline": draw_timeline, "tree": draw_tree, "sequence": draw_sequence,
           "flowchart": draw_flowchart}


def default_size(spec: dict) -> list:
    """Quy trình ngang và bảng nhiều cột cần khung rộng để chữ không bị ngắt."""
    n = len(spec.get("steps", spec.get("columns", [])))
    if spec["type"] == "flow" and spec.get("direction", "h" if n <= 4 else "v") == "h":
        return [max(8, 2.7 * n), 3.8 if not spec.get("branch") else 5.2]
    if spec["type"] == "columns" and n >= 3:
        return [10, 5.5]
    if spec["type"] == "flowchart":
        cols = max(x["pos"][0] for x in spec["nodes"]) + 1
        rows = max(x["pos"][1] for x in spec["nodes"]) + 1
        return [max(5.5, 3.9 * cols + 0.8), max(3, 1.75 * rows + (0.6 if spec.get("title") else 0))]
    return [8, 6]


def render_diagram(name: str, spec: dict, out: Path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams["font.family"] = ["Arial", "DejaVu Sans"]
    if spec.get("type") not in DRAWERS:
        raise ValueError(f"{name}: kiểu sơ đồ '{spec.get('type')}' không hỗ trợ ({', '.join(DRAWERS)})")
    W, H = spec.get("size") or default_size(spec)
    fig = plt.figure(figsize=(W, H), dpi=200)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.axis("off")
    DRAWERS[spec["type"]](ax, spec, W, H)
    fig.savefig(out, dpi=200, facecolor="white", bbox_inches="tight", pad_inches=0.15)  # cắt khoảng trắng thừa
    plt.close(fig)


# ---------------------------------------------------------------- Wikimedia Commons
def commons_info(file_title: str, width: int) -> dict:
    query = urllib.parse.urlencode({
        "action": "query", "format": "json", "prop": "imageinfo", "titles": file_title,
        "iiprop": "url|extmetadata", "iiurlwidth": width})
    req = urllib.request.Request(f"https://commons.wikimedia.org/w/api.php?{query}", headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        pages = json.load(resp)["query"]["pages"]
    page = next(iter(pages.values()))
    if "imageinfo" not in page:
        raise ValueError(f"không tìm thấy {file_title} trên Wikimedia Commons")
    info = page["imageinfo"][0]
    meta = info.get("extmetadata", {})
    clean = lambda k: re.sub(r"<[^>]+>", "", html.unescape(meta.get(k, {}).get("value", ""))).strip()
    return {"url": info.get("thumburl") or info["url"], "page": info["descriptionurl"],
            "artist": clean("Artist") or "không rõ", "license": clean("LicenseShortName") or "xem trang nguồn"}


def fetch_photo(name: str, spec, out: Path) -> str:
    """Tải ảnh (bản thu nhỏ rộng tối đa 1600px). Trả về một dòng ghi nguồn cho NGUON.md."""
    spec = {"file": spec} if isinstance(spec, str) else spec
    info = commons_info(spec["file"], spec.get("width", 1600))
    if not out.is_file():
        req = urllib.request.Request(info["url"], headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = resp.read()
        from io import BytesIO
        from PIL import Image as PILImage  # có sẵn cùng matplotlib
        img = PILImage.open(BytesIO(data))
        if out.suffix.lower() in (".jpg", ".jpeg"):  # nén lại cho nhẹ slide (kể cả khi nguồn là PNG)
            img.convert("RGB").save(out, "JPEG", quality=85, optimize=True)
        else:
            out.write_bytes(data)
    return f"| `{name}` | {info['artist']} | {info['license']} | [{spec['file']}]({info['page']}) |"


# ---------------------------------------------------------------- main
def main():
    parser = argparse.ArgumentParser(description="Sinh hình minh họa cho Slides/images/")
    parser.add_argument("course", help="Thư mục học phần")
    parser.add_argument("prefix", nargs="?", default="", help="Chỉ xử lý hình có tên bắt đầu bằng chuỗi này")
    args = parser.parse_args()

    images_dir = ROOT_DIR / args.course.strip("/\\") / "Slides" / "images"
    diagrams_file, photos_file = images_dir / "diagrams.json", images_dir / "photos.json"
    if not diagrams_file.is_file() and not photos_file.is_file():
        print(f"[LỖI] Chưa có {diagrams_file.relative_to(ROOT_DIR)} hoặc photos.json")
        return 1

    exit_code = 0
    if diagrams_file.is_file():
        for name, spec in json.loads(diagrams_file.read_text(encoding="utf-8")).items():
            if not name.startswith(args.prefix):
                continue
            try:
                render_diagram(name, spec, images_dir / name)
                print(f"[+] sơ đồ {name}")
            except Exception as e:  # một sơ đồ lỗi không chặn các sơ đồ khác
                print(f"[LỖI] {name}: {e}")
                exit_code = 1

    if photos_file.is_file():
        credits = []
        for name, spec in json.loads(photos_file.read_text(encoding="utf-8")).items():
            if not name.startswith(args.prefix):
                continue
            try:
                time.sleep(2)  # Wikimedia giới hạn tốc độ gọi API (HTTP 429)
                credits.append(fetch_photo(name, spec, images_dir / name))
                print(f"[+] ảnh {name}")
            except Exception as e:
                print(f"[LỖI] {name}: {e}")
                exit_code = 1
        if credits and not args.prefix:
            (images_dir / "NGUON.md").write_text(
                "# Nguồn ảnh minh họa\n\nẢnh tải từ Wikimedia Commons, dùng theo giấy phép ghi bên dưới. "
                "Khi trích dẫn trên slide, ghi tác giả và giấy phép.\n\n"
                "| File | Tác giả | Giấy phép | Trang gốc |\n|---|---|---|---|\n" + "\n".join(credits) + "\n",
                encoding="utf-8")
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
