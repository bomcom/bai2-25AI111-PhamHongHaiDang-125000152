BÀI THỰC HÀNH: ÔN TẬP LIST, DATACLASS VÀ FILE  TRONG PYTHON

Thời lượng: 120 phút — Các thao tác cơ bản và thuật toán trên mảng một chiều (List)

Mục tiêu

Củng cố kiến thức về kiểu dữ liệu List trong Python: cách khai báo, khởi tạo, duyệt và truy xuất phần tử.

Thực hành các thao tác thêm, chèn, xóa phần tử trong List.

Rèn luyện các thuật toán cơ bản trên mảng một chiều: sắp xếp, tìm kiếm, đếm, thống kê (tổng, trung bình, lớn nhất, nhỏ nhất).

Biết cách dùng công cụ AI để hỗ trợ sinh code và tối ưu hóa, đồng thời rèn khả năng tự đánh giá code.

Phân bổ thời gian (120 phút)

Thời gian

Nội dung

Hình thức

0 – 10 phút

Ôn tập nhanh lý thuyết: khai báo List, các phương thức thường dùng (append, insert, remove, sort, index...)

Giảng viên hướng dẫn

10 – 35 phút

Phần A – Bài 1: Chạy thử code mẫu chèn phần tử và xóa số nguyên tố trong List

Cá nhân / cặp đôi

35 – 60 phút

Phần A – Bài 2: Chạy thử code mẫu sắp xếp (bubble sort) và tìm kiếm nhị phân (binary search)

Cá nhân / cặp đôi

60 – 85 phút

Phần B: Tự viết code giải các bài tập tự giải, sau đó dùng AI sinh code để so sánh

Cá nhân

85 – 110 phút

Phần B: Tự viết code giải các bài tập tự giải, sau đó dùng AI sinh code để so sánh

Cá nhân

110 – 120 phút

Tổng kết, nhận xét, giải đáp thắc mắc

Cả lớp

Yêu cầu chung

1. Đối với phần A (bài tập mẫu):

Chạy thử code giải mẫu bằng Python: giải thích các hàm, kiểm tra lỗi (nếu có) và tính năng có đáp ứng yêu cầu đề bài không?

Sử dụng một công cụ AI (ChatGPT, Claude, Gemini...) để tối ưu hóa code giải mẫu.

2. Đối với phần B (bài tập tự giải):

Tự viết code Python giải quyết bài toán.

Sử dụng một vài công cụ AI để sinh code.

Đánh giá kết quả code sinh ra từ các công cụ AI và chọn cái tốt nhất theo quan điểm của bạn.

A. Bài tập mẫu

Bài 1: Chèn và xóa phần tử trong List

Cho n số nguyên dương a0, a1, a2, ..., an-1.

Chèn phần tử x vào vị trí k của dãy.

Xóa tất cả các số nguyên tố trong dãy.

Gợi ý:

Trong Python, List đã hỗ trợ sẵn hàm insert(k, x) để chèn phần tử vào vị trí k mà không cần tạo mảng trung gian như trong C#.

Để xóa các số nguyên tố, ta duyệt qua từng phần tử, kiểm tra xem có phải số nguyên tố hay không (số nguyên tố là số chỉ chia hết cho 1 và chính nó), rồi xây dựng danh sách mới chỉ gồm các phần tử không phải số nguyên tố (dùng list comprehension).

Lời giải mẫu:

def nhap_day():    n = int(input("Nhap n = "))    a = []    for i in range(n):        x = int(input(f"a[{i}] = "))        a.append(x)    return a  def chen(a, x, k):    if 0 <= k <= len(a):        a.insert(k, x)    else:        print("Du lieu khong hop le")  def la_nguyen_to(x):    if x < 2:        return False    for i in range(2, x):        if x % i == 0:            return False    return True  def xoa_nguyen_to(a):    return [x for x in a if not la_nguyen_to(x)]  def hien(a):    print("\t".join(str(x) for x in a))  def main():    a = nhap_day()    chen(a, 333, 1)    hien(a)    a = xoa_nguyen_to(a)    hien(a)  if __name__ == "__main__":    main()

Bài 2: Sắp xếp và tìm kiếm trên List

Cho n số nguyên dương a0, a1, a2, ..., an-1.

Sắp xếp dãy theo thứ tự tăng dần bằng thuật toán sắp xếp nổi bọt (bubble sort), tự viết thuật toán, không dùng hàm sort() có sẵn.

