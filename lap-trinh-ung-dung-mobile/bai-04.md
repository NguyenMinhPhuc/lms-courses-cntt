<details open="" style="border: 1px solid #007bff; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #e7f1ff; color: #007bff; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>📘 1. Tổng quan bài học</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>BÀI 04 - Quản lý trạng thái, danh sách &amp; form (5 tiết: 1 LT / 4 TH)</strong></p>
        <p><em>Người dùng thêm một món vào giỏ ở màn hình Chi tiết, rồi chuyển sang tab Giỏ hàng. Làm sao để tab Giỏ hàng biết ngay có món mới? Và khi thực đơn có 500 món, làm sao để cuộn vẫn mượt?</em></p>
        <p><strong>Mục tiêu:</strong> Phân biệt được trạng thái cục bộ, trạng thái toàn cục và trạng thái từ server; hiển thị được danh sách lớn hiệu quả bằng <code>FlatList</code>; xây dựng được form có kiểm tra dữ liệu bằng React Hook Form và Zod.</p>
        <p><strong>Nội dung:</strong></p>
        <ul>
            <li><strong>Ý chính 1 - Ba loại trạng thái:</strong> cục bộ (<code>useState</code>, <code>useReducer</code>), toàn cục dùng chung nhiều màn hình (Zustand), và dữ liệu từ server (bài 05).</li>
            <li><strong>Ý chính 2 - Danh sách hiệu quả:</strong> <code>FlatList</code> chỉ vẽ phần đang hiển thị; <code>keyExtractor</code>, danh sách rỗng, kéo để tải lại, nhiều cột.</li>
            <li><strong>Ý chính 3 - Form có kiểm tra dữ liệu:</strong> React Hook Form + Zod, thông báo lỗi tiếng Việt, bàn phím phù hợp và không che ô nhập.</li>
            <li><strong>Ý chính 4 - Vibe coding cho quy tắc nghiệp vụ:</strong> AI sinh schema Zod từ đặc tả; bạn tự viết các trường hợp biên để kiểm tra lại.</li>
        </ul>
        <p><strong>Kết quả cần đạt:</strong> Giỏ hàng LHU Food dùng chung giữa các màn hình; danh sách món dùng <code>FlatList</code>; form đăng ký kiểm tra đủ quy tắc; người phụ trách backend của nhóm đã khởi tạo NestJS kết nối SQL Server.</p>
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
            <h3 style="margin-top: 0; color: #fd7e14;">2.1. Ba loại trạng thái trong ứng dụng</h3>
            <table style="width: 100%; border-collapse: collapse; font-size: 14px;">
                <thead><tr style="background-color: #fff5eb;"><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Loại</th><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Ví dụ LHU Food</th><th style="padding: 8px; border: 1px solid #ffd6ad; text-align: left;">Công cụ</th></tr></thead>
                <tbody>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;"><strong>Cục bộ</strong>: chỉ một màn hình dùng</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Số lượng đang chọn ở màn hình Chi tiết, ô tìm kiếm đang gõ</td><td style="padding: 8px; border: 1px solid #ffd6ad;"><code>useState</code>, <code>useReducer</code></td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;"><strong>Toàn cục</strong>: nhiều màn hình cùng đọc/ghi</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Giỏ hàng, thông tin người đăng nhập</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Zustand (hoặc Context)</td></tr>
                    <tr><td style="padding: 8px; border: 1px solid #ffd6ad;"><strong>Từ server</strong>: bản gốc nằm trong SQL Server</td><td style="padding: 8px; border: 1px solid #ffd6ad;">Thực đơn, lịch sử đơn hàng</td><td style="padding: 8px; border: 1px solid #ffd6ad;">TanStack Query (bài 05)</td></tr>
                </tbody>
            </table>
            <p style="margin: 10px 0 6px 0;"><strong>💡 Giỏ hàng toàn cục với Zustand:</strong></p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>// stores/cart.ts
import { create } from 'zustand';

type CartItem = { id: number; name: string; price: number; quantity: number };

type CartState = {
  items: CartItem[];
  add: (product: Omit&lt;CartItem, 'quantity'&gt;) =&gt; void;
  remove: (id: number) =&gt; void;
  total: () =&gt; number;
};

