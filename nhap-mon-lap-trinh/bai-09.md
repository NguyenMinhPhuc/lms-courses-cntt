<details open="" style="border: 1px solid #007bff; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #e7f1ff; color: #007bff; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📘 1. Tổng quan bài học</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>BÀI 09 - Tổ chức mã nguồn và chuẩn PEP 8 (5 tiết: 1,5 LT / 3,5 TH)</strong></p>
        <p><em>Code được đọc nhiều hơn được viết. Ba tuần nữa, chính bạn đọc lại hàm <code>f(a, b, c)</code> và không nhớ nó làm gì; bạn cùng nhóm thì càng không. Mini Project sắp bắt đầu, và code của mỗi người phải để người khác đọc hiểu được.</em></p>
        <p><strong>Mục tiêu:</strong> Giải thích được phạm vi của biến cục bộ và toàn cục; áp dụng được quy tắc đặt tên và trình bày theo PEP 8; viết được docstring cho hàm và module; refactor được code cho dễ đọc mà không làm đổi kết quả, có dùng công cụ Ruff.</p>
        <p><strong>Nội dung:</strong></p>
        <ul>
            <li><strong>Ý chính 1 - Phạm vi biến:</strong> biến cục bộ, biến toàn cục, lỗi <code>UnboundLocalError</code>; truyền tham số và <code>return</code> thay cho biến toàn cục.</li>
            <li><strong>Ý chính 2 - PEP 8:</strong> <code>snake_case</code>, hằng số viết hoa, thụt lề 4 dấu cách, khoảng trắng, độ dài dòng; Ruff trong VS Code.</li>
            <li><strong>Ý chính 3 - Docstring và chú thích:</strong> mô tả hàm làm gì; chú thích giải thích "vì sao".</li>
            <li><strong>Ý chính 4 - Refactor có kiểm soát:</strong> đổi tên, bỏ số ma thuật, chạy lại để chắc kết quả không đổi; refactor cùng AI.</li>
        </ul>
        <p><strong>Kết quả cần đạt:</strong> Student Dashboard bản hoàn chỉnh theo PEP 8, mọi hàm có docstring, <code>ruff check</code> không còn cảnh báo, kèm bảng các thay đổi khi refactor.</p>
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
            <h3 style="margin-top: 0; color: #fd7e14;">2.1. Phạm vi biến (scope)</h3>
            <ul>
                <li><strong>Biến cục bộ</strong> (local): tạo bên trong hàm (kể cả tham số), chỉ dùng được trong hàm đó, mất đi khi hàm kết thúc.</li>
                <li><strong>Biến toàn cục</strong> (global): tạo ngoài mọi hàm; hàm đọc được, nhưng nếu hàm <em>gán</em> cho tên đó thì Python coi đó là biến cục bộ mới.</li>
            </ul>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>tong = 0


def cong_diem(d):
    tong = tong + d      # lỗi ở dòng này
    return tong


