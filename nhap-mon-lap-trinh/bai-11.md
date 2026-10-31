<details open="" style="border: 1px solid #007bff; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #e7f1ff; color: #007bff; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📘 1. Tổng quan bài học</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>BÀI 11 - Hoàn thiện project và quản lý mã nguồn với GitHub (5 tiết: 1,5 LT / 3,5 TH)</strong></p>
        <p><em>Bốn người, bốn máy, bốn phiên bản <code>main.py</code> gửi qua Zalo: "main_final.py", "main_final_2.py", "main_final_thật_sự.py". Ghép lại thì mất hàm của nhau. GitHub giải quyết đúng chuyện này, và lịch sử commit cũng cho thấy ai đã làm phần nào.</em></p>
        <p><strong>Mục tiêu:</strong> Ghép được các hàm của thành viên thành chương trình hoàn chỉnh và kiểm thử tích hợp với dữ liệu thường, biên và sai; lưu được mã nguồn lên GitHub bằng các thao tác cơ bản (tạo repository, commit, push); viết được README và kịch bản demo.</p>
        <p><strong>Nội dung:</strong></p>
        <ul>
            <li><strong>Ý chính 1 - Ghép code và kiểm thử tích hợp:</strong> danh sách kiểm thử theo từng chức năng.</li>
            <li><strong>Ý chính 2 - GitHub cơ bản:</strong> repository, clone, commit, push bằng GitHub Desktop; thông điệp commit rõ ràng.</li>
            <li><strong>Ý chính 3 - README.md:</strong> giới thiệu dự án, cách chạy, thành viên và vai trò, khai báo dùng AI.</li>
            <li><strong>Ý chính 4 - Rà soát cùng AI và kịch bản demo:</strong> AI góp ý, từng thành viên giải thích được phần mình.</li>
        </ul>
        <p><strong>Kết quả cần đạt:</strong> Repository của nhóm trên GitHub có mã nguồn chạy được, lịch sử commit của mọi thành viên, README hoàn chỉnh và bản nháp kịch bản demo.</p>
        <p style="margin-bottom: 0;"><strong>CLO liên quan:</strong> CLO1, CLO3.</p>
    </div>
</details>

