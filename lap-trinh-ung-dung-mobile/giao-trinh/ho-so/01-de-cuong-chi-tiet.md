# Đề cương chi tiết giáo trình

> Đề cương lập **hồi cứu** từ bản thảo đã biên soạn (bước 1, Điều 7 khoản 2 Thông tư 62/2026/TT-BGDĐT), để làm căn cứ lấy ý kiến và thẩm định. Nội dung cấu trúc dưới đây sinh tự động từ các file chương; số trang ước tính theo 350 từ/trang.

## 1. Thông tin chung

| Mục | Nội dung |
|---|---|
| Tên tài liệu | Giáo trình Lập trình ứng dụng di động |
| Loại tài liệu | Giáo trình |
| Học phần | Lập trình ứng dụng di động (111114), 3 tín chỉ; 60 tiết (15 LT + 45 TH) |
| Đối tượng người học | Sinh viên Công nghệ Thông tin học kỳ 6; đã học Thiết kế UI/UX, Thiết kế Web, Lập trình Frontend (React), Lập trình Backend |
| Chủ biên | {{Họ tên, học hàm, học vị, đơn vị}} |
| Người biên soạn | {{Họ tên}} (giảng viên phụ trách học phần theo course.json: ThS. Nguyễn Minh Phúc) |
| Ngôn ngữ | Tiếng Việt |
| Hình thức khai thác | Bản số (Word/PDF) và bản in; kèm học liệu số trên LMS |
| Căn cứ | Đề cương học phần; Thông tư 62/2026/TT-BGDĐT; {{quy định nội bộ của Trường về biên soạn giáo trình, nếu có}} |

## 2. Mục tiêu của tài liệu

{{Hai đến bốn câu do chủ biên xác nhận; tham khảo đoạn mở đầu của Lời nói đầu.}}

## 3. Ma trận chương – chuẩn đầu ra học phần

| CLO | Nội dung | Rèn luyện ở |
|---|---|---|
| CLO1 | Thiết kế các thành phần chức năng của ứng dụng di động đáp ứng các yêu cầu đặt ra | Sơ đồ chức năng (Chương 2), điều hướng và trạng thái (Chương 3–4), xác thực (Chương 6), tính năng thiết bị (Chương 8), thông báo realtime (Chương 9) |
| CLO2 | Thiết kế cơ sở dữ liệu đáp ứng cấu trúc dữ liệu phù hợp yêu cầu đặc tả | CSDL và stored procedure (Chương 5), ràng buộc, giao dịch, báo cáo (Chương 7), triển khai script CSDL (Chương 11) |
| CLO3 | Sử dụng được các công cụ đồ họa để trình bày các ý tưởng thiết kế dữ liệu | Sơ đồ chức năng (Chương 2), sơ đồ luồng màn hình và ERD sơ bộ (Chương 3), ERD hoàn chỉnh (Chương 5), sơ đồ tuần tự (Chương 9) |
| CLO4 | Thể hiện được vai trò cá nhân trong nhóm một cách rõ ràng | Phân vai (Chương 1), checkpoint sprint (Chương 3, 6, 9), báo cáo vai trò cá nhân và Demo Day (Chương 12) |

## 4. Nội dung chi tiết

### Chương 1. Tổng quan phát triển ứng dụng di động và khởi động dự án

**Mục tiêu:**

- So sánh các hướng phát triển ứng dụng di động: native, cross-platform và PWA.
- Giải thích cách React Native hiển thị giao diện native và vai trò của Expo.
- Cài đặt môi trường, tạo và chạy dự án Expo đầu tiên trên điện thoại Android.
- Chuyển cách viết component từ React web sang React Native.
- Thiết lập quy trình vibe coding có kiểm soát và bảng phân vai cho dự án nhóm.

**Nội dung:**

- 1.1. Các hướng phát triển ứng dụng di động
- 1.2. React Native hoạt động như thế nào
  - 1.2.1. Từ component đến view native
  - 1.2.2. Kiến trúc mới (New Architecture)
  - 1.2.3. Expo
- 1.3. Cài đặt môi trường và tạo dự án
  - 1.3.1. Công cụ cần có
  - 1.3.2. Tạo dự án LHU Food
  - 1.3.3. Cấu trúc thư mục
