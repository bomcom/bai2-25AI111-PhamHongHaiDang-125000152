"""
BÀI TẬP 8: CÂY KHUNG NHỎ NHẤT (MINIMUM SPANNING TREE – KRUSKAL) (MỨC ĐỘ: KHÓ)
Sử dụng cấu trúc Disjoint Set (Union-Find) kết hợp nén đường đi (Path Compression) và gộp theo hạng (Rank).
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


class DisjointSet:
    def __init__(self, items):
        self.parent = {x: x for x in items}
        self.rank = {x: 0 for x in items}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Nén đường đi
        return self.parent[x]

    def union(self, a, b) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False  # Cùng tập hợp -> thêm cạnh này sẽ tạo chu trình!

        # Gộp theo rank
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True


def kruskal(vertices: list, edges: list):
    """edges là danh sách các bộ (trọng_số, u, v)."""
    ds = DisjointSet(vertices)
    mst = []
    total = 0

    for w, u, v in sorted(edges):
        if ds.union(u, v):
            mst.append((u, v, w))
            total += w
            if len(mst) == len(vertices) - 1:
                break

    return mst, total


def main():
    print("=== BÀI TẬP 8: CÂY KHUNG NHỎ NHẤT (MST - KRUSKAL) ===")
    vertices = ["A", "B", "C", "D", "E", "F"]
    edges = [
        (7, "A", "B"), (5, "A", "D"), (8, "B", "C"), (9, "B", "D"),
        (7, "B", "E"), (5, "C", "E"), (15, "D", "E"), (6, "D", "F"),
        (8, "E", "F")
    ]

    mst, total = kruskal(vertices, edges)
    print("Các cạnh được chọn vào cây khung nhỏ nhất (MST):")
    for u, v, w in mst:
        print(f"  {u} - {v} (chi phí: {w})")
    print(f"-> Tổng chi phí tối thiểu của MST: {total}")
    print(f"Số cạnh = {len(mst)} (Kỳ vọng V - 1 = {len(vertices) - 1}): {len(mst) == len(vertices) - 1}")


if __name__ == "__main__":
    main()
