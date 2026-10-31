# Đề cương chi tiết giáo trình

> Bước 1 của quy trình biên soạn (Điều 7 khoản 2 Thông tư 62/2026/TT-BGDĐT). Đề cương lập từ đề cương học phần và 12 bài giảng LMS đã duyệt của học phần 111155; dùng làm căn cứ biên soạn, lấy ý kiến và thẩm định.

## 1. Thông tin chung

| Mục | Nội dung |
|---|---|
| Tên giáo trình | Giáo trình Nhập môn lập trình – Tư duy giải quyết vấn đề với Python |
| Loại tài liệu | Giáo trình |
| Học phần | Nhập môn lập trình (111155), 3 tín chỉ (1 LT – 2 TH); 60 tiết (15 LT + 45 TH) |
| Đối tượng người học | Sinh viên năm thứ nhất ngành Công nghệ Thông tin, học kỳ 1; chưa cần kiến thức lập trình trước |
| Người biên soạn | ThS. Nguyễn Minh Phúc, Khoa Công nghệ Thông tin, Trường Đại học Lạc Hồng |
| Ngôn ngữ | Tiếng Việt; thuật ngữ và mã nguồn giữ tiếng Anh theo Python |
| Hình thức khai thác | Bản số (Word/PDF) và bản in; kèm học liệu số trên LMS |
| Căn cứ | Đề cương học phần 111155; Thông tư 62/2026/TT-BGDĐT; {{quy định nội bộ của Trường về biên soạn giáo trình, nếu có}} |

## 2. Mục tiêu của giáo trình

Giáo trình giúp sinh viên năm nhất hình thành thói quen **phân tích bài toán trước khi viết mã**: mô tả bài toán bằng bảng Input – Process – Output, biểu diễn thuật toán bằng lưu đồ, rồi hiện thực bằng Python 3 ở mức cơ bản (CLO1, CLO2). Nội dung đi theo một dự án xuyên suốt, Student Dashboard, được hoàn thiện dần qua từng chương, và kết thúc bằng một Mini Project nhóm có phân công rõ ràng (CLO3).

So với các giáo trình Python nhập môn hiện có, giáo trình bổ sung hướng dẫn **dùng trợ lý AI như trợ giảng có kiểm soát**: hỏi để hiểu, tự viết, tự kiểm chứng bằng dữ liệu biên và ghi Nhật ký Prompt. Giáo trình không dạy cách để AI viết hộ chương trình.

## 3. Ma trận chương – chuẩn đầu ra học phần

| Chương | CLO1 | CLO2 | CLO3 |
|---|:-:|:-:|:-:|
| 1. Chương trình, Python và tư duy Input – Process – Output | x | x | |
| 2. Toán tử và biểu thức | x | | |
| 3. Cấu trúc rẽ nhánh và lưu đồ thuật toán | x | x | |
| 4. Vòng lặp for, chuỗi và list | x | x | |
| 5. Vòng lặp while và chương trình có menu | x | x | |
| 6. Lỗi, ngoại lệ và gỡ lỗi | x | | |
| 7. Hàm và module | x | x | |
| 8. Tổ chức mã nguồn và chuẩn PEP 8 | x | | |
| 9. Phân tích và thiết kế một dự án nhỏ theo nhóm | | x | x |
| 10. Hoàn thiện, kiểm thử, quản lý mã nguồn và trình bày sản phẩm | x | | x |

- **CLO1:** Áp dụng ngôn ngữ lập trình để hiện thực các thuật toán đề ra ở mức cơ bản (PLO1 / PI 1.3).
- **CLO2:** Sử dụng được các công cụ đồ họa để trình bày các ý tưởng thiết kế dữ liệu: bảng IPO, lưu đồ, sơ đồ phân rã trên Draw.io (PLO3 / PI 3.4).
- **CLO3:** Thể hiện được vai trò cá nhân trong nhóm một cách rõ ràng (PLO5 / PI 5.2).

Bài 07 (kiểm tra giữa kỳ) và bài 12 (Showcase) là buổi đánh giá, không đưa vào giáo trình. Quy định đánh giá, rubric và hồ sơ nộp bài nằm trong đề cương học phần và trang đánh giá trên LMS.

## 4. Nội dung chi tiết

### Chương 1. Chương trình, Python và tư duy Input – Process – Output

**Mục tiêu:**

