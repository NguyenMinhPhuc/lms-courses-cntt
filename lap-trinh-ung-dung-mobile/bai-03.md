<details open="" style="border: 1px solid #007bff; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #e7f1ff; color: #007bff; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📘 1. Tổng quan bài học</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>BÀI 03 - Điều hướng với Expo Router (5 tiết: 1 LT / 4 TH)</strong></p>
        <p><em>Trên web, người dùng bấm link và thanh địa chỉ đổi URL. Trên điện thoại không có thanh địa chỉ, nhưng có nút Back, có thanh tab và có cử chỉ vuốt. Ứng dụng của bạn nên tổ chức các màn hình thế nào để người dùng không bị "lạc"?</em></p>
        <p><strong>Mục tiêu:</strong> Giải thích được mô hình điều hướng trên mobile (stack, tab, modal); xây dựng được điều hướng theo file bằng Expo Router; phác thảo được sơ đồ luồng màn hình và ERD sơ bộ từ các chức năng.</p>
        <p><strong>Nội dung:</strong></p>
        <ul>
            <li><strong>Ý chính 1 - Điều hướng trên mobile:</strong> stack lịch sử màn hình, nút Back của Android, tab, modal.</li>
            <li><strong>Ý chính 2 - Expo Router:</strong> mỗi file trong <code>app/</code> là một màn hình; <code>_layout.tsx</code> khai báo Stack hoặc Tabs; nhóm route <code>(tabs)</code>.</li>
            <li><strong>Ý chính 3 - Route động và tham số:</strong> <code>[id].tsx</code>, <code>useLocalSearchParams</code>, chuyển màn hình bằng <code>Link</code> và <code>router</code>, deep link.</li>
            <li><strong>Ý chính 4 - Từ màn hình đến dữ liệu:</strong> mỗi màn hình cần thực thể nào; phác ERD sơ bộ làm đầu vào cho thiết kế CSDL SQL Server ở bài 05.</li>
        </ul>
        <p><strong>Kết quả cần đạt:</strong> Ứng dụng có đủ điều hướng với dữ liệu giả, nút Back của Android hoạt động đúng; nhóm hoàn thành <strong>Checkpoint Sprint 1</strong> kèm sơ đồ luồng màn hình và ERD sơ bộ.</p>
        <p style="margin-bottom: 0;"><strong>CLO liên quan:</strong> CLO1, CLO2, CLO3.</p>
    </div>
</details>

<details style="border: 1px solid #fd7e14; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #fff5eb; color: #fd7e14; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📚 2. Học liệu chính</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.1. Điều hướng trên mobile khác web thế nào?</h3>
            <ul>
                <li><strong>Stack:</strong> màn hình mới được "đặt chồng" lên màn hình cũ. Nút Back của Android hoặc cử chỉ vuốt sẽ gỡ màn hình trên cùng. Ví dụ: Danh sách món → Chi tiết món.</li>
                <li><strong>Tab:</strong> thanh điều hướng cố định ở cuối màn hình cho các khu vực chính. Ví dụ: Trang chủ, Giỏ hàng, Đơn hàng, Tài khoản.</li>
                <li><strong>Modal:</strong> màn hình trượt lên che màn hình hiện tại cho một tác vụ ngắn, đóng xong quay lại đúng chỗ cũ. Ví dụ: xác nhận đặt hàng.</li>
            </ul>
            <p style="margin-bottom: 0;">Một ứng dụng thật thường <strong>lồng</strong> các kiểu này: Stack gốc chứa nhóm Tab, mỗi tab lại có thể mở thêm màn hình chi tiết.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.2. Expo Router: điều hướng theo file</h3>
            <p>Expo Router dùng cấu trúc thư mục <code>app/</code> làm bản đồ điều hướng, tương tự cách Next.js dùng thư mục cho web. Dự án tạo bằng <code>create-expo-app</code> đã có sẵn Expo Router.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>app/
├── _layout.tsx          # Stack gốc của toàn ứng dụng
├── (tabs)/
│   ├── _layout.tsx      # Thanh tab
│   ├── index.tsx        # Tab Trang chủ  →  /
│   ├── cart.tsx         # Tab Giỏ hàng   →  /cart
│   ├── orders.tsx       # Tab Đơn hàng   →  /orders
│   └── account.tsx      # Tab Tài khoản  →  /account
├── product/
│   └── [id].tsx         # Chi tiết món   →  /product/12
└── confirm.tsx          # Modal xác nhận →  /confirm</code></pre>
            <p>Tên thư mục trong ngoặc như <code>(tabs)</code> là <strong>nhóm route</strong>: dùng để gom màn hình chung một layout, không xuất hiện trong đường dẫn.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// app/_layout.tsx
