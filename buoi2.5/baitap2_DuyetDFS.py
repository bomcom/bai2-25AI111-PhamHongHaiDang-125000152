"""
BÀI TẬP 2: DUYỆT ĐỒ THỊ THEO CHIỀU SÂU (DFS) (MỨC ĐỘ: DỄ)
Cài đặt cả DFS đệ quy và DFS dùng Stack tự quản lý.
Kiểm tra tính tồn tại của đường đi giữa 2 đỉnh (has_path).
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def dfs_recursive(graph: dict, start, visited=None, order=None) -> list:
    """Duyệt DFS bằng đệ quy."""
    if visited is None:
        visited, order = set(), []
    visited.add(start)
    order.append(start)
    for v in graph.get(start, []):
        if v not in visited:
            dfs_recursive(graph, v, visited, order)
    return order


def dfs_iterative(graph: dict, start) -> list:
    """Duyệt DFS bằng Stack tự quản lý (không dùng đệ quy)."""
    visited, order = set(), []
    stack = [start]
    while stack:
        u = stack.pop()
        if u in visited:
            continue
        visited.add(u)
        order.append(u)
        # Đảo ngược danh sách kề để thứ tự thăm giống bản đệ quy
        for v in reversed(graph.get(u, [])):
            if v not in visited:
                stack.append(v)
    return order


def has_path(graph: dict, u, v) -> bool:
    """Kiểm tra có đường đi từ u đến v hay không."""
    reachable = dfs_iterative(graph, u)
    return v in reachable


def main():
    print("=== BÀI TẬP 2: DUYỆT ĐỒ THỊ THEO CHIỀU SÂU (DFS) ===")
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"]
    }

    r1 = dfs_recursive(graph, "A")
    r2 = dfs_iterative(graph, "A")
    print(f"DFS đệ quy: {r1}")
    print(f"DFS Stack : {r2}")
    print(f"Hai kết quả trùng khớp hoàn toàn? {r1 == r2}")

    print(f"\nCó đường đi từ D đến F không? {has_path(graph, 'D', 'F')} (Kỳ vọng: True)")
    print(f"Có đường đi từ A đến Z không? {has_path(graph, 'A', 'Z')} (Kỳ vọng: False)")


if __name__ == "__main__":
    main()
