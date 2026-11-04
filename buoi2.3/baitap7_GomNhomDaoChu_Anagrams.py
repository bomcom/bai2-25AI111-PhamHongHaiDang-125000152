"""
BÀI TẬP 7: GOM NHÓM CÁC TỪ ĐẢO CHỮ (GROUP ANAGRAMS) (MỨC ĐỘ: TRUNG BÌNH - DICTIONARY)
Sử dụng chuỗi ký tự đã sắp xếp làm Key để gom nhóm các từ có cùng chữ cái.
"""

import sys
from collections import defaultdict

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def group_anagrams(strs: list[str]) -> list[list[str]]:
    # Dùng defaultdict(list) để tự động tạo danh sách rỗng cho key mới
    anagram_groups = defaultdict(list)

    for word in strs:
        # Sắp xếp các ký tự để tạo ra một "chữ ký" (signature) duy nhất
        signature = "".join(sorted(word))
        anagram_groups[signature].append(word)

    return list(anagram_groups.values())


def main():
    print("=== BÀI TẬP 7: GOM NHÓM TỪ ĐẢO CHỮ (GROUP ANAGRAMS) ===")
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"Danh sách từ gốc: {words}")

    groups = group_anagrams(words)
    print("\nCác nhóm đảo chữ tìm được:")
    for i, g in enumerate(groups, 1):
        print(f"  Nhóm {i}: {g}")


if __name__ == "__main__":
    main()
