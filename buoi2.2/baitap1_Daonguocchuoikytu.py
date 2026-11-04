"""
BÀI TẬP 1: ĐẢO NGƯỢC MỘT CHUỖI KÝ TỰ (MỨC ĐỘ: DỄ - STACK)
Nguyên tắc LIFO (Last-In, First-Out): Ký tự vào sau cùng sẽ được lấy ra đầu tiên.
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def reverse_string(s: str) -> str:
    char_stack = []

    # 1. Đẩy (Push) từng ký tự vào Stack
    for c in s:
        char_stack.append(c)

    # 2. Lấy ra (Pop) để xây dựng chuỗi đảo ngược
    reversed_chars = []
    while len(char_stack) > 0:
        reversed_chars.append(char_stack.pop())

    return "".join(reversed_chars)


def main():
    print("=== BÀI TẬP 1: ĐẢO NGƯỢC CHUỖI BẰNG STACK ===")
    user_input = input("Nhập một chuỗi bất kỳ: ").strip()
    if not user_input:
        user_input = "Hello World!"
        print(f"-> Chuỗi mặc định mẫu: {user_input}")

    res = reverse_string(user_input)
    print(f"-> Chuỗi sau khi đảo ngược: {res}")


if __name__ == "__main__":
    main()