- 1.4. Từ React web sang React Native
  - 1.4.1. Bảng tương ứng
  - 1.4.2. Một lỗi điển hình
- 1.5. Vibe coding có kiểm soát
  - 1.5.1. Khái niệm
  - 1.5.2. Quy trình năm bước
  - 1.5.3. File quy ước dự án
  - 1.5.4. Mẫu ghi `PROMPTS.md`
  - 1.5.5. Làm việc nhóm với Git
- 1.6. Dự án PBL và phân vai
- 1.7. Mã nguồn LHU Food của chương

**Thực hành:** câu hỏi ôn tập, bài tập cuối chương; bài tập hướng dẫn `bt-01`.
**Liên kết học liệu:** bài học `bai-01`, slide `Slides/bai-01.pptx`, quiz bài 01.
**Dung lượng ước tính:** khoảng 8 trang; tài liệu tham khảo: 4.

### Chương 2. Core Components, Styling và Layout với Flexbox

**Mục tiêu:**

- Sử dụng đúng các core component của React Native.
- Dựng bố cục bằng Flexbox, hiển thị đúng trên nhiều kích thước màn hình.
- Xây dựng design system gồm theme và component dùng chung.
- Chuyển thiết kế Figma thành mã bằng vibe coding và kiểm tra lại kết quả.
- Trình bày sơ đồ chức năng của ứng dụng bằng công cụ đồ họa.

**Nội dung:**

- 2.1. Core components
  - 2.1.1. View và Text
  - 2.1.2. Image
  - 2.1.3. ScrollView
  - 2.1.4. TextInput
  - 2.1.5. Pressable
  - 2.1.6. Vùng an toàn
- 2.2. Flexbox trong React Native
  - 2.2.1. Khác biệt so với CSS trên web
  - 2.2.2. Các thuộc tính chính
  - 2.2.3. Ví dụ: màn hình Chi tiết món
  - 2.2.4. Bố cục theo kích thước màn hình
- 2.3. Design system: theme và component dùng chung
  - 2.3.1. Vì sao cần theme
  - 2.3.2. File theme
  - 2.3.3. Chế độ sáng và tối
  - 2.3.4. Component dùng chung
- 2.4. Từ Figma đến mã bằng vibe coding
  - 2.4.1. Quy trình
  - 2.4.2. Lỗi trợ lý AI hay mắc khi dựng giao diện
- 2.5. Sơ đồ chức năng
  - 2.5.1. Khái niệm
  - 2.5.2. Sơ đồ chức năng LHU Food

**Thực hành:** câu hỏi ôn tập, bài tập cuối chương; bài tập hướng dẫn `bt-02`.
**Liên kết học liệu:** bài học `bai-02`, slide `Slides/bai-02.pptx`, quiz bài 02.
**Dung lượng ước tính:** khoảng 6 trang; tài liệu tham khảo: 4.

### Chương 3. Điều hướng với Expo Router

**Mục tiêu:**

- Giải thích các mô hình điều hướng trên di động: stack, tab, modal.
- Tổ chức màn hình theo cấu trúc thư mục của Expo Router.
- Dùng route động, truyền tham số và chuyển màn hình bằng mã.
- Cấu hình deep link cho ứng dụng.
- Vẽ sơ đồ luồng màn hình và ERD sơ bộ từ danh sách màn hình.

**Nội dung:**

- 3.1. Mô hình điều hướng trên di động
  - 3.1.1. Stack
  - 3.1.2. Tab
  - 3.1.3. Modal
  - 3.1.4. Lồng các mô hình
- 3.2. Expo Router: điều hướng dựa trên file
  - 3.2.1. Nguyên tắc
  - 3.2.2. Cấu trúc thư mục của LHU Food
  - 3.2.3. Layout gốc
  - 3.2.4. Layout thanh tab
- 3.3. Route động, tham số và chuyển màn hình
  - 3.3.1. Đọc tham số
  - 3.3.2. Chuyển màn hình
  - 3.3.3. Deep link
