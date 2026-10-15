"""
BÀI TẬP 1: XÂY DỰNG PLAYLIST NHẠC (MỨC ĐỘ: DỄ)
Được cấu trúc theo chuẩn Hướng đối tượng (OOP) với class Playlist sử dụng deque.

Yêu cầu:
1. Thêm một bài hát vào cuối playlist (.append())
2. Thêm một bài hát vào đầu playlist (.appendleft())
3. Hiển thị playlist hiện tại
4. Thoát
"""

from collections import deque


class Playlist:
    """Class quản lý danh sách bài hát sử dụng cấu trúc dữ liệu deque (LinkedList đôi)"""

    def __init__(self, danh_sach_ban_dau=None):
        # self.playlist là thuộc tính của CHÍNH đối tượng Playlist này
        if danh_sach_ban_dau:
            self.playlist = deque(danh_sach_ban_dau)
        else:
            self.playlist = deque()

    def them_vao_cuoi(self, ten_bai_hat: str):
        """Thêm bài hát vào cuối danh sách phát"""
        self.playlist.append(ten_bai_hat)
        print(f"-> Đã thêm '{ten_bai_hat}' vào cuối danh sách.")

    def them_vao_dau(self, ten_bai_hat: str):
        """Thêm bài hát vào đầu danh sách để phát ngay sau bài hiện tại"""
        self.playlist.appendleft(ten_bai_hat)
        print(f"-> Đã thêm '{ten_bai_hat}' vào đầu danh sách (ưu tiên phát tiếp theo).")

    def hien_thi(self):
        """Duyệt và hiển thị danh sách bài hát hiện tại"""
        if not self.playlist:
            print("-> Playlist hiện đang trống!")
            return

        print("\n--- DANH SÁCH BÀI HÁT ĐANG PHÁT ---")
        for i, bai_hat in enumerate(self.playlist, start=1):
            print(f"  {i}. 🎵 {bai_hat}")


def main():
    # Khởi tạo đối tượng playlist với 2 bài hát mẫu
    my_playlist = Playlist(["Shape of You", "Blinding Lights"])

    while True:
        print("\n=== MENU PLAYLIST CỦA BẠN ===")
        print("1. Thêm bài hát vào cuối")
        print("2. Thêm bài hát vào đầu")
        print("3. Hiển thị playlist")
        print("4. Thoát")

        choice = input("Lựa chọn (1-4): ").strip()

        if choice == "1":
            ten_bai = input("Nhập tên bài hát cần thêm vào cuối: ").strip()
            if ten_bai:
                my_playlist.them_vao_cuoi(ten_bai)
            else:
                print("Tên bài hát không được để trống!")

        elif choice == "2":
            ten_bai = input("Nhập tên bài hát cần phát ưu tiên (vào đầu): ").strip()
            if ten_bai:
                my_playlist.them_vao_dau(ten_bai)
            else:
                print("Tên bài hát không được để trống!")

        elif choice == "3":
            my_playlist.hien_thi()

        elif choice == "4":
            print("Đã thoát chương trình nghe nhạc. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 4!")


if __name__ == "__main__":
    main()
