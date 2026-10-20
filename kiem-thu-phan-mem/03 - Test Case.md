# Danh sách động từ và cách xây dựng Test Case trong kiểm thử phần mềm

## 1. Danh sách các động từ thường dùng trong Test Case

### a. Động từ hành động của người dùng (User actions)
- **Click / Nhấn**: click, double-click, right-click, tap  
- **Nhập dữ liệu**: enter, input, type, fill  
- **Chọn**: select, choose, check, uncheck, pick  
- **Điều hướng**: navigate, open, go to, scroll, swipe  
- **Gửi yêu cầu**: submit, upload, download, search, send  

### b. Động từ phản hồi/hành động của hệ thống (System actions)
- **Hiển thị**: display, show, render, present, pop up  
- **Xử lý**: process, calculate, validate, update, execute  
- **Thay đổi dữ liệu**: save, delete, modify, refresh  
- **Phản hồi**: return, notify, alert, confirm  

### c. Động từ xác minh (Validation/Verification)
- **Kiểm tra**: check, verify, validate, assert  
- **So sánh**: match, equal, contain, differ  
- **Đánh giá trạng thái**: ensure, confirm, guarantee  


## 2. Cách xây dựng Test Case bằng động từ

Một **Test Case** thường gồm 4 thành phần chính:  
1. **Test Case ID** – Mã định danh duy nhất.  
2. **Precondition** – Điều kiện tiên quyết (ví dụ: user đã đăng nhập).  
3. **Test Steps** – Các bước hành động (sử dụng động từ rõ ràng).  
4. **Expected Result** – Kết quả mong đợi (cũng dùng động từ mô tả hệ thống phản hồi).  

### Ví dụ minh họa

**Test Case**: Đăng nhập thành công vào hệ thống  

- **ID**: TC001  
- **Precondition**: Người dùng đã có tài khoản hợp lệ.  
- **Test Steps**:  
  1. Navigate đến trang đăng nhập.  
  2. Enter email hợp lệ vào trường “Email”.  
  3. Enter password hợp lệ vào trường “Password”.  
  4. Click vào nút **Login**.  
- **Expected Result**:  
  - Hệ thống **display** trang Dashboard.  
  - Một thông báo chào mừng **show** ra: “Welcome, [username]”.  


## 3. Nguyên tắc dùng động từ trong Test Case

- **Rõ ràng, nhất quán**: Mỗi bước nên bắt đầu bằng 1 động từ → dễ đọc, dễ làm theo.  
- **Tránh mơ hồ**: Thay vì viết “Làm thao tác đăng nhập”, nên viết “Enter username” + “Enter password” + “Click Login”.  
- **Kết hợp User action + System response**: Test Case phải đầy đủ cả 2 phía.  
- **Hạn chế viết chung chung**: Tránh “Check login works” → nên chi tiết từng hành động.

# Mẫu đầu câu khi viết Test Case

## 1. Mẫu đầu câu cho **Test Steps** (Hành động của người dùng)  

Thường bắt đầu bằng **động từ mạnh** (action verb):  

- **Navigate to...** → Navigate to the Login page.  
- **Open...** → Open the application.  
- **Enter...** → Enter valid username into the “Username” field.  
- **Type...** → Type password into the “Password” field.  
- **Click...** → Click on the “Login” button.  
- **Select...** → Select “Remember Me” checkbox.  
- **Upload...** → Upload a valid image file.  
- **Download...** → Download the generated report.  
- **Scroll...** → Scroll down to the bottom of the page.  


## 2. Mẫu đầu câu cho **Expected Result** (Kết quả mong đợi của hệ thống)  

Thường bắt đầu bằng **System response verbs**:  

- **System should display...** → System should display the Dashboard page.  
- **Message should appear...** → Message should appear: “Login successful”.  
- **Data should be saved...** → Data should be saved into the database.  
- **Field should be validated...** → Field should be validated for correct email format.  
- **System should return...** → System should return status code 200 (for API test).  
- **Notification should be sent...** → Notification should be sent to user’s email.  
- **Record should be updated...** → Record should be updated in the user profile.  

## 3. Gợi ý chuẩn hóa Test Case  

Một cách viết dễ đọc là **chia câu thành 2 phần**:  

- **User Action (Step):** `Enter valid email into the Email field.`  
- **Expected Result:** `System should display message 'Email accepted'.`  

Hoặc dùng mẫu câu dạng:  

- **When [User action], Then [System response]**  
  - *When user clicks on Login, then system should display Dashboard.*  

