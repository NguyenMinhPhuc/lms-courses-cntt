# LẬP TRÌNH FRONT-END (NEXT.JS, TYPESCRIPT & VIBE CODING)
## ASSESSMENT – RUBRIC THI HACKATHON & FINAL SHOWCASE (BUỔI 12)

> **Thời điểm:** Buổi 12 – Đồ án cuối kỳ · **Trọng số:** 40% điểm học phần
> **Chuẩn đầu ra:** CLO1 (PI 1.4), CLO2 (PI 2.3), CLO3 (PI 3.1), CLO4 (PI 5.1)
> **Đối tượng:** Nhóm đồ án 3–4 sinh viên (điểm nhóm) + từng sinh viên (điểm phản biện cá nhân)

---

### 1. Chương trình buổi Showcase (225 phút)

Buổi 12 giống một ngày "Demo Day" của startup: mọi nhóm mở link Vercel, các nhóm khác và giảng viên dùng thử sản phẩm thật, sau đó từng nhóm lên bảo vệ. Hãy tự hỏi trước: **người lạ mở link của nhóm trên điện thoại, họ có đặt được một vé mà không cần ai hướng dẫn không?**

| Phần | Thời lượng | Nội dung |
|---|---|---|
| 1. Khai mạc & Triển lãm Live Products | 30' | Các nhóm chia sẻ link Vercel Live; giảng viên và nhóm khác trải nghiệm chéo (Cross-Testing) bằng phiếu ở mục 7 |
| 2. Thuyết trình Hackathon Showcase | 160' | Mỗi nhóm 8' thuyết trình + demo live, 5' Q&A phản biện. Thể hiện rõ: Wireframe → Vercel App, kỹ thuật Vibe Coding đã dùng, minh chứng Git commit |
| 3. Tổng kết & Trao giải | 35' | Giảng viên công bố điểm, trao giải Nhóm có UI/UX Vibe Coding xuất sắc nhất |

---

### 2. Cấu trúc trọng số & tiêu chí tổng quan

| STT | Tiêu chí chính | Trọng số | Chuẩn đầu ra (PI) | Mô tả cốt lõi |
|---|---|---|---|---|
| 1 | Mô hình hóa UI & Wireframe Design | 15% (1.5đ) | PI 1.4 (CLO1) | Đủ 5 màn hình, chuẩn cấu trúc UX/UI, Wireframe Figma khớp với sản phẩm |
| 2 | Xây dựng Giao diện & Vibe Coding | 20% (2.0đ) | PI 2.3 (CLO2) | UI chuyên nghiệp (AntD/SCSS Custom), Responsive 100%, Hot Reload mượt không lỗi |
| 3 | Xử lý Logic, TypeScript & REST API | 20% (2.0đ) | PI 2.3 (CLO2) | TypeScript strict mode, Dynamic Routing, Fetching data API thật, LocalStorage/State |
| 4 | CI/CD Deployment, SEO & Lighthouse | 15% (1.5đ) | PI 5.1 (CLO4) | Deploy Live Vercel, Dynamic SEO Metadata, Lighthouse Performance > 85 |
| 5 | Báo cáo Văn bản & Minh chứng Git | 15% (1.5đ) | PI 3.1 (CLO3), PI 5.1 | Báo cáo Word/PDF đúng định dạng, Git Commit Log cá nhân đầy đủ |
| 6 | Thuyết trình Showcase & Phản biện Q&A | 15% (1.5đ) | PI 3.1 (CLO3), PI 5.1 | Demo Live tự tin, kịch bản chặt chẽ, trả lời phản biện tốt |
| | **Tổng** | **100% (10đ)** | | |

---

### 3. Bảng rubric chi tiết (thang điểm 10)

