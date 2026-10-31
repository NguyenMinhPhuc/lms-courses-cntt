# Chương 8. Prompt nâng cao và AI hỗ trợ lập trình

## Mục tiêu chương

Sau khi học xong chương này, bạn có thể:

- Áp dụng được các kỹ thuật prompt nâng cao: đóng vai chuyên gia, cho ví dụ mẫu (few-shot), yêu cầu suy luận từng bước (chain-of-thought).
- Dùng được AI để đọc thông báo lỗi, gỡ lỗi, giải thích mã, ước lượng độ phức tạp và gợi ý kiểm thử, mà vẫn tự hiểu và kiểm chứng mã.
- Phân biệt được trợ lý trò chuyện, trợ lý lập trình trong trình soạn thảo (GitHub Copilot) và nền tảng phát triển hướng tác tử (Google Antigravity).
- Dùng được công cụ AI tạo sinh để làm sản phẩm trực quan (slide, sơ đồ, infographic) có ghi nhãn và kiểm chứng.
- Xây dựng được thư viện prompt cá nhân cho các môn học.

## 8.1. Kỹ thuật prompt nâng cao

### 8.1.1. Đóng vai chuyên gia

Giao một vai cụ thể cho AI giúp câu trả lời đi đúng góc nhìn, đúng mức độ chi tiết [1]. Vai càng cụ thể, kết quả càng sát nhu cầu:

```text
Bạn là nhà tuyển dụng của một công ty phần mềm, đang phỏng vấn vị trí thực tập sinh lập trình C++.
Hãy hỏi tôi lần lượt 5 câu, mỗi lần một câu, từ dễ đến khó.
Sau mỗi câu trả lời, nhận xét ngắn: điểm tốt, điểm thiếu, cách trả lời tốt hơn.
```

Đóng vai có giới hạn: AI không có kinh nghiệm thực tế của chuyên gia thật, không tự xác minh được thông tin, và có thể trả lời rất tự tin về điều nó không chắc [1]. Hãy coi "chuyên gia AI" là người để luyện tập và gợi ý, không phải nguồn để trích dẫn (Chương 7).

### 8.1.2. Cho ví dụ mẫu (few-shot)

Thay vì chỉ mô tả yêu cầu, hãy đưa cho AI vài ví dụ đầu vào – đầu ra mẫu. Nghiên cứu về mô hình ngôn ngữ lớn cho thấy mô hình có thể học cách làm một nhiệm vụ mới chỉ từ vài ví dụ đặt ngay trong prompt [2]. Kỹ thuật này hữu ích khi bạn cần kết quả theo đúng một định dạng:

```text
Chuyển tên biến tối nghĩa thành tên có ý nghĩa theo quy ước snake_case.
Ví dụ:
- "t" trong hàm tính tổng tiền → "tong_tien"
- "n" là số sinh viên → "so_sinh_vien"
Bây giờ hãy đổi: "x" là điểm trung bình, "d" là danh sách điểm, "c" là số môn đạt.
```

Khi không đưa ví dụ nào, ta gọi là *zero-shot*; đưa một vài ví dụ là *few-shot*.

### 8.1.3. Yêu cầu suy luận từng bước (chain-of-thought)

Với bài toán cần nhiều bước suy luận (toán, logic, phân tích thuật toán), yêu cầu AI trình bày từng bước trước khi kết luận thường cho kết quả tốt hơn so với hỏi thẳng đáp án [3]. Thậm chí chỉ thêm câu "Hãy suy nghĩ từng bước" cũng cải thiện khả năng suy luận của mô hình trên nhiều bài toán [4].

```text
Một mảng đã sắp xếp có 1.000.000 phần tử. Tìm kiếm nhị phân cần tối đa bao nhiêu lần so sánh?
Hãy suy nghĩ từng bước, giải thích từng bước, rồi mới đưa ra kết quả.
```

Lợi ích lớn nhất với người học: khi AI trình bày từng bước, **bạn kiểm tra được từng bước** và phát hiện bước sai, thay vì chỉ nhận một con số không biết đúng sai.

