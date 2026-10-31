# Chương 5. Trí tuệ nhân tạo tạo sinh và kỹ thuật viết prompt

## Mục tiêu chương

Sau khi học xong chương này, bạn có thể:

- Giải thích được trí tuệ nhân tạo tạo sinh và mô hình ngôn ngữ lớn là gì, vì sao chúng trả lời trôi chảy nhưng vẫn có thể sai.
- Phân biệt được công dụng chính của các công cụ AI phổ biến: ChatGPT, Gemini, Claude, Microsoft Copilot, NotebookLM, Perplexity.
- Đăng ký và bảo vệ được tài khoản AI của mình; biết thông tin nào không được đưa vào AI.
- Viết được prompt theo cấu trúc 5 thành phần cho một nhiệm vụ học tập.
- Dùng được AI như một gia sư: hỏi nối tiếp, yêu cầu giải thích theo nhiều cấp độ, lập kế hoạch học tập mà không để AI làm thay.

## 5.1. AI tạo sinh và mô hình ngôn ngữ lớn

### 5.1.1. AI tạo sinh là gì

**Trí tuệ nhân tạo tạo sinh** (generative AI) là các hệ thống AI tạo ra nội dung mới: văn bản, hình ảnh, âm thanh, mã nguồn. Các trợ lý trò chuyện như ChatGPT dựa trên **mô hình ngôn ngữ lớn** (large language model, LLM): một mạng nơ-ron rất lớn được huấn luyện trên lượng văn bản khổng lồ để dự đoán phần tiếp theo của một đoạn văn bản. Kiến trúc nền tảng của hầu hết các mô hình này là *Transformer*, được công bố năm 2017 [2].

Cách hoạt động đơn giản hóa như sau: khi bạn gửi một câu hỏi, mô hình lần lượt sinh ra từng đơn vị văn bản (token) có xác suất phù hợp nhất với ngữ cảnh gồm câu hỏi của bạn và phần đã sinh trước đó. Hiểu điều này giúp bạn dùng AI đúng cách:

- **Trôi chảy không có nghĩa là đúng.** Mô hình được huấn luyện để tạo văn bản *hợp lý về mặt ngôn ngữ*; nó có thể "bịa" số liệu, tên sách, đoạn mã không tồn tại với giọng rất tự tin. Hiện tượng này gọi là **ảo giác** (hallucination), sẽ học kỹ ở Chương 7.
- **Ngữ cảnh quyết định chất lượng.** Mô hình chỉ biết những gì có trong dữ liệu huấn luyện và trong cuộc trò chuyện. Câu hỏi càng rõ, càng đủ ngữ cảnh thì câu trả lời càng sát nhu cầu (mục 5.3).
- **Kiến thức có mốc thời gian.** Dữ liệu huấn luyện dừng ở một thời điểm. Nhiều công cụ hiện đã có thêm khả năng tìm kiếm web, nhưng kết quả tìm kiếm cũng cần được kiểm tra lại.

### 5.1.2. Vai trò của AI tạo sinh trong học tập

Giáo trình [1] nêu ba vai trò chính của trợ lý AI đối với sinh viên, vẫn đúng với mọi công cụ hiện nay:

- **Hỗ trợ học tập cá nhân:** giải thích một chủ đề từ cơ bản đến chuyên sâu, theo tốc độ của bạn.
- **Hỗ trợ nghiên cứu và sáng tạo:** gợi ý dàn ý, tổng hợp tài liệu bạn cung cấp, góp ý bản viết.
- **Rèn tư duy và giao tiếp:** muốn nhận câu trả lời tốt, bạn phải diễn đạt vấn đề rõ ràng; đó cũng là kỹ năng cần cho học tập và làm việc nhóm.

Tuy vậy, AI không thay được việc bạn tự học: nếu AI làm bài thay, bạn mất chính kỹ năng mà bài tập muốn rèn luyện. Mục 5.4.4 trình bày cách dùng AI như một gia sư thay vì người làm thay.

### 5.1.3. Các công cụ AI phổ biến

Bảng 5.1 giới thiệu các công cụ bạn sẽ dùng trong học phần và trong những năm học tiếp theo. Tính năng, gói miễn phí và mô hình AI bên trong thay đổi thường xuyên; bảng chỉ nêu công dụng chính.