- Giải thích chương trình, ngôn ngữ lập trình và cách trình thông dịch Python chạy mã.
- Cài đặt Python 3.10+ và VS Code; tạo, chạy một chương trình Python.
- Phân tích bài toán đơn giản thành bảng Input – Process – Output.
- Dùng biến, các kiểu `int`, `float`, `str`, `bool`; nhập, xuất dữ liệu và định dạng bằng f-string.
- Đặt câu hỏi cho trợ lý AI đúng cách và ghi Nhật ký Prompt.

**Nội dung:**

- 1.1. Chương trình và ngôn ngữ lập trình
  - 1.1.1. Từ bài toán đến chương trình
  - 1.1.2. Python và trình thông dịch
- 1.2. Cài đặt môi trường làm việc
  - 1.2.1. Cài Python và VS Code
  - 1.2.2. Chương trình đầu tiên
  - 1.2.3. Chế độ tương tác và chạy file
- 1.3. Tư duy Input – Process – Output
  - 1.3.1. Ba thành phần của một bài toán
  - 1.3.2. Lập bảng IPO
- 1.4. Biến và kiểu dữ liệu cơ bản
  - 1.4.1. Biến và phép gán
  - 1.4.2. Quy tắc đặt tên
  - 1.4.3. Bốn kiểu dữ liệu cơ bản và hàm `type()`
- 1.5. Nhập, xuất và f-string
  - 1.5.1. `print()` và `input()`
  - 1.5.2. Chuyển kiểu dữ liệu
  - 1.5.3. Định dạng bằng f-string
- 1.6. Học lập trình cùng trợ lý AI
  - 1.6.1. AI là trợ giảng, không phải người làm hộ
  - 1.6.2. Viết prompt hỏi để hiểu
  - 1.6.3. Nhật ký Prompt

**Thực hành:** câu hỏi ôn tập, bài tập cuối chương; bài tập hướng dẫn `bt-01` (Student Dashboard v1: in thẻ hồ sơ cá nhân).
**Liên kết học liệu:** bài học `bai-01`, slide `Slides/bai-01.pptx`, quiz bài 01.
**Dung lượng dự kiến:** khoảng 14 trang; LT/TH khoảng 65/35.

### Chương 2. Toán tử và biểu thức

**Mục tiêu:**

- Sử dụng đúng các toán tử số học, kể cả `//`, `%`, `**`.
- Xác định thứ tự ưu tiên khi tính biểu thức và dùng dấu ngoặc đúng chỗ.
- Viết biểu thức so sánh, biểu thức logic và phép gán kết hợp.
- Làm tròn, định dạng số; giải thích sai số của số thực.
- Hiện thực bài toán tính toán có công thức (điểm trung bình, tiền điện theo bậc giả định).

**Nội dung:**

- 2.1. Toán tử số học
  - 2.1.1. Bảy toán tử số học
  - 2.1.2. Chia lấy nguyên và chia lấy dư
- 2.2. Thứ tự ưu tiên và dấu ngoặc
- 2.3. Toán tử so sánh, logic và gán kết hợp
  - 2.3.1. So sánh và kiểu `bool`
  - 2.3.2. `and`, `or`, `not`
  - 2.3.3. Gán kết hợp
- 2.4. Làm tròn, định dạng số và sai số số thực
  - 2.4.1. `round()` và định dạng `:.2f`
  - 2.4.2. Vì sao `0.1 + 0.2` khác `0.3`
- 2.5. Từ công thức đến chương trình
  - 2.5.1. Điểm trung bình học phần
  - 2.5.2. Kiểm tra kết quả bằng tính tay

**Thực hành:** câu hỏi ôn tập, bài tập cuối chương; bài tập hướng dẫn `bt-02` (Student Dashboard v2: điểm trung bình học phần).
**Liên kết học liệu:** bài học `bai-02`, slide, quiz bài 02.
**Dung lượng dự kiến:** khoảng 12 trang; LT/TH khoảng 60/40.

### Chương 3. Cấu trúc rẽ nhánh và lưu đồ thuật toán

**Mục tiêu:**

- Biểu diễn thuật toán bằng lưu đồ với bốn ký hiệu cơ bản.
- Viết đúng `if`, `if – else`, `if – elif – else` và quy tắc thụt lề.
- Sắp xếp điều kiện nhiều nhánh đúng thứ tự; kiểm thử bằng giá trị biên.
- Kết hợp điều kiện và viết rẽ nhánh lồng nhau.
- Vẽ lưu đồ trên Draw.io khớp với mã nguồn.

**Nội dung:**

