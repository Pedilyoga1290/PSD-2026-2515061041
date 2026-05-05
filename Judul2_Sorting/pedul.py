class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None
        self.prev = None

class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_song(self, title):
        new_node = SongNode(title)
        if not self.head:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def display(self):
        temp = self.head
        songs = []
        while temp:
            songs.append(temp.title)
            temp = temp.next
        print(" -> ".join(songs) if songs else "Playlist Kosong")

def bubble_sort(playlist):
    if not playlist.head or not playlist.head.next:
        return 

    swapped = True
    while swapped:
        swapped = False
        current = playlist.head
        
        while current.next:
            if current.title.lower() > current.next.title.lower():
                current.title, current.next.title = current.next.title, current.title
                swapped = True
            
            current = current.next

def main():
    try:
        n = int(input("Masukkan jumlah lagu dalam playlist :"))
    except ValueError:
        print("Masukkan input yang valid!")
        return
    playlist = Playlist()
    print("Masukkan judul Lagu:")
    for _ in range(n):
        title = input()
        playlist.add_song(title)
    print("\nPlaylist sebelum diurutkan:")
    playlist.display()
    bubble_sort(playlist)
    print("\nPlaylist setelah diurutkan:")
    playlist.display()
if __name__ == "__main__":
    main()