cong_diem(8)
# UnboundLocalError: cannot access local variable 'tong'
#                    where it is not associated with a value</code></pre>
            <p style="margin-bottom: 0;"><strong>Cách đúng:</strong> đưa dữ liệu vào qua tham số và lấy ra bằng <code>return</code>: <code>def cong_diem(tong, d): return tong + d</code>, gọi <code>tong = cong_diem(tong, 8)</code>. Từ khóa <code>global</code> giúp "chạy được" nhưng làm hàm phụ thuộc vào biến bên ngoài, khó kiểm thử; học phần này không dùng <code>global</code>.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.2. PEP 8 và công cụ Ruff</h3>
            <p><strong>PEP 8</strong> là hướng dẫn trình bày mã Python chính thức. Những quy tắc dùng nhiều nhất:</p>
            <table style="width: 100%; border-collapse: collapse; font-size: 14px;">
                <thead><tr style="background-color: #fff5eb;"><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Quy tắc</th><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Đúng</th><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Chưa đúng</th></tr></thead>
                <tbody>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;">Tên biến, hàm: chữ thường nối gạch dưới</td><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>diem_tb</code>, <code>tinh_diem_tb()</code></td><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>DiemTB</code>, <code>tinhDiem()</code></td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;">Hằng số: chữ hoa</td><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>NGUONG_DAT = 4.0</code></td><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>nguong = 4.0</code> rồi không đổi</td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;">Thụt lề 4 dấu cách</td><td style="padding: 8px; border: 1px solid #ffd6ad;">4 dấu cách mỗi cấp</td><td style="padding: 8px; border: 1px solid #ffd6ad;">2 dấu cách, trộn Tab</td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;">Khoảng trắng quanh toán tử, sau dấu phẩy</td><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>x = a * 0.3 + b</code>, <code>f(a, b)</code></td><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>x=a*0.3+b</code>, <code>f(a,b)</code></td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;">Mỗi lệnh một dòng; dòng không quá 79 ký tự</td><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>if x &gt;= 4:</code> xuống dòng rồi lệnh</td><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>if x&gt;=4: print("Dat")</code></td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;">2 dòng trống giữa các hàm cấp ngoài cùng</td><td style="padding: 8px; border: 1px solid #ffd6ad;">như code mẫu bài 08</td><td style="padding: 8px; border: 1px solid #ffd6ad;">các hàm dính liền nhau</td></tr>
                </tbody>
            </table>
            <p style="margin: 10px 0 0 0;"><strong>Ruff</strong> (cài extension <em>Ruff</em> trong VS Code, hoặc <code>pip install ruff</code>): <code>ruff check ten_file.py</code> tìm lỗi và vi phạm như nhiều lệnh trên một dòng, biến không dùng, <code>import</code> thừa; <code>ruff format ten_file.py</code> tự sửa khoảng trắng, thụt lề, xuống dòng. <strong>Công cụ không đặt lại tên giúp bạn:</strong> <code>f(a, b, c)</code> sau khi format vẫn là <code>f(a, b, c)</code>.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.3. Docstring và chú thích</h3>
            <ul>
                <li><strong>Docstring</strong> là chuỗi ba dấu nháy ngay dưới dòng <code>def</code> (hoặc đầu file), mô tả hàm làm gì, nhận gì, trả về gì. VS Code hiện docstring khi rê chuột vào tên hàm; <code>help(xep_loai)</code> cũng in ra nó.</li>
                <li><strong>Chú thích <code>#</code></strong> giải thích <em>vì sao</em>, không lặp lại code. Tốt: <code># trọng số theo đề cương: 30-30-40</code>. Thừa: <code># cộng 1 vào i</code> cho dòng <code>i += 1</code>.</li>
            </ul>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>def thong_ke(diem_list):
    """Trả về (thấp nhất, cao nhất, trung bình) của một list điểm khác rỗng."""
    return min(diem_list), max(diem_list), sum(diem_list) / len(diem_list)</code></pre>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.4. Refactor có kiểm soát</h3>
            <p><strong>Refactor</strong> là sửa cấu trúc code cho dễ đọc, dễ sửa mà <strong>không đổi kết quả</strong>. Quy trình: chạy và ghi kết quả trước → sửa một chỗ nhỏ → chạy lại, so kết quả → lặp lại → cuối cùng chạy <code>ruff check</code>.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code># TRƯỚC
def f(a,b,c):
  x=a*0.3+b*0.3+c*0.4
  if x&gt;=4: print("Dau")
  else: print("Rot")
  return x</code></pre>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code># SAU
NGUONG_DAT = 4.0


def tinh_diem_tb(qt, gk, ck):
    """Trả về điểm học phần theo trọng số 30-30-40."""
    return qt * 0.3 + gk * 0.3 + ck * 0.4


