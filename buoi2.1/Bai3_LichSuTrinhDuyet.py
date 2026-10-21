"""
BÀI TẬP 3: MÔ PHỎNG LỊCH SỬ TRÌNH DUYỆT WEB (DOUBLY LINKED LIST) (MỨC ĐỘ: TRUNG BÌNH)
Yêu cầu:
1. Visit(url): Thêm trang mới ngay sau trang hiện tại, cắt bỏ toàn bộ lịch sử phía trước (forward)
2. Back(): Quay lại trang trước (prev)
3. Forward(): Tiến tới trang sau (next)
4. Hiển thị trang hiện tại
"""


class Node:
    def __init__(self, value: str):
        self.value = value
        self.prev = None
        self.next = None


class BrowserHistory:
    def __init__(self, homepage: str):
        # TODO: Khởi tạo nút trang chủ và gán current_node trỏ vào đó
        self.current_node = Node(homepage)

    def visit(self, url: str):
        # TODO:
        # 1. Tạo new_node với giá trị url
        # 2. Cắt bỏ forward history: nối current_node.next = new_node, new_node.prev = current_node
        # 3. Cập nhật current_node = new_node
        new_node = Node(url)
        self.current_node.next = new_node
        new_node.prev = self.current_node
        self.current_node = new_node    

    def go_back(self):
        # TODO:
        # 1. Kiểm tra xem current_node.prev có tồn tại hay không
        # 2. Nếu có, lùi current_node = current_node.prev
        # 3. Nếu không, thông báo 'Không có trang trước đó.'
        if self.current_node.prev:
            self.current_node = self.current_node.prev
            print(f"-> Đã quay lại trang: {self.current_node.value}")
        else:
            print("-> Không có trang trước đó.")        

    def go_forward(self):
        # TODO:
        # 1. Kiểm tra xem current_node.next có tồn tại hay không
        # 2. Nếu có, tiến current_node = current_node.next
        # 3. Nếu không, thông báo 'Không có trang phía trước.'
        if self.current_node.next:
            self.current_node = self.current_node.next
            print(f"-> Đã tiến tới trang: {self.current_node.value}")
        else:
            print("-> Không có trang phía trước.")            

    def show_current(self):
        print(f"Trang hiện tại: {self.current_node.value}")


def main():
    browser = BrowserHistory("google.com")

    while True:
        print("\n=== TRÌNH DUYỆT WEB ===")
        browser.show_current()
        print("1. Truy cập trang mới (Visit)")
        print("2. Quay lại trang trước (Back)")
        print("3. Đi tới trang sau (Forward)")
        print("4. Thoát")

        choice = input("Lựa chọn: ").strip()
        if choice == "1":
            url = input("Nhập URL: ").strip()
            browser.visit(url)
        elif choice == "2":
            browser.go_back()
        elif choice == "3":
            browser.go_forward()
        elif choice == "4":
            break
        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()