- 3.4. Từ màn hình đến dữ liệu
  - 3.4.1. Sơ đồ luồng màn hình
  - 3.4.2. Xác định thực thể và quan hệ
  - 3.4.3. ERD sơ bộ
- 3.5. Checkpoint Sprint 1
- 3.6. Mã nguồn LHU Food của chương

**Thực hành:** câu hỏi ôn tập, bài tập cuối chương; bài tập hướng dẫn `bt-03`.
**Liên kết học liệu:** bài học `bai-03`, slide `Slides/bai-03.pptx`, quiz bài 03.
**Dung lượng ước tính:** khoảng 6 trang; tài liệu tham khảo: 4.

### Chương 4. Quản lý trạng thái, danh sách và form

**Mục tiêu:**

- Phân biệt trạng thái cục bộ, trạng thái toàn cục và dữ liệu từ server.
- Quản lý trạng thái toàn cục bằng Zustand.
- Hiển thị danh sách lớn hiệu quả bằng `FlatList` và `SectionList`.
- Xây dựng form có kiểm tra dữ liệu bằng React Hook Form và Zod.
- Dùng AI sinh quy tắc kiểm tra và tự kiểm chứng bằng giá trị biên.

**Nội dung:**

- 4.1. Ba loại trạng thái
  - 4.1.1. useReducer cho state có nhiều thao tác
- 4.2. Trạng thái toàn cục với Zustand
  - 4.2.1. Vì sao chọn Zustand
  - 4.2.2. Store giỏ hàng
  - 4.2.3. Nguyên tắc bất biến
  - 4.2.4. Đọc store ở màn hình
- 4.3. Danh sách với FlatList
  - 4.3.1. Vì sao không dùng ScrollView cho danh sách dài
  - 4.3.2. Các thuộc tính chính
  - 4.3.3. Không lồng FlatList trong ScrollView cùng chiều
  - 4.3.4. SectionList
- 4.4. Form với React Hook Form và Zod
  - 4.4.1. Vai trò của từng thư viện
  - 4.4.2. Schema đăng ký tài khoản
  - 4.4.3. Gắn TextInput bằng Controller
  - 4.4.4. Bàn phím trên di động
  - 4.4.5. Kiểm tra ở ứng dụng chưa đủ
- 4.5. Vibe coding cho quy tắc nghiệp vụ
  - 4.5.1. Quy trình
  - 4.5.2. Bảng giá trị biên mẫu
- 4.6. Chuẩn bị backend cho Chương 5

**Thực hành:** câu hỏi ôn tập, bài tập cuối chương; bài tập hướng dẫn `bt-04`.
**Liên kết học liệu:** bài học `bai-04`, slide `Slides/bai-04.pptx`, quiz bài 04.
**Dung lượng ước tính:** khoảng 6 trang; tài liệu tham khảo: 6.

### Chương 5. Thiết kế CSDL, stored procedure, API NestJS và kết nối ứng dụng

**Mục tiêu:**

- Hoàn thiện thiết kế cơ sở dữ liệu SQL Server từ ERD sơ bộ.
- Viết stored procedure có tham số, phân trang và báo lỗi bằng mã tự đặt.
- Xây dựng REST API NestJS chỉ truy cập dữ liệu qua stored procedure bằng thư viện `mssql`.
- Kết nối ứng dụng React Native với API và quản lý dữ liệu server bằng TanStack Query.

**Nội dung:**

- 5.1. Kiến trúc ba lớp của LHU Food
- 5.2. Hoàn thiện thiết kế cơ sở dữ liệu
  - 5.2.1. Từ ERD sơ bộ đến lược đồ
  - 5.2.2. Script tạo bảng
  - 5.2.3. ERD hoàn chỉnh
- 5.3. Stored procedure
  - 5.3.1. Vì sao bắt buộc dùng stored procedure
  - 5.3.2. Quy ước
  - 5.3.3. Thủ tục đọc dữ liệu
  - 5.3.4. Thủ tục ghi dữ liệu
  - 5.3.5. Chạy thử trong SSMS
  - 5.3.6. Danh mục stored procedure
