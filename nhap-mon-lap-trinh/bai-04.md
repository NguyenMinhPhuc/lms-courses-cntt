<details open="" style="border: 1px solid #007bff; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #e7f1ff; color: #007bff; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📘 1. Tổng quan bài học</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>BÀI 04 - Vòng lặp for, chuỗi và list cơ bản (5 tiết: 1,5 LT / 3,5 TH)</strong></p>
        <p><em>Học kỳ này bạn học 8 học phần. Viết 8 lần <code>input()</code> để nhập điểm thì được, nhưng nếu là 40 học phần của cả khóa thì sao? Máy tính giỏi nhất ở việc lặp lại một thao tác hàng trăm lần mà không sai.</em></p>
        <p><strong>Mục tiêu:</strong> Giải thích được cơ chế lặp và biến đếm; sử dụng được <code>for</code> với <code>range()</code>, với chuỗi và với list; viết được các mẫu tích lũy (tổng, đếm, lớn nhất) và vòng lặp lồng nhau; lần theo được từng chu kỳ lặp bằng bảng giá trị biến.</p>
        <p><strong>Nội dung:</strong></p>
        <ul>
            <li><strong>Ý chính 1 - Vòng lặp for và range():</strong> lặp số lần biết trước; <code>range(start, stop, step)</code>; bảng giá trị biến (trace table).</li>
            <li><strong>Ý chính 2 - Mẫu tích lũy:</strong> tính tổng, đếm theo điều kiện, tìm lớn nhất/nhỏ nhất.</li>
            <li><strong>Ý chính 3 - Duyệt chuỗi và list cơ bản:</strong> <code>for ch in chuoi</code>, <code>len()</code>, chỉ số; tạo list, <code>append</code>, duyệt list, <code>sum</code>, <code>max</code>, <code>min</code>.</li>
            <li><strong>Ý chính 4 - Vòng lặp lồng nhau:</strong> vẽ hình bằng ký tự, bảng cửu chương đầy đủ.</li>
        </ul>
        <p><strong>Kết quả cần đạt:</strong> Sinh viên viết được chức năng <em>nhập điểm nhiều học phần và thống kê</em> cho Student Dashboard bằng vòng lặp và list.</p>
        <p style="margin-bottom: 0;"><strong>CLO liên quan:</strong> CLO1, CLO2.</p>
    </div>
</details>

<details style="border: 1px solid #fd7e14; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #fff5eb; color: #fd7e14; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📚 2. Học liệu chính</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.1. Vòng lặp for và range()</h3>
            <p>Lệnh <code>for</code> lặp khối lệnh thụt lề bên dưới, mỗi lần gán cho biến lặp một giá trị mới. <code>range()</code> sinh dãy số nguyên:</p>
            <ul>
                <li><code>range(5)</code> → 0, 1, 2, 3, 4 (không gồm 5).</li>
                <li><code>range(1, 11)</code> → 1 đến 10.</li>
                <li><code>range(0, 21, 5)</code> → 0, 5, 10, 15, 20 (bước 5); <code>range(10, 0, -1)</code> đếm ngược 10 đến 1.</li>
            </ul>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code># Bảng cửu chương 7
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")</code></pre>
            <p style="margin-bottom: 0;"><strong>Bảng giá trị biến (trace table):</strong> khi chưa hiểu vòng lặp đang làm gì, kẻ bảng mỗi dòng là một chu kỳ, mỗi cột là một biến. Với <code>tong = 0</code> rồi <code>for i in range(1, 6): tong += i</code>, các dòng lần lượt là <code>i = 1, tong = 1</code>; <code>i = 2, tong = 3</code>; <code>i = 3, tong = 6</code>; <code>i = 4, tong = 10</code>; <code>i = 5, tong = 15</code>.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.2. Mẫu tích lũy: tổng, đếm, lớn nhất</h3>
            <p>Ba mẫu này dùng trong hầu hết bài toán có vòng lặp. Điểm chung: <strong>khởi tạo biến trước vòng lặp</strong>, <strong>cập nhật bên trong vòng lặp</strong>, <strong>dùng kết quả sau vòng lặp</strong>.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>n = int(input("Nhập n: "))
tong = 0              # khởi tạo
dem_chia_het_3 = 0
for i in range(1, n + 1):
    tong += i         # cập nhật
    if i % 3 == 0:
        dem_chia_het_3 += 1
