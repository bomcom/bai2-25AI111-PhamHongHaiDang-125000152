"""
Bài 2 - Phần A (Code do AI sinh và tối ưu)
Thuật toán sắp xếp nổi bọt (Bubble Sort) và Tìm kiếm nhị phân (Binary Search)
Tối ưu hóa:
- Bubble Sort có cờ hiệu `swapped` giúp đạt O(n) khi mảng đã sắp xếp.
- Binary Search chuẩn xác, kiểm tra điều kiện mảng đã sắp xếp trước khi tìm.
"""


def bubble_sort_toi_uu(arr: list) -> list:
    """
    Sắp xếp nổi bọt tối ưu:
    Nếu trong một lượt duyệt không có cặp nào bị hoán đổi,
    mảng đã sắp xếp xong -> dừng sớm (O(n)).
    """
    a = arr.copy()
    n = len(a)
    for i in range(n - 1):
        da_hoan_doi = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                da_hoan_doi = True
        # Nếu lượt này không có hoán đổi nào -> mảng đã xếp xong
        if not da_hoan_doi:
            break
    return a


def binary_search(a: list, x: int) -> int:
    """
    Tìm kiếm nhị phân trên dãy đã sắp xếp tăng dần.
    Trả về chỉ số vị trí tìm thấy (0-indexed), hoặc -1 nếu không tìm thấy.
    Độ phức tạp: O(log n).
    """
    left, right = 0, len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def nhap_day():
    n = int(input("Nhập số phần tử n = "))
    a = []
    for i in range(n):
        x = int(input(f"a[{i}] = "))
        a.append(x)
    return a


def main():
    print("=== BÀI 2: BUBBLE SORT & BINARY SEARCH (AI CODE) ===")
    a = nhap_day()
    print(f"\nDãy ban đầu: {a}")

    a_sap_xep = bubble_sort_toi_uu(a)
    print(f"Dãy sau khi sắp xếp tăng dần (Bubble sort): {a_sap_xep}")

    x = int(input("\nNhập giá trị x cần tìm kiếm (Binary Search): "))
    vt = binary_search(a_sap_xep, x)
    if vt != -1:
        print(f"-> Tìm thấy giá trị {x} tại vị trí chỉ số {vt} trong dãy đã sắp xếp.")
    else:
        print(f"-> Không tìm thấy giá trị {x} trong dãy.")


if __name__ == "__main__":
    main()
