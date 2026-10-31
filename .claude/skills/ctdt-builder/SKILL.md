---
name: ctdt-builder
description: Xây dựng, cập nhật và rà soát chương trình đào tạo (CTĐT) đại học chính quy của Khoa CNTT – Trường Đại học Lạc Hồng theo bộ biểu mẫu PĐT.QT.08 (BM01.1–BM09.2) - đánh giá CTĐT cũ, bảng đối sánh, phiếu ý kiến các bên liên quan và góp ý Hội đồng, công bố chuẩn đầu ra (PEO/PLO/PI), kế hoạch đào tạo, chương trình điều hành, đề cương học phần (BM05, BM05a/BM05b học liệu ASU), tóm tắt học phần, biên bản họp Hội đồng khoa học và đào tạo, tờ trình ban hành, cuốn CTĐT. Dùng khi người dùng nhắc tới xây dựng/điều chỉnh/rà soát chương trình đào tạo, CTĐT, niên khóa mới, kế hoạch đào tạo, BM03, đề cương học phần BM05, ma trận CLO–PI, chuẩn đầu ra chương trình, hồ sơ trình ban hành CTĐT.
---

# Xây dựng chương trình đào tạo đại học chính quy

Skill này hướng dẫn lập và rà soát **bộ hồ sơ xây dựng CTĐT** của một ngành cho một niên khóa (ví dụ CNTT 2026–2030), theo bộ biểu mẫu mà Khoa đang dùng. Bộ mẫu gốc (kèm hồ sơ đợt 2026) nằm ở `templates/xay-dung-ctdt-Dai hoc chinh quy/`.

**Mọi kết quả lưu trong `chuong-trinh-dao-tao/<ngành>-<khóa>/`** ở thư mục gốc repo (ví dụ `chuong-trinh-dao-tao/cntt-2027/`):
- `du-lieu/`: bộ dữ liệu duy nhất.
- `ho-so/`: file Word/Excel sinh tự động.
- `ra-soat/`: mọi báo cáo rà soát, kể cả khi chỉ rà soát một bộ hồ sơ có sẵn mà không build.

- Câu hỏi đầu vào theo từng bước (dùng khi hỏi người dùng từng ý) → [references/thong-tin-dau-vao.md](references/thong-tin-dau-vao.md)
- Định dạng bộ dữ liệu và lệnh `build-ctdt.py` → [references/du-lieu-ctdt.md](references/du-lieu-ctdt.md)
- Từng biểu mẫu: mục đích, nội dung bắt buộc, đầu vào, lỗi thường gặp → [references/bieu-mau.md](references/bieu-mau.md)
- Đề cương học phần BM05, BM05a, BM05b và quy tắc học liệu ASU → [references/de-cuong-hoc-phan.md](references/de-cuong-hoc-phan.md)
- PEO, PLO, PI hiện hành của ngành CNTT và quy tắc gắn CLO → [references/chuan-dau-ra-cntt.md](references/chuan-dau-ra-cntt.md)
- Danh mục rà soát trước khi trình ký → [references/checklist-ra-soat.md](references/checklist-ra-soat.md)

## Căn cứ: nói rõ với người dùng

- **Quy định của Bộ:** Thông tư 17/2021/TT-BGDĐT (22/6/2021) về chuẩn CTĐT; xây dựng, thẩm định và ban hành CTĐT. Quy chế đào tạo trình độ đại học: Thông tư 08/2021/TT-BGDĐT đã được **thay bằng Thông tư 56/2026/TT-BGDĐT** (hiệu lực 07/7/2026); hồ sơ lập từ tháng 7/2026 trở đi phải dẫn văn bản mới.
- **Quy định của Trường** (được ưu tiên ở các điểm Bộ không quy định chi tiết): Quyết định 1277/QĐ-ĐHLH (14/10/2024) về khối lượng kiến thức tối thiểu, chuẩn năng lực và quy định xây dựng, thẩm định, ban hành CTĐT; quy chế đào tạo tín chỉ của Trường cho từng khóa; thông báo, kế hoạch của Hiệu trưởng cho đợt xây dựng (ví dụ tích hợp nội dung quyền con người từ khóa 2026).
- Skill **không thay thế** các văn bản trên. Số điều, khoản, số tín chỉ tối thiểu, danh hiệu văn bằng (cử nhân, kỹ sư) phải đối chiếu văn bản gốc còn hiệu lực; chưa chắc thì đánh dấu `{{CẦN KIỂM TRA: ...}}`.
- Ngành CNTT dùng chuẩn đầu ra theo cách tiếp cận ABET (SO1–SO5, gọi là PLO1–PLO5) và có học phần dùng học liệu Arizona State University (liên minh ASU–Cintana).

