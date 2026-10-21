"""
BÀI TẬP 4: TRÒ CHƠI ĐẾM SỐ VÀ LOẠI NGƯỜI (JOSEPHUS PROBLEM) (MỨC ĐỘ: KHÓ)
Yêu cầu:
- Cho n người đứng thành vòng tròn (1 -> n)
- Đếm k bước, loại người thứ k
- Lặp lại cho đến khi chỉ còn 1 người duy nhất
- Triển khai bằng Circular Doubly LinkedList (Danh sách liên kết đôi trỏ vòng)
"""

import sys

# Đảm bảo in tiếng Việt có dấu chuẩn xác trên console Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.prev = None


def solve_josephus(n: int, k: int):
    # 1. Khởi tạo danh sách n người (từ 1 đến n) bằng vòng lặp while
    head = Node(1)
    current = head
    i = 2
    while i <= n:
        new_node = Node(i)
        current.next = new_node
        new_node.prev = current
        current = new_node
        i += 1

    # Nối nút cuối về nút đầu để tạo thành VÒNG TRÒN KHÉP KÍN
    current.next = head
    head.prev = current

    # 2. Vòng lặp đếm và loại người dùng duy nhất 1 vòng while (mô phỏng thực tế)
    current = head
    remaining = n
    step = 1

    print(f"\n--- BẮT ĐẦU VÒNG LOẠI (n = {n}, k = {k}) ---")
    while remaining > 1:
        if step == k:
            # Đã đếm tới k -> Người này bị loại!
            print(f"-> Loại người ở vị trí: {current.value}")

            # Ngắt người này ra khỏi vòng tròn:
            current.prev.next = current.next
            current.next.prev = current.prev

            # Giảm số người còn lại và đặt lại nhịp đếm về 1 cho lượt kế
            remaining -= 1
            step = 1
        else:
            # Chưa tới k -> Tăng bước đếm lên 1
            step += 1

        # Luôn luôn bước tiếp tới người kế tiếp trong vòng tròn
        current = current.next

    print(f"\n🎉 Người sống sót cuối cùng là người ở vị trí: {current.value}")
    return current.value


def main():
    print("=== TRÒ CHƠI ĐẾM SỐ JOSEPHUS ===")
    try:
        n = int(input("Nhập số người tham gia (n > 1): "))
        k = int(input("Nhập bước đếm loại bỏ (k >= 1): "))
        if n > 1 and k >= 1:
            solve_josephus(n, k)
        else:
            print("Giá trị n hoặc k không hợp lệ (cần n > 1 và k >= 1)!")
    except ValueError:
        print("Vui lòng nhập số nguyên!")


if __name__ == "__main__":
    main()
