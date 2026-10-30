# Chương 12. Báo cáo đồ án, Demo Day và tổng kết

## Mục tiêu chương

Sau khi học xong chương này, bạn có thể:

- Tổ chức báo cáo đồ án và bộ sơ đồ thiết kế đáp ứng rubric cuối kỳ theo từng CLO.
- Chuẩn bị và trình diễn sản phẩm trên thiết bị Android thật kết nối backend trên server Khoa.
- Bảo vệ thiết kế chức năng, thiết kế dữ liệu và giải thích được phần mã mình phụ trách.
- Viết báo cáo vai trò cá nhân có minh chứng.
- Đánh giá sản phẩm của nhóm khác theo rubric và rút kinh nghiệm về việc phát triển phần mềm cùng trợ lý AI.

## 12.1. Đánh giá cuối kỳ

### 12.1.1. Rubric theo CLO

Điểm cuối kỳ (chiếm 40% điểm học phần) chấm trên thang 10, tách thành bốn phần theo CLO của học phần [2]:

| CLO | Nội dung | Điểm tối đa | Đạt khi | Minh chứng chính |
|---|---|---|---|---|
| CLO1 | Thiết kế thành phần chức năng | 3 | ≥ 1,5 | Sơ đồ chức năng; luồng nghiệp vụ chính, xác thực, tính năng thiết bị và thông báo realtime chạy trên Android |
| CLO2 | Thiết kế cơ sở dữ liệu | 2 | ≥ 1 | CSDL SQL Server (bảng, khóa, ràng buộc), bộ stored procedure, script dựng được CSDL trên server Khoa |
| CLO3 | Trình bày thiết kế dữ liệu bằng công cụ đồ họa | 2 | ≥ 1 | ERD phiên bản cuối, sơ đồ tuần tự luồng realtime, sơ đồ luồng màn hình; rõ ràng và khớp CSDL thật |
| CLO4 | Vai trò cá nhân trong nhóm | 3 | ≥ 1,5 | Báo cáo vai trò cá nhân, lịch sử commit/PR, phần tự trình bày và trả lời câu hỏi kỹ thuật |

Một sinh viên đạt một CLO khi được ít nhất 50% điểm của CLO đó. CLO1, CLO2, CLO3 chấm chủ yếu trên sản phẩm chung của nhóm, nhưng có thể điều chỉnh cho từng thành viên dựa trên phần bảo vệ; CLO4 chấm riêng từng người.

### 12.1.2. Đọc rubric như một danh sách kiểm tra

Trước Demo Day, nhóm đi qua từng dòng rubric và trả lời: **minh chứng của dòng này nằm ở đâu?** Mỗi minh chứng phải chỉ ra được cụ thể: trang mấy của báo cáo, file nào trong repo, bước nào trong kịch bản demo.

| Câu hỏi | Ví dụ trả lời của LHU Food |
|---|---|
| Luồng chính chạy trên Android ở đâu? | Kịch bản demo bước 2–5; video dự phòng |
| Bộ thủ tục ở đâu, có giao dịch không? | `database/02-procedures.sql`, `04-stock-reports.sql`; báo cáo mục 4.3 |
| ERD khớp CSDL thật? | Báo cáo hình 4.1; đối chiếu trực tiếp trên SQL Server khi được hỏi |
| Sơ đồ tuần tự realtime? | Báo cáo hình 5.2; slide 7 |
| Phần việc của tôi? | Báo cáo cá nhân; PR số 14, 21, 30 |

Dòng nào chưa trả lời được là việc cần làm trước hạn nộp.

## 12.2. Báo cáo đồ án

### 12.2.1. Cấu trúc đề xuất

Báo cáo trình bày **sản phẩm đã làm và lý do của các quyết định thiết kế**, không chép lại lý thuyết trong giáo trình.

