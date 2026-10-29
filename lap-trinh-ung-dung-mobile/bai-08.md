<details open="" style="border: 1px solid #007bff; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #e7f1ff; color: #007bff; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📘 1. Tổng quan bài học</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>BÀI 08 - Tính năng thiết bị: Camera, Ảnh, Vị trí &amp; Bản đồ (5 tiết: 1 LT / 4 TH)</strong></p>
        <p><em>Đây là thứ web app làm không tốt nhưng ứng dụng di động làm rất tự nhiên: chụp ảnh, biết bạn đang ở đâu, chỉ đường tới quầy căn tin gần nhất. Nhưng điện thoại sẽ hỏi người dùng "Cho phép LHU Food truy cập camera?". Nếu họ bấm "Từ chối" thì sao?</em></p>
        <p><strong>Mục tiêu:</strong> Xin và xử lý được quyền truy cập thiết bị; tích hợp được camera, thư viện ảnh và vị trí; tải được ảnh lên API NestJS và lưu thông tin ảnh vào SQL Server qua stored procedure.</p>
        <p><strong>Nội dung:</strong></p>
        <ul>
            <li><strong>Ý chính 1 - Quyền truy cập:</strong> mô hình xin quyền trên Android (và iOS ở phần mở rộng); xin đúng lúc, giải thích lý do, xử lý khi bị từ chối.</li>
            <li><strong>Ý chính 2 - Camera và ảnh:</strong> <code>expo-image-picker</code> chụp/chọn ảnh, nén ảnh; upload <code>multipart/form-data</code> lên NestJS; lưu đường dẫn ảnh qua thủ tục.</li>
            <li><strong>Ý chính 3 - Vị trí và bản đồ:</strong> <code>expo-location</code> lấy vị trí hiện tại; <code>react-native-maps</code> hiển thị điểm; tính khoảng cách.</li>
            <li><strong>Ý chính 4 - Expo Go và development build:</strong> khi nào thư viện native buộc phải dùng development build; cấu hình quyền trong <code>app.json</code>.</li>
        </ul>
        <p><strong>Kết quả cần đạt:</strong> LHU Food đổi được ảnh đại diện bằng camera/thư viện và lưu lên server; có bản đồ các quầy căn tin; nhóm tích hợp được ít nhất một tính năng thiết bị có ý nghĩa với đề tài.</p>
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
            <h3 style="margin-top: 0; color: #fd7e14;">2.1. Quyền truy cập (permission)</h3>
            <p>Camera, thư viện ảnh và vị trí là dữ liệu riêng tư. Hệ điều hành chỉ cho ứng dụng dùng khi <strong>người dùng đồng ý</strong>, và người dùng có thể thu hồi quyền bất cứ lúc nào trong Cài đặt.</p>
            <ul>
                <li><strong>Xin đúng lúc:</strong> chỉ hỏi khi người dùng bấm "Chụp ảnh", không hỏi tất cả quyền ngay lúc mở app.</li>
                <li><strong>Giải thích trước:</strong> một dòng "LHU Food cần camera để chụp ảnh đại diện" giúp người dùng dễ đồng ý hơn.</li>
                <li><strong>Xử lý từ chối:</strong> ứng dụng vẫn chạy bình thường; tính năng đó hiện hướng dẫn mở Cài đặt (<code>Linking.openSettings()</code>).</li>
            </ul>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>import * as ImagePicker from 'expo-image-picker';
import { Alert, Linking } from 'react-native';

