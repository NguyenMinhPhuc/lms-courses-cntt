<details open="" style="border: 1px solid #007bff; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #e7f1ff; color: #007bff; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📘 1. Tổng quan bài học</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>BÀI 11 - Triển khai backend lên server Khoa, build &amp; phát hành ứng dụng (5 tiết: 1 LT / 4 TH)</strong></p>
        <p><em>Đến hôm nay, LHU Food chỉ chạy khi máy của bạn bật và điện thoại cùng mạng Wi-Fi. Sau buổi này, một người không thuộc nhóm cài file APK lên điện thoại của họ, đặt món qua mạng và nhận thông báo realtime từ server của Khoa.</em></p>
        <p><strong>Mục tiêu:</strong> Triển khai được backend NestJS và CSDL SQL Server lên Windows Server của Khoa; cấu hình được ứng dụng theo môi trường; build được APK/AAB bằng EAS Build; phát hành được bản cập nhật OTA và chuẩn bị được hồ sơ phát hành.</p>
        <p><strong>Nội dung:</strong></p>
        <ul>
            <li><strong>Ý chính 1 - Triển khai lên Windows Server:</strong> chạy script CSDL, thủ tục, dữ liệu mẫu; tài khoản SQL chỉ có quyền EXECUTE; <code>.env</code>; chạy API thành dịch vụ nền; mở cổng Windows Firewall; kiểm tra bằng Swagger từ máy khác.</li>
            <li><strong>Ý chính 2 - Cấu hình ứng dụng:</strong> <code>app.config.ts</code>: tên, biểu tượng, splash, package, phiên bản; địa chỉ API và socket theo môi trường.</li>
            <li><strong>Ý chính 3 - EAS Build và EAS Update:</strong> profile <code>preview</code> (APK, bắt buộc) và <code>production</code> (AAB); ký ứng dụng; quản lý lượt build miễn phí; cập nhật OTA; iOS là mở rộng.</li>
            <li><strong>Ý chính 4 - Phát hành và vận hành:</strong> hồ sơ cửa hàng (chính sách quyền riêng tư, ảnh chụp, mô tả); theo dõi log và lỗi sau phát hành.</li>
        </ul>
        <p><strong>Chuẩn bị trước buổi học:</strong> mỗi thành viên đã đăng ký tài khoản Expo miễn phí; nhóm đã nhận thông tin truy cập server (địa chỉ, tài khoản, cổng được cấp) từ bộ phận hỗ trợ triển khai của Khoa.</p>
        <p><strong>Kết quả cần đạt:</strong> API và CSDL của nhóm chạy trên server Khoa; file APK cài trên điện thoại Android của người ngoài nhóm, kết nối được API và socket của server.</p>
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
            <h3 style="margin-top: 0; color: #fd7e14;">2.1. Triển khai CSDL lên SQL Server của Khoa</h3>
            <p>Chạy các script trong thư mục <code>database/</code> (bài 07) <strong>theo thứ tự số</strong> trên một CSDL trống, bằng SQL Server Management Studio hoặc <code>sqlcmd</code>. Script phải chạy lại được nhiều lần (dùng <code>CREATE OR ALTER PROCEDURE</code>, kiểm tra tồn tại trước khi đổi bảng).</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>database/
  01-tables.sql          -- bảng và ràng buộc ban đầu
  02-procedures.sql      -- thủ tục sản phẩm, đơn hàng
  03-auth.sql ... 08-notifications.sql   -- các thay đổi theo từng sprint
  99-seed.sql            -- dữ liệu mẫu (món ăn, tài khoản thử)</code></pre>
            <p>Backend <strong>không</strong> dùng tài khoản quản trị (<code>sa</code>). Tạo một login riêng chỉ được thực thi thủ tục, đúng nguyên tắc "chỉ truy cập dữ liệu qua stored procedure":</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>CREATE LOGIN lhufood_api WITH PASSWORD = N'&lt;mật khẩu mạnh&gt;';
