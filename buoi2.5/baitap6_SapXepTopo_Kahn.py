"""
BÀI TẬP 6: SẮP XẾP TÔ-PÔ (TOPOLOGICAL SORT) – XẾP LỊCH HỌC (MỨC ĐỘ: TRUNG BÌNH - KHÓ)
Thuật toán Kahn dựa trên Bán bậc vào (In-degree) và Hàng đợi (Queue).
"""

import sys
from collections import deque

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def topological_sort(graph: dict):
    """Sắp xếp tô-pô bằng thuật toán Kahn. Trả về danh sách thứ tự hoặc None nếu có chu trình."""
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] = in_degree.get(v, 0) + 1

    queue = deque([u for u in graph if in_degree[u] == 0])
    order = []

    while queue:
        u = queue.popleft()
        order.append(u)
        for v in graph.get(u, []):
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    return order if len(order) == len(graph) else None


def is_valid_order(graph: dict, order: list) -> bool:
    """Kiểm tra thứ tự sắp xếp có thỏa mãn mọi quan hệ tiên quyết u -> v không."""
    if not order:
        return False
    position = {u: i for i, u in enumerate(order)}
    return all(position[u] < position[v] for u in graph for v in graph[u])


def main():
    print("=== BÀI TẬP 6: SẮP XẾP TÔ-PÔ (XẾP LỊCH HỌC) ===")
    courses = {
        "Lap trinh co ban": ["CTDL", "Co so du lieu"],
        "Toan roi rac": ["CTDL", "Do thi"],
        "CTDL": ["Giai thuat", "Do thi"],
        "Co so du lieu": ["Phan mem ung dung"],
        "Giai thuat": ["Phan mem ung dung"],
        "Do thi": [],
        "Phan mem ung dung": []
    }

    order = topological_sort(courses)
    print("Thứ tự học các môn hợp lệ:")
    print(" -> ".join(order))
    print(f"Kiểm tra tính hợp lệ: {is_valid_order(courses, order)}")

    # Tạo vòng lặp tiên quyết: Phần mềm ứng dụng -> Lập trình cơ bản
    courses["Phan mem ung dung"].append("Lap trinh co ban")
    res_cycle = topological_sort(courses)
    print(f"\nSau khi thêm ràng buộc vòng lặp: {res_cycle} (Phát hiện chu trình, không thể xếp lịch!)")


if __name__ == "__main__":
    main()
