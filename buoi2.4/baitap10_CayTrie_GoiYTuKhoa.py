"""
BÀI TẬP 10: CÂY TIỀN TỐ (TRIE) VÀ GỢI Ý TỪ KHÓA (AUTOCOMPLETE) (MỨC ĐỘ: RẤT KHÓ)
Cấu trúc cây đứng sau các hệ thống Auto-complete / Search Suggestion của Google.
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


class TrieNode:
    def __init__(self):
        self.children = {}  # Ký tự -> TrieNode
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for ch in word.lower():
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def _find_node(self, prefix: str):
        node = self.root
        for ch in prefix.lower():
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def search(self, word: str) -> bool:
        """Kiểm tra từ có tồn tại đầy đủ trong Trie không."""
        node = self._find_node(word)
        return node is not None and node.is_end

    def starts_with(self, prefix: str) -> bool:
        """Kiểm tra có từ nào bắt đầu bằng prefix không."""
        return self._find_node(prefix) is not None

    def autocomplete(self, prefix: str) -> list[str]:
        """Trả về tất cả các từ có tiền tố prefix theo thứ tự chữ cái."""
        node = self._find_node(prefix)
        if node is None:
            return []

        res = []
        def dfs(curr_node, current_word: str):
            if curr_node.is_end:
                res.append(current_word)
            for ch in sorted(curr_node.children.keys()):
                dfs(curr_node.children[ch], current_word + ch)

        dfs(node, prefix.lower())
        return res


def main():
    print("=== BÀI TẬP 10: CÂY TIỀN TỐ (TRIE) & GỢI Ý TỪ KHÓA ===")
    trie = Trie()
    sample_words = ["car", "card", "care", "cat", "dog", "do", "dot", "apple", "app", "application"]
    print(f"Nạp danh sách từ vựng: {sample_words}\n")
    for w in sample_words:
        trie.insert(w)

    print(f"search('car')       : {trie.search('car')} (Kỳ vọng: True)")
    print(f"search('ca')        : {trie.search('ca')} (Kỳ vọng: False - chỉ là tiền tố)")
    print(f"starts_with('do')   : {trie.starts_with('do')} (Kỳ vọng: True)")

    prefixes = ["ca", "do", "ap", "xyz"]
    print("\n--- Thử nghiệm gợi ý từ khóa (Autocomplete) ---")
    for p in prefixes:
        suggestions = trie.autocomplete(p)
        print(f"Tiền tố '{p:<3}' -> Gợi ý: {suggestions}")


if __name__ == "__main__":
    main()