### 8.1.4. Kết hợp các kỹ thuật

Các kỹ thuật trên kết hợp với cấu trúc 5 thành phần ở Chương 5: vai trò (đóng vai), bối cảnh, nhiệm vụ, ràng buộc (yêu cầu suy luận từng bước), định dạng (kèm ví dụ mẫu). Không phải lúc nào cũng cần dùng tất cả; hãy thêm dần khi câu trả lời chưa đạt.

## 8.2. AI hỗ trợ lập trình

### 8.2.1. Vibe coding có kiểm soát

**Vibe coding** là cách lập trình trong đó người lập trình mô tả điều muốn làm bằng ngôn ngữ tự nhiên, để AI sinh mã, rồi chạy thử và điều chỉnh. Cách làm này tăng tốc độ rất nhiều, nhưng với người học có một rủi ro lớn: chương trình chạy được mà bạn không hiểu vì sao. Học phần áp dụng **vibe coding có kiểm soát**:

1. **Hiểu bài toán trước:** tự mô tả đầu vào, đầu ra, các trường hợp đặc biệt.
2. **Prompt có ngữ cảnh:** ngôn ngữ, phiên bản, yêu cầu, ràng buộc (ví dụ: "chỉ dùng thư viện chuẩn").
3. **Đọc từng dòng mã AI sinh ra;** dòng nào không hiểu thì hỏi lại cho đến khi hiểu.
4. **Chạy thử với nhiều trường hợp,** gồm cả trường hợp biên.
5. **Không hiểu thì không nộp:** bạn phải giải thích được mọi dòng mã mình nộp.

### 8.2.2. Đọc lỗi và gỡ lỗi

Thông báo lỗi của trình biên dịch, thông báo ngoại lệ (stack trace) thường khó đọc với người mới. AI giúp giải thích, nhưng cần cung cấp đủ ngữ cảnh:

```text
Tôi đang học C++. Chương trình dưới đây biên dịch được nhưng in sai kết quả.
Đầu vào: 5 số 1 2 3 4 5. Kết quả mong đợi: tổng 15. Kết quả thực tế: tổng 10.
Hãy chỉ ra dòng có lỗi, giải thích nguyên nhân, nhưng đừng viết lại toàn bộ chương trình.
[dán đoạn mã]
```

Yêu cầu "chỉ ra dòng lỗi và giải thích" thay vì "sửa giúp tôi" giúp bạn học được lỗi đó, để lần sau tự phát hiện.

### 8.2.3. Giải thích mã, độ phức tạp và kiểm thử

Một số việc AI hỗ trợ tốt khi học lập trình:

| Việc | Prompt mẫu | Bạn cần kiểm tra |
|---|---|---|
| Giải thích mã | "Giải thích từng dòng đoạn mã sau cho sinh viên năm nhất." | Đối chiếu với tài liệu của ngôn ngữ |
| Ước lượng độ phức tạp | "Phân tích độ phức tạp thời gian và bộ nhớ của hàm sau, giải thích từng bước." | Tự đếm số vòng lặp, so với kết luận của AI |
| Gợi ý tái cấu trúc | "Đề xuất cách viết lại theo nguyên tắc mã sạch, giải thích từng thay đổi." | Kết quả chạy trước và sau phải giống nhau |
| Sinh ca kiểm thử | "Liệt kê 8 ca kiểm thử cho hàm sau, gồm trường hợp bình thường, lỗi và biên." | Tự chạy từng ca; thêm ca AI bỏ sót |

*Bảng 8.1. Các việc AI hỗ trợ khi học lập trình.*

### 8.2.4. Trợ lý lập trình trong môi trường viết mã

Ngoài trợ lý trò chuyện, có những công cụ AI tích hợp thẳng vào nơi bạn viết mã:

- **GitHub Copilot:** trợ lý lập trình của GitHub, gợi ý mã khi bạn gõ, trả lời câu hỏi về mã trong trình soạn thảo như VS Code, và có thể thực hiện các thay đổi trên nhiều tệp theo yêu cầu [5]. Sinh viên được xác minh qua GitHub Education có thể được dùng miễn phí; chính sách thay đổi theo thời gian, hãy kiểm tra trang chính thức [6].
- **Google Antigravity:** nền tảng phát triển phần mềm hướng tác tử (agentic) do Google ra mắt tháng 11/2025, trong đó các tác tử AI được dùng trình soạn thảo, terminal và trình duyệt để lập kế hoạch, viết mã, chạy và kiểm tra kết quả; người lập trình giao việc và giám sát [7].

Công cụ càng tự động, người dùng càng cần nắm vững nền tảng để giám sát: tác tử có thể sửa nhiều tệp cùng lúc, cài thư viện, chạy lệnh. Với sinh viên năm nhất, hãy dùng các công cụ này để **học** (hỏi, giải thích, gợi ý) trước khi dùng để **làm thay**.

### 8.2.5. An toàn khi đưa mã lên AI

- Không dán mật khẩu, khóa API, chuỗi kết nối cơ sở dữ liệu vào prompt; thay bằng giá trị giả.
- Không đưa mã nguồn của doanh nghiệp nơi thực tập vào công cụ AI công cộng nếu chưa được phép.
- Kiểm tra thư viện AI đề xuất có tồn tại thật và đúng tên; AI có thể "bịa" tên thư viện (Chương 7).
- Ứng dụng có tích hợp mô hình ngôn ngữ lớn có những rủi ro bảo mật riêng (ví dụ chèn lệnh độc hại vào prompt); OWASP duy trì danh sách 10 rủi ro hàng đầu cho loại ứng dụng này [8].

## 8.3. Công cụ AI tạo sinh đa phương tiện

### 8.3.1. Trực quan hóa kiến thức và sản phẩm

AI tạo sinh không chỉ tạo văn bản. Trong học tập và đồ án, bạn có thể dùng:

- **Tạo slide từ dàn ý:** công cụ như Gamma tạo bản trình bày từ văn bản [9]; bạn vẫn phải biên tập nội dung, kiểm tra hình ảnh và nguồn.
- **Vẽ sơ đồ bằng văn bản:** yêu cầu AI viết sơ đồ bằng cú pháp Mermaid (sơ đồ luồng, sơ đồ tuần tự, sơ đồ lớp), rồi hiển thị bằng công cụ hỗ trợ Mermaid [10].
- **Tạo ảnh, infographic, video ngắn** bằng các công cụ tạo ảnh, video; dùng để minh họa ý tưởng, không thay cho tư liệu thật.

### 8.3.2. Chủ đề thực hành

Tài liệu *Chủ đề thực hành Generative AI cho sinh viên* của học phần, phát triển từ bài giảng "A Practitioner's Guide to Generative AI" của ASU, đề xuất 15 chủ đề kèm yêu cầu sản phẩm [11]. Một số chủ đề phù hợp sinh viên CNTT năm nhất:

| Chủ đề | Sản phẩm đầu ra |
|---|---|
| Thiết kế infographic bằng AI | 03 infographic về một chủ đề học tập, kèm tệp thiết kế và prompt |
| Prompt engineering cho nội dung trực quan | Bộ 10 prompt tăng dần độ phức tạp, hình ảnh và phân tích cải tiến |
| Phát triển video quảng bá ngành học | Video 60–90 giây về ngành CNTT, kèm kịch bản phân cảnh (storyboard) |
| Xây dựng bộ học liệu cá nhân hóa | 03 phiên bản học liệu cho 03 nhóm người học khác nhau |
| Phát hiện thông tin sai do AI tạo ra | 20 câu trả lời AI, biên bản kiểm chứng, phân loại lỗi và báo cáo |
| Đánh giá thiên lệch (AI bias) | Ít nhất 20 prompt thử nghiệm, bảng phân tích và đề xuất giảm thiên lệch |
| Phân tích đạo đức và bản quyền AI | 03 tình huống nghiên cứu, báo cáo phân tích và nguyên tắc sử dụng AI |

