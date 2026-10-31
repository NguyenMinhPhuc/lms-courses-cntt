# Danh mục rà soát hồ sơ CTĐT trước khi trình ký

Chạy `validate-ctdt.py` trước (các mục đánh dấu ⚙ script đã kiểm tra), rồi rà các mục còn lại bằng cách đọc văn bản.

## A. Toàn bộ hồ sơ

- [ ] ⚙ Một mã một học phần; mã, tên, tín chỉ, LT/TH/BT, học kỳ trùng BM03 ở mọi văn bản.
- [ ] Tên ngành "Công nghệ thông tin", mã ngành 7480201 thống nhất; không lẫn "Công nghệ kỹ thuật thông tin", "chuyên ngành".
- [ ] Niên khóa thống nhất (ví dụ 2026–2030) ở mọi tiêu đề, căn cứ.
- [ ] ⚙ Không văn bản nào căn cứ vào văn bản có ngày sau nó. Thứ tự ngày: BM08, BM04, BM01 → BM02 → BM03 → BM05 → BM06 → BM09.2 → BM07.
- [ ] Văn bản pháp quy được dẫn còn hiệu lực tại ngày ký (Thông tư 08/2021 hết hiệu lực từ 07/7/2026, thay bằng Thông tư 56/2026/TT-BGDĐT).
- [ ] ⚙ Không còn dấu vết mẫu: `……`, `DOCX`, `Cần bổ sung`, `{Khóa 20xx}`, `{2025 trở về sau}`, dòng tài liệu mẫu, khung hướng dẫn.
- [ ] Không có nội dung chép từ hồ sơ ngành khác.
- [ ] Số văn bản, ký hiệu đúng loại (`/BB-HĐKH`, `/TTr-CNTT`) và trùng nhau khi văn bản này dẫn văn bản kia.
- [ ] Họ tên, học vị viết đúng một kiểu ("TS.", "ThS."); không gõ dư dấu.
- [ ] Đã hỏi người dùng trước khi đưa hồ sơ có dữ liệu cá nhân lên repo công khai.

## B. Kế hoạch đào tạo (BM03, chương trình điều hành, bảng trong BM06, BM07, BM09.2)

- [ ] ⚙ LT+TH+BT = TC; số tiết tổng = 50 × TC.
- [ ] ⚙ Dòng tổng học kỳ, toàn khóa đúng; tổng tín chỉ toàn khóa trùng điều kiện tốt nghiệp (154).
- [ ] ⚙ Mọi lựa chọn tự chọn ghi đủ TC, LT/TH/BT và bằng nhau.
- [ ] ⚙ Học phần trước có trong chương trình, xếp học kỳ trước; học phần bắt buộc không phụ thuộc học phần tự chọn.
- [ ] Số tiết lên lớp tính theo một quy tắc ghi rõ ở chú thích.
- [ ] Tỷ lệ khối kiến thức (BM09.2) cộng đúng và khớp phân loại khối của từng học phần trong đề cương.
- [ ] Khối lượng tối thiểu, danh hiệu văn bằng đúng quy định hiện hành của Bộ và Quyết định 1277/QĐ-ĐHLH.
- [ ] Mỗi học kỳ không quá số tín chỉ tối đa theo quy chế của Trường.

## C. Chuẩn đầu ra (BM02, file PLO, BM09.2)

- [ ] PEO, PLO, PI giống từng chữ ở BM02, BM08, BM09.2, file PLO, đề cương.
- [ ] Nhãn đúng: PEO ở mục tiêu, PLO/SO ở chuẩn đầu ra.
- [ ] Ma trận PEO – PLO: mỗi PEO có ít nhất 2 PLO hỗ trợ.
- [ ] Ma trận học phần – PI (BM09.2) chép đúng sheet Map CLO-PI; mỗi học phần chỉ ở một nhóm; đủ mọi học phần chuyên môn kể cả Kiến tập, Thực tập, Tốt nghiệp.
- [ ] Mỗi PI được ít nhất 2–3 học phần đánh giá; học phần đại cương không gắn PI gượng ép.
- [ ] Vị trí việc làm ở BM02 và BM09.2 giống nhau.
- [ ] Điều kiện tốt nghiệp ghi đúng chuẩn ngoại ngữ (TOEIC ≥ 400 hoặc tương đương), tin học, kỹ năng mềm theo quy định của Trường áp dụng cho khóa.

## D. Đề cương (BM05, BM05a, BM05b)

- [ ] ⚙ Mỗi học phần chuyên môn trong BM03 có đề cương; không có đề cương cho học phần đã bỏ.
- [ ] ⚙ Tên file `HK<n>-<mã>-<Tên>`, mã trong file và nội dung trùng nhau.
- [ ] ⚙ Thông tin chung trùng BM03 và chương trình điều hành (TC, LT/TH/BT bằng tín chỉ, môn học trước có mã).
- [ ] ⚙ CLO liên tục, gắn PI hợp lệ, có LLO, được đánh giá; tổng tỷ lệ 100%; CLO–PI trùng file PLO.
- [ ] CLO dùng động từ đo được, mức Bloom khớp động từ.
- [ ] Kế hoạch 15 tuần đầy đủ, không lặp hàng; nội dung tuần khớp mô tả học phần.
- [ ] Tài liệu tham khảo đủ thông tin, có năm, phù hợp ngôn ngữ/công nghệ dạy (ví dụ dạy Python thì không chỉ có sách C).
- [ ] Giảng viên phụ trách có họ tên và email; ngày ký năm của đợt.
- [ ] Học phần ASU dùng đúng mẫu BM05a/BM05b và qua danh mục kiểm tra trong [de-cuong-hoc-phan.md](de-cuong-hoc-phan.md#học-phần-dùng-học-liệu-asu-bm05a-bm05b).
- [ ] File Tracking và Tóm tắt học phần đã cập nhật theo BM03.

## E. Ý kiến và biên bản (BM01.1, BM01.2, BM06)

- [ ] Phiếu có họ tên, đơn vị, ngày, chữ ký; ngày trước ngày họp.
- [ ] BM01.2 có kết luận "đáp ứng / không đáp ứng" ở từng dòng.
- [ ] Ý kiến đúng ngành; số liệu trong ý kiến (số tín chỉ) đúng CTĐT đang lấy ý kiến.
- [ ] BM06 có kết luận tiếp thu hoặc giải trình cho từng ý kiến, chỉ ra thay đổi trong CTĐT.
- [ ] BM06 có thành phần đúng quyết định thành lập Hội đồng, kết quả thông qua, chữ ký chủ tịch, thư ký.

## F. Đối sánh và đánh giá (BM04, BM08)

- [ ] ⚙ Tỷ lệ % tính đúng.
- [ ] BM04 ghi nguồn, năm của chương trình đối sánh; dùng danh mục học phần CTĐT mới.
- [ ] BM08 đúng niên khóa ở tiêu đề và bảng; tổng các khối kiến thức đúng; số liệu giảng viên cộng ra đúng tổng.
