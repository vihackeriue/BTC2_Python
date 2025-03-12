num_sides = int(input("Nhập số cạnh của hình (từ 3 đến 10): "))

shapes = {
    3: "Hình tam giác",
    4: "Hình tứ giác",
    5: "Hình ngũ giác",
    6: "Hình lục giác",
    7: "Hình thất giác",
    8: "Hình bát giác",
    9: "Hình cửu giác",
    10: "Hình thập giác",
}

if num_sides in shapes:
    print(f"Hình có {num_sides} cạnh là {shapes[num_sides]}.")
else:
    print("Lỗi: Chương trình chỉ hỗ trợ các hình từ 3 đến 10 cạnh.")
