# Dàn ý chi tiết - Nhập môn lập trình (111155)

> Bản để giảng viên duyệt **trước khi** viết bài học, slide và quiz. Nguồn: `thong-tin-hoc-phan-nhap-mon-lap-trinh.md` (đề cương 12 buổi), CLO trong `templates/_KeHoach-Cac mon doc đánh giá các học phần.xlsx`, quy định cộng điểm trong `templates/thong-bao-truyen-thong.md`.

> **Đã duyệt (31/10/2026):** giảng viên đồng ý toàn bộ đề xuất:
> - Dự án xuyên suốt Student Dashboard.
> - Bài 4 dạy list cơ bản.
> - Bài toán tiền điện dùng bảng giá giả định.
> - Thang xếp loại dùng thang ví dụ, ghi rõ là ví dụ.
> - Không dạy `match-case`; dùng `random.randint`; Python 3.10+; Ruff.
> - Kiểm tra giữa kỳ:
>   - Được hỏi AI giải thích cú pháp, lỗi; không dán đề cho AI.
>   - Mọi prompt ghi vào Nhật ký Prompt.
>   - Giảng viên có thể quy định chặt hơn.
> - Mini Project:
>   - Nhóm 3–4 sinh viên.
>   - Đề tài chọn trong danh sách gợi ý hoặc tự đề xuất, giảng viên duyệt.
>   - Nộp mã nguồn qua GitHub (giao diện web hoặc GitHub Desktop).

- **Đối tượng:** sinh viên năm 1 ngành Công nghệ thông tin, học kỳ 1, chưa học lập trình (không có học phần tiên quyết). Đây là học phần học trước của Kỹ thuật lập trình (111161).
- **Khối lượng:** 3 TC (1-2-0), 60 tiết = 12 buổi × 5 tiết, gồm 15 tiết lý thuyết và 45 tiết thực hành. Mỗi buổi 1,5 tiết lý thuyết và 3,5 tiết thực hành. Buổi 7 (kiểm tra) và buổi 12 (Showcase) là 5 tiết thực hành.
- **Phương pháp:** lớp học đảo ngược (xem video và bài đọc trên LMS trước buổi học) kết hợp vibe coding nhập môn. Trên lớp chủ yếu là lab.
- **Công cụ:** Python 3 (từ 3.10), VS Code với Python extension, một trợ lý AI (ChatGPT, Claude hoặc Gemini), Draw.io để vẽ lưu đồ, GitHub để lưu mã nguồn (buổi 11).
- **Nguyên tắc dùng AI:**
  - AI là trợ giảng: giải thích, tìm lỗi, gợi ý hướng làm.
  - Sinh viên tự viết code và giải thích được từng dòng.
  - Mỗi bài lab ghi **Nhật ký Prompt**: prompt đã dùng, AI trả lời gì, mình đã kiểm tra và sửa ra sao.
- **Dự án xuyên suốt (đề xuất):** **"Student Dashboard"**, chương trình dòng lệnh quản lý hồ sơ và kết quả học tập của một sinh viên. Mỗi buổi thêm một chức năng:
  - Buổi 1: in hồ sơ.
  - Buổi 2: tính điểm trung bình.
  - Buổi 3: xếp loại.
  - Buổi 4: thống kê.
  - Buổi 5: menu.
  - Buổi 6: nhập liệu an toàn.
  - Buổi 8–9: tách hàm, refactor.

  Dự án này gắn với hashtag `#PythonDashboardChallenge` và là mẫu tham khảo cho Mini Project của nhóm ở buổi 10–12.
- **Nguồn tham khảo đề xuất (cần giảng viên xác nhận):**
  - Tài liệu chính thức Python: *The Python Tutorial* (docs.python.org) và PEP 8 – Style Guide for Python Code.
  - A. B. Downey, *Think Python*, 2nd ed., O'Reilly (bản mở trên greenteapress.com).
  - Giáo trình hoặc bài giảng nội bộ của Khoa (nếu có).

## Chuẩn đầu ra học phần (CLO)