import { Stack } from 'expo-router';

export default function RootLayout() {
  return (
    &lt;Stack&gt;
      &lt;Stack.Screen name="(tabs)" options={{ headerShown: false }} /&gt;
      &lt;Stack.Screen name="product/[id]" options={{ title: 'Chi tiết món' }} /&gt;
      &lt;Stack.Screen name="confirm" options={{ presentation: 'modal', title: 'Xác nhận' }} /&gt;
    &lt;/Stack&gt;
  );
}

// app/(tabs)/_layout.tsx
import { Tabs } from 'expo-router';

export default function TabLayout() {
  return (
    &lt;Tabs&gt;
      &lt;Tabs.Screen name="index" options={{ title: 'Trang chủ' }} /&gt;
      &lt;Tabs.Screen name="cart" options={{ title: 'Giỏ hàng' }} /&gt;
      &lt;Tabs.Screen name="orders" options={{ title: 'Đơn hàng' }} /&gt;
      &lt;Tabs.Screen name="account" options={{ title: 'Tài khoản' }} /&gt;
    &lt;/Tabs&gt;
  );
}</code></pre>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.3. Route động, tham số và deep link</h3>
            <p>File <code>product/[id].tsx</code> phục vụ mọi đường dẫn dạng <code>/product/1</code>, <code>/product/2</code>… Màn hình đọc tham số bằng <code>useLocalSearchParams</code>.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// app/product/[id].tsx
import { useLocalSearchParams, router } from 'expo-router';
import { View, Text, Pressable } from 'react-native';

export default function ProductDetail() {
  const { id } = useLocalSearchParams&lt;{ id: string }&gt;();

  return (
    &lt;View&gt;
      &lt;Text&gt;Món số {id}&lt;/Text&gt;
      &lt;Pressable onPress={() =&gt; router.push('/confirm')}&gt;
        &lt;Text&gt;Đặt ngay&lt;/Text&gt;
      &lt;/Pressable&gt;
    &lt;/View&gt;
  );
}

