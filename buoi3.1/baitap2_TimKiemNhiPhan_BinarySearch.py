"""
BÀI TẬP 2: TRA TỪ ĐIỂN NHANH (MỨC ĐỘ: TRUNG BÌNH)
Thuật toán: Tìm kiếm nhị phân (Binary Search) - Độ phức tạp O(log N).
Yêu cầu tiên quyết: Danh sách bắt buộc phải được SẮP XẾP TĂNG DẦN.
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def tim_nhi_phan(arr: list, x: int) -> int:
    """Trả về chỉ số của x trong mảng đã sắp xếp tăng dần, không thấy trả về -1."""
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1  # Tìm ở nửa bên phải
        else:
            high = mid - 1  # Tìm ở nửa bên trái

    return -1


def main():
    print("=== BÀI TẬP 2: TÌM KIẾM NHỊ PHÂN (BINARY SEARCH) ===")
    mang_so = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    print(f"Mảng đã sắp xếp: {mang_so}")

    for gia_tri in [23, 2, 91, 100]:
        idx = tim_nhi_phan(mang_so, gia_tri)
        if idx != -1:
            print(f"-> Tìm thấy {gia_tri:<3} tại vị trí: {idx}")
        else:
            print(f"-> Không tìm thấy {gia_tri:<3} trong mảng.")


if __name__ == "__main__":
    main()
