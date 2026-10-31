# Rà soát hồ sơ xây dựng CTĐT ngành Công nghệ thông tin, niên khóa 2026–2030

Hồ sơ rà soát: `templates/xay-dung-ctdt-Dai hoc chinh quy/` (BM01.1–BM09.2, file PLO, 45 đề cương BM05, mẫu BM05a/BM05b ASU). Ngày rà soát: 31/10/2026.

Kết quả kiểm tra tự động: **60 lỗi, 128 cảnh báo**, chi tiết từng file trong [ra-soat-ho-so-goc-tu-dong.md](ra-soat-ho-so-goc-tu-dong.md). Chạy lại sau khi sửa:

```bash
uv run --with python-docx --with openpyxl python validate-ctdt.py "templates/xay-dung-ctdt-Dai hoc chinh quy" --nam 2026 --report chuong-trinh-dao-tao/cntt-2026/ra-soat/ra-soat-ho-so-goc-tu-dong.md
```

Dưới đây là các vấn đề xếp theo mức ưu tiên, gồm cả những điểm script không phát hiện được.

## 1. Cần xử lý trước khi trình ký

| # | Vấn đề | Văn bản | Đề xuất |
|---|---|---|---|
| 1 | Biên bản họp ngày 17/3/2026 căn cứ Kế hoạch 524/KH-ĐHLH (29/4/2026) và Quyết định 1152/QĐ-ĐHLH (13/6/2026), tức văn bản ban hành sau cuộc họp; Quyết định 1152 lại là quyết định ban hành CTĐT. | BM06 | Bỏ hai căn cứ này hoặc sửa đúng văn bản có trước ngày họp. |
| 2 | Thiết kế UI/UX có ba mã: 111050 (BM03, BM06, BM07, BM09.2), 111162 (chương trình điều hành, Tracking, Tóm tắt, file PLO) và 111056 (đề cương). | nhiều | Chốt một mã, sửa mọi văn bản. |
| 3 | Học phần trước xếp **cùng học kỳ**: 111244 và 111186 (HK6) cần 111242 (HK6); 199008 và 111246 (HK7) cần 111245 (HK7). | Chương trình điều hành | Đổi sang song hành (`***`) hoặc đổi điều kiện. |
| 4 | Học phần **bắt buộc** 111245 yêu cầu học phần **tự chọn** 111244; 111242/111243 yêu cầu 111241 (tự chọn). Sinh viên chọn môn còn lại sẽ không đủ điều kiện. | Chương trình điều hành | Đổi điều kiện thành "một trong hai", hoặc ghi rõ lộ trình tự chọn. |
| 5 | Dòng tổng HK4 ghi 21 TC (cộng các học phần được 22); tổng các học kỳ 153 so với toàn khóa 154. Pháp luật đại cương ghi 100 tiết (BM03: 150). | BM07 | Lấy lại bảng từ BM03. |
| 6 | Tỷ lệ đối sánh tính sai: 33/54 ghi 47,27% (đúng 61,11%); 21/54 ghi 38,18% (đúng 38,89%). | BM04 | Tính lại; đồng thời bỏ các môn không còn trong CTĐT 2026 (Blockchain, Lập trình trên môi trường Windows, Khai phá dữ liệu và Học máy cơ bản, Thiết kế hệ thống mạng nâng cao), ghi nguồn và năm của chương trình đối sánh. |
| 7 | Ý kiến chép từ hồ sơ ngành khác: BM01.2 nói về "lĩnh vực TMĐT", "AI trong Marketing, SEO, FB Ads"; BM06 có góp ý về thanh toán, "Quản trị chiến lược", "nhóm môn kinh tế và quản lý". | BM01.2, BM06 | Người góp ý viết lại phiếu đúng ngành; biên bản ghi đúng ý kiến tại cuộc họp và có kết luận tiếp thu hoặc giải trình cho từng ý kiến. |
| 8 | File "HK7-111189 – PHÁT TRIỂN ỨNG DỤNG" mang mã 111173, nội dung Kiến tập; hai file 111178 (hướng đối tượng, hướng quan hệ) giống hệt nhau, trong khi BM03 dùng 111241 và 111179. | BM05 | Soạn lại đề cương 111189, 111241, 111179. |
| 9 | Đề cương cho học phần không có trong BM03: 111185 Lập trình Python cho học máy, 111190 Trí tuệ nhân tạo. Thiếu đề cương: 111159, 111174, 111050/111162, 111160, 111241, 111179, 199006, 111189, 199007, 199008. | BM05 | Bỏ hoặc chuyển hai đề cương thừa; soạn đề cương còn thiếu. |
| 10 | Đề cương Lập trình Back-End ghi tên "Phát triển ứng dụng di động". | BM05 111176 | Sửa tên. |

## 2. Không nhất quán giữa các văn bản

