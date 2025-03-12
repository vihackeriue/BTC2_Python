# Khởi tạo danh sách rỗng để lưu các từ
words = []
seen = set()  # Sử dụng tập hợp để kiểm tra từ trùng lặp

# Nhập dữ liệu từ người dùng cho đến khi nhập dòng trống
while True:
    word = input("Nhập từ (nhấn Enter để kết thúc): ").strip()
    if word == "":  # Dừng khi người dùng nhập dòng trống
        break
    if word not in seen:  # Kiểm tra nếu từ chưa xuất hiện trước đó
        words.append(word)  # Thêm vào danh sách kết quả
        seen.add(word)  # Đánh dấu từ đã xuất hiện

# Hiển thị kết quả
print("\nDanh sách từ không trùng lặp:")
for word in words:
    print(word)
