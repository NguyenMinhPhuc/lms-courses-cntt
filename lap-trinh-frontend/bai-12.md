# LẬP TRÌNH FRONT-END (NEXT.JS, TYPESCRIPT & VIBE CODING)
## CHƯƠNG 7: TỔNG KẾT HỌC PHẦN
### Bài 12: Thi Hackathon & Final Showcase (Báo cáo cuối kỳ 40%)

> **Thời lượng:** 5 tiết (225 phút) · **Hình thức:** Đánh giá cuối kỳ – Báo cáo công khai / Thi Showcase Hackathon giữa các lớp · **Chuẩn đầu ra:** PI 1.4 (CLO1), PI 2.3 (CLO2), PI 3.1 (CLO3), PI 5.1 (CLO4)
> **Dự án xuyên suốt:** Smart Event Hub – demo sản phẩm Live trên Vercel, thuyết trình và phản biện cá nhân

---

> 🎯 **MỤC TIÊU BÀI HỌC (Learning Objectives)**
> Sau khi hoàn thành bài học này, người học có thể:
> * **[Bloom 1/2 - Kiến thức]:** Trình bày được chương trình buổi Showcase, danh mục sản phẩm phải nộp, 6 tiêu chí rubric và công thức tính điểm cuối kỳ cá nhân.
> * **[Bloom 3/4 - Kỹ năng]:** Xây dựng kịch bản thuyết trình 8 phút thể hiện rõ hành trình Wireframe → Vercel App, kỹ thuật Vibe Coding đã dùng và minh chứng Git commit.
> * **[Bloom 5/6 - Năng lực]:** Demo Live tự tin, bảo vệ phần code cá nhân đảm nhiệm trước câu hỏi phản biện và tự đánh giá sản phẩm nhóm theo rubric.

---

### 📝 1. ĐẶT VẤN ĐỀ & DẪN NHẬP (Introduction / Hook)

Sau 11 buổi, Smart Event Hub của nhóm bạn đã có Wireframe, giao diện Ant Design, API thật, form Zod, link Vercel và điểm Lighthouse. Hôm nay, toàn bộ hành trình đó được nén vào **8 phút thuyết trình và 5 phút hỏi đáp**. Giảng viên có thể chỉ vào một hàm bất kỳ trong commit của bạn và hỏi: "Dòng này làm gì, sao bạn viết vậy?".

**Nếu demo Live bị mất mạng giữa chừng, hoặc câu hỏi phản biện rơi đúng vào đoạn code AI sinh mà bạn chưa đọc kỹ, bạn sẽ xử lý thế nào?** Bài này giúp các bạn chuẩn bị cho cả sản phẩm lẫn phần trình bày, để điểm số phản ánh đúng công sức cả học kỳ.

> 🧭 **Trước giờ học (Flipped Classroom):** Hoàn tất Báo cáo Word/PDF và Slide (BTVN Bài 11). Đọc kỹ rubric ở mục 2.5, tự chấm thử sản phẩm nhóm. Kiểm tra link Vercel Live trên cả điện thoại và máy tính. Mỗi thành viên tập giải thích phần code của mình. Làm quiz ôn tập trên LMS.

---

### 📖 2. NỘI DUNG CỐT LÕI (Core Content)

#### 2.1. Chương trình buổi Hackathon & Final Showcase

* **Khái niệm:** Buổi 12 là **báo cáo công khai**, chiếm **40% tổng điểm học phần**, đánh giá theo nhóm đồ án (3–4 sinh viên) kết hợp điểm phản biện cá nhân.
* **Chi tiết kỹ thuật / Lý thuyết:**

| Phần | Thời lượng | Nội dung |
|---|---|---|
| 1. Khai mạc & Triển lãm Live Products | 30' | Tất cả các nhóm mở link Vercel Live App để GV và các nhóm khác trải nghiệm chéo (Cross-Testing) |
| 2. Thuyết trình Hackathon Showcase | 160' | Mỗi nhóm: **8 phút** thuyết trình + demo tính năng Live, **5 phút** Q&A phản biện từ GV |
| 3. Tổng kết & Trao giải | 35' | GV công bố điểm đánh giá, trao giải Nhóm có UI/UX Vibe Coding xuất sắc nhất |

  * Mỗi lượt nhóm kéo dài 13 phút (8 + 5), nên việc giữ đúng giờ là yêu cầu bắt buộc chứ không phải lời khuyên.
  * Trong 8 phút, nhóm phải thể hiện rõ: **Wireframe → Vercel App**, **kỹ thuật Vibe Coding đã dùng**, **minh chứng Git commit**.