- **Số CLO và ma trận CLO–PI:** gần như mọi đề cương có số CLO hoặc PI khác sheet "Map CLO-PI" của file PLO. Ví dụ Nhập môn Ngành: đề cương 4 CLO (CLO2 → PI2.1), file PLO 3 CLO (CLO2 → PI3.1), BM09.2 lại gắn PI3.2, 3.3, 5.1, 5.2. Cần chọn file PLO làm nguồn và chép lại vào đề cương, BM09.2.
- **Tên ngành trong chuẩn đầu ra:** PEO1, PLO1, PLO2 (file PLO, BM08, BM09.2) viết "công nghệ kỹ thuật thông tin"; BM02 viết "công nghệ thông tin". Đề cương 111242 ghi "bắt buộc với sinh viên ngành Công nghệ kỹ thuật thông tin".
- **Vị trí việc làm:** BM02 liệt kê ba khối với nhiều vị trí; BM09.2 chỉ nêu vị trí về mạng.
- **Tên học phần khác BM03:** "Điện tử cơ bản", "Cấu trúc và lắp ráp máy tính", "Toán rời rạc", "Nhập môn phát triển kỹ thuật", "Nhập môn Công nghệ thông tin" (BM03: "Nhập môn Ngành").
- **Mã học phần Kiểm thử:** BM03 dùng 199005 "Software Verification, Validation, and Testing"; Tóm tắt học phần ghi 111187; đề cương và Tracking gọi "Kiểm thử và đảm bảo chất lượng phần mềm". Học phần trên LMS của repo đang dùng mã **111117**.
- **Nhập môn ngành:** BM03 mã 111154 "Nhập môn Ngành"; học phần trên LMS của repo dùng mã **111106** "Nhập môn Công nghệ Thông tin" với 4 CLO.
- **Khối kiến thức:** file PLO xếp Phần mềm mã nguồn mở, Thiết kế UI/UX, Thiết kế web, Cơ sở dữ liệu vào "Chuyên ngành"; BM09.2 xếp vào "Cơ sở ngành".
- **Niên khóa:** BM06 dùng cả 2026–2030 và 2026–2031.
- **Tổng số tiết toàn khóa:** BM03 7700; BM06 7770; BM07 7650.
- **Sheet 4 của BM03:** dùng mã cũ 111212–111215 cho các học phần 111242–111246; tên "AI tạo sinh và Đại lý tự hành", "kể chuyển".
- **Tracking và Tóm tắt học phần:** còn học phần đã bỏ (111177, 111180, 111185, 111190, 111191), thiếu 111241–111246 (Tracking).

## 3. Lỗi trong từng đề cương (nhóm lỗi; chi tiết trong báo cáo tự động)

- Tín chỉ gõ dính: "66" (Thực tập), "31", "32"; LT/TH/BT ghi bằng số tiết (15-45-0, 30-30-0) hoặc sai so với BM03 (1-1-1 thay cho 1-2-0 ở Back-End, Di động, Web; 1-2-0 thay cho 2-0-1 ở Generative AI; 2-0-0 thay cho 1-1-0 ở Tín hiệu số).
- Môn học trước ghi tên không có mã, ghi mã khóa cũ (111103, 111105, 111038, `{Khóa 2022}`), hoặc "Không" trong khi chương trình điều hành có yêu cầu: 21 đề cương.
- Bảng đánh giá nhắc CLO5 nhưng Bảng CLO chỉ có 4 (6 đề cương); CLO không có LLO; PI6.3 không tồn tại; tổng tỷ lệ 60% (111181); một số bảng không ghi tỷ lệ %.
- Ngày ký năm 2023 hoặc 2025 ở 27 đề cương; email giảng viên trống; "(Cần bổ sung tên GV)"; chữ "DOCX" trong tên học phần 111242.
- Nhập môn CNTT (111154): kế hoạch chỉ có 7 bài cho 15 tuần, Bài 2 lặp hai hàng, tài liệu tham khảo còn dòng mẫu.
- Tóm tắt Nhập môn lập trình nói dạy Python nhưng tài liệu tham khảo là sách lập trình C.

## 4. Cần đối chiếu văn bản gốc

- **Thông tư 08/2021/TT-BGDĐT** (dẫn trong BM06) đã được thay bằng Thông tư 56/2026/TT-BGDĐT từ 07/7/2026. Hồ sơ đợt sau phải dẫn văn bản mới.
- **Tình trạng hiệu lực của Thông tư 17/2021/TT-BGDĐT:** cần kiểm tra.
- **Điều kiện tốt nghiệp (BM09.2)** còn chữ "Ví dụ:", chuẩn "B Ngoại ngữ" và dẫn quy chế khóa 2022–2026 (Quyết định 311/QĐ-ĐHLH ngày 05/8/2021). Cần thay bằng quy chế áp dụng khóa 2026 (Quyết định 03/QĐ-ĐHLH ngày 02/01/2026 theo BM06) và chuẩn đầu ra tiếng Anh TOEIC từ 400 trở lên hoặc chứng chỉ tương đương.
- **Bìa BM09.2** ghi "KỸ SƯ CHÍNH QUY": cần đối chiếu quy định về danh hiệu văn bằng cho chương trình 154 tín chỉ.
- **Số tiết lên lớp trong BM03** không theo một quy tắc:
  - Nhập môn Ngành 3 TC lý thuyết nhưng có 30 tiết thực hành.
  - Triết học 3 TC lý thuyết chỉ 15 tiết.
  - Ghi chú "chuyển về 15 tiết cho giống k25".
  
  Cần quy tắc quy đổi theo quy định của Trường.

## 5. Dữ liệu cá nhân

Hồ sơ có họ tên, chức vụ, đơn vị của thành viên Hội đồng, doanh nghiệp, cựu sinh viên. Thư mục `templates/xay-dung-ctdt-Dai hoc chinh quy/` hiện **chưa được commit**. Nên quyết định có đưa lên repo hay không trước khi commit.