print(f"Tổng 1..{n} = {tong}; có {dem_chia_het_3} số chia hết cho 3")</code></pre>
            <p style="margin-bottom: 0;"><strong>⚠️ Lỗi hay gặp:</strong> đặt <code>tong = 0</code> <em>bên trong</em> vòng lặp, mỗi chu kỳ tổng bị xóa về 0; hoặc viết <code>range(1, n)</code> nên thiếu số <code>n</code>. Lập bảng giá trị biến với <code>n = 5</code> để phát hiện ngay.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.3. Duyệt chuỗi và list cơ bản</h3>
            <p><strong>Chuỗi</strong> là dãy ký tự: <code>len(s)</code> cho độ dài, <code>s[0]</code> ký tự đầu, <code>s[-1]</code> ký tự cuối. <code>for ch in s</code> lấy lần lượt từng ký tự.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>ma_sv = input("Mã số sinh viên: ")
so_chu_so = 0
for ch in ma_sv:
    if ch in "0123456789":
        so_chu_so += 1
print(f"Mã có {len(ma_sv)} ký tự, trong đó {so_chu_so} chữ số")</code></pre>
            <p><strong>List</strong> lưu nhiều giá trị trong một biến, viết trong ngoặc vuông: <code>diem = [7.5, 8.0, 9.0]</code>.</p>
            <ul style="margin-bottom: 0;">
                <li>Tạo list rỗng <code>diem = []</code>; thêm vào cuối <code>diem.append(6.5)</code>.</li>
                <li>Lấy phần tử theo chỉ số (bắt đầu từ 0): <code>diem[0]</code> → <code>7.5</code>, <code>diem[-1]</code> phần tử cuối.</li>
                <li><code>len(diem)</code> số phần tử; <code>sum(diem)</code>, <code>max(diem)</code>, <code>min(diem)</code>.</li>
                <li>Duyệt: <code>for d in diem: print(d)</code>.</li>
            </ul>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.4. Vòng lặp lồng nhau</h3>
            <p>Một vòng lặp nằm trong khối lệnh của vòng lặp khác. Vòng ngoài chạy 1 lần thì vòng trong chạy <em>trọn</em> một lượt.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>n = 4
for hang in range(1, n + 1):      # vòng ngoài: từng hàng
    for cot in range(hang):       # vòng trong: số dấu * của hàng
        print("*", end="")
    print()                       # xuống dòng sau mỗi hàng</code></pre>
            <p style="margin-bottom: 0;">Kết quả là tam giác 4 hàng: <code>*</code>, <code>**</code>, <code>***</code>, <code>****</code>. Cách ngắn hơn là <code>print("*" * hang)</code>, nhưng viết bằng hai vòng lặp giúp bạn hiểu cơ chế lồng nhau, dùng lại cho bảng cửu chương đầy đủ 2–9.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.5. Student Dashboard v4: nhập điểm và thống kê</h3>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>n = int(input("Số học phần: "))
diem_list = []
for i in range(n):
    d = float(input(f"Điểm học phần {i + 1}: "))
    diem_list.append(d)

tb = sum(diem_list) / len(diem_list)
so_rot = 0
for d in diem_list:
    if d &lt; 4.0:
        so_rot += 1
print(f"Điểm TB: {tb:.2f} | Cao nhất: {max(diem_list)} | Thấp nhất: {min(diem_list)}")
print(f"Số học phần chưa đạt: {so_rot}")</code></pre>
            <p style="margin-bottom: 0;"><strong>Thử nhập n = 0:</strong> chương trình dừng với lỗi <code>ZeroDivisionError</code> vì chia cho <code>len(diem_list) = 0</code>. Bài 06 sẽ xử lý trường hợp này. <strong>Prompt gợi ý:</strong> <em>"Giải thích từng chu kỳ của vòng lặp for trong đoạn code sau với n = 3, điểm 7, 3.5, 9. Trình bày dạng bảng giá trị biến, không viết lại code."</em></p>
        </div>

        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📄 Slide &amp; video bài giảng</p>
            <a href="{{LINK_SLIDE_BAI_04}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📄 Slide Bài 04: Vòng lặp for, chuỗi và list cơ bản</span>
            </a>
            <a class="nomediaplugin" href="{{LINK_VIDEO_BAI_04}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🎥 Video: vòng lặp for và bảng giá trị biến</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📖 Tài liệu đọc thêm (chính thức)</p>
            <a href="https://docs.python.org/3/tutorial/controlflow.html#for-statements" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 The Python Tutorial – for Statements và range()</span><br>
                <span style="color: #6c757d; font-size: 13px;">Cú pháp for, hàm range với start, stop, step.</span>
            </a>
            <a href="https://docs.python.org/3/tutorial/introduction.html#lists" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 The Python Tutorial – Lists</span><br>
                <span style="color: #6c757d; font-size: 13px;">Tạo list, chỉ số, append, len.</span>
            </a>
        </div>
    </div>
