"""
BÀI TẬP 5: SẮP XẾP LẠI PLAYLIST NHẠC - CẮT & NỐI CON TRỎ (MỨC ĐỘ: RẤT KHÓ)
Yêu cầu:
- Cho 1 playlist DoublyLinkedList ban đầu (A -> B -> C -> D -> E -> F -> G -> H)
- Cắt đoạn [start_song -> end_song]
- Chèn đoạn vừa cắt vào ngay sau destination_song
- Yêu cầu thao tác TRỰC TIẾP TRÊN CON TRỎ (next/prev), không sao chép mảng
"""


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
    # TODO:
    # 1. Tìm các nút start_node, end_node, dest_node
    # 2. Kiểm tra điều kiện hợp lệ (start xuất hiện trước end, dest không nằm trong [start -> end])
    # 3. Cắt rời đoạn [start_node -> end_node] ra khỏi danh sách
    # 4. Nối đoạn vừa cắt vào ngay sau dest_node
    pass


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