| Công cụ | Nhà phát triển | Công dụng chính khi học tập | Trang chính thức |
|---|---|---|---|
| ChatGPT | OpenAI | Trò chuyện đa năng: hỏi đáp, giải thích, viết và sửa văn bản, hỗ trợ lập trình | chatgpt.com |
| Gemini | Google | Trợ lý đa năng, tích hợp với tài khoản và dịch vụ Google (Gmail, Drive, Docs) | gemini.google.com |
| Claude | Anthropic | Trò chuyện đa năng, đọc và phân tích tài liệu, viết, hỗ trợ lập trình | claude.ai |
| Microsoft Copilot | Microsoft | Trợ lý đa năng, tích hợp với Windows, trình duyệt Edge và Microsoft 365 | copilot.microsoft.com |
| NotebookLM | Google | Trả lời, tóm tắt **dựa trên tài liệu bạn tải lên** (giáo trình, bài báo), có chỉ dẫn vị trí trong tài liệu | notebooklm.google.com |
| Perplexity | Perplexity AI | Tìm kiếm thông tin trên web và trả lời kèm danh sách nguồn | perplexity.ai |
| GitHub Copilot, Google Antigravity | GitHub (Microsoft), Google | Hỗ trợ lập trình ngay trong môi trường viết mã; giới thiệu ở Chương 8 [3] | github.com/features/copilot, antigravity.google |

*Bảng 5.1. Một số công cụ AI tạo sinh phổ biến.*

Không có công cụ nào "tốt nhất cho mọi việc". Một thói quen tốt là **so sánh câu trả lời của hai công cụ** cho cùng một câu hỏi quan trọng: chỗ hai câu trả lời khác nhau thường là chỗ bạn cần kiểm chứng thêm.

## 5.2. Thiết lập và quản trị tài khoản an toàn

### 5.2.1. Điều kiện sử dụng và độ tuổi

Trước khi đăng ký, hãy đọc điều khoản sử dụng của dịch vụ, đặc biệt là độ tuổi tối thiểu. Một số sinh viên năm nhất chưa đủ 18 tuổi cần lưu ý:

| Dịch vụ | Độ tuổi theo điều khoản (tháng 10/2026) |
|---|---|
| ChatGPT | Không dành cho người dưới 13 tuổi; người từ 13 đến 18 tuổi cần có sự đồng ý của cha mẹ [4] |
| Claude | Từ 18 tuổi trở lên (hoặc độ tuổi tối thiểu theo quy định nơi cư trú, lấy mức cao hơn) [5] |
| Gemini và các dịch vụ khác | Tùy loại tài khoản và quốc gia; xem điều khoản hiện hành của nhà cung cấp |

*Bảng 5.2. Độ tuổi sử dụng theo điều khoản của một số dịch vụ.*

### 5.2.2. Quy trình đăng ký

Giáo trình [1] hướng dẫn chi tiết từng bước đăng ký ChatGPT. Giao diện đã thay đổi nhiều lần, nhưng quy trình chung cho mọi công cụ vẫn gồm các bước sau:

1. **Truy cập đúng trang chính thức** bằng cách gõ địa chỉ trong Bảng 5.1 hoặc dùng ứng dụng tải từ kho ứng dụng chính thức. Cẩn thận với trang web, ứng dụng nhái tên công cụ AI để thu thập tài khoản.
2. **Chọn cách đăng ký:** bằng email, hoặc đăng nhập bằng tài khoản Google, Microsoft, Apple có sẵn. Gemini và NotebookLM dùng trực tiếp tài khoản Google.
3. **Xác nhận email** qua đường liên kết được gửi đến hộp thư (nếu đăng ký bằng email).
4. **Thiết lập hồ sơ:** tên hiển thị, ngôn ngữ ưu tiên. Có thể bỏ qua các bước không bắt buộc.
5. **Bắt đầu trò chuyện** trong ô nhập văn bản, ví dụ: "Bạn có thể giúp tôi học lập trình như thế nào?"

Khi gặp lỗi đăng ký (không nhận được mã xác nhận, mạng bị chặn), hãy thử đăng nhập bằng tài khoản Google hoặc đổi kết nối mạng, và báo giảng viên nếu vẫn không được.

### 5.2.3. Bảo mật tài khoản

- **Mật khẩu mạnh, không dùng lại:** ít nhất 8 ký tự, có chữ hoa, chữ thường, số và ký tự đặc biệt [1]; không dùng chung mật khẩu với tài khoản khác.
- **Bật xác minh 2 bước** (2FA) cho tài khoản email và tài khoản AI, để kẻ xấu có mật khẩu cũng không đăng nhập được [6].
- **Không chia sẻ tài khoản.** Lịch sử trò chuyện của bạn có thể chứa thông tin cá nhân, bài làm, ý tưởng đồ án.
- **Đăng xuất** khi dùng máy tính công cộng ở phòng máy, thư viện.

