# Hồ sơ biên soạn giáo trình (`giao-trinh/ho-so/`)

Các file đánh số được ghép thành một file Word: `uv run --with python-docx python build-textbook.py <hoc-phan> --ho-so`. Mẫu dưới đây chỉ là khung; **mọi thông tin hành chính, tên người, ý kiến góp ý, số quyết định phải do người dùng cung cấp**, chưa có thì để `{{...}}`. Nếu Trường có mẫu biểu riêng, dùng mẫu của Trường và giữ nội dung tương ứng.

Đối chiếu với Thông tư: 01 là bước 1 (Điều 7.2); 02–03 là bước 3–4 (Điều 7.2); 04, 05 và danh mục 06 là hồ sơ thẩm định (Điều 8.5 a–d).

## 02-phieu-lay-y-kien.md

```markdown
# Phiếu lấy ý kiến góp ý dự thảo giáo trình

**Giáo trình:** {{tên}} · **Học phần:** {{tên (mã)}} · **Bản dự thảo:** {{ngày/phiên bản}}

**Người góp ý:** {{họ tên}} · **Đơn vị/vai trò:** {{chuyên gia / giảng viên / người học / doanh nghiệp}}

| # | Tiêu chí | Đạt | Cần sửa | Ý kiến cụ thể (chương, mục, trang) |
|---|---|:-:|:-:|---|
| 1 | Phù hợp đề cương học phần, chuẩn đầu ra | | | |
| 2 | Nội dung khoa học, chính xác, cập nhật | | | |
| 3 | Trình bày logic, hệ thống, dễ hiểu | | | |
| 4 | Cân đối lý thuyết – thực hành, ví dụ thực tiễn | | | |
| 5 | Trích dẫn, nguồn tài liệu, bản quyền | | | |
| 6 | Câu hỏi, bài tập phù hợp mục tiêu | | | |
| 7 | Hình thức, khả năng tiếp cận (bản in, bản số) | | | |

**Ý kiến khác:**

**Kết luận chung:** ☐ Đồng ý sử dụng sau khi sửa nhỏ ☐ Cần sửa nhiều ☐ Không đồng ý
```

## 03-tong-hop-tiep-thu-giai-trinh.md

Chỉ ghi những ý kiến **người dùng đã nhận được và gửi lại**; trích đúng nội dung, không diễn giải lại làm lệch ý.

```markdown
# Bảng tổng hợp, tiếp thu và giải trình ý kiến góp ý

| # | Người góp ý | Vị trí | Nội dung góp ý | Tiếp thu / Giải trình | Vị trí đã sửa |
|---|---|---|---|---|---|
| 1 | {{...}} | Chương 2, mục 2.3 | ... | Tiếp thu: ... | Chương 2, mục 2.3, bảng 2.1 |
| 2 | {{...}} | ... | ... | Giải trình: lý do giữ nguyên (dẫn nguồn, đề cương) | — |

**Thống kê:** {{n}} ý kiến; tiếp thu {{a}}; giải trình {{b}}.
```

## 04-bao-cao-qua-trinh-bien-soan.md (Điều 8.5c)

