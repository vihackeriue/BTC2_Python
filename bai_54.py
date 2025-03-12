def format_word_list(words):

    if not words:
        return ""  # Trả về chuỗi rỗng nếu danh sách trống
    elif len(words) == 1:
        return words[0]  # Nếu chỉ có 1 từ, trả về chính từ đó
    elif len(words) == 2:
        return f"{words[0]} and {words[1]}"  # Nếu có 2 từ, nối bằng "and"
    else:
        return (
            f"{', '.join(words[:-1])} and {words[-1]}"  # Danh sách có từ 3 từ trở lên
        )


def main():

    # Nhập danh sách từ từ người dùng, phân tách bởi dấu phẩy
    user_input = input("Nhập danh sách các từ (cách nhau bằng dấu phẩy): ")

    # Chuyển chuỗi nhập vào thành danh sách (loại bỏ khoảng trắng)
    words = [word.strip() for word in user_input.split(",") if word.strip()]

    # Gọi hàm để định dạng danh sách
    formatted_string = format_word_list(words)

    # Hiển thị kết quả
    print("Chuỗi đã định dạng:", formatted_string)


# Chạy chương trình chính
if __name__ == "__main__":
    main()
