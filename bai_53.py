def generate_sublists(lst):
    # Nếu danh sách đầu vào rỗng, chỉ có một danh sách con duy nhất là danh sách rỗng []
    if not lst:
        return [[]]

    # Bước 1: Lấy phần tử đầu tiên của danh sách
    first_element = lst[0]

    # Bước 2: Gọi đệ quy để lấy tất cả danh sách con của phần còn lại (trừ phần tử đầu tiên)
    smaller_sublists = generate_sublists(lst[1:])

    # Bước 3: Tạo danh sách mới bằng cách thêm first_element vào từng danh sách con đã có
    new_sublists = []
    for sublist in smaller_sublists:
        new_sublist = [
            first_element
        ] + sublist  # Thêm phần tử đầu tiên vào danh sách con
        new_sublists.append(new_sublist)

    # Bước 4: Gộp tất cả danh sách con lại và trả về
    return smaller_sublists + new_sublists


lst = [1, 2, 3]
sublists = generate_sublists(lst)
print(sublists)