* **💡 Ví dụ thực tế (Real-world Example):**
  > Ở phần Cross-Testing, nhóm C mở link của nhóm D trên điện thoại, đặt thử một vé và phát hiện Booking Modal bị tràn ở 375px. Đây chính là kiểu lỗi giám khảo cũng sẽ thấy, vì vậy hãy tự Cross-Test với nhóm bạn trước buổi Showcase.

#### 2.2. Checklist sản phẩm nộp

* **Khái niệm:** Sản phẩm cuối kỳ là một **bộ hồ sơ**, không chỉ là trang web. Thiếu một hạng mục là mất điểm ở tiêu chí tương ứng trong rubric.
* **Chi tiết kỹ thuật / Lý thuyết:**
  * [ ] **Link Vercel Live** chạy ổn định: gọi API thật, LocalStorage hoạt động, không lỗi biến môi trường.
  * [ ] **GitHub Repository** công khai, branch `main` là bản cuối; commit log thể hiện đóng góp của **từng** thành viên, có Pull Request.
  * [ ] **Báo cáo Văn bản (Word/PDF)** đúng mẫu: mô tả kiến trúc, sơ đồ Wireframe, mô tả API tích hợp, phân công công việc, ảnh minh chứng Git commit, Link Vercel Live.
  * [ ] **Wireframe Figma đủ 5 màn hình:** Trang chủ, Chi tiết sự kiện, Đặt vé, Trang cá nhân, Admin Dashboard.
  * [ ] **Slide thuyết trình** cho phần Showcase 8 phút.
  * [ ] Kết quả **Lighthouse** (từ Bài 11) và kịch bản **Test_Cases_Scenario** (từ Bài 10) để dẫn chứng khi cần.
* **💡 Ví dụ thực tế (Real-world Example):**
  > Một nhóm có web rất đẹp nhưng Git log cho thấy 90% commit đến từ một người. Theo rubric, tiêu chí "Báo cáo & Git Commit" của nhóm rơi xuống mức Trung bình, và các thành viên còn lại gặp khó ở phần phản biện cá nhân.

```bash
# Kiểm tra nhanh trước khi nộp
git checkout main && git pull           # đảm bảo bản cuối nằm trên main
git shortlog -sn --no-merges            # số commit của từng thành viên
npm run build                           # build pass trên máy = Vercel ít rủi ro
```

#### 2.3. Xây dựng kịch bản thuyết trình & demo 8 phút

* **Khái niệm:** Kịch bản thuyết trình là trình tự **ai nói gì, demo màn hình nào, trong bao lâu**. Rubric đánh giá "kịch bản thuyết trình chặt chẽ" và "đúng thời gian (8 phút)".
* **Chi tiết kỹ thuật / Lý thuyết:**
  * Dàn ý gợi ý (nhóm tự phân bổ thời gian, tổng không vượt 8 phút):

| Bước | Nội dung | Gợi ý minh chứng |
|---|---|---|
| Mở đầu | Bài toán Smart Event Hub, thành viên & phân công | Slide giới thiệu |
| Wireframe → Sản phẩm | Đặt Wireframe Figma cạnh màn hình thật | Ảnh so sánh 5 màn hình |
| Demo Live | Trang chủ → Danh mục → Chi tiết sự kiện → Đặt vé → Admin Orders | Link Vercel, thao tác trên mobile view |
| Kỹ thuật | TypeScript strict, Dynamic Routing, REST API, Zod, LocalStorage | Đoạn code tiêu biểu |
| Vibe Coding | Prompt Workflow nhóm đã dùng, ví dụ code AI sai và cách nhóm sửa | Prompt + diff trước/sau |
| Deploy & chất lượng | CI/CD Vercel, Metadata động, Lighthouse | Ảnh Lighthouse, link chia sẻ có OG Image |
| Git | Minh chứng đóng góp của từng người | Commit log, danh sách PR |

  * **Phương án dự phòng:** quay sẵn video demo luồng chính, mở sẵn các tab cần dùng, đăng nhập sẵn tài khoản demo. Rubric trừ điểm khi "demo live bị sự cố bất ngờ" mà nhóm lúng túng.
  * Mỗi thành viên nên trình bày phần mình làm, để giám khảo thấy sự đóng góp ngay trong bài nói.