- 3.1. Lưu đồ thuật toán
  - 3.1.1. Bốn ký hiệu cơ bản
  - 3.1.2. Quy tắc vẽ
  - 3.1.3. Vẽ lưu đồ trên Draw.io
- 3.2. Lệnh `if` và `if – else`
  - 3.2.1. Cú pháp và thụt lề
  - 3.2.2. Lỗi thụt lề thường gặp
- 3.3. Rẽ nhiều nhánh với `if – elif – else`
  - 3.3.1. Thứ tự các điều kiện
  - 3.3.2. Giá trị biên và bảng kiểm thử
- 3.4. Điều kiện kết hợp và rẽ nhánh lồng nhau
- 3.5. Từ lưu đồ đến mã và ngược lại

**Thực hành:** câu hỏi ôn tập, bài tập cuối chương; bài tập hướng dẫn `bt-03` (Student Dashboard v3: xếp loại học lực theo thang ví dụ).
**Liên kết học liệu:** bài học `bai-03`, slide, quiz bài 03; lưu đồ mẫu trong `Slides/images`.
**Dung lượng dự kiến:** khoảng 14 trang; LT/TH khoảng 60/40.

### Chương 4. Vòng lặp for, chuỗi và list

**Mục tiêu:**

- Dùng vòng lặp `for` với `range()` để lặp một số lần xác định.
- Áp dụng mẫu tích lũy: tính tổng, đếm, tìm lớn nhất, nhỏ nhất.
- Duyệt chuỗi và list; dùng chỉ số, `len()`, `append()`, các hàm `sum()`, `min()`, `max()`.
- Viết vòng lặp lồng nhau đơn giản.
- Vẽ lưu đồ có vòng lặp.

**Nội dung:**

- 4.1. Vòng lặp `for` và `range()`
- 4.2. Mẫu tích lũy
  - 4.2.1. Tổng và đếm
  - 4.2.2. Lớn nhất và nhỏ nhất
  - 4.2.3. Lưu đồ của mẫu tích lũy
- 4.3. Chuỗi
  - 4.3.1. Chỉ số và cắt chuỗi
  - 4.3.2. Duyệt từng ký tự
  - 4.3.3. Một số phương thức thường dùng
- 4.4. List cơ bản
  - 4.4.1. Tạo, truy cập, thêm phần tử
  - 4.4.2. Duyệt list
  - 4.4.3. Hàm có sẵn cho list
- 4.5. Vòng lặp lồng nhau

**Thực hành:** câu hỏi ôn tập, bài tập cuối chương; bài tập hướng dẫn `bt-04` (Student Dashboard v4: nhập điểm nhiều học phần và thống kê).
**Liên kết học liệu:** bài học `bai-04`, slide, quiz bài 04.
**Dung lượng dự kiến:** khoảng 14 trang; LT/TH khoảng 60/40.

### Chương 5. Vòng lặp while và chương trình có menu

**Mục tiêu:**

- Viết vòng lặp `while` có điều kiện dừng đúng; nhận biết vòng lặp vô hạn.
- Lặp yêu cầu nhập cho tới khi dữ liệu hợp lệ.
- Dùng `break`, `continue`; chọn giữa `for` và `while`.
- Xây dựng chương trình dòng lệnh có menu.
- Dùng AI hỗ trợ tìm lỗi vòng lặp và tự kiểm chứng.

**Nội dung:**

- 5.1. Vòng lặp `while`
  - 5.1.1. Cú pháp và điều kiện dừng
  - 5.1.2. Vòng lặp vô hạn
  - 5.1.3. Chọn `for` hay `while`
- 5.2. Lặp nhập đến khi hợp lệ
- 5.3. `break` và `continue`
  - 5.3.1. Ví dụ: trò chơi đoán số với `random.randint`
- 5.4. Chương trình có menu
  - 5.4.1. Khung menu với `while True`
  - 5.4.2. Lưu đồ của chương trình có menu
- 5.5. Tìm lỗi vòng lặp cùng AI

**Thực hành:** câu hỏi ôn tập, bài tập cuối chương; bài tập hướng dẫn `bt-05` (Student Dashboard v5: menu dòng lệnh).
**Liên kết học liệu:** bài học `bai-05`, slide, quiz bài 05.
**Dung lượng dự kiến:** khoảng 12 trang; LT/TH khoảng 55/45.

### Chương 6. Lỗi, ngoại lệ và gỡ lỗi

**Mục tiêu:**

