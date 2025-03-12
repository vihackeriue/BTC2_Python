def tao_danh_sach_va_in_tru_5_phan_tu_dau():
    """Hàm tạo danh sách bình phương từ 1 đến 20 và in trừ 5 phần tử đầu tiên."""

    danh_sach = []  # Khởi tạo danh sách rỗng

    for i in range(1, 21):  # Lặp từ 1 đến 20
        danh_sach.append(i**2)  # Thêm bình phương của i vào danh sách

    # In danh sách trừ 5 phần tử đầu tiên
    print("Danh sách sau khi bỏ 5 phần tử đầu:", danh_sach[5:])


# Gọi hàm để thực thi
tao_danh_sach_va_in_tru_5_phan_tu_dau()