## Một nguồn dữ liệu

Mọi văn bản trong hồ sơ đều chép lại cùng một bộ dữ liệu. Sai lệch giữa các văn bản là lỗi phổ biến nhất (đợt 2026 có ba mã khác nhau cho cùng học phần Thiết kế UI/UX). Vì vậy **không soạn từng file Word/Excel riêng**: ghi dữ liệu vào `du-lieu/` rồi sinh toàn bộ hồ sơ bằng `build-ctdt.py`.

| Dữ liệu | Ghi một lần ở | Sinh ra |
|---|---|---|
| Mã, tên, tín chỉ, LT/TH/BT, học kỳ, khối, nhóm tự chọn, học phần trước | `du-lieu/ke-hoach.csv` | BM03, chương trình điều hành, bảng CTĐT trong BM06, BM07, BM09.2; thông tin chung của đề cương |
| PEO, PLO, PI, ma trận PEO–PLO, vị trí việc làm | `du-lieu/chuan-dau-ra.json` | BM02, file PLO, BM08, BM09.2 |
| CLO và CLO–PI của từng học phần | `du-lieu/de-cuong/<mã>.md` | Đề cương BM05, sheet Map CLO-PI, ma trận học phần – PI trong BM09.2, tóm tắt học phần |
| Ngày, số văn bản, Hội đồng, căn cứ, người góp ý | `du-lieu/thong-tin.json` | Đầu văn bản, BM01, BM06, BM07 |
| Chương trình đối sánh | `du-lieu/doi-sanh.csv` | BM04 (tỷ lệ tự tính) |

## Sinh hồ sơ

```bash
uv run --with python-docx --with openpyxl python build-ctdt.py init chuong-trinh-dao-tao/<ngành>-<khóa> [--tu-ho-so "<thư mục hồ sơ cũ>"]
uv run --with python-docx --with openpyxl python build-ctdt.py build chuong-trinh-dao-tao/<ngành>-<khóa> [--chi BM03,BM05]
```

- **`init`** tạo bộ dữ liệu mẫu. Với `--tu-ho-so`, script nhập từ bộ hồ sơ Word/Excel đã có (BM03, chương trình điều hành, PLO, BM02, BM06, BM01, BM04, đề cương BM05) và ghi chú những chỗ cần kiểm tra vào `ra-soat/nhap-du-lieu.md`. Đề cương nhập tự động phải được đọc lại.
- **`build`** mở đúng file mẫu của từng biểu mẫu, giữ đầu trang, logo, khổ giấy và sinh nội dung mới vào `ho-so/`. Sau đó tự chạy `validate-ctdt.py` và ghi `ra-soat/ra-soat-tu-dong.md`.
- **Phần chỉ người thật cung cấp được:** ý kiến góp ý, phát biểu và kết luận trong họp, biểu quyết, chữ ký. Phiếu BM01 sinh ra để trống, biên bản BM06 sinh ra là khung có `{{...}}`.
- **Thứ tự sửa:** sửa dữ liệu, build lại, đọc báo cáo, rồi sửa tiếp. Không sửa tay file trong `ho-so/`; nếu người dùng đã sửa tay (ví dụ điền biên bản sau họp), đổi tên file đó trước khi build lại để không bị ghi đè.

## Công cụ kiểm tra

```bash
uv run --with python-docx --with openpyxl python validate-ctdt.py "<thư mục hồ sơ>" --nam 2026 --report chuong-trinh-dao-tao/<ngành>-<khóa>/ra-soat/ra-soat-tu-dong.md
```

Dùng trực tiếp khi rà soát một bộ hồ sơ có sẵn (do người khác lập); `build` đã tự gọi script này. Báo cáo rà soát viết tay (xếp mức ưu tiên, kèm điểm script không phát hiện) lưu cạnh báo cáo tự động trong `ra-soat/`. Script tự nhận diện file theo tên (`BM03*.xlsx`, `*điều hành*` hoặc `*dieu-hanh*.docx`, `PLO*.xlsx`, thư mục `BM05*`) và kiểm tra:

- **Kế hoạch:** LT+TH+BT = tổng TC; số tiết = 50 × TC; dòng "TỔNG CỘNG HỌC KỲ" và "TOÀN KHÓA" khớp tổng cộng; nhóm tự chọn ghi đủ TC, các lựa chọn bằng TC nhau. Áp dụng cho BM03 và mọi bảng kế hoạch nhúng trong BM06, BM07, chương trình điều hành; đối chiếu từng bảng với BM03.
- **Học phần trước:** tồn tại trong chương trình, xếp ở học kỳ trước; cảnh báo khi học phần yêu cầu một môn **tự chọn** (sinh viên chọn môn còn lại sẽ không đủ điều kiện).
- **Đề cương:** mã trong tên file khớp mã trong đề cương, không trùng mã; tên, TC, LT/TH/BT, học phần trước khớp BM03 và chương trình điều hành; CLO đánh số liên tục, có gắn PLO/PI, có LLO, được đánh giá; tổng tỷ lệ đánh giá 100%; PI có trong danh mục; CLO–PI khớp file PLO; dấu vết mẫu chưa điền (`……`, `DOCX`, `Cần bổ sung`, `{Khóa 2022}`, dòng tài liệu mẫu); năm ký khác năm của đợt; học phần trong BM03 chưa có đề cương.
- **Văn bản khác:** mã học phần không có trong BM03; phép tính tỷ lệ % dạng "33/54 … Tỷ lệ x%"; văn bản căn cứ vào văn bản có ngày **sau** ngày của chính nó.

Script chỉ kiểm tra được phần có cấu trúc. Nội dung (ý kiến góp ý có đúng ngành không, CLO có đo được không, mô tả có khớp nội dung tuần không) phải rà bằng [references/checklist-ra-soat.md](references/checklist-ra-soat.md).

## Quy trình

Làm tuần tự. Bước có chữ **DỪNG** thì chờ người dùng xác nhận. Ở mỗi bước, hỏi người dùng theo nhóm câu hỏi tương ứng trong [references/thong-tin-dau-vao.md](references/thong-tin-dau-vao.md), ghi câu trả lời vào `du-lieu/`, chạy `build-ctdt.py build ... --chi <biểu mẫu của bước>` và báo các chỗ còn `{{...}}`.

1. **Thu thập đầu vào và khởi tạo.** Ngành, mã ngành, niên khóa, khóa tuyển; CTĐT khóa trước (bản ban hành); thông báo, kế hoạch của Trường cho đợt xây dựng; danh sách Hội đồng; danh sách giảng viên phụ trách đề cương. Có hồ sơ cũ thì `init --tu-ho-so`, không thì `init`. Thiếu thông tin hành chính thì hỏi, không tự đặt.
2. **Đánh giá CTĐT đang thực hiện – BM08.** Một bảng cho khóa đã tốt nghiệp, một bảng cho khóa giữa chương trình. Số liệu khối kiến thức lấy từ CTĐT đã ban hành của khóa đó; số giảng viên, cơ sở vật chất lấy từ báo cáo của Khoa, có năm.
3. **Đối sánh – BM04.** Chọn CTĐT cùng ngành của ít nhất một trường trong nước và một trường nước ngoài; ghi nguồn (URL, năm áp dụng). So sánh với **danh mục học phần của CTĐT mới** (BM03), không dùng tên học phần của khóa cũ. Tính lại tỷ lệ.
4. **Lấy ý kiến – BM01.1 (doanh nghiệp, cựu sinh viên, chuyên gia) và BM01.2 (thành viên Hội đồng).** Claude chỉ soạn **mẫu phiếu**; nội dung ý kiến do người góp ý viết. **DỪNG**: chờ phiếu thật.
5. **Mục tiêu và chuẩn đầu ra – BM02 và file PLO.** Cập nhật PEO, PLO, PI, ma trận PEO–PLO; vị trí việc làm sau tốt nghiệp. **DỪNG**: người dùng duyệt chuẩn đầu ra trước khi làm kế hoạch.
6. **Kế hoạch đào tạo – BM03, chương trình điều hành.** Bố trí học phần theo 8 học kỳ, nhóm tự chọn, học phần trước. Chạy `validate-ctdt.py` tới khi phần kế hoạch không còn lỗi. **DỪNG**: duyệt kế hoạch.
7. **Đề cương học phần – BM05 / BM05a / BM05b** và **tóm tắt học phần**. Mỗi học phần trong BM03 một đề cương, tên file `HK<n>-<mã>-<Tên học phần>.docx`. Chọn mẫu theo mức dùng học liệu ASU. Ma trận CLO–PI trong file PLO cập nhật cùng lúc. Làm theo đợt, chạy kiểm tra sau mỗi đợt.
8. **Họp Hội đồng khoa học và đào tạo Khoa – BM06.** Claude soạn khung biên bản: thành phần, căn cứ, nội dung trình bày, bảng thay đổi so với khóa trước, bảng CTĐT. **Ý kiến phát biểu, kết luận, biểu quyết do thư ký ghi từ cuộc họp thật**; không tự viết.
9. **Cuốn CTĐT – BM09.2.** Ghép từ BM02, BM03, file PLO, tóm tắt học phần và đề cương. Ma trận học phần – PI lấy đúng từ file PLO.
10. **Tờ trình ban hành – BM07.** Căn cứ biên bản BM06 (số, ngày), bảng CTĐT lấy từ BM03. Chạy kiểm tra toàn bộ; báo cáo lỗi còn lại cho người dùng.

