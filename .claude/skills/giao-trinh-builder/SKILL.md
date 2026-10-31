---
name: giao-trinh-builder
description: Soạn giáo trình học phần (giáo trình nội bộ, tài liệu học tập) cho Trường Đại học Lạc Hồng theo quy trình và yêu cầu của Thông tư 62/2026/TT-BGDĐT - đề cương chi tiết giáo trình, biên soạn từng chương, lấy ý kiến góp ý, tổng hợp tiếp thu - giải trình, báo cáo quá trình biên soạn và lập hồ sơ đề nghị thẩm định, phê duyệt. Xuất Word bằng build-textbook.py. Dùng khi người dùng yêu cầu viết/soạn/biên soạn giáo trình, viết chương giáo trình, lập đề cương giáo trình, chuẩn bị hồ sơ thẩm định giáo trình, rà soát giáo trình theo Thông tư 62, hoặc nhắc tới "Thông tư 62/2026".
---

# Soạn giáo trình theo Thông tư 62/2026/TT-BGDĐT

Skill này biến đề cương học phần và bài giảng đã duyệt thành một giáo trình hoàn chỉnh kèm hồ sơ biên soạn, theo quy trình 4 bước của Điều 7 khoản 2 Thông tư 62/2026/TT-BGDĐT (hiệu lực 12/9/2026). Tóm tắt Thông tư kèm số điều khoản: [references/thong-tu-62-2026.md](references/thong-tu-62-2026.md). Văn bản gốc: `templates/62_2026_TT-BGDDT_717415-Thông tư về viết giáo trình.docx`.

## Phạm vi áp dụng: nói rõ với người dùng

- Thông tư điều chỉnh trực tiếp giáo trình các **môn học, học phần bắt buộc sử dụng chung** (Điều 1, 2), do cơ quan được giao tổ chức biên soạn và phê duyệt.
- Với **học phần chuyên ngành** của Khoa, Thông tư không bắt buộc, nhưng skill vẫn dùng yêu cầu ở Điều 5 và quy trình ở Điều 7 làm chuẩn chất lượng. Quy định nội bộ của Trường về biên soạn giáo trình (nếu người dùng cung cấp) được ưu tiên hơn ở những điểm Thông tư không quy định (thể thức trình bày, mẫu biểu, số trang).
- Thông tư **không quy định thể thức trình bày** (khổ giấy, font, cấu trúc chương). Cấu trúc chương trong skill là quy ước của repo, không phải yêu cầu của Thông tư; không được nói với người dùng rằng Thông tư bắt buộc những điểm đó.

## Thư mục và công cụ

```
<hoc-phan>/giao-trinh/
├── 00-loi-noi-dau.md
├── chuong-01.md … chuong-NN.md
├── bai-tap-huong-dan/bt-XX.md       (tự chèn vào chương XX)
├── Giao-trinh-<hoc-phan>.docx       (sinh tự động)
└── ho-so/
    ├── 01-de-cuong-chi-tiet.md
    ├── 02-phieu-lay-y-kien.md
    ├── 03-tong-hop-tiep-thu-giai-trinh.md
    ├── 04-bao-cao-qua-trinh-bien-soan.md
    ├── 05-van-ban-de-nghi-tham-dinh.md
    ├── 06-danh-muc-ho-so.md
    └── Ho-so-bien-soan-<hoc-phan>.docx   (sinh tự động)
```

- Giáo trình: `uv run --with python-docx python build-textbook.py <hoc-phan>`
- Hồ sơ: `uv run --with python-docx python build-textbook.py <hoc-phan> --ho-so`
- Kiểm tra: `uv run python validate-course.py <hoc-phan>` (mỗi chương đủ mục bắt buộc; trích dẫn `[n]` khớp danh mục tài liệu tham khảo).
- `course.json`: `textbookKind` ("Giáo trình" hoặc "Tài liệu học tập"), `textbookSubtitle`, `textbookAuthor`, `watermark`.
- Markdown chỉ dùng phần `build-textbook.py` hỗ trợ: tiêu đề `#`–`####`, đoạn, **đậm**, *nghiêng*, `code`, danh sách 2 cấp, bảng, khối code, trích dẫn `>`, hình `![Hình X.Y. Chú thích](../Slides/images/ten.png)`.

## Quy trình (Điều 7 khoản 2)

Làm tuần tự. Bước nào có chữ **DỪNG** thì chờ người dùng xác nhận rồi mới làm tiếp.

