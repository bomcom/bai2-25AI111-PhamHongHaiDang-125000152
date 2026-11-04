"""
BÀI TẬP 8: SẮP XẾP TRỘN (MERGE SORT) (MỨC ĐỘ: KHÓ)
Thuật toán Chia để trị (Divide and Conquer):
1. Chia đôi danh sách thành 2 nửa.
2. Đệ quy sắp xếp 2 nửa.
3. Trộn (Merge) 2 nửa đã sắp xếp lại thành danh sách hoàn chỉnh.
Độ phức tạp luôn giữ vững O(N log N) trong mọi trường hợp!
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def merge(left: list, right: list) -> list:
    """Hàm trộn 2 danh sách đã sắp xếp thành một danh sách có thứ tự."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Thêm phần còn lại
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr: list) -> list:
    """Hàm sắp xếp trộn đệ quy."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


def main():
    print("=== BÀI TẬP 8: SẮP XẾP TRỘN (MERGE SORT) ===")
    mang_so = [38, 27, 43, 3, 9, 82, 10]
    print(f"Mảng ban đầu  : {mang_so}")

    mang_da_sap_xep = merge_sort(mang_so)
    print(f"Mảng sau sắp xếp: {mang_da_sap_xep}")


if __name__ == "__main__":
    main()
