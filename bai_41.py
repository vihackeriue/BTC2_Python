# Bước 1: Khai báo tuple ban đầu
original_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Bước 2: Tạo một danh sách chứa các số chẵn từ tuple ban đầu
even_numbers_list = []
for num in original_tuple:
    if num % 2 == 0:  # Kiểm tra nếu số đó là số chẵn
        even_numbers_list.append(num)  # Thêm số chẵn vào danh sách

# Bước 3: Chuyển danh sách thành tuple
even_numbers_tuple = tuple(even_numbers_list)

# Bước 4: Hiển thị kết quả
print("Tuple chứa các số chẵn:", even_numbers_tuple)