USE LhuFood;
CREATE USER lhufood_api FOR LOGIN lhufood_api;
GRANT EXECUTE ON SCHEMA::dbo TO lhufood_api;   -- không cấp SELECT/INSERT/UPDATE/DELETE trên bảng</code></pre>
            <p style="margin-bottom: 0;">Việc tạo login cấp server có thể do bộ phận hỗ trợ thực hiện; nhóm cung cấp tên CSDL và yêu cầu quyền cần thiết. Kiểm tra: đăng nhập bằng <code>lhufood_api</code>, <code>SELECT * FROM Products</code> phải bị từ chối, còn <code>EXEC sp_Product_GetList</code> chạy được.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.2. Chạy backend NestJS trên Windows Server</h3>
            <ol>
                <li>Lấy mã nguồn từ repo, cài phụ thuộc và build: <code>npm ci</code> rồi <code>npm run build</code> (tạo thư mục <code>dist/</code>).</li>
                <li>Tạo file <code>.env</code> trên server (không commit lên repo):</li>
            </ol>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>PORT=3000
DB_SERVER=localhost
DB_NAME=LhuFood
DB_USER=lhufood_api
DB_PASSWORD=&lt;mật khẩu&gt;
JWT_SECRET=&lt;chuỗi ngẫu nhiên dài, khác với máy phát triển&gt;</code></pre>
            <p>Thư mục <code>uploads/</code> (ảnh tải lên từ bài 08) nằm cạnh mã backend trên server và phải được sao lưu cùng CSDL.</p>
            <ol start="3">
                <li>Chạy thử bằng <code>node dist/main.js</code>; mở Swagger <code>http://localhost:3000/docs</code> trên server.</li>
                <li><strong>Chạy thành dịch vụ nền:</strong> để API tự khởi động lại khi server khởi động lại hoặc khi tiến trình bị lỗi, cài đặt theo hướng dẫn của bộ phận hỗ trợ (ví dụ đăng ký thành Windows Service bằng công cụ quản lý tiến trình mà Khoa sử dụng). Không để API chạy trong một cửa sổ terminal đang mở.</li>
                <li><strong>Mở cổng:</strong> cổng API (và socket, nếu dùng chung cổng thì chỉ một) phải được mở trên Windows Firewall cho kết nối từ ngoài; thường do bộ phận hỗ trợ thực hiện theo yêu cầu của nhóm.</li>
                <li><strong>Kiểm tra từ máy khác:</strong> mở <code>http://&lt;địa-chỉ-server&gt;:&lt;cổng&gt;/docs</code> từ máy của bạn; đăng nhập, gọi API danh sách món, tạo đơn thử.</li>
            </ol>
            <p style="margin-bottom: 0;"><strong>Ghi lại toàn bộ các bước</strong> vào mục "Triển khai trên Windows Server" trong README của repo backend: phiên bản Node.js, thứ tự script, biến môi trường cần có (không ghi giá trị bí mật), cách khởi động lại dịch vụ, cách xem log.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.3. Cấu hình ứng dụng theo môi trường</h3>
            <p>Đổi <code>app.json</code> thành <code>app.config.ts</code> để đọc biến môi trường. Khi phát triển, app gọi API trên máy cá nhân; bản build phát hành gọi server Khoa.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// app.config.ts
import { ExpoConfig } from 'expo/config';

