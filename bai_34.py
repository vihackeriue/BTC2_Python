def decimal_to_binary(n):
    if n == 0:
        return "0"  # Trường hợp đặc biệt cho số 0

    binary = ""
    while n > 0:
        binary = str(n % 2) + binary  # Lấy phần dư và ghép vào trước
        n = n // 2  # Chia nguyên cho 2

    return binary


# Nhập số thập phân từ người dùng
decimal_number = int(input("Nhập số nguyên thập phân: "))

# Chuyển đổi và hiển thị kết quả
binary_result = decimal_to_binary(decimal_number)
print(f"Số {decimal_number} trong hệ nhị phân là: {binary_result}")
