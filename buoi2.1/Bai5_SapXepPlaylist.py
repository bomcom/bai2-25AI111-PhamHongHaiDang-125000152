"""
BÀI TẬP 5: SẮP XẾP LẠI PLAYLIST NHẠC - CẮT & NỐI CON TRỎ (MỨC ĐỘ: RẤT KHÓ)
Yêu cầu:
- Cho 1 playlist DoublyLinkedList ban đầu (A -> B -> C -> D -> E -> F -> G -> H)
- Cắt đoạn [start_song -> end_song]
- Chèn đoạn vừa cắt vào ngay sau destination_song
- Yêu cầu thao tác TRỰC TIẾP TRÊN CON TRỎ (next/prev), không sao chép mảng
"""

import sys

# Đảm bảo in tiếng Việt có dấu chuẩn xác trên console Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


class Node:
    def __init__(self, value: str):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, items=None):
        self.head = None
        self.tail = None
        if items:
            for item in items:
                self.append(item)

    def append(self, value: str):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def find(self, value: str):
        curr = self.head
        while curr:
            if curr.value == value:
                return curr
            curr = curr.next
        return None

    def to_list(self):
        res = []
        curr = self.head
        while curr:
            res.append(curr.value)
            curr = curr.next
        return res


def move_segment(dll: DoublyLinkedList, start_val: str, end_val: str, dest_val: str):
    # 1. Tìm các nút chính
    start_node = dll.find(start_val)
    end_node = dll.find(end_val)
    dest_node = dll.find(dest_val)

    if not start_node or not end_node or not dest_node:
        print("Lỗi: Không tìm thấy bài hát trong playlist!")
        return

    # Xác định các nút ranh giới xung quanh
    before_start = start_node.prev
    after_end = end_node.next
    after_dest = dest_node.next

    # Bước 1: Khâu lại vết cắt ở vị trí cũ (rút đoạn start -> end ra)
    if before_start:
        before_start.next = after_end
    else:
        dll.head = after_end

    if after_end:
        after_end.prev = before_start
    else:
        dll.tail = before_start

    # Bước 2: Nối đoạn đã cắt vào ngay sau dest_node
    dest_node.next = start_node
    start_node.prev = dest_node

    end_node.next = after_dest
    if after_dest:
        after_dest.prev = end_node
    else:
        dll.tail = end_node

    print(f"-> Đã di chuyển thành công đoạn [{start_val} -> {end_val}] ra sau bài {dest_val}!")


def main():
    playlist = DoublyLinkedList(["A", "B", "C", "D", "E", "F", "G", "H"])
    print("Playlist ban đầu:", " -> ".join(playlist.to_list()))

    # Ví dụ: Di chuyển đoạn C, D, E vào sau G
    # Kết quả mong muốn: A -> B -> F -> G -> C -> D -> E -> H
    start_s = input("Nhập bài hát bắt đầu đoạn cắt (ví dụ C): ").strip()
    end_s = input("Nhập bài hát kết thúc đoạn cắt (ví dụ E): ").strip()
    dest_s = input("Nhập bài hát đích để chèn sau (ví dụ G): ").strip()

    move_segment(playlist, start_s, end_s, dest_s)
    print("Playlist sau khi di chuyển:", " -> ".join(playlist.to_list()))


if __name__ == "__main__":
    main()