### 5.2.4. Dữ liệu và quyền riêng tư

Những gì bạn nhập vào công cụ AI được gửi lên máy chủ của nhà cung cấp và có thể được lưu lại. Vì vậy:

- **Không nhập** số căn cước, số tài khoản ngân hàng, mật khẩu, thông tin cá nhân của người khác, dữ liệu nội bộ của doanh nghiệp nơi thực tập, đề thi chưa công bố.
- **Kiểm tra phần cài đặt quyền riêng tư** của dịch vụ: nhiều dịch vụ cho phép tắt việc dùng hội thoại để cải thiện mô hình, hoặc có chế độ trò chuyện tạm thời không lưu lịch sử.
- Khi cần AI phân tích tài liệu có thông tin cá nhân, hãy **xóa hoặc thay thế** thông tin đó trước.

## 5.3. Kỹ thuật viết prompt căn bản

**Prompt** là câu lệnh, câu hỏi hoặc yêu cầu bạn gửi cho AI. **Kỹ thuật viết prompt** (prompt engineering) là cách tổ chức yêu cầu để AI hiểu đúng bạn cần gì.

### 5.3.1. Ba nguyên tắc đặt câu hỏi

Giáo trình [1] nêu ba nguyên tắc cơ bản:

- **Rõ ràng, cụ thể:** tránh từ ngữ mơ hồ, quá chung chung.
- **Xác định mục tiêu:** biết mình mong đợi câu trả lời dạng gì, dùng để làm gì.
- **Cung cấp ngữ cảnh:** bạn là ai, đang học gì, đã biết gì, câu hỏi nối tiếp từ đâu.

**Ví dụ 5.1.** So sánh hai câu hỏi [1]:

- Chưa hiệu quả: "Làm sao để giỏi lập trình?"
- Hiệu quả hơn: "Tôi muốn trở thành lập trình viên web. Hãy cho tôi biết những ngôn ngữ cần học để xây dựng một website."

Câu thứ hai nêu mục tiêu (lập trình viên web) và phạm vi (ngôn ngữ để xây dựng website), nên câu trả lời sẽ đi thẳng vào điều bạn cần.

### 5.3.2. Cấu trúc prompt 5 thành phần

Với nhiệm vụ phức tạp hơn, hãy viết prompt theo năm thành phần:

| Thành phần | Trả lời câu hỏi | Ví dụ |
|---|---|---|
| Vai trò | AI đóng vai ai? | "Bạn là cố vấn học tập cho sinh viên năm nhất ngành CNTT." |
| Bối cảnh | Tình huống của bạn là gì? | "Tôi học 5 môn, tuần sau thi giữa kỳ môn Toán rời rạc, tôi còn yếu phần đồ thị." |
| Nhiệm vụ | AI cần làm gì? | "Lập thời khóa biểu ôn tập 7 ngày." |
| Ràng buộc | Điều kiện, giới hạn? | "Mỗi tối tối đa 2 giờ; thứ Bảy đi làm thêm; ưu tiên phần đồ thị." |
| Định dạng | Kết quả trình bày thế nào? | "Trình bày dạng bảng: Ngày, Nội dung, Thời lượng, Cách tự kiểm tra." |

*Bảng 5.3. Cấu trúc prompt 5 thành phần.*

Ghép lại thành prompt hoàn chỉnh:

```text
Bạn là cố vấn học tập cho sinh viên năm nhất ngành CNTT.
Tôi đang học 5 môn, tuần sau thi giữa kỳ môn Toán rời rạc và tôi còn yếu phần lý thuyết đồ thị.
Hãy lập thời khóa biểu ôn tập trong 7 ngày.
Mỗi tối tôi học tối đa 2 giờ; thứ Bảy tôi đi làm thêm nên không học; ưu tiên phần đồ thị.
Trình bày dạng bảng gồm các cột: Ngày, Nội dung, Thời lượng, Cách tự kiểm tra.
```

Không phải prompt nào cũng cần đủ năm thành phần. Câu hỏi đơn giản chỉ cần nhiệm vụ rõ ràng; nhiệm vụ càng quan trọng, càng nên bổ sung bối cảnh, ràng buộc và định dạng.

### 5.3.3. Chia nhỏ câu hỏi phức tạp

Khi muốn hiểu một vấn đề lớn, hãy chia thành các câu hỏi nhỏ theo thứ tự [1]:

```text
Tôi muốn hiểu về lập trình web. Hãy giải thích lần lượt:
1) Phần giao diện (frontend) thường dùng những ngôn ngữ nào?
2) Phần xử lý phía máy chủ (backend) thường dùng những ngôn ngữ nào?
3) Frontend và backend trao đổi dữ liệu với nhau như thế nào?
```

Chia nhỏ giúp câu trả lời có cấu trúc, và giúp chính bạn xác định rõ mình chưa hiểu ở bước nào.

### 5.3.4. Lỗi thường gặp

| Lỗi | Ví dụ | Cách sửa |
|---|---|---|
| Quá chung chung | "Giải thích về mạng." | Nêu phạm vi, cấp độ: "Giải thích mô hình client – server cho sinh viên năm nhất, kèm một ví dụ đời thường." |
| Thiếu ngữ cảnh | "Sửa lỗi code giúp tôi." | Dán đoạn mã, thông báo lỗi, ngôn ngữ, điều bạn đã thử. |
| Nhiều yêu cầu lẫn lộn | Hỏi năm việc khác nhau trong một câu | Tách thành từng prompt hoặc đánh số yêu cầu. |
| Không nêu định dạng | Nhận về một đoạn văn dài khó dùng | Yêu cầu bảng, gạch đầu dòng, số từ tối đa. |
| Tin ngay kết quả | Chép nguyên câu trả lời vào bài | Đọc, đối chiếu nguồn, chỉnh sửa bằng lời của mình (Chương 7). |

*Bảng 5.4. Lỗi thường gặp khi viết prompt.*

## 5.4. Dùng AI làm gia sư cá nhân

### 5.4.1. Hỏi nối tiếp

Một câu trả lời đầu tiên hiếm khi đủ. Hãy hỏi nối tiếp để đào sâu từng bước [1]:

1. "Giải thích khái niệm cơ bản về đa luồng (multithreading)."
2. "Đa luồng ảnh hưởng thế nào đến hiệu suất chương trình?"
3. "Cho một ví dụ trong đó dùng đa luồng lại làm chương trình chậm hơn."

Mỗi câu hỏi sau dựa trên câu trả lời trước. Cách hỏi này rèn tư duy phản biện: bạn phải đọc kỹ câu trả lời mới đặt được câu hỏi tiếp theo hay.

### 5.4.2. Giải thích theo nhiều cấp độ

Khi một khái niệm khó, hãy yêu cầu AI giải thích ở nhiều cấp độ rồi đi dần lên:

```text
Giải thích khái niệm đệ quy (recursion) theo ba cấp độ:
1) Cho một học sinh 10 tuổi, dùng ví dụ đời thường.
2) Cho sinh viên năm nhất ngành CNTT, kèm một đoạn mã Python ngắn.
3) Cho người đã biết lập trình, nêu rủi ro tràn ngăn xếp (stack overflow).
```

Cấp độ đầu giúp bạn có trực giác; cấp độ sau giúp bạn nối trực giác đó với kiến thức chuyên ngành.

### 5.4.3. Lập kế hoạch học tập

AI có thể gợi ý một lộ trình học tập ban đầu, ví dụ kế hoạch 4 tuần cho môn Lập trình Python [1]: tuần 1 cú pháp cơ bản, biến, kiểu dữ liệu, nhập xuất; tuần 2 câu lệnh điều kiện và vòng lặp; tuần 3 hàm và lập trình hướng đối tượng; tuần 4 làm việc với file và một dự án nhỏ, ôn tập.

Kế hoạch do AI đưa ra chỉ là **bản nháp**. Bạn cần điều chỉnh theo lịch học, lịch làm thêm, đề cương môn học thật và tốc độ của bản thân, rồi theo dõi việc thực hiện mỗi tuần. Kỹ năng lập và điều chỉnh kế hoạch này chính là CLO3 của học phần.

### 5.4.4. Gia sư, không làm thay

Cùng một công cụ, cách hỏi khác nhau dẫn đến hai kết quả rất khác: AI làm bài thay bạn, hoặc AI giúp bạn tự làm được. Với bài tập, hãy yêu cầu AI hướng dẫn thay vì đưa đáp án:

```text
Tôi đang làm bài tập: [dán đề bài].
Đừng đưa lời giải. Hãy hỏi tôi từng câu gợi mở để tôi tự tìm ra cách giải.
Nếu tôi trả lời sai, hãy chỉ ra tôi sai ở đâu và gợi ý thêm một bước.
```