</details>

<details style="border: 1px solid #28a745; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #eafaf1; color: #28a745; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>💡 3. Hoạt động &amp; Thực hành trên lớp</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🧑‍🏫 Thực hành có hướng dẫn (1,5 tiết): 5 bài từ dễ đến khó</strong></p>
            <ol style="margin: 0; color: #495057;">
                <li>In bảng cửu chương của một số <code>k</code> nhập từ bàn phím; vẽ lưu đồ vòng lặp (khối điều kiện và mũi tên quay lại).</li>
                <li>Tính tổng các số chẵn từ 1 đến <code>n</code>; lập bảng giá trị biến với <code>n = 6</code> trước khi chạy.</li>
                <li>Đảo ngược một chuỗi bằng vòng lặp (<code>dao = ch + dao</code>), không dùng <code>[::-1]</code>.</li>
                <li>Vẽ hình vuông rỗng cạnh <code>n</code> bằng dấu <code>*</code> (chỉ có viền).</li>
                <li>Nhờ AI giải thích "chu kỳ thứ 3 đang làm gì" ở bài 2; đối chiếu với bảng của bạn.</li>
            </ol>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">✍️ Thực hành tự làm (2 tiết): Student Dashboard v4 – thống kê</strong></p>
            <p style="margin: 0 0 6px 0; color: #495057;">Thêm vào <code>ho_so.py</code>: nhập <code>n</code> học phần, mỗi học phần nhập tên và điểm (lưu vào hai list), in bảng điểm có số thứ tự, điểm trung bình, học phần điểm cao nhất (in cả tên), số học phần chưa đạt (dưới 4,0) và xếp loại theo bài 03.</p>
            <p style="margin: 0 0 8px 0; color: #495057;"><strong>Nộp:</strong> <code>ho_so.py</code>, lưu đồ phần vòng lặp, bảng giá trị biến với 3 học phần, Nhật ký Prompt. <strong>Hoàn thành khi:</strong> chạy đúng với n = 1, n = 3, n = 5; tìm đúng tên học phần điểm cao nhất.</p>
            <a href="{{LINK_NOP_BAI_04}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp bài</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">💬 Diễn đàn thảo luận</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">Đăng ảnh bảng giá trị biến của một vòng lặp bạn từng chạy sai. Lỗi nằm ở khởi tạo, ở điều kiện <code>range</code> hay ở phần cập nhật? Bạn phát hiện ra ở chu kỳ thứ mấy?</p>
            <a href="{{LINK_DIEN_DAN_BAI_04}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Tham gia diễn đàn</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">📝 Trắc nghiệm nhanh (Quiz)</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">10 câu ôn tập: <code>range()</code>, mẫu tích lũy, duyệt chuỗi, thao tác list, vòng lặp lồng nhau.</p>
            <a href="{{LINK_QUIZ_BAI_04}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Làm bài Quiz Bài 04</a>
        </div>
    </div>
</details>

<details style="border: 1px solid #6f42c1; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #f3e5f5; color: #6f42c1; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>🆘 4. Góc trợ giúp và mở rộng</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>Thiếu hoặc thừa một vòng lặp:</strong> nhớ <code>range(a, b)</code> dừng <em>trước</em> <code>b</code>. Muốn từ 1 đến n thì viết <code>range(1, n + 1)</code>.</p>
        <p><strong><code>IndexError: list index out of range</code>:</strong> chỉ số vượt quá số phần tử; list có 3 phần tử thì chỉ số hợp lệ là 0, 1, 2 (hoặc -1, -2, -3).</p>
        <p><strong><code>AttributeError: 'str' object has no attribute 'append'</code>:</strong> bạn đang gọi <code>append</code> trên chuỗi; kiểm tra đã khởi tạo bằng <code>[]</code> chứ không phải <code>""</code>.</p>
        <p><strong>Kiến thức mở rộng:</strong> <code>enumerate(diem_list, start=1)</code> cho cả số thứ tự và giá trị khi duyệt; <code>sorted(diem_list)</code> sắp xếp tăng dần.</p>
        <p style="margin-bottom: 0;"><strong>Tự đánh giá:</strong> Không chạy máy, vòng lặp <code>for i in range(2, 11, 3)</code> lặp mấy lần, <code>i</code> nhận những giá trị nào? (Đáp án: 3 lần; 2, 5, 8.)</p>
    </div>
</details>
