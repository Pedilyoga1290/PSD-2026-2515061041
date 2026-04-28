class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None
        self.prev = None

class SmartPlayer:
    def __init__(self):
        self.head = None 
        self.tail = None 
        self.current = None 

    def add_song(self, title):
        new_song = SongNode(title)
        
        if self.head is None:
            self.head = new_song
            self.tail = new_song
            self.current = new_song 
            return
            
        self.tail.next = new_song
        new_song.prev = self.tail
        self.tail = new_song

    def now_playing(self):
        if self.current:
            print(f"\nSEDANG DIPUTAR: {self.current.title}")
        else:
            print("\nPlaylist masih kosong.")

    def play_next(self):
        if self.current and self.current.next:
            self.current = self.current.next
            print(f"\n⏭️ Beralih ke lagu selanjutnya...")
            self.now_playing()
        else:
            print("\n Ini adalah lagu terakhir di playlist. Tidak ada lagu selanjutnya.")

    def play_prev(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            print(f"\n⏮ Beralih ke lagu sebelumnya...")
            self.now_playing()
        else:
            print("\n Ini adalah lagu pertama. Tidak ada lagu sebelumnya.")

    def show_playlist(self):
        if self.head is None:
            print("\nPlaylist kosong.")
            return
            
        print("\n--- DAFTAR PLAYLIST ---")
        temp = self.head
        nomor = 1
        while temp:
            if temp == self.current:
                print(f"{nomor}. [▶] {temp.title}")
            else:
                print(f"{nomor}.     {temp.title}")
            temp = temp.next
            nomor += 1
        print("-----------------------")

if __name__ == "__main__":
    player = SmartPlayer()
    
    player.add_song("Bohemian Rhapsody - Queen")
    player.add_song("Metallica - For Whom The Bell Tolls")
    player.add_song("Tame Impala - Let It Happen")
    
    while True:
        player.now_playing()
        
        print("\n Pemutar Lagu Sederhana")
        print("1. Tambah Lagu Baru")
        print("2. Next Song")
        print("3. Previous Song")
        print("4. Lihat Daftar Playlist")
        print("5. Matikan Musik")
        
        pilihan = input("Pilih aksi (1-5): ")
        
        if pilihan == '1':
            judul_lagu = input("Masukkan judul lagu beserta penyanyinya: ")
            player.add_song(judul_lagu)
            print(f"Berhasil menambahkan '{judul_lagu}' ke playlist")
        elif pilihan == '2':
            player.play_next()
        elif pilihan == '3':
            player.play_prev()
        elif pilihan == '4':
            player.show_playlist()
        elif pilihan == '5':
            print("Mematikan Musik.")
            break
        else:
            print("Pilihan tidak valid.")
