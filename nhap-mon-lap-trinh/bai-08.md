<details open="" style="border: 1px solid #007bff; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #e7f1ff; color: #007bff; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📘 1. Tổng quan bài học</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>BÀI 08 - Hàm cơ bản và tách module (5 tiết: 1,5 LT / 3,5 TH)</strong></p>
        <p><em>Mở lại Student Dashboard v6: đoạn "nhập số an toàn" (vòng <code>while</code> và <code>try – except</code>) có lẽ đã bị chép 3–4 lần. Muốn đổi câu báo lỗi, bạn phải sửa ở 4 chỗ và rất dễ quên một chỗ. Hàm giải quyết đúng vấn đề này.</em></p>
        <p><strong>Mục tiêu:</strong> Định nghĩa và gọi được hàm có tham số, giá trị mặc định và <code>return</code>; phân biệt được hàm trả về giá trị với hàm chỉ in; tách được bài toán thành các hàm đơn nhiệm bằng sơ đồ phân rã; tổ chức được chương trình thành nhiều file và dùng <code>import</code>.</p>
        <p><strong>Nội dung:</strong></p>
        <ul>
            <li><strong>Ý chính 1 - Vì sao cần hàm:</strong> không lặp code, sửa một nơi, kiểm thử riêng từng phần.</li>
            <li><strong>Ý chính 2 - def, tham số, giá trị mặc định, return:</strong> cấu trúc một hàm; trả nhiều giá trị bằng tuple.</li>
            <li><strong>Ý chính 3 - print khác return:</strong> hàm chỉ in thì không dùng lại được kết quả.</li>
            <li><strong>Ý chính 4 - Phân rã bài toán và module:</strong> sơ đồ phân rã, tách file, <code>import</code>, <code>if __name__ == "__main__":</code>.</li>
        </ul>
        <p><strong>Kết quả cần đạt:</strong> Student Dashboard được viết lại bằng hàm và tách thành nhiều file, chạy đúng như bản v6, kèm sơ đồ phân rã chức năng.</p>
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
            <h3 style="margin-top: 0; color: #fd7e14;">2.1. Vì sao cần hàm</h3>
            <p><strong>Hàm</strong> (function) là một khối lệnh có tên, nhận dữ liệu vào, xử lý và trả kết quả ra. Bạn đã dùng nhiều hàm có sẵn: <code>print()</code>, <code>input()</code>, <code>len()</code>, <code>max()</code>. Bài này bạn tự viết hàm.</p>
            <ul style="margin-bottom: 0;">
                <li><strong>Không lặp code:</strong> viết một lần, gọi nhiều lần. Sửa lỗi ở một chỗ là mọi nơi gọi hàm đều được sửa.</li>
                <li><strong>Dễ đọc:</strong> <code>diem = nhap_so("Điểm: ")</code> nói rõ ý định hơn 8 dòng <code>while – try</code>.</li>
                <li><strong>Dễ kiểm thử và chia việc:</strong> mỗi hàm thử riêng được; trong Mini Project, mỗi thành viên viết một số hàm.</li>
            </ul>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.2. def, tham số, giá trị mặc định, return</h3>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>def tinh_diem_tb(qt, gk, ck):
    """Trả về điểm học phần theo trọng số 30-30-40."""
    return qt * 0.3 + gk * 0.3 + ck * 0.4


diem = tinh_diem_tb(8, 7, 9)     # gọi hàm: 8, 7, 9 là đối số
print(f"{diem:.2f}")             # 8.10</code></pre>
            <ul>
                <li><strong>Tham số</strong> (<code>qt, gk, ck</code>) là tên nhận dữ liệu khi định nghĩa; <strong>đối số</strong> (<code>8, 7, 9</code>) là giá trị truyền vào khi gọi.</li>
                <li><code>return</code> kết thúc hàm và trả giá trị về chỗ gọi. Hàm không có <code>return</code> trả về <code>None</code>.</li>
                <li><strong>Giá trị mặc định:</strong> <code>def nhap_so(loi_nhac, nho_nhat=0, lon_nhat=10):</code> cho phép gọi <code>nhap_so("Điểm: ")</code> hoặc <code>nhap_so("Số tín chỉ: ", 1, 5)</code>.</li>
                <li><strong>Trả nhiều giá trị:</strong> <code>return min(ds), max(ds), sum(ds) / len(ds)</code>; nơi gọi viết <code>thap, cao, tb = thong_ke(ds)</code>.</li>
            </ul>
            <p style="margin: 0 0 6px 0;"><strong>💡 Hàm nhập số an toàn</strong>, gom đoạn code đã chép nhiều lần ở bài 06:</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>def nhap_so(loi_nhac, nho_nhat=0, lon_nhat=10):
    """Hỏi lại tới khi người dùng nhập một số trong [nho_nhat, lon_nhat]."""
    while True:
        try:
            gia_tri = float(input(loi_nhac))
        except ValueError:
            print("Hãy nhập số, dùng dấu chấm cho phần thập phân.")
            continue
        if nho_nhat &lt;= gia_tri &lt;= lon_nhat:
            return gia_tri
        print(f"Giá trị phải trong khoảng {nho_nhat}-{lon_nhat}.")</code></pre>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.3. print khác return</h3>
            <p>So sánh hai cách viết hàm xếp loại:</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>def in_xep_loai(diem):          # chỉ in
    if diem &gt;= 8:
        print("Giỏi")
    else:
        print("Chưa giỏi")