| Tiêu chí & Trọng số | Xuất sắc (8.5–10đ) | Khá (7.0–8.4đ) | Trung bình (5.5–6.9đ) | Yếu / Tối thiểu (< 5.5đ) |
|---|---|---|---|---|
| **1. Mô hình hóa UI & Wireframe** (15% – Max 1.5đ) [PI 1.4 – CLO1] | Có bản vẽ Wireframe Figma đủ 5 màn hình chính. Cấu trúc Layout (Header, Footer, Content, Sidebar) rất khoa học. Sản phẩm web chạy thật khớp > 90% so với Wireframe. | Có đủ Wireframe Figma cho 5 màn hình. Bố cục rõ ràng các vùng Header/Footer. Sản phẩm web thật tái hiện được 75–80% so với bản vẽ. | Có Wireframe nhưng thiếu 1–2 màn hình, hoặc bản vẽ sơ sài bằng tay. Giao diện sản phẩm thật có nhiều điểm sai lệch so với bản vẽ. | Không có Wireframe hoặc bản vẽ không đạt yêu cầu cấu trúc cơ bản. Sản phẩm không tuân theo mô hình thiết kế. |
| **2. Giao diện & Vibe Coding** (20% – Max 2.0đ) [PI 2.3 – CLO2] | Sử dụng Ant Design/Bootstrap mượt mà, tùy biến Theme qua SCSS/ConfigProvider có dấu ấn riêng. Responsive hoàn hảo trên Mobile/Tablet/Desktop. Hot Reload mượt, không lỗi UI. | Giao diện đẹp, đúng theo thiết kế. Tùy biến được Theme cơ bản. Responsive tốt trên Mobile & Desktop nhưng còn lỗi nhỏ ở cỡ Tablet. Hot Reload ổn định. | Giao diện nguyên bản (rập khuôn) thư viện UI, chưa tùy biến Theme. Bị vỡ khung hoặc tràn màn hình ở di động (horizontal overflow). | Giao diện thô sơ, chưa áp dụng thư viện UI hoặc SCSS. Lỗi layout nghiêm trọng trên di động, Hot Reload liên tục báo lỗi UI. |
| **3. Logic, TS & REST API** (20% – Max 2.0đ) [PI 2.3 – CLO2] | Khai báo TypeScript strict mode (không dùng `any`). Routing mượt mà. Kết nối API RESTful thật đổ dữ liệu động (Array/Single). Xử lý Form với Zod & LocalStorage chuẩn xác. | Khai báo TypeScript cơ bản (còn 1–2 lỗi type `any`). Routing chuẩn. Kết nối được API thật ở đa số các trang. Form Validation và LocalStorage hoạt động ổn định. | Còn dùng `any` nhiều. Routing hoạt động nhưng bị reload lại trang. Kết nối API bị lỗi ở một số tính năng, chủ yếu dùng dữ liệu Mock JSON tĩnh. | Không dùng TypeScript hoặc lỗi compile nặng. Không kết nối được API Backend. Logic giỏ hàng / Form bị lỗi runtime nghiêm trọng. |
| **4. Deploy, SEO & Performance** (15% – Max 1.5đ) [PI 5.1 – CLO4] | Deploy live thành công trên Vercel. Cấu hình SEO Metadata động (OpenGraph). Google Lighthouse Performance > 85 điểm, SEO > 90 điểm. | Deploy live trên Vercel chạy ổn định. Cấu hình SEO Metadata tĩnh. Lighthouse Performance đạt từ 70–84 điểm. | Deploy Vercel thành công nhưng thỉnh thoảng bị lỗi API/biến môi trường. Chưa cấu hình SEO Metadata. Lighthouse Performance từ 50–69 điểm. | Không deploy thành công lên Vercel (chỉ chạy ở localhost). Lighthouse Performance < 50 điểm, lỗi tối ưu ảnh/script. |
| **5. Báo cáo & Git Commit** (15% – Max 1.5đ) [PI 3.1 – CLO3, PI 5.1] | File báo cáo Word/PDF trình bày khoa học, đúng quy định. Git Commit Log minh chứng rõ sự đóng góp đồng đều của tất cả thành viên (đầy đủ PR). | File báo cáo đúng mẫu, đủ nội dung mô tả logic. Git Commit Log thể hiện phối hợp nhóm tốt nhưng đóng góp chưa đồng đều. | File báo cáo sơ sài, thiếu các mục mô tả logic xử lý. Git Log thể hiện chỉ 1–2 thành viên gánh team. | Không nộp báo cáo hoặc sai quy định nghiêm trọng. Không có minh chứng Git Commit Log của các thành viên. |
| **6. Thuyết trình & Phản biện Q&A** (15% – Max 1.5đ) [PI 3.1 – CLO3, PI 5.1] | Thuyết trình chuyên nghiệp, đúng thời gian (8 phút). Demo live trơn tru. Trả lời phản biện xuất sắc, giải thích sâu đoạn code cá nhân đảm nhiệm. | Thuyết trình rõ ràng. Demo live ổn định. Cá nhân trả lời đúng các câu hỏi phản biện về phần code do mình thực hiện. | Thuyết trình quá thời lượng. Demo live gặp sự cố. Trả lời phản biện còn lúng túng, chưa nắm rõ phần code đảm nhiệm. | Thuyết trình ngập ngừng, không làm chủ Slide/Demo. Không trả lời được câu hỏi phản biện code. |

