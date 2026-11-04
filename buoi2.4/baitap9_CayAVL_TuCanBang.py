"""
BÀI TẬP 9: CÂY AVL - CÂY TÌM KIẾM TỰ CÂN BẰNG (MỨC ĐỘ: RẤT KHÓ)
Khắc phục suy biến của BST bằng 4 phép quay: Left-Left, Right-Right, Left-Right, Right-Left.
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


class Node:
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def get_height(n):
    return n.height if n else 0


def balance_factor(n):
    return get_height(n.left) - get_height(n.right) if n else 0


def update_height(n):
    n.height = 1 + max(get_height(n.left), get_height(n.right))


def rotate_right(y):
    x = y.left
    y.left = x.right
    x.right = y
    update_height(y)
    update_height(x)
    return x  # x trở thành gốc mới của cây con


def rotate_left(x):
    y = x.right
    x.right = y.left
    y.left = x
    update_height(x)
    update_height(y)
    return y  # y trở thành gốc mới của cây con


def insert(node, key: int):
    # 1. Thêm nút như BST thông thường
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    else:
        return node

    # 2. Cập nhật chiều cao nút hiện tại
    update_height(node)

    # 3. Tính hệ số cân bằng để kiểm tra mất cân bằng
    bf = balance_factor(node)

    # Trường hợp 1: Left - Left
    if bf > 1 and key < node.left.key:
        return rotate_right(node)

    # Trường hợp 2: Right - Right
    if bf < -1 and key > node.right.key:
        return rotate_left(node)

    # Trường hợp 3: Left - Right
    if bf > 1 and key > node.left.key:
        node.left = rotate_left(node.left)
        return rotate_right(node)

    # Trường hợp 4: Right - Left
    if bf < -1 and key < node.right.key:
        node.right = rotate_right(node.right)
        return rotate_left(node)

    return node


def preorder(node, res: list):
    if node:
        res.append(node.key)
        preorder(node.left, res)
        preorder(node.right, res)


def main():
    print("=== BÀI TẬP 9: CÂY AVL TỰ CÂN BẰNG ===")
    root = None
    insert_sequence = [10, 20, 30, 40, 50, 25]
    print(f"Thêm dãy khóa vào cây AVL: {insert_sequence}\n")

    for x in insert_sequence:
        root = insert(root, x)
        kq = []
        preorder(root, kq)
        print(f"Thêm {x:>2} -> Gốc = {root.key:<2} | Chiều cao = {root.height:<2} | Preorder = {kq}")


if __name__ == "__main__":
    main()
