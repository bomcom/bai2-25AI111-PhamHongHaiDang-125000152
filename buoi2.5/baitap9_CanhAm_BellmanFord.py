"""
BÀI TẬP 9: CẠNH ÂM VÀ CHU TRÌNH ÂM – THUẬT TOÁN BELLMAN-FORD (MỨC ĐỘ: RẤT KHÓ)
Tìm đường đi ngắn nhất khi có trọng số âm và phát hiện chu trình âm (Negative Cycle).
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

INF = float("inf")


def bellman_ford(vertices: list, edges: list, source):
    """Thuật toán Bellman-Ford. Trả về (dist, parent) hoặc (None, None) nếu có chu trình âm."""
    dist = {v: INF for v in vertices}
    parent = {v: None for v in vertices}
    dist[source] = 0

    # Nới lỏng toàn bộ các cạnh V - 1 lần
    for _ in range(len(vertices) - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                updated = True
        if not updated:  # Tối ưu: Dừng sớm nếu không còn nới lỏng được cạnh nào
            break

    # Vòng lặp thứ V để kiểm tra chu trình âm
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            return None, None  # Phát hiện chu trình âm!

    return dist, parent


def main():
    print("=== BÀI TẬP 9: THUẬT TOÁN BELLMAN-FORD ===")
    vertices = ["S", "A", "B", "C", "D"]

    # Đồ thị 1: Có cạnh âm nhưng KHÔNG có chu trình âm
    ok_edges = [
        ("S", "A", 4), ("S", "B", 5), ("A", "C", -3),
        ("B", "C", 2), ("C", "D", 4)
    ]
    dist, _ = bellman_ford(vertices, ok_edges, "S")
    print(f"Đồ thị 1 (cạnh âm hợp lệ): Khoảng cách từ S = {dist}")

    # Đồ thị 2: Có chu trình âm (A -> B -> C -> A với tổng trọng số 1 + 2 - 5 = -2 < 0)
    bad_edges = [
        ("S", "A", 1), ("A", "B", 1), ("B", "C", 2),
        ("C", "A", -5), ("C", "D", 3)
    ]
    dist_bad, _ = bellman_ford(vertices, bad_edges, "S")
    if dist_bad is None:
        print("Đồ thị 2: Phát hiện chu trình âm! Không tồn tại đường đi ngắn nhất.")


if __name__ == "__main__":
    main()
