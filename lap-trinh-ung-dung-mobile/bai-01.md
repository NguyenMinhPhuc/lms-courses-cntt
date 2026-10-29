<details open="" style="border: 1px solid #007bff; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #e7f1ff; color: #007bff; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📘 1. Tổng quan bài học</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>BÀI 01 - Tổng quan phát triển ứng dụng di động &amp; khởi động dự án (5 tiết: 2 LT / 3 TH)</strong></p>
        <p><em>Bạn đã viết được web app bằng React. Vậy cần học thêm gì để cùng một nhóm kỹ năng đó chạy được trên điện thoại Android, và làm sao để AI giúp bạn nhanh hơn mà không làm bạn mất kiểm soát mã nguồn?</em></p>
        <p><strong>Mục tiêu:</strong> So sánh được các hướng phát triển ứng dụng di động; giải thích được kiến trúc React Native và vai trò của Expo; thiết lập được môi trường, quy trình vibe coding và bảng phân vai của nhóm dự án.</p>
        <p><strong>Nội dung:</strong></p>
        <ul>
            <li><strong>Ý chính 1 - Ba hướng phát triển:</strong> Native, cross-platform và PWA; vì sao chọn React Native khi đã biết React.</li>
            <li><strong>Ý chính 2 - Kiến trúc React Native &amp; Expo:</strong> Mã JavaScript điều khiển component native; Expo Go, development build và EAS.</li>
            <li><strong>Ý chính 3 - Từ React web sang React Native:</strong> <code>View</code>/<code>Text</code> thay cho thẻ HTML, <code>StyleSheet</code> thay cho file CSS, <code>onPress</code> thay cho <code>onClick</code>.</li>
            <li><strong>Ý chính 4 - Vibe coding có kiểm soát:</strong> <code>AGENTS.md</code>, prompt có ngữ cảnh, review mã AI sinh ra, ghi <code>PROMPTS.md</code>.</li>
        </ul>
        <p><strong>Kết quả cần đạt:</strong> Sinh viên chạy được ứng dụng Expo đầu tiên trên điện thoại Android, đẩy mã lên GitHub; nhóm có Project Brief, bảng phân vai và repo chung.</p>
        <p style="margin-bottom: 0;"><strong>CLO liên quan:</strong> CLO1, CLO4.</p>
    </div>
</details>

