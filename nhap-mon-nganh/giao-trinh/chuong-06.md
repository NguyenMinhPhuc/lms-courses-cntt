# Chương 6. Đọc, tóm tắt và ghi nhớ tài liệu với AI

## Mục tiêu chương

Sau khi học xong chương này, bạn có thể:

- Yêu cầu AI tóm tắt một tài liệu theo nhiều cấp độ phù hợp với mục đích học tập.
- Trích xuất thuật ngữ, lập đề cương và sơ đồ khái niệm từ một chương sách.
- Áp dụng phương pháp học chủ động (tự kiểm tra) và lặp lại ngắt quãng với flashcard do AI hỗ trợ tạo.
- Tổ chức các cuộc trò chuyện với AI và tài liệu học tập theo môn học để tra cứu lại nhanh.
- Kiểm tra được độ chính xác và độ đầy đủ của bản tóm tắt do AI tạo ra.

## 6.1. Tóm tắt tài liệu nhiều cấp độ

### 6.1.1. Đưa tài liệu cho AI

Có ba cách đưa nội dung cần tóm tắt cho AI:

- **Dán văn bản** vào ô trò chuyện. Với tài liệu dài, chia thành từng phần khoảng 1.000–1.500 từ để không vượt giới hạn ngữ cảnh của công cụ.
- **Tải tệp lên** (PDF, Word) với các công cụ hỗ trợ đọc tệp. NotebookLM được thiết kế riêng cho việc này: câu trả lời dựa trên các tài liệu bạn tải lên và chỉ ra vị trí trong tài liệu (Chương 5, Bảng 5.1).
- **Nêu tên tài liệu** ("tóm tắt chương 1 của cuốn sách X"). Cách này **rủi ro nhất**: nếu AI không có nội dung cuốn sách, nó có thể tạo ra một bản tóm tắt nghe hợp lý nhưng sai. Chỉ dùng để định hướng trước khi đọc, không dùng để thay việc đọc.

Giáo trình [1] nhấn mạnh: tóm tắt giúp tiết kiệm thời gian, nhưng sau khi có bản tóm tắt, bạn vẫn phải đối chiếu với tài liệu gốc.

### 6.1.2. Chọn mức độ tóm tắt

Tùy mục đích, hãy yêu cầu mức độ tóm tắt khác nhau [1]:

| Mức độ | Khi nào dùng | Prompt mẫu |
|---|---|---|
| Siêu ngắn (3 ý then chốt) | Xem nhanh tài liệu có đáng đọc kỹ không | "Tóm tắt tài liệu sau thành đúng 3 gạch đầu dòng, mỗi dòng không quá 20 từ." |
| Ngắn (khoảng 50 từ) | Ghi chú nhanh sau giờ học | "Tóm tắt đoạn văn sau trong khoảng 50 từ." |
| Có cấu trúc | Hiểu lập luận của bài báo, chương sách | "Tóm tắt theo cấu trúc: Vấn đề → Luận điểm chính → Dẫn chứng → Kết luận." |
| Chi tiết (khoảng 200 từ trở lên) | Ôn thi, viết tổng quan tài liệu | "Tóm tắt chi tiết trong khoảng 200 từ, giữ lại các định nghĩa và ví dụ quan trọng." |

*Bảng 6.1. Các mức độ tóm tắt.*

**Ví dụ 6.1** [1]. Đoạn văn: "Deep learning là một nhánh của machine learning sử dụng mạng nơ-ron sâu để thực hiện các tác vụ phức tạp như xử lý hình ảnh và ngôn ngữ tự nhiên. Phương pháp này đã mang lại những đột phá trong nhiều lĩnh vực như xe tự lái, nhận diện giọng nói và trí tuệ nhân tạo. Mạng nơ-ron sâu bao gồm nhiều lớp kết nối, cho phép học từ dữ liệu lớn và phức tạp."

