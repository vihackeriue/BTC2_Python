def is_strong_password(password):

    # Kiểm tra độ dài mật khẩu (phải từ 8 ký tự trở lên)
    if len(password) < 8:
        return False

    # Kiểm tra có ít nhất 1 chữ cái viết hoa không
    has_upper = any(char.isupper() for char in password)

    # Kiểm tra có ít nhất 1 chữ cái viết thường không
    has_lower = any(char.islower() for char in password)

    # Kiểm tra có ít nhất 1 chữ số không
    has_digit = any(char.isdigit() for char in password)

    # Trả về kết quả cuối cùng (phải thỏa mãn cả 3 điều kiện trên)
    return has_upper and has_lower and has_digit


# Chương trình chính
if __name__ == "__main__":
    # Nhập mật khẩu từ người dùng
    user_password = input("Nhập mật khẩu của bạn: ")

    # Kiểm tra xem mật khẩu có mạnh không
    if is_strong_password(user_password):
        print("Mật khẩu của bạn là MẠNH!")
    else:
        print("Mật khẩu của bạn KHÔNG đủ mạnh. Hãy thử lại!")
