"""
FILE KIỂM THỬ THƯ VIỆN: main_test.py
Chạy file này để kiểm tra xem các hàm trong my_linkedlist.py của bạn đã hoạt động đúng chưa.
"""

from my_linkedlist import DoublyLinkedList


def run_tests():
    print("--- 1. Kiểm tra khởi tạo & hiển thị ---")
    dll = DoublyLinkedList(["A", "B", "C"])
    print(f"Danh sách ban đầu: {dll}")
    print(f"Độ dài len(dll): {len(dll)}")

    print("\n--- 2. Kiểm tra thêm đầu / cuối ---")
    dll.add_first("START")
    dll.add_last("END")
    print(f"Sau khi thêm START và END: {dll}")

    print("\n--- 3. Kiểm tra duyệt vòng lặp (Iterator) ---")
    for item in dll:
        print(f"-> {item}")

    print("\n--- 4. Kiểm tra tìm kiếm và chèn giữa ---")
    node_b = dll.find("B")
    if node_b:
        dll.add_after(node_b, "B_PLUS")
        print(f"Sau khi chèn B_PLUS sau B: {dll}")

    print("\n--- 5. Kiểm tra xóa ---")
    print("Xóa đầu:", dll.remove_first())
    print("Xóa cuối:", dll.remove_last())
    node_bp = dll.find("B_PLUS")
    if node_bp:
        dll.remove(node_bp)
        print("Đã xóa nút B_PLUS")
    print(f"Danh sách hiện tại: {dll}")


if __name__ == "__main__":
    run_tests()
