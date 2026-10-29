# Dàn ý chi tiết - Lập trình ứng dụng di động (111114)

> **Trạng thái:** ĐÃ DUYỆT. Đã soạn đủ 4 giai đoạn: đề cương, đánh giá, bài 01–12 (bài học, slide, quiz).

- **Mã học phần:** 111114.
- **Giảng viên phụ trách:** ThS. Nguyễn Minh Phúc.
- **Giảng viên cùng tham gia:** Lê Minh Nhật, Lê Chân Thiện Tâm.
- **Thời lượng:** 60 tiết = **15 tiết lý thuyết + 45 tiết thực hành**, 12 buổi × 5 tiết.
- **Học kỳ:** 6, học song song với *Lập trình ứng dụng Web*.
- **Đối tượng:** sinh viên đã học Thiết kế UI/UX, Thiết kế Web (HTML/CSS/JS), Lập trình Frontend (React), Lập trình Backend (Node.js/NestJS, SQL Server).
- **Công nghệ chính:** React Native + Expo (Expo Router, TypeScript), TanStack Query, Zustand, React Hook Form + Zod, Expo SecureStore, Socket.IO, EAS Build.
- **Cơ sở dữ liệu:** **chỉ dùng Microsoft SQL Server**. Ứng dụng mobile **không có CSDL trên thiết bị**; trên máy chỉ lưu token (SecureStore) và vài thiết lập nhỏ/cache tạm (AsyncStorage).
- **Truy cập CSDL - BẮT BUỘC qua thủ tục lưu trữ (stored procedure):** backend Node.js/NestJS **chỉ được gọi stored procedure** (`EXEC`) với tham số; **không viết câu lệnh SQL trực tiếp trong mã nguồn backend và không dùng ORM để sinh truy vấn**. Thư viện bắt buộc: **`mssql`** (node-mssql) với `request.input(...)` và `request.execute('tên_thủ_tục')`. Mọi `SELECT/INSERT/UPDATE/DELETE`, giao dịch và báo cáo đều nằm trong thủ tục trên SQL Server.
- **Hạ tầng triển khai:** **Khoa cấp cho mỗi nhóm một Windows Server** để triển khai backend (API + Socket.IO) và SQL Server, có **bộ phận hỗ trợ của Khoa** hướng dẫn và hỗ trợ triển khai. Bản APK nộp cuối kỳ phải kết nối tới server này.
- **Build ứng dụng:** mỗi sinh viên **tự đăng ký tài khoản Expo miễn phí** để dùng EAS Build/Update. Gói miễn phí giới hạn số lượt build và có hàng chờ, nên trong quá trình phát triển dùng Expo Go/development build, chỉ build APK khi cần nộp hoặc kiểm thử trên máy khác.
- **Nền tảng:** **bắt buộc chạy được trên Android** (máy thật hoặc emulator). **iOS là phần mở rộng** (Expo Go/TestFlight nếu có thiết bị và tài khoản Apple Developer); làm được iOS thì có điểm cộng sáng tạo, không làm không bị trừ điểm.
- **Backend:** **mỗi nhóm tự xây REST API** bằng NestJS + SQL Server cho đề tài của mình. **Khuyến khích dùng chung đề tài và backend với học phần Lập trình ứng dụng Web**, để hai môn cùng phục vụ một sản phẩm.
- **Phương pháp:** PBL theo nhóm 4–5 sinh viên, 4 sprint × 3 buổi, kết hợp **vibe coding** với **Google Antigravity** và **GitHub Copilot Chat**. AI được dùng để sinh mã; sinh viên chịu trách nhiệm hiểu, kiểm tra và giải thích được mã đó.
- **Ví dụ xuyên suốt cho phần thực hành có hướng dẫn:** **LHU Food**, ứng dụng đặt món căn tin (danh sách món, chi tiết, giỏ hàng, đăng nhập, đặt hàng, theo dõi đơn, thông báo thời gian thực). Giảng viên làm mẫu **cả app mobile và API NestJS** của LHU Food; sinh viên áp dụng vào dự án của nhóm.
- **Nguồn tham khảo đề xuất:** tài liệu chính thức React Native (reactnative.dev), Expo (docs.expo.dev), NestJS (docs.nestjs.com, gồm phần WebSockets/Gateways), Socket.IO, TanStack Query. ⚠️ Giảng viên xác nhận giáo trình/tài liệu nội bộ nếu có.

---

## Chuẩn đầu ra học phần (CLO)

| CLO | Mô tả | PLO / PI | Trọng số | Ngưỡng đạt | Đánh giá tại |
|---|---|---|:---:|:---:|---|
| **CLO1** | Thiết kế các thành phần chức năng của ứng dụng di động đáp ứng các yêu cầu đặt ra | PLO2 / PI 2.4: Phân tích thiết kế các thành phần chức năng của hệ thống thông tin dựa trên các giao diện và yêu cầu chức năng của hệ thống | 3 | 75% | Cuối kỳ |
| **CLO2** | Thiết kế cơ sở dữ liệu đáp ứng cấu trúc dữ liệu phù hợp yêu cầu đặc tả | PLO2 / PI 2.5: Có khả năng thiết kế được Database để quản lý hệ thống thông tin | 2 | 75% | Cuối kỳ |
| **CLO3** | Sử dụng được các công cụ đồ họa để trình bày các ý tưởng thiết kế dữ liệu | PLO3 / PI 3.4: Biết cách sử dụng đồ họa để trình bày các ý tưởng | 2 | 75% | Cuối kỳ|
| **CLO4** | Thể hiện được vai trò cá nhân trong nhóm một cách rõ ràng | PLO5 / PI 5.2: Thể hiện được vai trò cá nhân trong nhóm một cách rõ ràng | 3 | 75% | Cuối kỳ |

