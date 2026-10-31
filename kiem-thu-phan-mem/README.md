# Học phần: Kiểm thử và Đảm bảo chất lượng phần mềm (Software Testing)

- **Mã học phần:** 111117
- **Khoa phụ trách:** Khoa Công nghệ Thông tin - Trường Đại học Lạc Hồng
- **Số tín chỉ:** 3 TC — 45 tiết (15 tiết lý thuyết + 30 tiết thực hành)
- **Giảng viên, lịch học:** theo thông báo của lớp trên Moodle
- **Định dạng hiển thị LMS:** Accordion HTML 4 khối theo [template-lesson.md](../template-lesson.md)
- **Đề cương:** [thong-tin-hoc-phan.html](thong-tin-hoc-phan.html) (xem web) | [thong-tin-hoc-phan.md](thong-tin-hoc-phan.md) (dán vào Moodle)
- **Đánh giá & Rubric:** [danh-gia-hoc-phan.html](danh-gia-hoc-phan.html) | [danh-gia-hoc-phan.md](danh-gia-hoc-phan.md)
- **Trang học phần:** [index.html](index.html)

Học phần tập trung vào quy trình kiểm thử thủ công: hiểu yêu cầu → lập kế hoạch → thiết kế kiểm thử → thực thi và ghi nhận lỗi → đánh giá và báo cáo. Todo App được dùng xuyên suốt làm ví dụ; Notepad Cải Tiến minh họa yêu cầu sản phẩm.

---

## 1. Mục tiêu học tập

Sau học phần, sinh viên có thể:

1. Giải thích vai trò của kiểm thử đối với chất lượng và rủi ro sản phẩm.
2. Phân tích mô tả sản phẩm để xác định yêu cầu kiểm thử chức năng và phi chức năng.
3. Lập Test Plan cơ bản gồm phạm vi, phương pháp, nguồn lực, tiêu chí và rủi ro.
4. Thiết kế test case có tiền điều kiện, dữ liệu, các bước và kết quả mong đợi rõ ràng.
5. Thực thi kiểm thử, ghi lại kết quả và mô tả lỗi có thể tái hiện.
6. Liên kết yêu cầu, test case, kết quả và lỗi để đánh giá độ bao phủ.
7. Tổng hợp kết quả thành Test Report chính xác, nêu rủi ro và khuyến nghị.

---

## 2. Danh sách bài học

| Bài | Tên bài | Trọng tâm | File |
| :---: | :--- | :--- | :---: |
| 01 | Giới thiệu về kiểm thử phần mềm | Vai trò, hộp đen/trắng/xám, cấp độ kiểm thử, khi nào kiểm thử thủ công | [bai-01.md](bai-01.md) |
| 02 | Xây dựng Test Plan | Phạm vi, nguồn lực, tiêu chí bắt đầu/hoàn thành, rủi ro | [bai-02.md](bai-02.md) |
| 03 | Xác định yêu cầu kiểm thử | Yêu cầu chức năng/phi chức năng, viết yêu cầu kiểm chứng được, RTM | [bai-03.md](bai-03.md) |
| 04 | Test Case và cách xây dựng | Cấu trúc test case, trường hợp bình thường/lỗi/biên | [bai-04.md](bai-04.md) |
| 05 | Thực hiện báo cáo kiểm thử | Thành phần Test Report, tính tỷ lệ Pass/Fail, khuyến nghị | [bai-05.md](bai-05.md) |
| 06 | Nhận diện và phân loại lỗi phần mềm | UI/UX, chức năng, đầu vào, hiệu năng, bảo mật, tích hợp | [bai-06.md](bai-06.md) |
| 07 | Tổng hợp biểu mẫu kiểm thử | Test Plan, TR, RTM, Test Case, Execution Log, Bug Report, Test Report | [bai-07.md](bai-07.md) |
| 08 | Hướng dẫn báo cáo cuối kỳ | Sản phẩm nộp, cấu trúc báo cáo, kế hoạch 3 tuần, rubric | [bai-08.md](bai-08.md) |

Mỗi bài gồm 4 khối: `📘 Tổng quan`, `📚 Học liệu chính`, `💡 Hoạt động & Thực hành`, `🆘 Trợ giúp và mở rộng`.

---

## 3. Đánh giá

| Thành phần | Tỷ trọng |
| :--- | :---: |
| Điểm quá trình | 30% |
| Điểm thực hành | 30% |
| Báo cáo cuối kỳ theo nhóm (báo cáo viết 30% + thuyết trình 10%) | 40% |

Rubric chi tiết tại [danh-gia-hoc-phan.md](danh-gia-hoc-phan.md).

---

## 4. Ngân hàng câu hỏi (Aiken)

80 câu trắc nghiệm (10 câu/bài) trong thư mục [quiz/](quiz/):

- `quiz/quiz-bai-01-aiken.txt` … `quiz/quiz-bai-08-aiken.txt`: mỗi bài một file.
- `quiz/tong-hop-80-cau-quiz-aiken.txt`: gộp toàn bộ để import một lần.

**Import vào Moodle:** Question bank → Import → chọn **Aiken format** → chọn Category → kéo thả file `.txt` (UTF-8) → Import.

---

## 5. Học liệu khác trong thư mục

| Thư mục / file | Nội dung |
| :--- | :--- |
| `Slides/` | Slide bài giảng 1–5 (PPTX + ghi chú Markdown) và tài liệu bổ sung |
| `Report/` | Quy định báo cáo cuối kỳ và hướng dẫn cho trưởng nhóm |
| `Examples/` | Bài tập nhóm và lời giải mẫu kiểm thử thủ công Todo App |
| `01_PRD_Notepad_CaiTien.md_TiengViet.md` | PRD Notepad Cải Tiến dùng làm ví dụ |
| `02_TestRequirements_References.md`, `03 - Test Case.md` | Tài liệu tham khảo yêu cầu kiểm thử và test case |
| `Test_Report_Notepad_CaiTien.markdown` | Ví dụ Test Report |

---

## 6. Cập nhật nội dung

Chỉ sửa các file `.md`, sau đó chạy ở thư mục gốc repo:

```bash
uv run python build-lessons.py kiem-thu-phan-mem     # sinh bai-XX.html, thong-tin-hoc-phan.html, danh-gia-hoc-phan.html
uv run python build-quiz.py kiem-thu-phan-mem        # ghép file quiz tổng hợp
uv run python validate-course.py kiem-thu-phan-mem   # kiểm tra học phần
```