Người dùng chỉ yêu cầu một phần ("rà soát đề cương", "làm BM04", "kiểm tra kế hoạch") thì làm đúng phần đó nhưng vẫn theo quy tắc dưới đây và chạy kiểm tra liên quan.

## Quy tắc bắt buộc

- **Không bịa dữ kiện hành chính và ý kiến.** Không tự viết ý kiến góp ý, phát biểu trong họp, kết quả biểu quyết, số văn bản, ngày ký, chữ ký, thành phần Hội đồng, số liệu khảo sát. Chỗ chưa có để `{{...}}` và liệt kê lại cuối câu trả lời.
- **Ngày tháng hợp lệ.** Văn bản chỉ căn cứ vào văn bản đã có trước ngày của nó. Thứ tự hợp lý: BM08, BM04, BM01 → BM02 → BM03 → BM05 → BM06 → BM09.2 → BM07. Ngày ký trên đề cương là năm của đợt xây dựng.
- **Nhất quán tên gọi.** Ngành **Công nghệ thông tin** (mã 7480201) khác ngành **Công nghệ kỹ thuật thông tin**; không dùng lẫn trong PEO, PLO, đề cương. Tên học phần dùng đúng tên trong BM03 ở mọi văn bản. Một mã chỉ ứng với một học phần.
- **Không còn dấu vết mẫu hoặc khóa cũ:** `……`, `DOCX`, `(Cần bổ sung …)`, `{Khóa 2022}`, `{2025 trở về sau}`, dòng "Tên tác giả (năm xuất bản)", khung "Hướng dẫn sử dụng mẫu", ý kiến chép từ hồ sơ ngành khác (ví dụ góp ý về thương mại điện tử, thanh toán, "nhóm môn kinh tế và quản lý" trong hồ sơ ngành CNTT).
- **Học liệu ASU** theo [references/de-cuong-hoc-phan.md](references/de-cuong-hoc-phan.md): đúng mã mẫu BM05a/BM05b, khối bản quyền, nhãn nguồn [U]/[U-adapt]/[L], không đặt logo ASU rời, không dẫn link Canvas nội bộ, không dùng cụm "chương trình liên kết", "bằng do ASU cấp".
- **Dữ liệu cá nhân.** Hồ sơ có họ tên, chức vụ, đơn vị của người góp ý và thành viên Hội đồng. Nhắc người dùng trước khi commit thư mục hồ sơ lên repo công khai.
- **Thay đổi CTĐT đã ban hành** (đổi học phần, tín chỉ, chuẩn đầu ra) phải đi lại quy trình thẩm định, ban hành theo quy định của Trường; nhắc người dùng khi yêu cầu sửa thuộc loại này.
- **Đồng bộ với học phần LMS.** Khi đề cương thay đổi CLO, tên hoặc mã, cập nhật `course.json`, `thong-tin-hoc-phan.md`, `danh-gia-hoc-phan.md` của học phần tương ứng (skill `lms-lecture-builder`) và đề cương chi tiết giáo trình (skill `giao-trinh-builder`).