Tìm kiếm một giá trị x trong dãy đã sắp xếp bằng thuật toán tìm kiếm nhị phân (binary search).

Gợi ý:

Bubble sort: duyệt qua dãy nhiều lượt, ở mỗi lượt so sánh hai phần tử liền kề a[j] và a[j+1]; nếu a[j] > a[j+1] thì hoán đổi vị trí hai phần tử. Sau mỗi lượt duyệt, phần tử lớn nhất trong đoạn chưa sắp xếp sẽ được đẩy về cuối dãy.

Binary search: chỉ áp dụng được trên dãy đã sắp xếp tăng dần. Dùng hai biến left, right đánh dấu đoạn tìm kiếm hiện tại; tại mỗi bước tính mid = (left + right) // 2 và so sánh a[mid] với x để thu hẹp dần đoạn tìm kiếm.

Lời giải mẫu:

def bubble_sort(a):    n = len(a)    for i in range(n - 1):        for j in range(n - 1 - i):            if a[j] > a[j + 1]:                a[j], a[j + 1] = a[j + 1], a[j]    return a  def binary_search(a, x):    left, right = 0, len(a) - 1    while left <= right:        mid = (left + right) // 2        if a[mid] == x:            return mid        elif a[mid] < x:            left = mid + 1        else:            right = mid - 1    return -1  def nhap_day():    n = int(input("Nhap n = "))    a = []    for i in range(n):        x = int(input(f"a[{i}] = "))        a.append(x)    return a  def hien(a):    print("\t".join(str(x) for x in a))  def main():    a = nhap_day()    bubble_sort(a)    print("Day sau khi sap xep:")    hien(a)    x = int(input("Nhap gia tri can tim x = "))    vt = binary_search(a, x)    if vt != -1:        print(f"Tim thay {x} tai vi tri {vt}")    else:        print(f"Khong tim thay {x} trong day")  if __name__ == "__main__":    main()

B. Bài tập tự giải

Cho n số nguyên dương a0, a1, a2, ..., an-1. Hãy tự viết code Python (không dùng AI ở lần thử đầu) để giải quyết các yêu cầu sau, sau đó dùng công cụ AI để sinh code cho cùng yêu cầu và so sánh:

Chèn phần tử x vào vị trí k của dãy (đã làm ở bài mẫu, có thể tái sử dụng).

Xóa tất cả các số nguyên tố trong dãy (đã làm ở bài mẫu, có thể tái sử dụng).

Kiểm tra dãy có tăng dần hay không?

Tìm số nhỏ nhất chia hết cho tất cả các số của dãy (BCNN của cả dãy).

Tìm các cặp số nguyên tố cùng nhau (hai số nguyên dương được gọi là nguyên tố cùng nhau nếu ước số chung lớn nhất của chúng bằng 1).

Tìm tần số xuất hiện của các số trong dãy.

Đảo ngược thứ tự các phần tử trong dãy (tự viết thuật toán hoán đổi, không dùng reverse() hoặc a[::-1]).

Tính tổng, trung bình cộng, tìm phần tử lớn nhất và nhỏ nhất của dãy (không dùng sum(), max(), min() có sẵn).

Gợi ý:

Câu c: Duyệt qua các phần tử a[i] với i từ 0 → n-2, so sánh a[i] với a[i+1]. Nếu có một cặp a[i] >= a[i+1] thì dãy không tăng dần. Có thể viết ngắn gọn bằng: all(a[i] < a[i+1] for i in range(len(a)-1)).

Câu d: Xây dựng hàm bcnn(x, y) dựa trên module math có sẵn: from math import gcd, rồi bcnn = x * y // gcd(x, y). Sau đó khởi tạo bc = 1 và lần lượt tính BCNN của bc với từng phần tử trong dãy.

Câu e: Dùng math.gcd(a[i], a[j]) để tính ước chung lớn nhất của từng cặp phần tử (i từ 0 → n-2, j từ i+1 → n-1). Nếu gcd bằng 1 thì in ra cặp (a[i], a[j]).

Câu f: Có thể tự đếm bằng hai list song song (b chứa giá trị không trùng, c chứa tần số tương ứng) như hướng dẫn gốc, hoặc dùng collections.Counter để đếm tần số một cách ngắn gọn hơn.