1. **Thu thập đầu vào.** Đọc `course.json`, đề cương học phần, CLO, danh sách bài (`bai-XX.md`), slide, giáo trình chính đang dùng. Xác định: tên giáo trình, loại tài liệu, chủ biên, người biên soạn, đối tượng người học, số tín chỉ LT/TH, số chương (thường mỗi bài một chương). Thiếu thông tin hành chính thì hỏi; không tự đặt tên người, học hàm, đơn vị.
2. **Đề cương chi tiết giáo trình** (bước 1 của Điều 7.2). Viết `ho-so/01-de-cuong-chi-tiet.md` theo [references/de-cuong-chi-tiet.md](references/de-cuong-chi-tiet.md): mục tiêu, ma trận chương – CLO, nội dung từng chương tới mục cấp 2, tỷ lệ lý thuyết/thực hành, tài liệu tham khảo chính, kế hoạch học liệu kèm theo, phân công biên soạn, tiến độ. **DỪNG**: tóm tắt đề cương cho người dùng và chờ duyệt.
3. **Biên soạn** (bước 2). Viết `00-loi-noi-dau.md` và từng `chuong-XX.md` theo [references/cau-truc-chuong.md](references/cau-truc-chuong.md); nội dung mở rộng từ `bai-XX.md` đã duyệt và phải khớp với bài giảng, slide, quiz. Làm theo đợt (2–3 chương), build, chạy validate và để người dùng đọc trước khi viết tiếp.
4. **Tự rà soát** theo [references/checklist-yeu-cau.md](references/checklist-yeu-cau.md) (các yêu cầu của Điều 5). Ghi các điểm chưa đạt vào cuối câu trả lời.
5. **Lấy ý kiến góp ý** (bước 3). Tạo `ho-so/02-phieu-lay-y-kien.md` theo [references/ho-so-bien-soan.md](references/ho-so-bien-soan.md) để người dùng gửi chuyên gia, giảng viên, người học. **DỪNG**: chờ người dùng gửi lại các ý kiến thật.
6. **Tiếp thu – giải trình và hoàn thiện** (bước 4). Với từng ý kiến người dùng cung cấp: sửa giáo trình hoặc giải trình lý do không sửa; ghi vào `ho-so/03-tong-hop-tiep-thu-giai-trinh.md`, có vị trí đã sửa (chương, mục).
7. **Lập hồ sơ đề nghị thẩm định** (Điều 8 khoản 5). Viết `04-bao-cao-qua-trinh-bien-soan.md`, `05-van-ban-de-nghi-tham-dinh.md`, `06-danh-muc-ho-so.md`; build giáo trình và hồ sơ ra Word; chạy validate.
8. **Sau thẩm định** (Điều 8 khoản 7, Điều 9). Khi người dùng gửi kết luận của Hội đồng: sửa theo kết luận, cập nhật bảng tiếp thu – giải trình, chuẩn bị hồ sơ trình phê duyệt trong **15 ngày làm việc** kể từ khi có kết luận. Không đạt thì quay lại bước 6 rồi trình thẩm định lại.

Người dùng chỉ yêu cầu một phần (ví dụ "viết chương 3", "lập hồ sơ thẩm định") thì làm đúng bước đó nhưng vẫn theo định dạng và quy tắc dưới đây.

## Quy tắc bắt buộc

- **Không bịa dữ kiện hành chính và góp ý.** Không tự viết tên thành viên Hội đồng, số quyết định, ngày họp, nội dung lý lịch khoa học, kết quả bỏ phiếu, hay **ý kiến góp ý của chuyên gia**. Chỗ chưa có thì để placeholder `{{...}}` và liệt kê lại cuối câu trả lời.
- **Chính xác và có nguồn hợp pháp** (Điều 5.1). Mọi số liệu, định nghĩa, trích dẫn, quy định pháp luật đều có nguồn trong danh mục tài liệu tham khảo của chương (chuẩn IEEE, xem cau-truc-chuong.md). Không trích dẫn nguồn không kiểm chứng được. Kiến thức Claude tự soạn phải đúng với tài liệu chính thức; không chắc thì đánh dấu `{{CẦN KIỂM TRA: ...}}` cho người dùng.
- **Liêm chính học thuật và sở hữu trí tuệ.** Diễn đạt lại bằng lời của mình và ghi nguồn; trích nguyên văn thì để trong ngoặc kép hoặc khối `>`, ngắn, có nguồn. Không chép nguyên đoạn dài từ sách, web. Hình ảnh chỉ dùng hình tự vẽ hoặc có giấy phép mở, ghi tác giả và giấy phép. Mã nguồn mẫu do nhóm biên soạn viết hoặc có giấy phép tương thích.
- **Minh bạch khi dùng AI.** Giữ mục "Quy ước dùng AI" trong lời nói đầu, ghi rõ AI hỗ trợ ở khâu nào; người biên soạn chịu trách nhiệm nội dung (Điều 7.3). Báo cáo quá trình biên soạn có mục về công cụ AI đã dùng.
- **Không chứa nội dung bị cấm** theo pháp luật về xuất bản (Điều 5.1). Nội dung liên quan chủ trương, chính sách, pháp luật phải dẫn văn bản còn hiệu lực, ghi số hiệu và ngày ban hành.
- **Một nguồn nội dung.** Giáo trình mở rộng từ `bai-XX.md`; sửa kiến thức ở một nơi thì sửa cả bài học, slide, quiz.
- **Thay đổi lớn phải thẩm định lại.** Chỉnh sửa làm thay đổi mục tiêu, cấu trúc hoặc nội dung cơ bản của giáo trình đã phê duyệt thì phải đi lại quy trình thẩm định, phê duyệt (Điều 12.3). Nhắc người dùng khi yêu cầu sửa thuộc loại này.
- **Mã hóa UTF-8**, tên file đúng quy ước (`chuong-01.md`, số hai chữ số).
