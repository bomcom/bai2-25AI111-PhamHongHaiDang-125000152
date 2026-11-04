"""
BÀI TẬP 3: CÂY NHỊ PHÂN TÌM KIẾM (BST) - THÊM VÀ TÌM KIẾM (MỨC ĐỘ: DỄ - TRUNG BÌNH)
Tính chất: Nút con trái < Nút gốc < Nút con phải.
Duyệt Inorder trên BST luôn cho ra dãy số tăng dần!
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


class Node:
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key: int):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key: int):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        # Nếu key == node.key: bỏ qua không thêm trùng
        return node

    def search(self, key: int) -> bool:
        """Tìm kiếm khóa bằng vòng lặp while tối ưu O(H)."""
        curr = self.root
        while curr is not None:
            if key == curr.key:
                return True
            curr = curr.left if key < curr.key else curr.right
        return False

    def min_value(self):
        """Khóa nhỏ nhất luôn nằm ở nút tận cùng bên trái."""
        if not self.root:
            return None
        curr = self.root
        while curr.left is not None:
            curr = curr.left
        return curr.key

    def max_value(self):
        """Khóa lớn nhất luôn nằm ở nút tận cùng bên phải."""
        if not self.root:
            return None
        curr = self.root
        while curr.right is not None:
            curr = curr.right
        return curr.key

    def inorder(self) -> list[int]:
        res = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                res.append(node.key)
                _inorder(node.right)
        _inorder(self.root)
        return res


def main():
    print("=== BÀI TẬP 3: CÂY NHỊ PHÂN TÌM KIẾM (BST) ===")
    bst = BST()
    elements = [50, 30, 70, 20, 40, 60, 80, 40]  # Có phần tử 40 trùng lặp
    print(f"Thêm dãy số vào BST: {elements}")
    for x in elements:
        bst.insert(x)

    inorder_list = bst.inorder()
    print(f"Duyệt Inorder (dãy tăng dần): {inorder_list}")
    print(f"Khóa nhỏ nhất (Min): {bst.min_value()} | Khóa lớn nhất (Max): {bst.max_value()}")

    test_keys = [40, 60, 99]
    print("\n--- Kiểm tra tìm kiếm ---")
    for k in test_keys:
        found = bst.search(k)
        print(f"Tìm khóa {k:<3}: {'TÌM THẤY (True)' if found else 'KHÔNG TÌM THẤY (False)'}")


if __name__ == "__main__":
    main()
