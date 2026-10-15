"""
ỨNG DỤNG THƯ VIỆN my_linkedlist VÀO BÀI TOÁN PLAYLIST
"""

from my_linkedlist import DoublyLinkedList


def main():
    playlist = DoublyLinkedList(["Shape of You", "Blinding Lights"])

    while True:
        print("\n--- PLAYLIST CỦA BẠN (DÙNG my_linkedlist) ---")
        print("1. Thêm bài hát vào cuối")
        print("2. Thêm bài hát vào đầu")
        print("3. Chèn bài hát sau một bài cụ thể")
        print("4. Hiển thị playlist")
        print("5. Thoát")

        choice = input("Lựa chọn: ").strip()
        if choice == "1":
            song = input("Nhập tên bài hát: ").strip()
            playlist.add_last(song)
        elif choice == "2":
            song = input("Nhập tên bài hát: ").strip()
            playlist.add_first(song)
        elif choice == "3":
            target = input("Chèn sau bài hát nào: ").strip()
            node = playlist.find(target)
            if node:
                new_song = input("Nhập tên bài hát mới: ").strip()
                playlist.add_after(node, new_song)
            else:
                print("Không tìm thấy bài hát!")
        elif choice == "4":
            print("\n--- Danh sách phát ---")
            for song in playlist:
                print(f"🎵 {song}")
        elif choice == "5":
            break


if __name__ == "__main__":
    main()
