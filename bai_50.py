import random


def generate_random_password():

    # Chọn độ dài ngẫu nhiên cho mật khẩu
    password_length = random.randint(7, 10)

    # Tạo danh sách chứa các ký tự của mật khẩu
    password_chars = []
    for _ in range(password_length):
        random_char = chr(random.randint(33, 126))  # Chuyển mã ASCII thành ký tự
        password_chars.append(random_char)

    # Ghép các ký tự thành chuỗi mật khẩu
    password = "".join(password_chars)

    return password  # Trả về mật khẩu ngẫu nhiên


# Chương trình chính
if __name__ == "__main__":
    random_password = generate_random_password()
    print("Mật khẩu ngẫu nhiên được tạo:", random_password)
