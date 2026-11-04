"""
BÀI TẬP 2: QUẢN LÝ THÔNG TIN SINH VIÊN (MỨC ĐỘ: DỄ - TRUNG BÌNH - DICT)
Sử dụng dict[str, Student] với Key là MSSV, Value là đối tượng Student.
"""

import sys
from dataclasses import dataclass
from datetime import date

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


@dataclass
class Student:
    full_name: str
    date_of_birth: date
    average_score: float

    def __str__(self) -> str:
        dob_str = self.date_of_birth.strftime("%d/%m/%Y")
        return f"{self.full_name} | Ngày sinh: {dob_str} | ĐTB: {self.average_score:.2f}"


class StudentManager:
    def __init__(self):
        self.student_database: dict[str, Student] = {}

    def add_student(self, mssv: str, name: str, dob: date, score: float):
        if mssv in self.student_database:
            print(f"Lỗi: MSSV '{mssv}' đã tồn tại trong hệ thống!")
            return False
        self.student_database[mssv] = Student(name, dob, score)
        print(f"-> Đã thêm sinh viên: {name} (MSSV: {mssv})")
        return True

    def find_student(self, mssv: str):
        found = self.student_database.get(mssv)
        if found is not None:
            print(f"-> Tìm thấy: [{mssv}] {found}")
        else:
            print(f"-> Không tìm thấy sinh viên với MSSV: '{mssv}'")
        return found

    def remove_student(self, mssv: str):
        if mssv in self.student_database:
            removed = self.student_database.pop(mssv)
            print(f"-> Đã xóa sinh viên: {removed.full_name} (MSSV: {mssv})")
            return True
        else:
            print(f"-> Không tìm thấy sinh viên có MSSV '{mssv}' để xóa.")
            return False

    def display_all(self):
        if not self.student_database:
            print("Danh sách sinh viên đang trống.")
            return
        print(f"\n--- DANH SÁCH SINH VIÊN ({len(self.student_database)} sinh viên) ---")
        for mssv, s in self.student_database.items():
            print(f"MSSV: {mssv:<10} | {s}")


def main():
    manager = StudentManager()

    # Dữ liệu mẫu ban đầu
    manager.add_student("25AI001", "Phạm Hồng Hải Đăng", date(2004, 9, 9), 8.8)
    manager.add_student("25AI002", "Nguyễn Văn An", date(2004, 5, 15), 7.5)
    manager.add_student("25AI003", "Trần Thị Mai", date(2004, 11, 20), 9.2)

    while True:
        print("\n=== HỆ THỐNG QUẢN LÝ SINH VIÊN ===")
        print("1. Thêm sinh viên mới")
        print("2. Tìm sinh viên theo MSSV")
        print("3. Xóa sinh viên theo MSSV")
        print("4. Hiển thị toàn bộ danh sách")
        print("5. Thoát")

        choice = input("Lựa chọn (1-5): ").strip()
        if choice == "1":
            mssv = input("Nhập MSSV: ").strip()
            name = input("Nhập họ tên: ").strip()
            d_str = input("Nhập ngày sinh (dd/mm/yyyy): ").strip()
            try:
                day, month, year = map(int, d_str.split("/"))
                score = float(input("Nhập điểm trung bình: ").strip())
                manager.add_student(mssv, name, date(year, month, day), score)
            except Exception as e:
                print("Lỗi định dạng dữ liệu:", e)
        elif choice == "2":
            mssv = input("Nhập MSSV cần tìm: ").strip()
            manager.find_student(mssv)
        elif choice == "3":
            mssv = input("Nhập MSSV cần xóa: ").strip()
            manager.remove_student(mssv)
        elif choice == "4":
            manager.display_all()
        elif choice == "5":
            print("Đã thoát chương trình quản lý sinh viên.")
            break
        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()
