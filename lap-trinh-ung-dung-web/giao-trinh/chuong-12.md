# Chương 12. Demo Day chung và nộp báo cáo đồ án

## Mục tiêu chương

Sau khi học xong chương này, bạn có thể:

- Chuẩn bị và trình bày phần web của đồ án trong Demo Day chung với học phần di động.
- Xây dựng kịch bản demo xuyên suốt web và ứng dụng di động trên cùng backend, có cả trường hợp lỗi.
- Đối chiếu báo cáo đồ án với từng tiêu chí của rubric trước khi nộp.
- Chuẩn bị cho phần bảo vệ kỹ thuật: giải thích được mã do chính mình commit.
- Đánh giá sản phẩm của nhóm khác theo rubric và nhìn lại quá trình học.

## 12.1. Demo Day chung

### 12.1.1. Một hệ thống, hai học phần

Buổi 12 gộp với Demo Day của học phần Lập trình ứng dụng di động. Hội đồng thấy toàn bộ hệ thống LHU Food chạy thật: khách đặt món trên điện thoại, nhân viên xử lý trên màn hình quầy, quản lý xem báo cáo trên web, tất cả qua một backend triển khai trên server Khoa. Phần web của mỗi nhóm gồm 10 phút trình bày và 5 phút hỏi đáp; lịch ghép phần web với phần di động do giảng viên công bố. **Mỗi thành viên đều phải trình bày** phần mình phụ trách.

### 12.1.2. Cấu trúc phần trình bày web

| Thời lượng | Nội dung | Minh chứng cho tiêu chí rubric |
|---|---|---|
| 1 phút | Phạm vi web của nhóm, địa chỉ web trên server Khoa | 1.1 |
| 5 phút | Demo theo kịch bản, trên bản đã triển khai | 1.8 |
| 3 phút | Bảo vệ thiết kế: sơ đồ chức năng, ma trận phân quyền, sơ đồ tuần tự, ma trận truy vết kiểm thử | 1.2–1.7, 2.2 |
| 1 phút | Kế hoạch so với thực tế: velocity, burndown, một bài học | 4.1–4.3 |
| 5 phút | Hỏi đáp và bảo vệ kỹ thuật | 1.9 |

### 12.1.3. Kịch bản demo xuyên suốt

Demo kể **một câu chuyện**, không liệt kê từng trang:

1. Quản lý đăng nhập web, thêm một món mới kèm ảnh (US-A02); món hiện ngay trên thực đơn web và app.
2. Khách đặt món trên app di động; màn hình quầy trên web nhận đơn kèm âm báo mà không tải lại trang (US-S02).
3. Hai nhân viên mở màn hình quầy trên hai máy; một người chuyển trạng thái, máy kia và điện thoại khách cập nhật ngay (US-S03).
4. Quản lý mở báo cáo: doanh thu và món bán chạy thay đổi theo đơn vừa hoàn tất (US-A05).
5. **Trường hợp lỗi:** đặt quá tồn kho (409); tài khoản customer gõ `/admin/orders` (403); xóa danh mục còn món (409).

Phần trường hợp lỗi thường bị bỏ qua, nhưng chính nó chứng minh phân tích (ma trận phân quyền, quy tắc nghiệp vụ) và kiểm thử của nhóm có thực chất.

### 12.1.4. Chuẩn bị và dự phòng

- Dữ liệu demo thật và có nghĩa (tên món, giá, ảnh), không dùng "test1", "aaa".
- Trước buổi: mở `/api/health` của web và Swagger của backend từ máy lớp học; đăng nhập sẵn tài khoản quản lý và hai tài khoản nhân viên trên hai máy; bật âm báo; cài app bản build mới nhất trên thiết bị demo.
- Sơ đồ trên slide phải đọc được trên máy chiếu: chữ đủ lớn, không chụp màn hình mờ.
- **Phương án dự phòng:** video quay sẵn toàn bộ kịch bản trên bản đã triển khai, kèm ảnh danh sách kiểm tra sau triển khai có ngày giờ; máy thứ hai đã đăng nhập sẵn; kiểm tra server và mạng 30 phút trước buổi.

## 12.2. Đối chiếu báo cáo đồ án với rubric

### 12.2.1. Rubric 27 tiêu chí