def xep_loai(diem):             # trả về
    if diem &gt;= 8:
        return "Giỏi"
    return "Chưa giỏi"


kq = in_xep_loai(8.5)    # in "Giỏi", nhưng kq là None
kq = xep_loai(8.5)       # kq = "Giỏi": dùng tiếp được
print(f"Bạn đạt loại {kq}")</code></pre>
            <p style="margin-bottom: 0;"><strong>Quy tắc:</strong> hàm tính toán thì <code>return</code>; việc in để cho phần chương trình chính. Hàm <code>return</code> mới ghép được với hàm khác, dùng trong điều kiện <code>if</code> và kiểm thử được bằng cách so kết quả.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.4. Phân rã bài toán và tách module</h3>
            <p><strong>Sơ đồ phân rã chức năng:</strong> chương trình chính ở trên cùng, mỗi hộp con là một hàm làm <em>một</em> việc: <code>hien_menu()</code>, <code>nhap_so()</code>, <code>tinh_diem_tb()</code>, <code>xep_loai()</code>, <code>thong_ke()</code>. Hộp nào còn làm nhiều việc thì chia tiếp.</p>
            <p><strong>Module</strong> là một file <code>.py</code>. Đặt các hàm cùng nhóm vào cùng file rồi <code>import</code>:</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code># main.py  (cùng thư mục với nhap_lieu.py và tinh_toan.py)
from nhap_lieu import nhap_so
from tinh_toan import thong_ke, xep_loai


def main():
    diem_list = []
    while True:
        print("1. Thêm học phần   2. Thống kê   0. Thoát")
        chon = input("Chọn: ").strip()
        if chon == "1":
            diem_list.append(nhap_so("Điểm: "))
        elif chon == "2" and len(diem_list) &gt; 0:
            thap, cao, tb = thong_ke(diem_list)
            print(f"TB: {tb:.2f} ({xep_loai(tb)}) | {thap} - {cao}")
        elif chon == "0":
            break


