"""
BÀI TẬP 5: TỔ HỢP SỐ (COMBINATION SUM) - CÓ TỐI ƯU HÓA (MỨC ĐỘ: KHÓ)
Tìm tất cả các tổ hợp duy nhất từ mảng candidates sao cho tổng bằng target.
Một phần tử có thể được tái sử dụng nhiều lần.
Kỹ thuật tối ưu hóa:
  1. Sắp xếp mảng để cắt tỉa sớm (Pruning) khi candidates[i] > remaining_target.
  2. Truyền con trỏ start để tránh tạo ra các tổ hợp trùng thứ tự (như [2,2,3] và [2,3,2]).
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


class CombinationSumSolver:
    """Lớp tìm tổ hợp có tổng bằng target sử dụng quay lui kết hợp cắt tỉa."""

    def combination_sum(self, candidates: list[int], target: int) -> list[list[int]]:
        results = []
        candidates.sort()  # Sắp xếp để hỗ trợ cắt tỉa nhánh đệ quy

        def find_combinations(
            remaining_target: int,
            start: int,
            current_combination: list[int]
        ) -> None:
            # 1. Điều kiện dừng thành công: Tổng các số đã vừa đúng bằng target
            if remaining_target == 0:
                results.append(list(current_combination))
                return

            # 2. Vòng lặp các lựa chọn khả dĩ từ vị trí 'start' trở đi
            for i in range(start, len(candidates)):
                # Cắt tỉa (Pruning): Vì mảng đã xếp tăng dần, số hiện tại > target
                # thì mọi số phía sau cũng lớn hơn -> break ngay lập tức
                if candidates[i] > remaining_target:
                    break

                # 3. Thử (Try): Thêm candidates[i] vào tổ hợp đang xét
                current_combination.append(candidates[i])

                # 4. Đệ quy: Cho phép tái sử dụng chính candidates[i] nên truyền lại start là i
                find_combinations(
                    remaining_target - candidates[i],
                    i,
                    current_combination
                )

                # 5. Quay lui (Backtrack): Xóa số vừa thêm để thử lựa chọn kế tiếp
                current_combination.pop()

        find_combinations(target, 0, [])
        return results


def main():
    solver = CombinationSumSolver()

    test_cases = [
        ([2, 3, 6, 7], 7),
        ([2, 3, 5], 8),
        ([2], 1)
    ]

    for candidates, target in test_cases:
        ans = solver.combination_sum(candidates, target)
        print(f"Candidates = {candidates}, Target = {target}")
        print(f"-> Các tổ hợp tìm được: {ans}\n")


if __name__ == "__main__":
    main()