<details style="border: 1px solid #fd7e14; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #fff5eb; color: #fd7e14; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📚 2. Học liệu chính</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.1. Ba hướng phát triển ứng dụng di động</h3>
            <table style="width: 100%; border-collapse: collapse; font-size: 14px;">
                <thead><tr style="background-color: #fff5eb;"><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Hướng</th><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Cách làm</th><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Ưu điểm</th><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Hạn chế</th></tr></thead>
                <tbody>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;"><strong>Native</strong></td><td style="padding: 8px; border: 1px solid #ffd6ad;">Kotlin cho Android, Swift cho iOS</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Truy cập đầy đủ API thiết bị, hiệu năng tốt nhất</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Hai mã nguồn, hai đội phát triển</td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;"><strong>Cross-platform</strong></td><td style="padding: 8px; border: 1px solid #ffd6ad;">React Native, Flutter: một mã nguồn cho nhiều nền tảng</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Viết một lần, chạy Android và iOS; giao diện là component native</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Một số tính năng đặc thù cần thư viện native</td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;"><strong>PWA</strong></td><td style="padding: 8px; border: 1px solid #ffd6ad;">Web app cài được lên màn hình chính</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Dùng lại hoàn toàn kỹ năng web</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Truy cập thiết bị hạn chế, trải nghiệm kém "native" hơn</td></tr>
                </tbody>
            </table>
            <p style="margin-bottom: 0;"><strong>Vì sao chọn React Native?</strong> Bạn đã quen React: component, props, state, hook. React Native giữ nguyên cách tư duy đó, chỉ thay "đích hiển thị" từ trình duyệt sang giao diện native của điện thoại.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.2. React Native hoạt động thế nào? Expo giúp gì?</h3>
            <ul>
                <li><strong>React Native:</strong> mã JavaScript/TypeScript của bạn mô tả giao diện bằng component; React Native chuyển chúng thành <strong>view native</strong> của Android/iOS. Một <code>&lt;Text&gt;</code> trên Android là một <code>TextView</code> thật, không phải một trang web.</li>
                <li><strong>New Architecture:</strong> các phiên bản React Native hiện nay dùng kiến trúc mới (JSI, Fabric, TurboModules), cho phép JavaScript gọi mã native trực tiếp và nhanh hơn.</li>
                <li><strong>Expo:</strong> bộ công cụ và thư viện xây trên React Native, được tài liệu chính thức của React Native khuyến nghị để bắt đầu dự án mới.
                    <ul>
                        <li><strong>Expo Go:</strong> ứng dụng trên điện thoại để chạy thử dự án ngay, không cần build.</li>
                        <li><strong>Development build:</strong> bản app riêng của bạn, dùng khi cần thư viện native mà Expo Go không có.</li>
                        <li><strong>EAS (Build/Update):</strong> dịch vụ build file cài đặt (APK/AAB) và cập nhật ứng dụng qua mạng.</li>
                    </ul>
                </li>
            </ul>
            <p style="margin-bottom: 0;"><strong>💡 Trong học phần:</strong> Android là nền tảng <strong>bắt buộc</strong>; iOS là phần mở rộng. Mỗi sinh viên tự đăng ký <strong>tài khoản Expo miễn phí</strong>. Gói miễn phí giới hạn số lượt build, nên khi phát triển hãy dùng Expo Go, chỉ build APK khi cần nộp.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.3. Từ React web sang React Native</h3>
            <table style="width: 100%; border-collapse: collapse; font-size: 14px; margin-bottom: 10px;">
                <thead><tr style="background-color: #fff5eb;"><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">React web</th><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">React Native</th><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Ghi chú</th></tr></thead>
                <tbody>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>&lt;div&gt;</code></td><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>&lt;View&gt;</code></td><td style="padding: 8px; border: 1px solid #ffd6ad;">Khung chứa, mặc định xếp theo cột</td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>&lt;p&gt;</code>, <code>&lt;span&gt;</code></td><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>&lt;Text&gt;</code></td><td style="padding: 8px; border: 1px solid #ffd6ad;">Mọi chữ <strong>bắt buộc</strong> nằm trong <code>&lt;Text&gt;</code></td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>&lt;img&gt;</code></td><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>&lt;Image&gt;</code></td><td style="padding: 8px; border: 1px solid #ffd6ad;">Ảnh từ mạng cần khai báo kích thước</td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>&lt;button onClick&gt;</code></td><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>&lt;Pressable onPress&gt;</code></td><td style="padding: 8px; border: 1px solid #ffd6ad;">Sự kiện chạm thay cho click chuột</td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;">File CSS, <code>className</code></td><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>StyleSheet.create</code>, <code>style</code></td><td style="padding: 8px; border: 1px solid #ffd6ad;">Viết bằng JavaScript, tên thuộc tính dạng camelCase, không kế thừa như CSS</td></tr>
                </tbody>
            </table>
            <p style="margin: 0 0 6px 0;"><strong>💡 Ví dụ:</strong> thẻ món ăn của LHU Food.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>import { View, Text, Pressable, StyleSheet } from 'react-native';

export function ProductCard({ name, price, onAdd }) {
  return (
    &lt;View style={styles.card}&gt;
      &lt;Text style={styles.name}&gt;{name}&lt;/Text&gt;
      &lt;Text&gt;{price.toLocaleString('vi-VN')} đ&lt;/Text&gt;
      &lt;Pressable style={styles.button} onPress={onAdd}&gt;
        &lt;Text style={styles.buttonText}&gt;Thêm vào giỏ&lt;/Text&gt;
      &lt;/Pressable&gt;
    &lt;/View&gt;
  );
}

