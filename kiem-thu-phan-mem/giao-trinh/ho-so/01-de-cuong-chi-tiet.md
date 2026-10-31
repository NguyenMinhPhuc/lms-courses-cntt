# Đề cương chi tiết giáo trình

> Bước 1 của Điều 7 khoản 2 Thông tư 62/2026/TT-BGDĐT. **Dự thảo chờ duyệt**: chỉ biên soạn chương sau khi chủ biên duyệt đề cương này. Các chỗ `{{...}}` cần chủ biên cung cấp.

## 1. Thông tin chung

| Mục | Nội dung |
|---|---|
| Tên giáo trình | Kiểm thử và Đảm bảo chất lượng phần mềm |
| Loại tài liệu | {{Giáo trình / Tài liệu học tập}} |
| Học phần | Kiểm thử và Đảm bảo chất lượng phần mềm (111117), 3 tín chỉ; 45 tiết (15 LT + 30 TH) |
| Đối tượng người học | {{ngành, năm học, học phần tiên quyết}} |
| Chủ biên | {{Họ tên, học hàm, học vị, đơn vị}} |
| Người biên soạn | {{Họ tên}} (course.json chưa ghi giảng viên phụ trách) |
| Ngôn ngữ | Tiếng Việt |
| Hình thức khai thác | Bản số (Word/PDF) và bản in; kèm bài học LMS, slide, quiz và bộ biểu mẫu kiểm thử |
| Căn cứ | {{Đề cương học phần, số/năm}}; Thông tư 62/2026/TT-BGDĐT; {{quy định nội bộ của Trường, nếu có}} |

## 2. Mục tiêu của giáo trình

Giúp người học thực hiện trọn vẹn một vòng kiểm thử thủ công cho một sản phẩm phần mềm: lập kế hoạch, xác định yêu cầu kiểm thử, thiết kế và thực thi test case, ghi nhận và phân loại lỗi, lập báo cáo kiểm thử, với bộ biểu mẫu dùng được ngay trong đồ án và công việc. {{Chủ biên xác nhận hoặc chỉnh sửa.}}

## 3. Ma trận chương – chuẩn đầu ra học phần

CLO lấy từ bảng PI – CLO của Khoa (`templates/_KeHoach-Cac mon doc đánh giá các học phần.xlsx`, mã 111117, khóa 2024).

| CLO | Nội dung | PI | Chương rèn luyện chính |
|---|---|---|---|
| CLO1 | Viết báo cáo trình bày nội dung các công việc đã thực hiện bằng văn bản một cách hợp lý và đúng quy định về định dạng | PI 3.1 | 5, Phụ lục A, Phụ lục B |
| CLO2 | Thực hiện các bài kiểm thử để kiểm tra các yêu cầu chức năng phù hợp với các mục tiêu dự án | PI 4.1 | 1, 3, 4, 6 |
| CLO3 | Đo lường các kết quả thu được trong quá trình kiểm thử để đánh giá các chức năng đã xây dựng | PI 4.2 | 3 (độ bao phủ), 5 (số liệu báo cáo), 6 (mức độ lỗi) |
| CLO4 | Sử dụng kỹ năng trong việc sắp xếp công việc cá nhân hoặc nhóm phù hợp với mục tiêu công việc đề ra | PI 5.1 | 2 (Test Plan), Phụ lục B (kế hoạch đồ án 3 tuần) |

## 4. Nội dung chi tiết

Dự án mẫu xuyên suốt: **Notepad Cải Tiến** (đã có PRD, yêu cầu kiểm thử, test case, test report trong thư mục học phần); ví dụ nhỏ trên lớp dùng **Todo App** như bài giảng.

