<details open="" style="border: 1px solid #007bff; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #e7f1ff; color: #007bff; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📘 1. Tổng quan bài học</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>BÀI 06 - Xử lý ngoại lệ try – except và debugging (5 tiết: 1,5 LT / 3,5 TH)</strong></p>
        <p><em>Bạn đưa Student Dashboard cho một người bạn dùng thử. Ở ô "Điểm", bạn ấy gõ "tám rưỡi". Chương trình in ra một đoạn chữ đỏ khó hiểu rồi tắt, mất hết điểm đã nhập. Người dùng không sai: chương trình chưa sẵn sàng cho dữ liệu thật.</em></p>
        <p><strong>Mục tiêu:</strong> Phân biệt được lỗi cú pháp, lỗi thực thi và lỗi logic; đọc được Traceback để tìm loại lỗi và dòng gây lỗi; dùng được <code>try – except – else – finally</code> để bắt <code>ValueError</code>, <code>ZeroDivisionError</code>; debug được chương trình bằng <code>print</code> và breakpoint trong VS Code.</p>
        <p><strong>Nội dung:</strong></p>
        <ul>
            <li><strong>Ý chính 1 - Ba loại lỗi:</strong> cú pháp, thực thi (ngoại lệ), logic.</li>
            <li><strong>Ý chính 2 - Đọc Traceback:</strong> đọc từ dưới lên: loại lỗi, thông điệp, file và dòng.</li>
            <li><strong>Ý chính 3 - try – except – else – finally:</strong> bắt đúng loại lỗi, không dùng <code>except:</code> trống.</li>
            <li><strong>Ý chính 4 - Debugging trong VS Code và cùng AI:</strong> breakpoint, chạy từng bước, xem biến; nhờ AI giải thích lỗi.</li>
        </ul>
        <p><strong>Kết quả cần đạt:</strong> Student Dashboard không bị dừng khi người dùng nhập sai; sinh viên tự tìm và sửa được 5 lỗi trong bài "săn lỗi".</p>
        <p style="margin-bottom: 0;"><strong>CLO liên quan:</strong> CLO1.</p>
    </div>
</details>

<details style="border: 1px solid #fd7e14; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #fff5eb; color: #fd7e14; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📚 2. Học liệu chính</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.1. Ba loại lỗi</h3>
            <table style="width: 100%; border-collapse: collapse; font-size: 14px;">
                <thead><tr style="background-color: #fff5eb;"><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Loại</th><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Khi nào phát hiện</th><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Ví dụ</th></tr></thead>
                <tbody>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;"><strong>Lỗi cú pháp</strong> (syntax error)</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Trước khi chạy; chương trình không chạy được dòng nào</td><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>if diem &gt;= 5</code> thiếu dấu <code>:</code> → <code>SyntaxError</code></td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;"><strong>Lỗi thực thi</strong> (ngoại lệ, exception)</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Khi đang chạy; chương trình dừng giữa chừng, in Traceback</td><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>int("mười")</code> → <code>ValueError</code>; <code>8 / 0</code> → <code>ZeroDivisionError</code></td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;"><strong>Lỗi logic</strong></td><td style="padding: 8px; border: 1px solid #ffd6ad;">Không báo gì; chỉ phát hiện khi so với kết quả tính tay</td><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>8 + 9 / 2</code> thay cho <code>(8 + 9) / 2</code></td></tr>
                </tbody>
            </table>
            <p style="margin-bottom: 0;"><code>try – except</code> chỉ xử lý được <strong>lỗi thực thi</strong>. Lỗi cú pháp phải sửa code; lỗi logic phải phát hiện bằng kiểm thử với dữ liệu đã tính tay.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.2. Đọc Traceback</h3>
            <p>Khi nhập "mười" vào chương trình <code>ho_so.py</code>, Python in:</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>Traceback (most recent call last):
  File "D:\nhap-mon-lap-trinh\buoi-06\ho_so.py", line 2, in &lt;module&gt;
    nam_sinh = int(input("Năm sinh: "))
               ^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'mười'</code></pre>
            <ol style="margin-bottom: 0;">
                <li><strong>Đọc dòng cuối trước:</strong> loại lỗi là <code>ValueError</code>.</li>
                <li><strong>Đọc thông điệp:</strong> <code>int()</code> không đổi được chuỗi <code>'mười'</code> thành số.</li>
                <li><strong>Tìm vị trí:</strong> file <code>ho_so.py</code>, <code>line 2</code>, kèm nội dung dòng đó. Từ Python 3.11, dòng dấu <code>^</code> (một số phiên bản có thêm <code>~</code>) đánh dấu đúng biểu thức gây lỗi.</li>
                <li><strong>Mở đúng dòng, sửa và chạy lại:</strong> ở đây lỗi do dữ liệu nhập, nên cách sửa là bắt lỗi (mục 2.3).</li>
            </ol>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.3. try – except – else – finally</h3>
            <ul>
                <li><code>try:</code> khối lệnh có thể gây lỗi.</li>
                <li><code>except ValueError:</code> chạy khi gặp đúng loại lỗi này; có thể có nhiều <code>except</code> cho nhiều loại.</li>
                <li><code>else:</code> chạy khi <code>try</code> không lỗi. <code>finally:</code> luôn chạy, có lỗi hay không.</li>
                <li><strong>Không dùng <code>except:</code> trống:</strong> nó nuốt mọi lỗi, kể cả lỗi do bạn gõ sai tên biến, làm bug khó tìm hơn.</li>
            </ul>
            <p style="margin: 0 0 6px 0;"><strong>💡 Nhập điểm an toàn:</strong> kết hợp vòng lặp (bài 05) với <code>try – except</code>.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>while True:
    try:
        diem = float(input("Điểm (0-10): "))
    except ValueError:
        print("Hãy nhập số, dùng dấu chấm cho phần thập phân.")
    else:
        if 0 &lt;= diem &lt;= 10:
            break
        print("Điểm phải nằm trong khoảng 0-10.")
