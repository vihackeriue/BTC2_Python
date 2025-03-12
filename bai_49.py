def so_nguyen_to(n):

    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # Kiểm tra từ 2 đến căn bậc hai của n
        if n % i == 0:
            return False
    return True


# Chương trình chính
if __name__ == "__main__":
    # Nhập số từ người dùng
    so = int(input("Nhập một số nguyên: "))

    # Kiểm tra và hiển thị kết quả
    if so_nguyen_to(so):
        print(f"{so} là số nguyên tố.")
    else:
        print(f"{so} không phải là số nguyên tố.")
