## 1. Lỗi Giao diện & Trải nghiệm người dùng (UI/UX Bugs)
- Các lỗi liên quan đến cách hiển thị trực quan và tương tác với người dùng:
- Lỗi hiển thị văn bản: Sai chính tả, mất chữ, tràn viền, văn bản đè lên nhau hoặc xuống dòng không đúng chỗ.
- Lỗi giao diện đáp ứng (Responsive): Giao diện bị vỡ, méo mó hoặc hiển thị sai khi thay đổi kích thước màn hình (trên điện thoại, máy tính bảng, desktop).
- Lỗi căn chỉnh & màu sắc: Thành phần (nút bấm, icon, hình ảnh) bị lệch pha, sai màu thương hiệu, hoặc không đồng nhất font chữ.
- Trạng thái phần tử (States): Nút bấm không chuyển sang trạng thái mờ (disabled) khi chưa đủ điều kiện, hoặc thiếu hiệu ứng hover/active.

# 2. Lỗi Chức năng (Functional Bugs)
- Lỗi xảy ra khi tính năng của phần mềm không hoạt động đúng như tài liệu yêu cầu (SRS):
- Lỗi tính toán: Sai logic nghiệp vụ (ví dụ: tính sai tổng tiền đơn hàng, áp dụng sai mã giảm giá, thuế).
- Lỗi luồng nghiệp vụ (Workflow): Người dùng có thể nhảy cóc qua các bước bắt buộc (ví dụ: thanh toán thành công mà không cần qua bước chọn địa chỉ giao hàng).
- Lỗi tìm kiếm & lọc: Kết quả trả về không khớp với từ khóa tìm kiếm hoặc bộ lọc được chọn.
- Lỗi phân quyền (Access Control): Người dùng thông thường có thể truy cập vào trang quản trị (Admin) hoặc thực hiện hành động vượt quyền.

# 3. Lỗi Xác thực & Dữ liệu đầu vào (Validation & Input Bugs)
- Lỗi liên quan đến việc xử lý thông tin do người dùng nhập vào:
- Thiếu kiểm tra đầu vào (Missing Validation): Cho phép nhập chuỗi rỗng, nhập chữ vào ô số điện thoại, hoặc nhập email sai định dạng (thiếu ký tự @).
- Vượt quá giới hạn ký tự (Boundary Check): Hệ thống bị treo (crash) hoặc lỗi giao diện khi người dùng nhập quá số lượng ký tự cho phép (ví dụ: ô họ tên nhập 500 ký tự).
- Lỗi mã hóa/Ký tự đặc biệt: Hệ thống gặp lỗi khi nhập các ký tự đặc biệt như <, >, &, emoji hoặc tiếng Việt có dấu (lỗi hiển thị dấu hỏi ??? hoặc lỗi hệ thống).

# 4. Lỗi Hiệu năng & Tải (Performance & Load Bugs)
- Tời gian phản hồi chậm: Tải trang, tải dữ liệu (loading) quá lâu vượt ngưỡng cho phép (thường > 3 giây).
- Lỗi rò rỉ bộ nhớ (Memory Leak): Ứng dụng tiêu thụ RAM hoặc CPU tăng dần theo thời gian sử dụng và gây đơ máy.
- Quá tải hệ thống: Hệ thống sập (crash) hoặc không phản hồi khi có nhiều người dùng truy cập cùng một lúc (Concurrent Users).

# 5. Lỗi Bảo mật (Security Vulnerabilities)
- Lỗi SQL Injection: Kẻ tấn công có thể nhập câu lệnh SQL vào ô input để can thiệp vào cơ sở dữ liệu.
- Lỗi XSS (Cross-Site Scripting): Cho phép chạy mã độc JavaScript thông qua ô nhập liệu.
- Lộ thông tin nhạy cảm: Mật khẩu hiển thị dạng văn bản thuần túy (plain text) trên màn hình, hoặc token/session không được mã hóa an toàn.
- Quên phân quyền API: Gọi trực tiếp đường dẫn API nhưng không kiểm tra token xác thực.

# 6. Lỗi Tích hợp & Hệ thống (Integration & System Bugs)
- Lỗi kết nối API: API trả về mã lỗi (500, 404, 401) hoặc phản hồi sai định dạng dữ liệu (JSON/XML).
- Lỗi bên thứ ba (Third-party): Lỗi khi tích hợp cổng thanh toán (VNPay, Momo, Stripe), dịch vụ đăng nhập nhanh (Google, Facebook) hoặc dịch vụ gửi SMS OTP.
- Lỗi cơ sở dữ liệu: Mất kết nối DB, lỗi đồng bộ dữ liệu giữa các bảng hoặc sai lệch dữ liệu sau khi thực hiện giao dịch (Transaction rollback thất bại).
