# Chương 3. Cấu trúc rẽ nhánh và lưu đồ thuật toán

## Mục tiêu chương

Sau khi học chương này, người học có thể:

- Biểu diễn thuật toán có rẽ nhánh bằng lưu đồ với bốn ký hiệu cơ bản; vẽ lưu đồ trên Draw.io (CLO2).
- Viết đúng các lệnh `if`, `if – else`, `if – elif – else` theo quy tắc thụt lề của Python (CLO1).
- Sắp xếp các điều kiện của rẽ nhánh nhiều nhánh đúng thứ tự và kiểm thử bằng giá trị biên (CLO1).
- Kết hợp điều kiện bằng `and`, `or`, `not` và viết rẽ nhánh lồng nhau (CLO1).
- Đối chiếu lưu đồ với mã nguồn để phát hiện chỗ không khớp (CLO1, CLO2).

## 3.1. Lưu đồ thuật toán

### 3.1.1. Bốn ký hiệu cơ bản

Máy ATM chỉ cho rút tiền khi mã PIN đúng, số dư đủ và số tiền là bội số của 50.000 đồng. Thiếu một điều kiện, hoặc kiểm tra sai thứ tự, ngân hàng sẽ chịu thiệt hại. Khi một chương trình phải chọn giữa nhiều hướng xử lý, mô tả bằng lời rất dễ bỏ sót trường hợp. **Lưu đồ thuật toán** (flowchart) giải quyết vấn đề này bằng hình vẽ: mỗi bước là một khối, mũi tên chỉ thứ tự thực hiện, và mọi nhánh rẽ đều hiện rõ trên giấy.

Các ký hiệu lưu đồ được chuẩn hóa trong tiêu chuẩn ISO 5807:1985 [1]. Giáo trình dùng bốn ký hiệu cơ bản:

| Bảng 3.1. Ký hiệu lưu đồ | Hình dạng | Dùng cho |
|---|---|---|
| Bắt đầu / Kết thúc | Hình chữ nhật bo tròn hai đầu | Điểm vào và điểm ra của thuật toán |
| Nhập / Xuất | Hình bình hành | `input()`, `print()` |
| Xử lý | Hình chữ nhật | Phép gán, tính toán |
| Điều kiện | Hình thoi, có hai lối ra Đúng và Sai | Điều kiện của `if` và của vòng lặp |

![Hình 3.1. Bốn ký hiệu lưu đồ cơ bản: bắt đầu/kết thúc (chữ nhật bo tròn), nhập/xuất (bình hành), xử lý (chữ nhật), điều kiện (hình thoi)](../Slides/images/bai-03-ky-hieu.png)

### 3.1.2. Quy tắc vẽ

Một lưu đồ đúng cần thỏa các quy tắc sau:

1. Có đúng một điểm **Bắt đầu**; mọi đường đi đều dẫn tới **Kết thúc**.
2. Mũi tên chỉ rõ hướng; luồng chính đi từ trên xuống dưới hoặc từ trái sang phải.
3. Mỗi hình thoi có **đúng hai lối ra**, ghi nhãn **Đúng** và **Sai** trên mũi tên.
4. Nội dung trong mỗi khối ngắn gọn, viết gần với mã nguồn (ví dụ `diem >= 4?`), để đối chiếu dễ dàng.
5. Các mũi tên không cắt nhau khi có thể tránh.

Lưu đồ là sản phẩm thiết kế được đánh giá trong học phần (CLO2). Người học vẽ lưu đồ **trước** khi viết mã để thấy hết các nhánh, và **sau** khi viết mã để kiểm tra mã có khớp thiết kế không.

### 3.1.3. Vẽ lưu đồ trên Draw.io

Draw.io (diagrams.net) là công cụ vẽ sơ đồ miễn phí, dùng được trên trình duyệt tại app.diagrams.net hoặc ngay trong VS Code qua extension Draw.io Integration (tạo file có phần mở rộng `.drawio`) [2]. Các thao tác cơ bản:

1. Chọn nhóm hình **Flowchart** ở thanh bên trái; kéo hình vào trang vẽ.
2. Nhấp đúp vào hình để gõ nội dung.
3. Rê chuột lên một hình, kéo mũi tên xanh từ cạnh hình tới hình kế tiếp để nối.
4. Nhấp đúp lên mũi tên để ghi nhãn **Đúng** hoặc **Sai**.
5. Xuất ảnh bằng **File → Export as → PNG** để chèn vào báo cáo.