* **💡 Ví dụ thực tế (Real-world Example):**
  > Thay vì đọc slide "Chúng em dùng Next.js App Router", hãy mở link `/events/12` trên điện thoại, chia sẻ vào Zalo để mọi người thấy OG Image hiện đúng, rồi nói "đây là kết quả của `generateMetadata`".

#### 2.4. Chuẩn bị phản biện cá nhân

* **Khái niệm:** **Điểm Phản biện Cá nhân (30%)** được chấm độc lập cho từng sinh viên, dựa trên **minh chứng Git Commit Log** và **phần trả lời câu hỏi phản biện trực tiếp về code cá nhân đảm nhiệm**.
* **Chi tiết kỹ thuật / Lý thuyết:**
  * Liệt kê commit của chính mình, mở lại từng file đã sửa, tự hỏi: "Nếu xóa dòng này thì điều gì xảy ra?".
  * Code do AI sinh mà bạn đã commit **là code của bạn**. Phải giải thích được từng dòng, như nguyên tắc Vibe Coding xuyên suốt học phần: review, hiểu và debug chứ không copy-paste thụ động.
  * Các nhóm câu hỏi thường gặp: vì sao component này cần `'use client'`; vì sao `await params`; Interface này khớp với API Response ra sao; Zod schema kiểm tra những gì; dữ liệu LocalStorage được đọc ở đâu để tránh lỗi hydration; biến môi trường được cấu hình thế nào trên Vercel.
* **💡 Ví dụ thực tế (Real-world Example):**
  > GV hỏi bạn phụ trách Wishlist: "Refresh trang thì dữ liệu lấy từ đâu?". Câu trả lời mức Xuất sắc là chỉ ra đoạn `useEffect` đọc `localStorage`, giải thích vì sao không đọc ngay khi render và cách xử lý khi JSON bị hỏng.

```bash
# Xem lại toàn bộ commit của bản thân (thay tên theo cấu hình git của bạn)
git log --author="Nguyen Van A" --oneline --no-merges

# Xem chi tiết thay đổi trong một commit cụ thể
git show <commit-hash> --stat
```

> **Bài tập tự luyện:** Mỗi thành viên chọn 2 đoạn code quan trọng nhất của mình, giải thích cho bạn cùng nhóm trong 2 phút mỗi đoạn mà không nhìn ghi chú.

#### 2.5. Rubric 6 tiêu chí & công thức điểm cuối kỳ

* **Khái niệm:** Điểm đồ án chấm theo thang 10, gồm 6 tiêu chí ứng với 4 chuẩn đầu ra CLO1–CLO4.
* **Chi tiết kỹ thuật / Lý thuyết:**

