<details open="" style="border: 1px solid #007bff; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #e7f1ff; color: #007bff; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📘 1. Tổng quan bài học</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>BÀI 10 - Kiểm thử, gỡ lỗi &amp; tối ưu hiệu năng (5 tiết: 2 LT / 3 TH)</strong></p>
        <p><em>Ứng dụng của nhóm đã "chạy được". Nhưng nếu tuần sau một bạn sửa hàm tính tổng tiền, ai sẽ phát hiện nó tính sai? Và trên chiếc điện thoại Android cũ của giảng viên, danh sách món có còn cuộn mượt như trên máy của bạn?</em></p>
        <p><strong>Mục tiêu:</strong> Viết được unit test và component test cho ứng dụng; kiểm thử được stored procedure bằng script T-SQL; sử dụng được công cụ gỡ lỗi; đánh giá và cải thiện được hiệu năng và khả năng truy cập (accessibility).</p>
        <p><strong>Nội dung:</strong></p>
        <ul>
            <li><strong>Ý chính 1 - Kiểm thử tự động:</strong> Jest + React Native Testing Library; test logic nghiệp vụ, test component, mock API; kiểm thử stored procedure bằng T-SQL.</li>
            <li><strong>Ý chính 2 - Gỡ lỗi:</strong> React Native DevTools, xem log, request mạng, sự kiện socket; quy trình tái hiện lỗi (liên hệ học phần Kiểm thử phần mềm).</li>
            <li><strong>Ý chính 3 - Hiệu năng:</strong> vẽ lại thừa, <code>React.memo</code>/<code>useCallback</code>, tối ưu <code>FlatList</code> và ảnh; đo trước và sau khi sửa.</li>
            <li><strong>Ý chính 4 - Accessibility và test do AI sinh:</strong> nhãn cho trình đọc màn hình, cỡ chữ hệ thống, vùng chạm; kiểm chứng test AI sinh ra có thật sự bắt được lỗi.</li>
        </ul>
        <p><strong>Kết quả cần đạt:</strong> LHU Food có bộ test chạy bằng <code>npm test</code>, kịch bản kiểm thử thủ tục; nhóm có bug log và ít nhất một cải tiến hiệu năng có số liệu trước/sau.</p>
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
            <h3 style="margin-top: 0; color: #fd7e14;">2.1. Thiết lập Jest cho dự án Expo</h3>
            <p>Theo hướng dẫn của Expo, cài <code>jest-expo</code> (preset cấu hình sẵn Jest cho React Native) và React Native Testing Library:</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>npx expo install jest-expo jest @types/jest -- --save-dev
npx expo install @testing-library/react-native -- --save-dev</code></pre>
            <p>Thêm vào <code>package.json</code>:</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>"scripts": { "test": "jest --watchAll" },
"jest": { "preset": "jest-expo" }</code></pre>
            <p style="margin-bottom: 0;">File test đặt trong thư mục <code>__tests__/</code> hoặc đặt tên <code>*.test.ts(x)</code>. Chạy bằng <code>npm test</code>. Store giỏ hàng dùng AsyncStorage (bài 07) cần mock AsyncStorage trong file thiết lập Jest bằng mock có sẵn của thư viện.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.2. Unit test và component test</h3>
            <p><strong>Unit test</strong> kiểm tra một hàm hoặc một store, không cần giao diện:</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// stores/__tests__/cart.test.ts
import { useCart } from '../cart';

beforeEach(() =&gt; useCart.setState({ items: [] }));

test('thêm trùng món thì cộng dồn số lượng', () =&gt; {
  useCart.getState().add({ id: 1, name: 'Cơm gà', price: 35000 });
  useCart.getState().add({ id: 1, name: 'Cơm gà', price: 35000 });
  expect(useCart.getState().items).toHaveLength(1);
  expect(useCart.getState().items[0].quantity).toBe(2);
  expect(useCart.getState().total()).toBe(70000);
});

test('giảm số lượng về 0 thì xóa món khỏi giỏ', () =&gt; {
  useCart.getState().add({ id: 2, name: 'Trà đào', price: 20000 });
  useCart.getState().decrease(2);
  expect(useCart.getState().items).toEqual([]);
});</code></pre>
            <p><strong>Component test</strong> vẽ component và thao tác như người dùng: tìm theo chữ hiển thị, bấm, kiểm tra kết quả:</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// components/__tests__/ProductCard.test.tsx
import { render, screen, fireEvent } from '@testing-library/react-native';
import { ProductCard } from '../ProductCard';