**Cách hiểu trọng số và ngưỡng đạt:**
- **Trọng số** là điểm tối đa của CLO trong bài đánh giá cuối kỳ. Tổng 3 + 2 + 2 + 3 = **10 điểm**, tức đồ án cuối kỳ được chấm theo thang 10 và tách điểm theo CLO.
- **Một sinh viên đạt CLO** khi được **≥ 50% điểm trọng số** của CLO đó: CLO1 ≥ 1,5/3; CLO2 ≥ 1/2; CLO3 ≥ 1/2; CLO4 ≥ 1,5/3.
- **Ngưỡng đạt 75%** là chỉ tiêu của lớp: CLO được xem là đạt khi **ít nhất 75% số sinh viên** đạt CLO đó.

**Ghi chú thiết kế:** CLO2 và CLO3 yêu cầu sinh viên **thiết kế CSDL** và **trình bày thiết kế dữ liệu bằng công cụ đồ họa**. Vì vậy dàn ý có các sản phẩm bắt buộc: sơ đồ chức năng/luồng màn hình, **ERD trên SQL Server** (sơ bộ → hoàn chỉnh → phiên bản cuối), sơ đồ tuần tự luồng dữ liệu realtime. Nhóm dùng công cụ như draw.io, dbdiagram.io hoặc Figma (FigJam).

## Đánh giá

| Thành phần | Tỷ trọng | Nội dung |
|---|:---:|---|
| **Quá trình** | 30% | Chuyên cần, quiz từng bài, `PROMPTS.md`, các sơ đồ thiết kế nộp theo sprint, tham gia review chéo |
| **Thực hành** | 30% | Bài thực hành không hướng dẫn của từng buổi; checkpoint các sprint (buổi 03, 06, 09) |
| **Cuối kỳ: đồ án nhóm** | 40% | Sản phẩm cuối, báo cáo, Demo Day; **chấm thang 10 và tách điểm theo 4 CLO** (bảng dưới) |

Quá trình và thực hành là hoạt động **hình thành** để sinh viên luyện tập các CLO; việc **đo mức đạt CLO** thực hiện ở bài đánh giá cuối kỳ, theo bảng CLO ở trên.

**Rubric cuối kỳ theo CLO (thang 10):**

| CLO | Điểm tối đa | Minh chứng chấm | Đạt khi |
|---|:---:|---|:---:|
| **CLO1** | 3 | Sơ đồ chức năng và các thành phần của app đáp ứng đặc tả; luồng nghiệp vụ chính, xác thực, tính năng thiết bị và thông báo realtime chạy được trên Android | ≥ 1,5 |
| **CLO2** | 2 | CSDL SQL Server của nhóm: bảng, khóa, quan hệ, ràng buộc; **bộ stored procedure** phục vụ toàn bộ nghiệp vụ (tham số hóa, có giao dịch và xử lý lỗi cho nghiệp vụ chính); script tạo CSDL, thủ tục và dữ liệu mẫu chạy được trên server Khoa | ≥ 1 |
| **CLO3** | 2 | Bộ sơ đồ trình bày thiết kế dữ liệu (ERD phiên bản cuối, sơ đồ tuần tự realtime, luồng màn hình) trong báo cáo và slide; rõ ràng, nhất quán với CSDL thật | ≥ 1 |
| **CLO4** | 3 | Báo cáo vai trò cá nhân, lịch sử commit/PR, phần tự trình bày và trả lời câu hỏi kỹ thuật của từng thành viên ở Demo Day | ≥ 1,5 |

---

## Cấu trúc mỗi buổi (5 tiết)

Phân bổ lý thuyết: buổi 01, 05, 06, 10 có **2 tiết LT**; buổi 02, 03, 04, 07, 08, 09, 11 có **1 tiết LT**; buổi 12 là Demo Day. Tổng **15 tiết LT + 45 tiết TH**.

| Phần | Buổi 1 tiết LT | Buổi 2 tiết LT | Hình thức |
|---|:---:|:---:|---|
| **Lý thuyết** | 1 tiết | 2 tiết | Giảng ngắn, demo trực tiếp, câu hỏi dẫn nhập |
| **Thực hành có hướng dẫn** | 2 tiết | 1,5 tiết | Làm theo giảng viên trên LHU Food (code-along, cả mobile và API) |
| **Thực hành không hướng dẫn** | 1,5 tiết | 1 tiết | Cá nhân tự làm bài tương tự, chỉ có đặc tả và tiêu chí hoàn thành |
| **Thử thách nhóm (PBL)** | 0,5 tiết + ở nhà | 0,5 tiết + ở nhà | Nhiệm vụ sprint của dự án nhóm, nộp qua GitHub (Pull Request) |