*Bảng 8.2. Một số chủ đề thực hành AI tạo sinh, trích từ [11].*

Mỗi sản phẩm cần kèm **nhật ký prompt** (ít nhất 5 prompt quan trọng, đầu ra và cách điều chỉnh) và phần **đánh giá AI**: ưu điểm, hạn chế, lỗi, nội dung đã kiểm chứng, đóng góp thực tế của sinh viên [11].

### 8.3.3. Ghi nhãn và bản quyền

- Ghi rõ hình ảnh, video, giọng đọc nào được tạo bằng AI.
- Không dùng AI tạo tư liệu giả (ảnh sự kiện, nhân chứng, số liệu) và trình bày như thật.
- Kiểm tra điều khoản sử dụng của công cụ về quyền dùng sản phẩm tạo ra, đặc biệt khi dùng cho mục đích thương mại.

## 8.4. Thư viện prompt cá nhân

### 8.4.1. Vì sao cần thư viện prompt

Mỗi học kỳ bạn sẽ lặp lại nhiều loại yêu cầu: giải thích khái niệm, tạo flashcard, gỡ lỗi, góp ý báo cáo. Lưu lại những prompt hiệu quả giúp bạn không phải nghĩ lại từ đầu và cải thiện chúng theo thời gian. Đây là phần hoàn thiện của "thư viện prompt bước đầu" ở Chương 6.

### 8.4.2. Cấu trúc một mục trong thư viện

| Trường | Nội dung |
|---|---|
| Tên | Ngắn gọn, dễ tìm: "Gỡ lỗi C++ – chỉ ra dòng lỗi" |
| Môn học, mục đích | Nhập môn lập trình; tìm lỗi logic |
| Prompt | Nội dung đầy đủ, phần cần thay trong ngoặc vuông `[ ]` |
| Kỹ thuật dùng | Vai trò, few-shot, chain-of-thought, ràng buộc định dạng |
| Công cụ đã thử, kết quả | ChatGPT, Gemini; nhận xét ngắn |
| Lưu ý | Điều cần kiểm tra lại, lỗi AI hay mắc với prompt này |

*Bảng 8.3. Cấu trúc một mục thư viện prompt.*

Có thể lưu thư viện trong Google Docs, Notion hoặc tệp Markdown trên GitHub (Chương 3). Hãy chia theo môn học (Nhập môn lập trình, Toán rời rạc, Cấu trúc dữ liệu, Thiết kế web…) và theo loại việc (học khái niệm, ôn thi, lập trình, viết báo cáo).

## Tóm tắt chương

- Đóng vai chuyên gia định hướng góc nhìn; few-shot dùng ví dụ mẫu để kiểm soát định dạng; chain-of-thought yêu cầu suy luận từng bước để bạn kiểm tra được từng bước.
- Vibe coding có kiểm soát: hiểu bài toán, prompt có ngữ cảnh, đọc từng dòng, chạy thử nhiều trường hợp, không hiểu thì không nộp.
- AI hỗ trợ đọc lỗi, giải thích mã, ước lượng độ phức tạp, gợi ý tái cấu trúc và ca kiểm thử; GitHub Copilot và Google Antigravity đưa AI vào môi trường viết mã ở các mức tự động khác nhau.
- Không đưa mật khẩu, khóa API, mã nguồn mật vào AI; kiểm tra thư viện AI đề xuất có thật.
- Công cụ đa phương tiện giúp trực quan hóa; mọi sản phẩm cần nhật ký prompt, đánh giá AI, ghi nhãn và tôn trọng bản quyền; thư viện prompt cá nhân giúp tái sử dụng và cải thiện prompt.

## Câu hỏi ôn tập

