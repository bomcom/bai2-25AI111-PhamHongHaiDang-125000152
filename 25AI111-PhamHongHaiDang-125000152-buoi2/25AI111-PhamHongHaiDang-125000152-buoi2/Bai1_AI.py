"""
BÀI THỰC HÀNH ÔN TẬP KỸ THUẬT LẬP TRÌNH - PHẦN B: BÀI 1 (AI Solution)
Đề bài: Thao tác trên dãy số nguyên dương (List)
Các yêu cầu:
    a. Chèn phần tử x vào vị trí k của dãy.
    b. Xóa tất cả các số nguyên tố trong dãy.
    c. Kiểm tra dãy có tăng dần hay không?
    d. Tìm BCNN của cả dãy (số nhỏ nhất chia hết cho tất cả các số trong dãy).
    e. Tìm các cặp số nguyên tố cùng nhau (ước chung lớn nhất = 1).
    f. Tìm tần số xuất hiện của các số trong dãy.
"""

from math import gcd
from collections import Counter

def nhap_day_so() -> list[int]:
    while True:
        try:
            n = int(input("Nhập số lượng phần tử n (n > 0): "))
            if n <= 0:
                print("Lỗi: n > 0. Vui lòng nhập lại!")
                continue
            break
        except ValueError:
            print("Lỗi: Vui lòng nhập số nguyên hợp lệ!")

    a = []
    print(f"\n--- Nhập {n} số nguyên dương ---")
    for i in range(n):
        while True:
            try:
                val = int(input(f"a[{i}] = "))
                if val <= 0:
                    print("Cảnh báo: Đề bài yêu cầu số nguyên dương (> 0).")
                    continue
                a.append(val)
                break
            except ValueError:
                print("Lỗi: Giá trị nhập phải là số nguyên!")
    return a

def hien_thi_day(a: list[int], tieu_de: str = "Dãy số:") -> None:
    print(f"{tieu_de}: [{' '.join(map(str, a))}]")

# a. Chèn phần tử x vào vị trí k
def chen_phan_tu(a: list[int], x: int, k: int) -> list[int]:
    res = a.copy()
    if 0 <= k <= len(res):
        res.insert(k, x)
    return res

# b. Xóa số nguyên tố
def la_so_nguyen_to(x: int) -> bool:
    if x < 2: return False
    if x in (2, 3): return True
    if x % 2 == 0 or x % 3 == 0: return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True

def xoa_so_nguyen_to(a: list[int]) -> list[int]:
    return [x for x in a if not la_so_nguyen_to(x)]

# c. Kiểm tra dãy tăng dần
def kiem_tra_tang_dan(a: list[int]) -> bool:
    if len(a) <= 1: return True
    return all(a[i] < a[i + 1] for i in range(len(a) - 1))

# d. Tìm BCNN của cả dãy
def bcnn_ca_day(a: list[int]) -> int:
    if not a: return 0
    res = a[0]
    for x in a[1:]:
        res = (res * x) // gcd(res, x)
    return res

# e. Tìm các cặp số nguyên tố cùng nhau (gcd = 1)
def tim_cap_nguyen_to_cung_nhau(a: list[int]) -> list[tuple[int, int]]:
    ds_cap = []
    n = len(a)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if gcd(a[i], a[j]) == 1:
                ds_cap.append((a[i], a[j]))
    return ds_cap

# f. Tìm tần số xuất hiện
def tan_so_xuat_hien(a: list[int]) -> dict[int, int]:
    return dict(Counter(a))

def main():
    a = nhap_day_so()
    hien_thi_day(a, "Dãy số vừa nhập")

    print(f"\n[Câu c] Dãy tăng dần: {kiem_tra_tang_dan(a)}")
    print(f"[Câu d] BCNN cả dãy: {bcnn_ca_day(a)}")
    
    cap = tim_cap_nguyen_to_cung_nhau(a)
    print(f"[Câu e] Cặp số NT cùng nhau: {cap if cap else 'Không có'}")
    
    print(f"[Câu f] Tần số xuất hiện: {tan_so_xuat_hien(a)}")

if __name__ == "__main__":
    main()