| STT | Tiêu chí | Trọng số | PI | Mức Xuất sắc (8.5–10đ) cần đạt |
|---|---|---|---|---|
| 1 | Mô hình hóa UI & Wireframe Design | 15% (1.5đ) | PI 1.4 (CLO1) | Wireframe Figma đủ 5 màn hình, layout khoa học, sản phẩm khớp >90% bản vẽ |
| 2 | Xây dựng Giao diện & Vibe Coding | 20% (2.0đ) | PI 2.3 (CLO2) | AntD/Bootstrap tùy biến Theme qua SCSS/ConfigProvider có dấu ấn riêng, Responsive hoàn hảo Mobile/Tablet/Desktop, Hot Reload zero lỗi UI |
| 3 | Xử lý Logic, TypeScript & REST API | 20% (2.0đ) | PI 2.3 (CLO2) | TypeScript strict (không `any`), Routing mượt, API RESTful thật (Array/Single), Form Zod & LocalStorage chuẩn xác |
| 4 | CI/CD Deployment, SEO & Lighthouse | 15% (1.5đ) | PI 5.1 (CLO4) | Deploy Vercel thành công, SEO Metadata động (OpenGraph), Performance > 85, SEO > 90 |
| 5 | Báo cáo Văn bản & Minh chứng Git | 15% (1.5đ) | PI 3.1 (CLO3), PI 5.1 | Báo cáo khoa học đúng quy định, Git log thể hiện đóng góp đồng đều của tất cả thành viên (đầy đủ PR) |
| 6 | Thuyết trình Showcase & Phản biện Q&A | 15% (1.5đ) | PI 3.1 (CLO3), PI 5.1 | Đúng 8 phút, demo Live trơn tru, giải thích sâu sắc đoạn code cá nhân đảm nhiệm |

  * Bốn mức đánh giá: **Xuất sắc** (8.5–10đ), **Khá** (7.0–8.4đ), **Trung bình** (5.5–6.9đ), **Yếu** (< 5.5đ). Một số mốc phân biệt: Lighthouse 70–84 ở mức Khá, 50–69 ở mức Trung bình, < 50 ở mức Yếu; giao diện rập khuôn thư viện, chưa tùy biến Theme hoặc bị Horizontal Overflow ở di động rơi vào mức Trung bình.
  * **Công thức điểm cuối kỳ cá nhân:**

```text
Điểm Cuối Kỳ Cá Nhân = (Điểm Đồ Án Nhóm × 0.7) + (Điểm Phản Biện Cá Nhân × 0.3)
```

  * **Điểm Nhóm (70%)**: chung cho cả đội, dựa trên sản phẩm Live, Wireframe, UI/UX, Deploy Vercel và Báo cáo Văn bản. **Điểm Cá nhân (30%)**: riêng từng sinh viên, dựa trên Git Commit Log và phần trả lời phản biện.
* **💡 Ví dụ thực tế (Real-world Example):**
  > Nhóm đạt 8.0 điểm đồ án. Bạn An trả lời phản biện tốt, được 9.0: điểm cuối kỳ = 8.0 × 0.7 + 9.0 × 0.3 = 5.6 + 2.7 = **8.3**. Bạn Bình cùng nhóm nhưng lúng túng, được 5.0: điểm = 5.6 + 1.5 = **7.1**. Cùng một sản phẩm, điểm cá nhân vẫn khác nhau.

#### 2.6. Điểm thưởng Vibe Coding xuất sắc

* **Khái niệm:** Ngoài điểm cuối kỳ, nhóm có thể nhận **+0.5đ đến +1.0đ vào Điểm Quá trình** nếu đạt một trong các tiêu chí thưởng.
* **Chi tiết kỹ thuật / Lý thuyết:**
  * **Vibe Coding Master:** tự thiết kế Prompt Workflow độc đáo, tối ưu tốc độ sinh code mượt mà.
  * **UI Innovation:** giao diện UI/UX vượt trội so với yêu cầu cơ bản (có Dark/Light Mode, Micro-interactions).
  * **Ultra Performance:** điểm Google Lighthouse Performance đạt tuyệt đối 100/100.
  * Cuối buổi, GV trao giải **Nhóm có UI/UX Vibe Coding xuất sắc nhất**.
* **💡 Ví dụ thực tế (Real-world Example):**
  > Một nhóm trình bày chuỗi prompt gồm: sinh Interface từ Swagger → sinh Service API → sinh component → prompt review Clean Code, kèm ví dụ AI sai ở đâu và được sửa thế nào. Đây là minh chứng phù hợp cho hạng mục Vibe Coding Master.

#### 2.7. Vibe Coding – Prompt mẫu & cách kiểm duyệt code AI

AI có thể giúp nhóm luyện phản biện và rà soát báo cáo. Tuy vậy, câu trả lời trước giám khảo phải đến từ hiểu biết của chính bạn.