**Quy tắc vibe coding áp dụng mọi buổi:**
1. Được dùng **Google Antigravity** và **GitHub Copilot Chat** để sinh mã, nhưng **mỗi Pull Request phải kèm prompt chính đã dùng** (ghi trong `PROMPTS.md` hoặc phần mô tả PR).
2. **Không hiểu thì không merge:** người tạo PR phải giải thích được mọi đoạn mã khi giảng viên hoặc bạn cùng nhóm hỏi.
3. Mỗi nhóm có file quy ước dự án cho AI: `AGENTS.md` (kiến trúc, quy tắc đặt tên, thư viện được dùng) và `.github/copilot-instructions.md` cho GitHub Copilot, để AI sinh mã nhất quán.
4. Commit nhỏ, thông điệp rõ ràng; mỗi tính năng một nhánh; review chéo trước khi merge. Lịch sử commit/PR là căn cứ đánh giá vai trò cá nhân (CLO4).

---

## Lộ trình PBL: 4 sprint

| Sprint | Buổi | Mục tiêu sản phẩm | Sản phẩm thiết kế bắt buộc | Checkpoint |
|---|---|---|---|---|
| **Sprint 1: Nền tảng & Giao diện** | 01–03 | Dự án khởi tạo, UI các màn hình chính, điều hướng hoàn chỉnh (dữ liệu giả) | Sơ đồ chức năng, sơ đồ luồng màn hình, ERD sơ bộ | Buổi 03: demo khung ứng dụng trên Android |
| **Sprint 2: Dữ liệu & Người dùng** | 04–06 | CSDL + stored procedure + API NestJS của nhóm, form, kết nối API, đăng nhập/phân quyền | ERD hoàn chỉnh (SQL Server), danh mục stored procedure, tài liệu API (Swagger) | Buổi 06: demo luồng nghiệp vụ chính + bản nháp báo cáo vai trò cá nhân |
| **Sprint 3: Dữ liệu nâng cao, Thiết bị & Realtime** | 07–09 | Nghiệp vụ dữ liệu trên SQL Server (giao dịch, thống kê), camera/ảnh, vị trí, **thông báo realtime bằng Socket.IO** | ERD phiên bản cuối + script CSDL, sơ đồ tuần tự realtime | Buổi 09: demo tính năng native và realtime trên máy thật |
| **Sprint 4: Chất lượng & Phát hành** | 10–12 | Kiểm thử, tối ưu, **triển khai backend + SQL Server lên server Khoa**, build APK, báo cáo và Demo Day | Bộ sơ đồ thiết kế hoàn chỉnh trong báo cáo | Buổi 12: **cuối kỳ**, Demo Day |

---

## Bài 01 - Tổng quan phát triển ứng dụng di động & khởi động dự án (5 tiết: 2 LT / 3 TH)
- **CLO liên quan:** CLO1, CLO4
- **Mục tiêu (Bloom):** So sánh được các hướng phát triển mobile (native, cross-platform, PWA); giải thích được kiến trúc React Native và vai trò của Expo; thiết lập được môi trường, quy trình vibe coding và phân vai trong nhóm.
- **Ý chính:**
  1. Native, cross-platform, PWA: ưu nhược điểm; vì sao chọn React Native khi đã biết React. Ví dụ: cùng component `ProductCard` trên web và mobile khác nhau ở đâu.
  2. Kiến trúc React Native (JS thread, native components, New Architecture) và Expo (Expo Go, development build, EAS); Android là nền tảng bắt buộc, iOS là phần mở rộng.
  3. Từ React web sang React Native: `View`/`Text` thay `div`/`span`, không có DOM và file CSS, `StyleSheet`, sự kiện chạm.
  4. Quy trình vibe coding với Google Antigravity và GitHub Copilot Chat: viết `AGENTS.md`, prompt có ngữ cảnh, review mã AI sinh ra, ghi `PROMPTS.md`.
- **Thực hành có hướng dẫn:** cài Node, Expo CLI, Android Studio emulator / Expo Go; mỗi sinh viên đăng ký tài khoản Expo miễn phí; tạo dự án `lhu-food` bằng `create-expo-app` (TypeScript); chạy trên điện thoại Android; đọc cấu trúc thư mục; tạo repo GitHub, viết `AGENTS.md` đầu tiên bằng Antigravity, commit đầu tiên.
- **Thực hành không hướng dẫn:** tự tạo ứng dụng "Thẻ giới thiệu bản thân" (ảnh đại diện, tên, kỹ năng, nút liên hệ) chạy được trên máy Android; đẩy lên GitHub cá nhân.
- **Thử thách nhóm:** lập nhóm, chọn đề tài (khuyến khích dùng chung với môn Lập trình ứng dụng Web), viết **Project Brief 1 trang** (vấn đề, người dùng, 5–7 tính năng chính), **bảng phân vai** (mỗi thành viên ít nhất 1 vai chính: mobile UI, mobile logic, backend API, CSDL, kiểm thử/phát hành), tạo repo nhóm.
- **Slide dự kiến:** khoảng 18 slide.

