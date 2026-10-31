<details open="" style="border: 1px solid #007bff; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #e7f1ff; color: #007bff; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📘 1. Tổng quan bài học</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>BÀI 02 - Toán tử, biểu thức và bài toán tính toán (5 tiết: 1,5 LT / 3,5 TH)</strong></p>
        <p><em>Điểm quá trình 8, giữa kỳ 7, cuối kỳ 9. Điểm học phần của bạn là 8,0 hay 8,1? Viết sai một dấu ngoặc trong công thức là chương trình tính sai cho cả lớp mà không báo lỗi gì.</em></p>
        <p><strong>Mục tiêu:</strong> Sử dụng được các toán tử số học, so sánh, logic và gán kết hợp; xác định được thứ tự tính của một biểu thức; hiện thực được các bài toán tính toán từ bảng Input – Process – Output.</p>
        <p><strong>Nội dung:</strong></p>
        <ul>
            <li><strong>Ý chính 1 - Toán tử số học:</strong> <code>+ - * / // % **</code>; khác biệt giữa <code>/</code> và <code>//</code>; dùng <code>%</code> để lấy phần dư.</li>
            <li><strong>Ý chính 2 - Thứ tự ưu tiên và dấu ngoặc:</strong> tính một biểu thức theo từng bước, dùng ngoặc để công thức đúng và dễ đọc.</li>
            <li><strong>Ý chính 3 - So sánh, logic và gán kết hợp:</strong> <code>== != &lt; &gt; &lt;= &gt;=</code>, <code>and or not</code>, <code>+=</code>; biểu thức kiểm tra điểm hợp lệ.</li>
            <li><strong>Ý chính 4 - Làm tròn, định dạng số và sai số số thực:</strong> <code>round()</code>, f-string <code>:.2f</code>, <code>:,</code>; vì sao <code>0.1 + 0.2</code> không bằng <code>0.3</code>.</li>
        </ul>
        <p><strong>Kết quả cần đạt:</strong> Sinh viên viết được các chương trình đổi đơn vị, tính tiền điện theo bậc và thêm chức năng <em>tính điểm trung bình học phần</em> vào Student Dashboard.</p>
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
            <h3 style="margin-top: 0; color: #fd7e14;">2.1. Toán tử số học</h3>
            <table style="width: 100%; border-collapse: collapse; font-size: 14px;">
                <thead><tr style="background-color: #fff5eb;"><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Toán tử</th><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Ý nghĩa</th><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Ví dụ</th><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Kết quả</th></tr></thead>
                <tbody>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>+  -  *</code></td><td style="padding: 8px; border: 1px solid #ffd6ad;">Cộng, trừ, nhân</td><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>7 * 3</code></td><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>21</code></td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>/</code></td><td style="padding: 8px; border: 1px solid #ffd6ad;">Chia, luôn ra số thực</td><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>7 / 2</code></td><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>3.5</code></td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>//</code></td><td style="padding: 8px; border: 1px solid #ffd6ad;">Chia lấy phần nguyên</td><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>7 // 2</code></td><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>3</code></td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>%</code></td><td style="padding: 8px; border: 1px solid #ffd6ad;">Chia lấy phần dư</td><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>7 % 2</code></td><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>1</code></td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>**</code></td><td style="padding: 8px; border: 1px solid #ffd6ad;">Lũy thừa</td><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>2 ** 10</code></td><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>1024</code></td></tr>
                </tbody>
            </table>
            <p style="margin: 10px 0 6px 0;"><strong>💡 Ví dụ:</strong> đổi tổng số phút sang giờ và phút. Với 135 phút: <code>135 // 60 = 2</code> giờ, <code>135 % 60 = 15</code> phút.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>tong_phut = int(input("Số phút: "))