#### 3.1. Quy đổi mức điểm sang điểm tiêu chí

Giảng viên chọn một mức điểm trên thang 10 cho từng tiêu chí, sau đó nhân với trọng số:

```text
Điểm tiêu chí = Điểm tối đa của tiêu chí × (Mức điểm thang 10 ÷ 10)
Điểm Đồ án Nhóm = Tổng 6 điểm tiêu chí   (tối đa 10)
```

| Mức | Thang 10 | Tiêu chí 1.5đ | Tiêu chí 2.0đ |
|---|---|---|---|
| Xuất sắc | 8.5–10 | 1.3–1.5 | 1.7–2.0 |
| Khá | 7.0–8.4 | 1.05–1.25 | 1.4–1.65 |
| Trung bình | 5.5–6.9 | 0.85–1.0 | 1.1–1.35 |
| Yếu | < 5.5 | 0–0.8 | 0–1.0 |

---

### 4. Công thức điểm cuối kỳ cá nhân & điểm thưởng

#### 4.1. Công thức

```text
Điểm Cuối kỳ Cá nhân = (Điểm Đồ án Nhóm × 0.7) + (Điểm Phản biện Cá nhân × 0.3)
```

* **Điểm Đồ án Nhóm (70%):** chung cho cả nhóm, dựa trên sản phẩm Live, Wireframe, UI/UX, Deploy Vercel và báo cáo văn bản (bảng rubric mục 3).
* **Điểm Phản biện Cá nhân (30%):** đánh giá độc lập từng sinh viên dựa trên minh chứng Git commit log và phần trả lời câu hỏi phản biện trực tiếp về code cá nhân đảm nhiệm (phiếu mục 6).
* **Ví dụ:** Nhóm đạt 8.4. Bạn C phản biện 9.0 → 8.4 × 0.7 + 9.0 × 0.3 = **8.58**. Bạn D phản biện 4.0 → 8.4 × 0.7 + 4.0 × 0.3 = **7.08**. Cùng một sản phẩm, nhưng người hiểu code của mình sẽ nhận điểm cao hơn.

#### 4.2. Điểm thưởng Vibe Coding xuất sắc (+0.5đ đến +1.0đ vào Điểm Quá trình)

| Danh hiệu | Điều kiện | Minh chứng cần nộp |
|---|---|---|
| **Vibe Coding Master** | Tự thiết kế Prompt Workflow độc đáo, tối ưu tốc độ sinh code mà vẫn kiểm soát chất lượng | Nhật ký Vibe Coding: chuỗi prompt, kết quả AI, phần đã sửa |
| **UI Innovation** | Giao diện UI/UX vượt yêu cầu cơ bản (Dark/Light Mode, Micro-interactions) | Demo live + commit tương ứng |
| **Ultra Performance** | Google Lighthouse Performance đạt 100/100 | Ảnh chụp Lighthouse trên link Vercel, giảng viên chạy lại để xác nhận |

* Mỗi danh hiệu đạt được: **+0.5**; tổng tối đa **+1.0**; Điểm Quá trình sau khi cộng không vượt quá 10.
* Điểm thưởng áp dụng cho các thành viên có commit ở hạng mục tương ứng (đối chiếu Git log).