```text
Bạn là giảng viên chấm đồ án Front-End (Next.js 15, TypeScript, Ant Design v5).
Dưới đây là đoạn code tôi phụ trách trong dự án Smart Event Hub:
[Dán code của bạn]

Hãy đặt 5 câu hỏi phản biện từ dễ đến khó về đoạn code này (vì sao viết vậy, điều gì xảy ra nếu thay đổi,
có lỗi tiềm ẩn nào không). KHÔNG đưa đáp án. Sau khi tôi trả lời, hãy nhận xét câu trả lời còn thiếu ở đâu.
```

```text
Đây là mục lục và nội dung báo cáo đồ án của nhóm tôi:
[Dán mục lục / nội dung]

Hãy đối chiếu với các yêu cầu sau và liệt kê mục còn thiếu hoặc sơ sài:
mô tả kiến trúc, sơ đồ Wireframe 5 màn hình, mô tả API tích hợp, phân công công việc,
minh chứng Git commit, Link Vercel Live.
```

**Checklist trước khi lên Showcase:**

* **Không học thuộc câu trả lời do AI viết:** dùng AI để đặt câu hỏi, còn câu trả lời phải tự xây dựng.
* **Số liệu thật:** điểm Lighthouse, số commit, link Vercel trong slide phải khớp với thực tế lúc demo.
* **Code đã kiểm:** không còn `any`, Console sạch warning, responsive ở 375/768/1440px.
* **Thời gian:** tập dượt bấm giờ, đảm bảo không vượt 8 phút.

#### 2.8. Thực hành trên lớp

Buổi 12 không có phần Guided/Unguided. Toàn bộ 225 phút là buổi đánh giá công khai.

| Phần | Thời lượng | Nhiệm vụ | Output mong muốn |
|---|---|---|---|
| Khai mạc & Triển lãm Live Products | 30' | Mở link Vercel Live, trải nghiệm chéo sản phẩm các nhóm (Cross-Testing) | Mọi link Live truy cập được; nhóm ghi nhận góp ý từ nhóm bạn |
| Thuyết trình Hackathon Showcase | 160' | Mỗi nhóm 8' thuyết trình + demo Live, 5' Q&A phản biện cá nhân | Thể hiện Wireframe → Vercel App, kỹ thuật Vibe Coding, minh chứng Git |
| Tổng kết & Trao giải | 35' | GV công bố điểm, trao giải UI/UX Vibe Coding xuất sắc nhất | Điểm cuối kỳ theo rubric; nhóm nhận nhận xét tổng kết |

* **Triển lãm:** Mỗi nhóm cử một người trực máy, các thành viên còn lại đi trải nghiệm sản phẩm nhóm khác, đặc biệt trên điện thoại.
* **Thuyết trình:** Nhóm kế tiếp chuẩn bị sẵn máy và tab trình duyệt trong lúc nhóm trước Q&A để không mất thời gian chuyển giao.
* **Tổng kết:** Ghi lại nhận xét của GV để hoàn thiện sản phẩm cho portfolio cá nhân.

---

### 📌 3. TÓM TẮT & ĐIỂM CẦN NHỚ (Key Takeaways)

* 🔹 **Cấu trúc buổi:** 30' triển lãm & Cross-Testing → 160' thuyết trình (8' + 5' Q&A mỗi nhóm) → 35' tổng kết & trao giải.
* 🔹 **Hồ sơ nộp đủ:** Link Vercel Live, GitHub repo có commit từng người, Báo cáo Word/PDF đúng mẫu, Wireframe Figma 5 màn hình, Slide.
* 🔹 **Rubric 6 tiêu chí:** Wireframe 15%, Giao diện & Vibe Coding 20%, Logic/TS/API 20%, Deploy/SEO/Lighthouse 15%, Báo cáo & Git 15%, Thuyết trình & Phản biện 15%.
* 🔹 **Điểm cá nhân:** Nhóm × 0.7 + Phản biện cá nhân × 0.3; Git log và khả năng giải thích code của chính mình quyết định 30%.
* 🔹 **Điểm thưởng:** +0.5 đến +1.0 vào Điểm Quá trình cho Vibe Coding Master, UI Innovation hoặc Ultra Performance (Lighthouse 100/100).

---

### ❓ 4. HOẠT ĐỘNG KIỂM TRA NHANH (Self-Assessment / Quiz)