async function ensureCameraPermission() {
  const { status, canAskAgain } = await ImagePicker.requestCameraPermissionsAsync();
  if (status === 'granted') return true;
  Alert.alert(
    'Chưa có quyền camera',
    canAskAgain ? 'Bạn cần cho phép camera để chụp ảnh.' : 'Hãy bật quyền camera trong Cài đặt.',
    canAskAgain ? undefined : [{ text: 'Mở Cài đặt', onPress: () =&gt; Linking.openSettings() }, { text: 'Để sau' }],
  );
  return false;
}</code></pre>
            <p style="margin-bottom: 0;">Khai báo lời giải thích quyền trong <code>app.json</code> qua cấu hình plugin của từng thư viện (ví dụ <code>"cameraPermission"</code> của <code>expo-image-picker</code>); lời này hiện trên iOS và được dùng khi build bản cài đặt.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.2. Chụp/chọn ảnh và tải lên server</h3>
            <p>Cài: <code>npx expo install expo-image-picker</code>. Ảnh chụp từ điện thoại có thể vài MB; giảm <code>quality</code> và cho phép cắt ảnh vuông để file nhỏ, tải lên nhanh.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>async function pickAvatar(fromCamera: boolean) {
  if (fromCamera &amp;&amp; !(await ensureCameraPermission())) return;
  const options: ImagePicker.ImagePickerOptions = {
    mediaTypes: ['images'], allowsEditing: true, aspect: [1, 1], quality: 0.6,
  };
  const result = fromCamera
    ? await ImagePicker.launchCameraAsync(options)
    : await ImagePicker.launchImageLibraryAsync(options);
  if (result.canceled) return;
  await uploadAvatar(result.assets[0].uri);
}

async function uploadAvatar(uri: string) {
  const form = new FormData();
  form.append('file', { uri, name: 'avatar.jpg', type: 'image/jpeg' } as any);
  // Gọi fetch trực tiếp, KHÔNG đặt Content-Type: fetch tự thêm boundary cho multipart/form-data
  const res = await fetch(`${process.env.EXPO_PUBLIC_API_URL}/users/me/avatar`, {
    method: 'POST',
    body: form,
    headers: { Authorization: `Bearer ${useAuth.getState().token}` },
  });
  if (!res.ok) throw new Error('Tải ảnh lên thất bại');
}</code></pre>
            <p><strong>Phía NestJS:</strong> dùng <code>FileInterceptor</code> (Multer) nhận file, giới hạn kích thước và loại file, lưu vào thư mục <code>uploads/</code>, rồi gọi thủ tục lưu đường dẫn.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>@UseGuards(AuthGuard)
@Post('me/avatar')
@UseInterceptors(FileInterceptor('file', {
  storage: diskStorage({
    destination: './uploads/avatars',
    filename: (req: any, file, cb) =&gt; cb(null, `${req.user.sub}-${Date.now()}.jpg`),
  }),
  limits: { fileSize: 2 * 1024 * 1024 },                       // tối đa 2 MB
  fileFilter: (_req, file, cb) =&gt; cb(null, /^image\/(jpeg|png)$/.test(file.mimetype)),
}))
async uploadAvatar(@Req() req, @UploadedFile() file: Express.Multer.File) {
  if (!file) throw new BadRequestException('Chỉ nhận ảnh JPEG hoặc PNG');
  const url = `/uploads/avatars/${file.filename}`;
  await this.db.execute('sp_User_UpdateAvatar', {
    UserId: { type: sql.Int, value: req.user.sub },
    AvatarUrl: { type: sql.NVarChar(500), value: url },
  });
  return { avatarUrl: url };
}</code></pre>
            <ul style="margin-bottom: 0;">
                <li>Phục vụ file tĩnh: trong <code>main.ts</code> tạo app kiểu <code>NestExpressApplication</code> và gọi <code>app.useStaticAssets('uploads', { prefix: '/uploads' })</code>.</li>
                <li>CSDL <strong>chỉ lưu đường dẫn</strong> ảnh (cột <code>AvatarUrl NVARCHAR(500)</code>), không lưu nội dung ảnh vào bảng.</li>
                <li>Không tin tên file do app gửi lên; tự đặt tên theo mã người dùng và thời điểm.</li>
            </ul>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.3. Vị trí và bản đồ</h3>
            <p>Cài: <code>npx expo install expo-location react-native-maps</code>.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>import * as Location from 'expo-location';
import MapView, { Marker } from 'react-native-maps';

const { status } = await Location.requestForegroundPermissionsAsync();
if (status === 'granted') {
  const pos = await Location.getCurrentPositionAsync({ accuracy: Location.Accuracy.Balanced });
  setMyLocation(pos.coords);            // { latitude, longitude, accuracy... }
}

&lt;MapView style={{ flex: 1 }} showsUserLocation
  initialRegion={{ latitude: 10.9577, longitude: 106.8426, latitudeDelta: 0.01, longitudeDelta: 0.01 }}&gt;
  {counters.map((c) =&gt; (
    &lt;Marker key={c.id} coordinate={{ latitude: c.lat, longitude: c.lng }} title={c.name} /&gt;
  ))}
