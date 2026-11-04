"""
BÀI TẬP 7: SẮP XẾP CHÈN (INSERTION SORT) (MỨC ĐỘ: DỄ / TRUNG BÌNH)
Ý tưởng: Tương tự cách xếp bài tây trên tay - lấy từng phần tử và chèn vào đúng vị trí dãy đã sắp trước đó.
Cực kỳ hiệu quả với mảng gần như đã sắp xếp (Nearly Sorted Array) với độ phức tạp xấp xỉ O(N).
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def sap_xep_chen(arr: list) -> None:
    """Sắp xếp chèn in-place."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Dịch chuyển các phần tử lớn hơn key sang phải 1 vị trí
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def main():
    print("=== BÀI TẬP 7: SẮP XẾP CHÈN (INSERTION SORT) ===")
    mang_so = [12, 11, 13, 5, 6, 7]
    print(f"Mảng ban đầu  : {mang_so}")

    sap_xep_chen(mang_so)
    print(f"Mảng sau sắp xếp: {mang_so}")


if __name__ == "__main__":
    main()
