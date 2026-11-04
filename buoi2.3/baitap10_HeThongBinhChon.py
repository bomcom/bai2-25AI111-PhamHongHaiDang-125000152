"""
BÀI TẬP 10: HỆ THỐNG BÌNH CHỌN TRỰC TUYẾN (VOTING SYSTEM) (MỨC ĐỘ: RẤT KHÓ - TỔNG HỢP DICT & SORTING)
Sử dụng nhiều Dictionary để đảm bảo tính toàn vẹn (mỗi user bầu 1 lần) và lấy Top kết quả.
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


class VotingSystem:
    def __init__(self):
        # Lưu vết user đã bình chọn chưa: { user_id: bool }
        self.has_voted: dict[str, bool] = {}
        # Lưu tổng số phiếu của từng ứng viên: { candidate_name: int }
        self.vote_counts: dict[str, int] = {}

    def vote(self, user_id: str, candidate: str) -> bool:
        if user_id in self.has_voted:
            print(f"❌ [TỪ CHỐI] User '{user_id}' đã bình chọn rồi, không được bầu lần hai.")
            return False

        self.has_voted[user_id] = True
        self.vote_counts[candidate] = self.vote_counts.get(candidate, 0) + 1
        print(f"✅ [THÀNH CÔNG] User '{user_id}' đã bình chọn cho '{candidate}'.")
        return True

    def get_top_3(self):
        # Sắp xếp danh sách tuples (candidate, votes)
        # key = lambda x: (-x[1], x[0]) nghĩa là:
        # Tiêu chí 1: -x[1] (Sắp xếp số phiếu giảm dần)
        # Tiêu chí 2: x[0] (Nếu bằng phiếu, xếp theo thứ tự bảng chữ cái A-Z)
        sorted_candidates = sorted(
            self.vote_counts.items(),
            key=lambda x: (-x[1], x[0])
        )

        print("\n🏆 --- BẢNG XẾP HẠNG TOP 3 ỨNG CỬ VIÊN ---")
        for rank, (cand, votes) in enumerate(sorted_candidates[:3], start=1):
            print(f"Hạng {rank}: {cand:<10} ({votes} phiếu)")
        return sorted_candidates[:3]


def main():
    print("=== BÀI TẬP 10: HỆ THỐNG BÌNH CHỌN TRỰC TUYẾN ===")
    system = VotingSystem()

    # Kịch bản bình chọn
    system.vote("user_001", "Alice")
    system.vote("user_002", "Bob")
    system.vote("user_003", "Alice")
    system.vote("user_004", "Charlie")
    system.vote("user_001", "David")  # Thử bình chọn lần 2 -> Bị từ chối
    system.vote("user_005", "Charlie")
    system.vote("user_006", "Alice")
    system.vote("user_007", "Bob")

    system.get_top_3()


if __name__ == "__main__":
    main()