Yêu cầu tóm tắt trong khoảng 30 từ có thể cho kết quả: "Deep learning là nhánh của machine learning dùng mạng nơ-ron nhiều lớp để học từ dữ liệu lớn, tạo đột phá trong xử lý ảnh, ngôn ngữ, xe tự lái."

### 6.1.3. Kiểm tra bản tóm tắt

Bản tóm tắt có thể bỏ sót ý quan trọng, đổi nghĩa hoặc thêm thông tin không có trong tài liệu gốc. Trước khi dùng, hãy tự kiểm tra:

1. Mỗi ý trong bản tóm tắt có xuất hiện trong tài liệu gốc không? Ý nào không tìm thấy thì xóa.
2. Các tiêu đề lớn của tài liệu có được đại diện trong bản tóm tắt không?
3. Số liệu, tên riêng, định nghĩa có giữ đúng như bản gốc không?

Một cách nhanh là yêu cầu AI tự chỉ nguồn: "Với mỗi ý, trích câu tương ứng trong tài liệu gốc." Ý nào AI không trích được câu gốc là ý cần nghi ngờ.

## 6.2. Trích xuất thuật ngữ và lập đề cương

### 6.2.1. Bảng thuật ngữ

Sinh viên năm nhất gặp rất nhiều thuật ngữ mới. Hãy dùng AI để lập bảng thuật ngữ cho từng chương:

```text
Từ tài liệu dưới đây, lập bảng thuật ngữ gồm các cột:
Thuật ngữ (tiếng Anh) | Thuật ngữ tiếng Việt | Định nghĩa ngắn (không quá 25 từ) | Ví dụ.
Chỉ lấy thuật ngữ có trong tài liệu, không thêm thuật ngữ bên ngoài.
[dán tài liệu]
```

Câu cuối của prompt ("chỉ lấy thuật ngữ có trong tài liệu") giới hạn AI trong nội dung bạn cung cấp, giảm nguy cơ AI tự thêm định nghĩa không đúng ngữ cảnh môn học.

### 6.2.2. Đề cương bài học

AI giúp chuyển một chương sách dài thành đề cương phân cấp, ví dụ đề cương môn Hệ điều hành gồm ba mảng: quản lý tiến trình, quản lý bộ nhớ, quản lý hệ thống tệp [1]. Đề cương do AI tạo cần được bạn **đối chiếu với đề cương môn học** do giảng viên công bố: trọng tâm thi là đề cương môn học, không phải đề cương AI đề xuất.

### 6.2.3. Sơ đồ khái niệm

Bạn có thể yêu cầu AI biểu diễn quan hệ giữa các khái niệm dưới dạng sơ đồ bằng văn bản (ví dụ cú pháp Mermaid), rồi dán vào công cụ hỗ trợ để xem hình:

```text
Vẽ sơ đồ khái niệm cho chương "Thuật toán sắp xếp" bằng cú pháp Mermaid (flowchart).
Nút gốc là "Sắp xếp", các nhánh là từng thuật toán, mỗi thuật toán có nút con nêu ý tưởng chính.
```

Việc tự sửa lại sơ đồ cho đúng là một cách ôn tập: bạn phải hiểu quan hệ giữa các khái niệm mới sửa được.

## 6.3. Học chủ động: tự kiểm tra và flashcard

### 6.3.1. Vì sao phải tự kiểm tra

Đọc lại tài liệu nhiều lần tạo cảm giác "đã hiểu", nhưng nghiên cứu tâm lý học giáo dục cho thấy **tự kiểm tra** (retrieval practice, active recall), tức là cố gắng nhớ lại kiến thức để trả lời câu hỏi, giúp ghi nhớ lâu dài tốt hơn so với chỉ đọc lại [2]. Ngoài ra, **ôn tập ngắt quãng** (spaced repetition), tức là chia việc ôn ra nhiều lần cách nhau, cho kết quả ghi nhớ tốt hơn so với dồn ôn một lần [3]. AI giúp bạn áp dụng hai phương pháp này dễ dàng hơn.

