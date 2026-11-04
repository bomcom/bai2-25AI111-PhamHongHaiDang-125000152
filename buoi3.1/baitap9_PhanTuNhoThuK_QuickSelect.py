"""
BÀI TẬP 9: TÌM PHẦN TỬ NHỎ THỨ K (QUICKSELECT) (MỨC ĐỘ: KHÓ)
Ứng dụng tư tưởng Quick Sort để tìm phần tử thứ k mà KHÔNG cần sắp xếp toàn bộ mảng.
Độ phức tạp trung bình cực kỳ ấn tượng: O(N) thay vì O(N log N)!
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def partition(arr: list, low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_select_helper(arr: list, low: int, high: int, k_index: int) -> int:
    if low <= high:
        pi = partition(arr, low, high)
        if pi == k_index:
            return arr[pi]
        elif pi > k_index:
            return quick_select_helper(arr, low, pi - 1, k_index)
        else:
            return quick_select_helper(arr, pi + 1, high, k_index)
    return -1


def tim_phan_tu_nho_thu_k(arr: list, k: int) -> int:
    """Tìm phần tử nhỏ thứ k (k tính từ 1-based index)."""
    if 1 <= k <= len(arr):
        arr_copy = arr.copy()  # Tránh làm thay đổi mảng gốc
        return quick_select_helper(arr_copy, 0, len(arr_copy) - 1, k - 1)
    raise ValueError(f"Giá trị k = {k} không hợp lệ cho mảng có độ dài {len(arr)}!")


def main():
    print("=== BÀI TẬP 9: TÌM PHẦN TỬ NHỎ THỨ K (QUICKSELECT) ===")
    mang_so = [7, 10, 4, 3, 20, 15]
    print(f"Mảng số ban đầu: {mang_so}")
    # Nếu sắp xếp: [3, 4, 7, 10, 15, 20] -> k=1 là 3, k=2 là 4, k=3 là 7, k=4 là 10

    for k in [1, 3, 5]:
        val = tim_phan_tu_nho_thu_k(mang_so, k)
        print(f"-> Phần tử nhỏ thứ {k} là: {val}")


if __name__ == "__main__":
    main()