## Bài 02 - Core Components, Styling & Layout với Flexbox (5 tiết: 1 LT / 4 TH)
- **CLO liên quan:** CLO1, CLO3
- **Mục tiêu (Bloom):** Sử dụng được các core component; xây dựng được giao diện responsive bằng Flexbox; chuyển được thiết kế Figma thành component tái sử dụng; trình bày được sơ đồ chức năng của ứng dụng bằng công cụ đồ họa.
- **Ý chính:**
  1. Core components: `View`, `Text`, `Image`, `ScrollView`, `TextInput`, `Pressable`, `SafeAreaView`. Ví dụ: màn hình chi tiết món ăn.
  2. Flexbox trong React Native (mặc định `flexDirection: column`), kích thước, `useWindowDimensions`, safe area, tai thỏ.
  3. Design system: màu, font, spacing tập trung trong `theme.ts`; component dùng chung `Button`, `Card`, `Input`; dark mode.
  4. Vibe coding từ thiết kế: đưa ảnh chụp Figma + đặc tả cho Antigravity/Copilot để sinh component, so sánh với thiết kế và sửa.
- **Thực hành có hướng dẫn:** dựng màn hình Trang chủ và Chi tiết món của LHU Food từ file Figma mẫu; tách `theme.ts` và 3 component dùng chung; vẽ **sơ đồ chức năng** LHU Food bằng draw.io.
- **Thực hành không hướng dẫn:** dựng màn hình Hồ sơ người dùng theo ảnh thiết kế cho trước; đạt yêu cầu khi hiển thị đúng trên 2 kích thước màn hình Android (nhỏ và lớn).
- **Thử thách nhóm:** UI kit của nhóm (theme + tối thiểu 5 component dùng chung), giao diện tĩnh của 3 màn hình chính (bám theo Figma ở môn UI/UX) và **sơ đồ chức năng** của đề tài.
- **Slide dự kiến:** khoảng 16 slide.

## Bài 03 - Điều hướng với Expo Router (5 tiết: 1 LT / 4 TH)
- **CLO liên quan:** CLO1, CLO2, CLO3
- **Mục tiêu (Bloom):** Giải thích được mô hình điều hướng trên mobile (stack, tab, modal); xây dựng được điều hướng theo file bằng Expo Router; phác thảo được ERD sơ bộ từ các màn hình và chức năng.
- **Ý chính:**
  1. Điều hướng trên mobile khác web: stack lịch sử, nút Back của Android, cử chỉ vuốt.
  2. Expo Router: file-based routing, `_layout.tsx`, Stack, Tabs, nhóm route `(tabs)`, `(auth)`.
  3. Route động `[id].tsx`, truyền và đọc tham số, modal, chuyển màn hình bằng mã; deep link cơ bản (`lhufood://product/12`).
  4. Từ màn hình đến dữ liệu: mỗi màn hình cần những thực thể nào, từ đó phác ERD sơ bộ (Món, Danh mục, Người dùng, Đơn hàng, Chi tiết đơn).
- **Thực hành có hướng dẫn:** LHU Food có thanh tab (Trang chủ, Giỏ hàng, Đơn hàng, Tài khoản), stack Danh sách → Chi tiết món, modal xác nhận; vẽ **sơ đồ luồng màn hình** và **ERD sơ bộ** của LHU Food.
- **Thực hành không hướng dẫn:** thêm luồng "Danh mục → Danh sách món theo danh mục → Chi tiết" dùng route động; nút Back của Android hoạt động đúng.
- **Thử thách nhóm (Checkpoint Sprint 1):** khung ứng dụng đủ điều hướng với dữ liệu giả (mock JSON); nộp sơ đồ luồng màn hình và ERD sơ bộ; demo 3 phút trên Android; Sprint Review và Retrospective ngắn.
- **Slide dự kiến:** khoảng 15 slide.

## Bài 04 - Quản lý trạng thái, danh sách & form (5 tiết: 1 LT / 4 TH)
- **CLO liên quan:** CLO1
- **Mục tiêu (Bloom):** Phân biệt được trạng thái cục bộ, toàn cục và trạng thái từ server; hiển thị được danh sách lớn hiệu quả; xây dựng được form có kiểm tra dữ liệu.
- **Ý chính:**
  1. `useState`/`useReducer` và trạng thái toàn cục với Zustand (hoặc Context). Ví dụ: giỏ hàng dùng ở nhiều màn hình.
  2. `FlatList`/`SectionList`: `keyExtractor`, `renderItem`, danh sách rỗng, pull-to-refresh, vì sao không dùng `map` trong `ScrollView` cho danh sách dài.
  3. Form với React Hook Form + Zod: validate, thông báo lỗi, bàn phím (`KeyboardAvoidingView`, loại bàn phím).
  4. Vibe coding: yêu cầu Copilot sinh schema Zod từ đặc tả nghiệp vụ, rồi tự viết test case biên để kiểm tra lại schema.
- **Thực hành có hướng dẫn:** giỏ hàng LHU Food với Zustand (thêm, bớt, tổng tiền); danh sách món dùng `FlatList`; form ghi chú đơn hàng có validate.
- **Thực hành không hướng dẫn:** form Đăng ký tài khoản (họ tên, email, số điện thoại, mật khẩu, xác nhận mật khẩu) với đầy đủ quy tắc validate và thông báo lỗi tiếng Việt.
- **Thử thách nhóm:** store toàn cục cho nghiệp vụ chính và tối thiểu 1 form nghiệp vụ có validate; **thành viên phụ trách backend khởi tạo dự án NestJS, kết nối SQL Server bằng `mssql`** và tạo các bảng theo ERD sơ bộ.
- **Slide dự kiến:** khoảng 16 slide.