// Từ màn hình danh sách: mở chi tiết món
import { Link } from 'expo-router';
&lt;Link href={`/product/${item.id}`}&gt;Xem chi tiết&lt;/Link&gt;</code></pre>
            <ul style="margin-bottom: 0;">
                <li><code>router.push()</code> thêm màn hình vào stack; <code>router.back()</code> quay lại; <code>router.replace()</code> thay màn hình hiện tại (dùng khi đăng nhập xong, để Back không quay về màn hình đăng nhập).</li>
                <li><strong>Deep link:</strong> khai báo <code>"scheme": "lhufood"</code> trong <code>app.json</code>; khi đó đường dẫn <code>lhufood://product/12</code> mở thẳng màn hình chi tiết món 12. Bài 09 dùng tính năng này để bấm thông báo mở đúng đơn hàng.</li>
            </ul>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.4. Từ màn hình đến dữ liệu: sơ đồ luồng màn hình và ERD sơ bộ</h3>
            <p><strong>Sơ đồ luồng màn hình</strong> vẽ các màn hình và mũi tên chuyển giữa chúng. Nó giúp nhóm thống nhất cấu trúc thư mục <code>app/</code> trước khi viết mã.</p>
            <p>Mỗi màn hình hiển thị hoặc tạo ra dữ liệu. Liệt kê dữ liệu đó, ta có danh sách <strong>thực thể</strong> và <strong>quan hệ</strong>, tức là ERD sơ bộ. Bài 05 sẽ hoàn thiện ERD thành CSDL SQL Server thật và viết stored procedure.</p>
            <table style="width: 100%; border-collapse: collapse; font-size: 14px;">
                <thead><tr style="background-color: #fff5eb;"><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Màn hình LHU Food</th><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Thực thể cần có</th></tr></thead>
                <tbody>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;">Trang chủ, Danh mục</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Danh mục (Categories), Món (Products)</td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;">Giỏ hàng, Xác nhận</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Món, Người dùng (Users)</td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;">Đơn hàng, Chi tiết đơn</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Đơn hàng (Orders), Chi tiết đơn (OrderItems)</td></tr>
                </tbody>
            </table>
            <p style="margin-bottom: 0;"><strong>Quan hệ sơ bộ:</strong> một Danh mục có nhiều Món (1-n); một Người dùng có nhiều Đơn hàng (1-n); Đơn hàng và Món là quan hệ n-n, tách qua bảng Chi tiết đơn. Vẽ bằng dbdiagram.io hoặc draw.io.</p>
        </div>

        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📄 Slide &amp; video bài giảng</p>
            <a href="{{LINK_SLIDE_BAI_03}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📄 Slide Bài 03: Điều hướng với Expo Router</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📖 Tài liệu đọc thêm (chính thức)</p>
            <a href="https://docs.expo.dev/router/introduction/" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Expo Router - Introduction</span><br>
                <span style="color: #6c757d; font-size: 13px;">Điều hướng theo file, layout, Stack, Tabs, route động và deep link.</span>
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
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🧑‍🏫 Thực hành có hướng dẫn (2 tiết): Điều hướng LHU Food</strong></p>
            <ol style="margin: 0; color: #495057;">
                <li>Tổ chức lại thư mục <code>app/</code> theo cây ở mục 2.2; chuyển các màn hình đã làm ở bài 02 vào đúng vị trí.</li>
                <li>Khai báo Stack gốc và thanh 4 tab; thêm biểu tượng cho tab.</li>
                <li>Tạo <code>product/[id].tsx</code>; bấm món ở Trang chủ mở đúng chi tiết món (dữ liệu giả trong <code>data/products.ts</code>).</li>
                <li>Tạo modal <code>confirm.tsx</code> mở từ nút "Đặt ngay"; đóng modal quay lại chi tiết món.</li>
                <li>Kiểm tra nút Back của Android ở từng màn hình.</li>
                <li>Vẽ sơ đồ luồng màn hình và ERD sơ bộ của LHU Food, lưu vào <code>docs/</code>.</li>
            </ol>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">✍️ Thực hành không hướng dẫn (1,5 tiết): Luồng Danh mục</strong></p>
            <p style="margin: 0 0 6px 0; color: #495057;">Thêm luồng <strong>Danh mục → Danh sách món theo danh mục → Chi tiết món</strong>. Danh sách món dùng route động theo mã danh mục và hiển thị tên danh mục trên thanh tiêu đề.</p>
            <p style="margin: 0 0 8px 0; color: #495057;"><strong>Hoàn thành khi:</strong> mở đúng danh sách cho từng danh mục; tiêu đề đổi theo danh mục; nút Back của Android quay lại đúng từng bước; không có màn hình nào bị lặp trong stack.</p>
            <a href="{{LINK_NOP_BAI_03}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp bài</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🏁 Thử thách nhóm: Checkpoint Sprint 1</strong></p>
            <ul style="margin: 0 0 8px 0; color: #495057;">
                <li>Khung ứng dụng của nhóm đủ điều hướng với dữ liệu giả (mock JSON).</li>
                <li>Nộp <strong>sơ đồ luồng màn hình</strong> và <strong>ERD sơ bộ</strong> (file nguồn + ảnh) trong <code>docs/</code>.</li>
                <li>Demo 3 phút trên điện thoại Android; Sprint Review (đã làm gì, còn gì) và Retrospective ngắn (giữ gì, đổi gì ở sprint 2).</li>
            </ul>
            <a href="{{LINK_NOP_CHECKPOINT_1}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp Checkpoint 1</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">💬 Diễn đàn thảo luận</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">Trong ứng dụng của nhóm, màn hình nào nên là tab, màn hình nào nên mở bằng stack, tác vụ nào nên là modal? Giải thích lựa chọn dựa trên cách người dùng sẽ thao tác.</p>
            <a href="{{LINK_DIEN_DAN_BAI_03}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Tham gia diễn đàn</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">📝 Trắc nghiệm nhanh (Quiz)</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">10 câu ôn tập stack/tab/modal, Expo Router, route động, deep link và ERD sơ bộ.</p>
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
        <p><strong>Màn hình mới không hiện:</strong> file phải nằm trong <code>app/</code> và có <code>export default</code> một component. Kiểm tra tên trong <code>Stack.Screen name</code> khớp đúng đường dẫn file.</p>
        <p><strong>Thanh tiêu đề hiện hai lần:</strong> màn hình nằm trong Tabs nhưng Stack gốc cũng hiện header; thêm <code>headerShown: false</code> cho <code>(tabs)</code> ở Stack gốc.</p>
        <p><strong>Back quay về màn hình đăng nhập sau khi đã đăng nhập:</strong> dùng <code>router.replace()</code> thay cho <code>router.push()</code>.</p>
        <p><strong>Kiến thức mở rộng:</strong> Tìm hiểu typed routes của Expo Router để TypeScript báo lỗi khi gõ sai đường dẫn.</p>
        <p style="margin-bottom: 0;"><strong>Tự đánh giá:</strong> Nhìn vào thư mục <code>app/</code> của nhóm, một bạn mới có đoán được ứng dụng có những màn hình nào và đi từ đâu tới đâu không?</p>
    </div>
</details>