| CLO | Nội dung | Bloom | PI |
|---|---|---|---|
| CLO1 | Áp dụng ngôn ngữ lập trình để hiện thực các thuật toán đề ra ở mức cơ bản | Kỹ năng (3) | PI1.3 – Hiện thực các thuật toán bằng các kỹ năng lập trình |
| CLO2 | Sử dụng được các công cụ đồ họa để trình bày các ý tưởng thiết kế dữ liệu | Kỹ năng (3) | PI3.4 – Biết cách sử dụng đồ họa để trình bày các ý tưởng |
| CLO3 | Thể hiện được vai trò cá nhân trong nhóm một cách rõ ràng | Thái độ (3) | PI5.2 – Thể hiện được vai trò cá nhân trong nhóm một cách rõ ràng |

CLO2 được hiện thực bằng **lưu đồ thuật toán** (Flowchart, Draw.io) và sơ đồ Input – Process – Output. Mục tiêu KSA của đề cương mới được gắn vào ba CLO trên:
- Phần Kiến thức và kỹ năng phân tích thuộc CLO1.
- Phần vẽ lưu đồ thuộc CLO2.
- Phần làm việc nhóm, giải thích code thuộc CLO3.

## Đánh giá (đã chốt: 30 – 30 – 40)

| Thành phần | Hình thức | CLO | Tỷ lệ |
|---|---|---|---|
| A1. Quá trình | Bài lab mỗi buổi trên LMS; Nhật ký Prompt; thái độ và phản biện (giải thích được code AI hỗ trợ, tự sửa lỗi) | CLO1, CLO2 | 30% |
| A2. Giữa kỳ | Bài kiểm tra thực hành cá nhân tại lớp ở buổi 7 (5 tiết): bài toán tổng hợp buổi 1–6, có lưu đồ, nộp kèm Nhật ký Prompt | CLO1, CLO2 | 30% |
| A3. Cuối kỳ | Mini Project nhóm: chương trình Python, lưu đồ, README, Nhật ký Prompt; Showcase buổi 12 có vấn đáp từng thành viên | CLO1, CLO2, CLO3 | 40% |

**Điểm cộng truyền thông:** +0,5 đến +1,0 điểm vào điểm đồ án nhóm, theo thông báo chung. Bài đăng công khai, có ảnh nhóm cùng sản phẩm, caption 50–150 từ và đủ hashtag `#TenTruong #TenNganh #LapTrinhVoiAI #VibeCoding #TuyenSinh2027 #NhapMonLapTrinh #PythonDashboardChallenge`. Link bài đăng nộp trong phụ lục báo cáo ở buổi 12.

---

## Bài 01 - Làm quen Python và tư duy Input – Process – Output (5 tiết: 1,5 LT / 3,5 TH)
- **CLO liên quan:** CLO1, CLO2
- **Mục tiêu (Bloom):**
  - Cài đặt được Python 3 và VS Code; chạy được chương trình đầu tiên.
  - Phân tích được một bài toán thành Input – Process – Output.
  - Khai báo được biến với 4 kiểu `int`, `float`, `str`, `bool`; nhập và xuất bằng `input()`, `print()`, f-string.
- **Ý chính:**
  1. **Chương trình và ngôn ngữ lập trình.** Máy tính chỉ làm theo lệnh; Python là ngôn ngữ thông dịch, dễ đọc. Ví dụ: chạy `print("Hello, LHU!")` trong VS Code và trong chế độ tương tác.
  2. **Tư duy Input – Process – Output (IPO).** Trước khi viết code phải xác định đầu vào, xử lý, đầu ra. Ví dụ: bài toán "in hồ sơ sinh viên". Input là họ tên, năm sinh, lớp; Process là tính tuổi; Output là thẻ hồ sơ.
  3. **Biến và kiểu dữ liệu cơ bản.** Quy tắc đặt tên, `type()`, chuyển kiểu bằng `int()`, `float()`, `str()`. Ví dụ: `input()` luôn trả về `str`, nên `"2007" + 1` gây lỗi.
  4. **Nhập, xuất và f-string.** `input()`, `print()` với `sep`, `end`, f-string `f"{ten} - {tuoi} tuổi"`. Ví dụ: in "Hồ sơ số hóa cá nhân" có khung ký tự.
- **Hoạt động trên lớp:**
  - Cài môi trường theo checklist.
  - Lab 1: viết `ho_so.py`.
  - Hỏi AI giải thích cú pháp f-string, rồi tự viết lại không nhìn đáp án.