1. Viết một prompt đóng vai chuyên gia để luyện phỏng vấn vị trí bạn mong muốn. Nêu hai giới hạn của cách luyện tập này.
2. Phân biệt zero-shot và few-shot. Khi nào nên đưa ví dụ mẫu vào prompt?
3. Yêu cầu suy luận từng bước giúp gì cho người học khi kiểm tra kết quả của AI?
4. Trình bày năm nguyên tắc của vibe coding có kiểm soát.
5. Vì sao nên yêu cầu AI "chỉ ra dòng lỗi và giải thích" thay vì "sửa giúp tôi"?
6. GitHub Copilot và Google Antigravity khác nhau thế nào về mức độ tự động? Người dùng cần làm gì để giám sát?
7. Nêu ba điều không được đưa vào prompt khi nhờ AI hỗ trợ lập trình.

## Bài tập

1. **Ba kỹ thuật, một bài toán.** Chọn một bài toán trong môn Nhập môn lập trình; hỏi AI theo ba cách: hỏi thẳng, có đóng vai, có yêu cầu suy luận từng bước. So sánh ba câu trả lời và chỉ ra bước sai nếu có.
2. **Phỏng vấn thử** [1]. Dùng prompt ở mục 8.1.1 để luyện phỏng vấn 5 câu; ghi lại hội thoại, tự đánh giá câu trả lời yếu nhất và viết lại câu trả lời tốt hơn.
3. **Thư viện prompt.** Tạo thư viện prompt cá nhân gồm ít nhất 8 mục theo Bảng 8.3, cho ít nhất 3 môn học khác nhau.

## Tài liệu tham khảo

[1] Nguyễn Minh Phúc, *Giáo trình Áp dụng ChatGPT vào học tập và công việc*, Tài liệu lưu hành nội bộ. Đồng Nai, Việt Nam: Khoa Công nghệ Thông tin, Trường Đại học Lạc Hồng, 2024.

[2] T. B. Brown *et al.*, "Language models are few-shot learners," in *Advances in Neural Information Processing Systems 33 (NeurIPS 2020)*, 2020. [Online]. Available: https://arxiv.org/abs/2005.14165

[3] J. Wei *et al.*, "Chain-of-thought prompting elicits reasoning in large language models," in *Advances in Neural Information Processing Systems 35 (NeurIPS 2022)*, 2022. [Online]. Available: https://arxiv.org/abs/2201.11903

[4] T. Kojima, S. S. Gu, M. Reid, Y. Matsuo, and Y. Iwasawa, "Large language models are zero-shot reasoners," in *Advances in Neural Information Processing Systems 35 (NeurIPS 2022)*, 2022. [Online]. Available: https://arxiv.org/abs/2205.11916

[5] GitHub, "About GitHub Copilot," *GitHub Docs*. Accessed: Oct. 31, 2026. [Online]. Available: https://docs.github.com/en/copilot/get-started/about-github-copilot

[6] GitHub, "Access GitHub Copilot for free as a student," *GitHub Docs*. Accessed: Oct. 31, 2026. [Online]. Available: https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-students

[7] Google, "Build with Google Antigravity, our new agentic development platform," *Google Developers Blog*, Nov. 2025. Accessed: Oct. 31, 2026. [Online]. Available: https://developers.googleblog.com/build-with-google-antigravity-our-new-agentic-development-platform/

[8] OWASP Foundation, "OWASP Top 10 for Large Language Model Applications." Accessed: Oct. 31, 2026. [Online]. Available: https://owasp.org/projects/top-10-for-large-language-model-applications

[9] Gamma, "Gamma." Accessed: Oct. 31, 2026. [Online]. Available: https://gamma.app

[10] Mermaid, "Mermaid: Diagramming and charting tool." Accessed: Oct. 31, 2026. [Online]. Available: https://mermaid.js.org

[11] Khoa Công nghệ Thông tin, Trường Đại học Lạc Hồng, *Chủ đề thực hành Generative AI cho sinh viên*, tài liệu học phần, phát triển từ bài giảng "A Practitioner's Guide to Generative AI" của Arizona State University, 2026.
