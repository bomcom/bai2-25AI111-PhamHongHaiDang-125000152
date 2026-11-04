"""
BÀI TẬP 7: MÔ PHỎNG QUÁ TRÌNH TẢI TRANG WEB (WEB PAGE LOADING) (MỨC ĐỘ: KHÓ - QUEUE)
Trình duyệt dùng Queue để tải tuần tự các tài nguyên theo thứ tự FIFO.
"""

import sys
import time
from collections import deque
from dataclasses import dataclass

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


@dataclass
class Resource:
    name: str
    size: int  # tính bằng KB


def main():
    print("=== BÀI TẬP 7: MÔ PHỎNG TẢI TRANG WEB BẰNG QUEUE ===")
    loading_queue = deque()

    # Thêm tài nguyên cần tải
    loading_queue.append(Resource(name="style.css", size=150))
    loading_queue.append(Resource(name="logo.png", size=50))
    loading_queue.append(Resource(name="main.js", size=300))
    loading_queue.append(Resource(name="jquery.js", size=90))

    print("Bắt đầu tải tài nguyên trang web...")
    total_size = 0

    while len(loading_queue) > 0:
        current_resource = loading_queue.popleft()
        print(f" -> Đang tải {current_resource.name} ({current_resource.size}KB)...", end="", flush=True)

        # Giả lập thời gian tải (0.002 giây cho mỗi KB để chạy demo nhanh mượt)
        time.sleep(current_resource.size * 0.002)
        print(" [XONG!]")
        total_size += current_resource.size

    print(f"\n🎉 Tải trang hoàn tất! Tổng dung lượng: {total_size}KB.")


if __name__ == "__main__":
    main()
