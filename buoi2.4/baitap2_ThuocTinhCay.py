"""
BÀI TẬP 2: TÍNH CÁC THUỘC TÍNH CỦA CÂY (MỨC ĐỘ: DỄ)
Các hàm đệ quy: số nút, số nút lá, chiều cao cây, tổng giá trị, giá trị lớn nhất.
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None


def count_nodes(node) -> int:
    """Đếm tổng số nút trên cây."""
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def count_leaves(node) -> int:
    """Đếm số nút lá (nút không có con nào)."""
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)


def height(node) -> int:
    """Tính chiều cao của cây (quy ước: cây rỗng = -1, cây chỉ có gốc = 0)."""
    if node is None:
        return -1
    return 1 + max(height(node.left), height(node.right))


def sum_tree(node) -> int:
    """Tính tổng giá trị các nút trong cây."""
    if node is None:
        return 0
    return node.data + sum_tree(node.left) + sum_tree(node.right)


def max_value(node):
    """Tìm giá trị lớn nhất trong cây."""
    if node is None:
        return float("-inf")
    return max(node.data, max_value(node.left), max_value(node.right))


def main():
    print("=== BÀI TẬP 2: TÍNH CÁC THUỘC TÍNH CỦA CÂY ===")
    # Dựng cây nhị phân số nguyên mẫu:
    #         10
    #        /  \
    #       5    20
    #      / \    \
    #     3   8    30
    root = Node(10)
    root.left = Node(5)
    root.right = Node(20)
    root.left.left = Node(3)
    root.left.right = Node(8)
    root.right.right = Node(30)

    print(f"Tổng số nút     : {count_nodes(root)}")
    print(f"Số nút lá       : {count_leaves(root)}")
    print(f"Chiều cao cây   : {height(root)}")
    print(f"Tổng giá trị    : {sum_tree(root)}")
    print(f"Giá trị lớn nhất: {max_value(root)}")


if __name__ == "__main__":
    main()