- Phân biệt lỗi cú pháp, lỗi thực thi và lỗi logic.
- Đọc Traceback để xác định loại lỗi, dòng lỗi và nguyên nhân.
- Xử lý ngoại lệ bằng `try – except – else – finally`.
- Gỡ lỗi bằng breakpoint, chạy từng bước và quan sát biến trong VS Code.
- Dùng AI giải thích lỗi sau khi đã tự đoán, và kiểm chứng gợi ý của AI.

**Nội dung:**

- 6.1. Ba loại lỗi
- 6.2. Đọc Traceback
  - 6.2.1. Cấu trúc của Traceback
  - 6.2.2. Các ngoại lệ thường gặp
- 6.3. Xử lý ngoại lệ
  - 6.3.1. `try – except`
  - 6.3.2. Bắt đúng loại ngoại lệ
  - 6.3.3. `else` và `finally`
  - 6.3.4. Nhập số an toàn
- 6.4. Gỡ lỗi trong VS Code
  - 6.4.1. Breakpoint và chạy từng bước
  - 6.4.2. Tìm lỗi logic
- 6.5. Gỡ lỗi cùng AI
- 6.6. Kiểm thử bằng cách "phá chương trình"

**Thực hành:** câu hỏi ôn tập, bài tập cuối chương (dùng 5 đoạn mã của Lab "săn lỗi"); bài tập hướng dẫn `bt-06` (Student Dashboard v6: nhập liệu an toàn).
**Liên kết học liệu:** bài học `bai-06`, slide, quiz bài 06, `lab/bai-06-san-loi.zip`.
**Dung lượng dự kiến:** khoảng 13 trang; LT/TH khoảng 55/45.

### Chương 7. Hàm và module

**Mục tiêu:**

- Định nghĩa và gọi hàm với tham số, giá trị mặc định và `return`.
- Phân biệt hàm trả về giá trị với hàm chỉ in kết quả.
- Phân rã bài toán thành các hàm đơn nhiệm và vẽ sơ đồ phân rã.
- Tách chương trình thành nhiều module; dùng `import` và `if __name__ == "__main__"`.

**Nội dung:**

- 7.1. Vì sao cần hàm
- 7.2. Định nghĩa và gọi hàm
  - 7.2.1. `def`, tham số và đối số
  - 7.2.2. `return` và trả về nhiều giá trị
  - 7.2.3. Giá trị mặc định của tham số
- 7.3. `print` khác `return`
- 7.4. Phân rã bài toán
  - 7.4.1. Hàm đơn nhiệm
  - 7.4.2. Sơ đồ phân rã chức năng
- 7.5. Module
  - 7.5.1. Tách chương trình thành nhiều file
  - 7.5.2. `import` và `from … import`
  - 7.5.3. `if __name__ == "__main__"`
- 7.6. Thiết kế hàm cùng AI

**Thực hành:** câu hỏi ôn tập, bài tập cuối chương; bài tập hướng dẫn `bt-07` (Student Dashboard v8: ba module).
**Liên kết học liệu:** bài học `bai-08`, slide, quiz bài 08.
**Dung lượng dự kiến:** khoảng 13 trang; LT/TH khoảng 60/40.

### Chương 8. Tổ chức mã nguồn và chuẩn PEP 8

**Mục tiêu:**

- Giải thích phạm vi biến cục bộ, toàn cục và sửa lỗi `UnboundLocalError`.
- Đặt tên và trình bày mã theo PEP 8; kiểm tra bằng Ruff.
- Viết docstring và chú thích có ích.
- Refactor từng bước nhỏ mà không thay đổi kết quả chương trình.

**Nội dung:**

- 8.1. Phạm vi biến
  - 8.1.1. Biến cục bộ và biến toàn cục
  - 8.1.2. `UnboundLocalError`
  - 8.1.3. Truyền dữ liệu bằng tham số và `return`
- 8.2. PEP 8
  - 8.2.1. Quy tắc đặt tên
  - 8.2.2. Thụt lề, khoảng trắng, độ dài dòng
- 8.3. Ruff
  - 8.3.1. `ruff check` và `ruff format`
  - 8.3.2. Những gì công cụ không làm thay bạn
- 8.4. Docstring và chú thích
- 8.5. Refactor có kiểm soát
  - 8.5.1. Quy trình bốn bước
  - 8.5.2. Ví dụ trước và sau
  - 8.5.3. Refactor cùng AI

**Thực hành:** câu hỏi ôn tập, bài tập cuối chương; bài tập hướng dẫn `bt-08` (Student Dashboard v9: refactor theo PEP 8, Ruff sạch).
**Liên kết học liệu:** bài học `bai-09`, slide, quiz bài 09.
**Dung lượng dự kiến:** khoảng 12 trang; LT/TH khoảng 55/45.