- **Bài tập nộp:** `ho_so.py` (phiên bản đầu của Student Dashboard), bảng IPO của bài toán, Nhật ký Prompt (2–3 prompt).
- **Slide dự kiến:** khoảng 14 slide (có ảnh minh họa cài đặt, sơ đồ IPO).
- **Điểm cần giảng viên xác nhận:**
  - Phiên bản Python tối thiểu (đề xuất 3.10+).
  - Có dùng thêm Google Colab cho máy yếu không?
  - Giới thiệu sinh viên dùng AI nào (miễn phí)?

## Bài 02 - Toán tử, biểu thức và bài toán tính toán (5 tiết: 1,5 LT / 3,5 TH)
- **CLO liên quan:** CLO1, CLO2
- **Mục tiêu:**
  - Sử dụng được toán tử số học, so sánh, logic và gán kết hợp.
  - Xác định được thứ tự ưu tiên trong biểu thức.
  - Hiện thực được các bài toán tính toán từ bảng IPO.
- **Ý chính:**
  1. **Toán tử số học.**
     - `+ - * / // % **`; khác biệt giữa `/` và `//`.
     - `%` dùng để tách chữ số.
     - Ví dụ: đổi 135 phút thành "2 giờ 15 phút".
  2. **Thứ tự ưu tiên và dấu ngoặc.** Ví dụ: `a + b / 2` khác `(a + b) / 2` khi tính điểm trung bình. Cho AI trình bày từng bước tính một biểu thức, sinh viên đối chiếu bằng tay.
  3. **Toán tử so sánh, logic, gán kết hợp.**
     - `== != < > <= >=`, `and or not`, `+=`.
     - Ví dụ: biểu thức kiểm tra "điểm hợp lệ" `0 <= diem <= 10`.
  4. **Làm tròn và định dạng số.**
     - `round()`, f-string `:.2f`, phân cách hàng nghìn `:,`.
     - Lưu ý sai số số thực: `0.1 + 0.2`.
     - Ví dụ: tính tiền điện theo đơn giá một bậc rồi bậc thang đơn giản (bảng giá do giảng viên cung cấp).
- **Hoạt động trên lớp:** Lab 2 gồm 3 bài:
  - Điểm trung bình học phần theo trọng số 30-30-40.
  - Đổi đơn vị.
  - Tiền điện.
  - Mỗi bài viết bảng IPO trước khi code.
- **Bài tập nộp:** thêm chức năng "tính điểm trung bình" vào Student Dashboard; Nhật ký Prompt.
- **Slide dự kiến:** khoảng 14 slide (bảng thứ tự ưu tiên, sơ đồ tính từng bước).
- **Điểm cần giảng viên xác nhận:**
  - Bài tiền điện dùng bảng giá EVN thực tế (cần ghi nguồn, năm) hay bảng giá giả định cho đơn giản?

## Bài 03 - Cấu trúc rẽ nhánh if – elif – else (5 tiết: 1,5 LT / 3,5 TH)
- **CLO liên quan:** CLO1, CLO2
- **Mục tiêu:**
  - Biểu diễn được điều kiện rẽ nhánh bằng lưu đồ (khối hình thoi).
  - Viết được `if`, `if-else`, `if-elif-else` và rẽ nhánh lồng nhau với điều kiện kết hợp.
- **Ý chính:**
  1. **Lưu đồ thuật toán.** Các ký hiệu bắt đầu/kết thúc, nhập/xuất, xử lý, điều kiện, mũi tên. Ví dụ: lưu đồ kiểm tra số chẵn lẻ vẽ trên Draw.io.
  2. **`if` và `if-else`; thụt lề trong Python.** Ví dụ: kiểm tra đậu/rớt (điểm ≥ 4,0); lỗi `IndentationError` khi thụt lề sai.
  3. **`if-elif-else` nhiều nhánh.** Thứ tự điều kiện quan trọng. Ví dụ: xếp loại học lực từ điểm hệ 10 (Xuất sắc, Giỏi, Khá, Trung bình, Yếu); kiểm thử bằng các giá trị biên 8,0 và 6,5.
  4. **Điều kiện kết hợp và rẽ nhánh lồng.** Ví dụ:
     - ATM đơn giản: kiểm tra PIN, rồi kiểm tra số dư, rồi kiểm tra bội số 50.000.
     - Phân loại khách hàng theo tổng chi tiêu và năm thành viên.