---

### 5. Phiếu chấm nhóm – Hackathon

**Lớp:** ............ **Nhóm:** ............ **Link Vercel:** ........................................ **Giảng viên chấm:** ............

| Tiêu chí | Max | Mức (XS/K/TB/Y) | Thang 10 | Điểm tiêu chí | Minh chứng / Nhận xét |
|---|---|---|---|---|---|
| 1. Mô hình hóa UI & Wireframe | 1.5 | | | | |
| 2. Giao diện & Vibe Coding | 2.0 | | | | |
| 3. Logic, TypeScript & REST API | 2.0 | | | | |
| 4. Deploy, SEO & Performance | 1.5 | | | | |
| 5. Báo cáo & Git Commit | 1.5 | | | | |
| 6. Thuyết trình & Phản biện Q&A | 1.5 | | | | |
| **Điểm Đồ án Nhóm** | **10** | | | | |

**Kiểm tra kỹ thuật tại chỗ:**

| Hạng mục | Kết quả | Ghi chú |
|---|---|---|
| Link Vercel mở được, gọi API thành công | ☐ Đạt ☐ Chưa | |
| Lighthouse Performance / SEO (Mobile) | ...... / ...... | |
| `generateMetadata` cho `/events/[id]` (xem OG khi chia sẻ link) | ☐ Có ☐ Không | |
| Responsive 375px / 768px / 1440px | ☐ ☐ ☐ | |
| Form có Zod validation, Wishlist giữ sau khi refresh | ☐ Đạt ☐ Chưa | |
| Thời gian thuyết trình (chuẩn 8') | ...... phút | |
| Đề cử điểm thưởng | ☐ Vibe Coding Master ☐ UI Innovation ☐ Ultra Performance | |

---

### 6. Phiếu phản biện cá nhân (thang 10)

| Thành phần | Max | Xuất sắc | Khá | Trung bình | Yếu |
|---|---|---|---|---|---|
| **A. Minh chứng Git commit cá nhân** | 3.0 | 2.6–3.0: commit đều suốt học phần, đúng Conventional Commits, có PR được review | 2.1–2.5: commit đủ ở phần mình phụ trách, message chưa đều chuẩn | 1.7–2.0: ít commit, dồn vào cuối kỳ | 0–1.6: gần như không có commit cá nhân |
| **B. Giải thích phần code đảm nhiệm** | 4.0 | 3.4–4.0: giải thích luồng dữ liệu, type, lý do chọn giải pháp | 2.8–3.3: giải thích đúng, còn thiếu chiều sâu | 2.2–2.7: đọc lại code, chưa giải thích được lý do | 0–2.1: không giải thích được code mang tên mình |
| **C. Trả lời câu hỏi mở rộng / sửa code tại chỗ** | 3.0 | 2.6–3.0: sửa đúng yêu cầu nhỏ ngay tại chỗ, nêu được cách khác | 2.1–2.5: sửa được khi có gợi ý | 1.7–2.0: hiểu yêu cầu nhưng chưa sửa được | 0–1.6: không hiểu câu hỏi |

| STT | Họ tên | MSSV | Phần đảm nhiệm | A (/3) | B (/4) | C (/3) | Phản biện (/10) | Điểm nhóm | **Điểm CK cá nhân** |
|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | | |
| 2 | | | | | | | | | |
| 3 | | | | | | | | | |
| 4 | | | | | | | | | |

**Gợi ý câu hỏi phản biện:**

* "Hàm `generateMetadata` của trang chi tiết sự kiện lấy dữ liệu từ đâu? Nếu API trả 404 thì trang hiển thị gì?"
* "Schema Zod của form này kiểm tra những gì? Thử thêm điều kiện: số lượng vé từ 1 đến 10."
* "Vì sao Wishlist đọc LocalStorage trong `useEffect` mà không đọc trực tiếp khi render?"
* "Biến `NEXT_PUBLIC_API_URL` được cấu hình ở đâu trên Vercel? Vì sao cần tiền tố `NEXT_PUBLIC_`?"
* "Điểm Lighthouse của nhóm tăng nhờ thay đổi nào? Mở commit đó cho thầy/cô xem."

---

### 7. Phiếu Cross-Testing (nhóm chấm chéo – 30 phút đầu Buổi 12)

Mỗi nhóm được phân công kiểm thử sản phẩm của **2 nhóm khác** trên link Vercel. Mục tiêu là tìm lỗi và góp ý như một người dùng thật, không phải để "chấm điểm" đối thủ. Phiếu được chuyển cho nhóm được kiểm thử ngay sau buổi; giảng viên dùng phiếu để tham khảo khi đặt câu hỏi Q&A và tính vào điểm tham gia (quá trình) của **nhóm kiểm thử** dựa trên chất lượng góp ý.

**Nhóm kiểm thử:** ............ **Nhóm được kiểm thử:** ............ **Link Vercel:** ........................................ **Thiết bị:** ☐ Điện thoại ☐ Laptop

| STT | Kịch bản kiểm thử | Đạt | Lỗi | Mô tả lỗi (bước tái hiện) |
|---|---|---|---|---|
| 1 | Mở link, trang chủ hiển thị danh sách sự kiện từ API (không phải dữ liệu giả) | ☐ | ☐ | |
| 2 | Lọc theo danh mục / tìm kiếm sự kiện | ☐ | ☐ | |
| 3 | Mở chi tiết sự kiện bằng URL `/events/[id]`, refresh trang vẫn hiển thị đúng | ☐ | ☐ | |
| 4 | Chọn hạng vé, số lượng, ghế; tổng tiền cập nhật đúng | ☐ | ☐ | |
| 5 | Đặt vé thành công, có thông báo (Notification/Toast) | ☐ | ☐ | |
| 6 | Form đăng nhập/đăng ký báo lỗi khi nhập sai email, mật khẩu ngắn | ☐ | ☐ | |
| 7 | Thêm sự kiện vào Wishlist, refresh trang vẫn còn | ☐ | ☐ | |
| 8 | Giao diện điện thoại (375px) không tràn ngang, menu dùng được | ☐ | ☐ | |
| 9 | Trang không tồn tại hiển thị 404 tùy biến | ☐ | ☐ | |
| 10 | Console DevTools không có lỗi đỏ | ☐ | ☐ | |

**Cảm nhận chung của người dùng:**

| Hạng mục | 1 – Kém | 2 – Tạm được | 3 – Tốt | 4 – Rất tốt |
|---|---|---|---|---|
| Dễ sử dụng, không cần hướng dẫn | ☐ | ☐ | ☐ | ☐ |
| Giao diện có nhận diện riêng (không rập khuôn thư viện) | ☐ | ☐ | ☐ | ☐ |
| Tốc độ tải trang | ☐ | ☐ | ☐ | ☐ |

* **01 điểm mạnh nhất:** ......................................................................
* **01 lỗi nghiêm trọng nhất cần sửa:** ......................................................
* **01 gợi ý cải tiến:** .......................................................................

---

### ❓ Tự kiểm tra trước Hackathon

**Câu hỏi:** Nhóm deploy Vercel thành công, có metadata tĩnh ở Root Layout nhưng chưa có `generateMetadata` cho trang chi tiết; Lighthouse Performance đạt 78. Tiêu chí 4 của nhóm nằm ở mức nào và cần làm gì để lên mức Xuất sắc?

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án:</b> Mức Khá (khoảng 1.05–1.25đ).<br>
<b>Giải thích:</b> Mức Xuất sắc yêu cầu đồng thời SEO Metadata động (OpenGraph theo từng sự kiện), Performance trên 85 và SEO trên 90. Nhóm cần viết <code>generateMetadata</code> cho <code>/events/[id]</code> (nhớ <code>await params</code> trong Next.js 15), thay <code>&lt;img&gt;</code> bằng <code>next/image</code> có <code>sizes</code> và <code>priority</code>, dùng <code>next/font</code> và lazy load component nặng bằng <code>next/dynamic</code>.
</details>
