"""
BÀI TẬP 6: SẮP XẾP CHỌN (SELECTION SORT) (MỨC ĐỘ: DỄ / TRUNG BÌNH)
Ý tưởng: Tìm phần tử nhỏ nhất trong đoạn còn lại và hoán đổi với vị trí i hiện tại.
Ưu điểm: Số lần hoán đổi (swap) tối đa chỉ là N - 1 lần (rất tốt khi chi phí ghi nhớ đắt).
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def sap_xep_chon(arr: list) -> None:
    """Sắp xếp chọn in-place."""
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Đổi chỗ phần tử nhỏ nhất tìm được với vị trí i hiện tại
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]


def main():
    print("=== BÀI TẬP 6: SẮP XẾP CHỌN (SELECTION SORT) ===")
    mang_so = [29, 10, 14, 37, 13, 8, 24]
    print(f"Mảng ban đầu  : {mang_so}")

    sap_xep_chon(mang_so)
    print(f"Mảng sau sắp xếp: {mang_so}")


if __name__ == "__main__":
    main()
