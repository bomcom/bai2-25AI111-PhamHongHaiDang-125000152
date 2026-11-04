"""
BÀI TẬP 6: CẶP SỐ CÓ TỔNG BẰNG K (TWO SUM) (MỨC ĐỘ: DỄ - TRUNG BÌNH - DICTIONARY)
Bài toán phỏng vấn kinh điển, giải bằng Bảng băm đạt độ phức tạp tối ưu O(N).
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}  # Lưu trữ giá trị: vị trí (value -> index)

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []


def main():
    print("=== BÀI TẬP 6: TWO SUM BẰNG BẢNG BĂM O(N) ===")

    # Test cases mẫu
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
        ([1, 5, 8, 12, 14], 20)
    ]

    for nums, target in test_cases:
        res = two_sum(nums, target)
        if res:
            idx1, idx2 = res[0], res[1]
            print(f"Mảng: {nums:<20} | Target: {target:<2} -> Chỉ số: {res} ({nums[idx1]} + {nums[idx2]} = {target})")
        else:
            print(f"Mảng: {nums:<20} | Target: {target:<2} -> Không tìm thấy")


if __name__ == "__main__":
    main()
