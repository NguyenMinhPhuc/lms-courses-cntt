## 1. Test Requirement là gì?
Test Requirement (Yêu cầu kiểm thử) là tập hợp các điều kiện, tiêu chí hoặc chức năng của hệ thống/phần mềm cần được kiểm tra để đảm bảo rằng phần mềm hoạt động đúng như mong đợi.
Nó là cơ sở đầu tiên để xây dựng các test case, test script, và để đánh giá hệ thống có đáp ứng đúng yêu cầu người dùng hoặc đặc tả kỹ thuật hay không.

## 2. Ví dụ về Test Requirement
### Ví dụ: Hệ thống đăng nhập cho ứng dụng Web
Yêu cầu nghiệp vụ (BR - Business Requirement):
 Người dùng có thể đăng nhập vào hệ thống bằng tên người dùng và mật khẩu.
Test Requirement có thể viết:
| TR ID  | Test Requirement Description                                                               |
| ------ | ------------------------------------------------------------------------------------------ |
| TR-001 | The system shall provide input fields for username and password on the login page.         |
| TR-002 | The system shall allow users to log in with valid username and password credentials.       |
| TR-003 | The system shall display an error message when an invalid username or password is entered. |
| TR-004 | The username and password fields must not be left blank.                                   |
| TR-005 | The password input field shall be masked (characters hidden with asterisks or bullets).    |

Tiếng việt:
> TR-001: Đảm bảo UI có sẵn để nhập thông tin.

> TR-002: Kiểm tra logic đăng nhập hợp lệ.

> TR-003: Đảm bảo xử lý khi sai thông tin đăng nhập.

> TR-004: Xác minh ràng buộc dữ liệu không được để trống.

> TR-005: Đảm bảo bảo mật thông tin khi nhập mật khẩu.

## 3. Các điều kiện cần thiết để viết một Test Requirement tốt
Một Test Requirement tốt nên tuân thủ theo tiêu chí **SMART** (giống cách viết yêu cầu phần mềm):
| Yếu tố             | Ý nghĩa              | Giải thích                                                 |
| ------------------ | -------------------- | ---------------------------------------------------------- |
| **S - Specific**   | Cụ thể               | Nêu rõ chức năng, hành động, đầu vào, đầu ra cần kiểm thử. |
| **M - Measurable** | Đo lường được        | Có thể định lượng hoặc xác định kết quả kiểm thử rõ ràng.  |
| **A - Achievable** | Khả thi              | Có thể thực hiện được bằng cách viết test case.            |
| **R - Relevant**   | Phù hợp              | Liên quan trực tiếp đến chức năng và yêu cầu hệ thống.     |
| **T - Testable**   | Có thể kiểm thử được | Có thể kiểm tra bằng cách thủ công hoặc tự động.           |

### Các yếu tố kỹ thuật bổ sung (**TUC**):
- **Traceable**: Có thể truy vết về yêu cầu chức năng hoặc tài liệu đặc tả.
- **Unambiguous**: Không mơ hồ, không gây hiểu nhầm.
- **Consistent**: Không mâu thuẫn với yêu cầu khác.
## 4. Test Requirement type:

| TR Type         | Nội dung kiểm thử                             | Ví dụ minh họa                                             |
| --------------- | --------------------------------------------- | ---------------------------------------------------------- |
| **Functional**  | Kiểm tra chức năng chính theo yêu cầu         | Đăng nhập với username/password hợp lệ                     |
| **Boundary**    | Kiểm tra dữ liệu tại ranh giới (edge cases)   | Tuổi = 17 (fail), 18 (pass), 60 (pass), 61 (fail)          |
| **Look & Feel** | Kiểm tra giao diện, bố cục, hiển thị          | Nút “Login” phải nằm giữa màn hình, mật khẩu phải được che |
| **Negative**    | Kiểm tra tình huống sai, dữ liệu không hợp lệ | Nhập mật khẩu sai → hệ thống báo lỗi, không cho đăng nhập  |

