# Chương 7. Dịch thuật chuyên ngành, viết báo cáo và kiểm chứng thông tin

## Mục tiêu chương

Sau khi học xong chương này, bạn có thể:

- Dịch một đoạn tài liệu kỹ thuật tiếng Anh sang tiếng Việt với sự hỗ trợ của AI, giữ đúng thuật ngữ chuyên ngành.
- Dùng AI để phát hiện lỗi, góp ý cấu trúc và văn phong cho một bài viết mà vẫn giữ quyền tác giả của mình.
- Lập đề cương cho một báo cáo kỹ thuật, báo cáo đồ án.
- Giải thích hiện tượng ảo giác của AI và áp dụng quy trình kiểm chứng thông tin, trích dẫn.
- Khai báo minh bạch việc sử dụng AI trong bài làm theo nguyên tắc liêm chính học thuật.

## 7.1. Dịch thuật tài liệu kỹ thuật

### 7.1.1. Vì sao sinh viên CNTT cần đọc tài liệu tiếng Anh

Phần lớn tài liệu gốc của ngành (tài liệu chính thức của ngôn ngữ lập trình, thư viện, framework, bài báo khoa học) viết bằng tiếng Anh và được cập nhật trước khi có bản dịch. AI giúp bạn đọc nhanh hơn, nhưng mục tiêu dài hạn là **đọc được tài liệu gốc**: hãy dùng bản dịch như cầu nối để học thuật ngữ, không dùng như đích đến.

### 7.1.2. Văn phong và ngữ cảnh

Dịch không chỉ là chuyển từng từ: bản dịch phải truyền đúng nghĩa và phù hợp loại văn bản [1]. Văn bản văn chương cần chú ý cảm xúc, cách diễn đạt; văn bản kỹ thuật cần **chính xác, rõ ràng, nhất quán thuật ngữ**.

**Ví dụ 7.1** [1]. Câu gốc: "In the field of machine learning, overfitting occurs when a model performs well on training data but fails to generalize to unseen data."

Bản dịch: "Trong lĩnh vực học máy, hiện tượng quá khớp (overfitting) xảy ra khi mô hình hoạt động tốt trên dữ liệu huấn luyện nhưng không khái quát hóa được cho dữ liệu chưa từng thấy."

Bản dịch giữ thuật ngữ gốc *overfitting* trong ngoặc ở lần xuất hiện đầu: người đọc vừa hiểu nghĩa tiếng Việt, vừa tra cứu được tài liệu tiếng Anh.

### 7.1.3. Quy trình dịch bốn bước

Giáo trình [1] đề xuất quy trình bốn bước:

1. **Xác định ngữ cảnh và mục tiêu:** văn bản thuộc lĩnh vực nào, người đọc là ai (người mới học hay chuyên gia).
2. **Nhập văn bản và yêu cầu dịch,** kèm ngữ cảnh và yêu cầu về thuật ngữ.
3. **Kiểm tra và chỉnh sửa:** đọc bản dịch song song với bản gốc, sửa chỗ sai nghĩa, câu chưa tự nhiên.
4. **Kiểm tra thuật ngữ chuyên ngành** với từ điển chuyên ngành hoặc tài liệu chính thức.

Prompt mẫu cho bước 2:

```text
Bạn là biên dịch viên tài liệu kỹ thuật CNTT. Dịch đoạn văn sau sang tiếng Việt cho sinh viên năm nhất.
Giữ nguyên các thuật ngữ chuyên ngành tiếng Anh trong ngoặc ở lần xuất hiện đầu (ví dụ: API, framework, latency).
Sau bản dịch, lập bảng 5 thuật ngữ quan trọng nhất: Thuật ngữ | Nghĩa tiếng Việt | Giải thích ngắn.
[dán đoạn văn]
```

Một cách kiểm tra nhanh là **dịch ngược** [1]: yêu cầu AI dịch bản tiếng Việt trở lại tiếng Anh, rồi so với bản gốc. Chỗ nghĩa bị lệch nhiều là chỗ cần đọc lại.

## 7.2. Biên tập văn bản và văn phong học thuật

### 7.2.1. Phát hiện lỗi ngữ pháp, chính tả