## Bài 05 - Thiết kế CSDL, stored procedure, API NestJS & kết nối ứng dụng (5 tiết: 2 LT / 3 TH)
- **CLO liên quan:** CLO1, CLO2, CLO3
- **Mục tiêu (Bloom):** Thiết kế được CSDL SQL Server đáp ứng đặc tả và trình bày bằng ERD; viết được stored procedure cho các thao tác dữ liệu; xây dựng được REST API NestJS chỉ truy cập CSDL qua stored procedure; tích hợp và quản lý được dữ liệu server trong app.
- **Ý chính:**
  1. Hoàn thiện thiết kế CSDL: khóa chính/ngoại, quan hệ 1-n, n-n, chuẩn hóa vừa đủ, dữ liệu mẫu; trình bày ERD bằng dbdiagram.io/draw.io.
  2. Stored procedure: quy ước đặt tên (ví dụ `sp_Product_GetList`, `sp_Product_GetById`, `sp_Order_Create`), tham số vào/ra, phân trang bằng `OFFSET/FETCH`, trả mã lỗi bằng `THROW`. Vì sao bắt buộc dùng thủ tục: tách logic dữ liệu khỏi mã nguồn, phân quyền chỉ `EXECUTE`, chống SQL injection. Vibe coding: dùng Antigravity sinh thủ tục từ ERD, sau đó review từng thủ tục và chạy thử trong SSMS.
  3. API NestJS cho mobile: module, controller, service, DTO + validation, Swagger; lớp `DatabaseService` dùng chung để gọi `request.execute()` với tham số có kiểu (`sql.Int`, `sql.NVarChar`…).
  4. Gọi API từ mobile: lớp `api client` tập trung, biến môi trường `EXPO_PUBLIC_API_URL`; lỗi hay gặp: điện thoại không gọi được `localhost` (dùng IP LAN / `10.0.2.2` cho emulator), HTTP trên Android. TanStack Query: `useQuery`, `useMutation`, cache, invalidate, trạng thái loading/error/empty, infinite scroll.
- **Thực hành có hướng dẫn:** cùng giảng viên viết các stored procedure của LHU Food (Products, Categories, Orders) và dựng API NestJS gọi các thủ tục đó; app LHU Food lấy danh sách/chi tiết món từ API, đặt hàng bằng `useMutation`, kéo để tải lại.
- **Thực hành không hướng dẫn:** viết thủ tục `sp_Order_GetHistory` có phân trang, endpoint tương ứng ở API và màn hình infinite scroll trong app.
- **Thử thách nhóm:** **ERD hoàn chỉnh** (nộp file ảnh + file nguồn), **danh mục stored procedure** (tên, tham số, kết quả trả về) và script tạo thủ tục, API của nhóm với Swagger; thay toàn bộ dữ liệu giả trong app bằng API thật.
- **Slide dự kiến:** khoảng 20 slide.

## Bài 06 - Xác thực & bảo mật ứng dụng (5 tiết: 2 LT / 3 TH)
- **CLO liên quan:** CLO1, CLO4
- **Mục tiêu (Bloom):** Triển khai được đăng ký/đăng nhập bằng JWT ở cả API và app; lưu trữ token an toàn; bảo vệ được màn hình theo trạng thái đăng nhập và vai trò.
- **Ý chính:**
  1. Luồng xác thực JWT giữa app và NestJS: Passport/JWT Guard, access token, refresh token, hết hạn, mã hóa mật khẩu (bcrypt) ở backend; lưu và kiểm tra tài khoản qua thủ tục (`sp_User_Register`, `sp_User_GetByEmail`, lưu refresh token bằng thủ tục).
  2. Lưu token đúng chỗ: Expo SecureStore và AsyncStorage, vì sao không lưu mật khẩu.
  3. Bảo vệ route: nhóm `(auth)`/`(app)` trong Expo Router, chuyển hướng khi chưa đăng nhập, phân quyền khách hàng/nhân viên căn tin ở cả app và API (Roles Guard).
  4. Rủi ro bảo mật trên mobile: lộ khóa bí mật trong bundle, log nhạy cảm, chỉ kiểm tra quyền ở app mà không kiểm tra ở server. Review bảo mật cho mã AI sinh ra; tài khoản SQL Server của API chỉ có quyền `EXECUTE` trên các thủ tục, không có quyền truy cập trực tiếp vào bảng.
- **Thực hành có hướng dẫn:** LHU Food có đăng ký/đăng nhập (API + app), lưu token bằng SecureStore, tự gắn token vào request, đăng xuất, tự đăng nhập lại khi mở app.
- **Thực hành không hướng dẫn:** xử lý token hết hạn: gọi refresh token, hoặc chuyển về màn hình đăng nhập kèm thông báo.
- **Thử thách nhóm (Checkpoint Sprint 2):** luồng nghiệp vụ chính chạy với dữ liệu thật và đăng nhập; demo + Sprint Review. **Mỗi thành viên nộp bản nháp báo cáo vai trò cá nhân** (1 trang: nhiệm vụ đảm nhận, PR/commit tiêu biểu, khó khăn đã giải quyết) và **tự trình bày 2 phút** phần mình làm; giảng viên góp ý để hoàn thiện cho cuối kỳ (CLO4).
- **Slide dự kiến:** khoảng 18 slide.

