"""
BÀI TẬP 8: SINH DÃY SỐ NHỊ PHÂN TỪ 1 ĐẾN N BẰNG HÀNG ĐỢI (MỨC ĐỘ: TRUNG BÌNH - QUEUE)
Tư duy sinh dữ liệu theo tầng (Level-order / Breadth-First Search).
"""

import sys
from collections import deque

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def generate_binary_numbers(n: int) -> list[str]:
    if n <= 0:
        return []

    result = []
    q = deque()
    q.append("1")  # Bắt đầu từ số 1 (nhị phân là "1")

    for _ in range(n):
        curr = q.popleft()
        result.append(curr)

        # Sinh hai nhánh con tiếp theo: thêm 0 và thêm 1
        q.append(curr + "0")
        q.append(curr + "1")

    return result


def main():
    print("=== BÀI TẬP 8: SINH SỐ NHỊ PHÂN BẰNG HÀNG ĐỢI (BFS) ===")
    user_inp = input("Nhập số N (ví dụ 10): ").strip()
    n = int(user_inp) if user_inp.isdigit() else 10

    binary_list = generate_binary_numbers(n)
    print(f"\nDãy {n} số nhị phân đầu tiên:")
    print(" -> ".join(binary_list))


if __name__ == "__main__":
    main()
