# LẬP TRÌNH FRONT-END (NEXT.JS, TYPESCRIPT & VIBE CODING)
## ASSESSMENT – KẾ HOẠCH ĐÁNH GIÁ HỌC PHẦN

> **Áp dụng cho:** 12 buổi (60 tiết) · **Dự án đánh giá:** Smart Event Hub (nhóm 3–4 sinh viên) · **Chuẩn đầu ra:** CLO1 (PI 1.4), CLO2 (PI 2.3), CLO3 (PI 3.1), CLO4 (PI 5.1)
> **Tài liệu liên quan:** `rubric-giua-ky.md` · `rubric-hackathon-cuoi-ky.md` · `tu-danh-gia-va-danh-gia-cheo.md`

---

### 1. Nguyên tắc đánh giá

Một sinh viên có thể nhờ AI sinh ra một trang web khá đẹp chỉ trong một buổi tối. Vậy điểm số của học phần nên đo điều gì? Câu trả lời của chúng ta: đo **quá trình** các bạn xây sản phẩm và **mức độ hiểu** đối với code mình đưa vào repository, chứ không chỉ đo kết quả cuối cùng.

* **Đánh giá trên sản phẩm thật:** mọi cột điểm lớn đều gắn với dự án Smart Event Hub, chạy được trên trình duyệt và (từ Buổi 11) trên Vercel.
* **Minh chứng bằng dữ liệu:** Git log, Pull Request, kết quả `npm run build`, điểm Lighthouse là căn cứ khách quan, khó "làm đẹp" vào phút chót.
* **Tách điểm nhóm và điểm cá nhân:** sản phẩm chung chấm cho nhóm; phần Git commit và phản biện code chấm riêng từng người.
* **Phản hồi sớm, phản hồi thường xuyên:** sinh viên biết mình đang ở đâu sau mỗi buổi, không phải chờ đến Buổi 12.

---

### 2. Cơ cấu điểm học phần

**Điểm học phần = Quá trình × 0.3 + Giữa kỳ × 0.3 + Cuối kỳ × 0.4** (thang 10; đạt khi ≥ 4.0 và tham gia đủ Buổi 7, Buổi 12).

| Thành phần | Tỷ lệ | Nội dung | Thời điểm | CLO |
|---|---|---|---|---|
| Quá trình – Quiz trước giờ | 10% | 10 bài Quiz LMS (Bài 01–06, 08–11), 10 câu/bài | Trước mỗi buổi học | CLO1, CLO2, CLO4 |
| Quá trình – Bài tập về nhà | 10% | BTVN cá nhân nộp qua Pull Request + link trên LMS | Sau Buổi 1–11 | CLO1, CLO2, CLO4 |
| Quá trình – Tham gia trên lớp | 10% | Guided, Unguided, Team Challenge, phiếu Cross-Testing | Mỗi buổi | CLO2, CLO4 |
| Giữa kỳ | 30% | Báo cáo tiến độ 50% dự án, demo 10' + phản biện 5' | Buổi 7 | CLO1, CLO2, CLO4 |
| Cuối kỳ | 40% | Thi Hackathon & Final Showcase, demo 8' + Q&A 5' | Buổi 12 | CLO1, CLO2, CLO3, CLO4 |

> 💡 **Điểm thưởng Vibe Coding xuất sắc** (+0.5 đến +1.0) được cộng vào **Điểm Quá trình**, tổng sau khi cộng không vượt quá 10. Tiêu chí chi tiết xem `rubric-hackathon-cuoi-ky.md`, mục 4.

**Cách tính Điểm Quá trình (thang 10):**

```text
Điểm Quá trình = (TB Quiz × 1/3) + (TB BTVN × 1/3) + (Điểm tham gia × 1/3) + Điểm thưởng   (tối đa 10)
```

---

### 3. Lịch đánh giá theo buổi

