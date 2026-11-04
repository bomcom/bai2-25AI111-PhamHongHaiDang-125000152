"""
BÀI TẬP 4: MÔ PHỎNG HÀNG CHỜ TỔNG ĐÀI CHĂM SÓC KHÁCH HÀNG (MỨC ĐỘ: DỄ - TRUNG BÌNH - QUEUE)
Phân phối cuộc gọi đến nhân viên theo quy luật FIFO.
"""

import sys
import time
from collections import deque
from dataclasses import dataclass

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


@dataclass
class Call:
    call_id: int
    caller_name: str
    arrival_time: float


class CallCenter:
    def __init__(self):
        self.call_queue = deque()
        self.call_id_counter = 1

    def receive_call(self, name: str):
        new_call = Call(self.call_id_counter, name, time.time())
        self.call_queue.append(new_call)
        print(f"Cuộc gọi #{self.call_id_counter} từ '{name}' đã vào hàng chờ.")
        self.call_id_counter += 1

    def answer_call(self):
        if not self.call_queue:
            print("Tổng đài đang rảnh, không có cuộc gọi chờ.")
            return
        call = self.call_queue.popleft()
        waited_seconds = round(time.time() - call.arrival_time, 2)
        print(f"-> Đang kết nối cuộc gọi #{call.call_id} ('{call.caller_name}'). Thời gian chờ: {waited_seconds}s.")

    def peek_longest_waiting(self):
        if not self.call_queue:
            print("Không có cuộc gọi nào trong hàng chờ.")
            return
        call = self.call_queue[0]
        waited_seconds = round(time.time() - call.arrival_time, 2)
        print(f"-> Người đang chờ lâu nhất: '{call.caller_name}' (#{call.call_id}), đã chờ {waited_seconds}s.")

    def show_queue(self):
        print(f"\nTổng số người đang chờ: {len(self.call_queue)}")
        for c in self.call_queue:
            waited = round(time.time() - c.arrival_time, 1)
            print(f"  - #{c.call_id}: {c.caller_name} (chờ {waited}s)")


def main():
    center = CallCenter()
    print("=== MÔ PHỎNG TỔNG ĐÀI HỖ TRỢ KHÁCH HÀNG ===")

    # Giả lập vài cuộc gọi mẫu
    center.receive_call("Nguyễn Văn A")
    center.receive_call("Trần Thị B")
    time.sleep(0.5)
    center.receive_call("Lê Văn C")

    while True:
        print("\n--- MENU TỔNG ĐÀI ---")
        print("1. Tiếp nhận cuộc gọi mới đến")
        print("2. Nhân viên nhấc máy hỗ trợ (Answer Call)")
        print("3. Xem người đang chờ lâu nhất (Peek)")
        print("4. Xem danh sách hàng chờ")
        print("5. Thoát")

        choice = input("Chọn: ").strip()
        if choice == "1":
            name = input("Nhập tên khách hàng gọi đến: ").strip()
            if name:
                center.receive_call(name)
        elif choice == "2":
            center.answer_call()
        elif choice == "3":
            center.peek_longest_waiting()
        elif choice == "4":
            center.show_queue()
        elif choice == "5":
            break
        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()
