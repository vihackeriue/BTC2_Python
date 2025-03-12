# Khởi tạo danh sách rỗng
numbers = []

# Nhập số từ người dùng cho đến khi nhập 0
while True:
    num = int(input("Nhập số nguyên (nhập 0 để kết thúc): "))
    if num == 0:
        break  # Thoát vòng lặp khi nhập 0
    numbers.append(num)  # Thêm số vào danh sách

# Sắp xếp danh sách theo thứ tự tăng dần
numbers.sort()

# Hiển thị danh sách đã sắp xếp, mỗi số trên một dòng
print("\nCác số đã nhập (sắp xếp tăng dần):")
for num in numbers:
    print(num)
