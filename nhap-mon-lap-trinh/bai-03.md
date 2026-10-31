<details open="" style="border: 1px solid #007bff; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #e7f1ff; color: #007bff; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📘 1. Tổng quan bài học</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>BÀI 03 - Cấu trúc rẽ nhánh if – elif – else và lưu đồ thuật toán (5 tiết: 1,5 LT / 3,5 TH)</strong></p>
        <p><em>Máy ATM chỉ cho rút tiền khi mã PIN đúng, số dư đủ và số tiền là bội số của 50.000. Thiếu một điều kiện, hoặc kiểm tra sai thứ tự, ngân hàng sẽ mất tiền. Làm sao mô tả các lựa chọn này cho rõ trước khi viết code?</em></p>
        <p><strong>Mục tiêu:</strong> Biểu diễn được thuật toán có rẽ nhánh bằng lưu đồ đúng ký hiệu; viết được các lệnh <code>if</code>, <code>if-else</code>, <code>if-elif-else</code>, rẽ nhánh lồng nhau với điều kiện kết hợp; kiểm thử được chương trình bằng các giá trị biên.</p>
        <p><strong>Nội dung:</strong></p>
        <ul>
            <li><strong>Ý chính 1 - Lưu đồ thuật toán:</strong> bốn ký hiệu cơ bản và cách vẽ trên Draw.io.</li>
            <li><strong>Ý chính 2 - <code>if</code>, <code>if-else</code> và thụt lề:</strong> khối lệnh trong Python được xác định bằng thụt lề.</li>
            <li><strong>Ý chính 3 - <code>if-elif-else</code> nhiều nhánh:</strong> thứ tự điều kiện quyết định kết quả; kiểm thử giá trị biên.</li>
            <li><strong>Ý chính 4 - Điều kiện kết hợp và rẽ nhánh lồng:</strong> ATM đơn giản, phân loại khách hàng; dùng AI có giới hạn kiến thức.</li>
        </ul>
        <p><strong>Kết quả cần đạt:</strong> Sinh viên vẽ được lưu đồ và viết được chức năng <em>xếp loại học lực</em> cho Student Dashboard, chạy đúng với mọi giá trị biên.</p>
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
            <h3 style="margin-top: 0; color: #fd7e14;">2.1. Lưu đồ thuật toán (Flowchart)</h3>
            <p><strong>Lưu đồ</strong> mô tả thuật toán bằng hình vẽ: mỗi bước là một khối, mũi tên chỉ thứ tự thực hiện. Lưu đồ giúp bạn thấy hết các nhánh trước khi code và là minh chứng cho CLO2.</p>
            <table style="width: 100%; border-collapse: collapse; font-size: 14px;">
                <thead><tr style="background-color: #fff5eb;"><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Ký hiệu</th><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Hình dạng</th><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Dùng cho</th></tr></thead>
                <tbody>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;">Bắt đầu / Kết thúc</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Hình chữ nhật bo tròn hai đầu</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Điểm vào và điểm ra của thuật toán</td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;">Nhập / Xuất</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Hình bình hành</td><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>input()</code>, <code>print()</code></td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;">Xử lý</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Hình chữ nhật</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Phép gán, tính toán</td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;">Điều kiện</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Hình thoi, hai lối ra Đúng / Sai</td><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>if</code>, điều kiện của vòng lặp</td></tr>
                </tbody>
            </table>
            <p style="margin-bottom: 0;"><strong>Vẽ trên Draw.io:</strong> mở app.diagrams.net (hoặc extension Draw.io Integration trong VS Code, tạo file <code>.drawio</code>), dùng nhóm hình <em>Flowchart</em> ở thanh bên trái; ghi chữ <em>Đúng</em>/<em>Sai</em> trên mũi tên ra khỏi hình thoi; xuất ảnh bằng <em>File → Export as → PNG</em>.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.2. Lệnh if, if-else và thụt lề</h3>
            <p>Sau dấu hai chấm <code>:</code> là <strong>khối lệnh</strong>, viết thụt vào 4 dấu cách. Python dựa vào thụt lề để biết lệnh nào thuộc nhánh nào; thụt sai sẽ báo <code>IndentationError</code> hoặc chạy sai nhánh.</p>
            <p style="margin: 0 0 6px 0;"><strong>💡 Ví dụ:</strong> đậu hay rớt học phần (<em>ngưỡng 4,0 dùng làm ví dụ</em>).</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>diem = float(input("Điểm học phần: "))

if diem &gt;= 4.0:
    print("Đậu")
else:
    print("Rớt, đăng ký học lại")
