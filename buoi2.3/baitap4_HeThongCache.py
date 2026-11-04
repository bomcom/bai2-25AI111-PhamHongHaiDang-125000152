"""
BÀI TẬP 4: MÔ PHỎNG HỆ THỐNG CACHE ĐƠN GIẢN (MỨC ĐỘ: KHÓ - DICT)
Ứng dụng dict làm bộ nhớ đệm (Cache) để giảm thiểu truy vấn tốn kém.
"""

import sys
import time

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Cache khai báo ở cấp module để tồn tại qua nhiều lần gọi hàm
_cache: dict[str, str] = {}


def get_data_from_database(query: str) -> str:
    """Giả lập hàm lấy dữ liệu chậm từ cơ sở dữ liệu."""
    print(f"... Đang truy vấn database cho '{query}' (mất 2s)...")
    time.sleep(2)  # Giả lập độ trễ truy vấn database
    return f"Dữ liệu kết quả của [{query}]"


def get_smart_data(query: str) -> str:
    """Hàm thông minh có tích hợp cơ chế Caching."""
    if query in _cache:
        print(f"⚡ [CACHE HIT] Tìm thấy trong Cache! Lấy ra ngay tức thì (0.00s).")
        return _cache[query]

    print(f"⏳ [CACHE MISS] Chưa có trong Cache. Bắt đầu lấy từ Database...")
    start_time = time.time()
    result = get_data_from_database(query)
    elapsed = time.time() - start_time

    # Lưu vào Cache cho các lần gọi sau
    _cache[query] = result
    print(f"-> Đã lưu vào Cache. Thời gian hoàn thành: {elapsed:.2f}s.")
    return result


def main():
    print("=== BÀI TẬP 4: MÔ PHỎNG HỆ THỐNG CACHE ĐƠN GIẢN ===")

    print("\n[Lần 1] Lấy danh sách Users:")
    print(get_smart_data("SELECT * FROM Users"))

    print("\n[Lần 2] Lấy danh sách Products:")
    print(get_smart_data("SELECT * FROM Products"))

    print("\n[Lần 3] Lấy lại danh sách Users (Quan sát tốc độ Cache Hit):")
    print(get_smart_data("SELECT * FROM Users"))

    print(f"\nTổng số query đang lưu trong Cache: {len(_cache)} mục.")


if __name__ == "__main__":
    main()
