"""
Phần D: Bài tập tổng hợp nâng cao: Quản lý thư viện
Code do AI sinh và tối ưu:
- Dataclass Sach với đầy đủ kiểu dữ liệu type annotations.
- Tách bạch hàm đọc/ghi file và các nghiệp vụ: Sắp xếp, Tìm kiếm, Thống kê, Mượn sách.
- Giao diện console tương tác đầy đủ, kiểm tra ràng buộc số lượng sách khả dụng.
"""

from dataclasses import dataclass
import os


@dataclass
class Sach:
    ma_sach: str
    ten_sach: str
    tac_gia: str
    so_luong: int
    gia_tien: float

    def tong_gia_tri(self) -> float:
        """Tổng giá trị của đầu sách = số lượng * giá tiền"""
        return self.so_luong * self.gia_tien

    def dinh_dang_file(self) -> str:
        """Định dạng ghi file: ma_sach,ten_sach,tac_gia,so_luong,gia_tien"""
        return f"{self.ma_sach},{self.ten_sach},{self.tac_gia},{self.so_luong},{self.gia_tien:.0f}"


def doc_du_lieu(duong_dan: str) -> list[Sach]:
    """1. Đọc dữ liệu từ file 'sach.txt', tạo danh sách đối tượng Sach"""
    ds = []
    if not os.path.exists(duong_dan):
        print(f"[Cảnh báo] File '{duong_dan}' chưa có. Tạo dữ liệu mẫu...")
        du_lieu_mau = [
            "S001,Lap trinh Python co ban,Nguyen Van A,10,85000",
            "S002,Cau truc du lieu va giai thuat,Tran Thi B,5,120000",
            "S003,Co so du lieu,Le Van C,8,95000"
        ]
        with open(duong_dan, "w", encoding="utf-8") as f:
            f.write("\n".join(du_lieu_mau) + "\n")

    with open(duong_dan, "r", encoding="utf-8") as f:
        for dong in f:
            dong = dong.strip()
            if not dong:
                continue
            parts = [p.strip() for p in dong.split(",")]
            if len(parts) >= 5:
                ma, ten, tg, sl, gia = parts[0], parts[1], parts[2], int(parts[3]), float(parts[4])
                ds.append(Sach(ma, ten, tg, sl, gia))
    return ds


def sap_xep_theo_ten(ds: list[Sach]) -> list[Sach]:
    """2. Sắp xếp danh sách sách theo tên sách tăng dần (thứ tự chữ cái)"""
    return sorted(ds, key=lambda s: s.ten_sach.lower())


def tim_theo_ma(ds: list[Sach], ma_sach: str) -> Sach | None:
    """3. Tìm kiếm theo mã sách, trả về đối tượng Sach hoặc None"""
    for s in ds:
        if s.ma_sach.strip().upper() == ma_sach.strip().upper():
            return s
    return None


def thong_ke_thu_vien(ds: list[Sach]) -> tuple[int, int, float]:
    """4. Thống kê: (tổng số đầu sách, tổng số lượng sách, tổng giá trị toàn kho)"""
    tong_dau_sach = len(ds)
    tong_so_luong = sum(s.so_luong for s in ds)
    tong_gia_tri = sum(s.tong_gia_tri() for s in ds)
    return tong_dau_sach, tong_so_luong, tong_gia_tri


def muon_sach(ds: list[Sach], ma_sach: str, so_luong_muon: int) -> bool:
    """5. Cho phép mượn sách: trừ số lượng tồn nếu đủ, thông báo nếu không đủ"""
    sach_tim = tim_theo_ma(ds, ma_sach)
    if not sach_tim:
        print(f"-> Không tìm thấy mã sách '{ma_sach}' trong thư viện!")
        return False
    if sach_tim.so_luong < so_luong_muon:
        print(f"-> Không đủ sách để cho mượn! (Hiện còn {sach_tim.so_luong} quyển, yêu cầu {so_luong_muon} quyển)")
        return False
    sach_tim.so_luong -= so_luong_muon
    print(f"-> Cho mượn thành công {so_luong_muon} quyển '{sach_tim.ten_sach}'. Số lượng còn lại: {sach_tim.so_luong}")
    return True


def ghi_ra_file(duong_dan: str, ds: list[Sach]) -> None:
    """6. Ghi danh sách sách (đã cập nhật) xuống file mới"""
    with open(duong_dan, "w", encoding="utf-8") as f:
        for s in ds:
            f.write(s.dinh_dang_file() + "\n")
    print(f"-> Đã ghi danh sách cập nhật xuống file '{duong_dan}'.")


def in_bang_sach(ds: list[Sach]) -> None:
    """In danh sách sách thành bảng rõ ràng"""
    print("-" * 85)
    print(f"{'Mã':<6} | {'Tên sách':<32} | {'Tác giả':<18} | {'Số lượng':>8} | {'Giá tiền':>10}")
    print("-" * 85)
    for s in ds:
        print(f"{s.ma_sach:<6} | {s.ten_sach:<32} | {s.tac_gia:<18} | {s.so_luong:>8} | {s.gia_tien:>10,.0f}")
    print("-" * 85)


def main():
    file_vao = "sach.txt"
    file_ra = "sach_capnhat.txt"

    print("=== HỆ THỐNG QUẢN LÝ THƯ VIỆN SÁCH (AI OPTIMIZED) ===")
    
    # 1. Đọc dữ liệu
    ds = doc_du_lieu(file_vao)
    print(f"\n1. Danh sách ban đầu đọc từ '{file_vao}':")
    in_bang_sach(ds)

    # 2. Sắp xếp theo tên
    ds_sap_xep = sap_xep_theo_ten(ds)
    print("\n2. Danh sách sau khi sắp xếp theo tên sách (A-Z):")
    in_bang_sach(ds_sap_xep)

    # 4. Thống kê kho sách
    dau_sach, tong_sl, tong_tien = thong_ke_thu_vien(ds)
    print(f"\n4. Thống kê thư viện:")
    print(f"   - Tổng số đầu sách: {dau_sach}")
    print(f"   - Tổng số lượng bản sách: {tong_sl}")
    print(f"   - Tổng giá trị kho sách: {tong_tien:,.0f} VNĐ")

    # 3. Tìm kiếm theo mã
    print("\n3. Tìm kiếm sách theo mã:")
    ma_tim = input("   Nhập mã sách cần tìm (ví dụ: S002): ").strip()
    ket_qua = tim_theo_ma(ds, ma_tim)
    if ket_qua:
        print(f"   -> Tìm thấy: [{ket_qua.ma_sach}] {ket_qua.ten_sach} - TG: {ket_qua.tac_gia} - SL: {ket_qua.so_luong} - Giá: {ket_qua.gia_tien:,.0f} VNĐ")
    else:
        print(f"   -> Không tìm thấy mã sách '{ma_tim}' trong hệ thống.")

    # 5. Nghiệp vụ mượn sách
    print("\n5. Thực hiện mượn sách:")
    ma_muon = input("   Nhập mã sách muốn mượn: ").strip()
    try:
        sl_muon = int(input("   Nhập số lượng muốn mượn: "))
        if sl_muon > 0:
            muon_sach(ds, ma_muon, sl_muon)
        else:
            print("   Số lượng mượn phải lớn hơn 0!")
    except ValueError:
        print("   Số lượng không hợp lệ!")

    # 6. Ghi file cập nhật
    ghi_ra_file(file_ra, ds)


if __name__ == "__main__":
    main()