test('hiển thị tên món và gọi onAdd khi bấm nút', () =&gt; {
  const onAdd = jest.fn();
  render(&lt;ProductCard name="Bún bò Huế" price={40000} onAdd={onAdd} /&gt;);

  expect(screen.getByText('Bún bò Huế')).toBeTruthy();
  fireEvent.press(screen.getByText('Thêm vào giỏ'));
  expect(onAdd).toHaveBeenCalledTimes(1);
});</code></pre>
            <ul style="margin-bottom: 0;">
                <li><strong>Mock API:</strong> test màn hình có gọi API thì thay <code>lib/api</code> bằng <code>jest.mock('@/lib/api')</code> và quy định dữ liệu trả về, để test không phụ thuộc server.</li>
                <li><strong>Test hành vi, không test chi tiết cài đặt:</strong> tìm phần tử theo chữ người dùng thấy hoặc <code>accessibilityLabel</code>, không theo tên biến hay cấu trúc bên trong.</li>
                <li>Mỗi test độc lập: <code>beforeEach</code> đặt lại state để thứ tự chạy không ảnh hưởng kết quả.</li>
            </ul>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.3. Kiểm thử stored procedure</h3>
            <p>Logic dữ liệu nằm trong thủ tục, nên thủ tục cũng phải được kiểm thử. Chạy trên <strong>CSDL kiểm thử</strong> riêng (tạo từ thư mục <code>database/</code>), không chạy trên CSDL thật.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>-- tests/test-order-create.sql (chạy trên CSDL LhuFood_Test)
UPDATE Products SET Stock = 1, IsAvailable = 1 WHERE ProductId = 1;

-- TC-01: đặt quá tồn kho phải báo lỗi 50409 và không tạo đơn
DECLARE @before INT = (SELECT COUNT(*) FROM Orders);
BEGIN TRY
  EXEC sp_Order_Create @UserId = 1, @ItemsJson = N'[{"productId":1,"quantity":2}]';
  PRINT N'FAIL TC-01: không báo lỗi';
END TRY
BEGIN CATCH
  IF ERROR_NUMBER() = 50409 AND (SELECT COUNT(*) FROM Orders) = @before
    PRINT N'PASS TC-01';
  ELSE
    PRINT N'FAIL TC-01: ' + ERROR_MESSAGE();
END CATCH

-- TC-02: đặt đúng 1 suất thì tồn kho về 0
EXEC sp_Order_Create @UserId = 1, @ItemsJson = N'[{"productId":1,"quantity":1}]';
IF (SELECT Stock FROM Products WHERE ProductId = 1) = 0 PRINT N'PASS TC-02' ELSE PRINT N'FAIL TC-02';</code></pre>
            <p style="margin-bottom: 0;">Thiết kế ca kiểm thử theo kỹ thuật đã học ở môn Kiểm thử phần mềm: <strong>giá trị hợp lệ</strong>, <strong>không hợp lệ</strong> (JSON sai, số lượng âm), <strong>giá trị biên</strong> (đặt đúng bằng tồn kho, lớn hơn 1).</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.4. Gỡ lỗi</h3>
            <ul>
                <li><strong>React Native DevTools:</strong> nhấn <code>j</code> trong cửa sổ <code>npx expo start</code> để mở; có Console, đặt breakpoint, xem cây component và Profiler.</li>
                <li><strong>Màn hình đỏ (RedBox):</strong> đọc dòng đầu tiên của stack trace thuộc mã của bạn (không phải trong <code>node_modules</code>); đó thường là nơi phát sinh lỗi.</li>
                <li><strong>Lỗi mạng:</strong> log URL, mã trạng thái và nội dung lỗi trả về; thử cùng request bằng Swagger để biết lỗi ở app hay ở API.</li>
                <li><strong>Socket:</strong> lắng nghe <code>connect_error</code> để biết vì sao không kết nối được (token, địa chỉ, phiên bản).</li>
            </ul>
            <p style="margin: 0 0 6px 0;"><strong>Quy trình xử lý một lỗi</strong> (bug log của nhóm):</p>
            <ol style="margin-bottom: 0;">
                <li><strong>Tái hiện:</strong> ghi lại các bước, dữ liệu, thiết bị, phiên bản để lỗi xảy ra lại được.</li>
                <li><strong>Khoanh vùng:</strong> lỗi ở app, API, thủ tục hay dữ liệu? Kiểm tra từng ranh giới.</li>
                <li><strong>Viết test tái hiện lỗi</strong> (test phải đỏ), sửa mã, test chuyển xanh.</li>
                <li><strong>Ghi vào bug log:</strong> mô tả, mức độ, nguyên nhân, cách sửa, commit.</li>
            </ol>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.5. Hiệu năng</h3>
            <p><strong>Vẽ lại thừa:</strong> khi màn hình cha đổi state, mọi component con vẽ lại, kể cả khi props không đổi. Với danh sách 200 món, mỗi lần gõ một ký tự vào ô tìm kiếm có thể làm 200 thẻ vẽ lại.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// Chỉ vẽ lại ProductCard khi props thật sự đổi