## Bài 07 - CSDL SQL Server nâng cao & đồng bộ dữ liệu qua backend (5 tiết: 1 LT / 4 TH)
- **CLO liên quan:** CLO1, CLO2, CLO3
- **Mục tiêu (Bloom):** Hoàn thiện được thiết kế CSDL SQL Server cho nghiệp vụ thực tế (ràng buộc, chỉ mục); viết được stored procedure có giao dịch và xử lý lỗi cho nghiệp vụ nhiều bảng và báo cáo thống kê; đồng bộ được dữ liệu giữa app và server mà không lưu CSDL trên thiết bị.
- **Ý chính:**
  1. Toàn vẹn dữ liệu trên SQL Server: ràng buộc `CHECK`/`UNIQUE`/khóa ngoại, giá trị mặc định, chỉ mục cho các truy vấn app gọi nhiều. Ví dụ: không cho số lượng món âm, mỗi người chỉ có một giỏ hàng đang mở.
  2. Giao dịch trong stored procedure: `sp_Order_Create` tạo `Orders` + `OrderItems` + trừ tồn kho trong `BEGIN TRAN ... COMMIT`, dùng `TRY...CATCH` để `ROLLBACK` và `THROW` mã lỗi khi một bước thất bại; truyền danh sách món bằng tham số kiểu bảng (table-valued parameter) hoặc JSON (`OPENJSON`). Backend chỉ gọi một thủ tục và chuyển mã lỗi thành thông báo cho app.
  3. Thủ tục báo cáo: `sp_Report_RevenueByDay`, `sp_Report_TopProducts` (có thể đọc từ view bên trong thủ tục) và endpoint thống kê cho vai trò nhân viên; script tạo CSDL + thủ tục + dữ liệu mẫu đánh số phiên bản để cả nhóm có cùng CSDL.
  4. Đồng bộ app với server: dữ liệu luôn lấy từ API; optimistic update với TanStack Query; giữ giỏ hàng và cache tạm bằng AsyncStorage để mở lại app vẫn thấy, nhưng nguồn dữ liệu chuẩn là SQL Server.
- **Thực hành có hướng dẫn:** viết `sp_Order_Create` có giao dịch cho LHU Food (cố ý làm lỗi giữa chừng để thấy rollback và mã lỗi trả về app); viết thủ tục và endpoint "Thống kê doanh thu", màn hình thống kê cho nhân viên căn tin; cập nhật ERD.
- **Thực hành không hướng dẫn:** tính năng "Món yêu thích": thiết kế bảng `Favorites` (quan hệ n-n giữa người dùng và món, có ràng buộc không trùng), viết các thủ tục thêm/xóa/danh sách, API gọi thủ tục, màn hình trong app với optimistic update.
- **Thử thách nhóm:** rà soát và hoàn thiện CSDL của nhóm (ràng buộc, chỉ mục, thủ tục có giao dịch cho nghiệp vụ chính, 1 thủ tục báo cáo); kiểm tra **không còn câu SQL trực tiếp** trong mã backend; nộp **ERD phiên bản cuối** và **script tạo CSDL + thủ tục + dữ liệu mẫu** trong repo.
- **Slide dự kiến:** khoảng 16 slide.

## Bài 08 - Tính năng thiết bị: Camera, Ảnh, Vị trí & Bản đồ (5 tiết: 1 LT / 4 TH)
- **CLO liên quan:** CLO1
- **Mục tiêu (Bloom):** Xin và xử lý được quyền truy cập thiết bị; tích hợp được camera, thư viện ảnh và vị trí; tải được ảnh lên API NestJS.
- **Ý chính:**
  1. Mô hình quyền (permission) trên Android (và iOS ở phần mở rộng); xin quyền đúng thời điểm và xử lý khi người dùng từ chối.
  2. `expo-image-picker`/`expo-camera`: chụp, chọn, nén ảnh; upload multipart lên NestJS (Multer), lưu đường dẫn ảnh vào SQL Server qua thủ tục.
  3. `expo-location` và bản đồ (`react-native-maps`): vị trí hiện tại, hiển thị điểm, tính khoảng cách.
  4. Expo Go và development build: khi nào bắt buộc phải dùng development build cho thư viện native.
- **Thực hành có hướng dẫn:** LHU Food đổi ảnh đại diện bằng camera/thư viện và upload lên API; bản đồ các quầy căn tin trong khuôn viên.
- **Thực hành không hướng dẫn:** chức năng "Báo cáo sự cố": chụp ảnh, tự lấy vị trí, nhập mô tả, gửi lên API; xử lý đủ trường hợp từ chối quyền.
- **Thử thách nhóm:** tích hợp tối thiểu **1 tính năng thiết bị** có ý nghĩa với nghiệp vụ của nhóm (không làm cho có).
- **Slide dự kiến:** khoảng 15 slide.