gio = tong_phut // 60
phut = tong_phut % 60
print(f"{tong_phut} phút = {gio} giờ {phut} phút")</code></pre>
            <p style="margin-bottom: 0;"><code>%</code> còn dùng để tách chữ số: <code>2007 % 10</code> cho chữ số hàng đơn vị <code>7</code>, <code>2007 // 10</code> bỏ chữ số đó còn <code>200</code>.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.2. Thứ tự ưu tiên và dấu ngoặc</h3>
            <p>Python tính theo thứ tự (cao đến thấp): <code>( )</code> → <code>**</code> → <code>* / // %</code> → <code>+ -</code> → so sánh → <code>not</code> → <code>and</code> → <code>or</code>. Các toán tử cùng mức tính từ trái sang phải (riêng <code>**</code> tính từ phải sang trái).</p>
            <p style="margin: 0 0 6px 0;"><strong>💡 Tính từng bước</strong> <code>2 + 3 * 4 ** 2 // 5</code>:</p>
            <ol>
                <li><code>4 ** 2 = 16</code> → <code>2 + 3 * 16 // 5</code></li>
                <li><code>*</code> và <code>//</code> cùng mức, tính trái sang phải: <code>3 * 16 = 48</code>, rồi <code>48 // 5 = 9</code></li>
                <li><code>2 + 9 = 11</code></li>
            </ol>
            <p style="margin-bottom: 0;"><strong>⚠️ Lỗi hay gặp:</strong> <code>8 + 9 / 2</code> cho <code>12.5</code>, không phải trung bình của 8 và 9. Viết đúng là <code>(8 + 9) / 2</code>. Khi không chắc thứ tự, hãy thêm ngoặc: code đúng và người đọc cũng dễ hiểu hơn.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.3. So sánh, logic và gán kết hợp</h3>
            <ul>
                <li><strong>So sánh</strong> cho kết quả <code>True</code>/<code>False</code>: <code>==</code> (bằng, hai dấu bằng), <code>!=</code> (khác), <code>&lt; &gt; &lt;= &gt;=</code>. Đừng nhầm <code>==</code> với phép gán <code>=</code>.</li>
                <li><strong>Logic:</strong> <code>a and b</code> đúng khi cả hai đúng; <code>a or b</code> đúng khi ít nhất một đúng; <code>not a</code> đảo giá trị.</li>
                <li><strong>So sánh nối:</strong> Python cho viết <code>0 &lt;= diem &lt;= 10</code>, tương đương <code>0 &lt;= diem and diem &lt;= 10</code>.</li>
                <li><strong>Gán kết hợp:</strong> <code>tong += 5</code> nghĩa là <code>tong = tong + 5</code>; tương tự <code>-=</code>, <code>*=</code>, <code>/=</code>.</li>
            </ul>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>diem = 8.5
hop_le = 0 &lt;= diem &lt;= 10           # True
du_hoc_bong = diem &gt;= 8 and hop_le  # True
print(hop_le, du_hoc_bong, not hop_le)   # True True False</code></pre>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.4. Làm tròn, định dạng số và sai số số thực</h3>
            <ul>
                <li><code>round(x, 2)</code> làm tròn đến 2 chữ số thập phân; <code>f"{x:.2f}"</code> chỉ định dạng khi in, không đổi giá trị của <code>x</code>.</li>
                <li><code>f"{tien:,}"</code> thêm dấu phẩy ngăn cách hàng nghìn: <code>315000</code> in thành <code>315,000</code>.</li>
                <li><strong>Sai số số thực:</strong> máy tính lưu số thực ở hệ nhị phân nên <code>0.1 + 0.2</code> cho <code>0.30000000000000004</code>. Vì vậy không so sánh hai số thực bằng <code>==</code>; khi in kết quả hãy định dạng với <code>:.2f</code>.</li>
            </ul>
            <p style="margin: 0 0 6px 0;"><strong>💡 Ví dụ:</strong> tiền điện theo bậc. <em>Bảng giá giả định cho bài tập (không phải giá điện thực tế):</em> 50 kWh đầu giá 2.000 đ/kWh, 50 kWh tiếp theo 2.500 đ/kWh, phần còn lại 3.000 đ/kWh. Chưa học <code>if</code> nên ta dùng <code>min()</code>, <code>max()</code> để chia số kWh vào từng bậc.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>kwh = int(input("Số kWh tiêu thụ: "))
