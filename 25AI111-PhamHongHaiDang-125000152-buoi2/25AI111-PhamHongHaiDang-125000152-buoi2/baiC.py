# Một kho hàng lưu trữ thông tin các sản phẩm trong một file văn bản tên "sanpham.txt", mỗi dòng trong file lưu thông tin một sản phẩm theo định dạng: ma_sp,ten_sp,so_luong,don_gia (các trường cách nhau bởi dấu phẩy). Ví dụ nội dung file:

#SP001,Ban phim,50,150000
#SP002,Chuot khong day,120,90000
#SP003,Man hinh 24 inch,15,2500000

#Hãy viết chương trình Python thực hiện các yêu cầu sau, trong đó mỗi sản phẩm được biểu diễn bằng một dataclass SanPham và toàn bộ kho hàng được lưu trong một List các đối tượng SanPham:

#1. Đọc dữ liệu từ file "sanpham.txt", tạo danh sách các đối tượng SanPham tương ứng.
#2. Cho phép người dùng nhập thông tin một sản phẩm mới và thêm vào cuối danh sách.
#3. Tính tổng giá trị tồn kho của toàn bộ kho hàng (giá trị tồn kho của một sản phẩm = số lượng × đơn giá).
#4. Tìm và in ra sản phẩm có giá trị tồn kho lớn nhất.
#5. Ghi lại toàn bộ danh sách sản phẩm (đã bao gồm sản phẩm vừa thêm) xuống một file mới tên "sanpham_moi.txt", giữ nguyên định dạng như file đầu vào.
#Gợi ý:

#Khai báo @dataclass SanPham gồm các trường ma_sp, ten_sp, so_luong, don_gia; có thể thêm một phương thức gia_tri_ton(self) trả về so_luong * don_gia.
#Dùng with open(duong_dan, "r", encoding="utf-8") as f: rồi duyệt for dong in f: để đọc từng dòng; dùng dong.strip().split(",") để tách các trường, nhớ ép kiểu int/float cho so_luong và don_gia.
#Dùng ds.append(SanPham(...)) để thêm sản phẩm mới vào List, giống cách thêm phần tử đã học ở các bài trước.
#Dùng sum(sp.gia_tri_ton() for sp in ds) để tính tổng giá trị tồn kho, và max(ds, key=lambda sp: sp.gia_tri_ton()) để tìm sản phẩm có giá trị tồn kho lớn nhất.
#Khi ghi file, dùng with open(duong_dan, "w", encoding="utf-8") as f: rồi f.write(f"{sp.ma_sp},{sp.ten_sp},{sp.so_luong},{sp.don_gia}\n") cho từng sản phẩm trong danh sách.

from dataclasses import dataclass

filename="sanpham.txt"  

@dataclass
class SanPham:
    ma_sp: str
    ten_sp: str
    so_luong: int
    don_gia: float
    
    def gia_tri_ton(self):
        return self.so_luong * self.don_gia

    # 1. Đọc dữ liệu từ file "sanpham.txt", tạo danh sách các đối tượng SanPham tương ứng.
    def doc_san_pham(filename):
        try:
            ds = []
            with open(filename, "r", encoding="utf-8") as f:
                for dong in f:
                    if dong.strip():
                        parts = dong.strip().split(",")
                        ds.append(SanPham(parts[0], parts[1], int(parts[2]), float(parts[3])))
            return ds
        except FileNotFoundError:
            print(f"Khong tim thay file {filename}")
            return []
    
    def ghi_san_pham(filename, ds):
        try:
            with open(filename, "w", encoding="utf-8") as f:
                for sp in ds:
                    f.write(f"{sp.ma_sp},{sp.ten_sp},{sp.so_luong},{sp.don_gia}\n")
            print(f"Da ghi {len(ds)} san pham xuong file {filename}")
        except Exception as e:
            print(f"Loi khi ghi file: {e}") 
    # 3. Tính tổng giá trị tồn kho của toàn bộ kho hàng (giá trị tồn kho của một sản phẩm = số lượng × đơn giá).
    def tinh_tong_gia_tri_ton(ds):
        return sum(sp.gia_tri_ton() for sp in ds)
    
    # 4. Tìm và in ra sản phẩm có giá trị tồn kho lớn nhất.
    def tim_san_pham_lon_nhat(ds):
        if not ds:
            return None
        return max(ds, key=lambda sp: sp.gia_tri_ton())
    
    def hien_san_pham(ds):
        print("Ma SP\tTen SP\tSo luong\tDon gia\tGia tri ton kho")
        for sp in ds:
            print(f"{sp.ma_sp}\t{sp.ten_sp}\t{sp.so_luong}\t{sp.don_gia}\t{sp.gia_tri_ton()}")
    
    def nhap_san_pham():
        ma_sp = input("Nhap ma san pham: ")
        ten_sp = input("Nhap ten san pham: ")
        so_luong = int(input("Nhap so luong: "))
        don_gia = float(input("Nhap don gia: "))
        return SanPham(ma_sp, ten_sp, so_luong, don_gia)   

    def main():
        ds = SanPham.doc_san_pham(filename)
        if ds:
            SanPham.hien_san_pham(ds)
            print(f"Tong gia tri ton kho: {SanPham.tinh_tong_gia_tri_ton(ds)}")
            sp_max = SanPham.tim_san_pham_lon_nhat(ds)
            if sp_max:
                print(f"\nSan pham co gia tri ton kho lon nhat: {sp_max.ten_sp}")
            sp_moi = SanPham.nhap_san_pham()
            ds.append(sp_moi)
            SanPham.ghi_san_pham("sanpham_moi.txt", ds)

    # 2. Cho phép người dùng nhập thông tin một sản phẩm mới và thêm vào cuối danh sách.

    def __init__(self, ma_sp, ten_sp, so_luong, don_gia):
        self.ma_sp = ma_sp
        self.ten_sp = ten_sp
        self.so_luong = so_luong
        self.don_gia = don_gia           

    if __name__ == "__main__":
        main()
