@echo off
chcp 65001 > nul
title Khoa CNTT - LHU: Cổng Học Phần Trực Tuyến
echo =====================================================================
echo  KHOA CÔNG NGHỆ THÔNG TIN - ĐẠI HỌC LẠC HỒNG (LHU)
echo  CỔNG TỔNG HỢP HỌC PHẦN TRỰC TUYẾN - AUTO-DISCOVERY PORTAL
echo =====================================================================
echo.
echo Đang quét danh mục học phần mới nhất...

:: Tự động chạy quét thư mục
uv run python scan-courses.py > nul 2>&1
if %errorlevel% neq 0 (
    python scan-courses.py > nul 2>&1
)

echo Đang khởi động máy chủ nội bộ tại http://localhost:8000 ...
echo Khi bạn thêm thư mục học phần mới (chứa file index.html),
echo hệ thống sẽ TỰ ĐỘNG nhận diện và hiển thị khi bạn tải lại trang web!
echo.
echo Nhấn Ctrl + C để dừng máy chủ khi không sử dụng.
echo =====================================================================

:: Mở trình duyệt mặc định sau 1.5 giây
start "" http://localhost:8000/index.html

:: Chạy máy chủ qua uv python hoặc python
uv run python -m http.server 8000
if %errorlevel% neq 0 (
    python -m http.server 8000
)

pause

