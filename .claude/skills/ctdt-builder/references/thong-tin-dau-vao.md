# Thông tin đầu vào: hỏi người dùng theo từng bước

Dùng khi xây dựng CTĐT mới hoặc khi người dùng muốn được hỏi từng ý.

**Cách hỏi:**
- Hỏi **theo bước**, mỗi lượt một nhóm câu hỏi (dùng AskUserQuestion khi câu trả lời là lựa chọn, hỏi bằng văn bản khi cần số liệu, danh sách).
- Ghi câu trả lời vào đúng trường dữ liệu ngay sau mỗi lượt (cột "Ghi vào"), rồi mới hỏi tiếp.
- Người dùng chưa có thông tin thì ghi `{{...}}` và đi tiếp. Liệt kê các chỗ còn trống ở cuối mỗi bước.
- Không hỏi lại điều đã có trong dữ liệu hoặc đọc được từ hồ sơ cũ.
- Hỏi trước: người dùng có bộ hồ sơ khóa trước hoặc dự thảo (Word/Excel) không. Có thì chạy `build-ctdt.py init <thư mục> --tu-ho-so <thư mục hồ sơ>` để nhập sẵn, chỉ hỏi phần còn thiếu.

Định dạng từng file dữ liệu: [du-lieu-ctdt.md](du-lieu-ctdt.md).

## Bước 0 – Khởi tạo

| # | Câu hỏi | Ghi vào |
|---|---|---|
| 0.1 | Ngành, mã ngành, tên tiếng Anh? | `thong-tin.json`: `nganh`, `ma_nganh`, `nganh_en` |
| 0.2 | Niên khóa, khóa tuyển, năm của đợt xây dựng? | `nien_khoa`, `khoa_tuyen`, `nam`; tên thư mục `chuong-trinh-dao-tao/<ngành>-<khóa>` |
| 0.3 | Xây dựng mới hay điều chỉnh từ CTĐT khóa trước? Có file hồ sơ khóa trước không (đường dẫn)? | `--tu-ho-so`; `ke-hoach-khoa-truoc.csv` |
| 0.4 | Danh hiệu văn bằng (cử nhân / kỹ sư), loại hình, thời gian đào tạo? | `danh_hieu`, `loai_hinh`, `thoi_gian` |
| 0.5 | Trưởng khoa, trưởng ngành, người trình bày dự thảo tại cuộc họp? | `truong_khoa`, `truong_nganh`, `nguoi_trinh_bay` |
| 0.6 | Văn bản căn cứ của đợt này: quy chế đào tạo áp dụng cho khóa, thông báo/kế hoạch của Hiệu trưởng (số, ngày)? | `can_cu[]` |
| 0.7 | Quy tắc quy đổi số tiết lên lớp (1 TC LT = ? tiết, 1 TC TH = ? tiết)? | `quy_doi_tiet` |

## Bước 1 – Đánh giá CTĐT đang thực hiện (BM08)

| # | Câu hỏi | Ghi vào |
|---|---|---|
| 1.1 | Đánh giá khóa nào đã tốt nghiệp, khóa nào giữa chương trình? Có kế hoạch đào tạo (BM03) của các khóa đó không? | `danh_gia_ctdt[]`: `nien_khoa`, `trang_thai`, `ke_hoach` |
| 1.2 | Hiện trạng phương pháp dạy học, đánh giá học phần (ưu điểm, hạn chế)? | `danh_gia_ctdt[].Phương pháp dạy và học`, `.Đánh giá học phần` |
| 1.3 | Số giảng viên toàn thời gian theo học hàm, học vị, có năm số liệu? | `.Đội ngũ giảng viên` |
| 1.4 | Phòng học, phòng thực hành, thiết bị (số lượng, năm)? | `.Cơ sở vật chất` |
| 1.5 | Kết luận và hướng điều chỉnh? | `.ket_luan` |

## Bước 2 – Đối sánh (BM04)

| # | Câu hỏi | Ghi vào |
|---|---|---|
| 2.1 | Đối sánh với những chương trình nào (ít nhất 1 trong nước, 1 nước ngoài)? Có URL và năm áp dụng không? | `doi-sanh.csv`: `truong`, `chuong_trinh`, `nguon`, `nam` |
| 2.2 | Danh sách học phần của chương trình đối sánh (dán hoặc gửi link)? Claude ghép học phần tương đương, người dùng duyệt. | `mon_doi_sanh`, `ma_lhu` |

Claude có thể tra cứu chương trình đối sánh trên web, nhưng phải ghi nguồn và để người dùng xác nhận.

## Bước 3 – Ý kiến các bên liên quan (BM01.1, BM01.2)

