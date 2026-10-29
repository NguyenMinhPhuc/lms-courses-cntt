# Ngân hàng câu hỏi Aiken (Moodle)

Ví dụ chuẩn: `nhap-mon-nganh/quiz/quiz-bai-01-aiken.txt`.

## Định dạng
```
Câu hỏi viết trên MỘT dòng duy nhất?
A. Phương án A
B. Phương án B
C. Phương án C
D. Phương án D
ANSWER: B

Câu hỏi tiếp theo...
```

Quy tắc Moodle sẽ báo lỗi nếu vi phạm:
- Câu hỏi nằm trên đúng 1 dòng; không đánh số "Câu 1:" ở đầu.
- Phương án bắt đầu bằng `A.` `B.` `C.` `D.` (chữ hoa, dấu chấm, khoảng trắng).
- Dòng `ANSWER: X` ngay sau phương án cuối; các câu cách nhau một dòng trống.
- Không dùng HTML, không xuống dòng trong phương án. File lưu UTF-8.

## Yêu cầu nội dung
- Tối thiểu **10 câu/bài**, phủ đủ 4 ý chính của khối "Tổng quan bài học".
- Phân bố mức độ: khoảng 4 câu nhớ/hiểu, 4 câu áp dụng (tình huống), 2 câu phân tích/đánh giá.
- Đáp án đúng phân bố đều A/B/C/D, không dồn vào một chữ cái.
- Phương án nhiễu hợp lý, độ dài tương đương đáp án đúng; tránh "Tất cả đều đúng/sai".
- Mọi đáp án phải kiểm chứng được từ nội dung bài học hoặc tài liệu nguồn.

## File tổng hợp và trang tải
Không ghép tay. Chạy `uv run python build-quiz.py <hoc-phan> --balance` để:
- ghép thành `quiz/tong-hop-<N>-cau-quiz-aiken.txt` (N = tổng số câu);
- sinh `quiz/index.html` để giảng viên tải từng file hoặc file tổng hợp về import (trang này có đáp án, không đưa link cho sinh viên).

## Luyện tập trực tiếp trên trang bài học
`build-lessons.py` đọc `quiz/quiz-bai-XX-aiken.txt` và thêm khung "Luyện tập trắc nghiệm" ở cuối `bai-XX.html` (khung lấy từ `templates/practice-quiz.html`). Khung này chỉ có trên trang web, không có trong `bai-XX.md` dán vào Moodle.
- Thứ tự câu hỏi và phương án được xáo mỗi lần làm.
- Nộp bài chỉ hiện số câu **Đúng / Sai / Bỏ trống** và tỷ lệ; không chỉ ra câu nào sai, không hiện đáp án.
- Không lưu kết quả (không localStorage, không gửi đi đâu); tải lại trang là làm lại từ đầu.
- Đáp án trong mã nguồn trang chỉ được mã hóa nhẹ. Đây là bài luyện tập, **không dùng thay cho kiểm tra có tính điểm**; bài có tính điểm phải làm trên Moodle.

Vì vậy câu hỏi phải tự đứng được: không viết "câu trên", "như câu 3", vì thứ tự sẽ bị xáo.
