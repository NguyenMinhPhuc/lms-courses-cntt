# 4. Kế hoạch Sprint

## 4.1. Tổng quan release 1.0

| Sprint | Tuần | Sprint Goal | Story | SP cam kết | SP kéo dài (Could) | MVP |
|---|---|---|---|---|---|---|
| Sprint 1 | 1–2 | Khách xem thực đơn, đăng ký, đăng nhập và có giỏ hàng chạy với API thật | 8 | 34 | 0 | ✔ |
| Sprint 2 | 3–4 | **MVP:** đặt món end-to-end, nhân viên nhận và xử lý đơn, khách theo dõi và hủy đơn | 10 | 36 | 0 | ✔ |
| Sprint 3 | 5–6 | Thông báo thời gian thực, tính năng thiết bị, tìm kiếm, yêu thích | 11 | 36 | 0 | |
| Sprint 4 | 7–8 | Vận hành căn tin và quản trị trên web, báo cáo, chọn quầy nhận | 10 | 31 | 0 | |
| Sprint 5 | 9–10 | Chất lượng và phát hành: kiểm thử, hiệu năng, triển khai server Khoa, APK | 13 | 20 | 16 | |
| **Tổng** | 10 tuần | | **52** | **157** | **16** | |

Các story Could-have của Sprint 5 là **mục tiêu kéo dài**: chỉ làm khi đã xong phần cam kết; không xong thì quay lại Product Backlog, không làm sprint thất bại.

## 4.2. Sprint 1 (tuần 1–2): Nền tảng và thực đơn

**Sprint Goal:** Một khách vãng lai mở ứng dụng trên Android, xem thực đơn và chi tiết món lấy từ API thật, đăng ký, đăng nhập và thêm món vào giỏ.

| ID | User Story (rút gọn) | Priority | SP |
|---|---|---|---|
| TS-01 | Khởi tạo repo, quy ước, AGENTS.md | Must-have | 5 |
| TS-02 | Script CSDL, thủ tục nền tảng, dữ liệu mẫu | Must-have | 5 |
| US-G01 | Xem thực đơn theo danh mục | Must-have | 5 |
| US-G03 | Xem chi tiết món | Must-have | 3 |
| US-G04 | Đăng ký tài khoản | Must-have | 5 |
| US-G05 | Đăng nhập | Must-have | 5 |
| US-C01 | Thêm món vào giỏ | Must-have | 3 |
| US-C02 | Sửa, xóa món trong giỏ, tổng tiền | Must-have | 3 |
| | **Tổng** | | **34** |

**Demo Sprint Review:** mở APK hoặc Expo Go → xem danh mục → chi tiết món hết hàng bị khóa nút → đăng ký → đăng nhập → thêm món, thấy badge và tổng tiền.

**Phụ thuộc:** TS-01, TS-02 làm trong 3 ngày đầu; các story còn lại dùng dữ liệu giả cho đến khi API sẵn sàng.

## 4.3. Sprint 2 (tuần 3–4): MVP đặt món và xử lý đơn

**Sprint Goal:** Khách đặt món thật, nhân viên thấy đơn, chuyển trạng thái đúng trình tự; khách xem trạng thái và hủy được đơn chưa chuẩn bị; không bao giờ bán quá số suất.

| ID | User Story (rút gọn) | Priority | SP |
|---|---|---|---|
| US-C14 | Giữ đăng nhập, làm mới token | Must-have | 3 |
| US-C13 | Hồ sơ, đăng xuất | Must-have | 2 |
| US-S01 | Giao diện và phân quyền nhân viên | Must-have | 3 |
| US-C04 | Đặt món có giao dịch | Must-have | 8 |
| US-SYS03 | Chặn đặt quá tồn kho khi đặt đồng thời | Must-have | 3 |
| US-C06 | Lịch sử đơn hàng | Must-have | 3 |
| US-C07 | Chi tiết và trạng thái đơn | Must-have | 3 |
| US-C08 | Hủy đơn khi pending | Must-have | 3 |
| US-S02a | Danh sách đơn cần xử lý | Must-have | 3 |
| US-S03 | Chuyển trạng thái đơn đúng trình tự | Must-have | 5 |
| | **Tổng** | | **36** |

**Demo Sprint Review (chấp nhận MVP):** hai điện thoại (khách, nhân viên) → khách đặt 2 món → nhân viên kéo tải lại thấy đơn → chuyển preparing → ready → completed → khách kéo tải lại thấy trạng thái → đặt món còn 1 suất từ hai máy, một máy nhận 409.

**Rủi ro chính:** US-C04 (8 SP) có giao dịch và khóa dòng; bắt đầu ngay ngày đầu sprint, viết kịch bản kiểm thử T-SQL song song.