print("Kết thúc chương trình")   # không thụt lề: luôn chạy</code></pre>
            <p style="margin-bottom: 0;">Chỉ cần làm thêm việc khi điều kiện đúng thì dùng <code>if</code> không có <code>else</code>, ví dụ: <code>if diem &gt;= 8: print("Đủ điều kiện xét học bổng")</code>.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.3. if-elif-else nhiều nhánh và giá trị biên</h3>
            <p>Python kiểm tra các điều kiện <strong>từ trên xuống</strong>, gặp điều kiện đúng đầu tiên thì chạy nhánh đó và bỏ qua phần còn lại. <code>else</code> bắt mọi trường hợp còn lại.</p>
            <p style="margin: 0 0 6px 0;"><strong>💡 Ví dụ:</strong> xếp loại theo thang 10. <em>Thang dưới đây là thang ví dụ cho bài tập, không phải quy chế của Trường.</em></p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>diem = float(input("Điểm trung bình: "))

if diem &gt;= 9:
    xep_loai = "Xuất sắc"
elif diem &gt;= 8:
    xep_loai = "Giỏi"
elif diem &gt;= 6.5:
    xep_loai = "Khá"
elif diem &gt;= 5:
    xep_loai = "Trung bình"
else:
    xep_loai = "Yếu"
print(f"Xếp loại: {xep_loai}")</code></pre>
            <ul style="margin-bottom: 0;">
                <li><strong>Vì sao thứ tự quan trọng:</strong> nếu viết <code>if diem &gt;= 5</code> lên đầu, điểm 9,5 cũng rơi vào "Trung bình" vì điều kiện đầu đã đúng.</li>
                <li><strong>Kiểm thử giá trị biên:</strong> chạy với 9; 8,99; 8; 6,5; 6,49; 5; 4,99 và một điểm ngoài khoảng (11). Lỗi rẽ nhánh thường nằm đúng ở các ngưỡng này.</li>
            </ul>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.4. Điều kiện kết hợp và rẽ nhánh lồng nhau</h3>
            <p>Một nhánh có thể chứa một <code>if</code> khác (rẽ nhánh lồng). Dùng lồng khi điều kiện sau chỉ có nghĩa khi điều kiện trước đã đúng: chưa đúng PIN thì không hỏi số tiền.</p>
            <p style="margin: 0 0 6px 0;"><strong>💡 Ví dụ:</strong> ATM đơn giản (số dư và PIN cố định để thử nghiệm).</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>so_du = 2000000
pin = input("Nhập PIN: ")

if pin == "1234":
    so_tien = int(input("Số tiền rút: "))
    if so_tien &lt;= so_du and so_tien % 50000 == 0:
        so_du -= so_tien
        print(f"Rút thành công. Số dư còn: {so_du:,} đồng")
    else:
        print("Không rút được: vượt số dư hoặc không phải bội số 50.000")
else:
    print("Sai mã PIN")</code></pre>
            <p style="margin: 8px 0 6px 0;"><strong>Phân loại khách hàng</strong> dùng <code>and</code>, <code>or</code> trong một chuỗi <code>if-elif-else</code>:</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>if tong_chi &gt;= 5000000 and so_nam &gt;= 2:
    hang = "VIP"
elif tong_chi &gt;= 2000000 or so_nam &gt;= 3:
    hang = "Thân thiết"
