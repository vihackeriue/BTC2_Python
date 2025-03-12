def tinh_giai_thua(n):
    """Hàm tính giai thừa của số nguyên dương n"""
    if n == 0 or n == 1:
        return 1  # Giai thừa của 0 và 1 đều bằng 1
    else:
        giai_thua = 1
        for i in range(2, n + 1):
            giai_thua *= i  # Nhân dần các số từ 2 đến n
        return giai_thua


# Nhập số nguyên từ người dùng
n = int(input("Nhập số nguyên để tính giai thừa: "))

# Tính giai thừa và hiển thị kết quả
ket_qua = tinh_giai_thua(n)
print(f"Kết quả: {ket_qua}")
