# Đoạn 4: nhập điểm tới khi bấm Enter, rồi tính trung bình.
# Chạy thử hai lần: lần 1 nhập 8, 7, Enter; lần 2 bấm Enter ngay.
diem_list = []
while True:
    s = input("Nhập điểm (Enter để dừng): ")
    if s == "":
        break
    diem_list.append(float(s))
tb = sum(diem_list) / len(diem_list)
print(f"Trung bình: {tb:.2f}")