export const useCart = create&lt;CartState&gt;((set, get) =&gt; ({
  items: [],
  add: (product) =&gt;
    set((state) =&gt; {
      const found = state.items.find((i) =&gt; i.id === product.id);
      return {
        items: found
          ? state.items.map((i) =&gt; (i.id === product.id ? { ...i, quantity: i.quantity + 1 } : i))
          : [...state.items, { ...product, quantity: 1 }],
      };
    }),
  remove: (id) =&gt; set((state) =&gt; ({ items: state.items.filter((i) =&gt; i.id !== id) })),
  total: () =&gt; get().items.reduce((sum, i) =&gt; sum + i.price * i.quantity, 0),
}));

// Ở bất kỳ màn hình nào
const items = useCart((state) =&gt; state.items);
const add = useCart((state) =&gt; state.add);</code></pre>
            <p style="margin-bottom: 0;">Mỗi màn hình chỉ "chọn" phần state mình cần (<code>state =&gt; state.items</code>), nên màn hình chỉ vẽ lại khi phần đó thay đổi.</p>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.2. Danh sách hiệu quả với FlatList</h3>
            <p><code>ScrollView</code> vẽ <strong>tất cả</strong> phần tử ngay khi mở màn hình. Với 500 món, máy phải dựng 500 thẻ cùng lúc. <code>FlatList</code> chỉ vẽ những phần tử đang hiển thị (và một ít phía trước/sau), nên cuộn mượt và tốn ít bộ nhớ.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>&lt;FlatList
  data={products}
  keyExtractor={(item) =&gt; String(item.id)}
  renderItem={({ item }) =&gt; &lt;ProductCard {...item} onAdd={() =&gt; add(item)} /&gt;}
  numColumns={2}
  columnWrapperStyle={{ gap: 16 }}
  contentContainerStyle={{ padding: 16, gap: 16 }}
  ListEmptyComponent={&lt;Text&gt;Chưa có món nào trong danh mục này.&lt;/Text&gt;}
  refreshing={refreshing}
  onRefresh={reload}
/&gt;</code></pre>
            <ul style="margin-bottom: 0;">
                <li><code>keyExtractor</code> trả về khóa <strong>duy nhất và ổn định</strong> (mã món), không dùng chỉ số mảng.</li>
                <li><code>ListEmptyComponent</code>: luôn có trạng thái rỗng, đừng để màn hình trắng trơn.</li>
                <li><code>refreshing</code> + <code>onRefresh</code>: kéo xuống để tải lại (bài 05 nối với API thật).</li>
                <li><code>SectionList</code>: danh sách chia nhóm có tiêu đề, ví dụ món theo từng danh mục.</li>
            </ul>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.3. Form với React Hook Form + Zod</h3>
            <p><strong>Zod</strong> mô tả quy tắc dữ liệu một lần (schema); <strong>React Hook Form</strong> quản lý giá trị, lỗi và việc gửi form. Cài: <code>npx expo install react-hook-form zod @hookform/resolvers</code>.</p>
<pre style="background-color: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 13px; line-height: 1.5;"><code>import { useForm, Controller } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';

const orderNoteSchema = z.object({
  phone: z.string().regex(/^0\d{9}$/, 'Số điện thoại gồm 10 chữ số, bắt đầu bằng 0'),
  note: z.string().max(200, 'Ghi chú tối đa 200 ký tự').optional(),
});
type OrderNote = z.infer&lt;typeof orderNoteSchema&gt;;