Cách học này chậm hơn chép đáp án, nhưng sau buổi học bạn tự làm được bài tương tự, và đó là điều kỳ thi đánh giá.

## Tóm tắt chương

- AI tạo sinh dựa trên mô hình ngôn ngữ lớn: sinh văn bản theo xác suất dựa trên ngữ cảnh, nên trôi chảy nhưng có thể sai và có mốc thời gian kiến thức.
- Các công cụ phổ biến (ChatGPT, Gemini, Claude, Microsoft Copilot, NotebookLM, Perplexity) có thế mạnh khác nhau; so sánh câu trả lời giữa các công cụ giúp phát hiện chỗ cần kiểm chứng.
- Đọc điều khoản độ tuổi; đăng ký từ trang chính thức; mật khẩu mạnh, xác minh 2 bước; không đưa dữ liệu cá nhân, dữ liệu mật vào AI.
- Prompt tốt rõ ràng, có mục tiêu và ngữ cảnh; nhiệm vụ phức tạp dùng cấu trúc 5 thành phần: vai trò, bối cảnh, nhiệm vụ, ràng buộc, định dạng.
- Dùng AI như gia sư: hỏi nối tiếp, giải thích nhiều cấp độ, lập kế hoạch rồi tự điều chỉnh, yêu cầu gợi mở thay vì đáp án.

## Câu hỏi ôn tập

1. Mô hình ngôn ngữ lớn tạo ra câu trả lời như thế nào? Vì sao điều đó dẫn đến hiện tượng ảo giác?
2. Nêu công dụng chính của NotebookLM và Perplexity. Khi nào nên dùng chúng thay cho một trợ lý trò chuyện đa năng?
3. Vì sao không nên nhập số căn cước hay dữ liệu nội bộ của doanh nghiệp vào công cụ AI?
4. Xác minh 2 bước bảo vệ tài khoản trong tình huống nào?
5. Trình bày 5 thành phần của một prompt và cho ví dụ từng thành phần.
6. Viết lại câu hỏi "Giải thích về cơ sở dữ liệu" thành một prompt hiệu quả hơn.
7. Phân biệt cách dùng AI "làm thay" và "làm gia sư" khi làm bài tập. Cách nào giúp bạn đạt mục tiêu học tập?

## Bài tập

1. **Đặt câu hỏi hiệu quả** [1]. Đặt một câu hỏi chung chung về môn bạn đang học, sau đó viết lại cho cụ thể hơn. So sánh hai câu trả lời và viết 150–200 từ về sự khác biệt.
2. **So sánh hai công cụ.** Gửi cùng câu hỏi "Giải thích khái niệm đệ quy cho người chưa biết lập trình" cho hai công cụ khác nhau. Lập bảng so sánh: độ dễ hiểu, ví dụ, độ chính xác, điểm bạn cần kiểm chứng thêm.
3. **Kế hoạch học tập** [1]. Dùng prompt 5 thành phần để AI lập kế hoạch học 4 tuần cho một môn của học kỳ này. Chỉnh sửa cho phù hợp lịch cá nhân và viết 100–150 từ giải thích những gì bạn đã thay đổi, vì sao.

## Tài liệu tham khảo

[1] Nguyễn Minh Phúc, *Giáo trình Áp dụng ChatGPT vào học tập và công việc*, Tài liệu lưu hành nội bộ. Đồng Nai, Việt Nam: Khoa Công nghệ Thông tin, Trường Đại học Lạc Hồng, 2024.

[2] A. Vaswani *et al.*, "Attention is all you need," in *Advances in Neural Information Processing Systems 30 (NeurIPS 2017)*, 2017. [Online]. Available: https://arxiv.org/abs/1706.03762

[3] Google, "Build with Google Antigravity, our new agentic development platform," *Google Developers Blog*, Nov. 2025. Accessed: Oct. 31, 2026. [Online]. Available: https://developers.googleblog.com/build-with-google-antigravity-our-new-agentic-development-platform/

[4] OpenAI, "Is ChatGPT safe for all ages?," *OpenAI Help Center*. Accessed: Oct. 31, 2026. [Online]. Available: https://help.openai.com/en/articles/8313401-is-chatgpt-safe-for-all-ages

[5] Anthropic, "Consumer Terms of Service," effective Oct. 8, 2025. Accessed: Oct. 31, 2026. [Online]. Available: https://www.anthropic.com/legal/consumer-terms

[6] Google, "Turn on 2-Step Verification," *Google Account Help*. Accessed: Oct. 31, 2026. [Online]. Available: https://support.google.com/accounts/answer/185839
