# Đoạn 5: tính điểm trung bình của 4 học phần.
# Chương trình chạy không báo lỗi. Kết quả có đúng không?
diem_list = [8, 6.5, 9, 7]
for d in diem_list:
    tong = 0
    tong = tong + d
tb = tong / len(diem_list)
print(f"Trung bình: {tb:.2f}")
