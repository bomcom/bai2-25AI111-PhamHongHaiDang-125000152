"""
BÀI TẬP 5: PHÁT HIỆN CHU TRÌNH (CYCLE DETECTION) (MỨC ĐỘ: TRUNG BÌNH)
- Vô hướng: DFS kiểm tra gặp đỉnh đã thăm không phải cha (parent).
- Có hướng: Thuật toán 3 màu (WHITE, GRAY, BLACK). Gặp lại đỉnh GRAY = có chu trình!
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def has_cycle_undirected(graph: dict) -> bool:
    """Phát hiện chu trình trong đồ thị vô hướng."""
    visited = set()

    def dfs(u, parent):
        visited.add(u)
        for v in graph.get(u, []):
            if v not in visited:
                if dfs(v, u):
                    return True
            elif v != parent:
                # Đã thăm và không phải đỉnh cha trực tiếp -> có chu trình!
                return True
        return False

    return any(s not in visited and dfs(s, None) for s in graph)


def has_cycle_directed(graph: dict) -> bool:
    """Phát hiện chu trình trong đồ thị có hướng bằng 3 màu: 0=WHITE, 1=GRAY, 2=BLACK."""
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {u: WHITE for u in graph}

    def dfs(u):
        color[u] = GRAY  # Đang thăm
        for v in graph.get(u, []):
            if color.get(v, WHITE) == GRAY:
                # Quay về đỉnh đang nằm trên đường đi DFS hiện tại -> có chu trình!
                return True
            if color.get(v, WHITE) == WHITE and dfs(v):
                return True
        color[u] = BLACK  # Đã duyệt xong toàn bộ nhánh của u
        return False

    return any(color[u] == WHITE and dfs(u) for u in graph)


def is_tree(graph: dict) -> bool:
    """Đồ thị vô hướng là cây khi và chỉ khi nó liên thông và không có chu trình."""
    if not graph:
        return False
    start = next(iter(graph))
    visited, stack = {start}, [start]
    while stack:
        u = stack.pop()
        for v in graph.get(u, []):
            if v not in visited:
                visited.add(v)
                stack.append(v)
    return len(visited) == len(graph) and not has_cycle_undirected(graph)


def main():
    print("=== BÀI TẬP 5: PHÁT HIỆN CHU TRÌNH ===")

    triangle = {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}
    line = {"A": ["B"], "B": ["A", "C"], "C": ["B"]}

    print(f"Tam giác vô hướng có chu trình? {has_cycle_undirected(triangle)} (Kỳ vọng: True)")
    print(f"Đường thẳng vô hướng có chu trình? {has_cycle_undirected(line)} (Kỳ vọng: False)")
    print(f"Đường thẳng có phải là cây? {is_tree(line)} (Kỳ vọng: True)")

    loop_directed = {"A": ["B"], "B": ["C"], "C": ["A"]}
    diamond_directed = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}

    print(f"\nĐồ thị vòng A->B->C->A có chu trình? {has_cycle_directed(loop_directed)} (Kỳ vọng: True)")
    print(f"Đồ thị kim cương có chu trình? {has_cycle_directed(diamond_directed)} (Kỳ vọng: False)")


if __name__ == "__main__":
    main()
