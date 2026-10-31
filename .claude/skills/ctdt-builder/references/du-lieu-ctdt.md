# Bộ dữ liệu CTĐT và lệnh build-ctdt.py

Mỗi CTĐT (một ngành, một khóa tuyển) là một thư mục trong `chuong-trinh-dao-tao/`:

```
chuong-trinh-dao-tao/<nganh>-<khoa>/        ví dụ cntt-2026, cntt-2027
├── du-lieu/                  SỬA Ở ĐÂY
│   ├── thong-tin.json
│   ├── ke-hoach.csv
│   ├── chuan-dau-ra.json
│   ├── doi-sanh.csv                (tùy chọn)
│   ├── ke-hoach-khoa-truoc.csv     (tùy chọn)
│   └── de-cuong/<mã>.md
├── ho-so/                    SINH TỰ ĐỘNG, không sửa tay
│   ├── BM01-Phieu-y-kien/          phiếu trống + phiếu in sẵn tên từng người góp ý
│   ├── BM02-Cong-bo-chuan-dau-ra.docx
│   ├── BM03-Ke-hoach-dao-tao-<đv>-<khóa>.xlsx
│   ├── PLO-<khóa>-Chuan-dau-ra-va-ma-tran-CLO-PI.xlsx
│   ├── Chuong-trinh-dao-tao-dieu-hanh.docx
│   ├── BM04-Bang-doi-chieu-so-sanh-CTDT.docx
│   ├── BM05-De-cuong/HK<n>-<mã>-<Tên>.docx
│   ├── Tom-tat-hoc-phan.docx
│   ├── BM06-Bien-ban-hop-HDKH-va-DT.docx     (khung; thư ký điền ý kiến, kết luận)
│   ├── BM07-To-trinh-de-nghi-ban-hanh-CTDT.docx
│   ├── BM08-Danh-gia-CTDT.docx
│   └── BM09.2-Chuong-trinh-dao-tao-<đv>-<khóa>.docx
└── ra-soat/                  báo cáo rà soát
    ├── ra-soat-tu-dong.md          validate-ctdt.py chạy trên ho-so/ sau mỗi lần build
    ├── nhap-du-lieu.md             ghi chú khi nhập từ hồ sơ cũ (--tu-ho-so)
    └── ra-soat-<...>.md            báo cáo rà soát viết tay (hồ sơ do người khác lập…)
```

Rà soát một bộ hồ sơ có sẵn (không build) cũng lưu vào `chuong-trinh-dao-tao/<nganh>-<khoa>/ra-soat/`.

## Lệnh

```bash
# tạo bộ dữ liệu mẫu cho CTĐT mới
uv run --with python-docx --with openpyxl python build-ctdt.py init chuong-trinh-dao-tao/cntt-2027
# hoặc nhập từ một bộ hồ sơ Word/Excel đã có (BM03, chương trình điều hành, PLO, BM02, BM06, BM01, BM04, BM05)
uv run --with python-docx --with openpyxl python build-ctdt.py init chuong-trinh-dao-tao/cntt-2027 --tu-ho-so "templates/xay-dung-ctdt-Dai hoc chinh quy"
# sinh hồ sơ (toàn bộ hoặc một phần) và rà soát
uv run --with python-docx --with openpyxl python build-ctdt.py build chuong-trinh-dao-tao/cntt-2027
uv run --with python-docx --with openpyxl python build-ctdt.py build chuong-trinh-dao-tao/cntt-2027 --chi BM03,DH,PLO,BM05
```

Mã cho `--chi`: BM01, BM02, BM03, PLO, DH (chương trình điều hành), BM04, BM05, TT (tóm tắt học phần), BM06, BM07, BM08, BM09.

- **Khung lấy từ file mẫu:**
  - Mỗi file Word mở từ file mẫu tương ứng trong `thu_muc_mau` (mặc định `templates/xay-dung-ctdt-Dai hoc chinh quy/`).
  - Giữ đầu trang, logo, lề, khổ giấy, header/footer phía trước tiêu đề; thay ngày, số văn bản; nội dung sau tiêu đề sinh mới.
  - Font nhúng của mẫu bị loại để file nhẹ (khoảng 20 KB thay vì 900 KB).
  - Không có mẫu thì dùng khung trống A4.