- **Hoạt động trên lớp:**
  - Vẽ lưu đồ trước, code sau.
  - Prompt mẫu: "Viết ví dụ if-elif-else mức nhập môn, chỉ dùng kiến thức buổi 1–3, không dùng hàm hay list."
  - So sánh lời giải của AI với lưu đồ của mình.
- **Bài tập nộp:** chức năng "xếp loại" cho Student Dashboard kèm lưu đồ (.drawio hoặc .png); Nhật ký Prompt.
- **Slide dự kiến:** khoảng 15 slide (ký hiệu lưu đồ, 2–3 lưu đồ mẫu).
- **Điểm cần giảng viên xác nhận:**
  - Thang xếp loại dùng mức nào: theo quy chế của Trường hay thang ví dụ?
  - Có giới thiệu `match-case` (Python 3.10) không? Đề xuất: không, để giữ mức nhập môn.

## Bài 04 - Vòng lặp for và duyệt tập hợp cơ bản (5 tiết: 1,5 LT / 3,5 TH)
- **CLO liên quan:** CLO1, CLO2
- **Mục tiêu:**
  - Giải thích được cơ chế lặp và biến đếm.
  - Sử dụng được `for` với `range()` và với chuỗi.
  - Viết được vòng lặp lồng nhau và các mẫu tích lũy (tổng, đếm, lớn nhất).
- **Ý chính:**
  1. **Vì sao cần vòng lặp; `range(start, stop, step)`.** Ví dụ: in bảng cửu chương 7; lần theo từng chu kỳ lặp bằng bảng giá trị biến (trace table).
  2. **Mẫu tích lũy.** Tổng, đếm, tìm lớn nhất/nhỏ nhất. Ví dụ: tổng 1 + 2 + … + n, tổng các số chẵn, đếm số chia hết cho 3.
  3. **Duyệt chuỗi.** `for ch in chuoi`, `len()`, chỉ số. Ví dụ: đếm nguyên âm trong họ tên, đảo ngược chuỗi.
  4. **Vòng lặp lồng nhau.** Ví dụ: vẽ hình vuông, tam giác vuông, tam giác cân bằng ký tự `*`; in bảng cửu chương đầy đủ.
- **Hoạt động trên lớp:**
  - Lab 4: 5 bài từ dễ đến khó.
  - Nhờ AI giải thích "chu kỳ lặp thứ 3 đang làm gì", sinh viên tự ghi bảng trace để đối chiếu.
- **Bài tập nộp:** chức năng "thống kê" cho Student Dashboard (nhập điểm n học phần bằng vòng lặp, tính trung bình, điểm cao nhất); Nhật ký Prompt.
- **Slide dự kiến:** khoảng 15 slide (lưu đồ vòng lặp, bảng trace).
- **Điểm cần giảng viên xác nhận:**
  - Đề cương ghi "duyệt tập hợp cơ bản". Có dạy **list** ở mức cơ bản (tạo, `append`, duyệt, `len`, `sum`, `max`) không, hay chỉ `range` và chuỗi?
  - Đề xuất: dạy list cơ bản ở bài này, vì Mini Project gần như chắc chắn cần lưu nhiều dữ liệu.

## Bài 05 - Vòng lặp while và menu tương tác (5 tiết: 1,5 LT / 3,5 TH)
- **CLO liên quan:** CLO1, CLO2
- **Mục tiêu:**
  - Phân biệt được khi nào dùng `for`, khi nào dùng `while`.
  - Thiết lập được điều kiện dừng; dùng được `break`, `continue`.
  - Xây dựng được menu dòng lệnh (CLI) lặp tới khi người dùng chọn thoát.