```markdown
# Báo cáo quá trình biên soạn giáo trình

## 1. Thông tin chung
Tên giáo trình, học phần, chủ biên, người biên soạn, căn cứ biên soạn (quyết định giao nhiệm vụ {{số, ngày}}).

## 2. Mục tiêu và phạm vi
Tóm tắt từ đề cương chi tiết đã duyệt.

## 3. Quá trình thực hiện
| Giai đoạn | Thời gian | Kết quả | Minh chứng |
|---|---|---|---|
| Xây dựng đề cương chi tiết | | Đề cương được duyệt ngày {{...}} | 01-de-cuong-chi-tiet.md |
| Biên soạn | | {{n}} chương, {{n}} trang | Lịch sử phiên bản (git log) |
| Lấy ý kiến | | {{n}} phiếu từ {{n}} người | 02, phiếu đã nhận |
| Tiếp thu, hoàn thiện | | {{a}} tiếp thu, {{b}} giải trình | 03-tong-hop-tiep-thu-giai-trinh.md |

## 4. Cấu trúc giáo trình
Bảng chương – nội dung chính – CLO – số trang; tỷ lệ lý thuyết/thực hành.

## 5. Nguồn tài liệu và bản quyền
Nhóm nguồn đã dùng; tư liệu đã xin phép (kèm minh chứng); giấy phép hình ảnh, mã nguồn.

## 6. Sử dụng công cụ AI
Công cụ, khâu hỗ trợ (dàn ý, diễn đạt, sinh ví dụ, sơ đồ…), cách nhóm kiểm tra lại; khẳng định trách nhiệm nội dung thuộc người biên soạn (Điều 7.3).

## 7. Tự đánh giá theo Điều 5
Bảng từ checklist-yeu-cau.md: yêu cầu – kết quả – ghi chú.

## 8. Tồn tại và đề xuất
```

Lấy minh chứng tiến độ từ lịch sử git khi có: `git log --format="%ad %s" --date=short -- <hoc-phan>/giao-trinh/`.

## 05-van-ban-de-nghi-tham-dinh.md (Điều 8.5a)

```markdown
# Văn bản đề nghị thẩm định giáo trình

Kính gửi: {{cơ quan/đơn vị có thẩm quyền}}

Căn cứ Thông tư số 62/2026/TT-BGDĐT ngày 28/7/2026 của Bộ trưởng Bộ Giáo dục và Đào tạo;
Căn cứ {{quyết định giao nhiệm vụ biên soạn số ..., ngày ...}};

{{Tổ chức/cá nhân chủ trì biên soạn}} đề nghị thẩm định dự thảo giáo trình:
- Tên giáo trình: {{...}}
- Học phần: {{tên (mã), số tín chỉ}}
- Chủ biên: {{...}}; người biên soạn: {{...}}
- Dự thảo: {{n}} chương, {{n}} trang, phiên bản {{ngày}}

Hồ sơ gửi kèm (Điều 8 khoản 5): dự thảo giáo trình; báo cáo quá trình biên soạn và minh chứng; lý lịch khoa học của chủ biên và người biên soạn.

{{Nơi, ngày}}
{{Chức danh, họ tên, chữ ký}}
```

## 06-danh-muc-ho-so.md

```markdown
# Danh mục hồ sơ

## Hồ sơ đề nghị thẩm định (Điều 8 khoản 5)
| Thành phần | File | Trạng thái |
|---|---|---|
| a) Văn bản đề nghị thẩm định | 05-van-ban-de-nghi-tham-dinh | |
| b) Dự thảo giáo trình | Giao-trinh-<hoc-phan>.docx | |
| c) Báo cáo quá trình biên soạn và minh chứng | 04-bao-cao-...; 01; 02; 03 | |
| d) Lý lịch khoa học chủ biên, người biên soạn | {{do từng người cung cấp, lưu ngoài repo}} | |

## Hồ sơ trình phê duyệt (Điều 9 khoản 1, trong 15 ngày làm việc từ khi có kết luận thẩm định)
| Thành phần | File | Trạng thái |
|---|---|---|
| a) Văn bản đề nghị phê duyệt | {{...}} | |
| b) Dự thảo đã được Hội đồng kết luận đủ điều kiện | | |
| c) Biên bản họp Hội đồng thẩm định | {{do Hội đồng cung cấp}} | |
| d) Hồ sơ thẩm định | (mục trên) | |
```

## Lưu ý

- Lý lịch khoa học, phiếu góp ý có chữ ký chứa dữ liệu cá nhân: lưu theo chỉ dẫn của người dùng, không commit lên repo công khai (Điều 10.2; Luật Bảo vệ dữ liệu cá nhân).
- Không viết biên bản, kết luận Hội đồng: đó là văn bản của Hội đồng.
