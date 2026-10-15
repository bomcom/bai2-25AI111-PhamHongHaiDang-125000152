"""
BÀI TẬP 2: MÔ PHỎNG HÀNG CHỜ KHÁM BỆNH (QUEUE - FIFO) (MỨC ĐỘ: DỄ - TRUNG BÌNH)
Được cấu trúc theo chuẩn Hướng đối tượng (OOP) với class HangChoKhamBenh sử dụng collections.deque.

Yêu cầu:
1. Thêm bệnh nhân mới vào hàng chờ (.append())
2. Gọi bệnh nhân tiếp theo vào khám (.popleft() - lấy người đầu tiên và xóa khỏi hàng)
3. Xem danh sách bệnh nhân đang chờ
4. Thoát
Lưu ý: Nếu hàng chờ trống mà gọi khám, phải thông báo 'Hàng chờ trống.'
"""

from collections import deque


class HangChoKhamBenh:
    """Class quản lý hàng đợi khám bệnh (Vào trước - Ra trước: FIFO)"""

    def __init__(self):
        # Tạo hàng đợi rỗng cho chính đối tượng này
        self.patient_queue = deque()

    def them_benh_nhan(self, ten_benh_nhan: str):
        """Thêm bệnh nhân mới vào cuối hàng chờ (.append())"""
        self.patient_queue.append(ten_benh_nhan)
        print(f"-> Đã thêm bệnh nhân '{ten_benh_nhan}' vào hàng chờ.")

    def goi_kham(self):
        """Gọi bệnh nhân đầu tiên vào khám (.popleft())"""
        # Kiểm tra nếu hàng chờ trống
        if len(self.patient_queue) == 0:
            print("-> Hàng chờ trống.")
            return None

        # Lấy người đứng đầu hàng ra khám (FIFO: First In First Out)
        benh_nhan = self.patient_queue.popleft()
        print(f"-> Mời bệnh nhân '{benh_nhan}' vào phòng khám!")
        return benh_nhan

    def xem_danh_sach(self):
        """Hiển thị tất cả bệnh nhân đang chờ"""
        if len(self.patient_queue) == 0:
            print("-> Hiện tại không có bệnh nhân nào đang chờ.")
            return

        print(f"\n--- DANH SÁCH BỆNH NHÂN ĐANG CHỜ ({len(self.patient_queue)} người) ---")
        for stt, ten in enumerate(self.patient_queue, start=1):
            print(f"  {stt}. {ten}")


def main():
    phong_kham = HangChoKhamBenh()

    while True:
        print("\n=== PHÒNG KHÁM - HÀNG CHỜ BỆNH NHÂN ===")
        print("1. Thêm bệnh nhân mới vào hàng chờ")
        print("2. Bác sĩ gọi bệnh nhân tiếp theo vào khám")
        print("3. Xem danh sách bệnh nhân đang chờ")
        print("4. Thoát")

        choice = input("Lựa chọn (1-4): ").strip()

        if choice == "1":
            ten = input("Nhập tên bệnh nhân: ").strip()
            if ten:
                phong_kham.them_benh_nhan(ten)
            else:
                print("Tên bệnh nhân không được để trống!")

        elif choice == "2":
            phong_kham.goi_kham()

        elif choice == "3":
            phong_kham.xem_danh_sach()

        elif choice == "4":
            print("Đã kết thúc ca khám bệnh. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 4!")


if __name__ == "__main__":
    main()