if __name__ == "__main__":
    main()</code></pre>
            <p style="margin-bottom: 0;"><code>if __name__ == "__main__":</code> nghĩa là: chỉ gọi <code>main()</code> khi chạy trực tiếp file này. Khi file khác <code>import</code> nó, các hàm được nạp nhưng menu không tự chạy.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.5. Nhờ AI đề xuất cách chia hàm</h3>
            <p>Đây là lúc AI hữu ích: nhìn chương trình dài và gợi ý cách chia. Nhưng hãy giữ phần viết code cho mình.</p>
            <p style="margin: 0 0 8px 0; padding: 8px 10px; background-color: #fff; border-left: 4px solid #fd7e14;"><em>"Đây là chương trình Python của tôi (dán code). Đề xuất cách chia thành các hàm đơn nhiệm. Với mỗi hàm chỉ nêu: tên, tham số, giá trị trả về, một câu mô tả. Không viết code."</em></p>
            <p style="margin-bottom: 0;">So sánh đề xuất của AI với sơ đồ phân rã của bạn: chọn hàm nào, bỏ hàm nào, vì sao. Ghi quyết định vào Nhật ký Prompt; đây là minh chứng bạn làm chủ thiết kế.</p>
        </div>

        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📄 Slide &amp; video bài giảng</p>
            <a href="{{LINK_SLIDE_BAI_08}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📄 Slide Bài 08: Hàm cơ bản và tách module</span>
            </a>
            <a class="nomediaplugin" href="{{LINK_VIDEO_BAI_08}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🎥 Video: viết lại Student Dashboard bằng hàm</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📖 Tài liệu đọc thêm (chính thức)</p>
            <a href="https://docs.python.org/3/tutorial/controlflow.html#defining-functions" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 The Python Tutorial – Defining Functions</span><br>
                <span style="color: #6c757d; font-size: 13px;">def, return, giá trị mặc định của tham số.</span>
            </a>
            <a href="https://docs.python.org/3/tutorial/modules.html" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 The Python Tutorial – Modules</span><br>
                <span style="color: #6c757d; font-size: 13px;">import, from … import, __name__.</span>
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
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🧑‍🏫 Thực hành có hướng dẫn (1,5 tiết): những hàm đầu tiên</strong></p>
            <ol style="margin: 0; color: #495057;">
                <li>Viết <code>tinh_diem_tb</code> và <code>xep_loai</code>; gọi thử với 5 bộ dữ liệu, so với kết quả tính tay.</li>
                <li>Viết <code>nhap_so</code> có giá trị mặc định; gọi với <code>nhap_so("Điểm: ")</code> và <code>nhap_so("Số tín chỉ: ", 1, 5)</code>.</li>
                <li>Đổi <code>xep_loai</code> từ <code>return</code> sang <code>print</code>, gán kết quả vào biến và in ra để thấy <code>None</code>.</li>
                <li>Vẽ sơ đồ phân rã Student Dashboard v6 trên Draw.io trước khi tách file.</li>
            </ol>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">✍️ Thực hành tự làm (2 tiết): Student Dashboard v8 – viết lại bằng hàm</strong></p>
            <p style="margin: 0 0 6px 0; color: #495057;">Viết lại toàn bộ v6 thành 3 file: <code>nhap_lieu.py</code> (nhập an toàn), <code>tinh_toan.py</code> (điểm, xếp loại, thống kê), <code>main.py</code> (menu và hàm <code>main</code>). Mỗi hàm làm một việc, có docstring một dòng. Hàm tính toán không được chứa <code>input()</code> hay <code>print()</code>.</p>
            <p style="margin: 0 0 8px 0; color: #495057;"><strong>Nộp:</strong> 3 file <code>.py</code>, sơ đồ phân rã, Nhật ký Prompt (có prompt đề xuất chia hàm và quyết định của bạn). <strong>Hoàn thành khi:</strong> chạy cho kết quả giống v6 với cùng dữ liệu; không còn đoạn code nào bị chép lặp.</p>
            <a href="{{LINK_NOP_BAI_08}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp bài</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">💬 Diễn đàn thảo luận</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">Đăng sơ đồ phân rã của bạn và cách chia hàm AI đề xuất. Hai cách khác nhau ở đâu? Bạn giữ cách nào cho từng chỗ và vì sao?</p>
            <a href="{{LINK_DIEN_DAN_BAI_08}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Tham gia diễn đàn</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">📝 Trắc nghiệm nhanh (Quiz)</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">10 câu ôn tập: định nghĩa và gọi hàm, tham số, giá trị mặc định, <code>return</code>, module và <code>import</code>.</p>
            <a href="{{LINK_QUIZ_BAI_08}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Làm bài Quiz Bài 08</a>
        </div>
    </div>
</details>

<details style="border: 1px solid #6f42c1; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #f3e5f5; color: #6f42c1; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>🆘 4. Góc trợ giúp và mở rộng</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong><code>TypeError: tinh_diem_tb() missing 1 required positional argument: 'ck'</code>:</strong> gọi hàm thiếu đối số; đếm lại số tham số trong <code>def</code>.</p>
        <p><strong><code>ModuleNotFoundError: No module named 'tinh_toan'</code>:</strong> file <code>tinh_toan.py</code> không nằm cùng thư mục với <code>main.py</code>, hoặc bạn đang chạy từ thư mục khác; mở đúng thư mục bằng VS Code rồi chạy lại.</p>
        <p><strong>In ra <code>None</code> lạ:</strong> bạn viết <code>print(ham())</code> với một hàm không có <code>return</code>.</p>
        <p><strong>Kiến thức mở rộng:</strong> gọi hàm bằng tên tham số <code>nhap_so("Điểm: ", lon_nhat=4)</code>; kiểm thử nhanh bằng <code>assert xep_loai(8) == "Giỏi"</code>.</p>
        <p style="margin-bottom: 0;"><strong>Tự đánh giá:</strong> Với <code>def f(a, b=2): return a * b</code>, <code>f(3)</code> và <code>f(3, 4)</code> trả về gì? (Đáp án: 6 và 12.)</p>
    </div>
</details>
