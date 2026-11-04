"""
BÀI TẬP 5: XÂY DỰNG CHỈ MỤC NGƯỢC (INVERTED INDEX) (MỨC ĐỘ: RẤT KHÓ - DICT)
Nguyên lý cốt lõi của các cỗ máy tìm kiếm (Google, Elasticsearch) cho phép tìm kiếm văn bản tốc độ cao.
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def build_inverted_index(documents: list[str]) -> dict[str, list[int]]:
    inverted_index: dict[str, list[int]] = {}

    for doc_id, doc in enumerate(documents):
        # Chuẩn hóa chữ thường và tách từ
        words = doc.lower().split()
        for word in words:
            if word not in inverted_index:
                inverted_index[word] = []
            if doc_id not in inverted_index[word]:  # Tránh thêm trùng ID văn bản
                inverted_index[word].append(doc_id)

    return inverted_index


def main():
    print("=== BÀI TẬP 5: CHỈ MỤC NGƯỢC (INVERTED INDEX) ===")

    documents = [
        "the quick brown fox",          # Document 0
        "jumps over the lazy dog",      # Document 1
        "the quick brown dog",          # Document 2
        "an intelligent brown fox"      # Document 3
    ]

    print("--- Tập hợp tài liệu gốc ---")
    for idx, doc in enumerate(documents):
        print(f"Doc {idx}: '{doc}'")

    index = build_inverted_index(documents)

    print("\n--- Bảng chỉ mục ngược đã xây dựng (Inverted Index) ---")
    for word, doc_ids in sorted(index.items()):
        print(f"Từ '{word:<12}': xuất hiện ở tài liệu {doc_ids}")

    print("\n--- Tìm kiếm tài liệu ---")
    search_term = input("Nhập từ cần tìm (ví dụ: brown, dog, quick): ").strip().lower()
    if not search_term:
        search_term = "brown"
        print(f"-> Tìm mẫu từ '{search_term}':")

    found_ids = index.get(search_term)
    if found_ids is not None:
        print(f"-> Từ '{search_term}' xuất hiện trong các tài liệu: {found_ids}")
        for i in found_ids:
            print(f'   + Doc {i}: \"{documents[i]}\"')
    else:
        print(f"-> Không tìm thấy từ '{search_term}' trong bất kỳ tài liệu nào.")


if __name__ == "__main__":
    main()
