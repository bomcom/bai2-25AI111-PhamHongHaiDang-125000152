"""
BÀI TẬP 5: KIỂM TRA CHUỖI NGOẶC HỢP LỆ (MỨC ĐỘ: TRUNG BÌNH - STACK)
Bài toán kinh điển xác thực cú pháp biểu thức toán học / code.
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


class Solution:
    def is_valid(self, s: str) -> bool:
        stack = []
        bracket_pairs = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for c in s:
            if c in bracket_pairs:
                # Nếu là ngoặc mở -> Push vào stack
                stack.append(c)
            elif c in bracket_pairs.values():
                # Nếu là ngoặc đóng
                if len(stack) == 0:
                    return False  # Có ngoặc đóng mà không có ngoặc mở
                open_bracket = stack.pop()
                if bracket_pairs[open_bracket] != c:
                    return False  # Sai loại ngoặc tương ứng
            # Bỏ qua các ký tự khác (khoảng trắng, toán tử, chữ cái)

        # Hợp lệ nếu toàn bộ ngoặc mở đều đã được đóng (stack rỗng)
        return len(stack) == 0


def main():
    solution = Solution()
    print("=== BÀI TẬP 5: KIỂM TRA CHUỖI NGOẶC HỢP LỆ ===")

    # Test cases mẫu
    test_cases = [
        "()[]{}",
        "([{}])",
        "( [ { } ] )",
        "([)]",
        "((()",
        ")(",
        "3 * (a + [b - c])"
    ]

    print("--- Chạy thử các kịch bản mẫu ---")
    for s in test_cases:
        res = solution.is_valid(s)
        status = "HỢP LỆ (True)" if res else "KHÔNG HỢP LỆ (False)"
        print(f"Chuỗi: '{s:<18}' -> {status}")

    print("\n--- Nhập thử chuỗi của bạn ---")
    user_str = input("Nhập chuỗi ngoặc để kiểm tra: ").strip()
    if user_str:
        res = solution.is_valid(user_str)
        print(f"Kết quả: {'HỢP LỆ' if res else 'KHÔNG HỢP LỆ'}")


if __name__ == "__main__":
    main()
