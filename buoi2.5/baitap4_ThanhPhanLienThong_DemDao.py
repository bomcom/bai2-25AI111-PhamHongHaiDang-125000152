"""
BÀI TẬP 4: THÀNH PHẦN LIÊN THÔNG VÀ ĐẾM HÒN ĐẢO (MỨC ĐỘ: TRUNG BÌNH)
- Tìm các thành phần liên thông trong đồ thị vô hướng.
- Đếm số hòn đảo trên ma trận nhị phân (Connected Components trên Grid).
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def connected_components(graph: dict) -> list[list]:
    """Tìm danh sách tất cả các thành phần liên thông."""
    visited = set()
    components = []
    for s in graph:
        if s in visited:
            continue
        comp = []
        stack = [s]
        visited.add(s)
        while stack:
            u = stack.pop()
            comp.append(u)
            for v in graph.get(u, []):
                if v not in visited:
                    visited.add(v)
                    stack.append(v)
        components.append(comp)
    return components


def is_connected(graph: dict) -> bool:
    """Kiểm tra đồ thị vô hướng có liên thông toàn bộ không."""
    if not graph:
        return True
    return len(connected_components(graph)) <= 1


def count_islands(grid: list[str]) -> int:
    """Đếm số hòn đảo trên lưới 2D (4 hướng: trên, dưới, trái, phải)."""
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited = set()
    count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                count += 1  # Gặp đảo mới -> loang hết hòn đảo này
                visited.add((r, c))
                stack = [(r, c)]
                while stack:
                    x, y = stack.pop()
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nx, ny = x + dx, y + dy
                        if (0 <= nx < rows and 0 <= ny < cols and
                                grid[nx][ny] == "1" and (nx, ny) not in visited):
                            visited.add((nx, ny))
                            stack.append((nx, ny))
    return count


def main():
    print("=== BÀI TẬP 4: THÀNH PHẦN LIÊN THÔNG VÀ ĐẾM ĐẢO ===")

    graph = {
        "A": ["B"],
        "B": ["A"],
        "C": ["D"],
        "D": ["C"],
        "E": []
    }
    comps = connected_components(graph)
    print("Các thành phần liên thông:", comps)
    print(f"Số thành phần: {len(comps)} | Đồ thị liên thông? {is_connected(graph)}")

    grid = [
        "11000",
        "11000",
        "00100",
        "00011"
    ]
    print(f"\nSố hòn đảo đếm được trên lưới: {count_islands(grid)} (Kỳ vọng: 3)")


if __name__ == "__main__":
    main()