print(f"Đã ghi nhận điểm {diem}")</code></pre>
            <p style="margin: 8px 0 6px 0;"><strong>💡 Chia cho 0</strong> khi chưa có học phần nào (lỗi để lại từ bài 04):</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>try:
    tb = sum(diem_list) / len(diem_list)
except ZeroDivisionError:
    print("Chưa có điểm nào để tính trung bình.")
else:
    print(f"Điểm trung bình: {tb:.2f}")</code></pre>
            <p style="margin-bottom: 0;">Với trường hợp đoán trước được như list rỗng, kiểm tra trước bằng <code>if len(diem_list) == 0</code> (bài 05) cũng đúng và dễ đọc. Dùng <code>try</code> cho những lỗi không kiểm tra trước được dễ dàng, như chuỗi người dùng gõ có đổi được thành số hay không.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.4. Debugging trong VS Code và cùng AI</h3>
            <ul>
                <li><strong>Debug bằng <code>print</code>:</strong> in giá trị biến ở các điểm nghi ngờ, ví dụ <code>print("DEBUG tong =", tong)</code> trong vòng lặp. Xóa các dòng này khi đã sửa xong.</li>
                <li><strong>Breakpoint:</strong> bấm vào lề trái số dòng (chấm đỏ) hoặc nhấn <code>F9</code>; chạy bằng <code>F5</code> (Run and Debug, chọn Python File).</li>
                <li><strong>Chạy từng bước:</strong> <code>F10</code> (Step Over) chạy dòng tiếp theo; khung <em>Variables</em> hiện giá trị mọi biến; <code>F5</code> chạy tiếp tới breakpoint sau.</li>
            </ul>
            <p style="margin: 0 0 6px 0;"><strong>Nhờ AI đọc lỗi:</strong> dán Traceback và đoạn code liên quan, yêu cầu giải thích chứ không sửa hộ.</p>
            <p style="margin: 0; padding: 8px 10px; background-color: #fff; border-left: 4px solid #fd7e14;"><em>"Tôi mới học Python. Giải thích Traceback dưới đây bằng ngôn ngữ dễ hiểu: lỗi gì, ở dòng nào, vì sao xảy ra, và gợi ý chỗ cần sửa. Không viết lại toàn bộ code. [dán Traceback và code]"</em></p>
        </div>

        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📄 Slide &amp; video bài giảng</p>
            <a href="{{LINK_SLIDE_BAI_06}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📄 Slide Bài 06: Xử lý ngoại lệ try – except và debugging</span>
            </a>
            <a class="nomediaplugin" href="{{LINK_VIDEO_BAI_06}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🎥 Video: đọc Traceback và debug bằng breakpoint trong VS Code</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📖 Tài liệu đọc thêm (chính thức)</p>
            <a href="https://docs.python.org/3/tutorial/errors.html" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 The Python Tutorial – Errors and Exceptions</span><br>
                <span style="color: #6c757d; font-size: 13px;">Lỗi cú pháp, ngoại lệ, try – except – else – finally.</span>
            </a>
            <a href="https://code.visualstudio.com/docs/python/debugging" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 VS Code – Python debugging</span><br>
                <span style="color: #6c757d; font-size: 13px;">Breakpoint, chạy từng bước, xem biến.</span>
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
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🧑‍🏫 Thực hành có hướng dẫn (1,5 tiết): Lab "săn lỗi"</strong></p>
            <ol style="margin: 0; color: #495057;">
                <li>Tải 5 đoạn code có lỗi (<code>loi_1.py</code> … <code>loi_5.py</code>): <a href="{{LINK_LAB_SAN_LOI}}" target="_blank" rel="noopener noreferrer" style="color: #28a745; font-weight: bold;">bai-06-san-loi.zip</a>. Đoạn 3 và 4 có ghi dữ liệu chạy thử trong chú thích: hãy nhập đúng như vậy.</li>
                <li>Với mỗi đoạn: <strong>tự đoán</strong> lỗi trước, sau đó chạy, đọc Traceback; đoạn không báo lỗi thì tính tay để tìm lỗi logic.</li>
                <li>Chỉ hỏi AI khi đã đoán xong; dùng prompt ở mục 2.4.</li>
                <li>Đặt breakpoint ở đoạn có vòng lặp, chạy từng bước và quan sát khung Variables.</li>
                <li>Ghi bảng 5 cột: lỗi, loại lỗi, nguyên nhân, cách sửa, đoán đúng trước khi hỏi AI chưa.</li>
            </ol>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">✍️ Thực hành tự làm (2 tiết): Student Dashboard v6 – nhập liệu an toàn</strong></p>
            <p style="margin: 0 0 6px 0; color: #495057;">Rà lại mọi chỗ <code>int(input())</code>, <code>float(input())</code> trong menu: nhập sai kiểu thì báo lỗi rõ ràng và hỏi lại; thống kê khi chưa có học phần không gây <code>ZeroDivisionError</code>. Thử phá chương trình bằng ít nhất 6 kiểu dữ liệu xấu: chữ, số âm, 11, để trống, <code>8,5</code>, chọn menu không tồn tại.</p>
            <p style="margin: 0 0 8px 0; color: #495057;"><strong>Nộp:</strong> <code>ho_so.py</code>, bảng săn lỗi 5 cột, bảng "phá chương trình" (dữ liệu nhập, kết quả), Nhật ký Prompt. <strong>Hoàn thành khi:</strong> không kiểu dữ liệu xấu nào làm chương trình dừng.</p>
            <a href="{{LINK_NOP_BAI_06}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp bài</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">💬 Diễn đàn thảo luận</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">Đăng một lần AI giải thích lỗi chưa đúng hoặc gợi ý cách sửa làm phát sinh lỗi mới. Bạn phát hiện ra bằng cách nào?</p>
            <a href="{{LINK_DIEN_DAN_BAI_06}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Tham gia diễn đàn</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">📝 Trắc nghiệm nhanh (Quiz)</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">10 câu ôn tập: ba loại lỗi, đọc Traceback, <code>try – except – else – finally</code>, debugging.</p>
            <a href="{{LINK_QUIZ_BAI_06}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Làm bài Quiz Bài 06</a>
        </div>
    </div>
