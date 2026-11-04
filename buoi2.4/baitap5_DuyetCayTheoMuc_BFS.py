"""
BÀI TẬP 5: DUYỆT CÂY THEO MỨC (BFS) VÀ RIGHT SIDE VIEW (MỨC ĐỘ: TRUNG BÌNH)
Sử dụng collections.deque để duyệt từng tầng (Level-order Traversal).
"""

import sys
from collections import deque

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def level_order(root) -> list[list]:
    """Trả về danh sách các mức, mỗi mức là một list giá trị."""
    if root is None:
        return []
    levels = []
    queue = deque([root])

    while queue:
        size = len(queue)
        level = []
        for _ in range(size):
            node = queue.popleft()
            level.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        levels.append(level)

    return levels


def right_side_view(root) -> list:
    """Các nút nhìn thấy khi đứng bên phải cây (phần tử cuối cùng của mỗi mức)."""
    return [level[-1] for level in level_order(root)]


def main():
    print("=== BÀI TẬP 5: DUYỆT CÂY THEO MỨC (BFS) ===")
    # Dựng cây mẫu:
    #         1
    #       /   \
    #      2     3
    #     / \   / \
    #    4   5 6   7
    #   /
    #  8
    root = Node(1)
    root.left, root.right = Node(2), Node(3)
    root.left.left, root.left.right = Node(4), Node(5)
    root.right.left, root.right.right = Node(6), Node(7)
    root.left.left.left = Node(8)

    print("--- Duyệt theo từng mức (Tầng) ---")
    levels = level_order(root)
    for i, lvl in enumerate(levels):
        print(f"Mức {i}: {lvl}")

    print(f"\nNút nhìn thấy từ bên phải (Right Side View): {right_side_view(root)}")


if __name__ == "__main__":
    main()
