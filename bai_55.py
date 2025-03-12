import zipfile


def compress_files(zip_name, file_list):
    """
    Hàm nén các tệp vào một tệp ZIP.

    Tham số:
    - zip_name (str): Tên tệp ZIP đầu ra.
    - file_list (list): Danh sách các tệp cần nén.

    Trả về:
    - Không trả về gì, nhưng tạo tệp ZIP.
    """
    try:
        with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zipf:
            for file in file_list:
                zipf.write(file)
                print(f"Đã nén: {file}")
        print(f"\nTạo thành công tệp ZIP: {zip_name}")
    except Exception as e:
        print(f"Lỗi khi nén tệp: {e}")


def decompress_files(zip_name, extract_path):
    """
    Hàm giải nén tệp ZIP vào thư mục chỉ định.

    Tham số:
    - zip_name (str): Đường dẫn tệp ZIP cần giải nén.
    - extract_path (str): Thư mục để lưu các tệp sau khi giải nén.

    Trả về:
    - Không trả về gì, nhưng giải nén tất cả các tệp từ ZIP.
    """
    try:
        with zipfile.ZipFile(zip_name, "r") as zipf:
            zipf.extractall(extract_path)
            print(f"\n📂 Đã giải nén vào thư mục: {extract_path}")
    except Exception as e:
        print(f"Lỗi khi giải nén tệp: {e}")


import os


def main():
    """
    Chương trình chính:
    - Cho phép người dùng chọn chế độ: Nén hoặc Giải nén.
    - Nhập đường dẫn và gọi các hàm xử lý tương ứng.
    """
    while True:
        print("\nChương trình Nén/Giải Nén Tệp")
        print("1. Nén tệp")
        print("2. Giải nén tệp")
        print("3. Thoát")

        choice = input("Chọn một tùy chọn (1/2/3): ")

        if choice == "1":
            zip_name = input("Nhập tên tệp ZIP đầu ra (ví dụ: files.zip): ")
            files = input(
                "Nhập danh sách các tệp cần nén (cách nhau bởi dấu phẩy): "
            ).split(",")
            files = [file.strip() for file in files]  # Xóa khoảng trắng thừa
            compress_files(zip_name, files)

        elif choice == "2":
            zip_name = input("Nhập đường dẫn tệp ZIP cần giải nén: ")
            extract_path = input("Nhập thư mục lưu trữ tệp sau khi giải nén: ")
            os.makedirs(extract_path, exist_ok=True)  # Tạo thư mục nếu chưa có
            decompress_files(zip_name, extract_path)

        elif choice == "3":
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ! Vui lòng nhập 1, 2 hoặc 3.")


if __name__ == "__main__":
    main()