- 5.4. API NestJS với mssql
  - 5.4.1. Chuẩn bị
  - 5.4.2. DatabaseService dùng chung
  - 5.4.3. Module Products
  - 5.4.4. Module Orders và DTO
  - 5.4.5. Cấu hình khởi động
  - 5.4.6. Vibe coding cho backend
- 5.5. Kết nối ứng dụng với API
  - 5.5.1. Địa chỉ API
  - 5.5.2. Hàm gọi API tập trung
  - 5.5.3. TanStack Query
  - 5.5.4. Bốn trạng thái của màn hình dữ liệu
  - 5.5.5. Ghi dữ liệu với useMutation
  - 5.5.6. Cuộn vô hạn

**Thực hành:** câu hỏi ôn tập, bài tập cuối chương; bài tập hướng dẫn `bt-05`.
**Liên kết học liệu:** bài học `bai-05`, slide `Slides/bai-05.pptx`, quiz bài 05.
**Dung lượng ước tính:** khoảng 7 trang; tài liệu tham khảo: 7.

### Chương 6. Xác thực và bảo mật ứng dụng

**Mục tiêu:**

- Giải thích luồng xác thực bằng JWT với access token và refresh token.
- Lưu mật khẩu an toàn bằng bcrypt và quản lý tài khoản qua stored procedure.
- Xây dựng đăng ký, đăng nhập, Guard xác thực và phân quyền theo vai trò trong NestJS.
- Lưu token an toàn trên điện thoại và bảo vệ màn hình trong Expo Router.
- Nhận diện và phòng tránh các rủi ro bảo mật thường gặp của ứng dụng di động.

**Nội dung:**

- 6.1. Xác thực và phân quyền
- 6.2. JWT, access token và refresh token
  - 6.2.1. JWT là gì
  - 6.2.2. Hai loại token
  - 6.2.3. Luồng đầy đủ
- 6.3. Lưu mật khẩu và tài khoản trên SQL Server
  - 6.3.1. Băm mật khẩu bằng bcrypt
  - 6.3.2. Bảng và thủ tục
- 6.4. Xác thực trong NestJS
  - 6.4.1. Cài đặt và cấu hình
  - 6.4.2. AuthService
  - 6.4.3. AuthGuard
  - 6.4.4. Phân quyền theo vai trò
- 6.5. Phía ứng dụng
  - 6.5.1. SecureStore và AsyncStorage
  - 6.5.2. Store xác thực
  - 6.5.3. Gắn token vào request
  - 6.5.4. Bảo vệ màn hình
  - 6.5.5. Xử lý token hết hạn
- 6.6. Rủi ro bảo mật thường gặp
  - 6.6.1. Tài khoản SQL Server chỉ có quyền EXECUTE
  - 6.6.2. Review bảo mật mã do AI sinh
- 6.7. Checkpoint Sprint 2

**Thực hành:** câu hỏi ôn tập, bài tập cuối chương; bài tập hướng dẫn `bt-06`.
**Liên kết học liệu:** bài học `bai-06`, slide `Slides/bai-06.pptx`, quiz bài 06.
**Dung lượng ước tính:** khoảng 7 trang; tài liệu tham khảo: 7.

### Chương 7. CSDL SQL Server nâng cao và đồng bộ dữ liệu qua backend

**Mục tiêu:**

- Bảo vệ toàn vẹn dữ liệu bằng ràng buộc và tăng tốc truy vấn bằng chỉ mục.
- Viết stored procedure có giao dịch, xử lý lỗi và chống tranh chấp khi nhiều người thao tác cùng lúc.
- Viết thủ tục báo cáo và quản lý script cơ sở dữ liệu theo phiên bản.
- Đồng bộ dữ liệu giữa ứng dụng và server: cache, optimistic update, lưu trạng thái tạm trên thiết bị.

**Nội dung:**

- 7.1. Toàn vẹn dữ liệu
  - 7.1.1. Vì sao đặt quy tắc ở cơ sở dữ liệu
  - 7.1.2. Các loại ràng buộc
- 7.2. Chỉ mục
  - 7.2.1. Chỉ mục là gì
  - 7.2.2. Chọn chỉ mục theo thủ tục