## Bài 09 - Thông báo thời gian thực với Socket.IO (BẮT BUỘC) (5 tiết: 1 LT / 4 TH)
- **CLO liên quan:** CLO1, CLO3
- **Mục tiêu (Bloom):** Giải thích được cơ chế giao tiếp thời gian thực (WebSocket/Socket.IO) và so sánh với polling; xây dựng được thông báo realtime từ NestJS tới ứng dụng; trình bày được luồng dữ liệu realtime bằng sơ đồ.
- **Ý chính:**
  1. WebSocket, Socket.IO và polling: khi nào cần realtime; kết nối, sự kiện, room; vẽ **sơ đồ tuần tự (sequence diagram)** luồng thông báo.
  2. NestJS Gateway (`@WebSocketGateway`): xác thực kết nối bằng JWT, phát sự kiện theo room (theo người dùng, theo vai trò), lưu lịch sử thông báo và trạng thái đã đọc vào SQL Server qua thủ tục (`sp_Notification_Create`, `sp_Notification_MarkRead`).
  3. Phía app: `socket.io-client`, kết nối/ngắt/kết nối lại theo vòng đời app và trạng thái mạng, cập nhật cache TanStack Query khi nhận sự kiện.
  4. Hiển thị thông báo: banner trong app, badge số thông báo chưa đọc, thông báo cục bộ bằng `expo-notifications` khi nhận sự kiện; không spam, cho phép tắt. *Mở rộng:* Expo Push Notification để nhận thông báo khi app đã tắt.
- **Thực hành có hướng dẫn:** khi nhân viên căn tin đổi trạng thái đơn (đang làm → sẵn sàng), API phát sự kiện Socket.IO tới đúng người đặt; app LHU Food hiện thông báo, cập nhật màn hình đơn hàng ngay lập tức, bấm thông báo mở chi tiết đơn.
- **Thực hành không hướng dẫn:** màn hình "Thông báo" có danh sách lịch sử (lấy từ API), đánh dấu đã đọc, badge chưa đọc cập nhật realtime, và cài đặt bật/tắt thông báo.
- **Thử thách nhóm (Checkpoint Sprint 3):** **bắt buộc** có ít nhất 1 luồng thông báo realtime bằng Socket.IO phù hợp nghiệp vụ; nộp sơ đồ tuần tự luồng realtime; demo tính năng native và realtime trên Android; cập nhật backlog cho sprint cuối.
- **Slide dự kiến:** khoảng 16 slide.

## Bài 10 - Kiểm thử, gỡ lỗi & tối ưu hiệu năng (5 tiết: 2 LT / 3 TH)
- **CLO liên quan:** CLO1
- **Mục tiêu (Bloom):** Viết được unit test và component test cho ứng dụng; sử dụng được công cụ gỡ lỗi; đánh giá và cải thiện được hiệu năng, khả năng truy cập.
- **Ý chính:**
  1. Jest + React Native Testing Library: test hàm nghiệp vụ, test component, mock API và mock socket; kiểm thử stored procedure bằng script T-SQL (gọi thủ tục với dữ liệu hợp lệ, không hợp lệ, biên và kiểm tra kết quả/mã lỗi).
  2. Gỡ lỗi: React Native DevTools, log, xem request mạng và sự kiện socket, đọc stack trace; quy trình tái hiện lỗi (liên hệ học phần Kiểm thử phần mềm).
  3. Hiệu năng: re-render thừa (`memo`, `useCallback`), tối ưu `FlatList`, ảnh, kích thước bundle; chỉ số đo trên máy Android tầm trung.
  4. Accessibility: `accessibilityLabel`, cỡ chữ hệ thống, độ tương phản. Dùng Copilot sinh test, nhưng con người kiểm tra test có thực sự bắt được lỗi.
- **Thực hành có hướng dẫn:** viết test cho giỏ hàng (tính tổng tiền, xóa món) và component `ProductCard`; tìm và sửa một lỗi re-render trong danh sách món.
- **Thực hành không hướng dẫn:** đạt tối thiểu 5 test pass cho một module tự chọn; dùng kỹ thuật **mutation thủ công** (cố ý sửa sai logic) để chứng minh test bắt được lỗi.
- **Thử thách nhóm:** bộ test cho các luồng chính, danh sách lỗi đã sửa (bug log), 1 cải tiến hiệu năng có số liệu trước/sau.
- **Slide dự kiến:** khoảng 18 slide.

