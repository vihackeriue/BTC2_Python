numbers = list(
    map(int, input("Nhập danh sách số, cách nhau bởi dấu phẩy: ").split(","))
)
odd_numbers = []
for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)

# Hiển thị kết quả
print("Danh sách số lẻ:", odd_numbers)
