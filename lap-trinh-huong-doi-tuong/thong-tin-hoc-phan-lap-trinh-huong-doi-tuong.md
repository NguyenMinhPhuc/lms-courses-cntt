# ĐỀ CƯƠNG CHI TIẾT HỌC PHẦN
## LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG (OOP, DESIGN PATTERNS & AI ARCHITECTURE)

* **Mã học phần:** 111163
* **Học phần tiên quyết:** Kỹ thuật lập trình (111161)
* **Thời lượng:** 60 tiết (12 buổi × 5 tiết/buổi | 15 LT + 45 TH)
* **Phương pháp giảng dạy chủ đạo:** Architecture-First Vibe Coding & Gitflow Advanced
* **Ngôn ngữ/Công cụ:** Python 3 (Advanced OOP), VS Code, Draw.io / Mermaid (UML), Git/GitHub, AI Architecture Reviewer

---

## I. THÔNG TIN CHUNG & MỤC TIÊU KSA

### 1. Trọng tâm học phần
Tập trung vào **Khái niệm, Phương pháp OOP trong Phân tích và Lập trình**, ứng dụng các **Design Patterns kinh điển** và kỹ thuật **AI Architecture Review** để thiết kế kiến trúc phần mềm chuyên nghiệp.

### 2. Mục tiêu KSA (Knowledge - Skills - Attitude)
* **Knowledge (Kiến thức):** Nắm vững 4 trụ cột OOP (Abstraction, Encapsulation, Inheritance, Polymorphism), Nguyên lý thiết kế SOLID và các Mẫu thiết kế phần mềm (Design Patterns: Singleton, Factory, Observer, Strategy, Adapter...).
* **Skills (Kỹ năng):**
  * Phân tích hệ thống và thiết kế Sơ đồ lớp (UML Class Diagram) trước khi code.
  * Vibe Coding hệ thống hướng đối tượng phức tạp, chia lớp/module chặt chẽ.
  * Sử dụng AI làm **Architecture Reviewer**: Kiểm tra tuân thủ nguyên lý SOLID, phát hiện Code Smells (mã thối) và tiêm phụ thuộc (Dependency Injection).
* **Attitude (Thái độ):** Tư duy của một Kiến trúc sư Phần mềm (Software Architect), coi trọng tính mở rộng, khả năng tái sử dụng và dễ bảo trì của hệ thống.

---

## II. KẾ HOẠCH GIẢNG DẠY CHI TIẾT (12 BUỔI × 5 TIẾT)

> **Phương pháp Architecture-First:** 1 tiết định hướng thiết kế OOP/SOLID + 4 tiết thực hành Vibe Coding, vẽ UML và AI Review Kiến trúc.