bac1 = min(kwh, 50)                  # tối đa 50 kWh
bac2 = min(max(kwh - 50, 0), 50)     # phần từ 51 đến 100
bac3 = max(kwh - 100, 0)             # phần trên 100
tien = bac1 * 2000 + bac2 * 2500 + bac3 * 3000
print(f"Tiền điện: {tien:,} đồng")</code></pre>
            <p style="margin-bottom: 0;">Với 130 kWh: 50 × 2.000 + 50 × 2.500 + 30 × 3.000 = <strong>315,000 đồng</strong>. Hãy tự tính tay trường hợp 40 kWh và 100 kWh để kiểm tra chương trình.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.5. Student Dashboard v2: điểm trung bình học phần</h3>
            <p><strong>IPO:</strong> Input là điểm quá trình, giữa kỳ, cuối kỳ (thang 10). Process là <code>tb = qt × 0,3 + gk × 0,3 + ck × 0,4</code> và kiểm tra cả ba điểm nằm trong 0–10. Output là điểm học phần với 2 chữ số thập phân.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>qt = float(input("Điểm quá trình: "))
gk = float(input("Điểm giữa kỳ: "))
ck = float(input("Điểm cuối kỳ: "))

tb = qt * 0.3 + gk * 0.3 + ck * 0.4
hop_le = 0 &lt;= qt &lt;= 10 and 0 &lt;= gk &lt;= 10 and 0 &lt;= ck &lt;= 10

