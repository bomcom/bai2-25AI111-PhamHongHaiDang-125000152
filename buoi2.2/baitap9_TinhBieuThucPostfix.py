"""
BÀI TẬP 9: TÍNH TOÁN BIỂU THỨC DẠNG POSTFIX (KÝ PHÁP BA LAN NGƯỢC) (MỨC ĐỘ: RẤT KHÓ - STACK)
Ứng dụng kinh điển của Stack trong biên dịch và phân tích biểu thức toán học.
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


class PostfixCalculator:
    def evaluate(self, expression: str) -> int:
        operands = []
        tokens = expression.split()

        for token in tokens:
            try:
                # Nếu là số nguyên, đẩy vào stack
                number = int(token)
                operands.append(number)
            except ValueError:
                # Nếu là toán tử: toán hạng 2 được lấy ra trước, rồi đến toán hạng 1
                if len(operands) < 2:
                    raise ValueError(f"Biểu thức không hợp lệ: thiếu toán hạng cho toán tử '{token}'")

                operand2 = operands.pop()
                operand1 = operands.pop()

                if token == "+":
                    operands.append(operand1 + operand2)
                elif token == "-":
                    operands.append(operand1 - operand2)
                elif token == "*":
                    operands.append(operand1 * operand2)
                elif token == "/":
                    # Truncate towards zero giống chia số nguyên C#/C++
                    operands.append(int(operand1 / operand2))
                elif token == "^":
                    operands.append(operand1 ** operand2)
                else:
                    raise ValueError(f"Toán tử không hợp lệ: '{token}'")

        if len(operands) != 1:
            raise ValueError("Biểu thức không hợp lệ: dư toán hạng!")

        return operands.pop()


def main():
    calculator = PostfixCalculator()
    print("=== BÀI TẬP 9: TÍNH TOÁN BIỂU THỨC POSTFIX ===")

    # Test cases mẫu
    samples = [
        ("5 3 + 2 *", "(5 + 3) * 2"),
        ("4 13 5 / +", "4 + (13 / 5)"),
        ("10 6 9 3 + -11 * / * 17 + 5 +", "Biểu thức phức tạp")
    ]

    for expr, desc in samples:
        res = calculator.evaluate(expr)
        print(f"Postfix: '{expr:<22}' [{desc}] -> Kết quả: {res}")

    print("\n--- Tự nhập biểu thức ---")
    user_expr = input("Nhập biểu thức Postfix (cách nhau bởi dấu cách, ví dụ: 5 3 + 2 *): ").strip()
    if user_expr:
        try:
            print("Kết quả tính được:", calculator.evaluate(user_expr))
        except Exception as e:
            print("Lỗi:", e)


if __name__ == "__main__":
    main()
