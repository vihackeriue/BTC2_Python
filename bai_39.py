n = int(input("Nhập số nguyên dương n: "))

square_dict = {}

for i in range(1, n + 1):
    square_dict[i] = i * i

print("Dictionary chứa bình phương của các số từ 1 đến", n, "là:")
print(square_dict)
