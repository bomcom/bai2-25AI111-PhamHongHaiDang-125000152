"""
BÀI TẬP 1: ĐẾM TẦN SUẤT XUẤT HIỆN CỦA CÁC TỪ (MỨC ĐỘ: DỄ - DICT)
Sử dụng dict[str, int] để đếm số lần xuất hiện của mỗi từ trong câu.
Không phân biệt chữ hoa/thường.
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def count_word_frequencies(text: str) -> dict[str, int]:
    # 1. Chuyển về chữ thường
    text = text.lower()

    # 2. Loại bỏ các dấu câu đơn giản
    punctuation = [".", ",", "?", "!", ";", ":", '"', "'", "(", ")", "[", "]", "{", "}"]
    for p in punctuation:
        text = text.replace(p, " ")

    # 3. Tách từ
    words = text.split()
    word_frequencies: dict[str, int] = {}

    # 4. Đếm tần suất
    for word in words:
        if word in word_frequencies:
            word_frequencies[word] += 1
        else:
            word_frequencies[word] = 1

    return word_frequencies


def main():
    print("=== BÀI TẬP 1: ĐẾM TẦN SUẤT XUẤT HIỆN CỦA CÁC TỪ ===")
    user_input = input("Nhập một câu văn bản (Enter để dùng câu mẫu): ").strip()
    if not user_input:
        user_input = "Học lập trình Python rất thú vị, học AI lại càng thú vị hơn!"
        print(f"-> Câu mẫu: '{user_input}'")

    freqs = count_word_frequencies(user_input)

    print("\n--- Tần suất xuất hiện của các từ ---")
    # Sắp xếp giảm dần theo số lần xuất hiện
    sorted_words = sorted(freqs.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_words:
        print(f"Từ '{word}': {count} lần")


if __name__ == "__main__":
    main()
