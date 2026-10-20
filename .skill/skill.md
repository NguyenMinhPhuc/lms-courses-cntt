---
name: lms-lecture-builder
description: Directives, formatting rules, anti-AI detector guidelines, and output templates for generating standardized, high-quality LMS lecture modules from raw course materials. Automatically triggers when user asks to create, convert, or format content for LMS (Moodle, Canvas, Blackboard).
---

# LMS Lecture Builder & Content Structuring Skill

Bộ quy tắc và tiêu chuẩn bắt buộc AI tuân thủ khi soạn thảo, cấu trúc hóa và định dạng nội dung bài giảng cho các học phần trên hệ thống LMS (Learning Management System).

---

## 0. Quy tắc Kích hoạt & Nhận diện (Detection Rules)

AI **BẮT BUỘC** tự động áp dụng toàn bộ quy tắc và khung template trong Skill này khi phát hiện một trong các dấu hiệu hoặc từ khóa (Triggers) sau:
1. **Từ khóa trực tiếp:** `soạn bài giảng LMS`, `LMS template`, `tạo module Moodle`, `Canvas page builder`, `bài giảng e-learning`.
2. **Yêu cầu công việc:** Người dùng cung cấp tài liệu thô (slide, giáo trình, outline) và yêu cầu chuyển đổi thành bài giảng lên hệ thống học tập trực tuyến.
3. **Ngữ cảnh:** Soạn nội dung các mục: *Mục tiêu bài học, Nội dung cốt lõi, Hoạt động học tập, Bài tập củng cố, Câu hỏi thảo luận LMS*.

---

## 1. Quy tắc Viết Văn phong Chống AI Detector (Humanize Content)

Để đảm bảo bài giảng tự nhiên, sư phạm, giàu tính tương tác và tránh các công cụ quét văn bản AI (Turnitin, ZeroGPT):

### 1.1. Tăng độ biến thiên cấu trúc câu (Burstiness & Perplexity)
* **Đan xen độ dài câu:** Linh hoạt giữa câu ngắn hướng dẫn hành động (dưới 12 từ) và câu phân tích lý thuyết/ví dụ thực tế (25–35 từ).
* **Văn phong sư phạm chủ động:** Dùng đại từ xưng hô giảng dạy tự nhiên (ví dụ: *"Trong phần này, chúng ta sẽ...", "Hãy quan sát ví dụ dưới đây trước khi..."*).
* **Tránh cấu trúc lặp:** Không bắt đầu 3 câu liên tiếp cùng một mô-típ (e.g., liên tục dùng *"Nội dung này giúp...", "Bài học này cung cấp..."*).

### 1.2. Loại bỏ từ ngữ đặc trưng của AI (AI Buzzwords)
* **KHÔNG dùng các từ sáo rỗng:**
  * *Tiếng Việt:* "Đóng vai trò then chốt", "Bức tranh toàn cảnh", "Trụ cột vững chắc", "Làm sáng tỏ", "Đi sâu vào phân tích", "Mang tính cách mạng".
  * *Tiếng Anh:* "Delve into", "In today's fast-paced world", "Beacon", "Tapestry", "Crucial milestone", "Testament".
* **Thay bằng ngôn ngữ sư phạm thực tiễn:** Đi thẳng vào khái niệm, thao tác thực hành, tình huống thực tế và câu hỏi gợi mở tư duy.

---

## 2. Quy tắc Định dạng LMS (LMS-Friendly Formatting)

1. **Sử dụng chuẩn Markdown / HTML sạch:** Không dùng các đoạn mã phức tạp dễ bị LMS chặn (như JavaScript thô, CSS inline quá rối).
2. **Chia nhỏ nội dung (Chunking):** Mỗi mục không dài quá 300 từ. Dùng `Callout box`, `Quote`, `Bold` để làm nổi bật khái niệm quan trọng.
3. **Thêm thành phần tương tác:** Mỗi bài giảng LMS phải chứa ít nhất: 1 câu hỏi dẫn dắt (Hook), 1 ví dụ thực tế (Case study/Example), và 1 hoạt động tự đánh giá (Self-check question).

