# Danh sách tự rà soát theo Điều 5 Thông tư 62/2026/TT-BGDĐT

Dùng ở bước 4 (trước khi lấy ý kiến) và bước 7 (trước khi lập hồ sơ thẩm định). Chạy `validate-course.py` trước; những mục script không tự kiểm được thì rà tay. Ghi kết quả vào mục "Tự đánh giá" của báo cáo quá trình biên soạn (`ho-so/04-bao-cao-qua-trinh-bien-soan.md`).

| # | Yêu cầu (điều, khoản) | Cách kiểm tra |
|---|---|---|
| 1 | Phù hợp chương trình/đề cương học phần đã ban hành (Điều 2.2) | Ma trận chương – CLO đủ; nội dung khớp đề cương học phần |
| 2 | Khoa học, logic, hệ thống (5.1, 5.2) | Mục lục đi từ khái niệm đến vận dụng; không lặp, không nhảy cấp tiêu đề; thuật ngữ thống nhất |
| 3 | Sư phạm (5.1) | Mỗi chương có mục tiêu đo được, ví dụ, tóm tắt, câu hỏi ôn tập, bài tập |
| 4 | Chính xác (5.1) | Định nghĩa, số liệu, mã nguồn đã đối chiếu nguồn; mã nguồn mẫu đã chạy thử; không còn `{{CẦN KIỂM TRA}}` |
| 5 | Cập nhật (5.1, 5.2) | Phiên bản công nghệ, văn bản pháp luật còn hiệu lực, số liệu mới nhất có thể; ngày truy cập nguồn web |
| 6 | Nguồn trích dẫn hợp pháp (5.1) | `validate-course.py`: trích dẫn [n] khớp danh mục; nguồn là xuất bản phẩm, trang chính thức; không dùng tài liệu lậu |
| 7 | Liêm chính học thuật (5.1) | Không chép nguyên đoạn dài; trích nguyên văn có ngoặc kép/khối trích dẫn và nguồn; đã chạy kiểm tra trùng lặp nếu Trường yêu cầu |
| 8 | Sở hữu trí tuệ (5.1) | Hình tự vẽ hoặc giấy phép mở có ghi tác giả; tư liệu có bản quyền đã xin phép (lưu minh chứng); giấy phép của mã nguồn mẫu |
| 9 | Không có nội dung bị nghiêm cấm (5.1) | Rà các nội dung chính trị, lịch sử, tôn giáo, dân tộc, bản đồ (chủ quyền biển đảo), dữ liệu cá nhân trong ví dụ |
| 10 | Phù hợp chủ trương, chính sách, pháp luật (Điều 3, 5.2) | Nội dung liên quan dẫn văn bản còn hiệu lực, ghi số hiệu, ngày |
| 11 | Cân đối lý thuyết – thực hành, phù hợp thực tiễn (5.2) | Tỷ lệ LT/TH theo đề cương chi tiết; ví dụ từ thực tiễn Việt Nam, dự án mẫu |
| 12 | Khả năng tiếp cận (5.1) | Tiêu đề phân cấp, bảng có tiêu đề, hình có chú thích, không truyền tin chỉ bằng màu, chữ đủ lớn trong hình |
| 13 | Dùng được dạng in và dạng số (5.1) | Build `.docx`, cập nhật mục lục (F9), xem bản in đen trắng; liên kết ngoài có ghi URL đầy đủ |
| 14 | Kết hợp học liệu khác (5.1) | Lời nói đầu có mục học liệu đi kèm; chương trỏ tới bài giảng, slide, quiz tương ứng |
| 15 | Ngôn ngữ tiếng Việt (5.3) | Toàn văn tiếng Việt; thuật ngữ nước ngoài có giải thích |
| 16 | Minh bạch dùng AI (5.1 liêm chính; 7.3 trách nhiệm) | Lời nói đầu có quy ước dùng AI; báo cáo biên soạn ghi khâu AI hỗ trợ và cách kiểm tra |

Mục nào chưa đạt: ghi rõ chương, mục, việc cần làm; không đánh dấu đạt cho mục chưa kiểm tra.
