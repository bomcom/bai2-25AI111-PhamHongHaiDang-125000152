# B. Bài tập tự giải
# Bài 1: Thao tác trên dãy số (List)
# Cho n số nguyên dương a0, a1, a2, ..., an-1. 
# Giải quyết các yêu cầu sau:
# 
# a. Chèn phần tử x vào vị trí k của dãy (có thể tái sử dụng code cũ).
# b. Xóa tất cả các số nguyên tố trong dãy (có thể tái sử dụng code cũ).
# c. Kiểm tra dãy có tăng dần hay không?
# d. Tìm số nhỏ nhất chia hết cho tất cả các số của dãy (BCNN của cả dãy).
# e. Tìm các cặp số nguyên tố cùng nhau (hai số nguyên dương được gọi là 
#    nguyên tố cùng nhau nếu ước số chung lớn nhất của chúng bằng 1).
# f. Tìm tần số xuất hiện của các số trong dãy.
# g.Đảo ngược thứ tự các phần tử trong dãy (tự viết thuật toán hoán đổi, không dùng reverse() hoặc a[::-1]).
# h.Tính tổng, trung bình cộng, tìm phần tử lớn nhất và nhỏ nhất của dãy (không dùng sum(), max(), min() có sẵn).



import math
import collections

def nhap_so(n):
    """Nhập n phần tử từ bàn phím vào danh sách a"""
    a = []
    for i in range(n):
        a.append(int(input(f"Nhập a[{i}] = ")))
    return a

def kiemtra_so_nguyen_to(x):
    """Kiểm tra xem 1 số nguyên x có phải là số nguyên tố hay không"""
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1): #duyệt từ 2 đến căn bậc hai của x để kiểm tra nếu x chia hết cho bất kỳ số nào trong khoảng này thì x không phải là số nguyên tố#      
        if x % i == 0: # nếu x chia hết cho i
            return False
    return True #nếu x không chia hết cho bất kỳ số nào trong khoảng này thì x là số nguyên tố

def sap_xep(a):
    """Sắp xếp dãy tăng dần mà không làm thay đổi dãy gốc"""
    return sorted(a)

def chen_phan_tu(a, x, k):
    """Chèn phần tử x vào vị trí k của danh sách"""
    a_copy = a.copy()
    a_copy.insert(k, x)
    return a_copy

def xoa_so_nguyen_to(a):
    """Xóa tất cả các số nguyên tố trong danh sách a"""
    return [x for x in a if not kiemtra_so_nguyen_to(x)]

def kiem_tra_day_tang_dan(a):
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False
    return True

def uoc_so_lon_nhat(a, b):
    """Tìm ước số chung lớn nhất (USCLN) của hai số a và b"""
    while b:
        a, b = b, a % b
    return a

def tim_bcnn(a, b):
    """Tìm bội số chung nhỏ nhất (BCNN) của hai số a và b"""
    abs_a = abs(a)
    abs_b = abs(b)
    if abs_a == 0 or abs_b == 0:
        return 0
    return abs_a * abs_b // uoc_so_lon_nhat(abs_a, abs_b)   

def tim_bcnn_cua_day(a):
    """Tìm BCNN của cả dãy"""
    if not a:
        return 0
    bcnn = a[0]
    for num in a[1:]:
        bcnn = tim_bcnn(bcnn, num)
    return bcnn

def tan_so_xuat_hien(a):
    """Tìm tần số xuất hiện của các số trong dãy"""
    return dict(collections.Counter(a))


 # câu g Đảo ngược thứ tự các phần tử trong dãy (tự viết thuật toán hoán đổi, không dùng reverse() hoặc a[::-1]).
# câu g Đảo ngược thứ tự các phần tử trong dãy (tự viết thuật toán hoán đổi, không dùng reverse() hoặc a[::-1]).
def dao_nguoc_day(a):
    a_copy = a.copy()
    left = 0
    right = len(a_copy) - 1
    while left < right:
        a_copy[left], a_copy[right] = a_copy[right], a_copy[left]
        left += 1
        right -= 1
    return a_copy