Điểm cuối kỳ chấm bằng rubric 27 tiêu chí, tách theo 4 CLO (CLO1 4 điểm, CLO2, CLO3, CLO4 mỗi CLO 2 điểm). Mỗi tiêu chí chỉ chấm một vấn đề, có gợi ý chấm và minh chứng cần có. Báo cáo đồ án (Report) là minh chứng chính; phần trình bày và bảo vệ kỹ thuật bổ sung minh chứng cho tiêu chí cá nhân.

### 12.2.2. Tự đối chiếu trước khi nộp

Với mỗi tiêu chí, nhóm phải chỉ ra được **minh chứng nằm ở đâu** trong báo cáo:

| CLO (điểm) | Tiêu chí | Minh chứng cần có |
|---|---|---|
| CLO1 (4) | 1.1–1.8 (nhóm), 1.9 (cá nhân) | Chương 2–3: phạm vi, sơ đồ chức năng, sitemap, bảng route, ranh giới Server/Client, module quản trị, ma trận phân quyền, sơ đồ tuần tự; Chương 6: sản phẩm triển khai khớp phân tích; phần trả lời khi bảo vệ |
| CLO2 (2) | 2.1–2.6 | Chương 5: kế hoạch, ma trận truy vết, kết quả Vitest/Playwright, bảng đột biến, lỗi và khắc phục, Lighthouse và accessibility |
| CLO3 (2) | 3.1–3.6 | Cả báo cáo: đủ cấu trúc, định dạng đúng quy định, hình và bảng có số và chú thích, trích dẫn IEEE, văn phong rõ ràng |
| CLO4 (2) | 4.1–4.3 (nhóm), 4.4–4.6 (cá nhân) | Chương 7: backlog, kế hoạch sprint, phân công, velocity, burndown; board; báo cáo vai trò cá nhân |

Một CLO được coi là đạt khi điểm CLO đạt từ 50% trọng số trở lên (CLO1 ≥ 2; CLO2, CLO3, CLO4 ≥ 1). Một tiêu chí không có minh chứng thì không được điểm, dù sản phẩm chạy tốt. Lỗi hay gặp: sản phẩm có ma trận phân quyền nhưng báo cáo không đưa vào; test chạy được nhưng báo cáo không có ảnh kết quả; burndown vẽ theo trí nhớ không khớp board.

## 12.3. Bảo vệ kỹ thuật

### 12.3.1. Hình thức

Giảng viên mở repo, chọn ngẫu nhiên một đoạn mã và mời **thành viên đã commit đoạn đó** giải thích. Lịch sử commit cho biết ai viết dòng nào, nên mỗi thành viên phải hiểu phần mình làm, kể cả phần có dùng AI.

### 12.3.2. Câu hỏi thường gặp ở phần web

- Component này là Server hay Client Component? Vì sao? Nếu bỏ `"use client"` thì sao? (Chương 3–4)
- Token được lưu ở đâu, gửi lên API thế nào, hết hạn thì web làm gì? (Chương 5)
- Vì sao không chỉ dùng `proxy.ts` để phân quyền? Trang này còn kiểm tra quyền ở đâu nữa? (Chương 5)
- `revalidatePath` ở dòng này làm gì? Nếu xóa đi, người dùng thấy gì? (Chương 6)
- Vì sao Next.js không kết nối SQL Server trực tiếp? Quy tắc nghiệp vụ này nằm ở thủ tục nào? (Chương 1, 7)
- Màn hình quầy mất mạng một phút rồi có lại, đơn lỡ được bù thế nào? (Chương 9)
- Test này bắt được lỗi gì? Nếu sửa dòng X thì test có chuyển sang đỏ không? (Chương 10)
- Đoạn này do AI sinh ra phải không? Bạn đã kiểm tra và sửa gì?

Nguyên tắc cả học phần: **không hiểu thì không merge**. Trả lời được là minh chứng cho tiêu chí 1.9; không giải thích được đoạn mã của chính mình ảnh hưởng điểm cá nhân theo quy định ở trang Đánh giá học phần.

## 12.4. Sản phẩm nộp cuối kỳ

- Báo cáo đồ án (Word và PDF) theo cấu trúc và quy định định dạng ở trang Đánh giá học phần.
- Báo cáo kiểm thử (Chương 5 của báo cáo hoặc tài liệu riêng kèm báo cáo HTML của Playwright).
- Link web đã triển khai trên server Khoa; link repo GitHub của web và của backend; README triển khai.
- Link board công việc và các báo cáo sprint 1–3.
- Báo cáo vai trò cá nhân của từng thành viên (nộp riêng): việc đã làm, Pull Request tiêu biểu, khó khăn, cách sắp xếp công việc của bản thân.