## 3.2. Lệnh if và if – else

### 3.2.1. Cú pháp và thụt lề

Lệnh `if` thực hiện một khối lệnh khi điều kiện đúng [3], [4]:

```python
if dieu_kien:
    lenh_1
    lenh_2
```

Ba thành phần bắt buộc: từ khóa `if`, một biểu thức điều kiện cho ra `True` hoặc `False` (Chương 2), và dấu hai chấm `:`. Sau dấu hai chấm là **khối lệnh** (block), viết thụt vào so với dòng `if`.

Khác với nhiều ngôn ngữ dùng cặp ngoặc nhọn `{ }`, Python dùng **thụt lề** (indentation) để xác định lệnh nào thuộc khối nào [5]. Các lệnh cùng mức thụt lề thuộc cùng một khối. Quy ước chung là thụt 4 dấu cách cho mỗi cấp; VS Code tự chèn 4 dấu cách khi nhấn phím Tab trong file `.py`.

Lệnh `if – else` chọn một trong hai khối: khối dưới `if` chạy khi điều kiện đúng, khối dưới `else` chạy khi điều kiện sai.

**Ví dụ 3.1.** Đậu hay rớt học phần (ngưỡng 4,0 là ví dụ):

```python
diem = float(input("Điểm học phần: "))
if diem >= 4.0:
    print("Đậu")
else:
    print("Rớt, đăng ký học lại")
print("Kết thúc chương trình")
```

Dòng cuối không thụt lề nên không thuộc nhánh nào: nó luôn chạy, dù đậu hay rớt.

![Hình 3.2. Lưu đồ bài toán đậu hay rớt: một hình thoi diem >= 4.0 với hai nhánh Đúng và Sai, hai nhánh gặp lại nhau trước khi kết thúc](../Slides/images/bai-03-dau-rot.png)

Khi chỉ cần làm thêm một việc lúc điều kiện đúng, dùng `if` không có `else`:

```python
if diem >= 8:
    print("Đủ điều kiện xét học bổng")
```

### 3.2.2. Lỗi thụt lề thường gặp

| Bảng 3.2. Lỗi thường gặp với if | Nguyên nhân | Cách sửa |
|---|---|---|
| `SyntaxError: expected ':'` | Thiếu dấu `:` sau điều kiện | Thêm `:` cuối dòng `if`, `elif`, `else` |
| `IndentationError: expected an indented block` | Sau dấu `:` không có lệnh thụt vào | Thụt lề khối lệnh 4 dấu cách |
| `IndentationError: unexpected indent` | Một dòng thụt vào khi không cần | Đưa dòng đó về đúng mức |
| `SyntaxError: invalid syntax. Maybe you meant '==' ...` | Viết `=` thay cho `==` | Dùng `==` để so sánh |
| Chạy sai nhánh, không báo lỗi | Một lệnh thụt sai mức nên rơi vào khối khác | Đối chiếu với lưu đồ, sửa mức thụt lề |

Trộn lẫn ký tự Tab và dấu cách trong cùng một khối có thể gây lỗi `TabError` [5]. Khi chép mã từ nơi khác vào, dùng lệnh **Convert Indentation to Spaces** trong Command Palette của VS Code để thống nhất.

Dòng cuối của Bảng 3.2 là lỗi nguy hiểm nhất: chương trình chạy bình thường nhưng kết quả sai. Lưu đồ giúp phát hiện lỗi này, vì trên lưu đồ người học thấy rõ lệnh nào thuộc nhánh nào.

## 3.3. Rẽ nhiều nhánh với if – elif – else

### 3.3.1. Thứ tự các điều kiện

Khi có từ ba hướng xử lý trở lên, dùng `elif` (viết tắt của *else if*) [3]. Python kiểm tra các điều kiện **từ trên xuống**, gặp điều kiện đúng đầu tiên thì chạy khối của nhánh đó và **bỏ qua tất cả các nhánh còn lại**. Nhánh `else` (không bắt buộc) bắt mọi trường hợp chưa khớp nhánh nào.

