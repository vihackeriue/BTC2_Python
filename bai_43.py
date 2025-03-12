def in_chuoi_dai_hon(chuoi1, chuoi2):

    do_dai_1 = len(chuoi1)  # Lấy độ dài của chuỗi 1
    do_dai_2 = len(chuoi2)  # Lấy độ dài của chuỗi 2

    if do_dai_1 > do_dai_2:
        print("Chuỗi dài hơn là:", chuoi1)
    elif do_dai_2 > do_dai_1:
        print("Chuỗi dài hơn là:", chuoi2)
    else:
        print("Hai chuỗi có cùng độ dài:")
        print(chuoi1)
        print(chuoi2)


# Nhập hai chuỗi từ người dùng
chuoi_1 = input("Nhập chuỗi thứ nhất: ")
chuoi_2 = input("Nhập chuỗi thứ hai: ")

# Gọi hàm và thực hiện kiểm tra
in_chuoi_dai_hon(chuoi_1, chuoi_2)
