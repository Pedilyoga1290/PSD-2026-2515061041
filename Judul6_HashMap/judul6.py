class SongNode:
    """Node baru untuk Doubly Linked List (Antrean Playlist)"""
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.next_song = None
        self.prev_song = None


class Node:
    """Node asli untuk Separate Chaining di Hash Map"""
    def __init__(self, key, value):
        self.key = key      
        self.value = value  
        self.next = None


class HashMapSeparateChaining:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE
        self.head = None
        self.tail = None

    def hash_function(self, key):
        hash_val = 0
        for char in key:
            hash_val += ord(char)
        return hash_val % self.SIZE

    def insert(self, key, value):
        new_song = SongNode(key, value)

        if self.head is None:
            self.head = new_song
            self.tail = new_song
        else:
            self.tail.next_song = new_song
            new_song.prev_song = self.tail
            self.tail = new_song
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                current.value.artist = value 
                return
            current = current.next
        new_hash_node = Node(key, new_song)
        new_hash_node.next = self.table[index]
        self.table[index] = new_hash_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def remove_key(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        
        target_song_node = None

        while current is not None:
            if current.key == key:
                target_song_node = current.value
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                break
            prev = current
            current = current.next
            
        if target_song_node is None:
            return False

        if target_song_node.prev_song:
            target_song_node.prev_song.next_song = target_song_node.next_song
        else:
            self.head = target_song_node.next_song 

        if target_song_node.next_song:
            target_song_node.next_song.prev_song = target_song_node.prev_song
        else:
            self.tail = target_song_node.prev_song 

        return True

    def display_hash(self):
        print("\nIsi Hash Table (Penyimpanan Indeks Lagu):")
        for i in range(self.SIZE):
            print(f"Indeks {i}: ", end="")
            current = self.table[i]
            while current is not None:
                print(f"[{current.key}] -> ", end="")
                current = current.next
            print("NULL")

    def display_playlist(self):
        print("\nAntrean Lagu SmartPlayer (Doubly Linked List):")
        current = self.head
        while current is not None:
            print(f"🎵 {current.title} - {current.artist}")
            current = current.next_song


def main():
    smart_player = HashMapSeparateChaining(size=7)

    smart_player.insert("Bohemian Rhapsody", "Queen")
    smart_player.insert("Shape of You", "Ed Sheeran")
    smart_player.insert("Hotel California", "Eagles")
    smart_player.insert("Blinding Lights", "The Weeknd")
    smart_player.insert("Imagine", "John Lennon")

    smart_player.display_playlist()

    smart_player.display_hash()

    cari_judul = "Hotel California"
    hasil = smart_player.search(cari_judul)
    
    if hasil is not None:
        print(f"\n✅ Pencarian Berhasil! Melompat ke lagu: {hasil.title} oleh {hasil.artist}")

        if hasil.next_song:
            print(f"   ⏭️ Lagu selanjutnya: {hasil.next_song.title}")
        if hasil.prev_song:
            print(f"   ⏮️ Lagu sebelumnya: {hasil.prev_song.title}")
    else:
        print(f"\n❌ Lagu '{cari_judul}' tidak ditemukan di playlist.")

    print("\nMenghapus 'Shape of You' dari sistem...")
    smart_player.remove_key("Shape of You")
    smart_player.display_playlist()

if __name__ == "__main__":
    main()