## Bài 11 - Triển khai backend lên server Khoa, build & phát hành ứng dụng (5 tiết: 1 LT / 4 TH)
- **CLO liên quan:** CLO1, CLO2
- **Mục tiêu (Bloom):** Triển khai được backend (API + Socket.IO) và CSDL SQL Server lên server do Khoa cấp; cấu hình được ứng dụng để phát hành; build được bản cài đặt Android bằng EAS Build kết nối tới server thật.
- **Ý chính:**
  1. Triển khai lên Windows Server của Khoa (cùng bộ phận hỗ trợ): chạy script tạo CSDL + stored procedure + dữ liệu mẫu trên SQL Server, tạo tài khoản SQL Server chỉ có quyền `EXECUTE`, cấu hình biến môi trường (`.env`), chạy API Node.js như dịch vụ nền của Windows theo hướng dẫn của bộ phận hỗ trợ, mở cổng cho API và socket trên Windows Firewall, kiểm tra bằng Swagger từ máy khác.
  2. Cấu hình `app.json`/`app.config.ts`: tên, icon, splash screen, package name, version/versionCode, địa chỉ API và socket theo môi trường (dev trỏ máy cá nhân, production trỏ server Khoa).
  3. EAS Build với tài khoản Expo miễn phí của sinh viên: profile `preview` (APK cài thử, **bắt buộc**) và `production` (AAB); ký ứng dụng; quản lý lượt build có hạn (build ít lần, kiểm tra kỹ trước khi build); EAS Update (OTA) cho thay đổi không cần build lại. *Mở rộng iOS:* build và cài qua TestFlight nếu nhóm có tài khoản Apple Developer.
  4. Đưa lên cửa hàng và vận hành: yêu cầu của Google Play (chính sách quyền riêng tư, ảnh chụp màn hình, mô tả); xem log server và theo dõi lỗi sau phát hành.
- **Thực hành có hướng dẫn:** triển khai API LHU Food và CSDL lên Windows Server mẫu, build APK trỏ tới server đó, cài lên điện thoại Android và đặt hàng thử qua mạng; đổi một nội dung và phát hành bằng EAS Update.
- **Thực hành không hướng dẫn:** chuẩn bị bộ "store listing" cho LHU Food: icon, 4 ảnh chụp màn hình, mô tả ngắn/dài, chính sách quyền riêng tư.
- **Thử thách nhóm:** cùng bộ phận hỗ trợ triển khai backend + SQL Server của nhóm lên **Windows Server Khoa cấp**; APK của nhóm cài và chạy được trên máy Android của người không thuộc nhóm (kết nối được API và socket trên server Khoa); hoàn thiện README (hướng dẫn triển khai trên Windows Server), store listing và bản nháp báo cáo; *mở rộng:* chạy được trên iOS.
- **Slide dự kiến:** khoảng 16 slide.
- **Chuẩn bị trước buổi học:** mỗi sinh viên đã đăng ký tài khoản Expo; nhóm đã nhận thông tin truy cập server từ bộ phận hỗ trợ của Khoa.

## Bài 12 - Demo Day: báo cáo đồ án & tổng kết (5 tiết: 0 LT / 5 TH)
- **CLO liên quan:** CLO1, CLO2, CLO3, CLO4 (đánh giá cuối kỳ)
- **Mục tiêu (Bloom):** Trình bày và bảo vệ được thiết kế thành phần chức năng và thiết kế CSDL của sản phẩm; đánh giá được sản phẩm của nhóm mình và nhóm khác; rút ra được bài học về làm việc nhóm và sử dụng AI có trách nhiệm.
- **Ý chính:**
  1. Demo sản phẩm trên thiết bị Android thật, kết nối backend trên server Khoa: luồng chính, tính năng thiết bị, dữ liệu đồng bộ với SQL Server, thông báo realtime.
  2. Bảo vệ thiết kế: sơ đồ chức năng, ERD phiên bản cuối và CSDL SQL Server thật, sơ đồ tuần tự realtime; giải thích lựa chọn thiết kế.
  3. Bảo vệ kỹ thuật: giảng viên chọn ngẫu nhiên một đoạn mã, thành viên được hỏi phải giải thích (kiểm chứng nguyên tắc "không hiểu thì không merge").
  4. Phản biện chéo giữa các nhóm theo rubric; retrospective toàn khóa: AI giúp gì, AI gây lỗi gì, lần sau làm khác ra sao.
- **Hoạt động:** mỗi nhóm trình bày 10 phút + hỏi đáp 5 phút (mỗi thành viên tự trình bày phần mình phụ trách); các nhóm chấm chéo theo rubric; nộp báo cáo cuối kỳ, bộ sơ đồ thiết kế, script CSDL + stored procedure SQL Server, báo cáo vai trò cá nhân, `PROMPTS.md`, link repo (app + API) và file APK.
- **Slide dự kiến:** khoảng 8 slide (hướng dẫn Demo Day và rubric); các nhóm tự làm slide trình bày.

---

## Thông tin đã chốt với giảng viên

mã học phần 111114; giảng viên phụ trách ThS. Nguyễn Minh Phúc, cùng tham gia Lê Minh Nhật, Lê Chân Thiện Tâm; thời lượng 15 LT / 45 TH; trọng số CLO 3/2/2/3 đánh giá cuối kỳ (sinh viên đạt CLO khi ≥ 50% điểm trọng số, chỉ tiêu ≥ 75% số sinh viên đạt); đánh giá 30% / 30% / 40%; CSDL chỉ dùng SQL Server qua backend, **backend bắt buộc truy cập CSDL qua stored procedure**; Khoa cấp Windows Server cho mỗi nhóm, có bộ phận hỗ trợ triển khai backend và SQL Server; thư viện gọi thủ tục là `mssql`; sinh viên tự đăng ký tài khoản Expo miễn phí; công cụ AI là Google Antigravity và GitHub Copilot Chat; khuyến khích dùng chung đề tài với môn Web; sinh viên tự xây API; Socket.IO realtime bắt buộc; Android bắt buộc, iOS mở rộng; ví dụ xuyên suốt LHU Food.
