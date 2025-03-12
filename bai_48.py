def tinh_trung_binh(a, b, c):
    """Hàm tính giá trị trung bình của ba số."""
    return (a + b + c) / 3


# Chương trình chính
if __name__ == "__main__":
    # Nhập ba số từ người dùng
    so1 = float(input("Nhập số thứ nhất: "))
    so2 = float(input("Nhập số thứ hai: "))
    so3 = float(input("Nhập số thứ ba: "))

    # Gọi hàm tính trung bình
    ket_qua = tinh_trung_binh(so1, so2, so3)

    # Hiển thị kết quả
    print(f"Giá trị trung bình của {so1}, {so2}, {so3} là: {ket_qua:.2f}")