const styles = StyleSheet.create({
  card: { padding: 16, borderRadius: 12, backgroundColor: '#fff' },
  name: { fontSize: 18, fontWeight: 'bold' },
  button: { marginTop: 8, padding: 10, borderRadius: 8, backgroundColor: '#013D88' },
  buttonText: { color: '#fff', textAlign: 'center' },
});</code></pre>
            <p style="margin-bottom: 0;">Hãy để ý: cách viết component, props và hàm xử lý giống hệt React web. Thứ thay đổi chỉ là tên component và cách viết style.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.4. Vibe coding có kiểm soát</h3>
            <p><strong>Vibe coding</strong> là cách lập trình trong đó bạn mô tả điều mình muốn bằng ngôn ngữ tự nhiên và để AI (Google Antigravity, GitHub Copilot Chat) sinh mã. AI viết nhanh, nhưng <strong>người chịu trách nhiệm về mã vẫn là bạn</strong>.</p>
            <ol>
                <li><strong>Cho AI ngữ cảnh:</strong> file <code>AGENTS.md</code> (và <code>.github/copilot-instructions.md</code> cho Copilot) mô tả dự án, thư viện được dùng, quy ước đặt tên.</li>
                <li><strong>Prompt cụ thể:</strong> nêu màn hình nào, dữ liệu gì, tiêu chí hoàn thành ra sao.</li>
                <li><strong>Đọc và chạy thử</strong> mã AI sinh ra; sửa chỗ sai thay vì chấp nhận nguyên văn.</li>
                <li><strong>Ghi lại prompt</strong> chính vào <code>PROMPTS.md</code> kèm nhận xét: mã dùng được tới đâu, phải sửa gì.</li>
                <li><strong>Không hiểu thì không merge:</strong> trước khi gộp vào nhánh chính, bạn phải giải thích được từng dòng.</li>
            </ol>
            <p style="margin: 0 0 6px 0;"><strong>💡 Ví dụ <code>AGENTS.md</code> rút gọn:</strong></p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code># LHU Food - Quy ước dự án
