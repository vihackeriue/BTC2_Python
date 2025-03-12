# Nhập năm từ người dùng
year = int(input("Nhập một năm: "))

# Kiểm tra năm nhuận
if year % 400 == 0:
    print(f"{year} là năm nhuận.")
elif year % 100 == 0:
    print(f"{year} không phải là năm nhuận.")
elif year % 4 == 0:
    print(f"{year} là năm nhuận.")
else:
    print(f"{year} không phải là năm nhuận.")