| Chương | Nội dung | Liên quan CLO |
|---|---|---|
| 1. Giới thiệu | Bài toán, người dùng, phạm vi; thành viên và vai trò | |
| 2. Phân tích yêu cầu | User story, chức năng theo vai trò, yêu cầu phi chức năng (hiệu năng, bảo mật, Android/iOS) | CLO1 |
| 3. Thiết kế chức năng | Sơ đồ chức năng, sơ đồ luồng màn hình, kiến trúc (ứng dụng – API – SQL Server – Socket.IO), các thành phần chính của ứng dụng | CLO1, CLO3 |
| 4. Thiết kế dữ liệu | ERD phiên bản cuối, mô tả bảng và ràng buộc, danh mục stored procedure, giao dịch và xử lý lỗi | CLO2, CLO3 |
| 5. Hiện thực | Tính năng thiết bị, xác thực, realtime (sơ đồ tuần tự), các điểm kỹ thuật đáng chú ý | CLO1, CLO3 |
| 6. Kiểm thử | Phạm vi test, kết quả test tự động, kịch bản kiểm thử thủ tục, bug log tóm tắt, cải tiến hiệu năng có số liệu | CLO1 |
| 7. Triển khai | Triển khai trên Windows Server của Khoa, build APK, EAS Update | CLO1, CLO2 |
| 8. Sử dụng AI | Cách nhóm dùng trợ lý AI, ví dụ tiêu biểu từ `PROMPTS.md`, lỗi do AI gây ra và cách phát hiện | CLO4 |
| 9. Kết luận | Đã đạt, chưa đạt, hướng phát triển | |
| Phụ lục | Link repo app và API, link APK, hướng dẫn cài đặt, bảng phân công | CLO4 |

### 12.2.2. Viết phần thiết kế

- **Mỗi sơ đồ có một đoạn giải thích:** sơ đồ thể hiện gì, quyết định nào đáng chú ý và vì sao. Ví dụ: "Bảng `OrderItems` lưu `UnitPrice` tại thời điểm đặt, vì giá món có thể thay đổi sau đó".
- **Danh mục stored procedure** dạng bảng (tên, tham số, kết quả, mã lỗi) như Chương 5, đủ cho mọi nghiệp vụ; nêu rõ thủ tục nào có giao dịch.
- **Quyết định về trạng thái:** dữ liệu nào ở server (TanStack Query), dữ liệu nào chỉ ở máy (Zustand, AsyncStorage, SecureStore), và lý do (Chương 7).
- **Nhất quán thuật ngữ:** cùng một khái niệm dùng cùng một tên trong báo cáo, sơ đồ, CSDL và mã nguồn.

### 12.2.3. Phần kiểm thử và triển khai

Dùng số liệu thật thay cho nhận xét chung chung:

- "32 test tự động, tất cả pass; mutation thủ công với 6 lỗi cố ý, test bắt được 6" thay cho "ứng dụng đã được kiểm thử kỹ".
- "Gõ 5 ký tự vào ô tìm kiếm: từ 1.000 lần vẽ lại thẻ món xuống 0 sau khi dùng `React.memo`" thay cho "ứng dụng chạy mượt hơn".
- Triển khai: địa chỉ server (nếu được phép công khai trong báo cáo), ảnh chụp `/health`, ảnh ứng dụng chạy trên máy của người ngoài nhóm.

### 12.2.4. Phần sử dụng AI

Học phần cho phép và khuyến khích dùng Google Antigravity, GitHub Copilot Chat, nhưng yêu cầu minh bạch. Chương 8 của báo cáo nên có:

- Các loại việc nhóm giao cho AI (sinh khung màn hình, viết thủ tục, sinh test, giải thích lỗi) và loại việc nhóm tự làm.
- Hai đến ba ví dụ từ `PROMPTS.md`: prompt, kết quả, những gì nhóm phải sửa.
- Ít nhất một lỗi do AI gây ra (mã chạy được nhưng sai, lỗ hổng bảo mật, thư viện không tồn tại hoặc sai phiên bản) và cách nhóm phát hiện.

## 12.3. Bộ sơ đồ thiết kế

### 12.3.1. Bốn sơ đồ bắt buộc

| Sơ đồ | Thể hiện | Đã giới thiệu ở |
|---|---|---|
| Sơ đồ chức năng | Các nhóm chức năng theo vai trò (khách hàng, nhân viên) | Chương 2 |
| Sơ đồ luồng màn hình | Các màn hình và đường điều hướng giữa chúng (tab, stack, modal) | Chương 3 |
| ERD phiên bản cuối | Bảng, khóa chính, khóa ngoại, quan hệ, các cột quan trọng | Chương 3 (sơ bộ), Chương 5, Chương 7 |
| Sơ đồ tuần tự realtime | Từ thao tác đổi trạng thái đến thông báo trên điện thoại | Chương 9 |

Vẽ bằng công cụ đồ họa (draw.io, Figma, dbdiagram…); lưu cả file nguồn (`.drawio`, link Figma) và file ảnh trong `docs/` để chỉnh sửa được khi thiết kế thay đổi [6].

### 12.3.2. ERD phải khớp CSDL thật

