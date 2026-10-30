<details open="" style="border: 1px solid #007bff; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #e7f1ff; color: #007bff; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📘 1. Tổng quan bài học</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>BÀI 02 - Core Components, Styling &amp; Layout với Flexbox (5 tiết: 1 LT / 4 TH)</strong></p>
        <p><em>Bản Figma của nhóm ở môn UI/UX đã đẹp. Làm thế nào để màn hình trên điện thoại giống bản thiết kế, và vẫn hiển thị đúng trên máy màn hình nhỏ lẫn máy màn hình lớn?</em></p>
        <p><strong>Mục tiêu:</strong> Sử dụng được các core component; xây dựng được giao diện responsive bằng Flexbox; chuyển được thiết kế Figma thành component tái sử dụng; trình bày được sơ đồ chức năng của ứng dụng bằng công cụ đồ họa.</p>
        <p><strong>Nội dung:</strong></p>
        <ul>
            <li><strong>Ý chính 1 - Core components:</strong> <code>View</code>, <code>Text</code>, <code>Image</code>, <code>ScrollView</code>, <code>TextInput</code>, <code>Pressable</code> và vùng an toàn (safe area).</li>
            <li><strong>Ý chính 2 - Flexbox trên mobile:</strong> mặc định xếp theo cột, <code>flex</code>, căn chỉnh, kích thước theo màn hình với <code>useWindowDimensions</code>.</li>
            <li><strong>Ý chính 3 - Design system:</strong> màu, cỡ chữ, khoảng cách tập trung trong <code>theme.ts</code>; component dùng chung <code>Button</code>, <code>Card</code>, <code>Input</code>.</li>
            <li><strong>Ý chính 4 - Từ Figma đến mã bằng vibe coding:</strong> đưa ảnh thiết kế và đặc tả cho AI, so sánh kết quả với thiết kế rồi chỉnh sửa; vẽ sơ đồ chức năng của ứng dụng.</li>
        </ul>
        <p><strong>Kết quả cần đạt:</strong> Sinh viên dựng được màn hình theo thiết kế, hiển thị đúng trên 2 kích thước màn hình Android; nhóm có UI kit và sơ đồ chức năng.</p>
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
            <h3 style="margin-top: 0; color: #fd7e14;">2.1. Các core component thường dùng</h3>
            <table style="width: 100%; border-collapse: collapse; font-size: 14px;">
                <thead><tr style="background-color: #fff5eb;"><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Component</th><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Dùng để</th><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Lưu ý</th></tr></thead>
                <tbody>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>View</code></td><td style="padding: 8px; border: 1px solid #ffd6ad;">Khung chứa, bố cục</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Không cuộn được</td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>Text</code></td><td style="padding: 8px; border: 1px solid #ffd6ad;">Hiển thị chữ</td><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>numberOfLines</code> để cắt chữ dài</td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>Image</code></td><td style="padding: 8px; border: 1px solid #ffd6ad;">Ảnh trong <code>assets/</code> hoặc từ URL</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Ảnh từ URL phải có <code>width</code>/<code>height</code></td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>ScrollView</code></td><td style="padding: 8px; border: 1px solid #ffd6ad;">Nội dung dài, cuộn được</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Không dùng cho danh sách dài (bài 04 dùng <code>FlatList</code>)</td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>TextInput</code></td><td style="padding: 8px; border: 1px solid #ffd6ad;">Ô nhập liệu</td><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>keyboardType</code>, <code>secureTextEntry</code></td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>Pressable</code></td><td style="padding: 8px; border: 1px solid #ffd6ad;">Vùng bấm được</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Đổi style khi đang bấm qua <code>({ pressed })</code></td></tr>
                </tbody>
            </table>
            <p style="margin-bottom: 0;"><strong>Vùng an toàn (safe area):</strong> điện thoại có tai thỏ, thanh trạng thái và thanh điều hướng. Dùng <code>SafeAreaView</code> của thư viện <code>react-native-safe-area-context</code> (đã có sẵn trong dự án Expo) để nội dung không bị che.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.2. Flexbox trên mobile</h3>
            <ul>
                <li><strong>Khác web:</strong> mặc định <code>flexDirection: 'column'</code> (xếp dọc). Muốn xếp ngang phải ghi <code>flexDirection: 'row'</code>.</li>
                <li><strong><code>flex: 1</code>:</strong> chiếm phần không gian còn lại. Màn hình gốc thường có <code>flex: 1</code> để phủ kín.</li>
                <li><strong>Căn chỉnh:</strong> <code>justifyContent</code> theo trục chính, <code>alignItems</code> theo trục phụ; <code>gap</code> tạo khoảng cách giữa các phần tử con.</li>
                <li><strong>Đơn vị:</strong> số không có đơn vị là <strong>dp</strong> (điểm độc lập mật độ), tự co giãn theo mật độ điểm ảnh của máy.</li>
                <li><strong>Theo kích thước màn hình:</strong> <code>useWindowDimensions()</code> trả về chiều rộng hiện tại để đổi số cột, cỡ ảnh.</li>
            </ul>
            <p style="margin: 0 0 6px 0;"><strong>💡 Ví dụ:</strong> lưới món ăn 2 cột trên máy nhỏ, 3 cột trên máy rộng.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>import React from 'react';