---

## 3. Khung Template Mẫu Bài giảng LMS (Mandatory Output Template)

Khi xuất nội dung bài giảng, AI **BẮT BUỘC** trình bày chính xác theo cấu trúc Template dưới đây:

# [TÊN HỌC PHẦN]
## CHƯƠNG [X]: [TÊN CHƯƠNG]
### Bài [Y]: [Tên bài giảng]

---

> 🎯 **MỤC TIÊU BÀI HỌC (Learning Objectives)**
> Sau khi hoàn thành bài học này, người học có thể:
> * **[Bloom 1/2 - Kiến thức]:** Trình bày/Giải thích được...
> * **[Bloom 3/4 - Kỹ năng]:** Phân tích/Áp dụng được...
> * **[Bloom 5/6 - Năng lực]:** Đánh giá/Thực hiện được...

---

### 📝 1. ĐẶT VẤN ĐỀ & DẪN NHẬP (Introduction / Hook)
*(Viết 1-2 đoạn ngắn mô tả tình huống thực tế hoặc đặt ra bài toán thực tiễn để kích thích tư duy người học trước khi vào bài)*

---

### 📖 2. NỘI DUNG CỐT LÕI (Core Content)

#### 2.1. [Tên khái niệm / Nội dung 1]
* **Khái niệm:** *(Trình bày ngắn gọn, súc tích)*
* **Chi tiết kỹ thuật / Lý thuyết:**
  * Point 1: ...
  * Point 2: ...
* **💡 Ví dụ thực tế (Real-world Example):**
  > *(Mô tả ví dụ cụ thể, dễ hiểu)*

#### 2.2. [Tên khái niệm / Nội dung 2]
*(Trình bày tương tự, có chia mục rõ ràng)*

---

### 📌 3. TÓM TẮT & ĐIỂM CẦN NHỚ (Key Takeaways)
* 🔹 **Điểm 1:** ...
* 🔹 **Điểm 2:** ...
* 🔹 **Điểm 3:** ...

---

### ❓ 4. HOẠT ĐỘNG KIỂM TRA NHANH (Self-Assessment / Quiz)

**Câu 1:** [Nội dung câu hỏi trắc nghiệm/tình huống]
- A. [Phương án A]
- B. [Phương án B]
- C. [Phương án C]
- D. [Phương án D]

<details>
<summary>👉 Bấm vào đây để xem Đáp án & Giải thích</summary>
<b>Đáp án đúng:</b> [X]<br>
<b>Giải thích:</b> [Lý do ngắn gọn tại sao chọn đáp án này]
</details>

---

### 💬 5. NHIỆM VỤ HỌC TẬP & THẢO LUẬN (LMS Discussion / Assignment)
* **Chủ đề thảo luận Diễn đàn (Forum Discussion):** *(Đặt câu hỏi mở yêu cầu người học phân tích/chia sẻ quan điểm)*
* **Yêu cầu nộp bài (Nếu có):** *(Mô tả ngắn gọn yêu cầu bài tập cá nhân/nhóm)*

## YÊU cầu về thành phần file
1. Mỗi học phần phải có phần QUIZ - chứa file câu hỏi trắc nghiệm theo từng bài (mỗi bài tối thiểu 10 câu)
2. Mỗi học phần phải có phần DISCUSSION - chứa nội dung thảo luận và hoạt động nhóm.
3. Mỗi học phần phải có phần ASSIGNMENT - chứa các bài tập và nhiệm vụ cụ thể cho người học.
4. Mỗi học phần phải có phần RESOURCES - chứa các tài nguyên hỗ trợ học tập như tài liệu, video, link tham khảo.
5. Mỗi học phần phải có phần ASSESSMENT - chứa các công cụ đánh giá và phản hồi cho người học.
6. Mỗi học phần phải có phần DOCUMENTATION - chứa các tài liệu hướng dẫn sử dụng và thông tin chi tiết về nội dung học.
7. có file bai-hoc??.md và file bai-hoc??.html
8. có file index.html để tổng hợp nội dung bài học (landing-page)