export const ProductCard = React.memo(function ProductCard({ name, price, onAdd }: Props) { ... });

// Giữ nguyên tham chiếu hàm giữa các lần vẽ, nếu không memo sẽ vô tác dụng
const handleAdd = useCallback((item: Product) =&gt; add(item), [add]);
const renderItem = useCallback(
  ({ item }: { item: Product }) =&gt; &lt;ProductCard {...item} onAdd={() =&gt; handleAdd(item)} /&gt;,
  [handleAdd],
);</code></pre>
            <ul style="margin-bottom: 0;">
                <li><strong>FlatList:</strong> <code>keyExtractor</code> ổn định; <code>initialNumToRender</code> vừa đủ một màn hình; <code>getItemLayout</code> khi các dòng có chiều cao cố định.</li>
                <li><strong>Ảnh:</strong> dùng ảnh có kích thước phù hợp từ server; thư viện <code>expo-image</code> có bộ nhớ đệm và hiệu ứng hiện ảnh mượt hơn <code>Image</code> mặc định.</li>
                <li><strong>Đo trước khi sửa:</strong> dùng Profiler trong React Native DevTools để xem component nào vẽ lại nhiều và mất bao lâu; ghi số liệu trước và sau.</li>
                <li><strong>Đo ở chế độ gần thật:</strong> chế độ phát triển chậm hơn bản phát hành; chạy <code>npx expo start --no-dev --minify</code> và thử trên một máy Android tầm trung.</li>
            </ul>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.6. Accessibility và test do AI sinh</h3>
            <ul>
                <li><strong>Trình đọc màn hình (TalkBack):</strong> nút chỉ có biểu tượng phải có <code>accessibilityLabel</code> ("Thêm vào yêu thích") và <code>accessibilityRole="button"</code>.</li>
                <li><strong>Cỡ chữ hệ thống:</strong> người dùng có thể tăng cỡ chữ; kiểm tra giao diện không vỡ khi chữ lớn hơn.</li>
                <li><strong>Vùng chạm:</strong> tối thiểu khoảng 44–48 dp; dùng <code>hitSlop</code> cho biểu tượng nhỏ.</li>
                <li><strong>Độ tương phản:</strong> chữ xám nhạt trên nền trắng khó đọc ngoài trời.</li>
            </ul>
            <p style="margin: 0 0 6px 0;"><strong>Test do AI sinh:</strong> Copilot sinh test rất nhanh, nhưng test có thể "luôn xanh" mà không kiểm tra gì. Dùng <strong>mutation thủ công</strong> để kiểm chứng:</p>
            <ol style="margin-bottom: 0;">
                <li>Cố ý sửa sai logic (ví dụ đổi <code>price * quantity</code> thành <code>price + quantity</code>).</li>
                <li>Chạy test: nếu vẫn xanh, test đó không có giá trị.</li>
                <li>Hoàn lại mã; bổ sung khẳng định (<code>expect</code>) cho đến khi bản sửa sai làm test đỏ.</li>
            </ol>
        </div>

        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📄 Slide &amp; video bài giảng</p>
            <a href="{{LINK_SLIDE_BAI_10}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📄 Slide Bài 10: Kiểm thử, gỡ lỗi &amp; tối ưu hiệu năng</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📖 Tài liệu đọc thêm (chính thức)</p>
            <a href="https://docs.expo.dev/develop/unit-testing/" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Expo - Unit testing with Jest</span><br>
                <span style="color: #6c757d; font-size: 13px;">Cài jest-expo, cấu hình và viết test đầu tiên.</span>
            </a>
            <a href="https://callstack.github.io/react-native-testing-library/" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 React Native Testing Library</span><br>
                <span style="color: #6c757d; font-size: 13px;">render, screen, fireEvent và cách tìm phần tử.</span>
            </a>
            <a href="https://reactnative.dev/docs/performance" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 React Native - Performance</span><br>
                <span style="color: #6c757d; font-size: 13px;">Nguyên nhân giật lag và cách tối ưu danh sách.</span>
            </a>
            <a href="https://reactnative.dev/docs/accessibility" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 React Native - Accessibility</span><br>
                <span style="color: #6c757d; font-size: 13px;">Thuộc tính accessibility và kiểm tra với TalkBack.</span>
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
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🧑‍🏫 Thực hành có hướng dẫn (1,5 tiết): Test và tối ưu LHU Food</strong></p>
            <ol style="margin: 0; color: #495057;">
                <li>Cài và cấu hình Jest theo mục 2.1; chạy test mẫu.</li>
                <li>Viết test cho store giỏ hàng (thêm, cộng dồn, giảm, xóa, tổng tiền) và test cho <code>ProductCard</code>.</li>
                <li>Viết <code>tests/test-order-create.sql</code> và chạy trên CSDL kiểm thử.</li>
                <li>Mở Profiler, gõ vào ô tìm kiếm ở Trang chủ và ghi số lần vẽ lại của danh sách; áp dụng <code>React.memo</code> và <code>useCallback</code>; đo lại.</li>
                <li>Thêm <code>accessibilityLabel</code> cho các nút chỉ có biểu tượng; thử bằng TalkBack.</li>
            </ol>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">✍️ Thực hành không hướng dẫn (1 tiết): Test có giá trị</strong></p>
            <p style="margin: 0 0 6px 0; color: #495057;">Chọn một module tự làm (form đăng ký, hàm khoảng cách, store xác thực…). Viết tối thiểu 5 test (có thể nhờ AI sinh), sau đó áp dụng <strong>mutation thủ công</strong> với ít nhất 3 lỗi cố ý.</p>
            <p style="margin: 0 0 8px 0; color: #495057;"><strong>Hoàn thành khi:</strong> 5 test pass; nộp bảng gồm lỗi cố ý, test nào bắt được, test bổ sung cho lỗi chưa bị bắt; ghi prompt sinh test vào <code>PROMPTS.md</code>.</p>
            <a href="{{LINK_NOP_BAI_10}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp bài</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">👥 Thử thách nhóm (0,5 tiết + ở nhà)</strong></p>
            <ul style="margin: 0; color: #495057;">
                <li>Bộ test cho các luồng chính của ứng dụng và kịch bản kiểm thử cho các thủ tục quan trọng.</li>
                <li><strong>Bug log</strong> (<code>docs/bug-log.md</code>): mỗi lỗi có mô tả, bước tái hiện, mức độ, nguyên nhân, cách sửa, commit.</li>
                <li>Ít nhất <strong>1 cải tiến hiệu năng có số liệu trước/sau</strong> (thời gian, số lần vẽ lại).</li>
            </ul>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">💬 Diễn đàn thảo luận</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">Chia sẻ một test do AI sinh ra mà bạn phát hiện "luôn xanh" khi áp dụng mutation thủ công. Test đó thiếu điều gì?</p>
            <a href="{{LINK_DIEN_DAN_BAI_10}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Tham gia diễn đàn</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">📝 Trắc nghiệm nhanh (Quiz)</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">10 câu ôn tập Jest, React Native Testing Library, kiểm thử thủ tục, gỡ lỗi, hiệu năng và accessibility.</p>
            <a href="{{LINK_QUIZ_BAI_10}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Làm bài Quiz Bài 10</a>
        </div>
    </div>