import { View, useWindowDimensions, StyleSheet } from 'react-native';

export function ProductGrid({ children }) {
  const { width } = useWindowDimensions();
  const columns = width &gt;= 600 ? 3 : 2;
  const itemWidth = (width - 16 * (columns + 1)) / columns;

  return (
    &lt;View style={styles.grid}&gt;
      {React.Children.map(children, (child) =&gt; (
        &lt;View style={{ width: itemWidth }}&gt;{child}&lt;/View&gt;
      ))}
    &lt;/View&gt;
  );
}

const styles = StyleSheet.create({
  grid: { flexDirection: 'row', flexWrap: 'wrap', gap: 16, padding: 16 },
});</code></pre>
            <p style="margin-bottom: 0;">Bài 04 sẽ thay lưới này bằng <code>FlatList</code> với thuộc tính <code>numColumns</code>, phù hợp hơn khi danh sách dài.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.3. Design system: theme và component dùng chung</h3>
            <p>Không viết màu <code>'#013D88'</code> rải rác ở 20 file. Gom về một chỗ để đổi một lần là cả app đổi theo, và để AI sinh mã đúng màu của nhóm.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// constants/theme.ts
export const colors = {
  primary: '#013D88',
  accent: '#FFC627',
  text: '#212529',
  muted: '#6C757D',
  background: '#F8F9FA',
};
export const spacing = { xs: 4, sm: 8, md: 16, lg: 24 };
export const fontSize = { body: 16, title: 20, heading: 24 };</code></pre>
            <p style="margin-bottom: 0;">Từ theme, xây các component dùng chung: <code>Button</code> (biến thể chính/phụ, trạng thái vô hiệu), <code>Card</code>, <code>Input</code> (có nhãn và dòng báo lỗi). <strong>Dark mode:</strong> <code>useColorScheme()</code> cho biết máy đang ở chế độ sáng hay tối để chọn bảng màu tương ứng.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.4. Từ Figma đến mã bằng vibe coding</h3>
            <ol>
                <li>Xuất ảnh màn hình từ Figma và ghi đặc tả: thành phần nào, dữ liệu mẫu nào, bấm vào đâu thì làm gì.</li>
                <li>Prompt cho Antigravity/Copilot: <em>"Dựng màn hình Chi tiết món theo ảnh đính kèm. Dùng màu và khoảng cách trong constants/theme.ts, dùng component Button có sẵn, không thêm thư viện mới."</em></li>
                <li>Chạy thử, <strong>đặt cạnh ảnh thiết kế</strong> để so: khoảng cách, cỡ chữ, màu, căn lề.</li>
                <li>Sửa chỗ lệch; tách phần lặp lại thành component; ghi prompt và nhận xét vào <code>PROMPTS.md</code>.</li>
            </ol>
            <p style="margin-bottom: 0;"><strong>Lỗi AI hay mắc:</strong> viết cứng màu thay vì lấy từ theme, dùng thư viện UI ngoài không được phép, đặt chữ ngoài <code>&lt;Text&gt;</code>, quên safe area.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.5. Sơ đồ chức năng của ứng dụng</h3>
            <p><strong>Sơ đồ chức năng</strong> (sơ đồ phân rã chức năng) chia ứng dụng thành các nhóm chức năng và chức năng con. Đây là bước đầu để thiết kế màn hình, API và dữ liệu, đồng thời là minh chứng cho CLO1 và CLO3.</p>
            <p style="margin: 0 0 6px 0;"><strong>💡 Ví dụ LHU Food:</strong></p>
            <ul style="margin-bottom: 0;">
                <li><strong>Khách hàng:</strong> xem thực đơn, xem chi tiết món, quản lý giỏ hàng, đặt hàng, theo dõi đơn, nhận thông báo.</li>
                <li><strong>Nhân viên căn tin:</strong> xem đơn mới, cập nhật trạng thái đơn, quản lý món, xem thống kê.</li>
                <li><strong>Tài khoản:</strong> đăng ký, đăng nhập, cập nhật hồ sơ, đăng xuất.</li>
            </ul>
        </div>

        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📄 Slide &amp; video bài giảng</p>
            <a href="{{LINK_SLIDE_BAI_02}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📄 Slide Bài 02: Core Components, Styling &amp; Flexbox</span>
            </a>
            <a href="{{LINK_FIGMA_LHU_FOOD}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🎨 File Figma mẫu LHU Food</span><br>
                <span style="color: #6c757d; font-size: 13px;">Thiết kế màn hình Trang chủ, Chi tiết món và Hồ sơ dùng cho phần thực hành.</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📚 Giáo trình &amp; tài liệu dự án</p>
            <a href="{{LINK_GIAO_TRINH}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📘 Giáo trình nội bộ – Chương 2: Core Components, Styling và Layout với Flexbox</span><br>
                <span style="color: #6c757d; font-size: 13px;">Lý thuyết chi tiết, mã nguồn LHU Food và bài tập hướng dẫn theo dự án ở cuối Chương 2 (file Word).</span>
            </a>
            <a href="{{LINK_SRS_LHU_FOOD}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🧾 SRS dự án LHU Food</span><br>
                <span style="color: #6c757d; font-size: 13px;">Đọc SRS mục 4.2 (US-G01, US-G03 và tiêu chí chấp nhận ở 4.7), mục 5.1 (danh sách module), mục 5.14.1. User story của buổi: US-G01, US-G03 (phần giao diện).</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📖 Tài liệu đọc thêm (chính thức)</p>
            <a href="https://reactnative.dev/docs/flexbox" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 React Native - Layout with Flexbox</span><br>
                <span style="color: #6c757d; font-size: 13px;">Các thuộc tính Flexbox và ví dụ chạy trực tiếp.</span>
            </a>
            <a href="https://reactnative.dev/docs/style" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 React Native - Style</span><br>
                <span style="color: #6c757d; font-size: 13px;">Cách viết style và <code>StyleSheet</code>.</span>
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
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🧑‍🏫 Thực hành có hướng dẫn (2 tiết): Giao diện LHU Food</strong></p>
            <ol style="margin: 0; color: #495057;">
                <li>Tạo <code>constants/theme.ts</code> theo mục 2.3.</li>
                <li>Tạo 3 component dùng chung trong <code>components/</code>: <code>Button</code>, <code>Card</code>, <code>ProductCard</code>.</li>
                <li>Dựng màn hình Trang chủ: lời chào, ô tìm kiếm (<code>TextInput</code>), lưới món ăn với dữ liệu mẫu.</li>
                <li>Dựng màn hình Chi tiết món: ảnh lớn, tên, giá, mô tả, nút "Thêm vào giỏ" cố định ở cuối màn hình.</li>
                <li>Dùng Copilot Chat sinh màn hình Chi tiết từ ảnh Figma, sau đó so với thiết kế và sửa.</li>
                <li>Vẽ sơ đồ chức năng LHU Food bằng draw.io; lưu file nguồn và ảnh vào thư mục <code>docs/</code> của repo.</li>
            </ol>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">✍️ Thực hành không hướng dẫn (1,5 tiết): Màn hình Hồ sơ</strong></p>
            <p style="margin: 0 0 6px 0; color: #495057;">Dựng màn hình Hồ sơ người dùng theo ảnh thiết kế được cung cấp: ảnh đại diện tròn, họ tên, email, số điện thoại, danh sách mục cài đặt và nút Đăng xuất.</p>
            <p style="margin: 0 0 8px 0; color: #495057;"><strong>Hoàn thành khi:</strong> dùng màu/khoảng cách từ <code>theme.ts</code>; không bị che bởi tai thỏ; hiển thị đúng trên 2 kích thước màn hình Android (chụp 2 ảnh màn hình nộp kèm).</p>
            <a href="{{LINK_NOP_BAI_02}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp bài</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">👥 Thử thách nhóm (0,5 tiết + ở nhà): UI kit &amp; sơ đồ chức năng</strong></p>
            <ul style="margin: 0; color: #495057;">
                <li>UI kit của nhóm: <code>theme.ts</code> + tối thiểu 5 component dùng chung.</li>
                <li>Giao diện tĩnh của 3 màn hình chính, bám theo bản Figma nhóm đã làm ở môn UI/UX.</li>
                <li><strong>Sơ đồ chức năng</strong> của đề tài (file nguồn + ảnh) trong <code>docs/</code>.</li>
            </ul>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">💬 Diễn đàn thảo luận</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">Đăng một ví dụ AI sinh giao diện chưa đúng thiết kế (ảnh trước và sau khi sửa). Bạn đã thay đổi prompt hay sửa mã thế nào để có kết quả đúng?</p>
            <a href="{{LINK_DIEN_DAN_BAI_02}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Tham gia diễn đàn</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">📝 Trắc nghiệm nhanh (Quiz)</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">10 câu ôn tập core components, Flexbox, theme và sơ đồ chức năng.</p>
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
        <p><strong>Lỗi "Text strings must be rendered within a &lt;Text&gt; component":</strong> có chữ hoặc khoảng trắng nằm trực tiếp trong <code>&lt;View&gt;</code>. Bọc lại bằng <code>&lt;Text&gt;</code>.</p>
        <p><strong>Ảnh từ URL không hiện:</strong> thiếu <code>width</code>/<code>height</code> trong style, hoặc URL dùng <code>http</code> thay vì <code>https</code>.</p>
        <p><strong>Phần tử bị tràn khỏi màn hình:</strong> kiểm tra hướng <code>flexDirection</code>, thêm <code>flexWrap: 'wrap'</code> cho hàng nhiều phần tử, hoặc dùng <code>flex: 1</code> cho phần tử co giãn.</p>
        <p><strong>Kiến thức mở rộng:</strong> Tìm hiểu thuộc tính <code>accessibilityLabel</code> và cách hỗ trợ cỡ chữ lớn của hệ thống.</p>
        <p style="margin-bottom: 0;"><strong>Tự đánh giá:</strong> Khi đổi màu chủ đạo của app, bạn phải sửa bao nhiêu file? Nếu nhiều hơn một, theme của bạn chưa được dùng đúng.</p>
    </div>
</details>