<details style="border: 1px solid #fd7e14; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #fff5eb; color: #fd7e14; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📚 2. Học liệu chính</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.1. Ghép code và kiểm thử tích hợp</h3>
            <p>Mỗi hàm chạy đúng khi thử riêng chưa chắc chạy đúng khi ghép. <strong>Kiểm thử tích hợp</strong> là chạy cả chương trình qua menu, theo từng chức năng, với 5 loại dữ liệu:</p>
            <table style="width: 100%; border-collapse: collapse; font-size: 14px;">
                <thead><tr style="background-color: #fff5eb;"><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Loại dữ liệu</th><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Ví dụ với chức năng "Thêm khoản chi"</th></tr></thead>
                <tbody>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;">Bình thường</td><td style="padding: 8px; border: 1px solid #ffd6ad;">50000, danh mục "Ăn uống"</td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;">Giá trị biên</td><td style="padding: 8px; border: 1px solid #ffd6ad;">1 đồng; đúng bằng ngân sách còn lại</td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;">Sai kiểu</td><td style="padding: 8px; border: 1px solid #ffd6ad;">"năm mươi nghìn", để trống</td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;">Ngoài khoảng</td><td style="padding: 8px; border: 1px solid #ffd6ad;">-20000, 0</td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;">Chưa có dữ liệu</td><td style="padding: 8px; border: 1px solid #ffd6ad;">chọn Thống kê khi danh sách còn rỗng</td></tr>
                </tbody>
            </table>
            <p style="margin: 10px 0 0 0;">Ghi kết quả vào bảng kiểm thử (dữ liệu, mong đợi, thực tế, đạt/chưa đạt). Lỗi tìm được giao lại cho người viết hàm đó sửa; đây là lúc lời chú thích và docstring ở bài 09 phát huy tác dụng.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.2. GitHub cơ bản</h3>
            <ul>
                <li><strong>Git</strong> lưu lịch sử thay đổi của mã nguồn; <strong>GitHub</strong> (github.com) là nơi lưu repository trên mạng để cả nhóm dùng chung.</li>
                <li><strong>Repository</strong> (repo): thư mục dự án có lịch sử. <strong>Commit</strong>: một lần lưu thay đổi kèm thông điệp. <strong>Push</strong>: đẩy các commit lên GitHub. <strong>Pull</strong>: lấy thay đổi mới của bạn cùng nhóm về máy.</li>
            </ul>
            <p style="margin: 0 0 6px 0;"><strong>Các bước với GitHub Desktop</strong> (desktop.github.com):</p>
            <ol>
                <li>Trưởng nhóm tạo repository trên github.com (tick <em>Add a README file</em>), vào <em>Settings → Collaborators</em> mời các thành viên.</li>
                <li>Mỗi thành viên mở GitHub Desktop, <em>File → Clone repository</em>, chọn repo của nhóm.</li>
                <li>Mở thư mục bằng VS Code, viết code phần mình.</li>
                <li>Quay lại GitHub Desktop: bấm <em>Fetch/Pull origin</em> để lấy code mới nhất, ghi thông điệp ở ô <em>Summary</em>, bấm <em>Commit to main</em>, rồi <em>Push origin</em>.</li>
            </ol>
            <p style="margin-bottom: 0;"><strong>Thông điệp commit</strong> nói rõ đã làm gì: <code>Thêm hàm thong_ke_theo_danh_muc</code>, <code>Sửa lỗi chia cho 0 khi chưa có khoản chi</code>. Tránh <code>update</code>, <code>sửa</code>, <code>final</code>. Mỗi người commit phần mình phụ trách: lịch sử commit là minh chứng cho CLO3. Lệnh Git trong Terminal (<code>git add</code>, <code>git commit -m "..."</code>, <code>git push</code>) làm cùng việc, bạn sẽ học kỹ ở các học phần sau.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.3. README.md</h3>
            <p>README là trang đầu tiên người khác thấy khi mở repository. Viết bằng Markdown (<code>#</code> tiêu đề, <code>-</code> gạch đầu dòng, <code>![mô tả](docs/anh.png)</code> chèn ảnh):</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code># Quản lý chi tiêu sinh viên

Chương trình dòng lệnh ghi lại và thống kê chi tiêu cá nhân.

## Thành viên và vai trò
- Nguyễn Văn A: nhap_lieu.py, chức năng Thêm khoản chi
- Trần Thị B: chức năng Thống kê, lưu đồ
- ...

## Cách chạy
Python 3.10+. Mở thư mục dự án, chạy: python main.py

## Ảnh chụp màn hình
![Menu chính](docs/menu.png)

## Khai báo sử dụng AI
Dùng ChatGPT để brainstorm chức năng và giải thích lỗi; chi tiết trong NHAT-KY-PROMPT.md.</code></pre>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.4. Rà soát cùng AI và kịch bản demo</h3>
            <p style="margin: 0 0 8px 0; padding: 8px 10px; background-color: #fff; border-left: 4px solid #fd7e14;"><em>"Đây là chương trình Python của nhóm sinh viên năm nhất (dán code). Liệt kê các trường hợp nhập liệu có thể làm chương trình dừng hoặc cho kết quả sai, kèm số dòng. Không viết lại code."</em></p>
            <p><strong>Kịch bản demo</strong> 3 phút: chức năng nào chạy trước, dùng dữ liệu nào (chuẩn bị sẵn để không phải nghĩ khi đứng trước lớp), cố ý nhập sai một lần để cho thấy chương trình không dừng.</p>
            <p style="margin-bottom: 0;"><strong>Tập vấn đáp trong nhóm:</strong> mỗi người hỏi người khác 2 câu về phần không phải của mình. Nếu cả nhóm chỉ một người hiểu toàn bộ code, buổi Showcase sẽ lộ ra ngay.</p>
        </div>

        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📄 Slide &amp; video bài giảng</p>
            <a href="{{LINK_SLIDE_BAI_11}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📄 Slide Bài 11: Hoàn thiện project và quản lý mã nguồn với GitHub</span>
            </a>
            <a class="nomediaplugin" href="{{LINK_VIDEO_BAI_11}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🎥 Video: tạo repository, clone, commit và push bằng GitHub Desktop</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📖 Tài liệu đọc thêm (chính thức)</p>
            <a href="https://docs.github.com/en/desktop" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 GitHub Desktop Documentation</span><br>
                <span style="color: #6c757d; font-size: 13px;">Clone, commit, push, pull bằng giao diện đồ họa.</span>
            </a>
            <a href="https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 GitHub Docs – Basic writing and formatting syntax</span><br>
                <span style="color: #6c757d; font-size: 13px;">Cú pháp Markdown để viết README.</span>
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
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🧑‍🏫 Thực hành có hướng dẫn (1 tiết): repository của nhóm</strong></p>
            <ol style="margin: 0; color: #495057;">
                <li>Trưởng nhóm tạo repository, mời thành viên; mọi người clone về máy.</li>
                <li>Mỗi người thêm một dòng tên mình vào README, commit, push; lần lượt pull để thấy thay đổi của nhau.</li>
                <li>Đưa các file <code>.py</code>, thư mục <code>docs/</code> (lưu đồ) lên repository.</li>
            </ol>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">👥 Làm việc nhóm (2,5 tiết): ghép, kiểm thử, hoàn thiện</strong></p>
            <ul style="margin: 0 0 6px 0; color: #495057;">
                <li>Ghép code; chạy kiểm thử tích hợp với 5 loại dữ liệu cho từng chức năng; sửa lỗi và commit.</li>
                <li>Cập nhật lưu đồ cho khớp code; chạy <code>ruff check</code>.</li>
                <li>Viết README theo mẫu mục 2.3; viết kịch bản demo; tập vấn đáp chéo.</li>
            </ul>
            <p style="margin: 0 0 8px 0; color: #495057;"><strong>Nộp:</strong> link repository, bảng kiểm thử tích hợp, bản nháp kịch bản demo. <strong>Hoàn thành khi:</strong> mỗi thành viên có ít nhất 2 commit có nội dung code; không dữ liệu xấu nào trong bảng kiểm thử làm chương trình dừng.</p>
            <a href="{{LINK_NOP_BAI_11}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp link repository</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">💬 Diễn đàn thảo luận</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">Khi ghép code, nhóm bạn gặp lỗi gì mà lúc thử riêng từng hàm không thấy? Nguyên nhân là gì (đặt tên khác nhau, kiểu dữ liệu trả về khác nhau, thiếu kiểm tra list rỗng…)?</p>
            <a href="{{LINK_DIEN_DAN_BAI_11}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Tham gia diễn đàn</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">📝 Trắc nghiệm nhanh (Quiz)</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">10 câu ôn tập: kiểm thử tích hợp, khái niệm Git và GitHub, thông điệp commit, README.</p>
            <a href="{{LINK_QUIZ_BAI_11}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Làm bài Quiz Bài 11</a>
        </div>
    </div>
</details>

<details style="border: 1px solid #6f42c1; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #f3e5f5; color: #6f42c1; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>🆘 4. Góc trợ giúp và mở rộng</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>Push bị từ chối (rejected):</strong> trên GitHub đã có commit mới của bạn khác. Bấm <em>Pull origin</em> trước rồi push lại.</p>
        <p><strong>Xung đột (conflict):</strong> hai người sửa cùng một đoạn trong cùng một file. GitHub Desktop sẽ báo file xung đột; mở bằng VS Code, chọn giữ phần nào (<em>Accept Current/Incoming/Both</em>), lưu, rồi commit. Cách phòng tránh: mỗi người làm ở file hoặc hàm riêng như bảng phân công.</p>
        <p><strong>Không thấy nút Push:</strong> chưa được trưởng nhóm thêm vào Collaborators, hoặc chưa đăng nhập GitHub trong GitHub Desktop.</p>
        <p><strong>Kiến thức mở rộng:</strong> nhánh (branch) và Pull Request để review code trước khi ghép; file <code>.gitignore</code> để bỏ qua thư mục <code>__pycache__</code>.</p>
        <p style="margin-bottom: 0;"><strong>Tự đánh giá:</strong> Mở tab <em>History</em> trong GitHub Desktop: nhìn lịch sử commit, người ngoài có biết ai làm phần nào không?</p>
    </div>
</details>