Lỗi phổ biến nhất khi chấm CLO2, CLO3: ERD vẽ ở Sprint 1, CSDL thay đổi qua bốn sprint nhưng ERD không được cập nhật. Cách kiểm tra [5]:

```sql
-- Danh sách bảng và khóa ngoại đang có trên server
SELECT fk.name AS foreignKey,
       OBJECT_NAME(fk.parent_object_id) AS fromTable,
       OBJECT_NAME(fk.referenced_object_id) AS toTable
FROM sys.foreign_keys fk
ORDER BY fromTable;
```

Đối chiếu từng dòng kết quả với ERD: mỗi khóa ngoại trên server phải có đường quan hệ tương ứng trên sơ đồ, và ngược lại. SQL Server Management Studio cũng có công cụ Database Diagrams để xem nhanh quan hệ, nhưng sơ đồ trong báo cáo nên vẽ lại cho rõ ràng, có chú thích.

### 12.3.3. Sơ đồ đọc được trên máy chiếu

- Chữ trong sơ đồ không nhỏ hơn chữ thân của slide; tách sơ đồ lớn thành nhiều phần (ERD theo nhóm bảng).
- Không chụp màn hình mờ; xuất ảnh từ công cụ vẽ với độ phân giải cao.
- Sơ đồ tuần tự chỉ vẽ một luồng (ví dụ "nhân viên chuyển đơn sang Sẵn sàng"), đủ các bên: ứng dụng nhân viên, API, thủ tục, SQL Server, gateway Socket.IO, room, ứng dụng khách hàng.

## 12.4. Chuẩn bị Demo Day

### 12.4.1. Cấu trúc phần trình bày

Mỗi nhóm có 10 phút trình bày và 5 phút hỏi đáp:

| Phần | Thời gian | Người trình bày | Nội dung |
|---|---|---|---|
| Giới thiệu | 1 phút | Trưởng nhóm | Bài toán, người dùng, thành viên và vai trò |
| Demo | 5 phút | Các thành viên phụ trách từng tính năng | Kịch bản demo trên điện thoại thật |
| Thiết kế | 4 phút | Thành viên phụ trách thiết kế, CSDL, realtime | Sơ đồ chức năng, ERD, sơ đồ tuần tự |
| Hỏi đáp | 5 phút | Thành viên được hỏi | Bảo vệ kỹ thuật và câu hỏi từ lớp |

**Mọi thành viên đều phải trình bày** một phần mình trực tiếp làm. Phần trình bày là minh chứng CLO4; thành viên không trình bày sẽ thiếu minh chứng.

### 12.4.2. Kịch bản demo

Viết kịch bản ra giấy và tập trên đúng thiết bị, đúng mạng sẽ dùng (nếu được, tập tại phòng học). Kịch bản của LHU Food:

| Bước | Thao tác | Điều cần chứng minh |
|---|---|---|
| 1 | Mở APK (không phải Expo Go), đăng nhập | Bản build kết nối server Khoa; xác thực JWT |
| 2 | Tìm món, xem chi tiết, thêm vào giỏ; tắt và mở lại ứng dụng | Danh sách từ SQL Server; giỏ hàng được lưu trên máy |
| 3 | Đặt món | Thủ tục đặt hàng có giao dịch; đơn xuất hiện trên SQL Server |
| 4 | Chụp ảnh đánh giá, chọn vị trí nhận trên bản đồ | Tính năng thiết bị, quyền |
| 5 | Thành viên khác (tài khoản nhân viên) đổi trạng thái đơn | Thông báo realtime đến ngay trên máy khách |
| 6 | Đặt món đã hết | Mã lỗi 50409 từ thủ tục hiển thị thành thông báo dễ hiểu |

Bước 5 cần **hai thiết bị** (hoặc một thiết bị và một màn hình quản lý trên máy khác). Bước 3 và 6 nên chuẩn bị sẵn dữ liệu (một món còn đúng 1 suất) bằng script, không sửa tay trước mặt lớp.

### 12.4.3. Kiểm tra trước giờ demo

Ba mươi phút trước buổi:

- ☐ `/health` của API trên server Khoa trả `ok` khi mở từ mạng phòng học.
- ☐ APK đã cài là bản mới nhất (hoặc đã nhận EAS Update mới nhất).
- ☐ Đăng nhập được bằng tài khoản demo; socket kết nối (thử bước 5 một lần).
- ☐ Quyền camera, vị trí, thông báo đã cấp; pin đầy; tắt chế độ tiết kiệm pin và chế độ không làm phiền.
- ☐ Dữ liệu demo sạch: tên món, giá, ảnh thật; không có "test1", "aaa", đơn rác.
- ☐ Màn hình điện thoại chiếu được lên máy chiếu (công cụ phản chiếu màn hình qua cáp USB hoặc qua mạng).
- ☐ Slide và sơ đồ đã mở sẵn; video dự phòng đã tải về máy (không phụ thuộc mạng).