- **Đổi mẫu:** đặt mẫu mới vào thư mục mẫu, giữ tên khớp mẫu tìm kiếm trong `FORMS` của `build-ctdt.py` (ví dụ `BM07*.docx`, `BM05*/HK3-111166*.docx`), hoặc sửa `FORMS`.
- **Sau khi build:**
  - Mở BM09.2 bằng Word, nhấn F9 ở mục lục.
  - File đang mở trong Word/Excel thì không ghi được: đóng rồi build lại.
- **Ổ đĩa:** cả bộ hồ sơ khoảng 2 MB.

## thong-tin.json

| Khóa | Ý nghĩa |
|---|---|
| `nganh`, `nganh_en`, `ma_nganh`, `trinh_do`, `danh_hieu`, `loai_hinh`, `thoi_gian`, `ten_chuong_trinh` | Thông tin ngành, văn bằng |
| `nien_khoa` ("2026 - 2030"), `khoa_tuyen` ("2026"), `nam` (2026) | Niên khóa; `nam` dùng kiểm tra năm ký đề cương |
| `don_vi`, `ky_hieu_don_vi`, `noi_ky`, `truong_khoa`, `truong_nganh`, `nguoi_trinh_bay` | Đơn vị, người ký |
| `thu_muc_mau` | Thư mục file mẫu (tương đối so với gốc repo) |
| `quy_doi_tiet` | `{"lt": 15, "th": 30}`: tính số tiết LT/TH lên lớp trong BM03; `{}` để trống |
| `ngay` | `{"BM08": "2026-03-01", …, "BM07": "2026-04-19"}`: ngày từng văn bản (YYYY-MM-DD); build cảnh báo khi sai thứ tự |
| `so_van_ban` | `{"BM06": "26030/BB-HĐKH", "BM07": "26056/TTr-CNTT"}` |
| `hop_hoi_dong` | `gio`, `dia_diem`, `ket_thuc`, `chu_tich`, `thu_ky` |
| `hoi_dong` | `[{ho_ten, chuc_vu, vai_tro}]` theo quyết định thành lập Hội đồng |
| `khach_moi` | `{"Doanh nghiệp sử dụng lao động": [{ho_ten, chuc_vu}], …}` |
| `can_cu` | `[{van_ban, ngay}]`: căn cứ trong BM06; build cảnh báo văn bản có ngày sau ngày họp |
| `nguoi_gop_y` | `[{ho_ten, don_vi, loai: "BM01.1" \| "BM01.2"}]`: sinh phiếu in sẵn tên |
| `chuoi_mon` | `{"Lập trình ứng dụng web": ["111164", "111171", …]}` |
| `dieu_kien_tot_nghiep` | Danh sách dòng; `{tong}` = tổng tín chỉ, `{khoa}` = khóa tuyển |
| `danh_gia_ctdt` | `[{nien_khoa, trang_thai, ke_hoach: "ke-hoach-khoa-truoc.csv", "Phương pháp dạy và học": "...", "Đánh giá học phần": "...", "Đội ngũ giảng viên": "...", "Cơ sở vật chất": "...", ket_luan}]` cho BM08 |
| `bm02_kem_pi` | `true` (mặc định): BM02 liệt kê PI dưới từng PLO |

## ke-hoach.csv (mở bằng Excel, lưu dạng CSV UTF-8)

| Cột | Ví dụ | Ghi chú |
|---|---|---|
| `hoc_ky` | 5 | 1–8 |
| `ma` | 111176 | |
| `ten` | Lập trình Back-End | tên dùng ở mọi văn bản |
| `ten_en` | Back-End Programming | |
| `tc`, `lt`, `th`, `bt` | 3, 1, 2, 0 | tín chỉ; số tiết tổng = 50 × tc |
| `khoi` | Chuyên ngành | Lý luận chính trị · Ngoại ngữ · Đại cương khác · Giáo dục thể chất · Giáo dục quốc phòng · Cơ sở ngành · Chuyên ngành · Chuyên nghiệp khác · Thực tập · Tốt nghiệp |
| `nhom_tu_chon` | HK5-1 | các học phần cùng mã nhóm là một nhóm "chọn 1"; `HK6-2:2` = chọn 2 |
| `hoc_truoc` | `111170**; 111171*` | `*` tiên quyết, `**` học trước, `***` song hành |
| `ghi_chu` | | in vào cột ghi chú BM03 |