export function OrderNoteForm({ onSubmit }: { onSubmit: (data: OrderNote) =&gt; void }) {
  const { control, handleSubmit, formState: { errors } } = useForm&lt;OrderNote&gt;({
    resolver: zodResolver(orderNoteSchema),
  });

  return (
    &lt;View&gt;
      &lt;Controller
        control={control}
        name="phone"
        render={({ field: { onChange, onBlur, value } }) =&gt; (
          &lt;TextInput value={value} onChangeText={onChange} onBlur={onBlur}
            keyboardType="phone-pad" placeholder="Số điện thoại" /&gt;
        )}
      /&gt;
      {errors.phone &amp;&amp; &lt;Text style={{ color: 'red' }}&gt;{errors.phone.message}&lt;/Text&gt;}
      &lt;Button title="Xác nhận" onPress={handleSubmit(onSubmit)} /&gt;
    &lt;/View&gt;
  );
}</code></pre>
            <ul style="margin-bottom: 0;">
                <li><strong>So khớp hai trường</strong> (mật khẩu và xác nhận mật khẩu): dùng <code>.refine((d) =&gt; d.password === d.confirm, { message: 'Mật khẩu xác nhận không khớp', path: ['confirm'] })</code>.</li>
                <li><strong>Bàn phím:</strong> chọn <code>keyboardType</code> đúng loại (email, số điện thoại); bọc form trong <code>KeyboardAvoidingView</code> để bàn phím không che ô đang nhập.</li>
                <li><strong>Kiểm tra ở app chưa đủ:</strong> API ở bài 05–06 vẫn phải kiểm tra lại, vì request có thể không đi từ app của bạn.</li>
            </ul>
        </div>

        <div style="max-width: 900px; padding: 14px; margin: 8px 0; background-color: #fff8f1; border: 1px solid #ffd6ad; border-radius: 8px;">
            <h3 style="margin-top: 0; color: #fd7e14;">2.4. Vibe coding cho quy tắc nghiệp vụ</h3>
            <ol>
                <li>Viết đặc tả bằng lời: <em>"Họ tên 2–100 ký tự; email đúng định dạng; số điện thoại 10 chữ số bắt đầu bằng 0; mật khẩu tối thiểu 8 ký tự, có chữ và số; xác nhận mật khẩu phải khớp."</em></li>
                <li>Nhờ Copilot Chat sinh schema Zod với thông báo lỗi tiếng Việt.</li>
                <li><strong>Tự viết bảng trường hợp biên</strong> rồi thử từng trường hợp: họ tên 1 ký tự và 2 ký tự; số điện thoại 9 và 10 chữ số; mật khẩu 7 và 8 ký tự; mật khẩu chỉ có chữ.</li>
                <li>Trường hợp nào AI viết sai, sửa schema và ghi vào <code>PROMPTS.md</code>.</li>
            </ol>
            <p style="margin-bottom: 0;"><strong>Vì sao không tin ngay?</strong> AI hay viết biểu thức chính quy "gần đúng", ví dụ chấp nhận số điện thoại 11 chữ số hoặc quên chặn khoảng trắng. Kỹ thuật kiểm tra giá trị biên bạn đã học ở môn Kiểm thử phần mềm dùng được ngay ở đây.</p>
        </div>

        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📄 Slide &amp; video bài giảng</p>
            <a href="{{LINK_SLIDE_BAI_04}}" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">📄 Slide Bài 04: Quản lý trạng thái, danh sách &amp; form</span>
            </a>
        </div>
        <div style="margin-top: 16px;">
            <p style="margin: 0 0 8px 0; color: #fd7e14; font-weight: bold;">📖 Tài liệu đọc thêm (chính thức)</p>
            <a href="https://reactnative.dev/docs/flatlist" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 React Native - FlatList</span><br>
                <span style="color: #6c757d; font-size: 13px;">Thuộc tính của FlatList và các lưu ý hiệu năng.</span>
            </a>
            <a href="https://zustand.docs.pmnd.rs" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 Zustand Documentation</span><br>
                <span style="color: #6c757d; font-size: 13px;">Tạo store, chọn state và cập nhật state.</span>
            </a>
            <a href="https://react-hook-form.com" target="_blank" rel="noopener noreferrer" style="display: block; max-width: 760px; padding: 10px 12px; margin: 6px 0; background-color: #fff8f1; color: #212529; border: 1px solid #ffd6ad; border-radius: 8px; text-decoration: none;">
                <span style="color: #fd7e14; font-weight: bold;">🔗 React Hook Form</span><br>
                <span style="color: #6c757d; font-size: 13px;">Controller cho React Native và tích hợp Zod qua resolver.</span>
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
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">🧑‍🏫 Thực hành có hướng dẫn (2 tiết): Giỏ hàng &amp; thực đơn LHU Food</strong></p>
            <ol style="margin: 0; color: #495057;">
                <li>Cài Zustand: <code>npx expo install zustand</code>; tạo <code>stores/cart.ts</code> theo mục 2.1.</li>
                <li>Nút "Thêm vào giỏ" ở Chi tiết món gọi <code>add()</code>; tab Giỏ hàng hiển thị danh sách và tổng tiền; nút xóa từng món.</li>
                <li>Hiện số món trong giỏ trên biểu tượng tab (<code>tabBarBadge</code>).</li>
                <li>Đổi lưới món ở Trang chủ sang <code>FlatList</code> 2 cột, có danh sách rỗng và kéo để tải lại (dữ liệu giả).</li>
                <li>Tạo form ghi chú đơn hàng (số điện thoại, ghi chú) bằng React Hook Form + Zod trong modal Xác nhận.</li>
            </ol>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">✍️ Thực hành không hướng dẫn (1,5 tiết): Form Đăng ký</strong></p>
            <p style="margin: 0 0 6px 0; color: #495057;">Xây form Đăng ký tài khoản với các trường họ tên, email, số điện thoại, mật khẩu, xác nhận mật khẩu theo đặc tả ở mục 2.4.</p>
            <p style="margin: 0 0 8px 0; color: #495057;"><strong>Hoàn thành khi:</strong> mọi quy tắc báo lỗi tiếng Việt ngay dưới ô nhập; nút Đăng ký chỉ gửi khi form hợp lệ; bàn phím đúng loại cho từng ô và không che ô đang nhập; nộp kèm bảng trường hợp biên đã thử (đạt/không đạt).</p>
            <a href="{{LINK_NOP_BAI_04}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Nộp bài</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">👥 Thử thách nhóm (0,5 tiết + ở nhà)</strong></p>
            <ul style="margin: 0; color: #495057;">
                <li>Store toàn cục cho nghiệp vụ chính của đề tài và tối thiểu 1 form nghiệp vụ có kiểm tra dữ liệu.</li>
                <li><strong>Người phụ trách backend:</strong> khởi tạo dự án NestJS (<code>nest new</code>), cài <code>mssql</code>, kết nối SQL Server bằng biến môi trường trong <code>.env</code>, tạo các bảng theo ERD sơ bộ.</li>
            </ul>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">💬 Diễn đàn thảo luận</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">Trong đề tài của nhóm, liệt kê 3 dữ liệu là trạng thái cục bộ, 2 dữ liệu là trạng thái toàn cục và 2 dữ liệu lấy từ server. Có dữ liệu nào nhóm còn phân vân không?</p>
            <a href="{{LINK_DIEN_DAN_BAI_04}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Tham gia diễn đàn</a>
        </div>
        <div style="max-width: 760px; padding: 10px 12px; margin: 8px 0; background-color: #f4fff8; border: 1px solid #bfe8cc; border-radius: 8px;">
            <p style="margin: 0 0 6px 0;"><strong style="color: #28a745;">📝 Trắc nghiệm nhanh (Quiz)</strong></p>
            <p style="margin: 0 0 8px 0; color: #495057;">10 câu ôn tập các loại trạng thái, Zustand, FlatList và form với React Hook Form + Zod.</p>
            <a href="{{LINK_QUIZ_BAI_04}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 6px 12px; background-color: #eafaf1; color: #28a745; border: 1px solid #28a745; border-radius: 6px; text-decoration: none; font-weight: bold;">Làm bài Quiz Bài 04</a>
        </div>
    </div>
