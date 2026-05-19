class Stack:
    def __init__(self):
        self.books = []

    def is_empty(self):
        return len(self.books) == 0

    def push(self, book):
        self.books.append(book)
        print(f"{book} dimasukkan ke dalam rak buku.")

    def pop(self):
        if self.is_empty():
            return "Rak buku Kosong, Tidak ada buku yang bisa diambil."
        book_taken = self.books.pop()
        print(f"{book_taken} dikeluarkan dari rak buku.")
        return book_taken

    def peek(self):
        if self.is_empty():
            return "Rak buku Kosong, tidak ada buku yang bisa dilihat"
        
        return self.books[-1]

    def size(self):
        return len(self.books)

    def display(self):
        print(f"Isi Rak Buku saat ini (Bawah -> Atas): {self.books}")

def main():
    stack = Stack()
    pilihan = 0
    while pilihan != 5:
        print("\n=== Aplikasi Rak Buku ===")
        print("1. Masukkan Buku ke Rak (Push)")
        print("2. Ambil Buku Teratas (Pop)")
        print("3. Lihat Buku Teratas (Peek)")
        print("4. Tampilkan Buku di Rak")
        print("5. Keluar")

        try:
            pilihan = int(input("Pilih operasi (1-5): "))
        except ValueError:
            print("Input tidak valid! Silakan masukkan angka antara 1 dan 5.")
            continue

        if pilihan == 1:
            book = input("Masukkan nama buku yang ingin dimasukkan ke rak buku: ")
            stack.push(book)
        elif pilihan == 2:
            stack.pop()
        elif pilihan == 3:
            top_book = stack.peek()
            if top_book != "Rak buku Kosong, tidak ada buku yang bisa dilihat":
                print(f"buku teratas: {top_book}")
            else:
                print(top_book)
        elif pilihan == 4:
            stack.display()
        elif pilihan == 5:
            print("Keluar dari program. Terima kasih!")
        else:
            print("Pilihan tidak valid! Silakan pilih antara 1 dan 5.")

if __name__ == "__main__":
    main()