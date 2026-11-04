"""
BÀI TẬP 10: TRA CỨU VÀ LỌC SẢN PHẨM E-COMMERCE (MỨC ĐỘ: RẤT KHÓ / VẬN DỤNG THỰC TẾ)
Thuật toán: Sắp xếp danh sách đối tượng & Tìm kiếm nhị phân khoảng giá (Binary Search Range).
Sử dụng module bisect (bisect_left và bisect_right) để lọc khoảng giá cực nhanh O(log N).
"""

import bisect
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


class SanPham:
    def __init__(self, ma_sp: str, ten_sp: str, gia: float):
        self.ma_sp = ma_sp
        self.ten_sp = ten_sp
        self.gia = gia

    def __str__(self) -> str:
        return f"[{self.ma_sp}] {self.ten_sp:<20} - Giá: {self.gia:,.0f} VNĐ"


def tim_san_pham_theo_khoang_gia(ds_da_sap_xep: list, gia_min: float, gia_max: float) -> list:
    """Lọc các sản phẩm có giá nằm trong [gia_min, gia_max] bằng Binary Search."""
    cac_muc_gia = [sp.gia for sp in ds_da_sap_xep]

    # Tìm chỉ số đầu tiên có giá >= gia_min
    left_idx = bisect.bisect_left(cac_muc_gia, gia_min)

    # Tìm chỉ số đầu tiên có giá > gia_max
    right_idx = bisect.bisect_right(cac_muc_gia, gia_max)

    # Trích xuất danh sách con bằng Python Slicing
    return ds_da_sap_xep[left_idx:right_idx]


def main():
    print("=== BÀI TẬP 10: LỌC SẢN PHẨM THEO KHOẢNG GIÁ (E-COMMERCE) ===")
    ds_sp = [
        SanPham("SP01", "Chuột Không Dây", 250000),
        SanPham("SP02", "Bàn Phím Cơ", 1200000),
        SanPham("SP03", "Tai Nghe Bluetooth", 850000),
        SanPham("SP04", "Màn Hình 24 inch", 3500000),
        SanPham("SP05", "Lót Chuột RGB", 150000),
        SanPham("SP06", "Webcam HD", 650000),
    ]

    # 1. Sắp xếp danh sách theo giá tăng dần
    ds_sp_sap_xep = sorted(ds_sp, key=lambda sp: sp.gia)

    print("--- Danh sách sản phẩm đã sắp xếp theo giá ---")
    for sp in ds_sp_sap_xep:
        print(sp)

    # 2. Lọc sản phẩm trong khoảng giá 200,000 đến 1,000,000 VNĐ
    gia_tu = 200000
    gia_den = 1000000
    ket_qua = tim_san_pham_theo_khoang_gia(ds_sp_sap_xep, gia_tu, gia_den)

    print(f"\n--- SẢN PHẨM TRONG KHOẢNG GIÁ {gia_tu:,.0f} - {gia_den:,.0f} VNĐ ---")
    if ket_qua:
        for sp in ket_qua:
            print(sp)
    else:
        print("Không có sản phẩm nào trong khoảng giá này.")


if __name__ == "__main__":
    main()