### Chương 1. Tổng quan về kiểm thử phần mềm (bài 01)
- **Mục tiêu:** trình bày khái niệm, mục đích của kiểm thử; phân biệt các cấp độ, loại và kỹ thuật kiểm thử; quyết định khi nào kiểm thử thủ công.
- **Nội dung:**
  - 1.1. Kiểm thử phần mềm là gì; kiểm thử và đảm bảo chất lượng
  - 1.2. Giá trị của hoạt động kiểm thử
  - 1.3. Các cách phân loại kiểm thử (cấp độ, loại, hộp đen – hộp trắng, thủ công – tự động)
  - 1.4. Khi nào nên kiểm thử thủ công
  - 1.5. *(Đề xuất bổ sung)* Bảy nguyên tắc kiểm thử [ISTQB]
- **Thực hành:** phân loại các hoạt động kiểm thử của Notepad Cải Tiến; bài tập hướng dẫn `bt-01`: đọc PRD Notepad Cải Tiến, liệt kê đối tượng kiểm thử.
- **Liên kết học liệu:** `bai-01`, slide, quiz bài 01.

### Chương 2. Lập kế hoạch kiểm thử (bài 02)
- **Mục tiêu:** xác định phạm vi, chiến lược, nguồn lực, lịch trình, rủi ro; viết được Test Plan.
- **Nội dung:**
  - 2.1. Test Plan là gì
  - 2.2. Thành phần chính của Test Plan
  - 2.3. Quy trình lập Test Plan
  - 2.4. Rủi ro và khả năng thích ứng
  - 2.5. Ví dụ phạm vi cho Todo App
- **Thực hành:** `bt-02`: Test Plan cho Notepad Cải Tiến theo biểu mẫu Phụ lục A.1.

### Chương 3. Xác định yêu cầu kiểm thử (bài 03)
- **Mục tiêu:** chuyển yêu cầu phần mềm thành yêu cầu kiểm thử rõ ràng, kiểm chứng được; lập ma trận truy xuất.
- **Nội dung:**
  - 3.1. Yêu cầu kiểm thử là gì
  - 3.2. Quy trình xác định yêu cầu kiểm thử
  - 3.3. Viết yêu cầu rõ ràng, có thể kiểm chứng
  - 3.4. Truy xuất và độ bao phủ (RTM)
  - 3.5. Thách thức và cách xử lý
- **Thực hành:** `bt-03`: danh sách yêu cầu kiểm thử và RTM cho Notepad Cải Tiến.

### Chương 4. Thiết kế test case (bài 04)
- **Mục tiêu:** viết test case đủ thành phần; thiết kế trường hợp bình thường, lỗi, biên; đánh giá chất lượng test case.
- **Nội dung:**
  - 4.1. Test case là gì
  - 4.2. Cấu trúc của một test case
  - 4.3. Quy trình thiết kế test case
  - 4.4. Trường hợp bình thường, lỗi và biên
  - 4.5. *(Đề xuất bổ sung)* Kỹ thuật phân vùng tương đương, phân tích giá trị biên, bảng quyết định [ISTQB]
  - 4.6. Chất lượng, khả năng bảo trì và ví dụ
- **Thực hành:** `bt-04`: bộ test case cho một chức năng Notepad Cải Tiến.

### Chương 5. Thực thi và báo cáo kiểm thử (bài 05)
- **Mục tiêu:** ghi nhật ký thực thi; lập Test Report; đọc và diễn giải số liệu kiểm thử.
- **Nội dung:**
  - 5.1. Test Report là gì
  - 5.2. Thành phần của báo cáo
  - 5.3. Quy trình lập Test Report
  - 5.4. Đọc và diễn giải số liệu
  - 5.5. Nguyên tắc báo cáo hiệu quả
- **Thực hành:** `bt-05`: nhật ký thực thi và Test Report cho Notepad Cải Tiến (mẫu `Test_Report_Notepad_CaiTien`).

### Chương 6. Nhận diện, phân loại và mô tả lỗi (bài 06)
- **Mục tiêu:** nhận diện và phân loại lỗi theo nhóm; đánh giá mức độ nghiêm trọng, độ ưu tiên; viết báo cáo lỗi tái hiện được.
- **Nội dung:**
  - 6.1. Vì sao cần phân loại lỗi
  - 6.2. Lỗi giao diện và trải nghiệm người dùng
  - 6.3. Lỗi chức năng
  - 6.4. Lỗi xác thực và dữ liệu đầu vào
  - 6.5. Lỗi hiệu năng và tải
  - 6.6. Lỗi bảo mật và lỗi tích hợp, hệ thống
  - 6.7. Mô tả lỗi hữu ích