def ket_qua(diem):
    """Trả về "Đậu" nếu diem đạt NGUONG_DAT, ngược lại "Rớt"."""
    if diem &gt;= NGUONG_DAT:
        return "Đậu"
    return "Rớt"</code></pre>
            <p>Các thay đổi: tên có nghĩa; số <code>4</code> "ma thuật" thành hằng số <code>NGUONG_DAT</code>; tách một hàm làm hai việc (tính và in) thành hai hàm, mỗi hàm một việc; hàm trả về chuỗi thay vì in; thêm docstring; trình bày theo PEP 8.</p>
            <p style="margin: 0; padding: 8px 10px; background-color: #fff; border-left: 4px solid #fd7e14;"><em>"Refactor đoạn code sau theo PEP 8, giữ nguyên chức năng. Liệt kê từng thay đổi và lý do. Không thêm thư viện hay tính năng mới. [dán code]"</em> Sau đó chạy lại cả bản cũ và bản AI đề xuất với cùng dữ liệu; chỉ nhận thay đổi giữ đúng kết quả.</p>
        </div>

        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📄 Slide &amp; video bài giảng</p>
            <a href="{{LINK_SLIDE_BAI_09}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📄 Slide Bài 09: Tổ chức mã nguồn và chuẩn PEP 8</span>
            </a>
            <a class="nomediaplugin" href="{{LINK_VIDEO_BAI_09}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🎥 Video: refactor một chương trình và dùng Ruff trong VS Code</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📖 Tài liệu đọc thêm (chính thức)</p>
            <a href="https://peps.python.org/pep-0008/" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 PEP 8 – Style Guide for Python Code</span><br>
                <span style="color: #6c757d; font-size: 13px;">Quy ước đặt tên, thụt lề, khoảng trắng, độ dài dòng.</span>
            </a>
            <a href="https://peps.python.org/pep-0257/" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 PEP 257 – Docstring Conventions</span><br>
                <span style="color: #6c757d; font-size: 13px;">Cách viết docstring cho hàm và module.</span>
            </a>
            <a href="https://docs.astral.sh/ruff/" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Ruff Documentation</span><br>
                <span style="color: #6c757d; font-size: 13px;">ruff check, ruff format và tích hợp VS Code.</span>
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
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🧑‍🏫 Thực hành có hướng dẫn (1,5 tiết): refactor một chương trình "xấu"</strong></p>
            <ol style="margin: 0; color: #495057;">
                <li>Chạy ví dụ <code>UnboundLocalError</code> ở mục 2.1, sửa bằng tham số và <code>return</code>.</li>
                <li>Cài extension Ruff; mở chương trình "xấu" giảng viên cung cấp, chạy <code>ruff check</code> và đọc từng cảnh báo.</li>
                <li>Ghi kết quả chạy với 3 bộ dữ liệu, rồi refactor từng bước theo mục 2.4, chạy lại sau mỗi bước.</li>
                <li>Nhờ AI đề xuất refactor; lập bảng: thay đổi của AI, nhận hay không, lý do.</li>
            </ol>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">✍️ Thực hành tự làm (2 tiết): Student Dashboard v9 – bản hoàn chỉnh</strong></p>
            <p style="margin: 0 0 6px 0; color: #495057;">Rà lại 3 file của bản v8: đổi tên chưa rõ nghĩa, thay số ma thuật bằng hằng số, bỏ biến toàn cục bị gán trong hàm, thêm docstring cho mọi hàm và đầu mỗi file, chạy <code>ruff format</code> và <code>ruff check</code> tới khi không còn cảnh báo.</p>
            <p style="margin: 0 0 8px 0; color: #495057;"><strong>Nộp:</strong> 3 file <code>.py</code>, bảng thay đổi khi refactor (trước, sau, lý do), ảnh chụp <code>ruff check</code> báo "All checks passed!", Nhật ký Prompt. <strong>Hoàn thành khi:</strong> kết quả chạy giống hệt bản v8 với cùng dữ liệu.</p>
            <a href="{{LINK_NOP_BAI_09}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp bài</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">💬 Diễn đàn thảo luận</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">Đăng một thay đổi AI đề xuất khi refactor mà bạn <strong>không</strong> nhận. Vì sao? (Ví dụ: đổi kết quả, dùng kiến thức chưa học, làm code khó đọc hơn.)</p>
            <a href="{{LINK_DIEN_DAN_BAI_09}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Tham gia diễn đàn</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">📝 Trắc nghiệm nhanh (Quiz)</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">10 câu ôn tập: phạm vi biến, quy tắc PEP 8, docstring, refactor, Ruff.</p>
            <a href="{{LINK_QUIZ_BAI_09}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Làm bài Quiz Bài 09</a>
        </div>
    </div>
</details>

<details style="border: 1px solid #6f42c1; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #f3e5f5; color: #6f42c1; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>🆘 4. Góc trợ giúp và mở rộng</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>Lệnh <code>ruff</code> báo "not recognized":</strong> extension Ruff trong VS Code vẫn hoạt động (gạch chân và Format Document); muốn dùng lệnh trong Terminal thì cài <code>pip install ruff</code>.</p>
        <p><strong>Refactor xong chương trình chạy khác trước:</strong> quay lại bản trước (vì vậy nên sửa từng bước nhỏ và lưu bản cũ), so từng thay đổi để tìm chỗ làm đổi kết quả.</p>
        <p><strong>Ruff báo <code>F401 ... imported but unused</code>:</strong> có <code>import</code> mà không dùng; xóa dòng đó.</p>
        <p><strong>Kiến thức mở rộng:</strong> gợi ý kiểu dữ liệu (type hints) <code>def tinh_diem_tb(qt: float, gk: float, ck: float) -&gt; float:</code>; bật Format on Save trong VS Code để tự format mỗi lần lưu.</p>
        <p style="margin-bottom: 0;"><strong>Tự đánh giá:</strong> Đưa file của bạn cho một bạn khác đọc 2 phút, không giải thích. Bạn ấy có nói đúng từng hàm làm gì không?</p>
    </div>
</details>
