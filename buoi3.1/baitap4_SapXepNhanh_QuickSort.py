"""
BÀI TẬP 4: CHIA ĐỂ TRỊ (MỨC ĐỘ: KHÓ)
Thuật toán: Sắp xếp nhanh (Quick Sort) - Phân hoạch Lomuto in-place.
Độ phức tạp trung bình: O(N log N).
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def partition(arr: list, low: int, high: int) -> int:
    """Chọn pivot là phần tử cuối cùng arr[high] và phân hoạch danh sách."""
    pivot = arr[high]
    i = low - 1  # Chỉ số của phần tử nhỏ hơn pivot

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Đưa pivot về đúng vị trí giữa hai nửa
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr: list, low: int, high: int) -> None:
    """Hàm đệ quy Quick Sort."""
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)   # Nửa bên trái pivot
        quick_sort(arr, pi + 1, high)  # Nửa bên phải pivot


def main():
    print("=== BÀI TẬP 4: SẮP XẾP NHANH (QUICK SORT) ===")
    mang_so = [10, 7, 8, 9, 1, 5]
    print(f"Mảng ban đầu  : {mang_so}")

    quick_sort(mang_so, 0, len(mang_so) - 1)
    print(f"Mảng sau sắp xếp: {mang_so}")


if __name__ == "__main__":
    main()
