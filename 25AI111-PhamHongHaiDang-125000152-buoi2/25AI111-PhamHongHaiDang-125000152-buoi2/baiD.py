# Một thư viện lưu trữ thông tin các đầu sách trong một file văn bản tên "sach.txt", mỗi dòng lưu thông tin một quyển sách theo định dạng: ma_sach,ten_sach,tac_gia,so_luong,gia_tien. Ví dụ nội dung file:

#S001,Lap trinh Python co ban,Nguyen Van A,10,85000
#S002,Cau truc du lieu va giai thuat,Tran Thi B,5,120000
#S003,Co so du lieu,Le Van C,8,95000

# Mỗi quyển sách được biểu diễn bằng một dataclass Sach, toàn bộ thư viện được lưu trong một List các đối tượng Sach. Hãy viết chương trình Python thực hiện các yêu cầu sau:

# 1. Đọc dữ liệu từ file "sach.txt", tạo danh sách các đối tượng Sach tương ứng.
# 2. Sắp xếp danh sách sách theo tên sách tăng dần (thứ tự chữ cái).
# 3. Cho phép người dùng nhập vào một mã sách và tìm kiếm, in ra đầy đủ thông tin quyển sách nếu tìm thấy, hoặc thông báo không tìm thấy.
# 4. Thống kê: tổng số đầu sách, tổng số lượng sách hiện có, và tổng giá trị toàn bộ kho sách (số lượng × giá tiền, cộng dồn qua tất cả các sách).
# 5. Cho phép mượn sách: người dùng nhập mã sách và số lượng muốn mượn; nếu số lượng còn lại đủ thì trừ đi số lượng tương ứng, ngược lại thông báo không đủ sách để cho mượn.
# 6. Ghi lại danh sách sách (đã cập nhật số lượng sau khi cho mượn) xuống một file mới tên "sach_capnhat.txt", giữ nguyên định dạng như file đầu vào.

from dataclasses import dataclass

filename = "sach.txt"

class sach():
    def __init__(self,ma_sach,ten_sach,tac_gia,so_luong,gia_tien):
        self.ma_sach = ma_sach
        self.ten_sach = ten_sach
        self.tac_gia = tac_gia
        self.so_luong = so_luong
        self.gia_tien = gia_tien
    
    def tinh_gia_tri_ton(self):
        return self.so_luong * self.gia_tien
    
    # 2. Sắp xếp danh sách sách theo tên sách tăng dần (thứ tự chữ cái).
    def sap_xep_sach(ds):
        ds.sort(key=lambda x: x.ten_sach)
        return ds
    
    # 3. Cho phép người dùng nhập vào một mã sách và tìm kiếm, in ra đầy đủ thông tin quyển sách nếu tìm thấy, hoặc thông báo không tìm thấy.
    def tim_kiem_sach(ds, ma_sach):
        for sp in ds:
            if sp.ma_sach == ma_sach:
                return sp
        return None
    
    # 4. Thống kê: tổng số đầu sách, tổng số lượng sách hiện có, và tổng giá trị toàn bộ kho sách (số lượng × giá tiền, cộng dồn qua tất cả các sách).
    def tinh_tong_gia_tri_ton(ds):
        return sum(sp.tinh_gia_tri_ton() for sp in ds)
    
    # 5. Cho phép mượn sách: người dùng nhập mã sách và số lượng muốn mượn; nếu số lượng còn lại đủ thì trừ đi số lượng tương ứng, ngược lại thông báo không đủ sách để cho mượn.
    def muon_sach(ds, ma_sach, so_luong):
        sp = sach.tim_kiem_sach(ds, ma_sach)
        if sp:
            if sp.so_luong >= so_luong:
                sp.so_luong -= so_luong
                return True
            else:
                print("Khong du sach de cho muon")
                return False
        else:
            print("Khong tim thay sach")
            return False
    
    # 6. Ghi lại danh sách sách (đã cập nhật số lượng sau khi cho mượn) xuống một file mới tên "sach_capnhat.txt", giữ nguyên định dạng như file đầu vào.
    
def doc_file(filename):
    ds = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                parts = line.strip().split(",")
                ds.append(sach(parts[0], parts[1], parts[2], int(parts[3]), float(parts[4])))
    return ds

def ghi_file(filename, ds):
    with open(filename, "w", encoding="utf-8") as f:
        for sp in ds:
            f.write(f"{sp.ma_sach},{sp.ten_sach},{sp.tac_gia},{sp.so_luong},{sp.gia_tien}\n")

def hien(ds):
    print("Ma sach\tTen sach\tTac gia\tSo luong\tGia tien")
    for sp in ds:
        print(f"{sp.ma_sach}\t{sp.ten_sach}\t{sp.tac_gia}\t{sp.so_luong}\t{sp.gia_tien}")   

def main():
    ds = doc_file(filename)
    sach.sap_xep_sach(ds)
    hien(ds)

if __name__ == "__main__":
    main()
        