Câu g: Dùng hai chỉ số dau = 0 và cuoi = n - 1, hoán đổi a[dau] với a[cuoi] rồi tăng dau, giảm cuoi, lặp lại cho đến khi dau >= cuoi.

Câu h: Khởi tạo tong = 0, lon_nhat = a[0], nho_nhat = a[0], sau đó duyệt qua từng phần tử: cộng dồn vào tong, so sánh và cập nhật lon_nhat/nho_nhat nếu cần. Trung bình cộng = tong / n.

C. Bài tập nâng cao: Kết hợp List, Dataclass và File

Một kho hàng lưu trữ thông tin các sản phẩm trong một file văn bản tên "sanpham.txt", mỗi dòng trong file lưu thông tin một sản phẩm theo định dạng: ma_sp,ten_sp,so_luong,don_gia (các trường cách nhau bởi dấu phẩy). Ví dụ nội dung file:

SP001,Ban phim,50,150000SP002,Chuot khong day,120,90000SP003,Man hinh 24 inch,15,2500000

Hãy viết chương trình Python thực hiện các yêu cầu sau, trong đó mỗi sản phẩm được biểu diễn bằng một dataclass SanPham và toàn bộ kho hàng được lưu trong một List các đối tượng SanPham:

Đọc dữ liệu từ file "sanpham.txt", tạo danh sách các đối tượng SanPham tương ứng.

Cho phép người dùng nhập thông tin một sản phẩm mới và thêm vào cuối danh sách.

Tính tổng giá trị tồn kho của toàn bộ kho hàng (giá trị tồn kho của một sản phẩm = số lượng × đơn giá).

Tìm và in ra sản phẩm có giá trị tồn kho lớn nhất.

Ghi lại toàn bộ danh sách sản phẩm (đã bao gồm sản phẩm vừa thêm) xuống một file mới tên "sanpham_moi.txt", giữ nguyên định dạng như file đầu vào.

Gợi ý:

Khai báo @dataclass SanPham gồm các trường ma_sp, ten_sp, so_luong, don_gia; có thể thêm một phương thức gia_tri_ton(self) trả về so_luong * don_gia.

Dùng with open(duong_dan, "r", encoding="utf-8") as f: rồi duyệt for dong in f: để đọc từng dòng; dùng dong.strip().split(",") để tách các trường, nhớ ép kiểu int/float cho so_luong và don_gia.

Dùng ds.append(SanPham(...)) để thêm sản phẩm mới vào List, giống cách thêm phần tử đã học ở các bài trước.

Dùng sum(sp.gia_tri_ton() for sp in ds) để tính tổng giá trị tồn kho, và max(ds, key=lambda sp: sp.gia_tri_ton()) để tìm sản phẩm có giá trị tồn kho lớn nhất.

Khi ghi file, dùng with open(duong_dan, "w", encoding="utf-8") as f: rồi f.write(f"{sp.ma_sp},{sp.ten_sp},{sp.so_luong},{sp.don_gia}\n") cho từng sản phẩm trong danh sách.

Lời giải mẫu (tham khảo sau khi đã tự làm):

from dataclasses import dataclass  @dataclassclass SanPham:    ma_sp: str    ten_sp: str    so_luong: int    don_gia: float     def gia_tri_ton(self):        return self.so_luong * self.don_gia  def doc_tu_file(duong_dan):    ds = []    with open(duong_dan, "r", encoding="utf-8") as f:        for dong in f:            dong = dong.strip()            if not dong:                continue            ma_sp, ten_sp, so_luong, don_gia = dong.split(",")            ds.append(SanPham(ma_sp, ten_sp, int(so_luong), float(don_gia)))    return ds  def them_san_pham(ds):    ma_sp = input("Ma san pham: ")    ten_sp = input("Ten san pham: ")    so_luong = int(input("So luong: "))    don_gia = float(input("Don gia: "))    ds.append(SanPham(ma_sp, ten_sp, so_luong, don_gia))  def tong_gia_tri_kho(ds):    return sum(sp.gia_tri_ton() for sp in ds)  def san_pham_gia_tri_lon_nhat(ds):    if not ds:        return None    return max(ds, key=lambda sp: sp.gia_tri_ton())  def ghi_ra_file(duong_dan, ds):    with open(duong_dan, "w", encoding="utf-8") as f:        for sp in ds:            f.write(f"{sp.ma_sp},{sp.ten_sp},{sp.so_luong},{sp.don_gia}\n")  def main():    ds = doc_tu_file("sanpham.txt")    them_san_pham(ds)    print("Tong gia tri kho hang:", tong_gia_tri_kho(ds))    sp_max = san_pham_gia_tri_lon_nhat(ds)    if sp_max:        print(f"San pham co gia tri ton kho lon nhat: {sp_max.ma_sp} - {sp_max.ten_sp}")    ghi_ra_file("sanpham_moi.txt", ds)  if __name__ == "__main__":    main()

