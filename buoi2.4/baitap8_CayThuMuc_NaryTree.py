"""
BÀI TẬP 8: CÂY THƯ MỤC - CÂY TỔNG QUÁT (N-ARY TREE) (MỨC ĐỘ: KHÓ)
Mô phỏng hệ thống tệp và thư mục phân cấp với số lượng con tùy ý.
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


class TreeNode:
    """Nút của cây tổng quát: đại diện cho thư mục hoặc tệp tin."""
    def __init__(self, name: str, size: int = 0, is_folder: bool = False):
        self.name = name
        self.size = size  # Chỉ có ý nghĩa với tệp (file)
        self.is_folder = is_folder
        self.children = []

    def add(self, child):
        self.children.append(child)
        return child


def print_tree(node, prefix=""):
    """In cấu trúc cây thư mục với thụt lề theo độ sâu."""
    tag = "[D]" if node.is_folder else "[F]"
    size_str = f" ({node.size} KB)" if not node.is_folder else ""
    print(f"{prefix}{tag} {node.name}{size_str}")
    for child in node.children:
        print_tree(child, prefix + "    ")


def total_size(node) -> int:
    """Tính tổng dung lượng (KB) của toàn bộ thư mục."""
    if not node.is_folder:
        return node.size
    return sum(total_size(c) for c in node.children)


def count_files(node) -> int:
    """Đếm tổng số tệp tin bên trong thư mục."""
    if not node.is_folder:
        return 1
    return sum(count_files(c) for c in node.children)


def find_path(node, target_name: str, path=None):
    """Tìm đường dẫn đầy đủ đến tệp có tên target_name."""
    current_path = (path or []) + [node.name]
    if node.name == target_name:
        return "/".join(current_path)

    for child in node.children:
        found = find_path(child, target_name, current_path)
        if found:
            return found
    return None


def main():
    print("=== BÀI TẬP 8: CÂY THƯ MỤC HỆ THỐNG (N-ARY TREE) ===")
    root = TreeNode("root", is_folder=True)

    docs = root.add(TreeNode("Documents", is_folder=True))
    docs.add(TreeNode("bao_cao.docx", 120))
    docs.add(TreeNode("de_cuong.pdf", 340))

    pics = root.add(TreeNode("Pictures", is_folder=True))
    trip = pics.add(TreeNode("DaLat", is_folder=True))
    trip.add(TreeNode("anh1.jpg", 2048))
    trip.add(TreeNode("anh2.jpg", 1536))

    root.add(TreeNode("readme.txt", 4))

    print("\n--- Cấu trúc cây thư mục ---")
    print_tree(root)

    print(f"\nTổng số tệp tin       : {count_files(root)} tệp")
    print(f"Tổng dung lượng thư mục: {total_size(root)} KB")

    target = "anh2.jpg"
    print(f"Đường dẫn đến '{target}': {find_path(root, target)}")


if __name__ == "__main__":
    main()