## 4.4. Sprint 3 (tuần 5–6): Realtime và tính năng thiết bị

**Sprint Goal:** Khách nhận thông báo ngay khi đơn đổi trạng thái; nhân viên thấy đơn mới không cần tải lại; ứng dụng dùng camera, bản đồ và giữ giỏ hàng khi tắt.

| ID | User Story (rút gọn) | Priority | SP |
|---|---|---|---|
| US-SYS01 | Xác thực kết nối socket | Must-have | 3 |
| US-SYS02 | Lưu thông báo trước khi gửi | Must-have | 3 |
| US-C09 | Thông báo realtime trạng thái đơn | Must-have | 5 |
| US-C10 | Danh sách thông báo, badge chưa đọc | Must-have | 3 |
| US-S02b | Đơn mới tự xuất hiện, âm báo | Must-have | 3 |
| US-G02 | Tìm món không dấu | Must-have | 3 |
| US-C03 | Giữ giỏ hàng khi tắt ứng dụng | Should-have | 2 |
| US-C11 | Món yêu thích | Should-have | 3 |
| US-C12 | Đổi ảnh đại diện bằng camera/thư viện | Should-have | 5 |
| US-G06 | Bản đồ quầy | Should-have | 5 |
| US-G07 | Kéo để tải lại thực đơn | Should-have | 1 |
| | **Tổng** | | **36** |

**Demo Sprint Review:** nhân viên chuyển ready → điện thoại khách hiện thông báo trong vài giây, bấm vào mở đúng đơn → tắt ứng dụng khách, đổi trạng thái, mở lại thấy thông báo → chụp ảnh đại diện → bản đồ quầy.

## 4.5. Sprint 4 (tuần 7–8): Vận hành căn tin và quản trị

**Sprint Goal:** Căn tin tự quản lý thực đơn, số suất, tài khoản nhân viên và xem doanh thu trên web; khách chọn được quầy nhận.

| ID | User Story (rút gọn) | Priority | SP |
|---|---|---|---|
| US-A01 | Quản lý danh mục (web) | Must-have | 3 |
| US-A02 | Quản lý món, ảnh món (web) | Must-have | 5 |
| US-A04 | Quản lý tài khoản nhân viên (web) | Must-have | 5 |
| US-A05 | Báo cáo theo khoảng ngày (web) | Must-have | 3 |
| US-S04 | Bật/tắt món còn bán | Should-have | 2 |
| US-S05 | Cập nhật tồn kho | Should-have | 3 |
| US-S06 | Lọc đơn theo trạng thái | Should-have | 2 |
| US-S08 | Báo cáo nhanh cuối ca | Should-have | 3 |
| US-A03 | Quản lý quầy (web) | Should-have | 2 |
| US-C05 | Chọn quầy nhận khi đặt | Should-have | 3 |
| | **Tổng** | | **31** |

Sprint này có năng lực dư khoảng 3–5 SP: dùng để trả nợ kỹ thuật và sửa lỗi tồn từ Sprint 3, hoặc kéo sớm TS-03 (kiểm thử).

**Demo Sprint Review:** quản lý tạo món mới kèm ảnh trên web → món xuất hiện trên điện thoại → nhân viên tắt món → khách không đặt được → báo cáo doanh thu khớp số đơn đã demo.

## 4.6. Sprint 5 (tuần 9–10): Chất lượng và phát hành

**Sprint Goal:** Phát hành bản 1.0: hệ thống chạy trên server Khoa, APK cài được trên máy người ngoài nhóm, có bộ test tự động cho mọi story Must.

| ID | User Story (rút gọn) | Priority | SP |
|---|---|---|---|
| TS-03 | Bộ test tự động cho story Must | Must-have | 5 |
| US-SYS04 | Triển khai server Khoa, health check | Must-have | 5 |
| TS-05 | Build APK, EAS Update | Must-have | 3 |
| TS-04 | Hiệu năng và accessibility | Should-have | 3 |
| US-SYS05 | Log lỗi backend | Should-have | 2 |
| TS-06 | Hồ sơ phát hành | Should-have | 2 |
| | **Tổng cam kết** | | **20** |
| US-C15 | Quầy gần tôi (kéo dài) | Could-have | 3 |
| US-C17 | Đánh giá món (kéo dài) | Could-have | 5 |
| US-C16 | Đặt lại đơn cũ (kéo dài) | Could-have | 2 |
| US-S07 | Nhân viên hủy kèm lý do (kéo dài) | Could-have | 2 |
| US-A06 | Thống kê trạng thái đơn (kéo dài) | Could-have | 2 |
| US-C18 | Bật/tắt thông báo (kéo dài) | Could-have | 1 |
| US-A07 | Tình trạng hệ thống (kéo dài) | Could-have | 1 |
| | **Tổng kéo dài** | | **16** |