**Ví dụ 3.2.** Xếp loại học lực theo thang điểm 10. Thang dưới đây là **thang ví dụ cho bài tập**, không phải quy chế đào tạo của Trường.

```python
diem = float(input("Điểm trung bình: "))
if diem >= 9:
    xep_loai = "Xuất sắc"
elif diem >= 8:
    xep_loai = "Giỏi"
elif diem >= 6.5:
    xep_loai = "Khá"
elif diem >= 5:
    xep_loai = "Trung bình"
else:
    xep_loai = "Yếu"
print(f"Xếp loại: {xep_loai}")
```

![Hình 3.3. Lưu đồ xếp loại học lực: bốn hình thoi nối tiếp nhau theo nhánh Sai, mỗi nhánh Đúng dẫn tới một kết quả xếp loại](../Slides/images/bai-03-xep-loai.png)

Vì sao thứ tự quan trọng? Giả sử đảo điều kiện `diem >= 5` lên đầu. Với điểm 9,5, điều kiện đầu tiên đã đúng nên chương trình in "Trung bình" và không bao giờ xét tới các nhánh sau. Nguyên tắc: với các ngưỡng dạng `>=`, sắp xếp **từ ngưỡng cao xuống ngưỡng thấp**.

Nhờ cơ chế "gặp nhánh đúng đầu tiên thì dừng", nhánh `elif diem >= 8` không cần viết `8 <= diem < 9`: khi chương trình xét tới nhánh này, chắc chắn `diem >= 9` đã sai.

### 3.3.2. Giá trị biên và bảng kiểm thử

Lỗi rẽ nhánh thường nằm đúng ở các ngưỡng: viết `>` thay vì `>=`, gõ nhầm 6.5 thành 6.0. Vì vậy, khi kiểm thử chương trình có rẽ nhánh, người học chọn **giá trị biên** (boundary value): giá trị nằm đúng tại ngưỡng và giá trị ngay sát dưới ngưỡng.

| Bảng 3.3. Bảng kiểm thử giá trị biên cho Ví dụ 3.2 | Mong đợi |
|---|---|
| 9 | Xuất sắc |
| 8.99 | Giỏi |
| 8 | Giỏi |
| 6.5 | Khá |
| 6.49 | Trung bình |
| 5 | Trung bình |
| 4.99 | Yếu |
| 11 | ? |

Dòng cuối cho thấy chương trình hiện xếp loại "Xuất sắc" cho điểm 11, vốn không hợp lệ. Bảng kiểm thử không chỉ xác nhận chương trình đúng mà còn giúp phát hiện **trường hợp chưa được xử lý**. Bài tập hướng dẫn cuối chương bổ sung bước kiểm tra điểm hợp lệ trước khi xếp loại.

## 3.4. Điều kiện kết hợp và rẽ nhánh lồng nhau

Một khối lệnh trong nhánh có thể chứa một lệnh `if` khác, gọi là **rẽ nhánh lồng nhau** (nested if). Dùng rẽ nhánh lồng khi điều kiện sau chỉ có nghĩa khi điều kiện trước đã đúng.

**Ví dụ 3.3.** Máy ATM đơn giản. Số dư và mã PIN cố định để thử nghiệm.

```python
so_du = 2000000
pin = input("Nhập PIN: ")
if pin == "1234":
    so_tien = int(input("Số tiền rút: "))
    if so_tien <= so_du and so_tien % 50000 == 0:
        so_du -= so_tien
        print(f"Rút thành công. Số dư còn: {so_du:,} đồng")
    else:
        print("Không rút được: vượt số dư hoặc không phải bội số 50.000")
else:
    print("Sai mã PIN")
```

Chưa đúng PIN thì không hỏi số tiền: câu hỏi số tiền nằm bên trong nhánh `pin == "1234"`. Điều kiện bên trong kết hợp hai yêu cầu bằng `and`, nên chỉ cho rút khi **cả hai** cùng đúng.

![Hình 3.4. Lưu đồ ATM đơn giản: hình thoi kiểm tra PIN; ở nhánh Đúng, nhập số tiền rồi kiểm tra đủ số dư và bội số 50.000 trước khi trừ số dư](../Slides/images/bai-03-atm.png)

