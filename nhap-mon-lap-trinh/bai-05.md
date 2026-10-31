<details open="" style="border: 1px solid #007bff; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #e7f1ff; color: #007bff; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📘 1. Tổng quan bài học</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>BÀI 05 - Vòng lặp while và menu tương tác (5 tiết: 1,5 LT / 3,5 TH)</strong></p>
        <p><em>Máy bán nước tự động không biết trước có bao nhiêu khách. Nó cứ hiện menu, nhận lựa chọn, trả nước, rồi quay lại chờ khách tiếp theo. Chương trình của bạn cũng cần chạy cho đến khi người dùng chọn "Thoát", chứ không phải đúng 5 lần.</em></p>
        <p><strong>Mục tiêu:</strong> Phân biệt được khi nào dùng <code>for</code>, khi nào dùng <code>while</code>; thiết lập được điều kiện dừng và tránh vòng lặp vô hạn; dùng được <code>break</code>, <code>continue</code>; xây dựng được menu dòng lệnh lặp tới khi người dùng thoát.</p>
        <p><strong>Nội dung:</strong></p>
        <ul>
            <li><strong>Ý chính 1 - while và điều kiện dừng:</strong> lặp khi điều kiện còn đúng; vòng lặp vô hạn và cách dừng.</li>
            <li><strong>Ý chính 2 - Lặp nhập dữ liệu hợp lệ:</strong> hỏi lại cho tới khi dữ liệu đúng yêu cầu.</li>
            <li><strong>Ý chính 3 - break, continue và trò chơi đoán số:</strong> thoát sớm, bỏ qua một chu kỳ; dùng <code>random.randint</code>.</li>
            <li><strong>Ý chính 4 - Menu dòng lệnh (CLI):</strong> mẫu <code>while True</code> gồm in menu, đọc lựa chọn, rẽ nhánh, "0. Thoát".</li>
        </ul>
        <p><strong>Kết quả cần đạt:</strong> Sinh viên hoàn thành trò chơi đoán số và đưa Student Dashboard vào một menu chạy liên tục tới khi chọn Thoát.</p>
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
            <h3 style="margin-top: 0; color: #fd7e14;">2.1. while và điều kiện dừng</h3>
            <p><code>while dieu_kien:</code> kiểm tra điều kiện <strong>trước mỗi chu kỳ</strong>; còn đúng thì chạy khối lệnh, sai thì thoát. Dùng <code>while</code> khi <strong>chưa biết trước số lần lặp</strong>; biết trước số lần thì <code>for</code> gọn hơn.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>dem = 5
while dem &gt; 0:
    print(dem)
    dem -= 1          # thiếu dòng này: lặp vô hạn
print("Hết giờ!")</code></pre>
            <p style="margin-bottom: 0;"><strong>Vòng lặp vô hạn</strong> xảy ra khi điều kiện không bao giờ sai, thường do quên cập nhật biến điều khiển. Dừng chương trình bằng <code>Ctrl + C</code> trong Terminal. Khi viết <code>while</code>, luôn tự hỏi: <em>dòng nào làm điều kiện tiến dần tới sai?</em></p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.2. Lặp nhập dữ liệu hợp lệ</h3>
            <p>Thay vì chỉ báo <code>False</code> như ở bài 02, chương trình hỏi lại cho tới khi người dùng nhập đúng.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>diem = float(input("Điểm (0-10): "))
while diem &lt; 0 or diem &gt; 10:
    print("Điểm không hợp lệ, hãy nhập lại.")
    diem = float(input("Điểm (0-10): "))
print(f"Đã ghi nhận điểm {diem}")</code></pre>
            <p style="margin-bottom: 0;">Lưu đồ của đoạn này có mũi tên từ khối "báo lỗi, nhập lại" <strong>quay ngược lên</strong> khối điều kiện: đó là dấu hiệu nhận biết vòng lặp trên lưu đồ. Đoạn code vẫn bị dừng nếu người dùng gõ chữ thay vì số; bài 06 sẽ xử lý tiếp.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.3. break, continue và trò chơi đoán số</h3>
            <ul>
                <li><code>break</code>: thoát khỏi vòng lặp ngay lập tức.</li>
                <li><code>continue</code>: bỏ phần còn lại của chu kỳ hiện tại, sang chu kỳ tiếp theo.</li>
                <li><code>import random</code> rồi <code>random.randint(1, 100)</code> cho một số nguyên ngẫu nhiên từ 1 đến 100 (gồm cả hai đầu).</li>
            </ul>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>import random

