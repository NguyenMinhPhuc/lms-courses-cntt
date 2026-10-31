# Lời nói đầu

Giáo trình *Nhập môn lập trình – Tư duy giải quyết vấn đề với Python* được biên soạn cho học phần Nhập môn lập trình (mã 111155, 3 tín chỉ: 1 lý thuyết, 2 thực hành) của Khoa Công nghệ Thông tin, Trường Đại học Lạc Hồng. Người học là sinh viên năm thứ nhất ngành Công nghệ Thông tin, học kỳ 1. Giáo trình không đòi hỏi kiến thức lập trình trước; người học chỉ cần biết sử dụng máy tính ở mức cơ bản: cài phần mềm, quản lý thư mục, gõ văn bản.

Mục tiêu của giáo trình không phải là liệt kê hết các tính năng của Python. Giáo trình rèn cho người học một thói quen: **phân tích bài toán trước khi viết mã**. Với mỗi bài toán, người học xác định dữ liệu vào, cách xử lý và kết quả ra (bảng Input – Process – Output), mô tả thuật toán bằng lưu đồ, rồi mới hiện thực bằng Python và kiểm thử với nhiều bộ dữ liệu, kể cả dữ liệu sai và giá trị biên. Python được chọn vì cú pháp gọn, gần với ngôn ngữ tự nhiên, để người học tập trung vào tư duy thay vì vật lộn với cú pháp.

Giáo trình cũng hướng dẫn cách học lập trình khi trợ lý AI (ChatGPT, Claude, Gemini…) đã trở nên phổ biến. Người học dùng AI như một **trợ giảng**: hỏi để hiểu một câu lệnh, nhờ giải thích một thông báo lỗi, xin gợi ý hướng làm. Người học không dùng AI để viết hộ chương trình rồi nộp. Mọi dòng mã nộp phải do người học tự gõ, chạy thử và giải thích được.

Nội dung kỹ thuật được đối chiếu với tài liệu chính thức của Python (The Python Tutorial, The Python Language Reference, PEP 8) và các công cụ dùng trong học phần. Các ví dụ được viết và chạy thử trên Python 3.10 trở lên.

Căn cứ biên soạn: đề cương học phần Nhập môn lập trình (111155); Thông tư số 62/2026/TT-BGDĐT của Bộ Giáo dục và Đào tạo quy định việc biên soạn, thẩm định, phê duyệt và sử dụng giáo trình.

## Cách trích dẫn giáo trình

N. M. Phúc, *Giáo trình Nhập môn lập trình – Tư duy giải quyết vấn đề với Python*, Bản thảo lưu hành nội bộ. Đồng Nai, Việt Nam: Khoa Công nghệ Thông tin, Trường Đại học Lạc Hồng, 2026.

Khi trích dẫn một quy định của ngôn ngữ (cú pháp, hàm có sẵn, thứ tự ưu tiên toán tử), nên dẫn tài liệu chính thức ghi ở cuối chương tương ứng, vì tài liệu gốc được cập nhật theo từng phiên bản Python.

## Cách tổ chức giáo trình

Giáo trình gồm 10 chương, đi theo trình tự các buổi học của học phần. Hai buổi đánh giá (kiểm tra giữa kỳ và báo cáo đồ án cuối kỳ) không có chương riêng; quy định đánh giá nằm trong đề cương học phần.

| Chương | Nội dung chính | Buổi học |
|---|---|:-:|
| 1. Chương trình, Python và tư duy Input – Process – Output | Cài đặt môi trường, bảng IPO, biến, kiểu dữ liệu, nhập xuất, học cùng AI | 01 |
| 2. Toán tử và biểu thức | Toán tử số học, so sánh, logic; thứ tự ưu tiên; làm tròn và sai số số thực | 02 |
| 3. Cấu trúc rẽ nhánh và lưu đồ thuật toán | Lưu đồ, `if – elif – else`, giá trị biên, rẽ nhánh lồng | 03 |
| 4. Vòng lặp for, chuỗi và list | `for`, `range()`, mẫu tích lũy, chuỗi, list | 04 |
| 5. Vòng lặp while và chương trình có menu | `while`, lặp nhập đến khi hợp lệ, `break`, `continue`, menu | 05 |
| 6. Lỗi, ngoại lệ và gỡ lỗi | Ba loại lỗi, Traceback, `try – except`, debugger | 06 |
| 7. Hàm và module | `def`, tham số, `return`, phân rã, module | 08 |
| 8. Tổ chức mã nguồn và chuẩn PEP 8 | Phạm vi biến, PEP 8, Ruff, docstring, refactor | 09 |
| 9. Phân tích và thiết kế một dự án nhỏ theo nhóm | Phạm vi đề tài, IPO, sơ đồ phân rã, lưu đồ, phân công | 10 |
| 10. Hoàn thiện, kiểm thử, quản lý mã nguồn và trình bày sản phẩm | Kiểm thử tích hợp, GitHub, README, trình bày | 11 |

Mỗi chương gồm:

- **Mục tiêu chương:** những gì người học làm được sau khi học xong.
- **Nội dung lý thuyết:** giải thích khái niệm và lý do, kèm ví dụ đã chạy thử. Mỗi ví dụ có đầu vào và kết quả mong đợi để người học tự đối chiếu.
- **Tóm tắt, câu hỏi ôn tập và bài tập:** dùng để tự kiểm tra trước buổi học sau.
- **Bài tập hướng dẫn theo dự án Student Dashboard:** từng bước hoàn thiện một chương trình quản lý hồ sơ và điểm của sinh viên, mỗi chương thêm một chức năng.
- **Tài liệu tham khảo:** theo chuẩn IEEE, đánh số lại từ [1] trong mỗi chương.

