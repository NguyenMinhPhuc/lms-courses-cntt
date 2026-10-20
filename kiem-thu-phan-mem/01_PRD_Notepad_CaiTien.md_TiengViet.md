# MẪU YÊU CẦU SẢN PHẨM

## TÊN SẢN PHẨM
Notepad Cải Tiến Hỗ Trợ Testing Manual

## TÁC GIẢ
Nguyễn Văn An

## ĐIỆN THOẠI
+84 987 654 321

## E-MAIL
nguyenvanan@example.com

## ĐỊA CHỈ
789 Đường Testing, Quận 1, TP. Hồ Chí Minh, Việt Nam

## NGÀY
29/04/2025

## TỔNG QUAN
Notepad Cải Tiến là một ứng dụng ghi chú trên Windows, được phát triển dựa trên Notepad gốc, nhằm hỗ trợ các nhóm kiểm thử thủ công (manual testing). Ứng dụng giữ lại các tính năng cốt lõi như chỉnh sửa văn bản, lưu/mở file, tìm kiếm, đồng thời bổ sung các tính năng như gắn thẻ, tìm kiếm nâng cao, và xuất báo cáo để phục vụ QA engineer trong việc ghi lại và quản lý kết quả kiểm thử.

## MỤC TIÊU SẢN PHẨM
- **Mục tiêu 1**: Duy trì giao diện đơn giản và tính năng cơ bản của Notepad để dễ sử dụng.
- **Mục tiêu 2**: Cung cấp công cụ gắn thẻ và tìm kiếm nâng cao để quản lý ghi chú kiểm thử.
- **Mục tiêu 3**: Hỗ trợ xuất báo cáo kiểm thử dưới dạng CSV hoặc TXT.
- **Mục tiêu 4**: Đảm bảo ứng dụng nhẹ, tương thích với Windows 10 trở lên.
- **Mục tiêu 5**: Cho phép hoạt động offline, phù hợp với môi trường kiểm thử không có internet.

## XÁC ĐỊNH CÁC BÊN LIÊN QUAN
| TÊN              | VAI TRÒ                 | TRÁCH NHIỆM                                      | LỢI ÍCH ĐỐI VỚI SẢN PHẨM                          |
|------------------|-------------------------|--------------------------------------------------|--------------------------------------------------|
| Trần Thị Bình    | Trưởng nhóm QA          | Cung cấp thông tin về nhu cầu kiểm thử.          | Công cụ hỗ trợ quản lý ghi chú kiểm thử hiệu quả.|
| Lê Văn Cường, Phạm Đức Dũng | Nhóm phát triển         | Phát triển và bảo trì ứng dụng.                  | Yêu cầu rõ ràng để phát triển nhanh chóng.       |
| Nguyễn Minh Hoàng| Quản lý dự án           | Giám sát tiến độ và phân bổ nguồn lực.           | Hoàn thành đúng hạn trong ngân sách.            |

## YÊU CẦU CHỨC NĂNG
1. **Chỉnh sửa và lưu văn bản**:
   - Người dùng có thể tạo, chỉnh sửa và lưu ghi chú dưới dạng file .txt.
   - Hỗ trợ mở file .txt hiện có từ máy tính.
2. **Tìm kiếm và thay thế**:
   - Tìm kiếm văn bản trong ghi chú hiện tại (tương tự Notepad gốc).
   - Hỗ trợ thay thế văn bản (replace) với tùy chọn phân biệt hoa thường.
3. **Gắn thẻ (Tagging)**:
   - Người dùng có thể thêm thẻ tùy chỉnh cho từng ghi chú (ví dụ: "Lỗi", "Kiểm thử UI", "Hồi quy").
   - Hỗ trợ nhiều thẻ trên một ghi chú.
4. **Tìm kiếm nâng cao**:
   - Tìm kiếm ghi chú dựa trên thẻ, từ khóa hoặc trạng thái (ví dụ: Pass/Fail).
   - Lọc ghi chú theo ngày tạo hoặc trạng thái.
5. **Xuất báo cáo**:
   - Xuất ghi chú được chọn thành file CSV hoặc TXT.
   - Báo cáo bao gồm tiêu đề, nội dung, thẻ, trạng thái và thời gian tạo.

## YÊU CẦU PHI CHỨC NĂNG
1. **Hiệu suất**:
   - Thời gian khởi động ứng dụng dưới 1 giây.
   - Tìm kiếm hoàn thành trong vòng 0,5 giây với 10.000 ghi chú.
2. **Khả năng sử dụng**:
   - Giao diện tương tự Notepad gốc, tuân thủ thiết kế Windows.
   - Hỗ trợ phím tắt quen thuộc (Ctrl+S, Ctrl+F).
3. **Bảo mật**:
   - File ghi chú được lưu cục bộ và mã hóa bằng AES-256.
   - Tùy chọn bảo vệ ứng dụng bằng mật khẩu.
4. **Tương thích**:
   - Tương thích với Windows 10 và Windows 11 (64-bit).
   - Không yêu cầu kết nối internet.