### Chương 9. Phân tích và thiết kế một dự án nhỏ theo nhóm

**Mục tiêu:**

- Xác định phạm vi một đề tài dòng lệnh vừa sức nhóm 3–4 sinh viên.
- Lập bảng IPO cho từng chức năng; vẽ sơ đồ phân rã và lưu đồ cho chức năng chính.
- Lập bảng phân công, bảo đảm mỗi thành viên có phần mã riêng.
- Dùng AI để brainstorm phạm vi mà nhóm vẫn tự quyết định.

**Nội dung:**

- 9.1. Yêu cầu của Mini Project
- 9.2. Chọn và giới hạn đề tài
- 9.3. Phân tích chức năng
  - 9.3.1. Bảng IPO cho từng chức năng
  - 9.3.2. Sơ đồ phân rã
  - 9.3.3. Lưu đồ cho chức năng chính
- 9.4. Làm việc nhóm
  - 9.4.1. Bảng phân công
  - 9.4.2. Nhật ký Prompt của nhóm
- 9.5. Ví dụ: thiết kế đề tài Quản lý chi tiêu cá nhân

**Thực hành:** câu hỏi ôn tập, bài tập cuối chương; bài tập hướng dẫn `bt-09` (hồ sơ thiết kế đề tài Quản lý chi tiêu).
**Liên kết học liệu:** bài học `bai-10`, slide, quiz bài 10.
**Dung lượng dự kiến:** khoảng 11 trang; LT/TH khoảng 50/50.

### Chương 10. Hoàn thiện, kiểm thử, quản lý mã nguồn và trình bày sản phẩm

**Mục tiêu:**

- Ghép mã của các thành viên và kiểm thử tích hợp với năm loại dữ liệu.
- Quản lý mã nguồn nhóm trên GitHub: repository, clone, commit, push, pull, xử lý xung đột đơn giản.
- Viết README.md cho sản phẩm.
- Trình bày sản phẩm và giải thích được phần mã mình phụ trách.

**Nội dung:**

- 10.1. Ghép mã và kiểm thử tích hợp
  - 10.1.1. Năm loại dữ liệu kiểm thử
  - 10.1.2. Bảng kiểm thử
- 10.2. Quản lý mã nguồn với Git và GitHub
  - 10.2.1. Khái niệm cơ bản
  - 10.2.2. Quy trình với GitHub Desktop
  - 10.2.3. Thông điệp commit
  - 10.2.4. Push bị từ chối và xung đột
- 10.3. README.md
- 10.4. Rà soát mã cùng AI
- 10.5. Trình bày và giải thích sản phẩm
  - 10.5.1. Kịch bản demo
  - 10.5.2. Giải thích mã nguồn của mình

**Thực hành:** câu hỏi ôn tập, bài tập cuối chương; bài tập hướng dẫn `bt-10` (hoàn thiện, đưa lên GitHub và viết README cho đề tài Quản lý chi tiêu).
**Liên kết học liệu:** bài học `bai-11`, slide, quiz bài 11.
**Dung lượng dự kiến:** khoảng 12 trang; LT/TH khoảng 50/50.

### Phụ lục. Tra cứu nhanh

Bảng cú pháp Python dùng trong giáo trình, các hàm có sẵn thường dùng, các ngoại lệ thường gặp và cách xử lý, ký hiệu lưu đồ, các lệnh Ruff và thao tác GitHub Desktop. Dung lượng dự kiến khoảng 5 trang.

## 5. Cân đối lý thuyết – thực hành

| Chương | Trang dự kiến | Lý thuyết và ví dụ | Câu hỏi, bài tập, bài tập hướng dẫn |
|---|:-:|:-:|:-:|
| 1–3 | 40 | khoảng 62% | khoảng 38% |
| 4–6 | 39 | khoảng 57% | khoảng 43% |
| 7–8 | 25 | khoảng 57% | khoảng 43% |
| 9–10 | 23 | khoảng 50% | khoảng 50% |
| Phụ lục | 5 | – | – |
| **Tổng** | **khoảng 130** | | |

Học phần có 75% thời lượng thực hành (15 LT + 45 TH). Giáo trình giữ phần lý thuyết đủ để sinh viên tự học trước buổi học, còn phần thực hành nằm ở bài tập cuối chương và bài tập hướng dẫn. Các chương 9–10 nghiêng về thực hành vì là giai đoạn làm dự án nhóm.