bi_mat = random.randint(1, 100)
so_lan = 0
doan_dung = False
while so_lan &lt; 7:
    so_lan += 1
    doan = int(input(f"Lần {so_lan}/7 - Đoán số (1-100): "))
    if doan == bi_mat:
        doan_dung = True
        break
    elif doan &lt; bi_mat:
        print("Lớn hơn nữa.")
    else:
        print("Nhỏ hơn nữa.")

if doan_dung:
    print(f"Chính xác! Bạn đoán đúng sau {so_lan} lần.")
else:
    print(f"Hết lượt. Số bí mật là {bi_mat}.")</code></pre>
            <p style="margin-bottom: 0;"><strong>💡 continue:</strong> khi cộng dồn số tiền thu quỹ lớp, gặp số âm thì <code>continue</code> để bỏ qua, không cộng. Biến <code>doan_dung</code> là một <strong>cờ</strong> (flag): ghi nhớ điều gì đã xảy ra trong vòng lặp để dùng sau vòng lặp.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.4. Menu dòng lệnh: Student Dashboard v5</h3>
            <p>Mẫu menu dùng <code>while True</code>: lặp mãi, chỉ thoát bằng <code>break</code> khi người dùng chọn 0. Mỗi lựa chọn là một nhánh <code>if-elif</code>.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>diem_list = []
while True:
    print("\n=== STUDENT DASHBOARD ===")
    print("1. Nhập điểm   2. Xem thống kê   0. Thoát")
    chon = input("Chọn: ")
    if chon == "1":
        d = float(input("Điểm: "))
        diem_list.append(d)
    elif chon == "2":
        if len(diem_list) == 0:
            print("Chưa có điểm nào.")
        else:
            tb = sum(diem_list) / len(diem_list)
            print(f"Số học phần: {len(diem_list)} | TB: {tb:.2f}")
    elif chon == "0":
        print("Tạm biệt!")
        break
    else:
        print("Lựa chọn không hợp lệ.")</code></pre>
            <p style="margin-bottom: 0;">Lựa chọn được so sánh với chuỗi <code>"1"</code>, không phải số <code>1</code>, vì <code>input()</code> trả về chuỗi. Nhánh <code>else</code> cuối cùng xử lý mọi lựa chọn sai, kể cả khi người dùng chỉ nhấn Enter.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.5. Nhờ AI tìm lỗi vòng lặp</h3>
            <p>Khi vòng lặp không dừng hoặc dừng quá sớm, đừng nhờ AI viết lại cả chương trình. Hãy để AI chỉ ra chỗ sai, còn bạn tự sửa.</p>
            <p style="margin: 0 0 8px 0; padding: 8px 10px; background-color: #fff; border-left: 4px solid #fd7e14;"><em>"Vòng lặp while dưới đây không dừng khi tôi nhập 0. Hãy chỉ ra dòng gây lỗi và giải thích vì sao, đừng viết lại toàn bộ code. [dán đoạn code]"</em></p>
            <p style="margin-bottom: 0;">Sau khi sửa, ghi vào Nhật ký Prompt: AI chỉ ra dòng nào, nguyên nhân là gì, bạn sửa thế nào và đã kiểm tra lại bằng dữ liệu nào.</p>
        </div>

        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📄 Slide &amp; video bài giảng</p>
            <a href="{{LINK_SLIDE_BAI_05}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📄 Slide Bài 05: Vòng lặp while và menu tương tác</span>
            </a>
            <a class="nomediaplugin" href="{{LINK_VIDEO_BAI_05}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🎥 Video: trò chơi đoán số và menu dòng lệnh</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📖 Tài liệu đọc thêm (chính thức)</p>
            <a href="https://docs.python.org/3/reference/compound_stmts.html#the-while-statement" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Python Language Reference – The while statement</span><br>
                <span style="color: #6c757d; font-size: 13px;">Cú pháp while, break, continue.</span>
            </a>
            <a href="https://docs.python.org/3/library/random.html#random.randint" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Python Library – random.randint</span><br>
                <span style="color: #6c757d; font-size: 13px;">Sinh số nguyên ngẫu nhiên trong khoảng [a, b].</span>
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
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🧑‍🏫 Thực hành có hướng dẫn (1,5 tiết): đếm ngược và đoán số</strong></p>
            <ol style="margin: 0; color: #495057;">
                <li>Chạy đoạn đếm ngược ở mục 2.1, xóa dòng <code>dem -= 1</code> để thấy vòng lặp vô hạn, dừng bằng <code>Ctrl + C</code>.</li>
                <li>Vẽ lưu đồ cho đoạn nhập điểm hợp lệ (mục 2.2), chú ý mũi tên quay lại.</li>
                <li>Gõ trò chơi đoán số; thêm chức năng hỏi "Chơi tiếp? (c/k)" bằng một vòng <code>while</code> bao ngoài.</li>
            </ol>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">✍️ Thực hành tự làm (2 tiết): Student Dashboard v5 – menu hoàn chỉnh</strong></p>
            <p style="margin: 0 0 6px 0; color: #495057;">Gom các chức năng đã làm vào một menu: <strong>1.</strong> Xem/sửa hồ sơ; <strong>2.</strong> Thêm học phần (tên và điểm, điểm nhập lại tới khi trong 0–10); <strong>3.</strong> Xem bảng điểm; <strong>4.</strong> Thống kê và xếp loại; <strong>0.</strong> Thoát. Chương trình chỉ kết thúc khi chọn 0.</p>
            <p style="margin: 0 0 8px 0; color: #495057;"><strong>Nộp:</strong> <code>ho_so.py</code>, lưu đồ menu, Nhật ký Prompt. <strong>Hoàn thành khi:</strong> chọn sai (ví dụ 9, chữ, Enter) không làm chương trình dừng; chọn 3, 4 khi chưa có học phần thì báo "Chưa có dữ liệu".</p>
            <a href="{{LINK_NOP_BAI_05}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp bài</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">💬 Diễn đàn thảo luận</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">Với trò chơi đoán số từ 1 đến 100, chiến lược nào luôn đoán đúng trong tối đa 7 lần? Giải thích vì sao 7 lần là đủ.</p>
            <a href="{{LINK_DIEN_DAN_BAI_05}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Tham gia diễn đàn</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">📝 Trắc nghiệm nhanh (Quiz)</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">10 câu ôn tập: <code>while</code>, điều kiện dừng, <code>break</code>, <code>continue</code>, menu dòng lệnh.</p>
            <a href="{{LINK_QUIZ_BAI_05}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Làm bài Quiz Bài 05</a>
        </div>
    </div>