| # | Câu hỏi | Ghi vào |
|---|---|---|
| 3.1 | Danh sách người góp ý: họ tên, đơn vị, loại (doanh nghiệp/cựu SV/chuyên gia → BM01.1; thành viên Hội đồng → BM01.2)? | `nguoi_gop_y[]` |
| 3.2 | **DỪNG**: gửi phiếu (in sẵn tên trong `ho-so/BM01-Phieu-y-kien/`) và chờ phiếu thật. Ý kiến được tóm tắt vào biên bản BM06 khi người dùng gửi lại. | — |

## Bước 4 – Mục tiêu và chuẩn đầu ra (BM02, file PLO)

| # | Câu hỏi | Ghi vào |
|---|---|---|
| 4.1 | Giữ nguyên PEO, PLO, PI của khóa trước hay điều chỉnh? Điều chỉnh điểm nào? | `chuan-dau-ra.json`: `peo`, `plo`, `pi` |
| 4.2 | Ma trận PEO – PLO? | `peo_plo` |
| 4.3 | Vị trí việc làm sau tốt nghiệp (theo nhóm)? | `vi_tri_viec_lam` |
| 4.4 | **DỪNG**: người dùng duyệt chuẩn đầu ra. | — |

## Bước 5 – Kế hoạch đào tạo (BM03, chương trình điều hành)

| # | Câu hỏi | Ghi vào |
|---|---|---|
| 5.1 | Tổng số tín chỉ mục tiêu, số tín chỉ tối đa mỗi học kỳ? | kiểm tra khi build |
| 5.2 | Học phần thêm, bỏ, đổi học kỳ, đổi tín chỉ so với khóa trước (kèm mã mới do Phòng Đào tạo cấp)? | `ke-hoach.csv` |
| 5.3 | Nhóm tự chọn ở mỗi học kỳ (chọn mấy trong mấy)? | cột `nhom_tu_chon` |
| 5.4 | Học phần trước, tiên quyết, song hành của từng học phần? | cột `hoc_truoc` |
| 5.5 | Khối kiến thức của từng học phần mới? | cột `khoi` |
| 5.6 | Chuỗi môn theo hướng (web, mobile, IoT, mạng, dữ liệu…)? | `chuoi_mon` |
| 5.7 | **DỪNG**: chạy build, sửa tới khi phần kế hoạch không còn lỗi; người dùng duyệt. | — |

## Bước 6 – Đề cương học phần (BM05/BM05a/BM05b, tóm tắt học phần)

Với từng học phần (theo đợt, ví dụ mỗi học kỳ một đợt):

| # | Câu hỏi | Ghi vào |
|---|---|---|
| 6.1 | Giảng viên phụ trách, email, giảng viên tham gia? | `de-cuong/<mã>.md` frontmatter |
| 6.2 | Dùng học liệu ASU không? Toàn phần hay tăng cường? Học phần ASU nguồn? | `mau`, mục `Bản quyền` |
| 6.3 | Có đề cương cũ, slide, bài giảng LMS trong repo để làm nguồn không? | — (Claude soạn nháp từ nguồn) |
| 6.4 | Giáo trình chính và tài liệu tham khảo (có năm, nhà xuất bản)? | mục `Tài liệu` |
| 6.5 | Mức độ được phép dùng AI trong học phần? | mục `Quy định` |
| 6.6 | **DỪNG**: giảng viên phụ trách duyệt CLO, ma trận CLO–PI, cơ cấu đánh giá. | — |

## Bước 7 – Họp Hội đồng (BM06)

| # | Câu hỏi | Ghi vào |
|---|---|---|
| 7.1 | Ngày, giờ, địa điểm họp; số biên bản? | `ngay.BM06`, `hop_hoi_dong`, `so_van_ban.BM06` |
| 7.2 | Thành phần Hội đồng theo quyết định thành lập (họ tên, chức vụ, vai trò); khách mời? | `hoi_dong[]`, `khach_moi{}` |
| 7.3 | Sau cuộc họp: ý kiến từng người, kết luận tiếp thu/giải trình, kết quả biểu quyết (từ thư ký). | điền vào file BM06 đã sinh (không đưa vào dữ liệu) |

## Bước 8 – Cuốn CTĐT (BM09.2) và tờ trình (BM07)

| # | Câu hỏi | Ghi vào |
|---|---|---|
| 8.1 | Điều kiện tốt nghiệp (ngoại ngữ, tin học, kỹ năng mềm) theo quy định của Trường cho khóa? | `dieu_kien_tot_nghiep` |
| 8.2 | Ngày hoàn thành BM09.2; ngày và số tờ trình? | `ngay.BM09`, `ngay.BM07`, `so_van_ban.BM07` |
| 8.3 | Ngày của các văn bản còn lại (BM08, BM04, BM01, BM02, BM03, BM05)? | `ngay.*` (build cảnh báo khi sai thứ tự) |
