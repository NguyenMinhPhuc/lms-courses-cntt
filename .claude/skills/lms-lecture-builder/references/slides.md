# Slide bài giảng (ghi chú Markdown → PowerPoint)

Mỗi bài có 2 file trong `<hoc-phan>/Slides/`:
- `bai-XX.markdown`: ghi chú slide (cách C). **Đây là file nguồn**, chỉ sửa file này.
- `bai-XX.pptx`: slide PowerPoint (cách A). Sinh tự động bằng `build-slides.py`, không sửa tay.
- `images/`: hình minh họa dùng trong slide (xem mục **Hình ảnh minh họa** bên dưới).

Slide được dựng trên mẫu **`templates/Template-slide.pptx`** (logo LHU và Khoa, đường cong vàng – xanh, slide cảm ơn). Không tự vẽ khung/màu riêng; muốn đổi giao diện thì sửa file mẫu. Một học phần có thể dùng mẫu khác bằng `"slideTemplate": "đường/dẫn.pptx"` trong `course.json`. Các layout script dùng:

| Markdown | Slide sinh ra (layout của mẫu) |
|---|---|
| `# Bài XX: ...` (dòng đầu) | Bìa `TITLE`: tên bài, dải vàng ghi tên + mã học phần, phụ đề in nghiêng |
| `# Tên phần` (các dòng `# ` sau) | Slide mở phần `TITLE`; tên phần thành tiêu đề lớn trên các slide nội dung tiếp theo |
| `## Slide N: ...` | Slide nội dung `OBJECT`: tiêu đề lớn = tên phần (hoặc tên bài), tiêu đề phụ có mũi tên = tiêu đề slide, gạch đầu dòng ❖ |
| (tự động) | Slide cảm ơn cuối bộ: `instructor`, `instructorEmail`, `website`, học kỳ – năm, tên học phần lấy từ `course.json` |

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

# Phần 1: Tên phần lớn của bài

---

## Slide 2: Slide có hình minh họa
**Nội dung chính**:
- Ý chính ngắn gọn (chữ nằm cột trái, hình tự xếp cột phải)
![Trống đồng Ngọc Lũ – nguồn: Wikimedia Commons (CC BY-SA 4.0)](images/bai-01-trong-dong.jpg)

---

## Slide 3: Ví dụ có code
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
- `# ` các dòng sau: slide mở phần (không bắt buộc, dùng cho bài có 2–4 phần lớn).
- `**Nhãn**:` là dòng nhãn in đậm màu xanh; `- ` là gạch đầu dòng (thụt 2 khoảng trắng cho mỗi cấp). Nhãn `**Nội dung chính**:` không có chữ phía sau thì được ẩn trên slide.
- `![Chú thích](images/ten-hinh.jpg)` trên một dòng riêng: chèn hình, chú thích in nghiêng dưới hình. Slide có chữ thì hình nằm cột phải (tối đa 3 hình, xếp dọc); slide chỉ có hình thì hình chiếm cả vùng nội dung (xếp ngang). Đường dẫn tính từ thư mục `Slides/`. Hình chưa có thì script vẽ **khung chờ** nét đứt kèm chú thích và báo `[CẢNH BÁO]`.
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

## Hình ảnh minh họa (bắt buộc cân nhắc khi thiết kế slide)

Slide toàn chữ khó theo dõi. Khi viết `bai-XX.markdown`, chủ động thêm hình để bài giảng sinh động:

- **Mật độ:** khoảng 1 hình cho mỗi 2–3 slide nội dung; ưu tiên slide giới thiệu khái niệm mới, slide so sánh, slide quy trình, slide ví dụ thực tế và slide dẫn nhập. Slide mục tiêu, tóm tắt, câu hỏi ôn tập thường không cần hình.
- **Hình phải có ích:** minh họa đúng nội dung của slide (hiện vật, sơ đồ, ảnh chụp màn hình, biểu đồ), không dùng ảnh trang trí chung chung. Chú thích nói rõ hình là gì.
- **Nguồn hình, theo thứ tự ưu tiên:**
  1. **Sơ đồ** cho kiến thức có cấu trúc (quy trình, kiến trúc, phân loại, dòng thời gian, so sánh, luồng request): mô tả trong `Slides/images/diagrams.json` rồi sinh PNG bằng `build-images.py` (xem mục dưới). Không tự viết script vẽ riêng nếu một kiểu có sẵn đáp ứng được.
  2. **Ảnh chụp màn hình** công cụ, giao diện, kết quả chạy code (với học phần lập trình).
  3. **Ảnh có giấy phép mở** từ Wikimedia Commons: khai báo trong `Slides/images/photos.json`, `build-images.py` tự tải bản 1600px, nén JPG và ghi tác giả – giấy phép vào `Slides/images/NGUON.md`. Mở ảnh đã tải ra xem để chắc đúng nội dung. Chú thích ảnh ghi ngắn: `Tên hiện vật · Ảnh: Tác giả (giấy phép)`. Không dùng ảnh có bản quyền không rõ ràng, ảnh có watermark, không link nóng.
  4. Không tìm được hình phù hợp thì vẫn viết dòng `![Mô tả cụ thể hình cần có](images/bai-XX-ten.jpg)` để script vẽ khung chờ; liệt kê các hình còn thiếu ở cuối câu trả lời cho giảng viên bổ sung.