## 4. Mối liên hệ giữa Test Requirement và Test Case
Test Requirement là đầu vào để viết test case. Ví dụ:
| Test Requirement                                             | Test Case tương ứng                                                     |
| ------------------------------------------------------------ | ----------------------------------------------------------------------- |
| **TR-002:** Hệ thống chuyển đến trang chủ khi đăng nhập đúng | **TC-002:** Nhập đúng username/password → xác nhận chuyển đến dashboard |

### Ghi chú: 
> Việc viết Test Requirement không chỉ giúp đảm bảo chất lượng phần mềm, mà còn là cầu nối giữa phân tích nghiệp vụ và kỹ thuật kiểm thử.
> Một Test Requirement tốt sẽ giúp cho tester không bỏ sót tình huống kiểm tra nào, tăng khả năng phát hiện lỗi sớm, đồng thời dễ dàng truy vết khi có lỗi xảy ra trong vận hành thực tế.
> Trong môi trường Agile, việc đảm bảo yêu cầu kiểm thử được cập nhật kịp thời còn giúp đẩy nhanh tiến độ kiểm thử liên tục (Continuous Testing).

## 5. Structure of a Well-Written Test Requirement in English
| Field                   | Description                                               |
| ----------------------- | --------------------------------------------------------- |
| **ID**                  | Unique identifier, e.g., TR-001                           |
| **Title**               | Short and descriptive name                                |
| **Description**         | Clear and testable statement of what needs to be tested   |
| **Priority**            | (Optional) e.g., High / Medium / Low                      |
| **Related Requirement** | Link to business or functional requirement (if available) |
| **Acceptance Criteria** | (Optional) What must be true for the test to pass         |

## Example – Login Functionality
### Business Requirement (BR):
The system must allow users to log in using a valid username and password.
### Derived Test Requirements (in English):
| ID         | Title              | Description                                                                                   |
| ---------- | ------------------ | --------------------------------------------------------------------------------------------- |
| **TR-001** | Login Input Fields | The login page must display input fields for username and password.                           |
| **TR-002** | Successful Login   | The system must allow access and redirect the user to the dashboard upon correct credentials. |
| **TR-003** | Invalid Login      | The system must display an error message when invalid username or password is entered.        |
| **TR-004** | Required Fields    | Both username and password fields must be mandatory.                                          |
| **TR-005** | Password Masking   | The password input must be hidden (masked with asterisks or bullets).                         |

## 6. Tips for Writing Good Test Requirements in English
Apply the SMART + TUC principle:
| Aspect          | Explanation                                       | Sample Phrase / Note                             |
| --------------- | ------------------------------------------------- | ------------------------------------------------ |
| **Specific**    | Clearly identify what to test                     | "The system must display..."                     |
| **Measurable**  | Must produce a pass/fail result                   | "Must redirect to dashboard..."                  |
| **Achievable**  | Realistic to test with current tools              | Avoid vague goals like "Improve security"        |
| **Relevant**    | Tied to business or technical requirements        | Only write what supports BRD/FRD                 |
| **Testable**    | Can be verified through manual or automated tests | Avoid subjective terms                           |
| **Unambiguous** | Only one interpretation                           | Use precise terms: "must", "shall", not "should" |
| **Consistent**  | Do not contradict other requirements              | Align with system specs                          |

## 7. Useful Vocabulary & Phrases
| Vietnamese Term                     | English Test Requirement Equivalent |
| ----------------------------------- | ----------------------------------- |
| Người dùng nhập dữ liệu             | The user **shall** input data           |
| Hệ thống hiển thị thông báo         | The system **shall display** a message  |
| Chuyển hướng đến trang chủ          | **Redirect to** the home page           |
| Tên đăng nhập/mật khẩu không hợp lệ | **Invalid **username or password        |
| Không được để trống                 | **Must not be **left blank              |
| Dữ liệu phải được mã hóa            | The data **must be** encrypted          |

### 7.1.Nhóm từ vựng mô tả hành vi hệ thống (System behavior)

| English Phrase                  | Nghĩa tiếng Việt                  |
| ------------------------------- | --------------------------------- |
| The system shall allow\...      | Hệ thống phải cho phép...         |
| The system must prevent...      | Hệ thống phải ngăn không cho...   |
| The system shall display...     | Hệ thống phải hiển thị...         |
| The system must store...        | Hệ thống phải lưu trữ...          |
| The system shall validate...    | Hệ thống phải kiểm tra hợp lệ...  |
| The system must encrypt...      | Hệ thống phải mã hóa...           |
| The system shall support...     | Hệ thống phải hỗ trợ...           |
| The system shall redirect to... | Hệ thống phải chuyển hướng đến... |

