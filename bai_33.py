def is_palindrome(s):
    s = s.lower()  # Chuyển về chữ thường để so sánh không phân biệt hoa thường
    length = len(s)

    for i in range(length // 2):  # Chỉ cần kiểm tra nửa đầu chuỗi
        if s[i] != s[length - i - 1]:
            return False  # Nếu có ký tự không khớp, không phải Palindrome

    return True  # Nếu vòng lặp hoàn tất mà không có lỗi, là Palindrome


text = input("Nhập chuỗi cần kiểm tra: ").strip()

if is_palindrome(text):
    print(f"Chuỗi '{text}' là một Palindrome!")
else:
    print(f"Chuỗi '{text}' không phải là một Palindrome.")
