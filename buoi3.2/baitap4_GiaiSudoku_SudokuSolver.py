"""
BÀI TẬP 4: GIẢI SUDOKU (SUDOKU SOLVER) (MỨC ĐỘ: TRUNG BÌNH / KHÓ)
Điền các số từ 1 đến 9 vào ma trận 9x9 sao cho mỗi hàng, mỗi cột và
mỗi khối 3x3 đều chứa đủ các chữ số từ 1 đến 9 không trùng lặp.
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


class SudokuSolver:
    """Lớp giải bài toán Sudoku 9x9 bằng thuật toán quay lui."""

    def solve(self, board: list[list[int]]) -> bool:
        for r in range(9):
            for c in range(9):
                # 1. Tìm ô trống (có giá trị 0)
                if board[r][c] == 0:
                    # 2. Thử điền từng số từ 1 đến 9
                    for num in range(1, 10):
                        if self._is_valid(board, r, c, num):
                            # 3. Thử (Try): Điền số num vào ô
                            board[r][c] = num

                            # 4. Đệ quy tiếp tục giải phần còn lại
                            if self.solve(board):
                                return True

                            # 5. Quay lui (Backtrack): Hoàn tác về ô trống
                            board[r][c] = 0

                    # Đã thử từ 1-9 đều không thỏa mãn -> Nhánh sai
                    return False

        # Điều kiện dừng: Không còn ô trống nào -> Đã giải xong
        return True

    def _is_valid(self, board: list[list[int]], row: int, col: int, num: int) -> bool:
        # Kiểm tra trùng hàng và trùng cột
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False

        # Kiểm tra trùng trong ô vuông con 3x3
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for r in range(3):
            for c in range(3):
                if board[start_row + r][start_col + c] == num:
                    return False

        return True


def print_sudoku(board: list[list[int]]) -> None:
    for i, row in enumerate(board):
        if i > 0 and i % 3 == 0:
            print("- " * 11)
        row_str = []
        for j, val in enumerate(row):
            if j > 0 and j % 3 == 0:
                row_str.append("|")
            row_str.append(str(val) if val != 0 else ".")
        print(" ".join(row_str))


def main():
    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("=== MA TRẬN SUDOKU BAN ĐẦU ===")
    print_sudoku(sudoku_board)

    solver = SudokuSolver()
    if solver.solve(sudoku_board):
        print("\n=== GIẢI SUDOKU THÀNH CÔNG ===")
        print_sudoku(sudoku_board)
    else:
        print("\nKhông tìm được lời giải cho bảng Sudoku này.")


if __name__ == "__main__":
    main()