- **Ý chính:**
  1. **`while` và điều kiện dừng; lặp vô hạn.** Ví dụ: đếm ngược; cố ý tạo vòng lặp vô hạn rồi dừng bằng Ctrl + C, chỉ ra biến điều khiển không được cập nhật.
  2. **Lặp nhập dữ liệu hợp lệ.** Ví dụ: yêu cầu nhập điểm tới khi nằm trong 0–10.
  3. **`break`, `continue`, `while True`.** Ví dụ: trò chơi đoán số với `random.randint`, giới hạn 7 lần, gợi ý "lớn hơn/nhỏ hơn".
  4. **Menu CLI.** Mẫu `while True` gồm in menu, đọc lựa chọn, rẽ nhánh, "0. Thoát". Ví dụ: menu Student Dashboard gồm Xem hồ sơ, Nhập điểm, Xếp loại, Thống kê, Thoát.
- **Hoạt động trên lớp:**
  - Lab 5: trò chơi đoán số, rồi menu Student Dashboard.
  - Hỏi AI "vì sao vòng lặp của em không dừng", dán code của mình, yêu cầu AI chỉ ra dòng lỗi chứ không viết lại toàn bộ.
- **Bài tập nộp:** Student Dashboard có menu hoàn chỉnh; Nhật ký Prompt.
- **Slide dự kiến:** khoảng 14 slide (lưu đồ while, sơ đồ menu).
- **Điểm cần giảng viên xác nhận:**
  - Có dùng module `random` (chỉ `import` và `randint`) ở bài này không? Đề xuất: có, chỉ ở mức gọi hàm.

## Bài 06 - Xử lý ngoại lệ try – except và debugging (5 tiết: 1,5 LT / 3,5 TH)
- **CLO liên quan:** CLO1
- **Mục tiêu:**
  - Đọc được thông báo lỗi (Traceback) để tìm dòng và loại lỗi.
  - Phân biệt được lỗi cú pháp, lỗi thực thi và lỗi logic.
  - Dùng được `try-except` (có `else`, `finally`) để bắt `ValueError`, `ZeroDivisionError`.
  - Debug được bằng `print` và breakpoint trong VS Code.
- **Ý chính:**
  1. **Ba loại lỗi.** Cú pháp (`SyntaxError`), thực thi (exception), logic (chạy được nhưng sai kết quả). Ví dụ: mỗi loại một đoạn code ngắn.
  2. **Đọc Traceback.** Đọc từ dưới lên: loại lỗi, thông điệp, file và dòng. Ví dụ: nhập "mười" vào `int(input())` sinh ra `ValueError`.
  3. **`try-except-else-finally`.** Bắt đúng loại lỗi, không dùng `except:` trống. Ví dụ: hàm nhập số an toàn, chia cho 0 khi tính trung bình của 0 học phần.
  4. **Debugging trong VS Code.** Breakpoint, Step Over, xem biến. Dùng AI đọc lỗi: dán Traceback và yêu cầu "giải thích nguyên nhân bằng ngôn ngữ dễ hiểu và gợi ý chỗ cần sửa".
- **Hoạt động trên lớp:**
  - Lab 6 "săn lỗi": giảng viên phát 5 đoạn code có lỗi, sinh viên tự đoán trước rồi mới hỏi AI.
  - Ghi bảng gồm các cột: lỗi, loại, nguyên nhân, cách sửa, đoán đúng chưa.
- **Bài tập nộp:** Student Dashboard không bị dừng khi nhập sai; bảng săn lỗi; Nhật ký Prompt.
- **Slide dự kiến:** khoảng 14 slide (ảnh chụp Traceback có chú thích, ảnh debugger).
- **Điểm cần giảng viên xác nhận:** không có.

## Bài 07 - Kiểm tra giữa kỳ (thực hành tại lớp, 5 tiết TH)
- **CLO liên quan:** CLO1, CLO2 (A2 – 30%)
- **Mục tiêu:** tự giải được một bài toán tổng hợp kiến thức buổi 1–6 bằng Python, có phân tích IPO và lưu đồ, dùng AI có kiểm soát và ghi Nhật ký Prompt.
- **Ý chính (nội dung trang bài học):**
  1. **Phạm vi và hình thức.** Bài cá nhân, 5 tiết, trên máy phòng lab; được dùng AI hay không, mức nào do giảng viên quy định.
  2. **Cấu trúc bài làm.** Bảng IPO, lưu đồ phần xử lý chính, mã nguồn, chạy thử với ít nhất 3 bộ dữ liệu (có trường hợp biên và nhập sai).
  3. **Nhật ký Prompt khi kiểm tra.** Ghi đủ prompt, câu trả lời và phần mình tự sửa; không dán nguyên lời giải.
  4. **Tiêu chí chấm (rubric A2).** Phân tích IPO, lưu đồ đúng ký hiệu, chương trình chạy đúng, xử lý nhập sai, trình bày code, giải thích được code khi giảng viên hỏi.
