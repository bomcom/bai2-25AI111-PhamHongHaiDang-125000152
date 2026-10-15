"""
Phần C: Bài tập nâng cao kết hợp List, Dataclass và File
Quản lý kho hàng (SanPham)
Code do AI sinh và tối ưu kiến trúc:
- Tách bạch cấu trúc dữ liệu SanPham và các hàm xử lý nghiệp vụ (separation of concerns).
- Sử dụng dataclass chuẩn PEP 557 (tự sinh __init__, __repr__).
- Xử lý File I/O an toàn với UTF-8 và bắt lỗi tệp tin.
"""

from dataclasses import dataclass
import os


@dataclass
class SanPham:
    ma_sp: str
    ten_sp: str
    so_luong: int
    don_gia: float

    def gia_tri_ton(self) -> float:
        """Tính giá trị tồn kho = số lượng * đơn giá"""
        return self.so_luong * self.don_gia

    def dinh_dang_file(self) -> str:
        """Định dạng chuẩn để lưu xuống file: ma_sp,ten_sp,so_luong,don_gia"""
        return f"{self.ma_sp},{self.ten_sp},{self.so_luong},{self.don_gia:.0f}"


def doc_tu_file(duong_dan: str) -> list[SanPham]:
    """1. Đọc dữ liệu từ file văn bản và tạo danh sách đối tượng SanPham"""
    ds = []
    if not os.path.exists(duong_dan):
        print(f"[Cảnh báo] File '{duong_dan}' chưa tồn tại. Tạo file mẫu...")
        du_lieu_mau = [
            "SP001,Ban phim,50,150000",
            "SP002,Chuot khong day,120,90000",
            "SP003,Man hinh 24 inch,15,2500000"
        ]
        with open(duong_dan, "w", encoding="utf-8") as f:
            f.write("\n".join(du_lieu_mau) + "\n")

    with open(duong_dan, "r", encoding="utf-8") as f:
        for dong in f:
            dong = dong.strip()
            if not dong:
                continue
            parts = [p.strip() for p in dong.split(",")]
            if len(parts) >= 4:
                ma, ten, sl, dg = parts[0], parts[1], int(parts[2]), float(parts[3])
                ds.append(SanPham(ma, ten, sl, dg))
    return ds


def them_san_pham(ds: list[SanPham]) -> None:
    """2. Cho phép người dùng nhập thông tin sản phẩm mới và thêm vào cuối danh sách"""
    print("\n--- NHẬP THÔNG TIN SẢN PHẨM MỚI ---")
    ma_sp = input("Mã sản phẩm: ").strip()
    ten_sp = input("Tên sản phẩm: ").strip()
    while True:
        try:
            so_luong = int(input("Số lượng tồn kho: "))
            don_gia = float(input("Đơn giá (VNĐ): "))
            break
        except ValueError:
            print("Số lượng và đơn giá phải là số! Vui lòng nhập lại.")

    sp_moi = SanPham(ma_sp, ten_sp, so_luong, don_gia)
    ds.append(sp_moi)
    print(f"-> Đã thêm sản phẩm '{ten_sp}' vào kho thành công!")


def tong_gia_tri_kho(ds: list[SanPham]) -> float:
    """3. Tính tổng giá trị tồn kho của toàn bộ kho hàng"""
    return sum(sp.gia_tri_ton() for sp in ds)


def san_pham_gia_tri_lon_nhat(ds: list[SanPham]) -> SanPham | None:
    """4. Tìm sản phẩm có giá trị tồn kho lớn nhất"""
    if not ds:
        return None
    return max(ds, key=lambda sp: sp.gia_tri_ton())


def ghi_ra_file(duong_dan: str, ds: list[SanPham]) -> None:
    """5. Ghi lại danh sách sản phẩm xuống file mới đúng chuẩn định dạng"""
    with open(duong_dan, "w", encoding="utf-8") as f:
        for sp in ds:
            f.write(sp.dinh_dang_file() + "\n")
    print(f"-> Đã ghi thành công {len(ds)} sản phẩm xuống file '{duong_dan}'.")


def in_bang_san_pham(ds: list[SanPham]) -> None:
    """Hiển thị danh sách sản phẩm dưới dạng bảng đẹp mắt"""
    print("-" * 75)
    print(f"{'Mã SP':<10} | {'Tên sản phẩm':<25} | {'Số lượng':>10} | {'Đơn giá':>12} | {'Trị giá tồn':>14}")
    print("-" * 75)
    for sp in ds:
        print(f"{sp.ma_sp:<10} | {sp.ten_sp:<25} | {sp.so_luong:>10} | {sp.don_gia:>12,.0f} | {sp.gia_tri_ton():>14,.0f}")
    print("-" * 75)


def main():
    file_vao = "sanpham.txt"
    file_ra = "sanpham_moi.txt"

    print("=== CHƯƠNG TRÌNH QUẢN LÝ KHO HÀNG (DATACLASS & FILE - AI) ===")
    
    # 1. Đọc dữ liệu
    ds = doc_tu_file(file_vao)
    print(f"\n1. Đã đọc {len(ds)} sản phẩm từ '{file_vao}':")
    in_bang_san_pham(ds)

    # 3. Tổng giá trị kho
    tong_tien = tong_gia_tri_kho(ds)
    print(f"\n3. Tổng giá trị tồn kho toàn bộ kho hàng: {tong_tien:,.0f} VNĐ")

    # 4. Sản phẩm có giá trị tồn lớn nhất
    sp_max = san_pham_gia_tri_lon_nhat(ds)
    if sp_max:
        print(f"\n4. Sản phẩm có giá trị tồn lớn nhất: {sp_max.ten_sp} ({sp_max.gia_tri_ton():,.0f} VNĐ)")

    # 2. Thêm sản phẩm mới
    them_san_pham(ds)

    # Hiển thị lại sau khi thêm
    print("\nDanh sách kho hàng sau khi bổ sung sản phẩm:")
    in_bang_san_pham(ds)

    # 5. Ghi file mới
    ghi_ra_file(file_ra, ds)


if __name__ == "__main__":
    main()