5. **Dung lượng**:
   - Kích thước ứng dụng cài đặt dưới 50MB.

## GIẢ ĐỊNH VÀ RÀNG BUỘC
### Giả định
1. Người dùng đã quen với cách sử dụng Notepad trên Windows.
2. Ứng dụng sẽ được phân phối qua Microsoft Store hoặc cài đặt trực tiếp.
3. Đội kiểm thử sử dụng tiếng Anh hoặc tiếng Việt cho ghi chú.
4. Máy tính đáp ứng yêu cầu tối thiểu (2GB RAM, 500MB dung lượng trống).

### Ràng buộc
1. Ngân sách phát triển giới hạn ở 80.000 USD.
2. Phiên bản đầu tiên phải hoàn thành trong 2,5 tháng.
3. Không hỗ trợ đồng bộ đám mây trong giai đoạn đầu.
4. Chỉ hỗ trợ hệ điều hành Windows.

## PHỤ THUỘC
1. **Windows API**: Dùng cho giao diện và xử lý file.
2. **Thư viện mã hóa**: Sử dụng thư viện mã hóa tích hợp trong .NET để mã hóa file.
3. **SQLite**: Lưu trữ cục bộ thông tin thẻ và siêu dữ liệu ghi chú.

## TIÊU CHÍ CHẤP NHẬN
1. **Chức năng ghi chú**:
   - Người dùng có thể tạo, lưu và mở file .txt trong vòng 3 giây.
   - Ghi chú tự động lưu mỗi 5 giây.
2. **Tìm kiếm và thay thế**:
   - Tìm kiếm trả về kết quả chính xác 100% cho từ khóa hoặc thẻ.
   - Thay thế văn bản hoàn thành trong vòng 1 giây.
3. **Xuất báo cáo**:
   - Báo cáo CSV/TXT chứa đầy đủ thông tin (tiêu đề, thẻ, trạng thái).
   - Quá trình xuất hoàn thành trong 5 giây cho 1.000 ghi chú.
4. **Bảo mật**:
   - Tất cả file ghi chú được mã hóa và không thể truy cập nếu thiếu mật khẩu.

## PHÂN TÍCH RỦI RO
| RỦI RO                                    | GIẢM THIỂU                                          |
|-------------------------------------------|----------------------------------------------------|
| Hiệu suất giảm khi xử lý nhiều ghi chú    | Tối ưu hóa truy vấn SQLite và sử dụng index.       |
| Lỗi tương thích với bản cập nhật Windows  | Kiểm thử trên nhiều phiên bản Windows trước phát hành. |
| Thư viện mã hóa không ổn định             | Chọn thư viện mã hóa được cộng đồng hỗ trợ lâu dài. |
| Vượt ngân sách do yêu cầu bổ sung         | Giới hạn phạm vi tính năng theo danh sách ưu tiên. |

## NỖ LỰC ƯU TIÊN
| YÊU CẦU                         | MỨC ĐỘ ƯU TIÊN | NỖ LỰC DỰ KIẾN YÊU CẦU |
|---------------------------------|----------------|-------------------------|
| Chỉnh sửa và lưu văn bản        | Cao            | 2 tuần                  |
| Tìm kiếm và thay thế            | Cao            | 1,5 tuần                |
| Gắn thẻ                         | Trung bình     | 2 tuần                  |
| Tìm kiếm nâng cao               | Trung bình     | 2,5 tuần                |
| Xuất báo cáo                    | Thấp           | 2 tuần                  |

## LỊCH SỬ PHIÊN BẢN VÀ NHẬT KÝ THAY ĐỔI
| PHIÊN BẢN | NGƯỜI CHỈNH SỬ JulieA | NGÀY       | MÔ TẢ CHỈNH SỬA                   |
|-----------|-----------------------|------------|------------------------------------|
| 1.0       | Nguyễn Văn An         | 29/04/2025 | Bản nháp ban đầu của PRD.         |
| 1.1       | Nguyễn Văn An         | 01/05/2025 | Thêm chi tiết bên liên quan.      |
| 1.2       | Nguyễn Văn An         | 03/05/2025 | Bổ sung phân tích rủi ro và nỗ lực. |

## HỖ TRỢ THỊ GIÁC
- **Wireframe**: Giao diện gồm thanh menu (File, Edit, Search), khu vực nhập văn bản, và bảng điều khiển bên phải để quản lý thẻ và tìm kiếm.
- **Sơ đồ ERD**:
  - **Bảng**:
    - `Notes`: id, title, content, status, created_at, updated_at.
    - `Tags`: id, name.
    - `Note_Tags`: note_id, tag_id.
  - **Quan hệ**:
    - Một Note có thể có nhiều Tags (quan hệ nhiều-nhiều qua Note_Tags).
- **Sơ đồ luồng công việc**: Mô tả quy trình tạo ghi chú, gắn thẻ, tìm kiếm, và xuất báo cáo.
Beta
0 / 0
used queries
1