- **Hoạt động trên lớp:** làm bài; giảng viên vấn đáp ngẫu nhiên vài sinh viên về code của chính họ.
- **Bài tập nộp:** file `.py`, lưu đồ, Nhật ký Prompt lên LMS.
- **Slide dự kiến:** khoảng 6 slide (quy định, cấu trúc bài làm, rubric). Không có đề trong slide.
- **Điểm cần giảng viên xác nhận:**
  - **Đề kiểm tra** do giảng viên ra. Tôi chỉ soạn hướng dẫn, rubric và 1 đề luyện tập mẫu.
  - Mức được dùng AI khi kiểm tra.
  - Có đóng Internet không?

## Bài 08 - Hàm cơ bản và tách module (5 tiết: 1,5 LT / 3,5 TH)
- **CLO liên quan:** CLO1, CLO2
- **Mục tiêu:**
  - Định nghĩa và gọi được hàm với tham số, giá trị mặc định, `return`.
  - Phân biệt được `print` với `return`.
  - Tách được bài toán thành các hàm đơn nhiệm.
  - Import được hàm từ file `.py` khác.
- **Ý chính:**
  1. **Vì sao cần hàm.** Tránh lặp code, dễ kiểm thử. Ví dụ: đoạn "nhập số an toàn" bị chép 4 lần trong Student Dashboard.
  2. **`def`, tham số, đối số, giá trị mặc định, `return`.** Ví dụ: `tinh_diem_tb(qt, gk, ck)`, `xep_loai(diem)`; hàm trả nhiều giá trị bằng tuple ở mức đơn giản.
  3. **`print` khác `return`.** Hàm chỉ in thì không tái sử dụng được kết quả. Ví dụ: so sánh hai phiên bản của `xep_loai`.
  4. **Tách bài toán và module.**
     - Sơ đồ phân rã chức năng (mỗi hộp một hàm).
     - Tách `tinh_toan.py` và `main.py`, `import`.
     - Dùng `if __name__ == "__main__":` ở mức giới thiệu.
- **Hoạt động trên lớp:**
  - Vẽ sơ đồ phân rã Student Dashboard.
  - Yêu cầu AI "đề xuất cách chia chương trình thành các hàm, chỉ nêu tên hàm, tham số, giá trị trả về, không viết code".
  - Tự cài đặt từng hàm và kiểm thử riêng.
- **Bài tập nộp:** Student Dashboard viết lại bằng hàm, có 2 file; sơ đồ phân rã; Nhật ký Prompt.
- **Slide dự kiến:** khoảng 15 slide (giải phẫu một hàm, sơ đồ phân rã).
- **Điểm cần giảng viên xác nhận:** không có.

## Bài 09 - Tổ chức mã nguồn và chuẩn PEP 8 (5 tiết: 1,5 LT / 3,5 TH)
- **CLO liên quan:** CLO1
- **Mục tiêu:**
  - Giải thích được phạm vi biến (local, global) và hậu quả của biến toàn cục.
  - Áp dụng được quy tắc đặt tên và trình bày theo PEP 8.
  - Viết được docstring.
  - Refactor được code cho dễ đọc mà không đổi kết quả.
- **Ý chính:**
  1. **Phạm vi biến.** Biến cục bộ, biến toàn cục, `global` (biết để tránh). Ví dụ: hàm sửa nhầm biến toàn cục làm sai thống kê.
  2. **PEP 8.**
     - `snake_case`, hằng số `UPPER_CASE`, thụt lề 4 dấu cách, độ dài dòng, khoảng trắng quanh toán tử.
     - Kiểm tra tự động bằng Pylint hoặc Ruff trong VS Code.
  3. **Docstring và chú thích.** Mô tả mục đích, tham số, giá trị trả về; chú thích giải thích "vì sao", không lặp lại code.
  4. **Refactor có kiểm soát.**
     - Đặt lại tên biến.
     - Bỏ "số ma thuật" thành hằng số.
     - Rút gọn rẽ nhánh lặp.
     - Kiểm tra kết quả trước và sau.
     - Prompt: "Refactor đoạn code theo PEP 8, giữ nguyên chức năng, liệt kê từng thay đổi và lý do."
