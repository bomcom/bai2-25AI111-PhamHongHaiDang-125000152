def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a
 
 
def binary_search(a, x):
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
    n = int(input("Nhap n = "))
    a = []
    for i in range(n):
        x = int(input(f"a[{i}] = "))
        a.append(x)
    return a
 
 
def hien(a):
    print("\t".join(str(x) for x in a))
 
 
def main():
    a = nhap_day()
    bubble_sort(a)
    print("Day sau khi sap xep:")
    hien(a)
    x = int(input("Nhap gia tri can tim x = "))
    vt = binary_search(a, x)
    if vt != -1:
        print(f"Tim thay {x} tai vi tri {vt}")
    else:
        print(f"Khong tim thay {x} trong day")
 
 
if __name__ == "__main__":
    main()