| Buổi | Hoạt động đánh giá | Hình thức | Minh chứng / Công cụ | CLO |
|---|---|---|---|---|
| 01 | Quiz 01, BTVN: 3 component tĩnh (Footer, Badge, Search Bar) | Cá nhân | Quiz LMS, GitHub PR | CLO1, CLO2 |
| 02 | Quiz 02, BTVN: 5 Wireframe Figma + cấu trúc component | Cá nhân/Nhóm | Quiz LMS, link Figma | CLO1 |
| 03 | Quiz 03, BTVN: trang 404 + Loading Skeleton | Cá nhân | Quiz LMS, GitHub PR | CLO2 |
| 04 | Quiz 04, BTVN: tổ chức `/components/ui`, `/components/shared` | Cá nhân | Quiz LMS, GitHub PR | CLO2 |
| 05 | Quiz 05, BTVN: kiểm tra responsive 5 màn hình | Cá nhân | Quiz LMS, ảnh chụp DevTools | CLO2 |
| 06 | Quiz 06, BTVN: chuẩn bị slide, Wireframe, source cho giữa kỳ | Nhóm | Quiz LMS, repository | CLO2 |
| **07** | **Kiểm tra giữa kỳ (30%)** | Nhóm + cá nhân | `npm run build`, README, Git log, Figma | CLO1, CLO2, CLO4 |
| 08 | Quiz 08, BTVN: Loading Spinner, Error Boundary khi API lỗi | Cá nhân | Quiz LMS, GitHub PR | CLO2 |
| 09 | Quiz 09, BTVN: đăng ký Vercel, kết nối GitHub repo | Cá nhân | Quiz LMS, ảnh chụp Vercel | CLO2, CLO4 |
| 10 | Quiz 10, nghiệm thu tại máy, BTVN: kịch bản Test Case | Nhóm | Quiz LMS, file Test Case | CLO2, CLO4 |
| 11 | Quiz 11, link Vercel Live, BTVN: báo cáo Word/PDF + slide | Nhóm | Vercel, Lighthouse, báo cáo | CLO3, CLO4 |
| **12** | **Thi Hackathon & Final Showcase (40%)** | Nhóm + cá nhân | Vercel Live, Lighthouse, Git log, báo cáo | CLO1–CLO4 |

---

### 4. Công cụ đánh giá & cách giảng viên sử dụng

#### 4.1. Quiz LMS (Moodle)

* Câu hỏi nhập theo định dạng Aiken (thư mục `quiz/`), mỗi bài 10–12 câu, trộn câu hỏi và phương án.
* Cấu hình: 15 phút, tối đa 2 lần làm, lấy điểm cao nhất; mở sau buổi trước và đóng khi buổi học bắt đầu.
* Lớp học phần dùng chung một khóa Moodle thì dùng **Group overrides** để đặt giờ mở/đóng riêng theo lịch của từng lớp.

#### 4.2. Git log & GitHub

Git log là minh chứng chính cho tiêu chí đóng góp cá nhân ở cả giữa kỳ và cuối kỳ. Giảng viên có thể kiểm tra nhanh bằng các lệnh sau trên bản clone của nhóm:

```bash
# Số commit của từng thành viên (gộp theo tên + email)
git shortlog -sne --no-merges

# Lịch sử commit của một sinh viên, kèm file đã sửa
git log --author="nguyenvana" --stat --no-merges

# Kiểm tra phiên bản đã nộp đúng tag
git checkout v0.5-midterm
```

* Đối chiếu thêm tab **Insights → Contributors** và danh sách **Pull Requests** (ai mở, ai review, ai merge).
* Dấu hiệu cần hỏi kỹ khi phản biện: một người chiếm gần hết commit; commit dồn trong đêm trước buổi đánh giá; commit chỉ đổi định dạng hoặc đổi tên biến.

#### 4.3. Production build & chất lượng code

```bash
npm run lint
npm run build
```

* Build thất bại tại thời điểm chấm giữa kỳ → tiêu chí UI không vượt quá mức Trung bình.
* Giảng viên mở DevTools Console khi nhóm demo; lỗi đỏ hoặc hydration mismatch được ghi vào phiếu chấm.

#### 4.4. Vercel

* Link Vercel Live là điều kiện để chấm tiêu chí 4 (Deploy) của Hackathon. Ứng dụng chỉ chạy localhost thì tiêu chí này ở mức Yếu.
* Kiểm tra tab **Deployments**: deploy từ nhánh `main`, biến môi trường `NEXT_PUBLIC_API_URL` được cấu hình, không còn build lỗi.

#### 4.5. Google Lighthouse