## Dự án xuyên suốt: Student Dashboard

Student Dashboard là chương trình dòng lệnh mà người học tự xây dựng qua 8 chương đầu:

| Phiên bản | Chương | Chức năng thêm vào |
|:-:|:-:|---|
| v1 | 1 | In thẻ hồ sơ cá nhân từ dữ liệu nhập |
| v2 | 2 | Tính điểm học phần theo trọng số |
| v3 | 3 | Kiểm tra điểm hợp lệ, xếp loại học lực |
| v4 | 4 | Nhập điểm nhiều học phần, thống kê |
| v5 | 5 | Menu dòng lệnh |
| v6 | 6 | Nhập liệu an toàn, không dừng khi nhập sai |
| v8 | 7 | Viết lại bằng hàm, tách thành ba module |
| v9 | 8 | Chuẩn hóa theo PEP 8, kiểm tra bằng Ruff |

Phiên bản v7 không có vì buổi 07 là buổi kiểm tra giữa kỳ; số phiên bản được giữ theo số buổi học để khớp với bài giảng trên LMS. Chương 9 và 10 chuyển sang dự án nhóm (Mini Project), lấy đề tài *Quản lý chi tiêu cá nhân* làm ví dụ.

## Chuẩn đầu ra và cách giáo trình rèn luyện

| CLO | Nội dung | Rèn luyện ở |
|---|---|---|
| CLO1 | Áp dụng ngôn ngữ lập trình để hiện thực các thuật toán đề ra ở mức cơ bản | Chương 1–8 và 10: mọi ví dụ, bài tập và bài tập hướng dẫn có viết mã |
| CLO2 | Sử dụng được các công cụ đồ họa để trình bày các ý tưởng thiết kế dữ liệu | Bảng IPO (Chương 1), lưu đồ (Chương 3–5), sơ đồ phân rã (Chương 7), hồ sơ thiết kế đề tài (Chương 9) |
| CLO3 | Thể hiện được vai trò cá nhân trong nhóm một cách rõ ràng | Bảng phân công (Chương 9), lịch sử commit, README và trình bày sản phẩm (Chương 10) |

## Học liệu đi kèm

- **Bài học trên LMS** (`bai-01` … `bai-12`): mỗi buổi một trang gồm tổng quan, học liệu, hoạt động trên lớp và quiz luyện tập. Học phần tổ chức theo mô hình lớp học đảo ngược: người học đọc chương tương ứng và bài trên LMS trước buổi học; thời gian trên lớp dành cho thực hành.
- **Slide bài giảng** (`Slides/bai-XX.pptx`): dùng trên lớp.
- **Ngân hàng câu hỏi trắc nghiệm** (`quiz/`): luyện tập cuối mỗi bài trên web và nhập vào Moodle.
- **Mã nguồn mẫu:** các ví dụ trong giáo trình; bộ 5 đoạn mã có lỗi cho bài thực hành "săn lỗi" của Chương 6.
- **Thông tin học phần và trang đánh giá:** chuẩn đầu ra, kế hoạch 12 buổi, tỷ trọng đánh giá và rubric.

## Quy ước dùng AI

**Với người học.** AI là trợ giảng, không phải người làm hộ. Một câu hỏi tốt gửi AI có ba phần: bối cảnh (đang học buổi mấy, đã biết gì), câu hỏi cụ thể và giới hạn (ví dụ "chỉ giải thích, đừng viết code mới"). Mỗi lần dùng AI trong bài thực hành, người học ghi vào **Nhật ký Prompt**: câu hỏi đã dùng, AI trả lời gì, mình đã kiểm tra và sửa ra sao, bài học rút ra. AI có thể trả lời sai; mọi câu trả lời phải được kiểm chứng bằng cách chạy thử với nhiều bộ dữ liệu. Không giải thích được đoạn mã mình nộp thì đoạn mã đó không được tính là bài làm của mình.

**Trong quá trình biên soạn.** Bản thảo giáo trình được soạn với sự hỗ trợ của trợ lý AI ở các khâu: lập dàn ý, diễn đạt, viết mã nguồn ví dụ, vẽ sơ đồ và rà soát định dạng. Toàn bộ mã nguồn ví dụ đã được chạy thử; nội dung chuyên môn được đối chiếu với tài liệu tham khảo ghi ở cuối mỗi chương. Người biên soạn chịu trách nhiệm về tính chính xác, bản quyền và toàn bộ nội dung của giáo trình.

## Quy ước trình bày

- `Chữ đơn cách` dùng cho mã nguồn, tên biến, tên hàm, tên file và lệnh gõ trong terminal.
- Trong các ví dụ chạy chương trình, dòng sau dấu `>>>` là lệnh gõ ở chế độ tương tác; phần chú thích `# ...` ghi kết quả mong đợi.
- Tên biến trong ví dụ viết bằng tiếng Việt không dấu theo kiểu `snake_case` (ví dụ `diem_tb`, `nam_sinh`) để người mới học dễ đọc; chuỗi hiển thị cho người dùng được viết có dấu.
- Số thập phân trong mã nguồn và khi nhập vào chương trình dùng dấu chấm (`8.5`); trong lời văn dùng dấu phẩy theo quy ước tiếng Việt (8,5).
- Các thang điểm, bảng giá dùng trong ví dụ (xếp loại học lực, giá điện theo bậc…) là **số liệu giả định cho bài tập**, không phải quy chế hay biểu giá thực tế.

*Bản thảo lưu hành nội bộ, Khoa Công nghệ Thông tin – Trường Đại học Lạc Hồng, 2026.*
