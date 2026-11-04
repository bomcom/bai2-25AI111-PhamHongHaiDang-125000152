"""
BÀI TẬP 9: KIỂM TRA CỬA SỔ TRÙNG LẶP (CONTAINS DUPLICATE II) (MỨC ĐỘ: KHÓ - SLIDING WINDOW & DICTIONARY)
Tìm 2 vị trí i, j sao cho nums[i] == nums[j] và abs(i - j) <= k.
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    recent_indices: dict[int, int] = {}

    for i, num in enumerate(nums):
        if num in recent_indices:
            # Kiểm tra khoảng cách giữa vị trí hiện tại và lần xuất hiện gần nhất
            if i - recent_indices[num] <= k:
                return True

        # Luôn cập nhật vị trí xuất hiện mới nhất
        recent_indices[num] = i

    return False


def main():
    print("=== BÀI TẬP 9: CỬA SỔ TRÙNG LẶP (CONTAINS DUPLICATE II) ===")

    test_cases = [
        ([1, 2, 3, 1], 3),          # True: nums[0] == nums[3] (3 - 0 <= 3)
        ([1, 0, 1, 1], 1),          # True: nums[2] == nums[3] (3 - 2 <= 1)
        ([1, 2, 3, 1, 2, 3], 2),    # False: khoảng cách các cặp trùng đều = 3 > 2
        ([99, 99], 2)               # True: 1 - 0 <= 2
    ]

    for nums, k in test_cases:
        res = contains_nearby_duplicate(nums, k)
        print(f"Mảng: {nums:<20} | k = {k} -> Kết quả: {res}")


if __name__ == "__main__":
    main()
