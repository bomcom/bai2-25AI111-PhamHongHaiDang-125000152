"""
Bài 1 - Phần B (Code do AI sinh và tối ưu)
Các thuật toán và thao tác trên List:
a. Chèn phần tử x vào vị trí k
b. Xóa các số nguyên tố
c. Kiểm tra dãy tăng dần
d. Tìm BCNN của cả dãy
e. Tìm các cặp số nguyên tố cùng nhau
f. Tìm tần số xuất hiện của các số
g. Đảo ngược dãy (thuật toán 2 con trỏ Two Pointers)
h. Tính tổng, TBC, Max, Min không dùng hàm dựng sẵn
"""

import math
from collections import Counter


def nhap_day():
    """Nhập danh sách n số nguyên dương từ bàn phím với kiểm tra hợp lệ"""
    while True:
        try:
            n = int(input("Nhập số lượng phần tử n (> 0): "))
            if n <= 0:
                print("Vui lòng nhập số nguyên dương lớn hơn 0!")
                continue
            break
        except ValueError:
            print("Giá trị không hợp lệ! Vui lòng nhập số nguyên.")

    a = []
    for i in range(n):
        while True:
            try:
                x = int(input(f"Nhập a[{i}] = "))
                a.append(x)
                break
            except ValueError:
                print("Giá trị phần tử phải là số nguyên!")
    return a


def chen_phan_tu(a: list, x: int, k: int) -> list:
    """Câu a: Chèn x vào vị trí k, trả về list mới không làm thay đổi list gốc"""
    if 0 <= k <= len(a):
        res = a.copy()
        res.insert(k, x)
        return res
    print("Vị trí k nằm ngoài phạm vi cho phép!")
    return a.copy()


def la_so_nguyen_to(n: int) -> bool:
    """Kiểm tra số nguyên tố tối ưu O(sqrt(n))"""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def xoa_so_nguyen_to(a: list) -> list:
    """Câu b: Lọc bỏ tất cả số nguyên tố bằng list comprehension"""
    return [x for x in a if not la_so_nguyen_to(x)]


def kiem_tra_tang_dan(a: list) -> bool:
    """Câu c: Kiểm tra dãy có tăng ngặt hay không bằng all() generator"""
    return all(a[i] < a[i + 1] for i in range(len(a) - 1))


def bcnn_hai_so(x: int, y: int) -> int:
    """Tính BCNN của 2 số qua UCLN: lcm(x, y) = |x * y| // gcd(x, y)"""
    if x == 0 or y == 0:
        return 0
    return abs(x * y) // math.gcd(x, y)


def bcnn_cua_day(a: list) -> int:
    """Câu d: Tìm BCNN của cả dãy"""
    if not a or 0 in a:
        return 0
    res = a[0]
    for num in a[1:]:
        res = bcnn_hai_so(res, num)
    return res


def tim_cap_nguyen_to_cung_nhau(a: list) -> list[tuple[int, int]]:
    """Câu e: Tìm tất cả cặp (a[i], a[j]) có gcd == 1"""
    res = []
    n = len(a)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if math.gcd(a[i], a[j]) == 1:
                res.append((a[i], a[j]))
    return res


def tan_so_xuat_hien(a: list) -> dict[int, int]:
    """Câu f: Đếm tần số xuất hiện bằng collections.Counter"""
    return dict(Counter(a))


def dao_nguoc_day(a: list) -> list:
    """Câu g: Đảo ngược mảng bằng kỹ thuật 2 con trỏ Two Pointers"""
    res = a.copy()
    left, right = 0, len(res) - 1
    while left < right:
        res[left], res[right] = res[right], res[left]
        left += 1
        right -= 1
    return res


def thong_ke_day(a: list) -> tuple[int, float, int, int]:
    """Câu h: Duyệt 1 vòng (Single-pass) tính Tổng, TBC, Max, Min không dùng hàm có sẵn"""
    if not a:
        return 0, 0.0, 0, 0
    tong = 0
    lon_nhat = a[0]
    nho_nhat = a[0]
    for x in a:
        tong += x
        if x > lon_nhat:
            lon_nhat = x
        if x < nho_nhat:
            nho_nhat = x
    tbc = tong / len(a)
    return tong, tbc, lon_nhat, nho_nhat


def main():
    print("=== CHƯƠNG TRÌNH THAO TÁC TRÊN LIST (AI OPTIMIZED) ===")
    a = nhap_day()
    print(f"\nDãy ban đầu: {a}")

    # Câu a
    print("\n[a] Chèn phần tử:")
    try:
        x_val = int(input("  Nhập giá trị cần chèn x: "))
        k_pos = int(input(f"  Nhập vị trí cần chèn k (0 -> {len(a)}): "))
        print(f"  -> Dãy sau khi chèn: {chen_phan_tu(a, x_val, k_pos)}")
    except ValueError:
        print("  Dữ liệu không hợp lệ!")

    # Câu b
    print(f"\n[b] Dãy sau khi xóa số nguyên tố: {xoa_so_nguyen_to(a)}")

    # Câu c
    tang_dan = kiem_tra_tang_dan(a)
    print(f"\n[c] Kiểm tra dãy tăng dần: {'Dãy tăng dần' if tang_dan else 'Dãy KHÔNG tăng dần'}")

    # Câu d
    print(f"\n[d] BCNN của cả dãy: {bcnn_cua_day(a)}")

    # Câu e
    caps = tim_cap_nguyen_to_cung_nhau(a)
    print(f"\n[e] Các cặp số nguyên tố cùng nhau ({len(caps)} cặp):")
    if caps:
        print("     " + ", ".join(f"({x}, {y})" for x, y in caps))
    else:
        print("     Không có cặp nào.")

    # Câu f
    print(f"\n[f] Tần số xuất hiện của các phần tử:")
    for num, count in tan_so_xuat_hien(a).items():
        print(f"     Giá trị {num}: {count} lần")

    # Câu g
    print(f"\n[g] Dãy sau khi đảo ngược (Two Pointers): {dao_nguoc_day(a)}")

    # Câu h
    tong, tbc, max_val, min_val = thong_ke_day(a)
    print(f"\n[h] Thống kê thủ công (Single pass):")
    print(f"     - Tổng: {tong}")
    print(f"     - Trung bình cộng: {tbc:.2f}")
    print(f"     - Lớn nhất (Max): {max_val}")
    print(f"     - Nhỏ nhất (Min): {min_val}")


if __name__ == "__main__":
    main()