- **Thực hành:** `bt-06`: báo cáo lỗi cho các lỗi tìm được ở `bt-05`; tham khảo `list-system-error.md`.

### Phụ lục A. Bộ biểu mẫu kiểm thử (bài 07)
A.1 Test Plan · A.2 Danh sách yêu cầu kiểm thử · A.3 Ma trận truy xuất (RTM) · A.4 Test Case · A.5 Nhật ký thực thi · A.6 Báo cáo lỗi · A.7 Test Report · A.8 Luồng sử dụng các biểu mẫu.

### Phụ lục B. Hướng dẫn đồ án cuối kỳ (bài 08)
Sản phẩm cần nộp; chọn dự án và phạm vi; nhiệm vụ bắt buộc; cấu trúc báo cáo; kế hoạch 3 tuần; phân công và tiêu chí đánh giá; checklist trước khi nộp.

## 5. Cân đối lý thuyết – thực hành

Học phần 15 LT + 30 TH, nên giáo trình thiên về thực hành: đề xuất khoảng **40% lý thuyết, 60% ví dụ, bài tập và bài tập hướng dẫn** (tính cả Phụ lục A). Mỗi chương có một bài tập hướng dẫn trên dự án Notepad Cải Tiến; sản phẩm của các bài tập ghép lại thành bộ hồ sơ kiểm thử hoàn chỉnh.

## 6. Tài liệu tham khảo chính (đề xuất)

- International Software Testing Qualifications Board, *Certified Tester Foundation Level (CTFL) Syllabus*, v4.0, 2023. [Online]. Available: https://www.istqb.org
- ISO/IEC/IEEE 29119 *Software and systems engineering – Software testing* (các phần 1–4, đặc biệt phần 3 về tài liệu kiểm thử).
- G. J. Myers, C. Sandler, T. Badgett, *The Art of Software Testing*, 3rd ed. Hoboken, NJ: Wiley, 2011.
- Tài liệu dự án mẫu của học phần: PRD Notepad Cải Tiến, Test Requirements, Test Case, Test Report (thư mục học phần).
- {{Giáo trình chính trong đề cương học phần 111117, nếu có}}

Bản tiêu chuẩn ISO/IEC/IEEE 29119 có bản quyền; chỉ trích dẫn, không sao chép nội dung. {{Xác nhận Khoa có bản tiêu chuẩn để tham khảo.}}

## 7. Học liệu đi kèm

Bài học LMS `bai-01`…`bai-08`, slide, ngân hàng câu hỏi, bộ biểu mẫu (Phụ lục A, có thể phát hành kèm dạng Word/Excel), tài liệu dự án mẫu Notepad Cải Tiến.

## 8. Phân công và tiến độ

| Công việc | Người phụ trách | Thời hạn |
|---|---|---|
| Duyệt đề cương | {{...}} | {{...}} |
| Biên soạn chương 1–3 | {{...}} | {{...}} |
| Biên soạn chương 4–6, phụ lục | {{...}} | {{...}} |
| Lấy ý kiến góp ý | {{...}} | {{...}} |
| Hoàn thiện, lập hồ sơ thẩm định | {{...}} | {{...}} |

## 9. Điểm cần chủ biên quyết định

1. ~~CLO của học phần~~: đã có từ bảng PI – CLO của Khoa.
2. Thứ tự chương 5–6: giữ theo bài giảng (báo cáo trước, lỗi sau) hay đổi theo quy trình (lỗi trước, báo cáo sau). Đề cương này giữ theo bài giảng để khớp LMS.
3. Có bổ sung mục 1.5 và 4.5 (nội dung theo ISTQB, chưa có trong bài giảng) không. Nếu có, cập nhật cả bài học và slide.
4. Loại tài liệu: Giáo trình hay Tài liệu học tập.
