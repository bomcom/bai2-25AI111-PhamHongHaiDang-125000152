"""
BÀI TẬP 6: TÌM PHẦN TỬ LỚN HƠN TIẾP THEO (NEXT GREATER ELEMENT) (MỨC ĐỘ: KHÓ - MONOTONIC STACK)
Sử dụng Monotonic Stack (Ngăn xếp đơn điệu) đạt độ phức tạp O(N).
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def next_greater_element(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [-1] * n
    stack = []  # Lưu chỉ số (indices)

    for i in range(n):
        # Khi tìm thấy phần tử nums[i] lớn hơn phần tử ở đỉnh stack
        while stack and nums[i] > nums[stack[-1]]:
            prev_index = stack.pop()
            result[prev_index] = nums[i]

        stack.append(i)

    return result


def main():
    print("=== BÀI TẬP 6: NEXT GREATER ELEMENT (MONOTONIC STACK) ===")

    # Test case 1 từ đề bài
    arr1 = [4, 5, 2, 25]
    res1 = next_greater_element(arr1)
    print("Mảng gốc:                   ", arr1)
    print("Phần tử lớn hơn tiếp theo:  ", res1)

    # Test case 2
    arr2 = [13, 7, 6, 12, 10]
    res2 = next_greater_element(arr2)
    print("\nMảng gốc:                   ", arr2)
    print("Phần tử lớn hơn tiếp theo:  ", res2)

    # Nhập từ người dùng
    user_inp = input("\nNhập các số nguyên cách nhau bởi dấu cách (Enter để bỏ qua): ").strip()
    if user_inp:
        user_arr = [int(x) for x in user_inp.split()]
        print("Kết quả:", next_greater_element(user_arr))


if __name__ == "__main__":
    main()