Cam kết thấp hơn velocity có chủ đích: triển khai trên server Khoa phụ thuộc bộ phận hỗ trợ và lượt build EAS miễn phí có giới hạn, nên cần thời gian dự phòng.

**Demo Sprint Review (Release 1.0):** cài APK trên máy người ngoài nhóm → chạy kịch bản nghiệm thu mọi story Must với backend trên server Khoa → `npm test` xanh → `/health` ok.

## 4.7. Release burndown dự kiến

| Thời điểm | SP còn lại (Must + Should + Could) | SP hoàn thành lũy kế | Mốc |
|---|---|---|---|
| Bắt đầu | 173 | 0 | |
| Hết Sprint 1 | 139 | 34 | |
| Hết Sprint 2 | 103 | 70 | MVP |
| Hết Sprint 3 | 67 | 106 | |
| Hết Sprint 4 | 36 | 137 | Đủ tính năng Must/Should |
| Hết Sprint 5 | 0 – 16 | 157 – 173 | Release 1.0 (tùy phần kéo dài) |

Scrum Master cập nhật bảng này với số thực tế sau mỗi Sprint Review. Nếu SP hoàn thành thấp hơn kế hoạch hai sprint liên tiếp, Product Owner chuyển story Should-have có SP lớn (US-C12, US-G06) sang release sau, giữ nguyên mọi story Must.

# 5. Quản lý rủi ro

| Mã | Rủi ro | Khả năng | Ảnh hưởng | Biện pháp | Story liên quan |
|---|---|---|---|---|---|
| R1 | Giao dịch đặt món sai khi nhiều người đặt cùng lúc | Trung bình | Cao | Khóa dòng UPDLOCK/HOLDLOCK, kịch bản kiểm thử hai phiên, review kỹ mã AI sinh | US-C04, US-SYS03 |
| R2 | Server Khoa hoặc mạng không sẵn sàng đúng lúc triển khai | Trung bình | Cao | Liên hệ bộ phận hỗ trợ từ Sprint 4, có video demo dự phòng | US-SYS04 |
| R3 | Hết lượt build EAS miễn phí | Trung bình | Trung bình | Kiểm thử bằng Expo Go trước, dùng EAS Update cho sửa lỗi JavaScript | TS-05 |
| R4 | Mã do AI sinh chạy được nhưng sai hoặc không an toàn | Cao | Cao | Quy tắc "không hiểu thì không merge", review bảo mật, mutation test | Mọi story |
| R5 | Bản đồ trắng trên bản APK (thiếu API key) | Trung bình | Thấp | Cấu hình Google Maps API key ngay khi làm US-G06 | US-G06 |
| R6 | Velocity thực tế thấp hơn 30 SP | Trung bình | Trung bình | Đo sau Sprint 1, cắt Should-have theo mục 4.7 | Toàn release |

# 6. Truy vết SRS → Backlog

| Module SRS | Epic | User story SRS được đưa vào backlog |
|---|---|---|
| M01 Xác thực và tài khoản | E1 | US-G04, US-G05, US-C13, US-C14, US-S01 |
| M02 Thực đơn | E2 | US-G01, US-G02, US-G03, US-G07 |
| M03 Giỏ hàng | E3 | US-C01, US-C02, US-C03 |
| M04 Đơn hàng | E3, E4 | US-C04, US-C06, US-C07, US-C08, US-C16, US-SYS03 |
| M05 Yêu thích | E7 | US-C11 |
| M06 Quầy, vị trí, bản đồ | E6 | US-G06, US-C05, US-C15 |
| M07 Hồ sơ và tệp ảnh | E1, E7 | US-C12, US-C17 |
| M08 Thông báo | E5 | US-C09, US-C10, US-C18, US-S02b, US-SYS01, US-SYS02 |
| M09 Vận hành nhân viên | E4, E8 | US-S02a, US-S03, US-S04, US-S05, US-S06, US-S07 |
| M10 Báo cáo | E8 | US-S08, US-A05, US-A06 |
| M11 Quản trị (web) | E9 | US-A01, US-A02, US-A03, US-A04, US-A07 |
| M12 Hạ tầng và chất lượng | E10 | US-SYS04, US-SYS05, TS-01 … TS-06 |
| Ngoài phạm vi (SRS 1.2, 10.3) | E11, E12, E1, E3, E5 | W-01 … W-06 |

Toàn bộ 45 user story của SRS có trong backlog (US-S02 được tách thành US-S02a và US-S02b), cộng 6 technical story và 6 hạng mục Won't-have.
