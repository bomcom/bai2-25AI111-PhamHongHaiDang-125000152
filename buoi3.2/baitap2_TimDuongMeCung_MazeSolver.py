"""
BÀI TẬP 2: TÌM ĐƯỜNG ĐI TRONG MÊ CUNG (MAZE SOLVER) (MỨC ĐỘ: DỄ / TRUNG BÌNH)
Sử dụng quay lui 4 hướng (Xuống, Lên, Phải, Trái) để tìm đường từ (0,0) đến (N-1, M-1).
Ô giá trị:
  1: Đường đi hợp lệ (Walkable)
  0: Tường / Chướng ngại vật (Wall)
  2: Đã được đánh dấu thuộc đường đi thành công
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


class MazeSolver:
    """Lớp tìm đường đi trong mê cung ma trận 2D."""

    def find_path(self, maze: list[list[int]]) -> bool:
        if not maze or not maze[0]:
            return False

        n = len(maze)
        m = len(maze[0])

        def solve(x: int, y: int) -> bool:
            # 1. Điều kiện dừng thất bại: Vượt biên, gặp tường (0) hoặc ô đã đi (2)
            if x < 0 or x >= n or y < 0 or y >= m or maze[x][y] == 0 or maze[x][y] == 2:
                return False

            # 2. Thử (Try): Đánh dấu ô hiện tại thuộc đường đi
            maze[x][y] = 2

            # 3. Điều kiện dừng thành công: Đã chạm tới đích (n-1, m-1)
            if x == n - 1 and y == m - 1:
                return True

            # 4. Đệ quy thử 4 hướng di chuyển: Xuống, Lên, Phải, Trái
            if solve(x + 1, y):  # Xuống
                return True
            if solve(x - 1, y):  # Lên
                return True
            if solve(x, y + 1):  # Phải
                return True
            if solve(x, y - 1):  # Trái
                return True

            # 5. Quay lui (Backtrack): Cả 4 hướng đều là ngõ cụt, trả lại ô về 1
            maze[x][y] = 1
            return False

        return solve(0, 0)


def print_maze(maze: list[list[int]]) -> None:
    for row in maze:
        print(" ".join(f"{val:2}" for val in row))


def main():
    grid = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]
    ]

    print("Mê cung ban đầu (1: đường, 0: tường):")
    print_maze(grid)

    solver = MazeSolver()
    if solver.find_path(grid):
        print("\nTìm thấy đường đi! (Số 2 là đường đi tìm được):")
        print_maze(grid)
    else:
        print("\nKhông tìm thấy đường đi tới đích.")


if __name__ == "__main__":
    main()
