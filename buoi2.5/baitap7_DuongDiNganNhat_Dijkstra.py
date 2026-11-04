"""
BÀI TẬP 7: ĐƯỜNG ĐI NGẮN NHẤT CÓ TRỌNG SỐ – THUẬT TOÁN DIJKSTRA (MỨC ĐỘ: KHÓ)
Sử dụng hàng đợi ưu tiên heapq để tìm đường đi ngắn nhất trên đồ thị trọng số không âm.
"""

import heapq
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def dijkstra(graph: dict, source):
    """Thuật toán Dijkstra trả về dist và parent."""
    dist = {u: float("inf") for u in graph}
    parent = {u: None for u in graph}
    dist[source] = 0
    heap = [(0, source)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue

        for v, w in graph.get(u, []):
            if dist[u] + w < dist[v]:  # Bước nới lỏng (Relaxation)
                dist[v] = dist[u] + w
                parent[v] = u
                heapq.heappush(heap, (dist[v], v))

    return dist, parent


def get_path(parent: dict, target):
    """Truy vết đường đi từ nguồn đến đích."""
    path = []
    cur = target
    while cur is not None:
        path.append(cur)
        cur = parent.get(cur)
    return path[::-1]


def build_undirected(edges: list):
    graph = {}
    for u, v, w in edges:
        graph.setdefault(u, []).append((v, w))
        graph.setdefault(v, []).append((u, w))
    return graph


def main():
    print("=== BÀI TẬP 7: THUẬT TOÁN DIJKSTRA ===")
    edges = [
        ("A", "B", 4), ("A", "C", 2), ("B", "C", 1), ("B", "D", 5),
        ("C", "D", 8), ("C", "E", 10), ("D", "E", 2), ("D", "F", 6),
        ("E", "F", 3)
    ]
    graph = build_undirected(edges)
    graph["G"] = []  # Đỉnh không thể đến được

    dist, parent = dijkstra(graph, "A")
    print("Khoảng cách ngắn nhất và đường đi từ A:")
    for v in sorted(graph):
        if dist[v] == float("inf"):
            print(f"  A -> {v}: Không có đường đi")
        else:
            path_str = " -> ".join(get_path(parent, v))
            print(f"  A -> {v}: {dist[v]:>2} (Đường đi: {path_str})")


if __name__ == "__main__":
    main()
