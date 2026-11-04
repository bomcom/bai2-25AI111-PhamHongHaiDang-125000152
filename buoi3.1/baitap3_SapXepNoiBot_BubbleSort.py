"""
BÀI TẬP 3: XẾP HÀNG THEO CHIỀU CAO (MỨC ĐỘ: DỄ / TRUNG BÌNH)
Thuật toán: Sắp xếp nổi bọt (Bubble Sort) - Sắp xếp in-place.
Tối ưu hóa: Thêm cờ swapped để dừng sớm khi mảng đã có thứ tự O(N).
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def sap_xep_noi_bot(arr: list) -> None:
    """Sắp xếp nổi bọt in-place với cờ tối ưu dừng sớm."""
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Nếu không có cặp nào bị hoán đổi -> mảng đã sắp xếp xong!
        if not swapped:
            break


def main():
    print("=== BÀI TẬP 3: SẮP XẾP NỔI BỌT (BUBBLE SORT) ===")
    mang_so = [64, 34, 25, 12, 22, 11, 90]
    print(f"Mảng ban đầu  : {mang_so}")

    sap_xep_noi_bot(mang_so)
    print(f"Mảng sau sắp xếp: {mang_so}")


if __name__ == "__main__":
    main()
