"""
BÀI TẬP 4: XÓA MỘT NÚT KHỎI BST (MỨC ĐỘ: TRUNG BÌNH)
Ba trường hợp xóa:
1. Nút lá (không có con): Xóa trực tiếp.
2. Nút có 1 con: Nối con trực tiếp lên cha.
3. Nút có 2 con: Thay bằng inorder successor (nút nhỏ nhất của cây con phải).
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


class Node:
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None


def insert(node, key: int):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    return node


def min_node(node):
    curr = node
    while curr.left is not None:
        curr = curr.left
    return curr


def delete(node, key: int):
    if node is None:
        return None  # Không tìm thấy key

    if key < node.key:
        node.left = delete(node.left, key)
    elif key > node.key:
        node.right = delete(node.right, key)
    else:
        # Đã tìm thấy nút cần xóa:
        # Trường hợp 1 & 2: Nút lá hoặc chỉ có 1 cây con
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left

        # Trường hợp 3: Nút có đủ 2 con
        # Tìm nút kế thừa Inorder (nhỏ nhất bên phải)
        successor = min_node(node.right)
        node.key = successor.key
        # Xóa nút kế thừa ở nhánh phải
        node.right = delete(node.right, successor.key)

    return node


def inorder(node, res: list):
    if node:
        inorder(node.left, res)
        res.append(node.key)
        inorder(node.right, res)


def main():
    print("=== BÀI TẬP 4: XÓA NÚT KHỎI BST ===")
    root = None
    for x in [50, 30, 70, 20, 40, 60, 80]:
        root = insert(root, x)

    init_res = []
    inorder(root, init_res)
    print(f"Cây ban đầu: {init_res}")

    # Xóa lần lượt:
    # 20 (nút lá), 30 (nút có 1 con nếu xóa 20 trước), 50 (gốc có 2 con), 99 (không tồn tại)
    for x in [20, 30, 50, 99]:
        root = delete(root, x)
        res = []
        inorder(root, res)
        print(f"Sau khi xóa khóa {x:<2}: {res}")


if __name__ == "__main__":
    main()