### 12.4.4. Phương án dự phòng

Demo trực tiếp luôn có rủi ro: mạng phòng học, server bảo trì, điện thoại hết pin. Chuẩn bị:

- **Video demo đầy đủ** theo đúng kịch bản, quay màn hình điện thoại, có thể kèm ghi âm giải thích.
- **Thiết bị thứ hai** đã cài APK và đăng nhập.
- **Ảnh chụp** các bước quan trọng trong slide.

Nếu server gặp sự cố, báo ngay giảng viên và bộ phận hỗ trợ, chuyển sang video, và demo trực tiếp lại khi server hoạt động nếu thời gian cho phép. Giảng viên đánh giá cao nhóm xử lý sự cố bình tĩnh, giải thích được nguyên nhân.

## 12.5. Bảo vệ thiết kế và bảo vệ kỹ thuật

### 12.5.1. Bảo vệ thiết kế

Khi trình bày sơ đồ, nói về **quyết định và lý do**, không đọc lại tên từng ô trên sơ đồ:

- "Chúng em tách `OrderItems` ra bảng riêng vì một đơn có nhiều món; giá lưu lại tại thời điểm đặt."
- "Thủ tục đặt hàng khóa dòng sản phẩm bằng `UPDLOCK` để hai người không cùng mua suất cuối cùng."
- "Thông báo lưu vào bảng `Notifications` trước rồi mới gửi qua socket, để người đang tắt ứng dụng vẫn xem lại được."

Giảng viên có thể yêu cầu mở SQL Server trên server Khoa để đối chiếu một bảng, một khóa ngoại hoặc nội dung một thủ tục với sơ đồ và báo cáo.

### 12.5.2. Bảo vệ kỹ thuật

Giảng viên mở repo, chọn một đoạn mã và hỏi **thành viên đã commit đoạn đó** (xem bằng `git log` hoặc chế độ Blame trên GitHub). Các dạng câu hỏi [3]:

| Dạng câu hỏi | Ví dụ |
|---|---|
| Giải thích | Đoạn mã này làm gì? Hàm này được gọi khi nào? |
| Thay đổi giả định | Nếu xóa dòng `invalidateQueries` này thì người dùng thấy gì? |
| Lựa chọn thiết kế | Vì sao lưu token bằng SecureStore mà không dùng AsyncStorage? |
| Tình huống biên | Mất mạng đúng lúc bấm Đặt món thì chuyện gì xảy ra? |
| Liên kết các tầng | Lỗi 409 này xuất phát từ đâu và đi qua những lớp nào để đến màn hình? |
| AI | Đoạn này có do AI sinh không? Bạn đã kiểm tra và sửa gì? |

Cách chuẩn bị:

- Mỗi thành viên đọc lại **toàn bộ** mã mình đã commit, đặc biệt phần do AI sinh.
- Cặp đôi trong nhóm hỏi chéo nhau theo bảng trên.
- Nếu không chắc câu trả lời, nói rõ phần mình hiểu và phần chưa chắc; không đoán.

Nguyên tắc "**không hiểu thì không merge**" từ Chương 1 được áp dụng ở đây: phần mã chạy đúng nhưng người viết không giải thích được thì không được tính điểm.

## 12.6. Báo cáo vai trò cá nhân

Mỗi thành viên nộp riêng một báo cáo 1–2 trang:

```markdown
# Báo cáo vai trò cá nhân - <Họ tên> - <MSSV>

## 1. Vai trò và nhiệm vụ
Phụ trách: màn hình Giỏ hàng, Đặt món; thủ tục sp_Order_Create, sp_Order_Cancel.

## 2. Đóng góp tiêu biểu (có link)
- PR #14: Store giỏ hàng có persist và test (12 test).
- PR #21: Giao dịch và khóa dòng cho sp_Order_Create; kịch bản kiểm thử TC-01..06.
- PR #30: Sửa BUG-07 (tổng tiền sai khi giảm số lượng).

## 3. Khó khăn đã giải quyết
Hai người cùng đặt suất cuối cùng làm tồn kho âm; tái hiện bằng hai cửa sổ SSMS, sửa bằng UPDLOCK, HOLDLOCK.

## 4. Sử dụng AI
Copilot sinh khung thủ tục và test; em phải sửa phần gộp món trùng và bổ sung test giảm về 0
(PROMPTS.md mục 12, 18).

## 5. Tự đánh giá
Điều làm tốt, điều cần cải thiện, mức đóng góp so với nhóm.
```

