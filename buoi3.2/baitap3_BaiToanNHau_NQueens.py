"""
BÀI TẬP 3: BÀI TOÁN N HẬU (N-QUEENS) (MỨC ĐỘ: TRUNG BÌNH)
Đặt N con hậu trên bàn cờ N x N sao cho không có 2 con hậu nào ăn nhau
(không cùng hàng, cùng cột, cùng đường chéo chính hoặc chéo phụ).
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


class NQueensSolver:
    """Lớp giải bài toán N Hậu và đếm số lượng cách xếp hợp lệ."""

    def __init__(self):
        self.solution_count = 0
        self.solutions = []

    def solve_n_queens(self, n: int) -> int:
        self.solution_count = 0
        self.solutions = []
        positions = [-1] * n  # positions[row] = col

        def is_safe(current_row: int, current_col: int) -> bool:
            for prev_row in range(current_row):
                prev_col = positions[prev_row]
                # Kiểm tra trùng cột
                if prev_col == current_col:
                    return False
                # Kiểm tra trùng đường chéo (hiệu hàng == hiệu cột)
                if abs(current_row - prev_row) == abs(current_col - prev_col):
                    return False
            return True

        def place_queen(row: int) -> None:
            # 1. Điều kiện dừng: Đã đặt thành công N con hậu từ hàng 0 đến n-1
            if row == n:
                self.solution_count += 1
                self.solutions.append(list(positions))
                return

            # 2. Thử đặt hậu ở hàng 'row' vào từng cột 'col' từ 0 đến n-1
            for col in range(n):
                if is_safe(row, col):
                    # Thử (Try)
                    positions[row] = col

                    # Đệ quy sang hàng tiếp theo
                    place_queen(row + 1)

                    # Quay lui ngầm định: positions[row] sẽ bị ghi đè ở vòng lặp col sau

        place_queen(0)
        return self.solution_count

    def print_board(self, positions: list[int]) -> None:
        n = len(positions)
        for col in positions:
            row_str = ["."] * n
            row_str[col] = "Q"
            print(" ".join(row_str))
        print()


def main():
    solver = NQueensSolver()
    for n in [4, 8]:
        count = solver.solve_n_queens(n)
        print(f"=== KẾT QUẢ VỚI BÀN CỜ {n}x{n} ===")
        print(f"Tổng số cách đặt hợp lệ: {count}")
        if solver.solutions:
            print("Minh họa 1 cách đặt hợp lệ đầu tiên:")
            solver.print_board(solver.solutions[0])


if __name__ == "__main__":
    main()
