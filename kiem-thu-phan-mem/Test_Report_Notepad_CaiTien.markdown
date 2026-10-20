# Báo Cáo Kiểm Thử

## 1. Thông tin chung
- **Tên dự án**: Notepad Cải Tiến Hỗ Trợ Testing Manual
- **Phiên bản ứng dụng**: 1.0
- **Ngày bắt đầu kiểm thử**: 05/05/2025
- **Ngày kết thúc kiểm thử**: 12/05/2025
- **Người lập báo cáo**: Nguyễn Thị Hoa (Chuyên viên QA)
- **Người phê duyệt**: Trần Thị Bình (Quản lý kiểm thử)
- **Ngày báo cáo**: 13/05/2025

## 2. Mục tiêu kiểm thử
- Đảm bảo ứng dụng đáp ứng các yêu cầu chức năng và phi chức năng trong PRD.
- Xác minh các tính năng chính: chỉnh sửa văn bản, tìm kiếm nâng cao, xuất báo cáo.
- Đạt tỷ lệ bao phủ kiểm thử ít nhất 95% và không có lỗi nghiêm trọng trước khi phát hành.

## 3. Tóm tắt kết quả kiểm thử

### 3.1 Tổng quan
- **Tổng số test case**: 14
- **Test case thực thi**: 14
- **Test case passed**: 12
- **Test case failed**: 2
- **Tỷ lệ pass**: 85.7%
- **Tỷ lệ bao phủ yêu cầu**: 95% (tất cả yêu cầu chức năng và phi chức năng chính được kiểm tra)

### 3.2 Trạng thái test case
| TC ID | Mô tả | Kết quả | Ghi chú |
|-------|-------|---------|---------|
| TC-001 | Kiểm tra tạo và chỉnh sửa ghi chú văn bản | Passed | Auto-save hoạt động đúng |
| TC-002 | Kiểm tra lưu ghi chú dưới dạng .txt | Passed | File lưu đúng định dạng |
| TC-003 | Kiểm tra mở file .txt hiện có | Passed | Hỗ trợ file lên đến 10MB |
| TC-004 | Kiểm tra thông báo lỗi khi lưu file thất bại | Passed | Thông báo lỗi rõ ràng |
| TC-005 | Kiểm tra ghi chú được mã hóa bằng AES-256 | Passed | Nội dung mã hóa đúng chuẩn AES-256 |
| TC-006 | Kiểm tra tìm kiếm ghi chú theo thẻ | Passed | Kết quả tìm kiếm chính xác |
| TC-007 | Kiểm tra tìm kiếm ghi chú theo từ khóa | Passed | Phân biệt hoa thường hoạt động |
| TC-008 | Kiểm tra lọc ghi chú theo trạng thái | Passed | Bộ lọc trạng thái hoạt động đúng |
| TC-009 | Kiểm tra lọc ghi chú theo ngày tạo | Failed | Lọc theo ngày không hiển thị đúng với múi giờ khác |
| TC-010 | Kiểm tra hiệu suất tìm kiếm với 10,000 ghi chú | Passed | Thời gian tìm kiếm: 0.45 giây |
| TC-011 | Kiểm tra xuất ghi chú sang file CSV | Passed | File CSV chứa đầy đủ thông tin |
| TC-012 | Kiểm tra xuất ghi chú sang file TXT | Passed | File TXT định dạng đúng |
| TC-013 | Kiểm tra thông báo lỗi khi xuất báo cáo thất bại | Passed | Thông báo lỗi rõ ràng |
| TC-014 | Kiểm tra hiệu suất xuất báo cáo với 1,000 ghi chú | Failed | Thời gian xuất: 6 giây (vượt yêu cầu < 5 giây) |

## 4. Phân tích lỗi

### 4.1 Tổng quan lỗi
- **Tổng số lỗi phát hiện**: 5
- **Phân loại lỗi**:
  - **Nghiêm trọng (Critical)**: 0
  - **Cao (High)**: 1
  - **Trung bình (Medium)**: 2
  - **Thấp (Low)**: 2
- **Trạng thái lỗi**:
  - Đã sửa: 3
  - Chưa sửa: 2 (được lên lịch sửa trong bản phát hành tiếp theo)

