# Nhập một chữ cái từ người dùng
letter = input("Nhập một chữ cái: ").lower()

# Kiểm tra loại chữ cái
if letter in ("a", "e", "i", "o", "u"):
    print(f"'{letter}' là một nguyên âm.")
elif letter == "y":
    print(f"'{letter}' có thể là nguyên âm hoặc phụ âm.")
else:
    print(f"'{letter}' là một phụ âm.")
