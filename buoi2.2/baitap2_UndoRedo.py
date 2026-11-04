"""
BÀI TẬP 2: CƠ CHẾ HOÀN TÁC & LÀM LẠI (UNDO / REDO) (MỨC ĐỘ: DỄ - TRUNG BÌNH - 2 STACKS)
Mô phỏng tính năng Ctrl + Z (Undo) và Ctrl + Y (Redo) trong các trình soạn thảo văn bản.
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = []
        self.redo_stack = []

    def write(self, new_text: str):
        # Lưu trạng thái cũ trước khi thay đổi vào undo_stack
        self.undo_stack.append(self.text)
        # Nhập mới sẽ làm mất lịch sử Redo
        self.redo_stack.clear()
        self.text += new_text
        print(f'-> Đã thêm: "{new_text}"')

    def undo(self):
        if not self.undo_stack:
            print("Không còn thao tác nào để Undo.")
            return
        # Đẩy trạng thái hiện tại vào redo_stack
        self.redo_stack.append(self.text)
        # Khôi phục trạng thái trước đó
        self.text = self.undo_stack.pop()
        print("-> Đã hoàn tác (Undo).")

    def redo(self):
        if not self.redo_stack:
            print("Không còn thao tác nào để Redo.")
            return
        # Đẩy trạng thái hiện tại vào undo_stack
        self.undo_stack.append(self.text)
        # Khôi phục trạng thái từ redo_stack
        self.text = self.redo_stack.pop()
        print("-> Đã làm lại (Redo).")

    def show(self):
        print(f'Nội dung hiện tại: "{self.text}"')


def main():
    editor = TextEditor()
    while True:
        print("\n=== TRÌNH SOẠN THẢO VĂN BẢN (UNDO / REDO) ===")
        editor.show()
        print("1. Nhập văn bản mới (Type)")
        print("2. Hoàn tác (Undo - Ctrl+Z)")
        print("3. Làm lại (Redo - Ctrl+Y)")
        print("4. Xem nội dung hiện tại")
        print("5. Thoát")

        choice = input("Lựa chọn (1-5): ").strip()
        if choice == "1":
            text = input("Nhập văn bản cần thêm: ")
            editor.write(text)
        elif choice == "2":
            editor.undo()
        elif choice == "3":
            editor.redo()
        elif choice == "4":
            editor.show()
        elif choice == "5":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 5.")


if __name__ == "__main__":
    main()
