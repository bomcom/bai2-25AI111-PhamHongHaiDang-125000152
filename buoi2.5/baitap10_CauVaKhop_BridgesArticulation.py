"""
BÀI TẬP 10: CẦU VÀ KHỚP – ĐÁNH GIÁ ĐỘ TIN CẬY CỦA MẠNG (MỨC ĐỘ: RẤT KHÓ)
Thuật toán Tarjan (tin, low-link) tìm điểm nghẽn mạng trong O(V + E).
- Cầu (Bridge): cạnh mà nếu xóa đi thì đồ thị mất liên thông.
- Khớp (Articulation Point): đỉnh mà nếu xóa đi thì đồ thị mất liên thông.
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def find_bridges_and_articulation_points(graph: dict):
    tin, low = {}, {}
    timer = [0]
    bridges, points = [], set()

    def dfs(u, parent):
        tin[u] = low[u] = timer[0]
        timer[0] += 1
        children = 0

        for v in graph.get(u, []):
            if v == parent:
                continue
            if v in tin:
                # Cạnh ngược (Back edge)
                low[u] = min(low[u], tin[v])
            else:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                children += 1

                # Điều kiện là Cầu
                if low[v] > tin[u]:
                    bridges.append((u, v))

                # Điều kiện là Khớp (nút không phải gốc)
                if parent is not None and low[v] >= tin[u]:
                    points.add(u)

        # Điều kiện là Khớp (nút gốc cây DFS có từ 2 con trở lên)
        if parent is None and children > 1:
            points.add(u)

    for s in graph:
        if s not in tin:
            dfs(s, None)

    return bridges, sorted(points)


def is_connected_without(graph: dict, removed):
    """Hàm kiểm chứng: bỏ thử đỉnh removed và kiểm tra mạng còn liên thông không."""
    rest = [u for u in graph if u != removed]
    if not rest:
        return True
    visited, stack = {rest[0]}, [rest[0]]
    while stack:
        u = stack.pop()
        for v in graph.get(u, []):
            if v != removed and v not in visited:
                visited.add(v)
                stack.append(v)
    return len(visited) == len(rest)


def build_undirected(edges: list):
    graph = {}
    for u, v in edges:
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)
    return graph


def main():
    print("=== BÀI TẬP 10: TÌM CẦU VÀ KHỚP TRONG MẠNG ===")
    # Hai tam giác ABC và DEF nối với nhau bằng cạnh C-D
    edges = [
        ("A", "B"), ("B", "C"), ("C", "A"),
        ("C", "D"),
        ("D", "E"), ("E", "F"), ("F", "D")
    ]
    graph = build_undirected(edges)

    bridges, points = find_bridges_and_articulation_points(graph)
    print(f"Cầu (Bridges)             : {bridges} (Kỳ vọng: [('C', 'D')])")
    print(f"Khớp (Articulation Points): {points} (Kỳ vọng: ['C', 'D'])")

    print("\n--- Kiểm chứng bằng cách ngắt thử từng đỉnh ---")
    for u in sorted(graph):
        connected = is_connected_without(graph, u)
        status = "BÌNH THƯỜNG" if connected else "MẤT LIÊN THÔNG (KHỚP!)"
        print(f"Ngắt đỉnh {u}: {status}")


if __name__ == "__main__":
    main()