</details>

<details style="border: 1px solid #6f42c1; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #f3e5f5; color: #6f42c1; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>🆘 4. Góc trợ giúp và mở rộng</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>Đã có <code>try</code> mà chương trình vẫn dừng:</strong> loại lỗi trong <code>except</code> không khớp (ví dụ bắt <code>ValueError</code> nhưng lỗi là <code>ZeroDivisionError</code>), hoặc dòng gây lỗi nằm ngoài khối <code>try</code>.</p>
        <p><strong><code>NameError: name 'diem' is not defined</code> sau khối try:</strong> lần nhập đầu bị lỗi nên biến chưa được gán; dùng mẫu <code>while True</code> ở mục 2.3 để chỉ thoát vòng lặp khi đã có giá trị hợp lệ.</p>
        <p><strong>Nút F5 không dừng ở breakpoint:</strong> kiểm tra đã chọn cấu hình <em>Python Debugger: Current File</em> và đang mở đúng file.</p>
        <p><strong>Kiến thức mở rộng:</strong> bắt nhiều loại lỗi trong một dòng <code>except (ValueError, ZeroDivisionError):</code>; đọc thông điệp lỗi bằng <code>except ValueError as loi: print(loi)</code>; tự báo lỗi bằng <code>raise</code>.</p>
        <p style="margin-bottom: 0;"><strong>Tự đánh giá:</strong> Đoạn <code>x = int("7.5")</code> gây lỗi gì? Còn <code>x = float("7.5")</code>? (Đáp án: <code>ValueError</code>; không lỗi, x = 7.5.)</p>
    </div>
</details>