- 7.3. Giao dịch trong stored procedure
  - 7.3.1. Khái niệm và tính chất ACID
  - 7.3.2. Khuôn mẫu xử lý lỗi
  - 7.3.3. Tranh chấp đồng thời: suất cơm cuối cùng
  - 7.3.4. Thủ tục đặt hàng hoàn chỉnh
  - 7.3.5. Hủy đơn và hoàn tồn kho
  - 7.3.6. Tham số kiểu bảng (tùy chọn)
- 7.4. Thủ tục báo cáo
  - 7.4.1. Doanh thu theo ngày
  - 7.4.2. Món bán chạy
  - 7.4.3. API báo cáo chỉ dành cho nhân viên
- 7.5. Script CSDL theo phiên bản
  - 7.5.1. Tổ chức thư mục
  - 7.5.2. Vì sao quan trọng
- 7.6. Đồng bộ ứng dụng với server
  - 7.6.1. Nguồn dữ liệu chuẩn
  - 7.6.2. Độ "tươi" của cache
  - 7.6.3. Optimistic update
  - 7.6.4. Giữ giỏ hàng khi tắt ứng dụng
- 7.7. Mã nguồn bổ sung của chương

**Thực hành:** câu hỏi ôn tập, bài tập cuối chương; bài tập hướng dẫn `bt-07`.
**Liên kết học liệu:** bài học `bai-07`, slide `Slides/bai-07.pptx`, quiz bài 07.
**Dung lượng ước tính:** khoảng 8 trang; tài liệu tham khảo: 7.

### Chương 8. Tính năng thiết bị: Camera, Ảnh, Vị trí và Bản đồ

**Mục tiêu:**

- Giải thích mô hình quyền truy cập trên Android và cách xin quyền đúng cách.
- Chụp hoặc chọn ảnh, nén ảnh và tải lên API NestJS; lưu thông tin ảnh vào SQL Server qua stored procedure.
- Lấy vị trí hiện tại, hiển thị bản đồ và tính khoảng cách giữa hai tọa độ.
- Quyết định khi nào dùng Expo Go, khi nào cần development build.

**Nội dung:**

- 8.1. Quyền truy cập trên thiết bị
  - 8.1.1. Mô hình quyền
  - 8.1.2. Nguyên tắc xin quyền
  - 8.1.3. Khai báo quyền trong app.json
- 8.2. Chụp và chọn ảnh
  - 8.2.1. expo-image-picker
  - 8.2.2. Tải ảnh lên server
  - 8.2.3. Nhận file trong NestJS
  - 8.2.4. Phục vụ file tĩnh và lưu đường dẫn
- 8.3. Vị trí và bản đồ
  - 8.3.1. Lấy vị trí hiện tại
  - 8.3.2. Dữ liệu quầy căn tin
  - 8.3.3. Tính khoảng cách
  - 8.3.4. Màn hình bản đồ
- 8.4. Expo Go và development build
  - 8.4.1. So sánh
  - 8.4.2. Tạo development build (khi cần)
  - 8.4.3. Chọn thư viện thông minh

**Thực hành:** câu hỏi ôn tập, bài tập cuối chương; bài tập hướng dẫn `bt-08`.
**Liên kết học liệu:** bài học `bai-08`, slide `Slides/bai-08.pptx`, quiz bài 08.
**Dung lượng ước tính:** khoảng 7 trang; tài liệu tham khảo: 7.

### Chương 9. Thông báo thời gian thực với Socket.IO

**Mục tiêu:**

- So sánh polling, WebSocket và Socket.IO; giải thích sự kiện, room và xác thực kết nối.
- Thiết kế bảng và stored procedure lưu thông báo trên SQL Server.
- Xây dựng NestJS Gateway có xác thực JWT, gửi sự kiện tới đúng người dùng hoặc nhóm người dùng.
- Kết nối Socket.IO từ ứng dụng React Native, cập nhật dữ liệu và hiển thị thông báo cục bộ.
- Trình bày luồng dữ liệu realtime bằng sơ đồ tuần tự.

**Nội dung:**

- 9.1. Giao tiếp thời gian thực
  - 9.1.1. Vì sao cần realtime
  - 9.1.2. Ba cách tiếp cận
  - 9.1.3. Khái niệm của Socket.IO
