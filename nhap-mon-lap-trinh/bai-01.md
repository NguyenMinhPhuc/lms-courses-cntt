<details open="" style="border: 1px solid #007bff; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #e7f1ff; color: #007bff; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📘 1. Tổng quan bài học</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>BÀI 01 - Làm quen Python và tư duy Input – Process – Output (5 tiết: 1,5 LT / 3,5 TH)</strong></p>
        <p><em>Phòng Đào tạo cần in 3.000 thẻ hồ sơ tân sinh viên, mỗi thẻ gồm họ tên, lớp và tuổi. Làm tay mất cả tuần. Một chương trình 10 dòng làm xong trong vài giây, nhưng chỉ khi người viết biết rõ chương trình nhận vào gì, xử lý gì và in ra gì.</em></p>
        <p><strong>Mục tiêu:</strong> Cài đặt được Python 3 và VS Code, chạy được chương trình đầu tiên; phân tích được một bài toán thành Input – Process – Output; khai báo được biến với các kiểu <code>int</code>, <code>float</code>, <code>str</code>, <code>bool</code> và nhập, xuất dữ liệu bằng <code>input()</code>, <code>print()</code>, f-string.</p>
        <p><strong>Nội dung:</strong></p>
        <ul>
            <li><strong>Ý chính 1 - Chương trình và Python:</strong> máy tính chỉ làm đúng các lệnh được viết; Python là ngôn ngữ thông dịch, dễ đọc; cài đặt môi trường và chạy <code>print("Hello, LHU!")</code>.</li>
            <li><strong>Ý chính 2 - Tư duy Input – Process – Output (IPO):</strong> xác định đầu vào, xử lý, đầu ra trước khi viết code.</li>
            <li><strong>Ý chính 3 - Biến và kiểu dữ liệu cơ bản:</strong> đặt tên biến, bốn kiểu <code>int</code>, <code>float</code>, <code>str</code>, <code>bool</code>, hàm <code>type()</code> và chuyển kiểu.</li>
            <li><strong>Ý chính 4 - Nhập, xuất và f-string:</strong> <code>input()</code> luôn trả về chuỗi; in kết quả gọn gàng bằng f-string; dùng AI giải thích cú pháp và ghi Nhật ký Prompt.</li>
        </ul>
        <p><strong>Kết quả cần đạt:</strong> Sinh viên chạy được chương trình <code>ho_so.py</code> (phiên bản đầu tiên của <em>Student Dashboard</em>) in thẻ hồ sơ từ dữ liệu nhập vào, kèm bảng IPO và Nhật ký Prompt.</p>
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
            <h3 style="margin-top: 0; color: #fd7e14;">2.1. Chương trình, Python và cài đặt môi trường</h3>
            <p><strong>Chương trình</strong> là dãy lệnh viết bằng một ngôn ngữ lập trình để máy tính thực hiện theo đúng thứ tự. Máy tính không đoán ý: viết thiếu một dấu ngoặc là chương trình báo lỗi.</p>
            <p><strong>Python</strong> là ngôn ngữ <strong>thông dịch</strong> (interpreted): trình thông dịch đọc file <code>.py</code> và chạy từng lệnh, không cần bước biên dịch riêng. Cú pháp gần với tiếng Anh nên phù hợp người mới học; Python cũng được dùng nhiều trong khoa học dữ liệu, AI và tự động hóa.</p>
            <p style="margin: 0 0 6px 0;"><strong>Cài đặt (làm trước buổi học):</strong></p>
            <ol>
                <li>Tải Python 3.10 trở lên tại <strong>python.org/downloads</strong>. Trên Windows, ở màn hình đầu tiên của bộ cài, <strong>tick ô "Add python.exe to PATH"</strong> rồi bấm Install Now.</li>
                <li>Cài <strong>Visual Studio Code</strong> (code.visualstudio.com), mở mục Extensions và cài extension <strong>Python</strong> của Microsoft.</li>
                <li>Mở Terminal trong VS Code (<code>Ctrl + `</code>), gõ <code>python --version</code> (Windows có thể dùng <code>py --version</code>). Thấy <code>Python 3.1x.x</code> là cài đúng.</li>
                <li>Tạo file <code>hello.py</code>, gõ dòng dưới đây và bấm nút ▶ (Run Python File).</li>
            </ol>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>print("Hello, LHU!")</code></pre>
            <p style="margin-bottom: 0;"><strong>💡 Hai cách chạy Python:</strong> chạy cả file (<code>python hello.py</code>) hoặc gõ <code>python</code> để vào <strong>chế độ tương tác</strong> (dấu nhắc <code>&gt;&gt;&gt;</code>), gõ lệnh nào chạy ngay lệnh đó. Chế độ tương tác rất tiện để thử nhanh một phép tính; gõ <code>exit()</code> để thoát.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.2. Tư duy Input – Process – Output</h3>
            <p>Trước khi mở VS Code, hãy trả lời ba câu hỏi. Đây là thói quen quan trọng nhất của học phần.</p>
            <ul>
                <li><strong>Input (đầu vào):</strong> chương trình cần nhận những dữ liệu nào? Ai cung cấp?</li>
                <li><strong>Process (xử lý):</strong> cần tính toán, so sánh, biến đổi gì từ đầu vào?</li>
                <li><strong>Output (đầu ra):</strong> chương trình in ra gì, theo dạng nào?</li>
            </ul>
            <p style="margin: 0 0 6px 0;"><strong>💡 Ví dụ:</strong> bài toán "in thẻ hồ sơ tân sinh viên".</p>
            <table style="width: 100%; border-collapse: collapse; font-size: 14px;">
                <thead><tr style="background-color: #fff5eb;"><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Input</th><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Process</th><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Output</th></tr></thead>
                <tbody>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;">Họ tên, năm sinh, lớp (người dùng nhập từ bàn phím)</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Tuổi = năm hiện tại − năm sinh</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Thẻ hồ sơ có khung, gồm họ tên, lớp, tuổi</td></tr>
                </tbody>
            </table>
            <p style="margin-bottom: 0;">Viết bảng IPO giúp bạn phát hiện thiếu dữ liệu ngay từ đầu (ví dụ: muốn in tuổi thì phải hỏi năm sinh) và cho AI một mô tả rõ ràng khi cần hỏi.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.3. Biến và kiểu dữ liệu cơ bản</h3>
            <p><strong>Biến</strong> là một cái tên gắn với một giá trị trong bộ nhớ. Dấu <code>=</code> là phép <strong>gán</strong>: lấy giá trị bên phải gắn cho tên bên trái.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>ho_ten = "Nguyễn Văn An"     # str: chuỗi ký tự, đặt trong ngoặc kép
nam_sinh = 2007              # int: số nguyên
diem_tb = 8.25               # float: số thực, dùng dấu chấm
la_tan_sinh_vien = True      # bool: chỉ có True hoặc False

print(type(nam_sinh))        # &lt;class 'int'&gt;
print(type(diem_tb))         # &lt;class 'float'&gt;</code></pre>
            <ul>
                <li><strong>Quy tắc đặt tên:</strong> chỉ gồm chữ cái, chữ số, dấu gạch dưới; không bắt đầu bằng chữ số; phân biệt hoa thường (<code>diem</code> khác <code>Diem</code>); không trùng từ khóa như <code>if</code>, <code>for</code>.</li>
                <li><strong>Thói quen tốt:</strong> tên có nghĩa, viết thường, nối bằng gạch dưới (<code>nam_sinh</code>, không phải <code>ns</code> hay <code>x1</code>). Đây là kiểu <code>snake_case</code> sẽ học kỹ ở buổi 09.</li>
                <li><strong>Chuyển kiểu:</strong> <code>int("2007")</code> → <code>2007</code>; <code>float("8.5")</code> → <code>8.5</code>; <code>str(19)</code> → <code>"19"</code>.</li>
            </ul>
            <p style="margin-bottom: 0;"><strong>⚠️ Chú ý:</strong> <code>"2007"</code> (có ngoặc kép) là chuỗi, không phải số. <code>"2007" + 1</code> gây lỗi <code>TypeError</code> vì Python không cộng chuỗi với số.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.4. Nhập, xuất và f-string</h3>
            <ul>
                <li><code>input("Lời nhắc: ")</code> dừng chương trình chờ người dùng gõ và nhấn Enter. Kết quả <strong>luôn là chuỗi</strong>, muốn tính toán phải chuyển kiểu: <code>int(input(...))</code>.</li>
                <li><code>print(a, b)</code> in các giá trị cách nhau một khoảng trắng; <code>sep="-"</code> đổi ký tự ngăn cách, <code>end=""</code> để không xuống dòng.</li>
                <li><strong>f-string:</strong> đặt chữ <code>f</code> trước chuỗi, giá trị biến nằm trong <code>{ }</code>: <code>f"{ho_ten} - {tuoi} tuổi"</code>.</li>
            </ul>
            <p style="margin: 0 0 6px 0;"><strong>💡 Ví dụ:</strong> thẻ hồ sơ số hóa cá nhân, phiên bản 1 của <em>Student Dashboard</em>.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code># ho_so.py - Student Dashboard v1: in thẻ hồ sơ
ho_ten = input("Họ tên: ")
nam_sinh = int(input("Năm sinh: "))
lop = input("Lớp: ")

tuoi = 2026 - nam_sinh

print("=" * 36)
print(f"  HỒ SƠ SỐ HÓA: {ho_ten}")
print(f"  Lớp: {lop}  |  Tuổi: {tuoi}")
print("=" * 36)</code></pre>
            <p style="margin-bottom: 0;">Nhập <em>Nguyễn Văn An</em>, <em>2007</em>, <em>26CT111</em> sẽ in ra khung có dòng <code>Lớp: 26CT111  |  Tuổi: 19</code>. Biểu thức <code>"=" * 36</code> lặp chuỗi <code>"="</code> 36 lần để vẽ khung.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.5. Dùng AI đúng cách và Nhật ký Prompt</h3>
            <p>Trong học phần này, AI là <strong>trợ giảng</strong>: giải thích, gợi ý, tìm lỗi. Bạn là người viết code. Một prompt tốt cho người mới học có ba phần: <strong>bối cảnh</strong>, <strong>câu hỏi cụ thể</strong>, <strong>giới hạn</strong>.</p>
            <p style="margin: 0 0 6px 0;"><strong>💡 Prompt mẫu:</strong></p>
            <p style="margin: 0 0 8px 0; padding: 8px 10px; background-color: #fff; border-left: 4px solid #fd7e14;"><em>"Tôi là sinh viên năm nhất mới học Python buổi đầu. Giải thích dòng <code>print(f"Tuổi: {tuoi}")</code> làm gì, chữ f và dấu ngoặc nhọn có ý nghĩa gì. Đừng viết thêm code mới, chỉ giải thích."</em></p>
            <p style="margin: 0 0 6px 0;"><strong>Nhật ký Prompt</strong> (file <code>nhat-ky-prompt.md</code>, ghi cho mọi bài lab) gồm các cột:</p>
            <table style="width: 100%; border-collapse: collapse; font-size: 14px;">
                <thead><tr style="background-color: #fff5eb;"><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Prompt đã dùng</th><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">AI trả lời (tóm tắt)</th><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Mình kiểm tra / sửa gì</th><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Bài học rút ra</th></tr></thead>
                <tbody>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;">Prompt mẫu ở trên</td><td style="padding: 8px; border: 1px solid #ffd6ad;">f-string chèn giá trị biến vào chuỗi</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Tự viết lại dòng in lớp và tuổi, chạy thử đúng</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Thiếu chữ f thì in nguyên chữ <code>{tuoi}</code></td></tr>
                </tbody>
            </table>
        </div>

        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📄 Slide &amp; video bài giảng</p>
            <a href="{{LINK_SLIDE_BAI_01}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📄 Slide Bài 01: Làm quen Python và tư duy Input – Process – Output</span>
            </a>
            <a class="nomediaplugin" href="{{LINK_VIDEO_BAI_01}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🎥 Video: cài đặt Python, VS Code và chạy chương trình đầu tiên</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📖 Tài liệu đọc thêm (chính thức)</p>
            <a href="https://code.visualstudio.com/docs/python/python-tutorial" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Getting Started with Python in VS Code</span><br>
                <span style="color: #6c757d; font-size: 13px;">Cài extension Python, chọn trình thông dịch, chạy file.</span>
            </a>
            <a href="https://docs.python.org/3/tutorial/introduction.html" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 The Python Tutorial – An Informal Introduction to Python</span><br>
                <span style="color: #6c757d; font-size: 13px;">Số, chuỗi và cách dùng chế độ tương tác.</span>
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
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🧑‍🏫 Thực hành có hướng dẫn (1,5 tiết): môi trường và chương trình đầu tiên</strong></p>
            <ol style="margin: 0; color: #495057;">
                <li>Kiểm tra cài đặt theo mục 2.1; tạo thư mục <code>nhap-mon-lap-trinh/buoi-01</code> và mở bằng VS Code.</li>
                <li>Chạy <code>hello.py</code>; thử chế độ tương tác: tính <code>2026 - 2007</code>, <code>type(8.25)</code>, <code>"Ha" * 3</code>.</li>
                <li>Cố ý gõ sai: bỏ dấu ngoặc kép, viết <code>Print</code> thay cho <code>print</code>. Đọc thông báo lỗi và ghi lại.</li>
                <li>Gõ lại chương trình <code>ho_so.py</code> ở mục 2.4 (gõ tay, không sao chép) và chạy thử với dữ liệu của chính bạn.</li>
            </ol>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">✍️ Thực hành tự làm (2 tiết): Student Dashboard v1</strong></p>
            <p style="margin: 0 0 6px 0; color: #495057;">Mở rộng <code>ho_so.py</code>: nhập thêm mã số sinh viên, quê quán, chiều cao (mét, kiểu <code>float</code>) và cho biết có ở ký túc xá không (nhập <code>c</code>/<code>k</code>, lưu thành <code>True</code>/<code>False</code> bằng biểu thức <code>tra_loi == "c"</code>). In thẻ hồ sơ có khung, mỗi thông tin một dòng.</p>
            <p style="margin: 0 0 8px 0; color: #495057;"><strong>Nộp:</strong> file <code>ho_so.py</code>, bảng IPO của bài toán, <code>nhat-ky-prompt.md</code> (2–3 prompt). <strong>Hoàn thành khi:</strong> chạy được với 2 bộ dữ liệu khác nhau; bạn giải thích được vì sao phải dùng <code>int()</code> và <code>float()</code>.</p>
            <a href="{{LINK_NOP_BAI_01}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp bài</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">💬 Diễn đàn thảo luận</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">Chọn một ứng dụng bạn dùng hằng ngày (ví dụ ví điện tử, ứng dụng đặt xe). Viết bảng Input – Process – Output cho <strong>một</strong> chức năng của nó. Nhận xét bảng của một bạn khác: còn thiếu đầu vào nào không?</p>
            <a href="{{LINK_DIEN_DAN_BAI_01}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Tham gia diễn đàn</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">📝 Trắc nghiệm nhanh (Quiz)</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">10 câu ôn tập: cách chạy Python, bảng IPO, biến và kiểu dữ liệu, <code>input()</code>, f-string.</p>
            <a href="{{LINK_QUIZ_BAI_01}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Làm bài Quiz Bài 01</a>
        </div>
    </div>
</details>

<details style="border: 1px solid #6f42c1; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #f3e5f5; color: #6f42c1; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>🆘 4. Góc trợ giúp và mở rộng</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>Gõ <code>python</code> mà báo "not recognized" hoặc mở Microsoft Store:</strong> lúc cài chưa tick "Add python.exe to PATH". Thử lệnh <code>py</code>, hoặc chạy lại bộ cài, chọn Modify và bật tùy chọn thêm vào PATH. Trong Windows Settings, mục <em>App execution aliases</em>, tắt hai mục <code>python.exe</code> của App Installer.</p>
        <p><strong>Nút ▶ không chạy hoặc báo thiếu trình thông dịch:</strong> nhấn <code>Ctrl + Shift + P</code>, chọn <em>Python: Select Interpreter</em> và chọn bản Python vừa cài.</p>
        <p><strong><code>SyntaxError: unterminated string literal</code>:</strong> thiếu dấu ngoặc kép đóng chuỗi. <strong><code>TypeError: can only concatenate str (not "int") to str</code>:</strong> đang cộng chuỗi với số, kiểm tra đã dùng <code>int()</code> sau <code>input()</code> chưa.</p>
        <p><strong>Kiến thức mở rộng:</strong> Thử hàm <code>help(print)</code> trong chế độ tương tác để đọc tài liệu của một hàm; tìm hiểu cách định dạng số trong f-string như <code>{chieu_cao:.2f}</code> (sẽ dùng ở bài 02).</p>
        <p style="margin-bottom: 0;"><strong>Tự đánh giá:</strong> Không nhìn bài, bạn có tự viết lại được bảng IPO và chương trình in thẻ hồ sơ trong 10 phút không?</p>
    </div>
</details>
