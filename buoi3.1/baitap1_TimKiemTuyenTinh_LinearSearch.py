"""
BÀI TẬP 1: NGƯỜI ĐƯA THƯ TÌM NHÀ (MỨC ĐỘ: DỄ)
Thuật toán: Tìm kiếm tuyến tính (Linear Search) - Độ phức tạp O(N).
Duyệt qua từng phần tử từ đầu đến cuối danh sách chưa sắp xếp.
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def tim_tuyen_tinh(arr: list, x: int) -> int:
    """Trả về chỉ số (index) đầu tiên của x trong arr, nếu không thấy trả về -1."""
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


def main():
    print("=== BÀI TẬP 1: TÌM KIẾM TUYẾN TÍNH (LINEAR SEARCH) ===")
    mang_so = [4, 11, 2, 9, 7, 22, 5]
    print(f"Mảng số ban đầu: {mang_so}")

    for gia_tri in [7, 22, 99]:
        idx = tim_tuyen_tinh(mang_so, gia_tri)
        if idx != -1:
            print(f"-> Tìm thấy giá trị {gia_tri:<2} tại chỉ số (index): {idx}")
        else:
            print(f"-> Không tìm thấy giá trị {gia_tri:<2} trong mảng (trả về -1)")


if __name__ == "__main__":
    main()
