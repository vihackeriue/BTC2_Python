def tao_danh_sach_binh_phuong():
    """Hàm tạo và in danh sách chứa bình phương của các số từ 1 đến 20."""

    danh_sach = []  # Khởi tạo danh sách rỗng

    for i in range(1, 21):  # Lặp từ 1 đến 20
        danh_sach.append(i**2)  # Thêm bình phương của i vào danh sách

    print("Danh sách bình phương từ 1 đến 20:", danh_sach)


# Gọi hàm để thực thi
tao_danh_sach_binh_phuong()