else:
    hang = "Thường"</code></pre>
            <p style="margin-bottom: 0;"><strong>Dùng AI có giới hạn:</strong> <em>"Viết 1 ví dụ if-elif-else mức nhập môn về tính phí gửi xe theo số giờ. Chỉ dùng biến, input, print, if-elif-else; không dùng hàm, list hay vòng lặp."</em> Vẽ lưu đồ cho lời giải của AI; nếu lưu đồ và code không khớp, tìm xem chỗ nào sai.</p>
        </div>

        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📄 Slide &amp; video bài giảng</p>
            <a href="{{LINK_SLIDE_BAI_03}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📄 Slide Bài 03: Cấu trúc rẽ nhánh và lưu đồ thuật toán</span>
            </a>
            <a class="nomediaplugin" href="{{LINK_VIDEO_BAI_03}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🎥 Video: vẽ lưu đồ trên Draw.io và viết if-elif-else</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📖 Tài liệu đọc thêm (chính thức)</p>
            <a href="https://docs.python.org/3/tutorial/controlflow.html#if-statements" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 The Python Tutorial – if Statements</span><br>
                <span style="color: #6c757d; font-size: 13px;">Cú pháp if, elif, else.</span>
            </a>
            <a href="https://www.drawio.com/doc/" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 draw.io Documentation</span><br>
                <span style="color: #6c757d; font-size: 13px;">Hướng dẫn vẽ sơ đồ, nối mũi tên và xuất ảnh.</span>
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
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🧑‍🏫 Thực hành có hướng dẫn (1,5 tiết): lưu đồ trước, code sau</strong></p>
            <ol style="margin: 0; color: #495057;">
                <li>Vẽ trên Draw.io lưu đồ kiểm tra số chẵn lẻ (dùng <code>n % 2 == 0</code>), rồi viết code theo lưu đồ.</li>
                <li>Vẽ lưu đồ ATM ở mục 2.4; đánh dấu trên lưu đồ ba bộ dữ liệu sẽ đi qua ba nhánh khác nhau, chạy code để kiểm chứng.</li>
                <li>Cố ý đảo thứ tự điều kiện trong ví dụ xếp loại, chạy với điểm 9,5 và giải thích kết quả sai.</li>
            </ol>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">✍️ Thực hành tự làm (2 tiết): Student Dashboard v3 – xếp loại</strong></p>
            <ol style="margin: 0 0 6px 0; color: #495057;">
                <li>Sau khi tính điểm học phần (bài 02): nếu có điểm ngoài khoảng 0–10 thì in thông báo lỗi; ngược lại in điểm, kết quả đậu/rớt và xếp loại.</li>
                <li>Vẽ lưu đồ cho toàn bộ phần xử lý này trên Draw.io.</li>
                <li>Lập bảng kiểm thử gồm ít nhất 7 dòng (dữ liệu nhập, kết quả mong đợi, kết quả thực tế), có đủ các giá trị biên.</li>
            </ol>
            <p style="margin: 0 0 8px 0; color: #495057;"><strong>Nộp:</strong> <code>ho_so.py</code>, file lưu đồ (<code>.drawio</code> và <code>.png</code>), bảng kiểm thử, Nhật ký Prompt. <strong>Hoàn thành khi:</strong> mọi dòng trong bảng kiểm thử đúng; lưu đồ khớp với code.</p>
            <a href="{{LINK_NOP_BAI_03}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp bài</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">💬 Diễn đàn thảo luận</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">Đăng lưu đồ (ảnh) một quy tắc bạn gặp ngoài đời có từ 3 nhánh trở lên, ví dụ giá vé xem phim theo độ tuổi và ngày trong tuần. Nhận xét lưu đồ của một bạn: có trường hợp nào chưa được xử lý?</p>
            <a href="{{LINK_DIEN_DAN_BAI_03}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Tham gia diễn đàn</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">📝 Trắc nghiệm nhanh (Quiz)</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">10 câu ôn tập: ký hiệu lưu đồ, thụt lề, thứ tự điều kiện trong <code>if-elif-else</code>, điều kiện kết hợp và rẽ nhánh lồng.</p>
            <a href="{{LINK_QUIZ_BAI_03}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Làm bài Quiz Bài 03</a>
        </div>
    </div>
</details>

<details style="border: 1px solid #6f42c1; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #f3e5f5; color: #6f42c1; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>🆘 4. Góc trợ giúp và mở rộng</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong><code>IndentationError: expected an indented block</code>:</strong> sau dấu <code>:</code> chưa có lệnh thụt vào. <strong><code>SyntaxError: invalid syntax</code> ở dòng <code>if</code>:</strong> thường do thiếu dấu <code>:</code> hoặc viết <code>=</code> thay cho <code>==</code>.</p>
        <p><strong>Trộn Tab và dấu cách:</strong> VS Code mặc định đổi Tab thành 4 dấu cách; nếu copy code từ nơi khác, chọn <em>Convert Indentation to Spaces</em> trong Command Palette.</p>
        <p><strong>So sánh chuỗi phân biệt hoa thường:</strong> <code>"C" == "c"</code> là <code>False</code>. Khi hỏi người dùng có/không, dùng <code>tra_loi.lower() == "c"</code>.</p>
        <p><strong>Kiến thức mở rộng:</strong> Biểu thức điều kiện một dòng <code>ket_qua = "Đậu" if diem &gt;= 4 else "Rớt"</code>; lệnh <code>match-case</code> (Python 3.10) không thuộc phạm vi học phần nhưng bạn có thể tự tìm hiểu.</p>
        <p style="margin-bottom: 0;"><strong>Tự đánh giá:</strong> Với ví dụ phân loại khách hàng, tổng chi 6.000.000 đồng và 1 năm thành viên thì được hạng gì? Vẽ đường đi trên lưu đồ để kiểm tra câu trả lời.</p>
    </div>
</details>
