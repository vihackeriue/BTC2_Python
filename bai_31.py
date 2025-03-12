# Nhập tin nhắn từ người dùng
message = input("Nhập tin nhắn cần mã hóa: ")
shift = 3
# Mã hóa tin nhắn
result = ""
for char in message:
    if char.isalpha():  # Kiểm tra nếu là chữ cái
        shift_base = ord("A") if char.isupper() else ord("a")
        new_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
        result += new_char
    else:
        result += char  # Giữ nguyên ký tự không phải chữ cái


# Hiển thị kết quả
print("Tin nhắn đã mã hóa:", result)
