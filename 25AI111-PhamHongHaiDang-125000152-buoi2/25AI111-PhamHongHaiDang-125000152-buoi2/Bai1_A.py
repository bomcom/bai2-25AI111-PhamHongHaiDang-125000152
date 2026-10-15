# Cho n số nguyên dương a0, a1, a2, ..., an-1.
# a. Chèn phần tử x vào vị trí k của dãy.
# b. Xóa tất cả các số nguyên tố trong dãy.

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
    for i in range(2, int(x**0.5) + 1): #duyệt từ 2 đến căn bậc hai của x để kiểm tra nếu x chia hết cho bất kỳ số nào trong khoảng này thì x không phải là số nguyên tố        
        if x % i == 0: # nếu x chia hết cho i
            return False
    return True #nếu x không chia hết cho bất kỳ số nào trong khoảng này thì x là số nguyên tố

def sap_xep(a):
    """Sắp xếp dãy tăng dần mà không làm thay đổi dãy gốc"""
    return sorted(a)

def tim_min_max(a):
    """Tìm giá trị nhỏ nhất và lớn nhất trong dãy"""
    return min(a), max(a)

def chen_phan_tu(a, x, k):
    """Chèn phần tử x vào vị trí k của danh sách"""
    a_copy = a.copy()
    a_copy.insert(k, x)
    return a_copy

def xoa_so_nguyen_to(a):
    """Xóa tất cả các số nguyên tố trong danh sách a"""
    return [x for x in a if not kiemtra_so_nguyen_to(x)]

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

    # 3. Sắp xếp và tìm Min / Max
    print(f"Dãy sau khi sắp xếp: {sap_xep(a)}")
    min_val, max_val = tim_min_max(a)
    print(f"Giá trị nhỏ nhất: {min_val}, Giá trị lớn nhất: {max_val}")

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