Báo cáo phải khớp với lịch sử commit và PR. Đóng góp không có trên repo (họp, vẽ sơ đồ, viết báo cáo) vẫn được ghi nhận, kèm minh chứng (file sơ đồ, biên bản Sprint Review).

## 12.7. Sản phẩm nộp cuối kỳ

| Sản phẩm | Yêu cầu |
|---|---|
| Báo cáo đồ án | Theo cấu trúc mục 12.2 |
| Bộ sơ đồ thiết kế | Bốn sơ đồ ở mục 12.3, cả file nguồn và ảnh |
| Script CSDL | `database/` dựng được CSDL từ đầu: bảng, thủ tục, dữ liệu mẫu |
| Repo GitHub | Link repo ứng dụng và repo API; README có hướng dẫn chạy và triển khai; `PROMPTS.md` |
| File APK | Bản `preview` kết nối backend trên Windows Server của Khoa |
| Slide Demo Day | Kèm video demo dự phòng |
| Báo cáo vai trò cá nhân | Mỗi thành viên nộp riêng |

Trưởng nhóm nộp sản phẩm chung; mỗi thành viên nộp báo cáo cá nhân, theo hạn và cổng nộp trên Moodle. Sau hạn nộp, nhóm không sửa nhánh chính của repo cho đến khi có điểm, để giảng viên chấm đúng phiên bản đã nộp (gắn tag, ví dụ `v1.0-final`) [4].

## 12.8. Review chéo

Trong buổi Demo Day, mỗi nhóm được phân công đánh giá một số nhóm khác theo cùng rubric ở mục 12.1. Review chéo giúp người đánh giá học được cách nhìn sản phẩm từ phía người dùng và phía người chấm.

Nguyên tắc nhận xét:

- **Cụ thể:** "Thông báo realtime đến ngay khi đổi trạng thái" thay cho "demo tốt".
- **Có đề xuất:** mỗi điểm số kèm ít nhất một điểm mạnh và một đề xuất cải tiến có thể thực hiện.
- **Dựa trên minh chứng:** đánh giá những gì thấy trong phần trình bày, không dựa trên cảm tình.

Điểm review chéo là ý kiến tham khảo cho giảng viên và là minh chứng tham gia review trong điểm quá trình; điểm cuối kỳ do giảng viên quyết định.

## 12.9. Nhìn lại học phần

### 12.9.1. Những gì đã xây dựng

Qua bốn sprint, mỗi nhóm đã đi qua toàn bộ vòng đời của một ứng dụng di động [1]:

| Sprint | Kết quả |
|---|---|
| 1. Nền tảng | Dự án Expo, giao diện bằng core components và Flexbox, điều hướng bằng Expo Router |
| 2. Dữ liệu và người dùng | CSDL SQL Server, stored procedure, API NestJS, xác thực JWT |
| 3. Thiết bị và realtime | Giao dịch, đồng bộ, camera, vị trí, bản đồ, thông báo qua Socket.IO |
| 4. Chất lượng và phát hành | Kiểm thử, gỡ lỗi, tối ưu, triển khai lên server Khoa, build APK |

### 12.9.2. Phát triển phần mềm cùng AI

Câu hỏi thảo luận cuối học phần:

- Trợ lý AI giúp nhóm tiết kiệm thời gian nhất ở loại việc nào?
- Lỗi nào do AI gây ra khiến nhóm mất nhiều công nhất? Làm sao phát hiện?
- Khi nào nhóm quyết định không dùng mã AI sinh ra?
- Nếu làm lại từ đầu, bạn sẽ viết prompt, kiểm tra kết quả và chia việc với AI khác đi thế nào?

Điều học phần muốn bạn mang theo: AI làm phần gõ phím nhanh hơn, nhưng **hiểu bài toán, thiết kế dữ liệu, kiểm thử và chịu trách nhiệm về mã** vẫn là việc của người phát triển. Những kỹ năng này mới là điều học phần đánh giá.

### 12.9.3. Hướng phát triển tiếp