Để kiểm thử Ví dụ 3.3, cần ít nhất một bộ dữ liệu đi qua mỗi nhánh của lưu đồ: PIN sai; PIN đúng và số tiền hợp lệ (500.000); PIN đúng nhưng số tiền không phải bội số 50.000 (120.000); PIN đúng nhưng vượt số dư (3.000.000).

**Ví dụ 3.4.** Không phải lúc nào cũng cần lồng. Phân loại khách hàng theo tổng chi tiêu và số năm thành viên (ngưỡng giả định) có thể viết bằng một chuỗi `if – elif – else` với điều kiện kết hợp:

```python
tong_chi = int(input("Tổng chi tiêu (đồng): "))
so_nam = int(input("Số năm thành viên: "))
if tong_chi >= 5000000 and so_nam >= 2:
    hang = "VIP"
elif tong_chi >= 2000000 or so_nam >= 3:
    hang = "Thân thiết"
else:
    hang = "Thường"
print(f"Hạng khách hàng: {hang}")
```

Với tổng chi 6.000.000 đồng và 1 năm: điều kiện thứ nhất sai (`so_nam >= 2` sai), điều kiện thứ hai đúng (`tong_chi >= 2000000`), nên khách hàng hạng "Thân thiết". Người học có thể đối chiếu bằng cách vẽ lưu đồ và tô đường đi của bộ dữ liệu này.

Khi chọn giữa lồng nhau và điều kiện kết hợp, ưu tiên cách dễ đọc hơn. Rẽ nhánh lồng nhiều cấp nhanh chóng trở nên khó đọc, nên tránh khi có thể [6]; nếu phải lồng quá ba cấp, nên xem lại thiết kế.

## 3.5. Từ lưu đồ đến mã và ngược lại

Lưu đồ và mã nguồn là hai cách biểu diễn cùng một thuật toán, nên phải **khớp nhau**. Mỗi hình thoi tương ứng một `if` hoặc `elif`; mỗi hình bình hành tương ứng một `input()` hoặc `print()`; mỗi hình chữ nhật tương ứng một phép gán hoặc phép tính.

Hai thói quen giúp phát hiện lỗi:

1. **Từ lưu đồ sang mã:** viết mã theo đúng thứ tự các khối trên lưu đồ, mỗi khối một hoặc vài dòng.
2. **Từ mã sang lưu đồ:** với mã có sẵn (do bạn khác viết, hoặc do AI gợi ý), vẽ lại lưu đồ. Nếu không vẽ được, hoặc lưu đồ có nhánh không dẫn tới kết thúc, mã đó có vấn đề.

**Ví dụ 3.5.** Dùng AI có giới hạn kiến thức. Prompt: *"Viết 1 ví dụ if – elif – else mức nhập môn về tính phí gửi xe theo số giờ. Chỉ dùng biến, input, print, if – elif – else; không dùng hàm, list hay vòng lặp."* Phần giới hạn bảo đảm lời giải nằm trong kiến thức đã học. Sau đó người học vẽ lưu đồ cho lời giải của AI, lập bảng kiểm thử giá trị biên, chạy thử và ghi vào Nhật ký Prompt những chỗ lưu đồ và mã chưa khớp.

**Mở rộng.** Python có **biểu thức điều kiện** viết trên một dòng: `ket_qua = "Đậu" if diem >= 4 else "Rớt"` [7]. Cách viết này gọn khi chỉ chọn giữa hai giá trị. Lệnh `match – case` (có từ Python 3.10) không thuộc phạm vi học phần.

## Tóm tắt chương

- Lưu đồ biểu diễn thuật toán bằng bốn ký hiệu: bắt đầu/kết thúc, nhập/xuất, xử lý, điều kiện; mỗi hình thoi có hai lối ra Đúng/Sai.
- Python dùng thụt lề (4 dấu cách) để xác định khối lệnh; thiếu `:` hoặc thụt sai gây lỗi, hoặc tệ hơn là chạy sai nhánh mà không báo lỗi.
- `if – elif – else` kiểm tra điều kiện từ trên xuống, chạy nhánh đúng đầu tiên rồi bỏ qua phần còn lại; thứ tự điều kiện quyết định kết quả.
- Kiểm thử rẽ nhánh bằng giá trị biên: tại ngưỡng và ngay sát ngưỡng, cộng thêm dữ liệu ngoài khoảng hợp lệ.
- Dùng rẽ nhánh lồng khi điều kiện sau chỉ có nghĩa khi điều kiện trước đúng; dùng `and`, `or` để kết hợp điều kiện trong một nhánh.
- Lưu đồ và mã phải khớp nhau; vẽ lại lưu đồ từ mã là cách tốt để kiểm tra mã của người khác hoặc của AI.