print(f"Điểm học phần: {tb:.2f}")
print(f"Dữ liệu hợp lệ: {hop_le}")</code></pre>
            <p style="margin-bottom: 0;">Nhập 8, 7, 9 cho <code>8.10</code>. Lúc này chương trình chỉ <em>báo</em> dữ liệu sai bằng <code>False</code>; bài 03 sẽ dùng <code>if</code> để xử lý từng trường hợp. <strong>Prompt gợi ý:</strong> <em>"Trình bày từng bước Python tính biểu thức <code>8 * 0.3 + 7 * 0.3 + 9 * 0.4</code>. Sau đó giải thích vì sao <code>0.1 + 0.2</code> lại cho 0.30000000000000004."</em> Chạy thử cả hai biểu thức để kiểm chứng câu trả lời của AI.</p>
        </div>

        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📄 Slide &amp; video bài giảng</p>
            <a href="{{LINK_SLIDE_BAI_02}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📄 Slide Bài 02: Toán tử, biểu thức và bài toán tính toán</span>
            </a>
            <a class="nomediaplugin" href="{{LINK_VIDEO_BAI_02}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🎥 Video: toán tử và thứ tự tính biểu thức trong Python</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📖 Tài liệu đọc thêm (chính thức)</p>
            <a href="https://docs.python.org/3/reference/expressions.html#operator-precedence" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Python Language Reference – Operator precedence</span><br>
                <span style="color: #6c757d; font-size: 13px;">Bảng đầy đủ thứ tự ưu tiên của các toán tử.</span>
            </a>
            <a href="https://docs.python.org/3/tutorial/floatingpoint.html" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 The Python Tutorial – Floating-Point Arithmetic: Issues and Limitations</span><br>
                <span style="color: #6c757d; font-size: 13px;">Vì sao số thực có sai số và cách xử lý.</span>
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
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🧑‍🏫 Thực hành có hướng dẫn (1,5 tiết): tính tay rồi kiểm tra</strong></p>
            <ol style="margin: 0; color: #495057;">
                <li>Tự tính trên giấy 5 biểu thức giảng viên đưa ra (có <code>//</code>, <code>%</code>, <code>**</code>, ngoặc), sau đó kiểm tra bằng chế độ tương tác.</li>
                <li>Hỏi AI trình bày từng bước một biểu thức bạn tính sai; đối chiếu với bảng thứ tự ưu tiên ở mục 2.2.</li>
                <li>Viết bảng IPO rồi gõ chương trình đổi phút (mục 2.1) và tiền điện (mục 2.4); chạy thử với 40, 100, 130 kWh.</li>
            </ol>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">✍️ Thực hành tự làm (2 tiết): ba bài toán tính toán</strong></p>
            <ol style="margin: 0 0 6px 0; color: #495057;">
                <li><strong>Student Dashboard v2:</strong> thêm phần tính điểm học phần (mục 2.5) vào <code>ho_so.py</code>, in cùng thẻ hồ sơ.</li>
                <li><strong>Đổi đơn vị:</strong> nhập nhiệt độ °C, in ra °F (<code>F = C × 9/5 + 32</code>) với 1 chữ số thập phân.</li>
                <li><strong>Tách chữ số:</strong> nhập một số nguyên có 3 chữ số, in tổng các chữ số (ví dụ 527 → 14) chỉ bằng <code>//</code> và <code>%</code>.</li>
            </ol>
            <p style="margin: 0 0 8px 0; color: #495057;"><strong>Nộp:</strong> 3 file <code>.py</code>, bảng IPO cho từng bài, Nhật ký Prompt. <strong>Hoàn thành khi:</strong> mỗi bài chạy đúng với ít nhất 3 bộ dữ liệu bạn tự tính tay trước.</p>
            <a href="{{LINK_NOP_BAI_02}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp bài</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">💬 Diễn đàn thảo luận</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">Đăng một biểu thức bạn đoán sai kết quả trong buổi học. Bạn đã hiểu sai ở bước nào (thứ tự ưu tiên, <code>/</code> và <code>//</code>, hay sai số số thực)?</p>
            <a href="{{LINK_DIEN_DAN_BAI_02}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Tham gia diễn đàn</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">📝 Trắc nghiệm nhanh (Quiz)</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">10 câu ôn tập: toán tử số học, thứ tự ưu tiên, so sánh và logic, làm tròn và định dạng số.</p>
            <a href="{{LINK_QUIZ_BAI_02}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Làm bài Quiz Bài 02</a>
        </div>
    </div>
</details>

<details style="border: 1px solid #6f42c1; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #f3e5f5; color: #6f42c1; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>🆘 4. Góc trợ giúp và mở rộng</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>Nhập <code>8,5</code> bị lỗi <code>ValueError</code>:</strong> Python dùng dấu chấm cho số thập phân, hãy nhập <code>8.5</code>. Bài 06 sẽ học cách bắt lỗi này để chương trình không bị dừng.</p>
        <p><strong>Kết quả có rất nhiều chữ số lẻ (ví dụ 0.30000000000000004):</strong> đây là sai số số thực, không phải lỗi của bạn. In bằng <code>{x:.2f}</code>.</p>
        <p><strong>Muốn in tiền theo kiểu Việt Nam (315.000):</strong> dùng <code>f"{tien:,}".replace(",", ".")</code>.</p>
        <p><strong>Kiến thức mở rộng:</strong> Tìm hiểu module <code>math</code> (<code>math.sqrt</code>, <code>math.ceil</code>, <code>math.floor</code>) và kiểu <code>decimal.Decimal</code> dùng khi cần tính tiền chính xác tuyệt đối.</p>
        <p style="margin-bottom: 0;"><strong>Tự đánh giá:</strong> Không chạy máy, bạn có tính đúng <code>17 // 5 * 2 + 17 % 5 ** 2</code> không? (Đáp án: 23.)</p>
    </div>
</details>
