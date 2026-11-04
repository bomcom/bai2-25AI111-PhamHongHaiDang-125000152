"""
BÀI TẬP 7: CÂY BIỂU THỨC (EXPRESSION TREE) (MỨC ĐỘ: KHÓ)
Xây dựng cây từ biểu thức hậu tố (Postfix) và chuyển đổi sang Infix, Prefix, tính giá trị.
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

TOAN_TU = {"+", "-", "*", "/"}


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_from_postfix(tokens: list[str]) -> Node:
    """Dùng Stack để dựng cây biểu thức từ danh sách token hậu tố."""
    stack = []
    for t in tokens:
        if t in TOAN_TU:
            right = stack.pop()  # Toán hạng bên phải được pop trước
            left = stack.pop()
            node = Node(t)
            node.left, node.right = left, right
            stack.append(node)
        else:
            stack.append(Node(float(t)))
    return stack.pop()


def evaluate(node) -> float:
    """Tính toán giá trị biểu thức bằng đệ quy."""
    if node.data not in TOAN_TU:
        return node.data

    a = evaluate(node.left)
    b = evaluate(node.right)

    if node.data == "+":
        return a + b
    elif node.data == "-":
        return a - b
    elif node.data == "*":
        return a * b
    elif node.data == "/":
        if b == 0:
            raise ZeroDivisionError("Lỗi: Chia cho 0!")
        return a / b


def to_infix(node) -> str:
    """In biểu thức dạng Trung tố (Infix) kèm ngoặc."""
    if node.data not in TOAN_TU:
        return f"{node.data:g}"
    return f"({to_infix(node.left)} {node.data} {to_infix(node.right)})"


def to_prefix(node) -> str:
    """In biểu thức dạng Tiền tố (Prefix)."""
    if node.data not in TOAN_TU:
        return f"{node.data:g}"
    return f"{node.data} {to_prefix(node.left)} {to_prefix(node.right)}"


def main():
    print("=== BÀI TẬP 7: CÂY BIỂU THỨC (EXPRESSION TREE) ===")
    raw_input = input("Nhập biểu thức hậu tố cách nhau bởi dấu cách (Enter để dùng '3 4 + 2 * 7 /'): ").strip()
    if not raw_input:
        raw_input = "3 4 + 2 * 7 /"

    tokens = raw_input.split()
    root = build_from_postfix(tokens)

    print(f"\nBiểu thức hậu tố (Postfix): {raw_input}")
    print(f"Dạng trung tố   (Infix)  : {to_infix(root)}")
    print(f"Dạng tiền tố    (Prefix) : {to_prefix(root)}")
    print(f"Giá trị tính toán        : {evaluate(root):.4f}")


if __name__ == "__main__":
    main()
