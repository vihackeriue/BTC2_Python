def caesar_cipher(text, shift, mode="encrypt"):
    result = ""

    # Đảo chiều dịch chuyển nếu giải mã
    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():  # Kiểm tra nếu là chữ cái
            shift_base = ord("A") if char.isupper() else ord("a")
            new_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result += new_char
        else:
            result += char  # Giữ nguyên ký tự không phải chữ cái

    return result


# Nhập tin nhắn từ người dùng
message = input("Nhập tin nhắn: ")
shift = int(input("Nhập số ký tự dịch chuyển: "))
mode = input("Chọn chế độ (encrypt/decrypt): ").strip().lower()

# Kiểm tra chế độ hợp lệ
if mode not in ["encrypt", "decrypt"]:
    print("Lựa chọn không hợp lệ! Vui lòng nhập 'encrypt' hoặc 'decrypt'.")
else:
    # Mã hóa hoặc giải mã
    result_message = caesar_cipher(message, shift, mode)
    print("Kết quả:", result_message)