&lt;/MapView&gt;</code></pre>
            <ul style="margin-bottom: 0;">
                <li><strong>Chỉ xin quyền vị trí "khi dùng ứng dụng"</strong> (foreground); vị trí nền (background) cần lý do rõ ràng và quy trình duyệt khắt khe hơn trên cửa hàng.</li>
                <li><code>Accuracy.Balanced</code> đủ cho bản đồ khuôn viên và tiết kiệm pin hơn độ chính xác cao nhất.</li>
                <li><strong>Khoảng cách</strong> giữa hai tọa độ tính bằng công thức Haversine; dùng để sắp xếp "quầy gần bạn nhất".</li>
                <li>Tọa độ trong ví dụ chỉ để minh họa; tọa độ thật của các quầy lấy từ bảng <code>Counters</code> qua API.</li>
                <li><strong>Bản cài đặt Android</strong> dùng bản đồ Google cần khai báo Google Maps API key trong <code>app.json</code> (<code>android.config.googleMaps.apiKey</code>); khi chạy thử bằng Expo Go thì chưa cần.</li>
            </ul>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.4. Expo Go và development build</h3>
            <table style="width: 100%; border-collapse: collapse; font-size: 14px;">
                <thead><tr style="background-color: #fff5eb;"><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;"></th><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Expo Go</th><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Development build</th></tr></thead>
                <tbody>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;"><strong>Là gì</strong></td><td style="padding: 8px; border: 1px solid #ffd6ad;">Ứng dụng dùng chung, có sẵn một bộ thư viện native của Expo SDK</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Bản app riêng của dự án, chứa đúng các thư viện native dự án cần</td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;"><strong>Dùng khi</strong></td><td style="padding: 8px; border: 1px solid #ffd6ad;">Thư viện đều thuộc Expo SDK (image-picker, location, maps…)</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Thư viện native ngoài Expo SDK, cần cấu hình native riêng, hoặc thông báo đẩy từ xa</td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;"><strong>Cách tạo</strong></td><td style="padding: 8px; border: 1px solid #ffd6ad;">Tải từ Google Play</td><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>npx expo install expo-dev-client</code> rồi build bằng EAS (tốn một lượt build)</td></tr>
                </tbody>
            </table>
            <p style="margin: 10px 0 0 0;"><strong>Lời khuyên:</strong> ưu tiên thư viện thuộc Expo SDK để tiếp tục dùng Expo Go, tiết kiệm lượt build của tài khoản miễn phí. Trước khi cài một thư viện do AI gợi ý, kiểm tra nó có trong tài liệu Expo hay không.</p>
        </div>

        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📄 Slide &amp; video bài giảng</p>
            <a href="{{LINK_SLIDE_BAI_08}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📄 Slide Bài 08: Camera, Ảnh, Vị trí &amp; Bản đồ</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📖 Tài liệu đọc thêm (chính thức)</p>
            <a href="https://docs.expo.dev/versions/latest/sdk/imagepicker/" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Expo - ImagePicker</span><br>
                <span style="color: #6c757d; font-size: 13px;">Chụp, chọn ảnh và cấu hình quyền.</span>
            </a>
            <a href="https://docs.expo.dev/versions/latest/sdk/location/" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Expo - Location</span><br>
                <span style="color: #6c757d; font-size: 13px;">Xin quyền và lấy vị trí hiện tại.</span>
            </a>
            <a href="https://docs.expo.dev/versions/latest/sdk/map-view/" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Expo - MapView (react-native-maps)</span><br>
                <span style="color: #6c757d; font-size: 13px;">Hiển thị bản đồ, marker và cấu hình API key khi build.</span>
            </a>
            <a href="https://docs.nestjs.com/techniques/file-upload" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 NestJS - File upload</span><br>
                <span style="color: #6c757d; font-size: 13px;">FileInterceptor, giới hạn kích thước và kiểm tra loại file.</span>
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
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🧑‍🏫 Thực hành có hướng dẫn (2 tiết): Ảnh đại diện &amp; bản đồ căn tin</strong></p>
            <ol style="margin: 0; color: #495057;">
                <li>Thêm cột <code>AvatarUrl</code> vào <code>Users</code>, viết <code>sp_User_UpdateAvatar</code>; endpoint upload và phục vụ file tĩnh trong NestJS.</li>
                <li>Tab Tài khoản: bấm ảnh đại diện → chọn "Chụp ảnh" hoặc "Chọn từ thư viện" → cắt vuông → tải lên → hiển thị ảnh mới.</li>
                <li>Thử từ chối quyền camera rồi bấm lại: app hiện hướng dẫn mở Cài đặt, không bị treo.</li>
                <li>Tạo bảng <code>Counters</code> (tên, vĩ độ, kinh độ) và <code>sp_Counter_GetList</code>; màn hình Bản đồ hiện các quầy và vị trí người dùng.</li>
                <li>Sắp xếp danh sách quầy theo khoảng cách tới vị trí hiện tại.</li>
            </ol>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">✍️ Thực hành không hướng dẫn (1,5 tiết): Báo cáo sự cố</strong></p>
            <p style="margin: 0 0 6px 0; color: #495057;">Chức năng "Báo cáo sự cố" (ví dụ: món ăn có vấn đề, bàn ăn hỏng): chụp ảnh, tự lấy vị trí hiện tại, nhập mô tả, gửi lên API; API lưu ảnh và gọi <code>sp_Incident_Create</code> lưu mô tả, tọa độ, đường dẫn ảnh, người gửi.</p>
            <p style="margin: 0 0 8px 0; color: #495057;"><strong>Hoàn thành khi:</strong> chạy được trên máy Android thật; từ chối quyền camera hoặc vị trí thì vẫn gửi được (bỏ trống phần tương ứng) và có thông báo rõ ràng; ảnh lớn hơn 2 MB bị API từ chối với thông báo dễ hiểu.</p>
            <a href="{{LINK_NOP_BAI_08}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp bài</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">👥 Thử thách nhóm (0,5 tiết + ở nhà)</strong></p>
            <ul style="margin: 0; color: #495057;">
                <li>Tích hợp ít nhất <strong>một tính năng thiết bị</strong> có ý nghĩa với nghiệp vụ của đề tài (camera, ảnh, vị trí, bản đồ…), không làm "cho có".</li>
                <li>Ghi trong README: tính năng dùng quyền gì, xin quyền lúc nào, xử lý thế nào khi bị từ chối.</li>
                <li>Cập nhật ERD và danh mục thủ tục nếu có bảng/thủ tục mới.</li>
            </ul>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">💬 Diễn đàn thảo luận</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">Bạn từng từ chối cấp quyền cho ứng dụng nào? Vì sao? Từ trải nghiệm đó, ứng dụng của nhóm nên xin quyền như thế nào để người dùng tin tưởng?</p>
            <a href="{{LINK_DIEN_DAN_BAI_08}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Tham gia diễn đàn</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">📝 Trắc nghiệm nhanh (Quiz)</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">10 câu ôn tập quyền truy cập, camera, upload ảnh, vị trí, bản đồ và development build.</p>
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
        <p><strong>Upload báo lỗi "Network request failed" hoặc API không nhận file:</strong> thường do tự đặt header <code>Content-Type: multipart/form-data</code> mà thiếu boundary. Để fetch tự đặt header; tên trường trong <code>form.append('file', …)</code> phải trùng với <code>FileInterceptor('file')</code>.</p>
        <p><strong>Ảnh đại diện không hiện sau khi tải lên:</strong> đường dẫn trả về là đường dẫn tương đối; ghép với <code>EXPO_PUBLIC_API_URL</code> khi hiển thị, và kiểm tra đã bật phục vụ file tĩnh.</p>
        <p><strong>Emulator không có vị trí:</strong> trong Android Emulator mở Extended controls → Location để đặt tọa độ giả.</p>
        <p><strong>Kiến thức mở rộng:</strong> Tìm hiểu <code>expo-image-manipulator</code> để thu nhỏ ảnh trước khi gửi, và lưu ảnh lên dịch vụ lưu trữ đối tượng thay vì thư mục trên server.</p>
        <p style="margin-bottom: 0;"><strong>Tự đánh giá:</strong> Ứng dụng của nhóm có màn hình nào vẫn hoạt động được khi người dùng từ chối mọi quyền không? Nếu không, đó là dấu hiệu cần thiết kế lại.</p>
    </div>
</details>
