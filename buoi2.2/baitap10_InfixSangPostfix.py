"""
BÀI TẬP 10: CHUYỂN ĐỔI INFIX SANG POSTFIX (THUẬT TOÁN SHUNTING-YARD CỦA DIJKSTRA) (MỨC ĐỘ: RẤT KHÓ - STACK)
Biến đổi biểu thức trung tố (Infix) thông thường thành hậu tố (Postfix) để máy tính tính toán.
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def infix_to_postfix(expression: str) -> str:
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    stack = []
    tokens = expression.split()

    for token in tokens:
        # Nếu là toán hạng (chữ cái hoặc số)
        if token.isalnum() or (token.startswith('-') and token[1:].isdigit()):
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()  # Bỏ dấu '(' ra khỏi stack
        else:
            # Là toán tử
            while (stack and stack[-1] != '(' and
                   precedence.get(stack[-1], 0) >= precedence.get(token, 0)):
                output.append(stack.pop())
            stack.append(token)

    # Đưa các toán tử còn lại trong Stack ra kết quả
    while stack:
        output.append(stack.pop())

    return " ".join(output)


def main():
    print("=== BÀI TẬP 10: SHUNTING-YARD (INFIX -> POSTFIX) ===")

    # Test cases mẫu
    samples = [
        "( A + B ) * ( C - D )",
        "3 + 4 * 2 / ( 1 - 5 )",
        "A + B * C"
    ]

    for exp in samples:
        post = infix_to_postfix(exp)
        print(f"Infix:   {exp}")
        print(f"Postfix: {post}\n")

    user_exp = input("Nhập biểu thức Infix (các token cách nhau bởi dấu cách, vd: ( 5 + 3 ) * 2): ").strip()
    if user_exp:
        print("Postfix:", infix_to_postfix(user_exp))


if __name__ == "__main__":
    main()
