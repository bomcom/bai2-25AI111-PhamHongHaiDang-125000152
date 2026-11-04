"""
BÀI TẬP 3: LÀM VIỆC VỚI DỮ LIỆU KHÔNG ĐỒNG NHẤT (MỨC ĐỘ: TRUNG BÌNH - DICT "KIỂU HASHTABLE")
Mô phỏng rủi ro và cách kiểm soát khi lưu trữ nhiều kiểu dữ liệu khác nhau trong cùng một dict.
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def add_unique(d: dict, key, value) -> None:
    """Mô phỏng Hashtable.Add(): ném ngoại lệ nếu key đã tồn tại."""
    if key in d:
        raise KeyError(f"Khóa '{key}' đã tồn tại trong dict.")
    d[key] = value


def main():
    print("=== BÀI TẬP 3: DỮ LIỆU KHÔNG ĐỒNG NHẤT (DICT KIỂU HASHTABLE) ===")
    product_info = {}

    # 1. Thêm dữ liệu bằng hàm add_unique (báo lỗi nếu trùng khóa)
    add_unique(product_info, "ID", 101)
    add_unique(product_info, "Name", "Laptop Pro AI")
    add_unique(product_info, "Price", 2500.50)
    add_unique(product_info, "IsAvailable", True)

    # 2. Đọc và kiểm tra kiểu an toàn (Safe type checking)
    try:
        id_ = product_info["ID"]
        name = product_info["Name"]
        price = product_info["Price"]
        is_available = product_info["IsAvailable"]

        # Kiểm tra kiểu chủ động để tránh TypeError runtime
        if not isinstance(price, (int, float)):
            raise TypeError("Price phải là kiểu số (int hoặc float).")

        print("\n--- Thông tin sản phẩm ---")
        print(f"ID:         {id_}")
        print(f"Tên:        {name}")
        print(f"Giá:        {price:,.2f} VNĐ")
        print(f"Tình trạng: {'Còn hàng' if is_available else 'Hết hàng'}")
    except (KeyError, TypeError) as ex:
        print("Lỗi khi xử lý dữ liệu:", ex)

    # 3. Thử thêm lại key 'ID' bằng add_unique -> sẽ báo lỗi (giống Hashtable.Add)
    print("\n--- Thử nghiệm ném lỗi khi thêm trùng khóa ---")
    try:
        add_unique(product_info, "ID", 202)
    except KeyError as ex:
        print("Bắt được lỗi mong muốn khi thêm trùng khóa:", ex)

    # 4. Cập nhật giá trị hợp lệ (Ghi đè có chủ đích)
    product_info["Price"] = 2450.00
    print(f"-> Giá mới sau khi cập nhật: {product_info['Price']:,.2f} VNĐ")


if __name__ == "__main__":
    main()
