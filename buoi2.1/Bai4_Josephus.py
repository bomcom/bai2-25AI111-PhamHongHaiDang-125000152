"""
BÀI TẬP 4: TRÒ CHƠI ĐẾM SỐ VÀ LOẠI NGƯỜI (JOSEPHUS PROBLEM) (MỨC ĐỘ: KHÓ)
Yêu cầu:
- Cho n người đứng thành vòng tròn (1 -> n)
- Đếm k bước, loại người thứ k
- Lặp lại cho đến khi chỉ còn 1 người duy nhất
- Triển khai bằng Circular Doubly LinkedList (Danh sách liên kết đôi trỏ vòng)
"""


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.prev = None


def solve_josephus(n: int, k: int):
    # TODO:
    # 1. Khởi tạo danh sách n nút (1 đến n)
    # 2. Nối vòng tròn: nút cuối trỏ về nút đầu (tail.next = head, head.prev = tail)
    # 3. Vòng lặp while remaining > 1:
    #    - Di chuyển k - 1 bước: for _ in range(k - 1): current = current.next
    #    - Ngắt nút cần xóa khỏi vòng tròn:
    #         current.prev.next = current.next
    #         current.next.prev = current.prev
    #    - current = current.next
    #    - Giảm số lượng remaining -= 1
    # 4. In ra người sống sót cuối cùng
    pass


def main():
    print("=== TRÒ CHƠI ĐẾM SỐ JOSEPHUS ===")
    try:
        n = int(input("Nhập số người tham gia (n > 1): "))
        k = int(input("Nhập bước đếm loại bỏ (k >= 1): "))
        if n > 1 and k >= 1:
            solve_josephus(n, k)
        else:
            print("Giá trị n hoặc k không hợp lệ!")
    except ValueError:
        print("Vui lòng nhập số nguyên!")


if __name__ == "__main__":
    main()