- **Không bịa:** không tạo ảnh "giả tư liệu" (ảnh AI giả làm hiện vật, di tích, nhân vật lịch sử, số liệu thật). Ảnh AI chỉ dùng cho hình minh họa ý tưởng và phải ghi rõ "Ảnh minh họa tạo bằng AI".
- **Kỹ thuật:** định dạng PNG hoặc JPG (script không đọc SVG/WebP, cần chuyển đổi trước); chiều ngang 1200–2000px, dung lượng mỗi hình nên dưới 500 KB; tên file `bai-XX-ten-ngan.jpg` (không dấu, không khoảng trắng).
- Khi có hình, rút gọn phần chữ của slide còn 3–5 dòng vì cột chữ hẹp lại.
- **Không đặt hình cạnh khối code**: cột code hẹp lại làm chữ code quá nhỏ. Slide có code thì để code chiếm cả chiều ngang; sơ đồ đặt ở slide giải thích liền trước/sau.
- **Sơ đồ vẽ bằng ký tự** (khối ```` ```text ```` có mũi tên `→`, `─▶`, `└──`) nên thay bằng sơ đồ thật trong `diagrams.json`; cây thư mục thì giữ dạng text.
- Sơ đồ nên ít chữ: mỗi hộp 1–5 từ, chú thích phụ ngắn. Chữ dài là dấu hiệu nên tách thành gạch đầu dòng trên slide.

### `build-images.py`: sơ đồ và ảnh

```bash
uv run --with matplotlib python build-images.py <hoc-phan>           # mọi hình
uv run --with matplotlib python build-images.py <hoc-phan> bai-03    # chỉ hình tên bắt đầu bằng bai-03
```
Sau khi sinh hình, build lại slide (`build-slides.py`) vì hình được nhúng vào `.pptx` lúc build.

`Slides/images/diagrams.json` – khóa là tên file PNG, giá trị là mô tả sơ đồ. Mục nào nhận `"chữ"` hoặc `["chữ", "chú thích nhỏ"]`. Tùy chọn chung: `"title"`, `"size": [rộng, cao]` (inch, mặc định tự chọn).

| `type` | Dùng cho | Trường chính |
|---|---|---|
| `flow` | quy trình, các bước | `steps`, `direction` (`h`/`v`), `branch: {"from": [0,1], "to": "...", "label": "..."}` (nhánh rẽ, vd. trạng thái hủy) |
| `cycle` | vòng lặp (Scrum, ngũ hành) | `steps`, `center` |
| `hub` | một khái niệm và các thành phần | `center`, `nodes` |
| `layers` | kiến trúc nhiều tầng | `layers` (mỗi tầng `{"name", "items"}` hoặc `["tên", "ghi chú"]`), `arrows` (`down`/`both`/`none`) |
| `columns` | so sánh 2–3 phương án | `columns: [{"title", "items"}]` |
| `pairs` | ánh xạ A → B (route → quyền, mã lỗi → HTTP) | `items: [[trái, phải]]`, `headers`, `both` |
| `timeline` | mốc thời gian | `events` |
| `tree` | phân cấp, sơ đồ chức năng | `root`, `children: [{"name", "children"}]` |
| `sequence` | sơ đồ tuần tự giữa các thành phần | `actors`, `messages: [[từ, đến, nhãn, "return"?]]` |
| `flowchart` | lưu đồ thuật toán (ký hiệu chuẩn) | `nodes: [{"id", "shape": "terminal"\|"io"\|"process"\|"decision", "text", "pos": [cột, hàng], "code": true?}]`, `edges: [[từ, đến, nhãn?, "left"\|"right"\|"down"?]]` (cạnh quay lên trên được vẽ vòng ra bên trái/phải, dùng cho vòng lặp; `"down"`: đi xuống trước rồi gom vào đường chung phía trên khối đích, dùng khi nhiều nhánh cùng về "Kết thúc"). Slide bìa ngang nên lưu đồ cao trên 5 hàng sẽ nhỏ: bố trí theo chiều ngang (các điều kiện xếp một hàng, nhánh Đúng đi xuống) và đặt lưu đồ trên slide chỉ có hình |

`Slides/images/photos.json` – `{"bai-03-my-son.jpg": "File:Tên file trên Wikimedia Commons.jpg"}`. Tìm tên file bằng API tìm kiếm của Commons (lọc giấy phép CC0, PD, CC BY, CC BY-SA).

## Build và kiểm tra
```bash
uv run --with python-pptx python build-slides.py <hoc-phan>        # mọi bài
uv run --with python-pptx python build-slides.py <hoc-phan> 03     # chỉ bài 03
```
Sau khi build, mở một vài file `.pptx` để xem chữ có tràn khung không (script tự giảm cỡ chữ 26 → 14pt theo lượng chữ). Slide nào quá dài thì tách ra ở file `.markdown` rồi build lại. Xử lý hết các `[CẢNH BÁO] Chưa có hình` hoặc báo lại cho giảng viên; `validate-course.py` cũng liệt kê các hình còn thiếu.