## 6. Tài liệu tham khảo chính

- [1] Python Software Foundation, “The Python Tutorial,” *Python 3 Documentation*. Accessed: Oct. 31, 2026. [Online]. Available: https://docs.python.org/3/tutorial/
- [2] Python Software Foundation, “The Python Language Reference,” *Python 3 Documentation*. Accessed: Oct. 31, 2026. [Online]. Available: https://docs.python.org/3/reference/
- [3] Python Software Foundation, “Built-in Functions,” *Python 3 Documentation*. Accessed: Oct. 31, 2026. [Online]. Available: https://docs.python.org/3/library/functions.html
- [4] Python Software Foundation, “Built-in Exceptions,” *Python 3 Documentation*. Accessed: Oct. 31, 2026. [Online]. Available: https://docs.python.org/3/library/exceptions.html
- [5] G. van Rossum, B. Warsaw, and A. Coghlan, “PEP 8 – Style Guide for Python Code,” *Python Enhancement Proposals*. Accessed: Oct. 31, 2026. [Online]. Available: https://peps.python.org/pep-0008/
- [6] D. Goodger and G. van Rossum, “PEP 257 – Docstring Conventions,” *Python Enhancement Proposals*. Accessed: Oct. 31, 2026. [Online]. Available: https://peps.python.org/pep-0257/
- [7] A. B. Downey, *Think Python: How to Think Like a Computer Scientist*, 2nd ed. Sebastopol, CA, USA: O’Reilly Media, 2015.
- [8] Microsoft, “Python in Visual Studio Code,” *Visual Studio Code Documentation*. Accessed: Oct. 31, 2026. [Online]. Available: https://code.visualstudio.com/docs/languages/python
- [9] Astral, “Ruff,” *Ruff Documentation*. Accessed: Oct. 31, 2026. [Online]. Available: https://docs.astral.sh/ruff/
- [10] *Information processing – Documentation symbols and conventions for data, program and system flowcharts, program network charts and system resources charts*, ISO 5807:1985.
- [11] GitHub, “GitHub Desktop documentation,” *GitHub Docs*. Accessed: Oct. 31, 2026. [Online]. Available: https://docs.github.com/en/desktop
- [12] JGraph Ltd, “draw.io documentation,” *draw.io*. Accessed: Oct. 31, 2026. [Online]. Available: https://www.drawio.com/doc/

Ghi chú: mọi nguồn trên đều là tài liệu công khai, chỉ trích dẫn và diễn đạt lại, không chép nguyên văn nên không cần xin phép. Bản đọc trực tuyến của *Think Python* [7] phát hành theo giấy phép CC BY-NC; giáo trình chỉ trích dẫn, không sao chép nội dung. Tài liệu tham khảo của từng chương lập theo chuẩn IEEE và đánh số lại từ [1] trong mỗi chương.

## 7. Học liệu đi kèm

- 12 bài học trên LMS (`bai-01` … `bai-12`) theo mô hình lớp học đảo ngược, kèm quiz luyện tập trên web.
- Slide bài giảng PowerPoint cho 12 buổi.
- Ngân hàng 144 câu hỏi trắc nghiệm định dạng Aiken để nhập vào Moodle.
- Mã nguồn mẫu của từng chương (Student Dashboard v1–v9) và bộ 5 đoạn mã của Lab "săn lỗi".
- Đề cương, trang đánh giá học phần và rubric (quy định đánh giá không nằm trong giáo trình).

## 8. Phân công và tiến độ

| Công việc | Người phụ trách | Thời hạn |
|---|---|---|
| Duyệt đề cương chi tiết | ThS. Nguyễn Minh Phúc | {{...}} |
| Biên soạn Lời nói đầu, chương 1–3 | ThS. Nguyễn Minh Phúc | {{...}} |
| Biên soạn chương 4–6 | ThS. Nguyễn Minh Phúc | {{...}} |
| Biên soạn chương 7–8 | ThS. Nguyễn Minh Phúc | {{...}} |
| Biên soạn chương 9–10, phụ lục | ThS. Nguyễn Minh Phúc | {{...}} |
| Rà soát bản thảo theo Điều 5 | ThS. Nguyễn Minh Phúc | {{...}} |
| Lấy ý kiến góp ý (phiếu 02) | ThS. Nguyễn Minh Phúc | {{...}} |
| Tiếp thu, hoàn thiện, lập hồ sơ thẩm định | ThS. Nguyễn Minh Phúc | {{...}} |
