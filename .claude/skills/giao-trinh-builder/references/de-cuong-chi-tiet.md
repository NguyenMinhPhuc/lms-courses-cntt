# Đề cương chi tiết giáo trình (`ho-so/01-de-cuong-chi-tiet.md`)

Bước 1 của Điều 7 khoản 2. Đề cương là "hợp đồng" nội dung giữa nhóm biên soạn và người duyệt: viết xong phải **dừng chờ duyệt** rồi mới biên soạn chương.

Căn cứ: đề cương học phần (CLO, nội dung, số tiết), `course.json`, danh sách bài `bai-XX.md`, giáo trình chính đang dùng. Mục nào thiếu thông tin thì để `{{...}}`, không tự điền.

## Mẫu

```markdown
# Đề cương chi tiết giáo trình

## 1. Thông tin chung

| Mục | Nội dung |
|---|---|
| Tên giáo trình | {{Tên}} |
| Loại tài liệu | Giáo trình / Tài liệu học tập |
| Học phần | Tên (mã), số tín chỉ (LT/TH) |
| Đối tượng người học | Ngành, năm học, kiến thức cần có trước |
| Chủ biên | {{Họ tên, học hàm, học vị, đơn vị}} |
| Người biên soạn | {{...}} |
| Ngôn ngữ | Tiếng Việt |
| Hình thức khai thác | Bản in và bản số (Word/PDF), kèm học liệu số trên LMS |
| Căn cứ | Đề cương học phần {{số/năm}}; Thông tư 62/2026/TT-BGDĐT; {{quy định nội bộ của Trường, nếu có}} |

## 2. Mục tiêu của giáo trình
Hai đến bốn câu: giáo trình giúp người học đạt chuẩn đầu ra nào của học phần, khác/bổ sung gì so với tài liệu đang có.

## 3. Ma trận chương – chuẩn đầu ra học phần

| Chương | CLO1 | CLO2 | CLO3 | CLO4 |
|---|:-:|:-:|:-:|:-:|
| 1. ... | x | | | |

Mỗi CLO có ít nhất một chương đáp ứng; mỗi chương phục vụ ít nhất một CLO.

## 4. Nội dung chi tiết

### Chương 1. Tên chương
- **Mục tiêu:** 3–5 mục tiêu đo được (động từ Bloom: trình bày, phân tích, vận dụng…).
- **Nội dung:** mục cấp 1 (1.1, 1.2…) và cấp 2 (1.1.1…), mỗi mục một dòng mô tả.
- **Thực hành / ví dụ:** ví dụ minh họa, bài tập, bài tập hướng dẫn (nếu có).
- **Liên kết học liệu:** bài giảng `bai-01`, slide, quiz.
- **Dung lượng dự kiến:** {{số trang}}; tỷ lệ LT/TH.

(lặp cho các chương)

## 5. Cân đối lý thuyết – thực hành
Bảng số trang hoặc tỷ lệ % theo chương; giải thích ngắn nếu chương nào lệch nhiều (Điều 5.2).

## 6. Tài liệu tham khảo chính
Danh sách IEEE các nguồn chính sẽ dùng (giáo trình chính, văn bản pháp luật còn hiệu lực, tài liệu chính thức của công nghệ). Ghi rõ nguồn nào cần xin phép sử dụng.

## 7. Học liệu đi kèm
Bài giảng LMS, slide, ngân hàng câu hỏi, mã nguồn mẫu, video… và cách người học truy cập (Điều 5.1: kết hợp linh hoạt với học liệu khác).

## 8. Phân công và tiến độ

| Công việc | Người phụ trách | Thời hạn |
|---|---|---|
| Duyệt đề cương | | |
| Biên soạn chương 1–3 | | |
| Lấy ý kiến góp ý | | |
| Hoàn thiện, lập hồ sơ thẩm định | | |
```

## Khi trình bày cho người dùng duyệt

Tóm tắt trong câu trả lời: số chương và tên, ma trận CLO, tỷ lệ LT/TH, các điểm cần người dùng quyết định (ví dụ gộp/tách chương, nguồn cần xin phép, thông tin hành chính còn thiếu).
