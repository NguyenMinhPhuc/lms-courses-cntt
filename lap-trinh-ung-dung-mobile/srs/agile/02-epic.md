# 2. Danh sách Epic

Các chức năng trong SRS (mục 4 và 5) được gom thành 12 Epic. Epic E11, E12 là hạng mục **Won't-have** của release 1.0 (SRS mục 1.2 đặt ngoài phạm vi), giữ trong backlog cho Release 2.

| ID | Epic | Mô tả | Module SRS | Ưu tiên | Tổng SP | Sprint |
|---|---|---|---|---|---|---|
| E1 | Quản lý tài khoản & phân quyền | Đăng ký, đăng nhập, giữ phiên, hồ sơ, ảnh đại diện, giao diện theo vai trò | M01, M07 | Must-have | 23 | 1–3 |
| E2 | Thực đơn & tìm kiếm | Danh mục, danh sách món, tìm kiếm không dấu, chi tiết món | M02 | Must-have | 12 | 1, 3 |
| E3 | Giỏ hàng & đặt món | Giỏ hàng, đặt món có giao dịch, chặn đặt quá tồn kho, đặt lại đơn | M03, M04 | Must-have | 21 | 1–3, 5 |
| E4 | Quản lý đơn hàng | Lịch sử, chi tiết, hủy đơn của khách; nhận và xử lý đơn của nhân viên | M04, M09 | Must-have | 21 | 2, 4, 5 |
| E5 | Thông báo thời gian thực | Socket.IO có xác thực, lưu thông báo, thông báo trạng thái đơn, badge | M08 | Must-have | 18 | 3, 5 |
| E6 | Quầy, vị trí & bản đồ | Bản đồ quầy, chọn quầy nhận, quầy gần nhất | M06 | Should-have | 11 | 3–5 |
| E7 | Yêu thích & đánh giá | Món yêu thích, đánh giá món đã nhận | M05, F07.4 | Should-have | 8 | 3, 5 |
| E8 | Vận hành căn tin & báo cáo | Bật/tắt món, tồn kho, báo cáo doanh thu, món bán chạy | M09, M10 | Should-have | 13 | 4, 5 |
| E9 | Quản trị hệ thống (web) | Quản lý danh mục, món, quầy, tài khoản nhân viên, tình trạng hệ thống | M11 | Must-have | 16 | 4, 5 |
| E10 | Hạ tầng, chất lượng & phát hành | Khởi tạo dự án, CSDL, kiểm thử, hiệu năng, triển khai server Khoa, build APK | M12 | Must-have | 30 | 1, 5 |
| E11 | Thanh toán | Thanh toán trực tuyến, hóa đơn điện tử | Ngoài phạm vi (SRS 1.2) | Won't-have | (18) | Release 2 |
| E12 | Giao hàng | Giao món tận nơi trong khuôn viên trường | Ngoài phạm vi (SRS 1.2) | Won't-have | (13) | Release 2 |

**Tổng release 1.0:** 173 story point trên 5 sprint (Won't-have không tính).