</details>

<details style="border: 1px solid #6f42c1; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #f3e5f5; color: #6f42c1; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>🆘 4. Góc trợ giúp và mở rộng</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>Test báo lỗi khi import thư viện native (AsyncStorage, SecureStore…):</strong> môi trường Jest không có mã native; mock thư viện đó bằng <code>jest.mock(...)</code> hoặc dùng mock có sẵn của thư viện.</p>
        <p><strong>Test giỏ hàng ảnh hưởng lẫn nhau:</strong> store Zustand dùng chung giữa các test; đặt lại bằng <code>useCart.setState({ items: [] })</code> trong <code>beforeEach</code>.</p>
        <p><strong>Lỗi chỉ xảy ra trên bản APK, không xảy ra khi chạy Expo Go:</strong> thường do biến môi trường, quyền chưa khai báo trong <code>app.json</code>, hoặc kết nối HTTP bị chặn; bài 11 xử lý các trường hợp này.</p>
        <p><strong>Kiến thức mở rộng:</strong> Kiểm thử đầu-cuối (E2E) bằng Maestro, chạy kịch bản thao tác trên emulator như người dùng thật.</p>
        <p style="margin-bottom: 0;"><strong>Tự đánh giá:</strong> Nếu ngày mai một bạn trong nhóm sửa <code>sp_Order_Create</code>, nhóm có cách nào biết ngay thủ tục vẫn chặn được đặt quá tồn kho không?</p>
    </div>
</details>