Lưu ý: đây là bài tập nâng cao phù hợp để làm thêm ở nhà hoặc cho sinh viên muốn tìm hiểu cách kết hợp List, Dataclass và thao tác đọc/ghi File trong Python.

D. Bài tập tổng hợp nâng cao: Quản lý thư viện

Một thư viện lưu trữ thông tin các đầu sách trong một file văn bản tên "sach.txt", mỗi dòng lưu thông tin một quyển sách theo định dạng: ma_sach,ten_sach,tac_gia,so_luong,gia_tien. Ví dụ nội dung file:

S001,Lap trinh Python co ban,Nguyen Van A,10,85000S002,Cau truc du lieu va giai thuat,Tran Thi B,5,120000S003,Co so du lieu,Le Van C,8,95000

Mỗi quyển sách được biểu diễn bằng một dataclass Sach, toàn bộ thư viện được lưu trong một List các đối tượng Sach. Hãy viết chương trình Python thực hiện các yêu cầu sau:

Đọc dữ liệu từ file "sach.txt", tạo danh sách các đối tượng Sach tương ứng.

Sắp xếp danh sách sách theo tên sách tăng dần (thứ tự chữ cái).

Cho phép người dùng nhập vào một mã sách và tìm kiếm, in ra đầy đủ thông tin quyển sách nếu tìm thấy, hoặc thông báo không tìm thấy.

Thống kê: tổng số đầu sách, tổng số lượng sách hiện có, và tổng giá trị toàn bộ kho sách (số lượng × giá tiền, cộng dồn qua tất cả các sách).

Cho phép mượn sách: người dùng nhập mã sách và số lượng muốn mượn; nếu số lượng còn lại đủ thì trừ đi số lượng tương ứng, ngược lại thông báo không đủ sách để cho mượn.

Ghi lại danh sách sách (đã cập nhật số lượng sau khi cho mượn) xuống một file mới tên "sach_capnhat.txt", giữ nguyên định dạng như file đầu vào.

Gợi ý:

Khai báo @dataclass Sach gồm các trường ma_sach, ten_sach, tac_gia, so_luong, gia_tien, tương tự cách khai báo SanPham ở bài trước.

Đọc file và tách trường bằng split(",") giống bài tập nâng cao trước; nhớ ép kiểu int cho so_luong và float cho gia_tien.

Dùng sorted(ds, key=lambda s: s.ten_sach) để sắp xếp theo tên mà không làm thay đổi thứ tự trong danh sách gốc (nếu muốn giữ bản gốc để ghi file sau).

Viết một hàm tim_theo_ma(ds, ma_sach) duyệt qua List, so sánh s.ma_sach với giá trị cần tìm, trả về đối tượng Sach nếu tìm thấy, trả về None nếu không có.

Thống kê dùng len(ds) cho tổng số đầu sách, và sum(...) cho tổng số lượng cũng như tổng giá trị.

Cho mượn sách: gọi lại hàm tim_theo_ma để lấy đối tượng Sach, kiểm tra so_luong đủ hay không rồi cập nhật trực tiếp thuộc tính so_luong của đối tượng đó (vì dataclass mặc định có thể thay đổi được các trường).

Ghi file lại theo đúng định dạng ban đầu, tương tự hàm ghi_ra_file ở bài tập nâng cao trước.

Lưu ý: bài tập này tổng hợp gần như đầy đủ các kỹ năng đã học trong buổi thực hành — List, Dataclass, đọc/ghi File, sắp xếp, tìm kiếm và thống kê — phù hợp làm bài tập lớn cuối buổi hoặc bài tập về nhà.

Sản phẩm nộp lại

File mã nguồn Python (.py) cho Bài 1, Bài 2 (phần A), các câu a–h (phần B) và các bài tập nâng cao (phần C, D).

Một đoạn nhận xét ngắn (vài dòng) so sánh code tự viết với code do AI sinh ra: điểm giống, điểm khác, code nào tối ưu/dễ đọc hơn và vì sao.