- 9.2. Thiết kế luồng thông báo
  - 9.2.1. Nguyên tắc
  - 9.2.2. Sơ đồ tuần tự
- 9.3. Cơ sở dữ liệu cho thông báo
- 9.4. Socket.IO trong NestJS
  - 9.4.1. Cài đặt
  - 9.4.2. Gateway
  - 9.4.3. Gửi thông báo khi đổi trạng thái đơn
- 9.5. Phía ứng dụng
  - 9.5.1. Cài đặt
  - 9.5.2. Hook kết nối realtime
  - 9.5.3. Thông báo cục bộ và mở đúng màn hình
  - 9.5.4. Badge số thông báo chưa đọc
- 9.6. Trải nghiệm người dùng với thông báo
- 9.7. Mở rộng: push notification khi ứng dụng đã tắt
- 9.8. Checkpoint Sprint 3

**Thực hành:** câu hỏi ôn tập, bài tập cuối chương; bài tập hướng dẫn `bt-09`.
**Liên kết học liệu:** bài học `bai-09`, slide `Slides/bai-09.pptx`, quiz bài 09.
**Dung lượng ước tính:** khoảng 8 trang; tài liệu tham khảo: 7.

### Chương 10. Kiểm thử, gỡ lỗi và tối ưu hiệu năng

**Mục tiêu:**

- Thiết lập Jest và React Native Testing Library cho dự án Expo.
- Viết unit test cho logic nghiệp vụ, component test cho giao diện và mock API.
- Kiểm thử stored procedure bằng kịch bản T-SQL với giá trị hợp lệ, không hợp lệ và giá trị biên.
- Gỡ lỗi ứng dụng bằng React Native DevTools, log, request mạng và sự kiện socket; ghi bug log.
- Đo và cải thiện hiệu năng danh sách; bổ sung khả năng truy cập (accessibility).
- Kiểm chứng bộ test do trợ lý AI sinh ra bằng mutation thủ công.

**Nội dung:**

- 10.1. Kiểm thử trong một dự án di động
  - 10.1.1. Vì sao cần test tự động
  - 10.1.2. Các tầng kiểm thử
- 10.2. Thiết lập Jest cho dự án Expo
  - 10.2.1. Cài đặt
  - 10.2.2. Mock thư viện native
- 10.3. Unit test
  - 10.3.1. Cấu trúc một test
  - 10.3.2. Test store giỏ hàng
  - 10.3.3. Tách logic ra hàm thuần
- 10.4. Component test
  - 10.4.1. Nguyên tắc của React Native Testing Library
  - 10.4.2. Test `ProductCard`
  - 10.4.3. Mock API cho màn hình có gọi mạng
- 10.5. Kiểm thử stored procedure
  - 10.5.1. CSDL kiểm thử
  - 10.5.2. Thiết kế ca kiểm thử
  - 10.5.3. Kịch bản T-SQL
- 10.6. Gỡ lỗi
  - 10.6.1. Công cụ
  - 10.6.2. Gỡ lỗi mạng và socket
  - 10.6.3. Quy trình xử lý một lỗi
- 10.7. Tối ưu hiệu năng
  - 10.7.1. Ứng dụng chậm vì đâu
  - 10.7.2. Đo trước khi sửa
  - 10.7.3. `React.memo` và `useCallback`
  - 10.7.4. Tối ưu `FlatList`
  - 10.7.5. Ảnh
  - 10.7.6. Phía backend
- 10.8. Khả năng truy cập (accessibility)
- 10.9. Test do trợ lý AI sinh ra
  - 10.9.1. Lợi ích và rủi ro
  - 10.9.2. Mutation thủ công
- 10.10. Mã nguồn bổ sung của chương

**Thực hành:** câu hỏi ôn tập, bài tập cuối chương; bài tập hướng dẫn `bt-10`.
**Liên kết học liệu:** bài học `bai-10`, slide `Slides/bai-10.pptx`, quiz bài 10.
**Dung lượng ước tính:** khoảng 12 trang; tài liệu tham khảo: 11.

