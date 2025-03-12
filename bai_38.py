# Khởi tạo danh sách rỗng cho các nhóm số
negative_numbers = []  # Số âm
zero_numbers = []  # Số 0
positive_numbers = []  # Số dương

# Nhập dữ liệu từ người dùng cho đến khi nhập dòng trống
while True:
    num = input("Nhập số nguyên (nhấn Enter để kết thúc): ").strip()
    if num == "":  # Dừng khi nhập dòng trống
        break
    try:
        num = int(num)  # Chuyển đổi chuỗi thành số nguyên
        if num < 0:
            negative_numbers.append(num)  # Thêm vào danh sách số âm
        elif num == 0:
            zero_numbers.append(num)  # Thêm vào danh sách số 0
        else:
            positive_numbers.append(num)  # Thêm vào danh sách số dương
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ!")

# Ghép danh sách theo thứ tự yêu cầu
sorted_numbers = negative_numbers + zero_numbers + positive_numbers

# Hiển thị kết quả
print("\nCác số được sắp xếp theo nhóm:")
print(*sorted_numbers, sep=", ")