- Hoàn thiện ứng dụng và phát hành lên Google Play; bổ sung push notification khi ứng dụng đã tắt (Chương 9).
- Tự động hóa: GitHub Actions chạy test cho mỗi pull request và build khi gắn tag phiên bản.
- Kiểm thử đầu-cuối bằng Maestro; theo dõi lỗi bằng Sentry.
- Đưa đồ án vào portfolio cá nhân: README rõ ràng, ảnh chụp, video demo, mô tả phần mình phụ trách.
- Kết hợp với đề tài của học phần Phát triển ứng dụng web: cùng một backend phục vụ cả web và di động.

## Tóm tắt chương

- Điểm cuối kỳ chấm theo 4 CLO trên thang 10; nhóm dùng rubric làm danh sách kiểm tra minh chứng.
- Báo cáo trình bày sản phẩm và lý do thiết kế, có số liệu kiểm thử, triển khai và phần sử dụng AI minh bạch.
- Bộ sơ đồ gồm sơ đồ chức năng, luồng màn hình, ERD cuối và tuần tự realtime; ERD phải khớp CSDL trên server.
- Demo Day: 10 phút trình bày, 5 phút hỏi đáp; demo bằng APK trên điện thoại thật kết nối server Khoa; mọi thành viên đều trình bày.
- Chuẩn bị kịch bản, kiểm tra trước giờ demo và có phương án dự phòng.
- Bảo vệ kỹ thuật: người đã commit giải thích đoạn mã; không giải thích được thì không tính điểm.
- Báo cáo vai trò cá nhân có minh chứng từ repo; review chéo cụ thể, có đề xuất.

## Câu hỏi ôn tập

1. Nêu điểm tối đa, ngưỡng đạt và minh chứng chính của từng CLO trong rubric cuối kỳ.
2. Vì sao ERD vẽ ở Sprint 1 thường không còn đúng ở cuối kỳ? Kiểm tra sự khớp nhau giữa ERD và CSDL bằng cách nào?
3. Kịch bản demo của nhóm bạn chứng minh những gì cho CLO1 và CLO2?
4. Liệt kê các phương án dự phòng cho phần demo và tình huống mà mỗi phương án xử lý.
5. Báo cáo vai trò cá nhân cần những minh chứng gì? Vì sao phải khớp với lịch sử commit?
6. Một nhận xét review chéo tốt có những đặc điểm gì?

## Bài tập

1. **Ma trận minh chứng.** Lập bảng như mục 12.1.2 cho đề tài của nhóm: mỗi dòng rubric và vị trí minh chứng cụ thể. Bổ sung các minh chứng còn thiếu.
2. **Kịch bản và tập demo.** Viết kịch bản demo dạng bảng như mục 12.4.2, phân công người trình bày từng bước; tập ít nhất một lần có bấm giờ trên đúng thiết bị; quay video dự phòng.
3. **Hỏi chéo kỹ thuật.** Mỗi thành viên chuẩn bị 5 câu hỏi theo bảng mục 12.5.2 về phần mã của một thành viên khác; thực hành hỏi đáp và ghi lại câu chưa trả lời được để ôn.
4. **Báo cáo cá nhân.** Viết báo cáo vai trò cá nhân theo mẫu mục 12.6, kèm link PR/commit.

## Tài liệu tham khảo

[1] Khoa Công nghệ Thông tin, Trường Đại học Lạc Hồng, *Giáo trình Lập trình ứng dụng di động*, Bản thảo lưu hành nội bộ. Đồng Nai, Việt Nam, 2026.

[2] Khoa Công nghệ Thông tin, Trường Đại học Lạc Hồng, “Đánh giá học phần Lập trình ứng dụng di động (111114),” Hệ thống học tập trực tuyến LHU (Moodle), 2026.

[3] GitHub, Inc., “Viewing and understanding files,” *GitHub Docs*. Accessed: Oct. 30, 2026. [Online]. Available: https://docs.github.com/repositories/working-with-files/using-files/viewing-and-understanding-files

[4] GitHub, Inc., “Managing releases in a repository,” *GitHub Docs*. Accessed: Oct. 30, 2026. [Online]. Available: https://docs.github.com/repositories/releasing-projects-on-github/managing-releases-in-a-repository

[5] Microsoft, “sys.foreign_keys (Transact-SQL),” *Microsoft Learn*. Accessed: Oct. 30, 2026. [Online]. Available: https://learn.microsoft.com/sql/relational-databases/system-catalog-views/sys-foreign-keys-transact-sql

[6] JGraph Ltd., “draw.io documentation,” *draw.io Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://www.drawio.com/doc/