### Chương 11. Triển khai backend lên server Khoa, build và phát hành ứng dụng

**Mục tiêu:**

- Dựng CSDL SQL Server trên Windows Server của Khoa từ các script trong `database/` và cấu hình tài khoản chỉ có quyền `EXECUTE`.
- Triển khai backend NestJS (REST API và Socket.IO) thành dịch vụ chạy nền, kiểm tra được từ máy khác.
- Cấu hình ứng dụng Expo theo môi trường bằng `app.config.ts` và `eas.json`.
- Build file APK, AAB bằng EAS Build; phát hành bản cập nhật OTA bằng EAS Update.
- Chuẩn bị hồ sơ phát hành và theo dõi lỗi sau phát hành.

**Nội dung:**

- 11.1. Từ máy phát triển đến server
  - 11.1.1. Kiến trúc khi triển khai
  - 11.1.2. Thông tin cần có trước khi triển khai
- 11.2. Triển khai CSDL
  - 11.2.1. Dựng CSDL từ script
  - 11.2.2. Tài khoản cho backend
  - 11.2.3. Cập nhật CSDL sau lần triển khai đầu
- 11.3. Triển khai backend NestJS
  - 11.3.1. Build và cấu hình
  - 11.3.2. Chạy thử
  - 11.3.3. Chạy thành dịch vụ nền
  - 11.3.4. Mở cổng và kiểm tra từ máy khác
  - 11.3.5. Cập nhật phiên bản backend
  - 11.3.6. Ảnh tải lên
- 11.4. Cấu hình ứng dụng cho bản phát hành
  - 11.4.1. Từ `app.json` sang `app.config.ts`
  - 11.4.2. Địa chỉ API theo môi trường
  - 11.4.3. Kết nối HTTP không mã hóa
- 11.5. EAS Build
  - 11.5.1. Chuẩn bị
  - 11.5.2. Profile trong `eas.json`
  - 11.5.3. Build APK
  - 11.5.4. Ký ứng dụng
  - 11.5.5. Lượt build miễn phí
  - 11.5.6. iOS (phần mở rộng)
- 11.6. EAS Update
  - 11.6.1. Cập nhật qua mạng (OTA)
  - 11.6.2. Channel và runtime version
  - 11.6.3. Khi nào phải build lại
- 11.7. Hồ sơ phát hành
  - 11.7.1. Hồ sơ cửa hàng
  - 11.7.2. Chính sách quyền riêng tư
- 11.8. Vận hành sau phát hành
  - 11.8.1. Log phía backend
  - 11.8.2. Lỗi phía ứng dụng
  - 11.8.3. Quy trình khi người dùng báo lỗi
- 11.9. Mã nguồn và tài liệu bổ sung của chương

**Thực hành:** câu hỏi ôn tập, bài tập cuối chương; bài tập hướng dẫn `bt-11`.
**Liên kết học liệu:** bài học `bai-11`, slide `Slides/bai-11.pptx`, quiz bài 11.
**Dung lượng ước tính:** khoảng 14 trang; tài liệu tham khảo: 15.

### Chương 12. Báo cáo đồ án, Demo Day và tổng kết

**Mục tiêu:**

- Tổ chức báo cáo đồ án và bộ sơ đồ thiết kế đáp ứng rubric cuối kỳ theo từng CLO.
- Chuẩn bị và trình diễn sản phẩm trên thiết bị Android thật kết nối backend trên server Khoa.
- Bảo vệ thiết kế chức năng, thiết kế dữ liệu và giải thích được phần mã mình phụ trách.
- Viết báo cáo vai trò cá nhân có minh chứng.
- Đánh giá sản phẩm của nhóm khác theo rubric và rút kinh nghiệm về việc phát triển phần mềm cùng trợ lý AI.

**Nội dung:**

- 12.1. Đánh giá cuối kỳ
  - 12.1.1. Rubric theo CLO
  - 12.1.2. Đọc rubric như một danh sách kiểm tra
- 12.2. Báo cáo đồ án
  - 12.2.1. Cấu trúc đề xuất
  - 12.2.2. Viết phần thiết kế
  - 12.2.3. Phần kiểm thử và triển khai
  - 12.2.4. Phần sử dụng AI
