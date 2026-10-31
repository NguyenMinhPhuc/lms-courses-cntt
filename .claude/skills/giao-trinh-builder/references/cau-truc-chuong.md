# Cấu trúc lời nói đầu và chương

Đây là quy ước của repo (Thông tư không quy định thể thức), thiết kế để đáp ứng Điều 5: khoa học, sư phạm, cân đối lý thuyết – thực hành, có nguồn hợp pháp, dùng được ở dạng in và dạng số. Mẫu tham khảo đã có: `co-so-van-hoa-viet-nam/giao-trinh/`, `lap-trinh-ung-dung-mobile/giao-trinh/`.

## `00-loi-noi-dau.md`

```markdown
# Lời nói đầu
(Mục đích giáo trình, đối tượng người học, kiến thức cần có trước, căn cứ biên soạn.)

## Cách trích dẫn giáo trình
(Một dòng IEEE để người khác trích dẫn giáo trình này.)

## Cách tổ chức tài liệu
(Bảng: chương – nội dung chính – bài giảng/buổi học tương ứng.)

## Chuẩn đầu ra và cách tài liệu rèn luyện
(Bảng CLO – chương, lấy từ đề cương chi tiết.)

## Học liệu đi kèm
(LMS, slide, quiz, mã nguồn, video: ở đâu, dùng khi nào.)

## Quy ước dùng AI
(AI hỗ trợ ở khâu nào; nhóm biên soạn đã kiểm tra lại; người học dùng AI thế nào cho đúng.)
```

## `chuong-XX.md`

Tiêu đề mục đánh số theo chương để mục lục Word đúng. `validate-course.py` kiểm tra các mục in đậm dưới đây (tên mục `##` phải bắt đầu đúng như vậy).

```markdown
# Chương X. Tên chương

## Mục tiêu chương
Sau khi học chương này, người học có thể:
- (3–5 mục tiêu đo được, gắn CLO)

## X.1. Mục lớn
### X.1.1. Mục nhỏ
Lý thuyết diễn đạt bằng lời của nhóm biên soạn, có trích dẫn [1] đặt trước dấu câu ở câu đầu của đoạn dùng nguồn [1].

**Ví dụ X.1.** Ví dụ gắn thực tiễn Việt Nam hoặc dự án mẫu của học phần.

| Bảng X.1. Tên bảng | |
|---|---|

## Tóm tắt chương
(5–8 ý chính.)

## Câu hỏi ôn tập
1. (Câu hỏi hiểu, phân tích; không chỉ hỏi định nghĩa.)

## Bài tập
1. (Bài tập vận dụng; bài tập hướng dẫn dài đặt ở bai-tap-huong-dan/bt-XX.md.)

## Tài liệu tham khảo
[1] Tác giả, *Tên sách*. Nơi xuất bản: Nhà xuất bản, năm.

[2] Tổ chức, “Tên trang,” *Tên website*. Accessed: Mon. DD, YYYY. [Online]. Available: URL
```

## Quy tắc nội dung

- **Mở rộng từ `bai-XX.md` đã duyệt:** đủ sâu để tự học (giải thích "vì sao", không chỉ liệt kê như slide), nhưng không mâu thuẫn với bài giảng.
- **Cân đối lý thuyết – thực hành (Điều 5.2):** mỗi mục lý thuyết có ít nhất một ví dụ; mỗi chương có câu hỏi ôn tập và bài tập; học phần có thực hành thì có bài tập hướng dẫn `bt-XX.md` (nhiệm vụ, chuẩn bị, các bước, kiểm tra kết quả, tiêu chí hoàn thành).
- **Cập nhật (Điều 5.1, 5.2):** công nghệ ghi rõ phiên bản; văn bản pháp luật ghi số hiệu, ngày ban hành và kiểm tra còn hiệu lực; số liệu ghi năm.
- **Trích dẫn IEEE:** mỗi chương đánh số lại từ [1]; mỗi nguồn trong danh mục phải được trích dẫn trong bài và ngược lại; không liệt kê nguồn chưa đọc.
- **Thuật ngữ:** tiếng Việt trước, thuật ngữ tiếng Anh trong ngoặc ở lần xuất hiện đầu, dùng thống nhất cả giáo trình.
- **Khả năng tiếp cận, dạng in và số (Điều 5.1):** tiêu đề phân cấp đúng (không nhảy cấp), bảng có hàng tiêu đề, hình có chú thích nói rõ nội dung (người dùng trình đọc màn hình và bản in đen trắng vẫn hiểu), không truyền đạt thông tin chỉ bằng màu, khối code ngắn: đoạn mã dài hơn 40 dòng đặt ở `phu-luc-a-ma-nguon.md` (mục `## A.k. Tên mục (Chương X)`), trong chương chỉ trích khoảng 15 dòng đầu kèm chú thích `… mã đầy đủ ở Phụ lục A, mục A.k`. `build-textbook.py` tự ghép các file `phu-luc-*.md` sau chương cuối.
- **Hình ảnh:** sơ đồ tự vẽ hoặc ảnh giấy phép mở (có thể dùng lại `Slides/images/` và `build-images.py` của skill lms-lecture-builder), ghi tác giả, giấy phép. Cú pháp: `![Hình X.Y. Chú thích mô tả nội dung hình](../Slides/images/ten-hinh.png)` trên một dòng riêng; đường dẫn tính từ thư mục `giao-trinh/` (kể cả trong `bai-tap-huong-dan/bt-XX.md`, vì file này được chèn vào chương). `build-textbook.py` đặt hình rộng tối đa 15 cm, cao tối đa 9 cm, chú thích in nghiêng bên dưới.
- **Văn phong:** học thuật nhưng dễ hiểu, câu ngắn, ngôi "người học"; theo `.claude/skills/lms-lecture-builder/references/writing-style.md`.