AI phát hiện nhanh lỗi chính tả, ngữ pháp, dấu câu. **Ví dụ 7.2** (điều chỉnh từ [1]): câu "The quick brown fox jump over the lazy dog." sai **hòa hợp chủ ngữ – động từ**: chủ ngữ số ít "fox" ở thì hiện tại đơn cần động từ "jumps". Câu "She recieve the email yestarday." có lỗi chính tả (*recieve*, *yestarday*) và sai thì; câu đúng là "She received the email yesterday."

Ví dụ thứ nhất cho thấy AI có thể đề xuất nhiều cách sửa (đổi sang thì quá khứ "jumped" cũng là một câu đúng ngữ pháp). Bạn cần hiểu **vì sao** câu sai để chọn cách sửa giữ đúng ý mình.

### 7.2.2. Góp ý cấu trúc và văn phong, giữ quyền tác giả

AI có thể nhận xét bố cục bài viết (mở bài, thân bài, kết luận), đề xuất sắp xếp lại ý cho mạch lạc, và điều chỉnh văn phong theo đối tượng: văn phong báo cáo khác văn phong quảng cáo [1]. Để AI **góp ý** chứ không **viết lại toàn bộ**, hãy dùng prompt có ràng buộc:

```text
Đây là đoạn báo cáo do tôi viết. Chỉ sửa lỗi chính tả, ngữ pháp và câu lủng củng;
KHÔNG thay đổi ý, KHÔNG thêm thông tin mới.
Liệt kê từng chỗ đã sửa theo dạng: Câu gốc → Câu sửa → Lý do.
[dán đoạn văn]
```

Danh sách thay đổi giúp bạn kiểm soát từng chỗ sửa và học được lỗi của chính mình, thay vì nhận về một bài viết "đẹp" nhưng không còn là của bạn.

### 7.2.3. Đặc điểm văn phong học thuật

- Câu rõ ràng, chủ ngữ cụ thể; tránh từ cảm thán, từ ngữ quảng cáo ("cực kỳ", "đỉnh cao").
- Mỗi nhận định quan trọng có căn cứ: số liệu, kết quả thực nghiệm hoặc trích dẫn.
- Thuật ngữ dùng nhất quán trong toàn bài.
- Phân biệt rõ ý của mình và ý của người khác (trích dẫn, mục 7.4.3).

## 7.3. Đề cương báo cáo kỹ thuật

Báo cáo đồ án, báo cáo thực tập trong ngành CNTT thường theo cấu trúc:

| Phần | Nội dung chính |
|---|---|
| 1. Đặt vấn đề | Bối cảnh, vấn đề cần giải quyết, mục tiêu, phạm vi |
| 2. Tổng quan | Các giải pháp, công nghệ, nghiên cứu liên quan (có trích dẫn) |
| 3. Phân tích và thiết kế | Yêu cầu, sơ đồ chức năng, cơ sở dữ liệu, giao diện |
| 4. Cài đặt và thực nghiệm | Công cụ, quá trình xây dựng, kết quả chạy thử, kiểm thử |
| 5. Đánh giá và hướng phát triển | Kết quả đạt được so với mục tiêu, hạn chế, đề xuất |
| Tài liệu tham khảo, phụ lục | Danh mục nguồn; mã nguồn, prompt AI đã dùng, minh chứng |

*Bảng 7.1. Cấu trúc thường gặp của báo cáo kỹ thuật.*

AI có thể gợi ý đề cương chi tiết cho đề tài của bạn, nhưng **quy định định dạng của học phần và của Khoa** (khổ giấy, font, cách đánh số, cách trích dẫn) là chuẩn cuối cùng. Chương 9 hướng dẫn hoàn thiện báo cáo đồ án của học phần này.

## 7.4. Ảo giác AI và kiểm chứng thông tin

### 7.4.1. Ảo giác là gì

**Ảo giác** (hallucination) là hiện tượng mô hình sinh ra nội dung nghe hợp lý nhưng sai hoặc không có căn cứ trong dữ liệu nguồn. Một khảo sát lớn về ảo giác trong các hệ thống sinh ngôn ngữ tự nhiên xác định đây là vấn đề phổ biến của các mô hình hiện nay [2]. Các dạng ảo giác sinh viên hay gặp:

- **Nguồn dẫn không tồn tại:** tên bài báo, tác giả, DOI, đường link do AI tạo ra.
- **Số liệu bịa:** thống kê, năm tháng, phần trăm không có nguồn.
- **Mã nguồn không chạy:** gọi hàm, thư viện, tham số không tồn tại.
- **Sai lệch nội dung tài liệu:** tóm tắt có ý không có trong tài liệu gốc (Chương 6).

Giáo trình [1] cũng lưu ý: AI không thay được chuyên gia thật và không tự xác minh được thông tin nó đưa ra. Khi công cụ có tìm kiếm web, nó có thể dẫn nguồn, nhưng nguồn được dẫn vẫn cần bạn mở ra đọc.

### 7.4.2. Quy trình kiểm chứng bốn bước

1. **Tách nhận định cần kiểm chứng:** gạch chân mọi số liệu, tên riêng, trích dẫn, khẳng định quan trọng trong câu trả lời.
2. **Tìm nguồn gốc:** tài liệu chính thức, giáo trình, bài báo khoa học. Với bài báo, tra trên Google Scholar [3] hoặc theo DOI; với công nghệ, đọc tài liệu chính thức của công nghệ đó.
3. **Đối chiếu chéo:** so sánh ít nhất hai nguồn độc lập; ưu tiên nguồn gốc hơn nguồn trích lại.
4. **Ghi nhận:** nhận định đã kiểm chứng thì ghi nguồn; nhận định không kiểm chứng được thì bỏ hoặc ghi rõ là chưa xác minh.

Bảng 7.2, phát triển từ [1], so sánh thông tin từ AI với tài liệu học thuật:

| Tiêu chí | Câu trả lời của trợ lý AI | Tài liệu học thuật |
|---|---|---|
| Độ chính xác | Thường đúng ở mức khái quát, có thể sai chi tiết | Chi tiết, có trích dẫn rõ ràng |
| Độ tin cậy | Phụ thuộc dữ liệu huấn luyện, có thể ảo giác | Được chuyên gia phản biện, biên tập |
| Tính cập nhật | Có mốc thời gian kiến thức; tìm kiếm web không đảm bảo nguồn tốt | Có ngày xuất bản; nghiên cứu mới cập nhật kết quả mới |
| Khả năng truy vết | Khó biết thông tin lấy từ đâu | Ghi rõ tác giả, năm, nơi xuất bản |

*Bảng 7.2. So sánh thông tin từ AI và tài liệu học thuật.*

### 7.4.3. Giảm ảo giác bằng cách cung cấp nguồn

Một cách giảm ảo giác là **đưa tài liệu nguồn vào yêu cầu và buộc AI chỉ trả lời dựa trên tài liệu đó**. Ý tưởng này là nền tảng của kỹ thuật RAG (retrieval-augmented generation) trong các hệ thống AI, nơi mô hình truy xuất tài liệu liên quan trước khi sinh câu trả lời [4]. Với người dùng, có thể áp dụng đơn giản:

```text
Chỉ trả lời dựa trên tài liệu dưới đây. Với mỗi ý, trích câu tương ứng trong tài liệu.
Nếu tài liệu không có thông tin, trả lời "Tài liệu không đề cập", không tự suy đoán.
[dán tài liệu]
```

Cách này **giảm**, không loại bỏ hoàn toàn ảo giác; bước kiểm chứng ở mục 7.4.2 vẫn cần thiết.

## 7.5. Liêm chính học thuật khi dùng AI

### 7.5.1. Nguyên tắc

- **Trung thực về tác giả:** nội dung nộp phải thể hiện hiểu biết và công sức của bạn. Nộp nguyên văn bài do AI viết như bài của mình là vi phạm liêm chính.
- **Minh bạch:** khai báo công cụ AI đã dùng và dùng vào việc gì.
- **Ghi nguồn:** ý, số liệu, hình ảnh của người khác phải được trích dẫn, kể cả khi bạn tìm thấy chúng qua AI. AI không phải là nguồn để trích dẫn cho một sự kiện; nguồn là tài liệu gốc chứa sự kiện đó.
- **Tuân thủ quy định:** theo quy định của Trường và yêu cầu riêng của từng học phần, từng bài tập; khi quy định của học phần khác với giáo trình này, làm theo quy định của học phần.

### 7.5.2. Mẫu khai báo sử dụng AI

Đặt ở cuối báo cáo hoặc trong phụ lục:

| Công cụ | Dùng vào việc | Phần trong báo cáo | Cách kiểm tra lại |
|---|---|---|---|
| ChatGPT | Gợi ý dàn ý chương 2 | Chương 2 | Đối chiếu với đề cương môn học, viết lại bằng lời của nhóm |
| Gemini | Dịch đoạn tài liệu tiếng Anh về REST API | Mục 2.3 | Đối chiếu tài liệu gốc, sửa 4 thuật ngữ |

*Bảng 7.3. Ví dụ bảng khai báo sử dụng AI.*

Kèm theo là danh sách các prompt chính đã dùng (hoặc tệp nhật ký prompt), như yêu cầu của học phần.

## Tóm tắt chương

- Dịch tài liệu kỹ thuật cần chính xác, nhất quán thuật ngữ; quy trình 4 bước: ngữ cảnh → dịch → kiểm tra → đối chiếu thuật ngữ; có thể dịch ngược để kiểm tra.
- Dùng AI để góp ý có kiểm soát: chỉ sửa lỗi, liệt kê từng thay đổi, không thay ý của bạn.
- Báo cáo kỹ thuật thường gồm: đặt vấn đề, tổng quan, phân tích thiết kế, cài đặt thực nghiệm, đánh giá; quy định định dạng của Khoa là chuẩn.
- AI có thể ảo giác: bịa nguồn, số liệu, mã nguồn; kiểm chứng theo 4 bước và ưu tiên nguồn gốc.
- Cung cấp tài liệu nguồn giúp giảm ảo giác; liêm chính học thuật đòi hỏi trung thực, minh bạch, ghi nguồn và khai báo việc dùng AI.

## Câu hỏi ôn tập

1. Vì sao nên giữ thuật ngữ tiếng Anh trong ngoặc ở lần xuất hiện đầu khi dịch tài liệu kỹ thuật?
2. Trình bày quy trình dịch bốn bước và cách dịch ngược để kiểm tra bản dịch.
3. Viết một prompt yêu cầu AI chỉ sửa lỗi chính tả, ngữ pháp mà không thay đổi ý của đoạn văn.
4. Ảo giác của AI là gì? Kể bốn dạng ảo giác sinh viên hay gặp.
5. Trình bày quy trình kiểm chứng thông tin bốn bước.
6. Vì sao "AI nói vậy" không phải là một nguồn trích dẫn hợp lệ?
7. Cung cấp tài liệu nguồn cho AI giúp giảm ảo giác như thế nào? Vì sao vẫn cần kiểm chứng?

## Bài tập

1. **Dịch và lập bảng thuật ngữ.** Dịch một đoạn khoảng 300 từ từ tài liệu chính thức của một công nghệ (ví dụ Python, Git) bằng prompt ở mục 7.1.3; tự sửa bản dịch và ghi lại các chỗ đã sửa.
2. **Biên tập có kiểm soát** [1]. Viết một đoạn 200–300 từ giới thiệu ngành CNTT; dùng prompt ở mục 7.2.2 để AI góp ý. Chấp nhận hoặc từ chối từng góp ý và giải thích lý do.
3. **Săn ảo giác.** Yêu cầu AI đưa ra 3 bài báo khoa học (tác giả, năm, DOI) về "ứng dụng AI trong giáo dục đại học". Kiểm chứng từng bài trên Google Scholar và theo DOI; báo cáo bài nào có thật, bài nào sai một phần, bài nào không tồn tại.

## Tài liệu tham khảo

[1] Nguyễn Minh Phúc, *Giáo trình Áp dụng ChatGPT vào học tập và công việc*, Tài liệu lưu hành nội bộ. Đồng Nai, Việt Nam: Khoa Công nghệ Thông tin, Trường Đại học Lạc Hồng, 2024.

[2] Z. Ji *et al.*, "Survey of hallucination in natural language generation," *ACM Computing Surveys*, vol. 55, no. 12, pp. 1–38, 2023, doi: 10.1145/3571730.

[3] Google, "Google Scholar." Accessed: Oct. 31, 2026. [Online]. Available: https://scholar.google.com

[4] P. Lewis *et al.*, "Retrieval-augmented generation for knowledge-intensive NLP tasks," in *Advances in Neural Information Processing Systems 33 (NeurIPS 2020)*, 2020. [Online]. Available: https://arxiv.org/abs/2005.11401