- 12.3. Bộ sơ đồ thiết kế
  - 12.3.1. Bốn sơ đồ bắt buộc
  - 12.3.2. ERD phải khớp CSDL thật
  - 12.3.3. Sơ đồ đọc được trên máy chiếu
- 12.4. Chuẩn bị Demo Day
  - 12.4.1. Cấu trúc phần trình bày
  - 12.4.2. Kịch bản demo
  - 12.4.3. Kiểm tra trước giờ demo
  - 12.4.4. Phương án dự phòng
- 12.5. Bảo vệ thiết kế và bảo vệ kỹ thuật
  - 12.5.1. Bảo vệ thiết kế
  - 12.5.2. Bảo vệ kỹ thuật
- 12.6. Báo cáo vai trò cá nhân
- 12.7. Sản phẩm nộp cuối kỳ
- 12.8. Review chéo
- 12.9. Nhìn lại học phần
  - 12.9.1. Những gì đã xây dựng
  - 12.9.2. Phát triển phần mềm cùng AI
  - 12.9.3. Hướng phát triển tiếp

**Thực hành:** câu hỏi ôn tập, bài tập cuối chương; bài tập hướng dẫn `bt-12`.
**Liên kết học liệu:** bài học `bai-12`, slide `Slides/bai-12.pptx`, quiz bài 12.
**Dung lượng ước tính:** khoảng 13 trang; tài liệu tham khảo: 6.

## 5. Cân đối lý thuyết – thực hành

Ước tính theo số từ: phần lý thuyết và ví dụ khoảng 70%, phần câu hỏi, bài tập và bài tập hướng dẫn khoảng 30% (chưa tính mã nguồn ví dụ). Học phần 60 tiết (15 LT + 45 TH).

## 6. Tài liệu tham khảo chính

- Meta Platforms, Inc., “Introduction,” *React Native Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://reactnative.dev/docs/getting-started
- Meta Platforms, Inc., “Core Components and Native Components,” *React Native Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://reactnative.dev/docs/intro-react-native-components
- Expo, “Introduction to Expo,” *Expo Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://docs.expo.dev/get-started/introduction/
- Expo, “Introduction to development builds,” *Expo Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://docs.expo.dev/develop/development-builds/introduction/
- Meta Platforms, Inc., “Core Components and APIs,” *React Native Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://reactnative.dev/docs/components-and-apis
- Meta Platforms, Inc., “Layout with Flexbox,” *React Native Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://reactnative.dev/docs/flexbox
- Meta Platforms, Inc., “Style,” *React Native Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://reactnative.dev/docs/style
- Expo, “Safe areas,” *Expo Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://docs.expo.dev/develop/user-interface/safe-areas/
- Expo, “Introduction to Expo Router,” *Expo Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://docs.expo.dev/router/introduction/
- Expo, “Navigation layouts,” *Expo Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://docs.expo.dev/router/basics/layout/
- Expo, “Navigate between pages,” *Expo Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://docs.expo.dev/router/basics/navigation/
- Expo, “Linking overview,” *Expo Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://docs.expo.dev/linking/overview/
- Meta Platforms, Inc., “Choosing the State Structure,” *React Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://react.dev/learn/choosing-the-state-structure
- Poimandres, “Introduction,” *Zustand Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://zustand.docs.pmnd.rs
- Meta Platforms, Inc., “FlatList,” *React Native Documentation*. Accessed: Oct. 30, 2026. [Online]. Available: https://reactnative.dev/docs/flatlist
- … và 68 tài liệu khác, xem cuối mỗi chương.

## 7. Học liệu đi kèm

Xem mục "Học liệu đi kèm" trong Lời nói đầu.

## 8. Phân công và tiến độ

| Công việc | Người phụ trách | Thời hạn |
|---|---|---|
| Duyệt đề cương chi tiết | {{...}} | {{...}} |
| Rà soát bản thảo theo Điều 5 | {{...}} | {{...}} |
| Lấy ý kiến góp ý (phiếu 02) | {{...}} | {{...}} |
| Tiếp thu, hoàn thiện, lập hồ sơ thẩm định | {{...}} | {{...}} |
