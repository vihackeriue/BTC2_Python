def is_perfect_number(n):
    if n < 2:
        return False  # Số nhỏ hơn 2 không thể là số hoàn hảo

    # Tìm tất cả các ước số của n (trừ chính nó)
    sum_divisors = 0

    # Duyệt từ 1 đến n-1 để tìm các ước số
    for i in range(1, n):
        if n % i == 0:  # Nếu i là ước số của n
            sum_divisors += i  # Cộng vào tổng

    return sum_divisors == n  # Trả về True nếu tổng ước số bằng n


# Chương trình chính: Tìm số hoàn hảo trong khoảng từ 1 đến 10.000
if __name__ == "__main__":
    print("Các số hoàn hảo từ 1 đến 10.000 là:")
    for num in range(1, 10001):
        if is_perfect_number(num):
            print(num, end=" ")