**Câu 1:** Nhóm đạt 7.0 điểm đồ án, bạn Chi đạt 10 điểm phản biện cá nhân. Điểm cuối kỳ của Chi là bao nhiêu?
- A. 7.9
- B. 8.5
- C. 7.0
- D. 8.0

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> A<br>
<b>Giải thích:</b> 7.0 × 0.7 + 10 × 0.3 = 4.9 + 3.0 = 7.9.
</details>

**Câu 2:** Trong phần Thuyết trình Hackathon Showcase, mỗi nhóm được phân bổ thời gian thế nào?
- A. 10 phút thuyết trình + 5 phút phản biện
- B. 5 phút thuyết trình + 8 phút phản biện
- C. 8 phút thuyết trình & demo Live + 5 phút Q&A phản biện
- D. 15 phút thuyết trình, không có phản biện

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> C<br>
<b>Giải thích:</b> Theo đề cương Buổi 12, mỗi nhóm có 8 phút thuyết trình + demo và 5 phút Q&A. Mốc 10 + 5 phút là của buổi giữa kỳ (Bài 7).
</details>

**Câu 3:** Sản phẩm đạt Lighthouse Performance 78 điểm, Deploy Vercel ổn định, mới cấu hình SEO Metadata tĩnh. Tiêu chí 4 của nhóm thuộc mức nào?
- A. Xuất sắc
- B. Khá
- C. Trung bình
- D. Yếu

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> B<br>
<b>Giải thích:</b> Mức Khá: Deploy ổn định, Metadata tĩnh, Lighthouse Performance 70–84. Mức Xuất sắc cần Metadata động và Performance > 85.
</details>

**Câu 4:** Điểm Phản biện Cá nhân (30%) được đánh giá dựa trên những gì?
- A. Số lượng slide và hiệu ứng trình chiếu
- B. Điểm trung bình các quiz trên LMS
- C. Điểm Lighthouse của sản phẩm nhóm
- D. Git Commit Log cá nhân và phần trả lời phản biện về code mình đảm nhiệm

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> D<br>
<b>Giải thích:</b> Rubric quy định điểm cá nhân dựa trên minh chứng Git Commit Log và phần trả lời câu hỏi phản biện trực tiếp về code cá nhân đảm nhiệm.
</details>

> Bộ 10+ câu đầy đủ: `quiz/quiz-bai-12-aiken.txt`

---

### 💬 5. NHIỆM VỤ HỌC TẬP & THẢO LUẬN (LMS Discussion / Assignment)

* **Chủ đề thảo luận Diễn đàn (Forum Discussion):** Nhìn lại 12 buổi học, Vibe Coding đã thay đổi cách bạn viết code ra sao? Hãy kể một lần AI giúp bạn tiết kiệm nhiều thời gian và một lần AI khiến bạn mất thời gian hơn. Sau học phần này, bạn sẽ đặt nguyên tắc gì cho bản thân khi làm việc cùng AI?
* **Yêu cầu nộp bài (Bài tập về nhà):**
  * Nộp đầy đủ bộ hồ sơ cuối kỳ theo checklist mục 2.2: Link Vercel Live, link GitHub Repository, Báo cáo Word/PDF, Wireframe Figma 5 màn hình, Slide thuyết trình.
  * **Output:** một bài nộp trên LMS cho mỗi nhóm, gồm file `BaoCao_SmartEventHub_<TenNhom>.pdf`, `Slide_SmartEventHub_<TenNhom>.pdf` và file text chứa các link.
  * **Hạn nộp:** trước khi Buổi 12 bắt đầu, theo thông báo của GV trên LMS. Repo phải giữ nguyên trạng thái branch `main` tại thời điểm nộp.
* **📚 Tài liệu đọc & tham khảo:**
  * Rubric chấm Hackathon Lập trình Front-End (tài liệu học phần trên LMS)
  * Next.js Metadata Documentation: https://nextjs.org/docs/app/building-your-application/optimizing/metadata
  * Google Lighthouse Audit Guide: https://developer.chrome.com/docs/lighthouse/overview/
  * Refactoring Guru – Code Smells: https://refactoring.guru/refactoring/smells
  * Vercel Documentation: https://vercel.com/docs