Thứ tự dòng trong file là thứ tự in trong mọi bảng. `ke-hoach-khoa-truoc.csv` cùng định dạng: dùng để tự lập bảng "học phần mới / bỏ / đổi học kỳ / đổi khối lượng" trong BM06 và bảng khối kiến thức trong BM08.

## chuan-dau-ra.json

```json
{
  "peo": [{"ma": "PEO1", "noi_dung": "...", "nang_luc": "Năng lực nghề nghiệp"}],
  "plo": [{"ma": "PLO1", "noi_dung": "...", "mien": "Kiến thức"}],
  "pi":  [{"ma": "1.1", "noi_dung": "...", "target": 0.75}],
  "peo_plo": {"PLO1": ["PEO1", "PEO2"]},
  "vi_tri_viec_lam": [{"nhom": "Khối doanh nghiệp CNTT", "mo_ta": "...", "muc": ["Lập trình viên ...", "..."]}],
  "hoc_nang_cao": "Có khả năng học sau đại học ..."
}
```

`mien` là một trong: Kiến thức, Kỹ năng, Thái độ, Năng lực tự chủ và trách nhiệm. PI thuộc PLO theo số trước dấu chấm.

## doi-sanh.csv

Cột: `truong, chuong_trinh, nguon, nam, mon_doi_sanh, ma_lhu, ghi_chu`. Mỗi dòng là một học phần của chương trình đối sánh; `ma_lhu` là mã học phần LHU tương đương (nhiều mã cách nhau bằng `;`, để trống nếu không có). Học phần LHU không được ghép sẽ tự vào cột "không tương đương"; tỷ lệ % tính tự động trên số học phần có tín chỉ của LHU.

## de-cuong/<mã>.md

Tên, tín chỉ, LT/TH/BT, khối, môn học trước, tính chất (bắt buộc/tự chọn) **lấy từ ke-hoach.csv**, không ghi lại trong đề cương.

```markdown
---
ma: 111176
mau: BM05                 # BM05 | BM05a | BM05b
giang_vien: Hoàng Hải Dương
email: ...@lhu.edu.vn
giang_vien_tham_gia: ...
tom_tat: (tùy chọn) đoạn dùng cho Tóm tắt học phần và BM09.2; mặc định lấy mục Mô tả
---
## Mô tả
## Chuẩn đầu ra          bảng | CLO | Nội dung | Cấp độ | PLO/SO/PI |  (ma trận CLO–PI trong file PLO và BM09.2 sinh từ bảng này)
## Kế hoạch giảng dạy    bảng 15 tuần
## Ma trận LLO – CLO     bảng | LLO | CLO1 | … | Thành phần đánh giá |
## Đánh giá              bảng | Thành phần | Hình thức | CLOs | Tỷ lệ (%) |  (A1., A2., A3.)
## Quy định
## Tài liệu              ### Giáo trình / ### Tài liệu tham khảo, mỗi mục "- [n] ..."
## Phần mềm
```

- **Mẫu ASU (BM05a/BM05b):** thêm mục `## Bản quyền` (bảng Mục 0) đặt trước `## Mô tả`. Bảng phụ đặt ngay sau mục chính, tên bắt đầu bằng tên mục chính và dấu gạch, ví dụ `## Chuẩn đầu ra – Bảng 1b: Đối sánh CLO với chuẩn đầu ra gốc của ASU`, `## Kế hoạch – Bảng 2b: Bảng kê tỷ lệ kế thừa`. Bảng CLO, kế hoạch, đánh giá thêm cột nguồn `[U]/[U-adapt]/[L]`; build in đúng các cột có trong Markdown.
- **Trong ô bảng:** xuống dòng bằng `<br>`; chữ đậm `**...**`. Dòng `<!-- ... -->` là ghi chú, không in.
