"""
BÀI TẬP 1: XÂY DỰNG CÂY NHỊ PHÂN VÀ CÁC PHÉP DUYỆT CÂY (MỨC ĐỘ: DỄ)
Ba phép duyệt cơ bản:
- Preorder (Gốc - Trái - Phải / NLR)
- Inorder (Trái - Gốc - Phải / LNR)
- Postorder (Trái - Phải - Gốc / LRN)
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(node, result: list):
    """Duyệt tiền thứ tự: Gốc -> Trái -> Phải."""
    if node is None:
        return
    result.append(str(node.data))
    preorder(node.left, result)
    preorder(node.right, result)


def inorder(node, result: list):
    """Duyệt trung thứ tự: Trái -> Gốc -> Phải."""
    if node is None:
        return
    inorder(node.left, result)
    result.append(str(node.data))
    inorder(node.right, result)


def postorder(node, result: list):
    """Duyệt hậu thứ tự: Trái -> Phải -> Gốc."""
    if node is None:
        return
    postorder(node.left, result)
    postorder(node.right, result)
    result.append(str(node.data))


def main():
    print("=== BÀI TẬP 1: DUYỆT CÂY NHỊ PHÂN ===")
    # Dựng cây nhị phân mẫu:
    #         A
    #       /   \
    #      B     C
    #     / \     \
    #    D   E     F
    root = Node("A")
    root.left = Node("B")
    root.right = Node("C")
    root.left.left = Node("D")
    root.left.right = Node("E")
    root.right.right = Node("F")

    for name, func in [
        ("Preorder (NLR - Tiền thứ tự)", preorder),
        ("Inorder  (LNR - Trung thứ tự)", inorder),
        ("Postorder (LRN - Hậu thứ tự)", postorder)
    ]:
        kq = []
        func(root, kq)
        print(f"{name:<30}: {' -> '.join(kq)}")


if __name__ == "__main__":
    main()