### 7.2. Nhóm từ vựng mô tả hành động người dùng (User interaction)

| English Phrase                           | Nghĩa tiếng Việt                    |
| ---------------------------------------- | ----------------------------------- |
| The user shall enter...                  | Người dùng phải nhập...             |
| The user must be able to select...       | Người dùng phải có thể chọn...      |
| The user can submit...                   | Người dùng có thể gửi...            |
| The user must not be allowed to...       | Người dùng không được phép...       |
| The user should receive feedback when... | Người dùng nên nhận phản hồi khi... |

### 7.3. Nhóm từ mô tả điều kiện và ràng buộc (Conditions & Constraints)
| English Phrase                                 | Nghĩa tiếng Việt                          |
| ---------------------------------------------- | ----------------------------------------- |
| Input fields must not be left blank            | Các trường nhập không được để trống       |
| Password must be masked                        | Mật khẩu phải được ẩn (mask)              |
| Username must be unique                        | Tên người dùng phải là duy nhất           |
| Required fields must be indicated              | Trường bắt buộc phải được đánh dấu        |
| The process must be completed within 5 seconds | Quy trình phải hoàn tất trong vòng 5 giây |
| The user must have appropriate permissions     | Người dùng phải có quyền phù hợp          |

### 7.4. Nhóm từ mô tả thông báo lỗi và xử lý ngoại lệ (Error handling & Messages)

| English Phrase                             | Nghĩa tiếng Việt                               |
| ------------------------------------------ | ---------------------------------------------- |
| An error message must be displayed when... | Phải hiển thị thông báo lỗi khi...             |
| The system shall notify the user that...   | Hệ thống phải thông báo cho người dùng rằng... |
| A warning shall be triggered if...         | Cảnh báo phải được kích hoạt nếu...            |
| The system must log the error...           | Hệ thống phải ghi nhận lỗi...                  |
| Invalid inputs shall be rejected           | Dữ liệu không hợp lệ phải bị từ chối           |

### 7.5. Nhóm từ về xác thực, bảo mật, quyền truy cập (Security & Access Control)

| English Phrase                                      | Nghĩa tiếng Việt                                   |
| --------------------------------------------------- | -------------------------------------------------- |
| The password shall be encrypted using SHA-256       | Mật khẩu phải được mã hóa bằng SHA-256             |
| Access shall be restricted to authorized users only | Chỉ người dùng được cấp quyền mới được truy cập    |
| Users must log in before accessing the dashboard    | Người dùng phải đăng nhập trước khi vào dashboard  |
| The system shall log all login attempts             | Hệ thống phải ghi nhận tất cả lượt đăng nhập       |
| Session must expire after 15 minutes of inactivity  | Phiên làm việc hết hạn sau 15 phút không hoạt động |

## 7.6. Nhóm từ mô tả đầu vào, đầu ra (Input/Output Specifications)

| English Phrase                                  | Nghĩa tiếng Việt                                  |
| ----------------------------------------------- | ------------------------------------------------- |
| Input must be alphanumeric                      | Dữ liệu đầu vào phải là chữ và số                 |
| Output shall be formatted as JSON               | Dữ liệu đầu ra phải có định dạng JSON             |
| Input values shall be within the range of 1–100 | Dữ liệu đầu vào phải nằm trong khoảng 1–100       |
| Output must include timestamp and user ID       | Dữ liệu đầu ra phải có thời gian và mã người dùng |

## 7.7. Nhóm từ chỉ định mức độ ưu tiên và logic kiểm thử (Priority & Logic)

| English Phrase                                       | Nghĩa tiếng Việt                                      |
| ---------------------------------------------------- | ----------------------------------------------------- |
| This is a high-priority requirement                  | Đây là yêu cầu ưu tiên cao                            |
| Test cases shall be executed in the following order  | Các test case phải thực thi theo thứ tự sau           |
| This test shall be run in both normal and edge cases | Test này phải chạy trong cả trường hợp thường và biên |
| Dependencies must be resolved before execution       | Các phụ thuộc phải được xử lý trước khi chạy test     |

