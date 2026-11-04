"""
BÀI TẬP 3: DUYỆT THEO CHIỀU RỘNG (BFS) VÀ ĐƯỜNG ĐI NGẮN NHẤT (MỨC ĐỘ: DỄ - TRUNG BÌNH)
BFS trên đồ thị không trọng số luôn tìm ra đường đi ít cạnh nhất (ngắn nhất).
"""

import sys
from collections import deque

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def bfs(graph: dict, start) -> list:
    """Duyệt BFS loang theo từng lớp."""
    visited = {start}
    order = []
    queue = deque([start])
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in graph.get(u, []):
            if v not in visited:
                visited.add(v)
                queue.append(v)
    return order


def shortest_path(graph: dict, start, goal):
    """Tìm đường đi ngắn nhất (ít cạnh nhất) từ start đến goal bằng BFS."""
    if start == goal:
        return [start]
    parent = {start: None}
    queue = deque([start])

    while queue:
        u = queue.popleft()
        if u == goal:
            break
        for v in graph.get(u, []):
            if v not in parent:
                parent[v] = u
                queue.append(v)

    if goal not in parent:
        return None  # Không có đường đi

    # Truy vết ngược từ goal về start
    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    return path[::-1]


def distances(graph: dict, start) -> dict:
    """Tính khoảng cách (số cạnh) từ start đến tất cả các đỉnh khác."""
    dist = {start: 0}
    queue = deque([start])
    while queue:
        u = queue.popleft()
        for v in graph.get(u, []):
            if v not in dist:
                dist[v] = dist[u] + 1
                queue.append(v)
    return dist


def main():
    print("=== BÀI TẬP 3: DUYỆT THEO CHIỀU RỘNG (BFS) ===")
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
        "G": []  # Đỉnh cô lập
    }

    print("Thứ tự duyệt BFS từ đỉnh A:", bfs(graph, "A"))
    print("Đường đi ngắn nhất A -> F  :", shortest_path(graph, "A", "F"))
    print("Đường đi ngắn nhất A -> G  :", shortest_path(graph, "A", "G"))
    print("Khoảng cách từ A tới các đỉnh:", distances(graph, "A"))


if __name__ == "__main__":
    main()
