"""
TEST SUITE TOÀN DIỆN CHO BUỔI 3.2 - ĐỆ QUY & BACKTRACKING
Kiểm tra tính chính xác và hiệu năng của cả 5 bài tập.
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from baitap1_LietKeHoanVi_Permutations import Permutations
from baitap2_TimDuongMeCung_MazeSolver import MazeSolver
from baitap3_BaiToanNHau_NQueens import NQueensSolver
from baitap4_GiaiSudoku_SudokuSolver import SudokuSolver
from baitap5_ToHopSo_CombinationSum import CombinationSumSolver


def test_bai1():
    print("-> Đang kiểm tra Bài 1 (Hoán vị)...", end=" ")
    solver = Permutations()
    res1 = solver.find_permutations([1, 2, 3])
    assert len(res1) == 6, f"Sai số lượng hoán vị: {len(res1)}"
    assert [1, 2, 3] in res1
    assert [3, 2, 1] in res1

    res2 = solver.find_permutations([1])
    assert res2 == [[1]]
    print("PASS! [OK]")


def test_bai2():
    print("-> Đang kiểm tra Bài 2 (Mê cung)...", end=" ")
    solver = MazeSolver()

    # Mê cung có đường
    grid1 = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]
    ]
    assert solver.find_path(grid1) is True
    assert grid1[0][0] == 2 and grid1[3][3] == 2

    # Mê cung bị chặn hoàn toàn
    grid2 = [
        [1, 0],
        [0, 1]
    ]
    assert solver.find_path(grid2) is False
    print("PASS! [OK]")


def test_bai3():
    print("-> Đang kiểm tra Bài 3 (N Hậu)...", end=" ")
    solver = NQueensSolver()
    # N = 4 -> 2 lời giải
    assert solver.solve_n_queens(4) == 2, f"N=4 sai: {solver.solution_count}"
    # N = 8 -> 92 lời giải chuẩn xác
    assert solver.solve_n_queens(8) == 92, f"N=8 sai: {solver.solution_count}"
    # N = 1 -> 1 lời giải
    assert solver.solve_n_queens(1) == 1
    print("PASS! [OK]")


def test_bai4():
    print("-> Đang kiểm tra Bài 4 (Giải Sudoku)...", end=" ")
    solver = SudokuSolver()
    board = [
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
    success = solver.solve(board)
    assert success is True
    # Kiểm tra mỗi hàng đủ từ 1 đến 9
    for row in board:
        assert set(row) == set(range(1, 10))
    # Kiểm tra mỗi cột đủ từ 1 đến 9
    for col in range(9):
        col_vals = [board[r][col] for r in range(9)]
        assert set(col_vals) == set(range(1, 10))
    print("PASS! [OK]")


def test_bai5():
    print("-> Đang kiểm tra Bài 5 (Tổ hợp số Combination Sum)...", end=" ")
    solver = CombinationSumSolver()
    res1 = solver.combination_sum([2, 3, 6, 7], 7)
    assert sorted(res1) == [[2, 2, 3], [7]], f"Sai kết quả: {res1}"

    res2 = solver.combination_sum([2, 3, 5], 8)
    assert sorted(res2) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

    res3 = solver.combination_sum([2], 1)
    assert res3 == []
    print("PASS! [OK]")


if __name__ == "__main__":
    print("==================================================")
    print("    CHẠY TEST TOÀN BỘ BÀI TẬP BUỔI 3.2 (BACKTRACKING)")
    print("==================================================")
    test_bai1()
    test_bai2()
    test_bai3()
    test_bai4()
    test_bai5()
    print("==================================================")
    print("   TẤT CẢ 5 BÀI TẬP ĐỀU VƯỢT QUA TEST 100%! [SUCCESS]")
    print("==================================================")
