"""
BÀI TẬP 5: QUẢN LÝ DANH SÁCH SINH VIÊN (MỨC ĐỘ: RẤT KHÓ / VẬN DỤNG)
Thuật toán: Sắp xếp đối tượng (Object Sorting) đa tiêu chí và Tìm kiếm.
- Tiêu chí 1: Điểm trung bình giảm dần (-sv.diem_tb).
- Tiêu chí 2: Nếu bằng điểm, sắp xếp họ tên tăng dần theo A-Z (sv.ho_ten).
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


class SinhVien:
    def __init__(self, ma_sv: str, ho_ten: str, diem_tb: float):
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.diem_tb = diem_tb

    def __str__(self) -> str:
        return f"[{self.ma_sv}] {self.ho_ten:<16} - Điểm: {self.diem_tb:.1f}"


def tim_sinh_vien(ds: list, ten: str):
    """Tìm sinh viên đầu tiên khớp tên (không phân biệt hoa/thường)."""
    for sv in ds:
        if sv.ho_ten.lower() == ten.lower():
            return sv
    return None


def main():
    print("=== BÀI TẬP 5: SẮP XẾP ĐA TIÊU CHÍ VÀ TÌM KIẾM SINH VIÊN ===")
    ds_sinh_vien = [
        SinhVien("SV001", "Nguyen Van An", 8.5),
        SinhVien("SV002", "Tran Thi Binh", 7.2),
        SinhVien("SV003", "Le Van Cuong", 8.5),
        SinhVien("SV004", "Pham Thi Dung", 9.1),
        SinhVien("SV005", "Hoang Van Em", 7.2),
    ]

    # Yêu cầu 1: Sắp xếp đa tiêu chí bằng tuple trong lambda
    ds_da_sap_xep = sorted(
        ds_sinh_vien,
        key=lambda sv: (-sv.diem_tb, sv.ho_ten)
    )

    print("--- Danh sách sau khi sắp xếp (Điểm giảm dần, Tên A-Z) ---")
    for sv in ds_da_sap_xep:
        print(sv)

    # Yêu cầu 2: Tìm kiếm sinh viên
    print("\n--- Tìm kiếm sinh viên ---")
    for ten_can_tim in ["Le Van Cuong", "Tran Thi Mai"]:
        sv_tim_thay = tim_sinh_vien(ds_da_sap_xep, ten_can_tim)
        if sv_tim_thay:
            print(f"Tìm thấy: {sv_tim_thay}")
        else:
            print(f"Không tìm thấy sinh viên tên '{ten_can_tim}'.")


if __name__ == "__main__":
    main()