| Buổi | Chủ đề chính | Nội dung thực hành (Hands-on) | Kỹ năng AI Review & Architecture |
| :---: | :--- | :--- | :--- |
| **1** | **Tư duy Đối tượng & Thiết kế Sơ đồ UML Class** | Phân tích bài toán thực tế thành Class, Attribute, Method; Vẽ sơ đồ UML (Draw.io/Mermaid); Setup Gitflow nhóm. | Ra lệnh cho AI phân tích mô tả bài toán và đề xuất mã Mermaid vẽ sơ đồ UML. |
| **2** | **Tính Đóng gói (Encapsulation) & Access Modifiers** | Cài đặt Private/Protected/Public (`_`, `__`); Viết Getter/Setter (`@property`); Đóng gói toàn bộ logic truy xuất dữ liệu. | Yêu cầu AI review mã nguồn để phát hiện các vi phạm về rò rỉ dữ liệu (Data Leaks). |
| **3** | **Tính Kế thừa (Inheritance) & Ghi đè (Overriding)** | Xây dựng mối quan hệ Đơn/Đa kế thừa; Sử dụng `super()`; Ghi đè phương thức (Method Overriding) & Abstract Class. | Dùng AI kiểm tra tính hợp lý của mối quan hệ "IS-A" và gợi ý refactor tránh thừa kế sai. |
| **4** | **Tính Đa hình (Polymorphism) & Duck Typing** | Áp dụng Đa hình qua Nạp chồng/Ghi đè; Duck Typing trong Python; Xây dựng các Interface nhận tham số kiểu Lớp cha. | Đưa AI làm bài test: Đánh giá xem đoạn code đã đạt được tính Đa hình và lỏng lẻo (Loose Coupling) chưa. |
| **5** | **Tính Trừu tượng (Abstraction) & Interface** | Xây dựng Abstract Base Classes (ABC); Định nghĩa Interface chuẩn cho các module; Đảm bảo tính mở rộng hệ thống. | Sử dụng AI để Review mã nguồn: Kiểm tra xem các Lớp con đã cài đặt đầy đủ Interface chưa. |
| **6** | **Nguyên lý SOLID (Phần 1: S - O - L)** | Thực hành refactor code vi phạm SOLID: Single Responsibility, Open/Closed, Liskov Substitution. | Ra lệnh cho AI đánh giá mức độ tuân thủ SOLID của một class và gợi ý phương án chia nhỏ. |
| **7** | **Kiểm tra Giữa kỳ (Thực hành OOP & Git PR)** | **Bài kiểm tra cá nhân (5 tiết):** Thiết kế UML và cài đặt hệ thống OOP nhỏ; Tạo Pull Request trên GitHub để nộp bài. | Đánh giá tư duy thiết kế OOP, kỹ năng phân nhánh Git (Branching) và làm chủ mã nguồn. |
| **8** | **Nguyên lý SOLID (Phần 2: I - D) & Dependency Injection** | Interface Segregation, Dependency Inversion; Kỹ thuật Tiêm phụ thuộc (Dependency Injection) giảm độ phụ thuộc cứng. | Yêu cầu AI kiểm tra tính phụ thuộc cứng (Hard Coupling) và viết lại code dạng Dependency Injection. |
| **9** | **Mẫu thiết kế Creational Patterns (Singleton, Factory)** | Cài đặt Singleton Pattern (Quản lý kết nối DB/Config); Cài đặt Factory Pattern (Khởi tạo đối tượng linh hoạt). | Dùng AI giải thích ưu/nhược điểm của Singleton/Factory trong bài toán thực tế và review cách cài đặt. |
| **10** | **Mẫu thiết kế Behavioral & Structural Patterns** | Cài đặt Observer Pattern (Hệ thống thông báo/Event); Strategy Pattern (Thuật toán linh hoạt); Adapter Pattern (Kết nối module cũ/mới). | Hướng dẫn AI kiểm tra xem code có vi phạm nguyên lý thiết kế khi thêm tính năng mới hay không. |
| **11** | **Tích hợp Hệ thống OOP, Persistence & Git Release** | Kết nối OOP với File JSON/Database (SQLite); Hoàn thiện ứng dụng Desktop/Web; Đóng gói phiên bản v1.0 trên GitHub Release. | Sử dụng AI rà soát tổng thể mã nguồn (Static Code Analysis), phát hiện Code Smells và sửa chuẩn PEP8. |
| **12** | **Showcase Báo cáo Đồ án OOP & Git Architecture** | Thuyết trình sơ đồ UML, Demo hệ thống OOP, bảo vệ các quyết định thiết kế kiến trúc và quy trình Gitflow nhóm. | Phản biện trực tiếp với giảng viên về lý do lựa chọn Design Pattern và chứng minh sự kiểm soát AI 100%. |

---

## III. PHƯƠNG PHÁP ĐÁNH GIÁ & ĐIỂM CỘNG TRUYỀN THÔNG

### 1. Thang điểm đánh giá
* **Sản phẩm Đồ án Hệ thống OOP (70%):** Phần mềm OOP hoàn chỉnh có sơ đồ UML chuẩn, áp dụng đúng các nguyên lý SOLID và Design Patterns.
* **Nhật ký AI Architecture & Code Review (20%):** Báo cáo phân tích kiến trúc và các phiên Review code bằng AI.
* **Thái độ & Gitflow (10%):** Quy trình làm việc nhóm chuyên nghiệp trên GitHub (Branching, Pull Request, Review).

### 2. Điểm cộng Truyền thông Tuyển sinh 2027 (Bonus +1.0 đến +1.5 điểm)
* **Hình thức:** Bài viết/Video public chia sẻ Sơ đồ UML + Demo phần mềm OOP của nhóm.
* **Hashtag bắt buộc:** `#LapTrinhHuongDoiThuong` `#OOPSOLID` `#DesignPatterns` `#TuyenSinh2027` `#TenTruong_TenNganh`