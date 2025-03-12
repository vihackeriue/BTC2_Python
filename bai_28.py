month = input("Nhập tên tháng: ")


days_in_month = {
    "T1": 31,
    "T2": "28 hoặc 29",
    "T3": 31,
    "T4": 30,
    "T5": 31,
    "T6": 30,
    "T7": 31,
    "T8": 31,
    "T9": 30,
    "T10": 31,
    "T11": 30,
    "T12": 31,
}


if month in days_in_month:
    print(f"Tháng {month} có {days_in_month[month]} ngày.")
else:
    print("Lỗi: Vui lòng nhập đúng tên tháng bằng tiếng Anh, viết hoa chữ cái đầu.")
