"""
BÀI TẬP 1: LIỆT KÊ HOÁN VỊ (PERMUTATIONS) (MỨC ĐỘ: DỄ)
Thuật toán quay lui (Backtracking) để tìm tất cả hoán vị của danh sách số.
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


class Permutations:
    """Lớp sinh tất cả hoán vị của một tập hợp các số."""

    def find_permutations(self, nums: list[int]) -> list[list[int]]:
        """Khởi tạo trạng thái và bắt đầu quá trình quay lui."""
        results = []
        current_permutation = []
        used = [False] * len(nums)
        self._generate(nums, current_permutation, used, results)
        return results

    def _generate(
        self,
        nums: list[int],
        current_permutation: list[int],
        used: list[bool],
        results: list[list[int]],
    ) -> None:
        # 1. Điều kiện dừng: Khi độ dài hoán vị bằng độ dài danh sách ban đầu
        if len(current_permutation) == len(nums):
            results.append(list(current_permutation))
            return

        # 2. Vòng lặp duyệt qua các lựa chọn khả dĩ
        for i in range(len(nums)):
            if not used[i]:
                # 3. Thử (Try): Thêm phần tử và đánh dấu đã dùng
                current_permutation.append(nums[i])
                used[i] = True

                # 4. Đệ quy đi sâu vào nhánh tiếp theo
                self._generate(nums, current_permutation, used, results)

                # 5. Quay lui (Backtrack): Hoàn tác trạng thái để thử nhánh khác
                used[i] = False
                current_permutation.pop()


def main():
    solver = Permutations()
    data = [1, 2, 3]
    print(f"Danh sách đầu vào: {data}")
    permutations = solver.find_permutations(data)

    print(f"Tổng số hoán vị tìm được: {len(permutations)}")
    print("Danh sách các hoán vị:")
    for p in permutations:
        print(p)


if __name__ == "__main__":
    main()