</details>

<details style="border: 1px solid #6f42c1; border-radius: 8px; margin-bottom: 15px; font-family: sans-serif; overflow: hidden;">
    <summary style="padding: 15px; background-color: #f3e5f5; color: #6f42c1; font-weight: bold; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center;">
        <span>🆘 4. Góc trợ giúp và mở rộng</span>
        <span style="font-size: 12px;">▼</span>
    </summary>
    <div style="padding: 15px; background-color: #fff; line-height: 1.6;">
        <p><strong>Cảnh báo "VirtualizedLists should never be nested inside plain ScrollViews":</strong> bạn đặt <code>FlatList</code> bên trong <code>ScrollView</code>. Bỏ <code>ScrollView</code>, đưa phần đầu trang vào <code>ListHeaderComponent</code> của <code>FlatList</code>.</p>
        <p><strong>Giỏ hàng không cập nhật:</strong> kiểm tra hàm cập nhật trả về <strong>mảng mới</strong> (<code>map</code>, <code>filter</code>, spread), không sửa trực tiếp mảng cũ bằng <code>push</code>.</p>
        <p><strong>Form không báo lỗi:</strong> kiểm tra đã truyền <code>resolver: zodResolver(schema)</code> và tên trường trong <code>Controller name</code> khớp với schema.</p>
        <p><strong>Kiến thức mở rộng:</strong> Tìm hiểu middleware <code>persist</code> của Zustand để giữ giỏ hàng khi tắt app (bài 07 sẽ dùng).</p>
        <p style="margin-bottom: 0;"><strong>Tự đánh giá:</strong> Nếu xóa store Zustand và chuyển giỏ hàng về <code>useState</code> trong màn hình Chi tiết, tab Giỏ hàng sẽ gặp vấn đề gì?</p>
    </div>
</details>