## Câu hỏi ôn tập

1. Nêu bốn ký hiệu lưu đồ cơ bản và lệnh Python tương ứng với mỗi ký hiệu.
2. Vì sao mỗi hình thoi trong lưu đồ phải có đúng hai lối ra?
3. Trong Ví dụ 3.1, nếu dòng `print("Kết thúc chương trình")` được thụt vào 4 dấu cách thì chương trình thay đổi thế nào?
4. Giải thích vì sao trong Ví dụ 3.2 không cần viết `elif 8 <= diem < 9`.
5. Nếu đổi thứ tự hai nhánh `diem >= 9` và `diem >= 8` trong Ví dụ 3.2, với dữ liệu nào chương trình cho kết quả sai?
6. Vì sao kiểm thử với 8,99 và 4,99 lại quan trọng hơn kiểm thử với 7 hay 3?
7. Trong Ví dụ 3.3, vì sao câu hỏi số tiền nằm bên trong nhánh kiểm tra PIN?
8. Với Ví dụ 3.4, tổng chi 1.000.000 đồng và 3 năm thành viên thì khách hàng được hạng gì? Vẽ đường đi trên lưu đồ để kiểm tra.

## Bài tập

1. **Chẵn lẻ.** Vẽ lưu đồ rồi viết chương trình nhập một số nguyên, in "chẵn" hoặc "lẻ" (dùng `n % 2 == 0`).
2. **Phương trình bậc nhất.** Nhập `a`, `b`, giải phương trình `ax + b = 0`, xét đủ ba trường hợp: có một nghiệm, vô nghiệm, vô số nghiệm. Vẽ lưu đồ trước khi viết mã.
3. **Phí gửi xe.** Gửi xe máy với phí giả định: tối đa 4 giờ thu 5.000 đồng; từ trên 4 giờ đến 12 giờ thu 10.000 đồng; trên 12 giờ thu 20.000 đồng; số giờ âm thì báo lỗi. Lập bảng kiểm thử có đủ giá trị biên.
4. **Giá vé xem phim.** Giá vé giả định phụ thuộc độ tuổi (dưới 12, từ 12 đến 60, trên 60) và ngày trong tuần (thứ Hai đến thứ Năm giảm 20%). Vẽ lưu đồ, viết mã, lập bảng kiểm thử.
5. **Kiểm tra mã của AI.** Thực hiện Ví dụ 3.5 với một bài toán tự chọn có ít nhất 3 nhánh. Nộp lưu đồ, bảng kiểm thử và Nhật ký Prompt.

## Tài liệu tham khảo

[1] *Information processing – Documentation symbols and conventions for data, program and system flowcharts, program network charts and system resources charts*, ISO 5807:1985.

[2] JGraph Ltd, “draw.io documentation,” *draw.io*. Accessed: Oct. 31, 2026. [Online]. Available: https://www.drawio.com/doc/

[3] Python Software Foundation, “More Control Flow Tools,” *The Python Tutorial*. Accessed: Oct. 31, 2026. [Online]. Available: https://docs.python.org/3/tutorial/controlflow.html

[4] Python Software Foundation, “Compound statements,” *The Python Language Reference*. Accessed: Oct. 31, 2026. [Online]. Available: https://docs.python.org/3/reference/compound_stmts.html

[5] Python Software Foundation, “Lexical analysis,” *The Python Language Reference*. Accessed: Oct. 31, 2026. [Online]. Available: https://docs.python.org/3/reference/lexical_analysis.html

[6] A. B. Downey, *Think Python: How to Think Like a Computer Scientist*, 2nd ed. Sebastopol, CA, USA: O’Reilly Media, 2015.

[7] Python Software Foundation, “Expressions,” *The Python Language Reference*. Accessed: Oct. 31, 2026. [Online]. Available: https://docs.python.org/3/reference/expressions.html
