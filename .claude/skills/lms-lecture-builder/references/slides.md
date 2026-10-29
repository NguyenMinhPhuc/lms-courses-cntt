# Slide bài giảng (ghi chú Markdown → PowerPoint)

Mỗi bài có 2 file trong `<hoc-phan>/Slides/`:
- `bai-XX.markdown`: ghi chú slide (cách C). **Đây là file nguồn**, chỉ sửa file này.
- `bai-XX.pptx`: slide PowerPoint (cách A). Sinh tự động bằng `build-slides.py`, không sửa tay.

Viết slide **từ `bai-XX.md` đã được giảng viên duyệt**, không viết thẳng từ outline. Như vậy slide, trang Moodle và quiz dùng chung một nội dung.

## Định dạng `bai-XX.markdown`

```markdown
# Bài 01: Tên bài giảng
Mục tiêu một câu hoặc phụ đề (không bắt buộc, hiện trên slide tiêu đề)

---

## Slide 1: Tiêu đề slide
**Nội dung chính**:
- Ý cấp 1
  - Ý cấp 2 (thụt 2 khoảng trắng)
**Ví dụ**:
- Ví dụ cụ thể, gần gũi với sinh viên
**Hoạt động**: Câu hỏi hoặc nhiệm vụ ngắn cho lớp
**Ghi chú giảng viên**:
- Gợi ý cách giảng, câu hỏi gợi mở, thời lượng dự kiến

---

## Slide 2: Ví dụ có code
**Nội dung chính**:
- Hàm `tinh_tong(a, b)` trả về tổng hai số.
```python
def tinh_tong(a, b):
    return a + b
```
```

Quy tắc mà script dựa vào:
- `# ` (dòng đầu tiên): tiêu đề bài, tạo slide bìa. Dòng chữ ngay sau là phụ đề.
- `## `: mỗi slide. Tiền tố `Slide N:` được tự bỏ khi hiển thị.
- `**Nhãn**:` là dòng nhãn in đậm; `- ` là gạch đầu dòng (thụt 2 khoảng trắng cho mỗi cấp).
- Khối ```` ``` ```` là code, hiển thị font Consolas trên nền xám.
- `**Ghi chú giảng viên**:` và mọi dòng sau nó (tới slide kế tiếp) được đưa vào **Speaker Notes**, không hiện trên slide.
- `---` chỉ dùng để phân tách cho dễ đọc, không bắt buộc.

## Yêu cầu nội dung
- **Số slide:** khoảng 10–20 slide cho mỗi buổi 5 tiết; tính theo nội dung, không độn cho đủ số.
- **Cấu trúc gợi ý:** mục tiêu buổi học → câu hỏi dẫn nhập → các slide nội dung (mỗi slide một ý) → ví dụ/demo → hoạt động → tóm tắt → câu hỏi ôn tập.
- **Mật độ chữ:** tối đa khoảng 6–8 dòng mỗi slide, mỗi dòng một ý ngắn. Phần giải thích dài đưa vào `**Ghi chú giảng viên**`.
- **Code mẫu:** tối đa khoảng 12 dòng mỗi slide; code dài thì tách thành nhiều slide.
- **Văn phong:** theo [writing-style.md](writing-style.md).
- **Không bịa link** trong slide; link chưa có thì để `{{LINK_...}}`.

## Build và kiểm tra
```bash
uv run --with python-pptx python build-slides.py <hoc-phan>        # mọi bài
uv run --with python-pptx python build-slides.py <hoc-phan> 03     # chỉ bài 03
```
Sau khi build, mở một vài file `.pptx` để xem chữ có tràn khung không. Slide nào quá dài thì tách ra ở file `.markdown` rồi build lại.
