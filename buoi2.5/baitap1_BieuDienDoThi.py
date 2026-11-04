"""
BÀI TẬP 1: BIỂU DIỄN ĐỒ THỊ – MA TRẬN KỀ VÀ DANH SÁCH KỀ (MỨC ĐỘ: DỄ)
Lưu trữ đồng thời bằng Ma trận kề (Adjacency Matrix) và Danh sách kề (Adjacency List).
Hỗ trợ cả đồ thị có hướng và vô hướng, có trọng số.
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


class Graph:
    """Đồ thị lưu đồng thời bằng ma trận kề và danh sách kề."""
    def __init__(self, vertices, directed: bool = False):
        self.vertices = list(vertices)
        self.index = {v: i for i, v in enumerate(self.vertices)}
        self.directed = directed
        n = len(self.vertices)
        self.matrix = [[0] * n for _ in range(n)]
        self.adj = {v: [] for v in self.vertices}

    def add_edge(self, u, v, weight: int = 1):
        i, j = self.index[u], self.index[v]
        self.matrix[i][j] = weight
        self.adj[u].append((v, weight))
        if not self.directed:
            # Vô hướng: cập nhật cả chiều ngược lại
            self.matrix[j][i] = weight
            self.adj[v].append((u, weight))

    def has_edge(self, u, v) -> bool:
        return self.matrix[self.index[u]][self.index[v]] != 0

    def degree(self, v) -> int:
        """Đồ thị vô hướng: bậc của đỉnh; Đồ thị có hướng: bán bậc ra (out-degree)."""
        return len(self.adj[v])

    def in_degree(self, v) -> int:
        """Bán bậc vào (in-degree) đối với đồ thị có hướng."""
        j = self.index[v]
        return sum(1 for row in self.matrix if row[j] != 0)

    def print_matrix(self):
        print("  " + " ".join(self.vertices))
        for v, row in zip(self.vertices, self.matrix):
            print(f"{v} " + " ".join(str(x) for x in row))

    def print_adj(self):
        for v in self.vertices:
            neighbors = [f"{u}(w={w})" if w != 1 else str(u) for u, w in self.adj[v]]
            print(f"{v} -> [{', '.join(neighbors)}]")


def main():
    print("=== BÀI TẬP 1: BIỂU DIỄN ĐỒ THỊ ===")

    print("--- 1. Đồ thị vô hướng (5 đỉnh, 6 cạnh) ---")
    g = Graph(["A", "B", "C", "D", "E"], directed=False)
    edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E"), ("B", "C")]
    for u, v in edges:
        g.add_edge(u, v)

    print("\nMa trận kề:")
    g.print_matrix()

    print("\nDanh sách kề:")
    g.print_adj()

    print(f"\nCó cạnh A-D không? {g.has_edge('A', 'D')}")
    print(f"Bậc của đỉnh D: {g.degree('D')}")

    print("\n--- 2. Đồ thị có hướng (Directed Graph) ---")
    d = Graph(["X", "Y", "Z"], directed=True)
    d.add_edge("X", "Y")
    d.add_edge("X", "Z")
    d.add_edge("Y", "Z")
    for v in d.vertices:
        print(f"Đỉnh {v}: bậc ra = {d.degree(v)}, bậc vào = {d.in_degree(v)}")


if __name__ == "__main__":
    main()
