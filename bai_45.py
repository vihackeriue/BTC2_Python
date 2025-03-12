def tao_danh_sach_va_in_5_phan_tu_dau():
    """Hàm tạo danh sách bình phương từ 1 đến 20 và in 5 phần tử đầu tiên."""

    danh_sach = []  # Khởi tạo danh sách rỗng

    for i in range(1, 21):  # Lặp từ 1 đến 20
        danh_sach.append(i**2)  # Thêm bình phương của i vào danh sách

    # In 5 phần tử đầu tiên trong danh sách
    print("5 phần tử đầu tiên:", danh_sach[:5])


# Gọi hàm để thực thi
tao_danh_sach_va_in_5_phan_tu_dau()