### 6.3.2. AI làm giám khảo vấn đáp

Thay vì nhờ AI giải thích thêm, hãy nhờ AI **hỏi bạn**:

```text
Bạn là giám khảo vấn đáp môn [tên môn]. Dựa trên tài liệu dưới đây, hãy hỏi tôi lần lượt từng câu,
mỗi lần một câu. Chờ tôi trả lời rồi mới nhận xét: đúng/sai, thiếu ý gì, và cho điểm trên thang 10.
Sau 5 câu, tổng kết những phần tôi cần ôn lại.
[dán tài liệu]
```

Giáo trình [1] cũng gợi ý tạo 5 câu hỏi ôn tập từ bản tóm tắt, ví dụ với chương về deep learning: Deep learning là gì? Mạng nơ-ron sâu có vai trò gì? Vì sao mạng nơ-ron sâu học được từ dữ liệu lớn? Các ứng dụng thực tế là gì?

### 6.3.3. Flashcard và ôn tập ngắt quãng

Flashcard (thẻ ghi nhớ) có mặt trước là câu hỏi hoặc thuật ngữ, mặt sau là câu trả lời. AI có thể tạo bảng flashcard từ bản tóm tắt [1]:

```text
Từ tài liệu dưới đây, tạo 10 flashcard dạng bảng 2 cột: Mặt trước (câu hỏi ngắn) | Mặt sau (câu trả lời không quá 30 từ).
Xuất thêm dạng văn bản mỗi thẻ một dòng, hai mặt cách nhau bằng dấu chấm phẩy, để nhập vào Anki hoặc Quizlet.
[dán tài liệu]
```

Nhập các thẻ vào phần mềm hỗ trợ ôn tập ngắt quãng như Anki [4]: phần mềm tự xếp lịch cho thẻ bạn nhớ kém xuất hiện lại sớm hơn. Trước khi nhập, **đọc lại từng thẻ**: một thẻ sai sẽ được bạn ôn đi ôn lại nhiều lần.

## 6.4. Tổ chức hội thoại và tài liệu học tập

### 6.4.1. Đặt tên và gom nhóm cuộc trò chuyện

Sau vài tuần, lịch sử trò chuyện với AI có thể lên đến hàng trăm mục. Hãy đặt quy tắc đặt tên ngay từ đầu, ví dụ `[Môn học] - Chủ đề`:

- `[Toán rời rạc] - Lý thuyết đồ thị`
- `[Nhập môn lập trình] - Vòng lặp for`
- `[Nhập môn CNTT] - Bài tập chương 6`

Nếu công cụ có tính năng dự án hoặc thư mục, hãy tạo mỗi môn một dự án. Mỗi cuộc trò chuyện nên tập trung vào một chủ đề: hội thoại quá dài, lẫn nhiều chủ đề làm AI dễ nhầm ngữ cảnh.

### 6.4.2. Lưu kết quả có giá trị

Giáo trình [1] hướng dẫn quy trình bốn bước để lưu lại những câu trả lời hữu ích:

1. Sao chép nội dung có giá trị sau khi trò chuyện xong (đã kiểm tra, chỉnh sửa).
2. Dán vào tài liệu Google Docs hoặc Word.
3. Đặt tên tài liệu rõ ràng, ví dụ "Thuật toán sắp xếp - tóm tắt và flashcard".
4. Lưu vào thư mục riêng theo từng môn học.

Hãy ghi kèm **ngày** và **công cụ AI đã dùng** ở đầu mỗi tài liệu; khi cần trích dẫn hoặc khai báo việc dùng AI trong báo cáo (Chương 7), bạn có sẵn thông tin.

### 6.4.3. Thư viện prompt bước đầu

