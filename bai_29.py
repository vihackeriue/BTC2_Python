a = float(input("Nhập độ dài cạnh thứ 1: "))
b = float(input("Nhập độ dài cạnh thứ 2: "))
c = float(input("Nhập độ dài cạnh thứ 3: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Tam giác đều")
    elif a == b or a == c or b == c:
        print("Tam giác cân")
    else:
        print("Tam giác thường")
else:
    print("Ba cạnh không tạo thành một tam giác hợp lệ.")