# câu h Tính tổng, trung bình cộng, tìm phần tử lớn nhất và nhỏ nhất của dãy (không dùng sum(), max(), min() có sẵn).
def thong_ke_day(a):
    if not a:
        return 0, 0, None, None
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

if __name__ == "__main__":
    # 1. Nhập và kiểm tra số lượng n hợp lệ (> 0)
    while True:
        try:
            n = int(input("Nhập n (số lượng phần tử > 0): "))
            if n <= 0:
                print("Vui lòng nhập số nguyên dương lớn hơn 0!")
                continue
            break
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ!")

    # 2. Nhập các phần tử của dãy
    a = nhap_so(n)
    print(f"\nDãy vừa nhập: {a}")


    # 4. Câu a: Chèn phần tử x vào vị trí k
    print("\n--- a. Chèn phần tử ---")
    try:
        x_chen = int(input("Nhập giá trị x cần chèn: "))
        k_chen = int(input(f"Nhập vị trí k cần chèn (0 đến {len(a)}): "))
        if 0 <= k_chen <= len(a):
            a_da_chen = chen_phan_tu(a, x_chen, k_chen)
            print(f"Dãy sau khi chèn {x_chen} vào vị trí {k_chen}: {a_da_chen}")
        else:
            print("Vị trí k không hợp lệ!")
    except ValueError:
        print("Dữ liệu nhập phải là số nguyên!")

    # 5. Câu b: Xóa tất cả các số nguyên tố
    print("\n--- b. Xóa các số nguyên tố ---")
    a_khong_snt = xoa_so_nguyen_to(a)
    print(f"Dãy sau khi xóa tất cả số nguyên tố: {a_khong_snt}")

    # 6. Câu c: Kiểm tra dãy có tăng dần hay không
    print("\n--- c. Kiểm tra dãy có tăng dần hay không ---")
    if kiem_tra_day_tang_dan(a):
        print("Dãy tăng dần.")
    else:
        print("Dãy không tăng dần.")    

    # 7. Câu d: Tìm BCNN của cả dãy
    print("\n--- d. Tìm BCNN của cả dãy ---")
    bcnn = tim_bcnn_cua_day(a)
    if bcnn == 0:
        print("Dãy có chứa số 0, không thể tìm BCNN.")
    else:
        print(f"BCNN của cả dãy là: {bcnn}")

    # 8. Câu e: Tìm các cặp số nguyên tố cùng nhau
    print("\n--- e. Tìm các cặp số nguyên tố cùng nhau ---")
    cap_so_nguyen_to_cung_nhau = []
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if uoc_so_lon_nhat(a[i], a[j]) == 1:
                cap_so_nguyen_to_cung_nhau.append((a[i], a[j]))
    if cap_so_nguyen_to_cung_nhau:
        print("Các cặp số nguyên tố cùng nhau:")
        for pair in cap_so_nguyen_to_cung_nhau:
            print(pair)
    else:
        print("Không có cặp số nguyên tố cùng nhau nào trong dãy.")

    # 9. Câu f: Tìm tần số xuất hiện của các số trong dãy
    print("\n--- f. Tìm tần số xuất hiện của các số trong dãy ---")
    tan_so = tan_so_xuat_hien(a)
    print("Tần số xuất hiện của các số trong dãy:")
    for num, freq in tan_so.items():
        print(f"Số {num}: {freq} lần")
    
    # 10. Câu g: Đảo ngược dãy
    print('\n--- g. Đảo ngược thứ tự các phần tử trong dãy ---')
    a_dao = dao_nguoc_day(a)
    print(f'Dãy sau khi đảo ngược: {a_dao}')

    # 11. Câu h: Thống kê dãy số (không dùng hàm có sẵn)
    print('\n--- h. Thống kê dãy số (không dùng hàm có sẵn) ---')
    tong, tbc, max_val, min_val = thong_ke_day(a)
    print(f'Tổng: {tong}')
    print(f'Trung bình cộng: {tbc:.2f}')
    print(f'Phần tử lớn nhất: {max_val}')
    print(f'Phần tử nhỏ nhất: {min_val}')
