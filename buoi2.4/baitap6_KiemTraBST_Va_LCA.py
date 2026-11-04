"""
BÀI TẬP 6: KIỂM TRA BST HỢP LỆ VÀ TỔ TIÊN CHUNG GẦN NHẤT (LCA) (MỨC ĐỘ: TRUNG BÌNH - KHÓ)
- is_valid_bst(node, low, high): kiểm tra toàn bộ cây có thỏa mãn khoảng giá trị.
- lca_bst(root, p, q): tìm Lowest Common Ancestor trong BST.
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


class Node:
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None


def is_valid_bst(node, low=float("-inf"), high=float("inf")) -> bool:
    """Mỗi nút phải nằm nghiêm ngặt trong khoảng (low, high) do tất cả tổ tiên quy định."""
    if node is None:
        return True
    if not (low < node.key < high):
        return False
    return (is_valid_bst(node.left, low, node.key) and
            is_valid_bst(node.right, node.key, high))


def lca_bst(root, p: int, q: int):
    """Tìm tổ tiên chung gần nhất (LCA) của hai khóa p và q trong BST."""
    node = root
    while node is not None:
        if p < node.key and q < node.key:
            node = node.left
        elif p > node.key and q > node.key:
            node = node.right
        else:
            # p và q nằm ở hai phía khác nhau, hoặc một trong hai trùng với node
            return node.key
    return None


def main():
    print("=== BÀI TẬP 6: KIỂM TRA BST VÀ TỔ TIÊN CHUNG GẦN NHẤT (LCA) ===")

    # Cây a: BST chuẩn
    #         20
    #        /  \
    #       10   30
    #      / \  /  \
    #     5  15 25 35
    a = Node(20)
    a.left, a.right = Node(10), Node(30)
    a.left.left, a.left.right = Node(5), Node(15)
    a.right.left, a.right.right = Node(25), Node(35)

    print(f"Cây a có phải BST hợp lệ không? {is_valid_bst(a)} (Kỳ vọng: True)")
    print(f"LCA(5, 15) trong cây a = {lca_bst(a, 5, 15)} (Kỳ vọng: 10)")
    print(f"LCA(5, 35) trong cây a = {lca_bst(a, 5, 35)} (Kỳ vọng: 20)")
    print(f"LCA(25, 35) trong cây a = {lca_bst(a, 25, 35)} (Kỳ vọng: 30)")

    # Cây b: Cây sai tính chất BST (12 nằm bên trái gốc 10 dù 12 > 10)
    #       10
    #      /  \
    #     5    15
    #      \
    #       12
    b = Node(10)
    b.left, b.right = Node(5), Node(15)
    b.left.right = Node(12)
    print(f"\nCây b có phải BST hợp lệ không? {is_valid_bst(b)} (Kỳ vọng: False)")


if __name__ == "__main__":
    main()
