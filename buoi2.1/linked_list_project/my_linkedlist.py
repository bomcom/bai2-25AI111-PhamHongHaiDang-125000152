"""
MODULE: my_linkedlist
Mô tả: Tự cài đặt Doubly Linked List (Danh sách liên kết đôi)
chuẩn hoá với Type Hinting và Dunder Methods.
"""

from typing import Any, Optional, Iterator


class Node:
    """Đại diện cho một nút (Node) trong Danh sách liên kết đôi."""

    def __init__(self, data: Any):
        self.data: Any = data
        self.prev: Optional['Node'] = None
        self.next: Optional['Node'] = None

    def __repr__(self) -> str:
        return f"Node({self.data})"


class DoublyLinkedList:
    """Danh sách liên kết đôi hỗ trợ quản lý nút đầu (head) và đuôi (tail)."""

    def __init__(self, iterable=None):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size: int = 0
        if iterable is not None:
            for item in iterable:
                self.add_last(item)

    # ================= CÁC DUNDER METHODS HỖ TRỢ PYTHON =================
    def __len__(self) -> int:
        """Cho phép dùng hàm len(danh_sach) với O(1)."""
        # TODO: Trả về số lượng phần tử
        return self._size

    def __bool__(self) -> bool:
        """Kiểm tra if danh_sach: có rỗng hay không."""
        # TODO: Trả về True nếu danh sách có phần tử
        return self._size > 0

    def __iter__(self) -> Iterator[Any]:
        """Cho phép duyệt for item in danh_sach:"""
        # TODO: Dùng yield duyệt từ head đến tail
        curr = self.head
        while curr:
            yield curr.data
            curr = curr.next

    def __repr__(self) -> str:
        """Hiển thị dạng: A <-> B <-> C"""
        nodes = [str(x) for x in self]
        return " <-> ".join(nodes) if nodes else "Empty LinkedList"

    # ================= CÁC THAO TÁC CƠ BẢN =================
    @property
    def first(self) -> Optional[Node]:
        """Lấy nút đầu tiên (O(1))."""
        return self.head

    @property
    def last(self) -> Optional[Node]:
        """Lấy nút cuối cùng (O(1))."""
        return self.tail

    def add_first(self, data: Any) -> Node:
        """Thêm một phần tử vào đầu danh sách (O(1))."""
        # TODO: Viết code thêm vào đầu danh sách
        pass

    def add_last(self, data: Any) -> Node:
        """Thêm một phần tử vào cuối danh sách (O(1))."""
        # TODO: Viết code thêm vào cuối danh sách
        pass

    def add_after(self, node: Node, data: Any) -> Node:
        """Chèn một giá trị ngay sau nút được chỉ định (O(1))."""
        # TODO: Viết code chèn sau node
        pass

    def remove_first(self) -> Any:
        """Xóa phần tử đầu danh sách và trả về giá trị (O(1))."""
        # TODO: Viết code xóa nút đầu tiên
        pass

    def remove_last(self) -> Any:
        """Xóa phần tử cuối danh sách và trả về giá trị (O(1))."""
        # TODO: Viết code xóa nút cuối cùng
        pass

    def remove(self, node: Node) -> None:
        """Xóa trực tiếp một Node ra khỏi danh sách (O(1))."""
        # TODO: Viết code xóa nút bất kỳ
        pass

    def find(self, data: Any) -> Optional[Node]:
        """Tìm và trả về Node đầu tiên chứa giá trị data (O(n))."""
        # TODO: Viết code duyệt tìm nút có data
        pass

    def clear(self) -> None:
        """Xóa toàn bộ danh sách."""
        self.head = None
        self.tail = None
        self._size = 0