* Chạy trên Chrome DevTools (chế độ Incognito, thiết bị Mobile) với link Vercel, không chạy trên localhost.
* Nhóm chụp kết quả 4 chỉ số (Performance, Accessibility, Best Practices, SEO) đưa vào báo cáo; giảng viên chạy lại ngẫu nhiên một trang khi chấm.
* Mốc chấm: Performance > 85 và SEO > 90 (Xuất sắc) · 70–84 (Khá) · 50–69 (Trung bình) · < 50 (Yếu). Đạt 100/100 Performance được xét điểm thưởng Ultra Performance.

#### 4.6. Figma & README

* Figma: kiểm tra đủ 5 màn hình (Trang chủ, Chi tiết sự kiện, Đặt vé, Trang cá nhân, Admin Dashboard) và mức khớp giữa bản vẽ với sản phẩm.
* README: mô tả dự án, bảng phân công, hướng dẫn cài đặt, cấu trúc thư mục, link Figma, mục **Nhật ký Vibe Coding** (prompt chính + phần đã sửa).

---

### 5. Cơ chế phản hồi cho sinh viên

| Hoạt động | Hình thức phản hồi | Thời hạn | Kênh |
|---|---|---|---|
| Quiz LMS | Điểm + giải thích đáp án tự động | Ngay khi Quiz đóng | Moodle |
| BTVN | Nhận xét trên Pull Request (review comment) hoặc LMS | Trước buổi học kế tiếp | GitHub, Moodle |
| Team Challenge | Nhận xét trực tiếp tại máy, tổng kết chung 15' cuối buổi | Trong buổi học | Trên lớp |
| Giữa kỳ | Phiếu chấm rubric + 2–3 việc cần sửa trước Buổi 8 | Trước Buổi 8 | Moodle (Feedback file) |
| Buổi 10 (PBL 1) | Nghiệm thu tiến độ tại máy, danh sách lỗi cần xử lý | Cuối Buổi 10 | Trên lớp |
| Cross-Testing | Phiếu góp ý từ nhóm bạn (bug, điểm mạnh, gợi ý) | Trong Buổi 12 | Phiếu giấy/Google Form |
| Hackathon | Điểm nhóm, điểm phản biện cá nhân, nhận xét hội đồng | Công bố cuối Buổi 12 | Trên lớp, Moodle Gradebook |

> 🧭 **Vòng phản hồi giữa kỳ:** góp ý ở Buổi 7 không chỉ để biết điểm. Các bạn đưa từng góp ý thành một **GitHub Issue** có nhãn `midterm-feedback`, đóng Issue bằng commit sửa lỗi. Giảng viên sẽ kiểm tra danh sách Issue này khi chấm tiêu chí 5 (Báo cáo & Git) ở Buổi 12.

---

### 6. Đảm bảo công bằng & nhất quán

* **Rubric công bố từ Buổi 1** trên LMS, sinh viên dùng chính rubric đó để tự đánh giá trước mỗi mốc (`tu-danh-gia-va-danh-gia-cheo.md`).
* **Chấm theo tag:** giảng viên chấm đúng commit gắn tag `v0.5-midterm` / `v1.0-final`, tránh tình trạng sửa code trong lúc chấm.
* **Hội đồng Hackathon:** nếu có từ 2 giảng viên trở lên, điểm nhóm là trung bình cộng; chênh lệch một tiêu chí quá 1 mức thì hội đồng thống nhất lại.
* **Phiếu đánh giá đồng đẳng** chỉ dùng làm căn cứ tham khảo để đặt câu hỏi phản biện, không tự động thay đổi điểm. Điểm cá nhân vẫn tính theo công thức Nhóm × 0.7 + Phản biện × 0.3.

---

### ❓ Tự kiểm tra nhanh

**Câu hỏi:** Nhóm của bạn đạt Điểm Đồ án Nhóm 7.5, bạn đạt Điểm Phản biện Cá nhân 9.0. Điểm Cuối kỳ của bạn là bao nhiêu?

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án:</b> 7.95<br>
<b>Giải thích:</b> 7.5 × 0.7 + 9.0 × 0.3 = 5.25 + 2.7 = 7.95. Phần phản biện cá nhân giúp bạn kéo điểm lên khi nắm vững phần code mình đảm nhiệm.
</details>