### 4.2 Chi tiết lỗi
| ID lỗi | Mô tả | Mức độ | Test Case liên quan | Trạng thái | Ghi chú |
|--------|-------|--------|---------------------|------------|---------|
| BUG-001 | Lọc ghi chú theo ngày tạo không đúng với múi giờ khác | Cao | TC-009 | Chưa sửa | Cần cập nhật logic xử lý múi giờ |
| BUG-002 | Thời gian xuất 1,000 ghi chú vượt quá 5 giây | Trung bình | TC-014 | Chưa sửa | Cần tối ưu hóa truy vấn SQLite |
| BUG-003 | Thông báo lỗi khi lưu file không hiển thị tiếng Việt đầy đủ | Trung bình | TC-004 | Đã sửa | Cập nhật font Unicode |
| BUG-004 | Giao diện bảng tìm kiếm bị lệch trên màn hình nhỏ | Thấp | TC-006, TC-007 | Đã sửa | Điều chỉnh CSS |
| BUG-005 | Phím tắt Ctrl+F không hoạt động khi bảng tìm kiếm mở | Thấp | TC-006 | Đã sửa | Sửa xung đột phím tắt |

## 5. Ma Trận Truy Xuất Yêu Cầu (Requirement Traceability Matrix)

Ma trận dưới đây xác nhận rằng các yêu cầu trong PRD đã được kiểm thử thông qua các test case.

| Yêu cầu PRD | Mô tả yêu cầu | Loại yêu cầu | TR ID | TC ID | Trạng thái kiểm thử |
|-------------|---------------|--------------|-------|-------|---------------------|
| Yêu cầu chức năng 1 | Tạo, chỉnh sửa, lưu ghi chú .txt | Chức năng | TR-001, TR-002 | TC-001, TC-002 | Passed |
| Yêu cầu chức năng 1 | Mở file .txt hiện có | Chức năng | TR-003 | TC-003 | Passed |
| Yêu cầu chức năng 1 | Thông báo lỗi khi lưu/mở thất bại | Chức năng | TR-004 | TC-004 | Passed |
| Yêu cầu chức năng 4 | Tìm kiếm ghi chú theo từ khóa/thẻ | Chức năng | TR-010 | TC-006, TC-007, TC-010 | Passed |
| Yêu cầu chức năng 4 | Lọc ghi chú theo ngày/trạng thái | Chức năng | TR-011 | TC-008, TC-009 | Failed (TC-009) |
| Yêu cầu chức năng 5 | Xuất ghi chú thành CSV/TXT | Chức năng | TR-012 | TC-011, TC-012, TC-014 | Failed (TC-014) |
| Yêu cầu chức năng 5 | Thông báo lỗi khi xuất thất bại | Chức năng | TR-013 | TC-013 | Passed |
| Yêu cầu phi chức năng 1 | Khởi động dưới 1 giây | Phi chức năng | TR-014 | TC-001 (gián tiếp) | Passed |
| Yêu cầu phi chức năng 2 | Giao diện tuân thủ Windows, hỗ trợ phím tắt | Phi chức năng | - | TC-001, TC-006 | Passed |
| Yêu cầu phi chức năng 3 | Ghi chú mã hóa AES-256 | Phi chức năng | TR-015 | TC-005 | Passed |
| Yêu cầu phi chức năng 4 | Tương thích Windows 10/11 | Phi chức năng | TR-016 | TC-001 đến TC-014 | Passed |

## 6. Đánh giá và khuyến nghị

### 6.1 Đánh giá
- Ứng dụng đáp ứng 95% yêu cầu trong PRD, với 12/14 test case passed.
- Các tính năng chính (chỉnh sửa văn bản, tìm kiếm nâng cao, xuất báo cáo) hoạt động tốt, nhưng có hai vấn đề cần khắc phục:
  - Lọc ghi chú theo ngày (TC-009) gặp lỗi múi giờ.
  - Hiệu suất xuất báo cáo (TC-014) chưa đạt yêu cầu (< 5 giây).
- Không có lỗi nghiêm trọng, nhưng lỗi mức cao (BUG-001) cần được ưu tiên sửa trước khi phát hành.

### 6.2 Khuyến nghị
- **Trước phát hành**:
  - Sửa lỗi BUG-001 (lọc ngày theo múi giờ) và BUG-002 (tối ưu xuất báo cáo).
  - Chạy lại test case TC-009 và TC-014 để xác nhận sửa lỗi.
- **Cho bản cập nhật sau**:
  - Tối ưu giao diện cho màn hình nhỏ (liên quan BUG-004 đã sửa nhưng cần kiểm tra thêm).
  - Thêm kiểm thử tự động cho tìm kiếm nâng cao (TC-006, TC-007) bằng công cụ như Selenium.
- **Cải thiện quy trình**:
  - Tăng cường kiểm thử hiệu suất với dữ liệu lớn hơn (ví dụ: 50,000 ghi chú).
  - Cập nhật tài liệu kiểm thử để bao gồm các trường hợp biên (boundary cases) cho xuất báo cáo.

## 7. Phê duyệt
- **Người chuẩn bị**: Nguyễn Thị Hoa (Chuyên viên QA)
- **Người phê duyệt**: Trần Thị Bình (Quản lý kiểm thử)
- **Ngày phê duyệt**: 13/05/2025