- **Hoạt động trên lớp:**
  - Lab 9: refactor một chương trình "xấu" do giảng viên cung cấp.
  - So sánh với đề xuất của AI và chọn thay đổi nào chấp nhận, kèm lý do.
- **Bài tập nộp:** Student Dashboard bản hoàn chỉnh theo PEP 8, có docstring; bảng thay đổi khi refactor; Nhật ký Prompt.
- **Slide dự kiến:** khoảng 14 slide (so sánh trước/sau).
- **Điểm cần giảng viên xác nhận:** dùng Pylint hay Ruff (đề xuất: Ruff, cài qua extension).

## Bài 10 - Khởi động Mini Project và vẽ lưu đồ (5 tiết: 1,5 LT / 3,5 TH)
- **CLO liên quan:** CLO2, CLO3
- **Mục tiêu:**
  - Chọn và mô tả được đề tài nhóm.
  - Lập được bảng IPO và lưu đồ cho từng chức năng chính trên Draw.io.
  - Phân công được nhiệm vụ rõ ràng cho từng thành viên.
- **Ý chính:**
  1. **Yêu cầu Mini Project.**
     - Nhóm 3–4 sinh viên.
     - Chương trình CLI có menu, ít nhất 4 chức năng, dùng đủ rẽ nhánh, vòng lặp, hàm, try-except.
     - Danh sách đề tài gợi ý: quản lý chi tiêu, thư viện mini, bán vé xem phim, quiz trắc nghiệm, quản lý điểm lớp.
  2. **Phân tích đề tài.** Bảng IPO cho từng chức năng, sơ đồ phân rã thành các hàm.
  3. **Lưu đồ trên Draw.io.** Quy ước ký hiệu, mỗi lưu đồ một chức năng, xuất `.png` để đưa vào báo cáo.
  4. **Làm việc nhóm và phân công.**
     - Bảng phân công: ai làm hàm nào, hạn hoàn thành.
     - Dùng AI brainstorm ý tưởng, nhưng nhóm tự quyết định phạm vi.
     - Phổ biến quy định điểm cộng truyền thông.
- **Hoạt động trên lớp:** nhóm chọn đề tài và trình bày nhanh 2 phút; giảng viên duyệt phạm vi.
- **Bài tập nộp:** bản kế hoạch đồ án (đề tài, IPO, lưu đồ, sơ đồ hàm, bảng phân công).
- **Slide dự kiến:** khoảng 12 slide.
- **Điểm cần giảng viên xác nhận:**
  - Số thành viên mỗi nhóm.
  - Danh sách đề tài gợi ý; nhóm có được tự chọn đề tài ngoài danh sách không?

## Bài 11 - Hoàn thiện project và quản lý mã nguồn (5 tiết: 1,5 LT / 3,5 TH)
- **CLO liên quan:** CLO1, CLO3
- **Mục tiêu:**
  - Ghép được các hàm của thành viên thành chương trình hoàn chỉnh.
  - Xử lý được trường hợp biên.
  - Lưu mã nguồn lên GitHub (thao tác cơ bản).
  - Viết được README và kịch bản demo.
- **Ý chính:**
  1. **Ghép và kiểm thử tích hợp.** Danh sách kiểm thử theo từng chức năng, gồm dữ liệu thường, biên và sai.
  2. **Quản lý mã nguồn cơ bản.** Tạo repository trên GitHub, tải code lên qua giao diện web hoặc GitHub Desktop, commit có thông điệp rõ ràng. Git dòng lệnh chỉ giới thiệu.
  3. **README.md.** Tên đề tài, thành viên và vai trò, cách chạy, ảnh chụp màn hình, phần khai báo dùng AI.
  4. **Rà soát cùng AI.** Nhờ AI rà lỗi tổng thể và góp ý README, kịch bản demo. Từng thành viên phải giải thích được phần mình làm.