## 7.8. Nhóm từ mô tả logic điều kiện (Conditional logic)
| English Phrase                                     | Nghĩa tiếng Việt                                       |
| -------------------------------------------------- | ------------------------------------------------------ |
| If the user provides invalid credentials, then...  | Nếu người dùng nhập sai thông tin đăng nhập, thì...    |
| When the input is empty, the system must...        | Khi đầu vào rỗng, hệ thống phải...                     |
| Unless the user is an admin, access must be denied | Trừ khi người dùng là admin, quyền truy cập bị từ chối |
| Only after verification is complete...             | Chỉ sau khi xác thực hoàn tất...                       |

## 🎯 BÀI TẬP THỰC HÀNH – Viết Test Requirement và Test Case
### Bối cảnh bài toán:
Trường Đại học cần xây dựng một hệ thống Quản trị nhân sự nội bộ (HRMS). Chức năng đầu tiên cần phát triển là “Đăng nhập cho nhân viên”. Chức năng này đảm bảo rằng chỉ nhân viên có tài khoản hợp lệ mới có thể truy cập hệ thống, với các điều kiện bảo mật đi kèm.

### 📌 Yêu cầu nghiệp vụ (Business Requirement - BR):
- Người dùng là nhân viên được cấp tài khoản đăng nhập qua email và mật khẩu.
- Sau khi đăng nhập thành công, hệ thống sẽ chuyển đến Trang chính HR.
- Nếu đăng nhập sai, hệ thống phải hiển thị thông báo lỗi.
- Tài khoản bị khóa nếu sai mật khẩu 5 lần liên tiếp.
- Mật khẩu nhập vào phải được mã hóa, không hiển thị rõ.
- Session sẽ tự động hết hạn sau 10 phút không thao tác.

### 🧠 Yêu cầu sinh viên thực hiện:
👉 Nhiệm vụ:
Viết tối thiểu 5 Test Requirements dựa trên yêu cầu nghiệp vụ ở trên.

## ✍️ Gợi ý đáp án mẫu
### 🔶 1. Test Requirements (TR)

| TR ID      | Description                                                                       |
| ---------- | --------------------------------------------------------------------------------- |
| **TR-001** | The system shall allow users to log in using valid email and password.            |
| **TR-002** | The system shall display an error message when invalid credentials are used.      |
| **TR-003** | The system shall lock the user account after 5 consecutive failed login attempts. |
| **TR-004** | The password input field must be masked.                                          |
| **TR-005** | The system shall auto logout the session after 10 minutes of inactivity.          |

**Tiếng việt:**

| ID | Mô tả yêu cầu kiểm thử |
| --- | --- |
| TR-001 | Hệ thống phải cho phép người dùng nhập tên đăng nhập và mật khẩu. |
| TR-002 | Khi nhập đúng tên đăng nhập và mật khẩu, hệ thống chuyển đến trang chủ. |
| TR-003 | Khi nhập sai tên đăng nhập hoặc mật khẩu, hệ thống hiển thị thông báo lỗi. |
| TR-004 | Trường tên đăng nhập và mật khẩu không được để trống. |
| TR-005 | Mật khẩu phải được mã hóa và không hiển thị dưới dạng văn bản thuần. |
### Phân biệt nhanh Test Requirement và Test Case
| Câu hỏi                          | Nếu là Test Requirement | Nếu là Test Case       |
| -------------------------------- | ----------------------- | ---------------------- |
| Nó mô tả gì cần kiểm thử?        | ✅                       | ❌                      |
| Nó mô tả cách kiểm thử?          | ❌                       | ✅                      |
| Có bao gồm bước kiểm tra cụ thể? | ❌                       | ✅                      |
| Có dữ liệu đầu vào cụ thể không? | ❌                       | ✅                      |
| Có kết quả mong đợi?             | ❌ (mức khái quát cao)   | ✅ (cụ thể từng bước)   |
| Dùng để truy vết yêu cầu?        | ✅                       | ✅ (qua mapping đến TR) |
