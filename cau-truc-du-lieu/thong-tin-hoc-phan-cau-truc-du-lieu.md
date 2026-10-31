# ĐỀ CƯƠNG CHI TIẾT HỌC PHẦN
## CẤU TRÚC DỮ LIỆU VÀ GIẢI THUẬT (MODERN DATA STRUCTURES & AI EVALUATION)

* **Mã học phần:** 111162
* **Học phần tiên quyết:** Kỹ thuật lập trình (111161)
* **Thời lượng:** 60 tiết (12 buổi × 5 tiết/buổi | 15 LT + 45 TH)
* **Phương pháp giảng dạy chủ đạo:** Benchmark-Driven Vibe Coding & AI Evaluation
* **Ngôn ngữ/Công cụ:** Python 3 (NumPy/Pandas cơ bản cho DS/AI), VS Code, Git/GitHub, AI Benchmark Tools

---

## I. THÔNG TIN CHUNG & MỤC TIÊU KSA

### 1. Trọng tâm học phần
Tập trung vào các **Cấu trúc Dữ liệu Hiện đại cho bài toán CNTT, AI và Khoa học Dữ liệu**; kết hợp với kỹ thuật **AI Code Review & Benchmarking** (Đánh giá độ phức tạp và hiệu năng thực tế).

### 2. Mục tiêu KSA (Knowledge - Skills - Attitude)
* **Knowledge (Kiến thức):** Nắm vững DSA kinh điển (Array, LinkedList, Stack, Queue, Tree, Graph) và DSA hiện đại phục vụ AI/Data Science (Matrix/Tensor, Hash Table, Vector Embeddings cơ bản, KD-Tree/Spatial Data). Hiểu sâu sắc độ phức tạp Big-O ($O(1), O(N), O(N \log N)$).
* **Skills (Kỹ năng):**
  * Vibe Coding các cấu trúc dữ liệu và giải thuật phức tạp.
  * Sử dụng AI để **Review Code**, phát hiện lỗi tiềm ẩn (Infinite Loop, Memory Leak, Index Error) và đánh giá độ phức tạp Time/Space Complexity.
  * Đo đạc hiệu năng thực tế (Benchmarking) bằng script Python trên dữ liệu lớn.
* **Attitude (Thái độ):** Tư duy tối ưu hóa mã nguồn, luôn hướng đến hiệu năng cao nhất cho hệ thống dữ liệu.

---

## II. KẾ HOẠCH GIẢNG DẠY CHI TIẾT (12 BUỔI × 5 TIẾT)

> **Phương pháp Benchmark-Driven:** 1 tiết định hướng giải thuật + 4 tiết thực hành Vibe Coding, đo đạc hiệu năng và AI Code Review.