- **Hoạt động trên lớp:** lab nhóm; giảng viên kiểm tra tiến độ từng nhóm, hỏi ngẫu nhiên thành viên về code.
- **Bài tập nộp:** link repository, README, bản nháp kịch bản demo.
- **Slide dự kiến:** khoảng 12 slide (ảnh thao tác GitHub).
- **Điểm cần giảng viên xác nhận:**
  - Bắt buộc dùng GitHub hay chỉ nộp file nén lên LMS?
  - Có dùng GitHub Classroom không?

## Bài 12 - Showcase và báo cáo đồ án cuối kỳ (5 tiết TH)
- **CLO liên quan:** CLO1, CLO2, CLO3 (A3 – 40%)
- **Mục tiêu:**
  - Demo được chương trình.
  - Giải thích được thuật toán qua lưu đồ.
  - Trình bày được Nhật ký Prompt.
  - Trả lời được câu hỏi về phần việc của mình.
- **Ý chính (nội dung trang bài học):**
  1. **Cấu trúc buổi Showcase.** Mỗi nhóm 7–10 phút: demo, giải thích lưu đồ một chức năng, Nhật ký Prompt, vấn đáp.
  2. **Hồ sơ nộp.** Mã nguồn hoặc link repository, báo cáo ngắn (IPO, lưu đồ, phân công, khai báo AI), Nhật ký Prompt, link bài đăng truyền thông (phụ lục).
  3. **Rubric A3.**
     - Chương trình chạy đúng.
     - Chia hàm hợp lý.
     - Xử lý ngoại lệ.
     - Lưu đồ (CLO2).
     - Vai trò cá nhân và vấn đáp (CLO3).
     - Nhật ký Prompt.
  4. **Tổng kết học phần.** Nhìn lại kỹ năng IPO, lưu đồ, AI như co-pilot; kết nối với Kỹ thuật lập trình ở học kỳ 2.
- **Hoạt động trên lớp:** các nhóm báo cáo; bình chọn sản phẩm ấn tượng.
- **Bài tập nộp:** hồ sơ đồ án hoàn chỉnh lên LMS.
- **Slide dự kiến:** khoảng 8 slide.
- **Điểm cần giảng viên xác nhận:**
  - Thời lượng mỗi nhóm.
  - Có mời khách (doanh nghiệp, sinh viên khóa trên) chấm không?

---

## Sản phẩm sẽ làm sau khi dàn ý được duyệt

- **Trang thông tin:**
  - `thong-tin-hoc-phan.md`: đề cương LMS, bám file đề cương của giảng viên và các quyết định ở trên.
  - `danh-gia-hoc-phan.md`: rubric A1, A2, A3 và điểm cộng truyền thông.
  - `README.md`.
- **Bài học:** `bai-01.md` … `bai-12.md`.
- **Slide:** `Slides/bai-XX.markdown` và `.pptx` dựng trên `templates/Template-slide.pptx`, có hình minh họa.
- **Quiz:** `quiz/quiz-bai-XX-aiken.txt`, 10 câu mỗi bài cho bài 1–6 và 8–9; bài 7, 10, 11, 12 không có quiz kiến thức.
- **Landing page:** `index.html`.
- **Hoàn tất:** đăng ký portal, chạy `validate-course.py`.
- **Làm theo đợt:**
  - Đợt 1: đề cương, đánh giá, bài 1–3.
  - Đợt 2: bài 4–7.
  - Đợt 3: bài 8–12.
  - Slide và quiz làm cùng đợt với bài học.

## Ghi chú về các nguồn

- **Đề cương BM05 của CTĐT 2026 cho 111155 đã cũ.** Đề cương này (trong `chuong-trinh-dao-tao/cntt-2026/du-lieu/de-cuong/111155.md`) dạy Scratch và C#, có 3 CLO nhưng bảng đánh giá lại nhắc tới CLO4. Đề cương mới của bạn dạy Python, nên cần cập nhật BM05 theo học phần này khi xây dựng CTĐT khóa sau.
- **Tài liệu tham khảo trong Tóm tắt học phần không khớp.** File Tóm tắt học phần 2026 ghi học phần dạy Python nhưng tài liệu tham khảo là sách lập trình C.