## 12.5. Review chéo và nhìn lại học phần

### 12.5.1. Review chéo

Mỗi nhóm được phân công đánh giá một số nhóm khác theo rubric (thang 10, tách 4 CLO), dựa trên phần trình bày và báo cáo. Mỗi điểm số kèm một nhận xét cụ thể: một điểm mạnh và một đề xuất cải tiến. Review chéo rèn kỹ năng đọc sản phẩm của người khác theo tiêu chí, kỹ năng cần thiết khi review Pull Request trong công việc thật [2]. Điểm review chéo là ý kiến tham khảo cho giảng viên và được tính vào phần tham gia review ở điểm quá trình.

### 12.5.2. Nhìn lại bốn chuẩn đầu ra

| CLO | Bạn đã làm được |
|---|---|
| CLO1 | Phân tích phạm vi, sitemap, bảng ánh xạ, ranh giới Server/Client, ma trận phân quyền, module quản trị, luồng realtime trước khi viết mã |
| CLO2 | Viết test case từ tiêu chí chấp nhận, giá trị biên, truy cập trái phép, luồng nghiệp vụ, kiểm thử tự động có kiểm chứng bằng đột biến |
| CLO3 | Bốn báo cáo sprint và một báo cáo đồ án đúng quy định, có minh chứng |
| CLO4 | Lập kế hoạch sprint, theo dõi trên board, điều chỉnh theo velocity, tổng kết tiến độ theo khung Scrum [1] |

### 12.5.3. Đi tiếp sau học phần

- Đưa dự án vào hồ sơ năng lực (portfolio): README rõ ràng, ảnh giao diện, link demo, vai trò của bạn.
- Các chủ đề nên học thêm: TypeScript nâng cao, kiểm thử tự động trên CI (GitHub Actions), giám sát ứng dụng, thiết kế hệ thống.
- Thói quen nên giữ: phân tích trước khi code, mỗi thay đổi có test, mỗi đoạn mã AI sinh đều được đọc và hiểu trước khi merge.

## Tóm tắt chương

- Demo Day chung trình diễn một hệ thống LHU Food chạy thật; phần web 10 phút trình bày, 5 phút hỏi đáp; mọi thành viên trình bày.
- Kịch bản demo là một câu chuyện xuyên suốt web và app, có trường hợp lỗi; luôn có phương án dự phòng.
- Đối chiếu báo cáo với 27 tiêu chí rubric; tiêu chí không có minh chứng không được điểm.
- Bảo vệ kỹ thuật: người commit giải thích mã; không hiểu thì không merge.
- Review chéo theo rubric và nhìn lại bốn chuẩn đầu ra.

## Câu hỏi ôn tập

1. Vì sao kịch bản demo nên có trường hợp lỗi?
2. Phần nào của báo cáo là minh chứng cho tiêu chí 1.6 (phân tích phân quyền và bảo mật)?
3. Một CLO được coi là đạt khi nào?
4. Chuẩn bị gì để trả lời câu hỏi "đoạn này do AI sinh ra phải không"?
5. Phương án dự phòng khi server Khoa gặp sự cố ngay trước giờ demo là gì?
6. Review chéo rèn luyện kỹ năng gì có ích cho công việc sau này?

## Bài tập

1. **Tự đối chiếu rubric.** Lập bảng 27 tiêu chí, ghi vị trí minh chứng trong báo cáo (chương, mục, số hình/bảng) cho từng tiêu chí.
2. **Kịch bản demo.** Viết kịch bản demo của nhóm theo mục 12.1.3, ghi rõ ai thao tác, trên thiết bị nào, nói gì.
3. **Báo cáo vai trò cá nhân.** Viết báo cáo vai trò của bạn: việc đã làm, ba Pull Request tiêu biểu, một khó khăn và cách vượt qua, cách bạn sắp xếp công việc qua bốn sprint.

## Tài liệu tham khảo

[1] K. Schwaber and J. Sutherland, “The Scrum Guide,” Nov. 2020. Accessed: Oct. 30, 2026. [Online]. Available: https://scrumguides.org/scrum-guide.html

[2] GitHub, “About pull request reviews,” *GitHub Docs*. Accessed: Oct. 30, 2026. [Online]. Available: https://docs.github.com/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews
