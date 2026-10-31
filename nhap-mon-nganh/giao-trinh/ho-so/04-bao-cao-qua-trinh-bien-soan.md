# Báo cáo quá trình biên soạn giáo trình

> Bản nháp lập theo Điều 8 khoản 5 điểm c Thông tư 62/2026/TT-BGDĐT. Mục 3 hoàn thiện sau khi có ý kiến góp ý; các chỗ `{{...}}` do chủ biên điền.

## 1. Thông tin chung

- Tên tài liệu: Giáo trình Nhập môn Công nghệ Thông tin
- Học phần: Nhập môn Công nghệ Thông tin (111106), 45 tiết (9 buổi)
- Chủ biên: {{...}}; người biên soạn: {{...}}
- Căn cứ biên soạn: {{quyết định giao nhiệm vụ biên soạn, số, ngày}}

## 2. Mục tiêu và phạm vi

Xem `01-de-cuong-chi-tiet.md`: 9 chương, khoảng 74 trang (ước tính 350 từ/trang), kèm bài tập hướng dẫn theo từng chương.

## 3. Quá trình thực hiện

| Giai đoạn | Thời gian | Kết quả | Minh chứng |
|---|---|---|---|
| Lập và duyệt đề cương chi tiết | 2026-10-31 | Đề cương 9 chương, 4 CLO; giảng viên phụ trách duyệt | `01-de-cuong-chi-tiet.md` |
| Biên soạn bản thảo | 2026-10-31 | 9 chương, lời nói đầu, bài tập hướng dẫn | Lịch sử phiên bản git của thư mục `nhap-mon-nganh/giao-trinh` |
| Rà soát theo Điều 5 Thông tư 62/2026 | 2026-10-31 | Kiểm tra cấu trúc, trích dẫn, truy cập URL, đối chiếu nguồn chính thức | Mục 7 báo cáo này |
| Lấy ý kiến góp ý | {{...}} | {{số phiếu, đối tượng}} | `02-phieu-lay-y-kien.md`, phiếu đã nhận |
| Tiếp thu, hoàn thiện | {{...}} | {{số ý kiến tiếp thu / giải trình}} | `03-tong-hop-tiep-thu-giai-trinh.md` |

## 4. Cấu trúc tài liệu

Xem mục 3–5 của `01-de-cuong-chi-tiet.md` (ma trận CLO, nội dung từng chương, cân đối lý thuyết – thực hành).

## 5. Nguồn tài liệu và bản quyền

Danh mục tài liệu tham khảo chuẩn IEEE ở cuối mỗi chương; mỗi tài liệu được trích dẫn tại đúng đoạn sử dụng (kiểm tra tự động bằng `validate-course.py`). Tư liệu cần xin phép: {{không có / liệt kê}}.

## 6. Sử dụng công cụ AI

Bản thảo được soạn với sự hỗ trợ của trợ lý AI ở các khâu lập dàn ý, diễn đạt, viết mã nguồn ví dụ, rà soát định dạng và trích dẫn. Người biên soạn chịu trách nhiệm kiểm tra và chịu trách nhiệm về toàn bộ nội dung (Điều 7 khoản 3). {{Chủ biên bổ sung: cách kiểm tra đã thực hiện}}

## 7. Tự đánh giá theo Điều 5

