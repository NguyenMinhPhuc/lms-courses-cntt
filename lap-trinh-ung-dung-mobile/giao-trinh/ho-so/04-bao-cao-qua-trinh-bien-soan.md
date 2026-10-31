# Báo cáo quá trình biên soạn giáo trình

> Bản nháp lập theo Điều 8 khoản 5 điểm c Thông tư 62/2026/TT-BGDĐT. Mục 3 hoàn thiện sau khi có ý kiến góp ý; các chỗ `{{...}}` do chủ biên điền.

## 1. Thông tin chung

- Tên tài liệu: Giáo trình Lập trình ứng dụng di động
- Học phần: Lập trình ứng dụng di động (111114), 60 tiết (15 LT + 45 TH)
- Chủ biên: {{...}}; người biên soạn: {{...}}
- Căn cứ biên soạn: {{quyết định giao nhiệm vụ biên soạn, số, ngày}}

## 2. Mục tiêu và phạm vi

Xem `01-de-cuong-chi-tiet.md`: 12 chương, khoảng 125 trang (ước tính 350 từ/trang), kèm bài tập hướng dẫn theo từng chương.

## 3. Quá trình thực hiện

| Giai đoạn | Thời gian | Kết quả | Minh chứng |
|---|---|---|---|
| Biên soạn bản thảo | 2026-10-29, 2026-10-30 | 12 chương, lời nói đầu, bài tập hướng dẫn | Lịch sử phiên bản git của thư mục `lap-trinh-ung-dung-mobile/giao-trinh` |
| Rà soát theo Điều 5 Thông tư 62/2026 | 2026-10-31 | Bổ sung mục Lời nói đầu, cập nhật nguồn, sửa trích dẫn, kiểm tra truy cập URL | Mục 7 báo cáo này |
| Lập đề cương chi tiết (hồi cứu) | 2026-10-31 | Đề cương theo cấu trúc bản thảo | `01-de-cuong-chi-tiet.md` |
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
| 4 | Chính xác (5.1) | Cần xác nhận | Chưa chạy lại toàn bộ mã nguồn mẫu trong đợt rà soát này; đề nghị nhóm biên soạn chạy dự án LHU Food theo từng chương. |
| 5 | Cập nhật (5.1, 5.2) | Đạt | Tài liệu chính thức truy cập tháng 10/2026; hướng dẫn cài thư viện bằng npx expo install để lấy phiên bản tương thích. |
| 6 | Nguồn trích dẫn hợp pháp (5.1) | Đạt | Trích dẫn khớp danh mục ở 12 chương. Đã kiểm tra truy cập các URL; các link đổi địa chỉ (Zustand, AsyncStorage, draw.io) đã cập nhật. |
| 7 | Liêm chính học thuật (5.1) | Chưa kiểm tra | Chưa chạy phần mềm kiểm tra trùng lặp; đề nghị chạy nếu Trường có công cụ. |
| 8 | Sở hữu trí tuệ (5.1) | Đạt | Mã nguồn mẫu do nhóm biên soạn viết cho dự án LHU Food; giáo trình không dùng hình ảnh bên ngoài. |
| 9 | Không có nội dung bị nghiêm cấm (5.1) | Đạt | Đã rà các nội dung tôn giáo, dân tộc, bản đồ, chủ quyền, dữ liệu cá nhân: không phát hiện vấn đề. |
| 10 | Phù hợp chủ trương, chính sách, pháp luật (Điều 3, 5.2) | Không áp dụng | Giáo trình không dẫn văn bản pháp luật. |
| 11 | Cân đối lý thuyết – thực hành (5.2) | Cần xem xét | Theo số từ: khoảng 70% lý thuyết, 30% câu hỏi, bài tập, bài tập hướng dẫn (chưa tính mã nguồn). Học phần có 45/60 tiết thực hành; thực hành chủ yếu diễn ra trên lớp theo bài tập hướng dẫn. |
| 12 | Khả năng tiếp cận (5.1) | Đạt một phần | Tiêu đề phân cấp, bảng có tiêu đề. 9 khối code dài hơn 40 dòng đã chuyển sang Phụ lục A (trong chương giữ trích đoạn 15 dòng). Chưa có sơ đồ trong giáo trình. |
| 13 | Dùng được dạng in và dạng số (5.1) | Đạt | Build được file Word có mục lục; mở Word và cập nhật mục lục (F9) trước khi in. |
| 14 | Kết hợp học liệu khác (5.1) | Đạt | Đã bổ sung mục "Học liệu đi kèm" trong Lời nói đầu (bài học LMS, slide, quiz, rubric). |
| 15 | Ngôn ngữ tiếng Việt (5.3) | Đạt | Toàn văn tiếng Việt; thuật ngữ và mã nguồn tiếng Anh giữ nguyên khi cần. |
| 16 | Minh bạch dùng AI (5.1, 7.3) | Cần xác nhận | Đã bổ sung đoạn "AI trong quá trình biên soạn" ở Lời nói đầu; chủ biên xác nhận câu chữ. |

## 8. Tồn tại và đề xuất

{{Chủ biên tổng hợp từ các mục Cần xác nhận, Cần xem xét, Đạt một phần ở bảng trên.}}
