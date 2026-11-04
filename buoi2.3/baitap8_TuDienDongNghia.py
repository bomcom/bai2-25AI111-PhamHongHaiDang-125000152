"""
BÀI TẬP 8: TỪ ĐIỂN ĐỒNG NGHĨA ĐA CHIỀU (MỨC ĐỘ: TRUNG BÌNH - DICTIONARY & SET)
Kết hợp Dictionary và Set để quản lý quan hệ đồng nghĩa hai chiều không trùng lặp.
"""

import sys
from collections import defaultdict

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


class Thesaurus:
    def __init__(self):
        # Value là một Set để tự động loại bỏ từ trùng lặp
        self.data: dict[str, set[str]] = defaultdict(set)

    def add_synonyms(self, word1: str, word2: str):
        word1, word2 = word1.strip().lower(), word2.strip().lower()
        if word1 == word2:
            return
        # Quan hệ hai chiều
        self.data[word1].add(word2)
        self.data[word2].add(word1)
        print(f"-> Đã liên kết từ đồng nghĩa: '{word1}' <--> '{word2}'")

    def lookup(self, word: str):
        word = word.strip().lower()
        if word in self.data and len(self.data[word]) > 0:
            synonyms = ", ".join(sorted(self.data[word]))
            print(f"Các từ đồng nghĩa với '{word}': {synonyms}")
            return self.data[word]
        else:
            print(f"Không tìm thấy dữ liệu từ đồng nghĩa cho: '{word}'")
            return set()


def main():
    print("=== BÀI TẬP 8: TỪ ĐIỂN ĐỒNG NGHĨA ĐA CHIỀU (DICT & SET) ===")
    thesaurus = Thesaurus()

    thesaurus.add_synonyms("vui", "hạnh phúc")
    thesaurus.add_synonyms("vui", "phấn khởi")
    thesaurus.add_synonyms("hạnh phúc", "sung sướng")
    thesaurus.add_synonyms("vui", "hạnh phúc")  # Thử thêm trùng lặp

    print("\n--- Tra cứu từ đồng nghĩa ---")
    thesaurus.lookup("vui")
    thesaurus.lookup("hạnh phúc")
    thesaurus.lookup("buồn")


if __name__ == "__main__":
    main()
