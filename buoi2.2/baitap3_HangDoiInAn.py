"""
BÀI TẬP 3: MÔ PHỎNG HÀNG ĐỢI IN ẤN (MỨC ĐỘ: DỄ - QUEUE)
Quản lý các tài liệu chờ in theo nguyên tắc FIFO (First-In, First-Out).
"""

import sys
from collections import deque

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


class PrintSpooler:
    def __init__(self):
        self.queue = deque()

    def add_document(self, doc_name: str):
        self.queue.append(doc_name)
        print(f'-> Đã thêm tài liệu "{doc_name}" vào hàng đợi in.')

    def print_next(self):
        if len(self.queue) > 0:
            doc = self.queue.popleft()
            print(f'-> Đang in: "{doc}"... Đã in xong!')
        else:
            print("Không có tài liệu nào trong hàng đợi in.")

    def peek_next(self):
        if len(self.queue) > 0:
            print(f'-> Tài liệu tiếp theo sẽ được in: "{self.queue[0]}"')
        else:
            print("Hàng đợi in đang trống.")

    def show_all(self):
        if len(self.queue) == 0:
            print("Hàng đợi in đang trống.")
        else:
            print(f"Danh sách tài liệu đang chờ ({len(self.queue)} tài liệu):")
            for i, doc in enumerate(self.queue, 1):
                print(f"  {i}. {doc}")


def main():
    spooler = PrintSpooler()
    # Thêm sẵn một vài tài liệu mẫu
    spooler.add_document("BaoCaoDoAn.docx")
    spooler.add_document("TaiLieuMangCCNA.pdf")

    while True:
        print("\n=== MÔ PHỎNG MÁY IN (PRINT QUEUE) ===")
        print("1. Thêm tài liệu mới vào hàng đợi")
        print("2. Thực hiện in tài liệu tiếp theo")
        print("3. Xem tài liệu sắp được in (Peek)")
        print("4. Xem toàn bộ hàng đợi")
        print("5. Thoát")

        choice = input("Lựa chọn (1-5): ").strip()
        if choice == "1":
            name = input("Nhập tên tài liệu (kèm đuôi .pdf, .doc...): ").strip()
            if name:
                spooler.add_document(name)
        elif choice == "2":
            spooler.print_next()
        elif choice == "3":
            spooler.peek_next()
        elif choice == "4":
            spooler.show_all()
        elif choice == "5":
            print("Đã đóng chương trình quản lý in ấn.")
            break
        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()