Khi một prompt cho kết quả tốt (ví dụ prompt flashcard ở mục 6.3.3), hãy lưu lại vào một tài liệu riêng, ghi rõ: mục đích, nội dung prompt, công cụ đã thử, ghi chú khi dùng. Đây là bước đầu của thư viện prompt cá nhân, sẽ được hoàn thiện ở Chương 8.

## Tóm tắt chương

- Đưa tài liệu cho AI bằng cách dán văn bản, tải tệp hoặc dùng NotebookLM; tránh nhờ AI tóm tắt sách chỉ qua tên sách.
- Chọn mức độ tóm tắt theo mục đích; luôn kiểm tra bản tóm tắt với tài liệu gốc.
- Bảng thuật ngữ, đề cương, sơ đồ khái niệm giúp hệ thống hóa kiến thức; đề cương chính thức của môn học là chuẩn.
- Tự kiểm tra và ôn tập ngắt quãng giúp nhớ lâu hơn đọc lại; AI có thể làm giám khảo vấn đáp và tạo flashcard.
- Tổ chức hội thoại theo môn, lưu kết quả có giá trị kèm ngày và công cụ, bắt đầu xây dựng thư viện prompt.

## Câu hỏi ôn tập

1. Vì sao yêu cầu AI tóm tắt một cuốn sách chỉ bằng tên sách là cách rủi ro?
2. Nêu bốn mức độ tóm tắt và tình huống dùng từng mức độ.
3. Trình bày ba bước kiểm tra một bản tóm tắt do AI tạo ra.
4. Câu "Chỉ lấy thuật ngữ có trong tài liệu" trong prompt có tác dụng gì?
5. Tự kiểm tra (active recall) khác đọc lại ở điểm nào? Vì sao nó giúp nhớ lâu hơn?
6. Ôn tập ngắt quãng là gì? Phần mềm như Anki hỗ trợ phương pháp này như thế nào?
7. Đề xuất quy tắc đặt tên cuộc trò chuyện cho các môn học kỳ này của bạn.

## Bài tập

1. **So sánh tóm tắt ngắn và chi tiết** [1]. Chọn một đoạn tài liệu khoảng 500 từ; yêu cầu AI tóm tắt trong 50 từ và trong 200 từ. So sánh: bản ngắn bỏ những ý nào, bản chi tiết có thêm ý nào không có trong bản gốc không.
2. **Tóm tắt và tạo câu hỏi ôn tập** [1]. Tóm tắt một bài báo hoặc một chương tài liệu môn học, tạo 5 câu hỏi ôn tập; tự trả lời và nhờ AI nhận xét.
3. **Tóm tắt tài liệu ngoại ngữ** [1]. Yêu cầu AI tóm tắt một đoạn tiếng Anh ngắn về CNTT bằng tiếng Việt; đối chiếu với bản gốc và sửa các thuật ngữ dịch chưa chuẩn.

## Tài liệu tham khảo

[1] Nguyễn Minh Phúc, *Giáo trình Áp dụng ChatGPT vào học tập và công việc*, Tài liệu lưu hành nội bộ. Đồng Nai, Việt Nam: Khoa Công nghệ Thông tin, Trường Đại học Lạc Hồng, 2024.

[2] H. L. Roediger and J. D. Karpicke, "Test-enhanced learning: Taking memory tests improves long-term retention," *Psychological Science*, vol. 17, no. 3, pp. 249–255, 2006, doi: 10.1111/j.1467-9280.2006.01693.x.

[3] N. J. Cepeda, H. Pashler, E. Vul, J. T. Wixted, and D. Rohrer, "Distributed practice in verbal recall tasks: A review and quantitative synthesis," *Psychological Bulletin*, vol. 132, no. 3, pp. 354–380, 2006, doi: 10.1037/0033-2909.132.3.354.

[4] Anki, "Anki - powerful, intelligent flashcards." Accessed: Oct. 31, 2026. [Online]. Available: https://apps.ankiweb.net