const config: ExpoConfig = {
  name: 'LHU Food',
  slug: 'lhu-food',
  version: '1.0.0',
  icon: './assets/icon.png',
  splash: { image: './assets/splash.png', backgroundColor: '#ffffff' },
  android: {
    package: 'vn.edu.lhu.lhufood',      // duy nhất, không đổi sau khi phát hành
    versionCode: 1,                     // tăng mỗi lần đưa bản mới lên cửa hàng
    adaptiveIcon: { foregroundImage: './assets/adaptive-icon.png', backgroundColor: '#ffffff' },
  },
  extra: { eas: { projectId: '&lt;sinh ra khi chạy eas init&gt;' } },
};
export default config;</code></pre>
            <p>Địa chỉ API đọc từ biến <code>EXPO_PUBLIC_API_URL</code> (bài 05); Socket.IO (bài 09) kết nối cùng địa chỉ và cổng với API. Giá trị cho từng bản build khai báo trong <code>eas.json</code> (mục 2.4).</p>
            <ul style="margin-bottom: 0;">
                <li><strong>HTTP và HTTPS:</strong> Android mặc định chặn kết nối HTTP không mã hóa trong bản build. Nếu server Khoa chỉ cấp HTTP, cần cho phép cleartext cho bản build của đồ án (theo hướng dẫn trong tài liệu Expo về cấu hình Android); khi phát hành thật phải dùng HTTPS.</li>
                <li><strong>Google Maps (bài 08):</strong> bản build cần API key Google Maps cho Android khai báo trong cấu hình; trong Expo Go thì không cần, nên lỗi bản đồ trắng thường chỉ xuất hiện khi chạy APK.</li>
                <li>Biến <code>EXPO_PUBLIC_*</code> được nhúng vào app, ai cũng đọc được: <strong>không</strong> đặt mật khẩu hay khóa bí mật vào đó.</li>
            </ul>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.4. EAS Build</h3>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>npm install -g eas-cli
eas login                 # tài khoản Expo của bạn
eas init                  # gắn dự án với tài khoản, ghi projectId
eas build:configure       # tạo eas.json</code></pre>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// eas.json
{
  "build": {
    "preview": {
      "distribution": "internal",
      "android": { "buildType": "apk" },
      "channel": "preview",
      "env": { "EXPO_PUBLIC_API_URL": "http://&lt;server-khoa&gt;:&lt;cổng&gt;" }
    },
    "production": {
      "android": { "buildType": "app-bundle" },
      "channel": "production",
      "env": { "EXPO_PUBLIC_API_URL": "https://&lt;tên-miền&gt;" }
    }
  }
}</code></pre>
            <ul style="margin-bottom: 0;">
                <li><strong><code>eas build -p android --profile preview</code></strong> (bắt buộc): tạo file <strong>APK</strong>, có link tải và mã QR để cài trực tiếp lên điện thoại.</li>
                <li><strong><code>--profile production</code></strong>: tạo file <strong>AAB</strong> (định dạng Google Play yêu cầu), không cài trực tiếp được.</li>
                <li><strong>Ký ứng dụng:</strong> lần build đầu, EAS đề nghị tạo keystore và lưu trên Expo. Mọi bản cập nhật sau phải ký bằng cùng keystore; mất keystore là không cập nhật được ứng dụng trên cửa hàng.</li>
                <li><strong>Lượt build miễn phí có giới hạn</strong> mỗi tháng và phải xếp hàng chờ. Trước khi build: chạy thử kỹ bằng Expo Go hoặc development build, kiểm tra <code>eas.json</code>, chạy <code>npx expo-doctor</code>. Nhóm nên phân công build từ tài khoản của các thành viên khác nhau.</li>
            </ul>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.5. EAS Update (cập nhật OTA)</h3>
            <p>Sửa lỗi giao diện hoặc logic JavaScript không cần build lại APK. EAS Update gửi gói JavaScript mới; app tải về ở lần mở sau.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>npx expo install expo-updates
