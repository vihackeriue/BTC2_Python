# Bước 1: Khai báo tuple ban đầu
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Bước 2: Xác định vị trí giữa của tuple
mid_index = len(numbers) // 2  # Chia đôi tuple

# Bước 3: Tạo hai phần
first_half = numbers[:mid_index]  # Lấy nửa đầu
second_half = numbers[mid_index:]  # Lấy nửa sau

# Bước 4: In kết quả
print("Nửa đầu:", first_half)
print("Nửa sau:", second_half)