</details>

<details style="border: 1px solid #6f42c1; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #f3e5f5; color: #6f42c1; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>🆘 4. Góc trợ giúp và mở rộng</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>Chương trình treo, Terminal không phản hồi:</strong> nhiều khả năng là vòng lặp vô hạn. Nhấn <code>Ctrl + C</code>, rồi thêm <code>print</code> giá trị biến điều khiển ở đầu mỗi chu kỳ để xem nó có thay đổi không.</p>
        <p><strong>Chọn đúng "1" mà vẫn vào nhánh "không hợp lệ":</strong> có thể bạn so sánh <code>chon == 1</code> (số) thay vì <code>chon == "1"</code> (chuỗi), hoặc người dùng gõ thêm dấu cách; dùng <code>input().strip()</code>.</p>
        <p><strong><code>break</code> đặt ngoài vòng lặp</strong> gây <code>SyntaxError: 'break' outside loop</code>: kiểm tra thụt lề.</p>
        <p><strong>Kiến thức mở rộng:</strong> mệnh đề <code>else</code> của vòng lặp (<code>while ... else</code>) chạy khi vòng lặp kết thúc mà không gặp <code>break</code>; có thể dùng thay cho biến cờ trong trò chơi đoán số.</p>
        <p style="margin-bottom: 0;"><strong>Tự đánh giá:</strong> Đoạn <code>x = 10</code>; <code>while x &gt; 0: x -= 3</code> chạy mấy chu kỳ, cuối cùng <code>x</code> bằng bao nhiêu? (Đáp án: 4 chu kỳ; x = -2.)</p>
    </div>
</details>