eas update:configure
# ... sửa mã ...
eas update --channel preview --message "Sửa lỗi hiển thị tổng tiền"</code></pre>
            <ul style="margin-bottom: 0;">
                <li>Bản cập nhật chỉ đến được các bản build có cùng <strong>channel</strong> và cùng <strong>runtime version</strong>.</li>
                <li><strong>Không</strong> dùng OTA khi thêm thư viện có mã native, đổi quyền, đổi icon hay cấu hình trong <code>app.config.ts</code>: các thay đổi đó bắt buộc build lại.</li>
                <li>Với nhóm dùng tài khoản miễn phí, OTA là cách tiết kiệm lượt build khi sửa lỗi gần ngày Demo.</li>
            </ul>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.6. Hồ sơ phát hành và vận hành sau phát hành</h3>
            <p>Đồ án không bắt buộc đưa lên Google Play (cần tài khoản nhà phát triển trả phí), nhưng nhóm phải chuẩn bị <strong>hồ sơ cửa hàng</strong> như khi phát hành thật:</p>
            <ul>
                <li>Tên ứng dụng, mô tả ngắn (tối đa 80 ký tự) và mô tả đầy đủ.</li>
                <li>Biểu tượng 512×512, ảnh nổi bật (feature graphic), ít nhất 4 ảnh chụp màn hình thật từ điện thoại.</li>
                <li><strong>Chính sách quyền riêng tư:</strong> ứng dụng thu thập dữ liệu gì (tài khoản, vị trí, ảnh), dùng để làm gì, lưu ở đâu (SQL Server của Khoa), người dùng xóa tài khoản thế nào.</li>
                <li>Giải thích lý do xin từng quyền (camera, vị trí, thông báo).</li>
            </ul>
            <p style="margin: 0 0 6px 0;"><strong>Sau phát hành:</strong></p>
            <ul style="margin-bottom: 0;">
                <li>Backend ghi log ra file (request lỗi, exception, thời gian thủ tục chậm); biết vị trí file log trên server.</li>
                <li>Theo dõi lỗi phía app: tối thiểu bắt lỗi toàn cục và gửi về API; mở rộng: dịch vụ theo dõi lỗi như Sentry.</li>
                <li>Mỗi lỗi người dùng báo được ghi vào bug log (bài 10) và sửa bằng EAS Update hoặc bản build mới.</li>
            </ul>
        </div>

        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📄 Slide &amp; video bài giảng</p>
            <a href="{{LINK_SLIDE_BAI_11}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📄 Slide Bài 11: Triển khai, build &amp; phát hành</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📖 Tài liệu đọc thêm (chính thức)</p>
            <a href="https://docs.expo.dev/build/setup/" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Expo - Create your first build</span><br>
                <span style="color: #6c757d; font-size: 13px;">Cài eas-cli, cấu hình eas.json và build Android.</span>
            </a>
            <a href="https://docs.expo.dev/build-reference/apk/" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Expo - Build APKs for Android</span><br>
                <span style="color: #6c757d; font-size: 13px;">Cấu hình profile tạo APK để cài trực tiếp.</span>
            </a>
            <a href="https://docs.expo.dev/eas-update/getting-started/" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Expo - Get started with EAS Update</span><br>
                <span style="color: #6c757d; font-size: 13px;">Channel, runtime version và gửi bản cập nhật.</span>
            </a>
            <a href="https://docs.nestjs.com/techniques/configuration" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 NestJS - Configuration</span><br>
                <span style="color: #6c757d; font-size: 13px;">Đọc biến môi trường từ .env cho từng môi trường.</span>
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
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🧑‍🏫 Thực hành có hướng dẫn (1,5 tiết): Đưa LHU Food lên server</strong></p>
            <ol style="margin: 0; color: #495057;">
                <li>Trên Windows Server mẫu: chạy các script trong <code>database/</code> theo thứ tự, tạo login <code>lhufood_api</code> chỉ có quyền EXECUTE và kiểm tra quyền.</li>
                <li>Build và chạy API với <code>.env</code> của server; mở Swagger từ máy khác.</li>
                <li>Chuyển sang <code>app.config.ts</code>, khai báo <code>eas.json</code> với địa chỉ server; chạy <code>eas build -p android --profile preview</code>.</li>
                <li>Cài APK từ mã QR, tắt Wi-Fi phòng máy (dùng 4G nếu server cho phép truy cập từ ngoài), đăng nhập, đặt món, nhận thông báo realtime khi giảng viên đổi trạng thái đơn.</li>
                <li>Sửa một chữ trên giao diện, gửi <code>eas update</code>, mở lại app để thấy thay đổi.</li>
            </ol>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">✍️ Thực hành không hướng dẫn (1 tiết): Hồ sơ cửa hàng</strong></p>
            <p style="margin: 0 0 6px 0; color: #495057;">Chuẩn bị hồ sơ phát hành cho ứng dụng của nhóm theo mục 2.6: biểu tượng, 4 ảnh chụp màn hình thật, mô tả ngắn, mô tả đầy đủ và chính sách quyền riêng tư.</p>
            <p style="margin: 0 0 8px 0; color: #495057;"><strong>Hoàn thành khi:</strong> nộp thư mục <code>store-listing/</code>; chính sách quyền riêng tư nêu đúng các quyền và dữ liệu mà ứng dụng thực sự thu thập.</p>
            <a href="{{LINK_NOP_BAI_11}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp bài</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">👥 Thử thách nhóm (1,5 tiết + ở nhà)</strong></p>
            <ul style="margin: 0; color: #495057;">
                <li>Phối hợp với bộ phận hỗ trợ, triển khai backend và CSDL SQL Server của nhóm lên Windows Server của Khoa.</li>
                <li>File APK chạy trên điện thoại Android của <strong>một người không thuộc nhóm</strong>, kết nối API và socket trên server Khoa.</li>
                <li>README có mục hướng dẫn triển khai trên Windows Server; hồ sơ cửa hàng; bản nháp báo cáo đồ án.</li>
                <li><strong>Mở rộng:</strong> chạy được trên iOS (TestFlight hoặc development build).</li>
            </ul>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">💬 Diễn đàn thảo luận</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">Lỗi nào chỉ xuất hiện trên bản APK mà không có khi chạy Expo Go? Nhóm bạn tìm ra nguyên nhân bằng cách nào?</p>
            <a href="{{LINK_DIEN_DAN_BAI_11}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Tham gia diễn đàn</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">📝 Trắc nghiệm nhanh (Quiz)</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">10 câu ôn tập triển khai trên Windows Server, cấu hình môi trường, EAS Build, EAS Update và hồ sơ phát hành.</p>
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
        <p><strong>Swagger mở được trên server nhưng máy khác không vào được:</strong> cổng chưa được mở trên Windows Firewall, hoặc API chỉ lắng nghe <code>localhost</code>; trong <code>main.ts</code> dùng <code>app.listen(port, '0.0.0.0')</code>. Báo bộ phận hỗ trợ kèm số cổng.</p>
        <p><strong>API không kết nối được SQL Server:</strong> kiểm tra tên instance, cổng TCP của SQL Server đã bật, mật khẩu trong <code>.env</code>; thông báo "permission denied" khi gọi thủ tục nghĩa là thiếu quyền EXECUTE.</p>
        <p><strong>APK mở lên báo lỗi mạng, Expo Go thì chạy:</strong> app vẫn gọi địa chỉ máy cá nhân (biến môi trường chưa vào bản build) hoặc HTTP bị chặn (xem mục 2.3).</p>
        <p><strong>Bản đồ trắng trong APK:</strong> thiếu hoặc sai API key Google Maps cho Android.</p>
        <p><strong>Hết lượt build miễn phí:</strong> dùng EAS Update cho thay đổi JavaScript; build bằng tài khoản thành viên khác; hoặc build cục bộ (mở rộng, cần Android SDK).</p>
        <p><strong>Kiến thức mở rộng:</strong> Đặt API sau reverse proxy (IIS) với chứng chỉ HTTPS; thiết lập GitHub Actions tự build khi tạo tag phiên bản.</p>
        <p style="margin-bottom: 0;"><strong>Tự đánh giá:</strong> Nếu server Khoa khởi động lại lúc 2 giờ sáng, API của nhóm có tự chạy lại không? Bạn kiểm tra điều đó bằng cách nào?</p>
    </div>
</details>