| Buổi | Chủ đề chính | Nội dung thực hành (Hands-on) | Kỹ năng AI Review & Benchmarking |
| :---: | :--- | :--- | :--- |
| **1** | **Phân tích Big-O & Setup Đo đạc Hiệu năng** | Đánh giá Big-O ($O(1), O(N), O(N^2)$); Viết script đo thời gian chạy (`timeit`) & bộ nhớ (`memory_profiler`); Git Setup. | Ra lệnh cho AI phân tích độ phức tạp Big-O và phản biện lại phân tích của AI. |
| **2** | **Mảng Đa chiều, Ma trận & Tensor (Nền tảng DS/AI)** | Thao tác Ma trận/Tensor bằng NumPy/List; Kỹ thuật Vectorization thay thế vòng lặp tốn thời gian; Sliding Window trên dữ liệu. | Yêu cầu AI review mã nguồn: So sánh hiệu năng giữa Vòng lặp thuần vs Vectorization. |
| **3** | **Danh sách liên kết (Linked List) & Bộ nhớ** | Cài đặt Single/Double LinkedList; Đánh giá việc cấp phát bộ nhớ động vs Mảng liên tục trong xử lý dữ liệu. | Dùng AI trực quan hóa (visualize) luồng trỏ bộ nhớ và refactor code trỏ pointer sạch. |
| **4** | **Ngăn xếp (Stack), Hàng đợi (Queue) & Priority Queue** | Cài đặt Stack/Queue; Hàng đợi ưu tiên (Priority Queue/Heap) – Ứng dụng trong lập lịch tác vụ AI và thuật toán A\*. | Dùng AI kiểm tra lỗi Overflow/Underflow và review cách cài đặt Heap tối ưu. |
| **5** | **Bảng băm (Hash Table) & Tìm kiếm Dữ liệu Nhanh** | Cài đặt Hash Table, giải quyết đụng độ; Ứng dụng Bảng băm trong Indexing dữ liệu, Caching và Đếm tần suất từ (NLP). | Hướng dẫn AI tạo các Test Case đặc biệt (Edge Cases) để kiểm thử đụng độ hàm băm. |
| **6** | **Thuật toán Sắp xếp & Xử lý Dữ liệu Lớn** | QuickSort, MergeSort, RadixSort; Sắp xếp dữ liệu đa thuộc tính trong Khoa học dữ liệu; Benchmark trên tập $N = 500.000$. | Dùng AI giải thích các trường hợp xấu nhất của giải thuật và gợi ý cách tối ưu Pivot. |
| **7** | **Kiểm tra giữa kỳ (Thực hành DSA trên Git)** | **Bài kiểm tra cá nhân (5 tiết):** Vibe Coding giải quyết 2 bài toán xử lý dữ liệu; Push code & báo cáo Benchmark lên GitHub. | Đánh giá kỹ năng kiểm soát AI, tối ưu Big-O và thao tác Git Repository. |
| **8** | **Cây Tìm kiếm (BST, KD-Tree) cho Khoa học Dữ liệu** | Cây BST, Cây KD-Tree (Cấu trúc tìm kiếm láng giềng gần nhất - KNN trong AI/Data Science); Các phép duyệt cây. | Sử dụng AI hỗ trợ vẽ sơ đồ cây và review tính cân bằng của cây dữ liệu. |
| **9** | **Đồ thị (Graph) & Ứng dụng trong Social Network / AI** | Biểu diễn Đồ thị (Adjacency Matrix/List); BFS, DFS; Ứng dụng phân tích mạng xã hội và Graph Neural Network cơ bản. | Yêu cầu AI kiểm tra lỗi lặp vô hạn (Infinite Loop) khi duyệt đồ thị phức tạp. |
| **10** | **Thuật toán Đường đi Ngắn nhất & Recommendation Engine** | Thuật toán Dijkstra, A\*; Ứng dụng gợi ý tuyến đường và tìm kiếm khoảng cách trong không gian đặc trưng (Feature Space). | Phân tích bài toán, giao AI sinh code khung, sinh viên review và tối ưu độ phức tạp. |
| **11** | **Cấu trúc Dữ liệu Vector & Similarity Search (AI Modern)** | Khái niệm Vector Embedding; Cấu trúc dữ liệu tìm kiếm độ tương đồng (Cosine Similarity, Euclidean Distance) cho AI/RAG. | Dùng AI để Vibe Coding ứng dụng tìm kiếm tài liệu tương đồng bằng Vector đơn giản. |
| **12** | **Showcase Báo cáo Đồ án DSA & Git Benchmark** | Demo Data/AI Engine, trình bày Báo cáo Benchmarking (Đo đạc Time/Space), bảo vệ Git History & Code Review. | Chứng minh sinh viên làm chủ thuật toán, AI chỉ đóng vai trò hỗ trợ kiểm thử và gợi ý tối ưu. |

---

## III. PHƯƠNG PHÁP ĐÁNH GIÁ & ĐIỂM CỘNG TRUYỀN THÔNG

### 1. Thang điểm đánh giá
* **Đồ án Module Giải thuật / Data Engine (70%):** Sản phẩm xử lý dữ liệu lớn/AI chạy mượt mà, cấu trúc DSA tối ưu.
* **Nhật ký AI Review & Benchmarking (20%):** Báo cáo đo đạc hiệu năng Time/Space Complexity và phân tích code do AI tối ưu.
* **Thái độ & Lịch sử Git (10%):** Commit code đều đặn, quản lý repo khoa học.

### 2. Điểm cộng Truyền thông Tuyển sinh 2027 (Bonus +1.0 đến +1.5 điểm)
* **Hình thức:** Bài viết/Video giải thích 1 thuật toán trực quan hoặc khoe GitHub Repo dữ liệu nhóm.
* **Hashtag bắt buộc:** `#CauTrucDuLieuVaGiaiThuat` `#DataScienceDS` `#AlgorithmBenchmarking` `#TuyenSinh2027` `#TenTruong_TenNganh`