- Ứng dụng React Native + Expo, TypeScript, điều hướng bằng Expo Router (thư mục app/).
- Component dùng chung đặt trong components/, mỗi file một component, tên PascalCase.
- Style dùng StyleSheet.create; màu và khoảng cách lấy từ constants/theme.ts.
- Không thêm thư viện mới khi chưa hỏi nhóm.
- Chuỗi hiển thị bằng tiếng Việt có dấu.</code></pre>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.5. Dự án PBL và phân vai trong nhóm</h3>
            <p>Mỗi nhóm 4–5 sinh viên phát triển một ứng dụng suốt 4 sprint. Khuyến khích chọn cùng đề tài với môn Lập trình ứng dụng Web để dùng chung backend NestJS + SQL Server.</p>
            <ul>
                <li><strong>Project Brief (1 trang):</strong> vấn đề cần giải quyết, người dùng, 5–7 tính năng chính, tính năng nào cần realtime.</li>
                <li><strong>Vai trò gợi ý:</strong> mobile UI, mobile logic, backend API, CSDL và stored procedure, kiểm thử và phát hành. Mỗi người có ít nhất một vai chính; nhóm 4 người thì một người kiêm hai vai.</li>
            </ul>
            <p style="margin-bottom: 0;"><strong>💡 Vì sao phân vai rõ từ buổi đầu?</strong> Điểm CLO4 cuối kỳ chấm theo vai trò cá nhân, dựa trên lịch sử commit/PR và phần bạn tự trình bày. Vai trò mơ hồ thì minh chứng cũng mơ hồ.</p>
        </div>

        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📄 Slide &amp; video bài giảng</p>
            <a href="{{LINK_SLIDE_BAI_01}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📄 Slide Bài 01: Tổng quan phát triển ứng dụng di động</span>
            </a>
            <a class="nomediaplugin" href="{{LINK_VIDEO_BAI_01}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">▶ Video 01: Cài đặt môi trường và chạy ứng dụng Expo đầu tiên</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📖 Tài liệu đọc thêm (chính thức)</p>
            <a href="https://reactnative.dev/docs/getting-started" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 React Native - Introduction</span><br>
                <span style="color: #6c757d; font-size: 13px;">Core components và cách React Native hiển thị giao diện native.</span>
            </a>
            <a href="https://docs.expo.dev/get-started/introduction/" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Expo - Get started</span><br>
                <span style="color: #6c757d; font-size: 13px;">Tạo dự án, chạy trên Expo Go và emulator Android.</span>
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
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🧑‍🏫 Thực hành có hướng dẫn (1,5 tiết): Khởi tạo LHU Food</strong></p>
            <ol style="margin: 0 0 8px 0; color: #495057;">
                <li>Kiểm tra Node.js bản LTS: <code>node -v</code>. Cài Expo Go trên điện thoại Android.</li>
                <li>Đăng ký tài khoản Expo miễn phí tại expo.dev.</li>
                <li>Tạo dự án: <code>npx create-expo-app@latest lhu-food</code>, sau đó <code>cd lhu-food</code>.</li>
                <li>Chạy: <code>npx expo start</code>, quét mã QR bằng Expo Go (điện thoại và laptop cùng mạng Wi-Fi).</li>
                <li>Đọc cấu trúc thư mục: <code>app/</code> (màn hình), <code>components/</code>, <code>assets/</code>, <code>app.json</code>, <code>package.json</code>.</li>
                <li>Sửa nội dung màn hình đầu tiên, lưu file và quan sát app cập nhật ngay (Fast Refresh).</li>
                <li>Dùng Antigravity hoặc Copilot Chat viết <code>AGENTS.md</code> từ mô tả dự án; tạo repo GitHub và commit đầu tiên.</li>
            </ol>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">✍️ Thực hành không hướng dẫn (1 tiết): Thẻ giới thiệu bản thân</strong></p>
            <p style="margin: 0 0 6px 0; color: #495057;">Tự tạo một ứng dụng Expo hiển thị thẻ giới thiệu bản thân: ảnh đại diện, họ tên, lớp, 3 kỹ năng, nút "Liên hệ" (bấm vào hiện thông báo bằng <code>Alert</code>).</p>
            <p style="margin: 0 0 8px 0; color: #495057;"><strong>Hoàn thành khi:</strong> chạy được trên điện thoại Android; mã đẩy lên repo GitHub cá nhân; có <code>PROMPTS.md</code> ghi ít nhất 1 prompt đã dùng và nhận xét của bạn.</p>
            <a href="{{LINK_NOP_BAI_01}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp link repo</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">👥 Thử thách nhóm (0,5 tiết + ở nhà): Khởi động dự án</strong></p>
            <ul style="margin: 0; color: #495057;">
                <li>Lập nhóm 4–5 người, chọn đề tài (khuyến khích dùng chung với môn Lập trình ứng dụng Web).</li>
                <li>Viết <strong>Project Brief 1 trang</strong> và <strong>bảng phân vai</strong> (mỗi thành viên ít nhất 1 vai chính).</li>
                <li>Tạo repo nhóm, mời giảng viên; thêm <code>AGENTS.md</code>, <code>.github/copilot-instructions.md</code>, <code>PROMPTS.md</code>.</li>
            </ul>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">💬 Diễn đàn thảo luận</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">Ứng dụng di động nào bạn dùng hằng ngày mà bạn nghĩ có thể viết bằng React Native? Nêu một tính năng của nó cần truy cập phần cứng điện thoại và một tính năng cần dữ liệu thời gian thực.</p>
            <a href="{{LINK_DIEN_DAN_BAI_01}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Tham gia diễn đàn</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">📝 Trắc nghiệm nhanh (Quiz)</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">10 câu ôn tập các hướng phát triển mobile, React Native và Expo, khác biệt với React web và quy tắc vibe coding.</p>
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
        <p><strong>Expo Go không mở được dự án:</strong> kiểm tra điện thoại và laptop cùng một mạng Wi-Fi. Nếu mạng phòng lab chặn kết nối giữa các máy, chạy <code>npx expo start --tunnel</code>.</p>
        <p><strong>Lỗi khi tạo dự án:</strong> dùng Node.js bản LTS; xóa thư mục <code>node_modules</code> rồi chạy lại <code>npm install</code>.</p>
        <p><strong>Không có điện thoại Android:</strong> cài Android Studio, tạo emulator (Device Manager), rồi nhấn phím <code>a</code> trong cửa sổ <code>npx expo start</code>.</p>
        <p><strong>Kiến thức mở rộng:</strong> Đọc phần "Core Components and Native Components" trong tài liệu React Native để hiểu cách một component được ánh xạ thành view native.</p>
        <p style="margin-bottom: 0;"><strong>Tự đánh giá:</strong> Bạn có giải thích được vì sao chữ đặt trực tiếp trong <code>&lt;View&gt;</code> (không bọc <code>&lt;Text&gt;</code>) sẽ gây lỗi không?</p>
    </div>
</details>