| # | Yêu cầu | Kết quả | Ghi chú |
|---|---|---|---|
| 1 | Phù hợp đề cương học phần (Điều 2.2) | Đạt | Ma trận chương – CLO ở mục 3 của đề cương chi tiết; mỗi chương ứng với một buổi học. |
| 2 | Khoa học, logic, hệ thống (5.1, 5.2) | Đạt | Không có tiêu đề nhảy cấp; số mục khớp số chương. |
| 3 | Sư phạm (5.1) | Đạt | Mỗi chương có 4–6 mục tiêu, tóm tắt, 6–9 câu hỏi ôn tập, 3–5 bài tập. |
| 4 | Chính xác (5.1) | Đạt một phần | Dữ kiện về Khoa, ABET (chương trình Công nghệ kỹ thuật thông tin), ASU, BUILD-IT, lương đã đối chiếu nguồn (trang của Trường, Khoa, ITviec, tài liệu của Bộ TT&TT); chuẩn đầu ra tiếng Anh (TOEIC từ 400 hoặc tương đương) theo giảng viên phụ trách. Các dữ kiện chưa có văn bản công khai (năm thành lập Khoa, mô hình thực tập, doanh nghiệp đối tác) không đưa vào; sinh viên được hướng dẫn tra cứu nguồn chính thức. Mã nguồn ví dụ ngắn chưa chạy thử toàn bộ. |
| 5 | Cập nhật (5.1, 5.2) | Đạt | Công cụ AI (Gemini, Claude, Copilot, NotebookLM, Perplexity, Antigravity) và chính sách độ tuổi kiểm tra tháng 10/2026; báo cáo lương ITviec 2025–2026; tiêu chí ABET ETAC 2026–2027. Ghi rõ Luật CNTT 2006 được thay bởi Luật Chuyển đổi số 148/2025/QH15 (từ 01/7/2026) và Thông tư 08/2021 được thay bởi Thông tư 56/2026/TT-BGDĐT. |
| 6 | Nguồn trích dẫn hợp pháp (5.1) | Đạt | Trích dẫn khớp danh mục ở 9 chương; các bài báo khoa học đối chiếu qua Crossref; mọi URL kiểm tra truy cập tháng 10/2026. Kế thừa giáo trình Áp dụng ChatGPT của ThS. Nguyễn Minh Phúc (đã xác nhận tác giả, biên soạn năm 2024). |
| 7 | Liêm chính học thuật (5.1) | Chưa kiểm tra | Chưa chạy phần mềm kiểm tra trùng lặp; đề nghị chạy nếu Trường có công cụ. |
| 8 | Sở hữu trí tuệ (5.1) | Đạt | Không dùng hình ảnh bên ngoài; trích bảng lương, danh mục nghề có ghi nguồn; tài liệu nội bộ của Khoa ghi rõ là tài liệu nội bộ. |
| 9 | Không có nội dung bị nghiêm cấm (5.1) | Đạt | Đã rà các nội dung tôn giáo, dân tộc, bản đồ, chủ quyền, dữ liệu cá nhân: không phát hiện vấn đề. |
| 10 | Phù hợp chủ trương, chính sách, pháp luật (Điều 3, 5.2) | Đạt một phần | Dẫn Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15, Luật Sở hữu trí tuệ (sửa đổi 2025), Thông tư 56/2026/TT-BGDĐT. Định nghĩa CNTT vẫn dẫn Luật CNTT 2006 (đã ghi chú hết hiệu lực); nên đối chiếu Luật Chuyển đổi số 148/2025/QH15 và toàn văn Thông tư 56/2026 (định mức giờ/tín chỉ) khi hoàn thiện. |
| 11 | Cân đối lý thuyết – thực hành (5.2) | Đạt | Mỗi chương có câu hỏi ôn tập, 3 bài tập và bài tập hướng dẫn; học phần 3 tín chỉ (15 LT + 30 TH) với thực hành trên lớp mỗi buổi. |
| 12 | Khả năng tiếp cận (5.1) | Đạt một phần | Tiêu đề phân cấp, bảng có tiêu đề, prompt mẫu trong khung chữ đơn cách. Chưa có sơ đồ, hình minh họa trong giáo trình. |
| 13 | Dùng được dạng in và dạng số (5.1) | Đạt | Build được file Word có mục lục; mở Word và cập nhật mục lục (F9) trước khi in. |
| 14 | Kết hợp học liệu khác (5.1) | Đạt | Đã bổ sung mục "Học liệu đi kèm" trong Lời nói đầu (bài học LMS, slide, quiz, rubric). |
| 15 | Ngôn ngữ tiếng Việt (5.3) | Đạt | Toàn văn tiếng Việt; thuật ngữ và mã nguồn tiếng Anh giữ nguyên khi cần. |
| 16 | Minh bạch dùng AI (5.1, 7.3) | Cần xác nhận | Đã bổ sung đoạn "AI trong quá trình biên soạn" ở Lời nói đầu; chủ biên xác nhận câu chữ. |

## 8. Tồn tại và đề xuất

{{Chủ biên tổng hợp từ các mục Cần xác nhận, Cần xem xét, Đạt một phần ở bảng trên.}}
