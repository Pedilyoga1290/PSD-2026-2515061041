Judul Program : Pemutar Musik Sederhana

Deskripsi : Kode Python ini menjalankan sebuah sistem pemutar musik sederhana yang mengatur antrean lagu dengan struktur data Doubly Linked List. Setiap lagu disimpan sebagai simpul yang saling terhubung dua arah melalui kelas SongNode dan SmartPlayer. Ini memungkinkan pengguna dengan mudah menemukan daftar putar. Memasukkan lagu ke akhir daftar, menampilkan status lagu yang sedang diputar, dan melihat seluruh isi playlist secara berurutan adalah beberapa fitur dasar dari kode ini.

<img width="1177" height="596" alt="image" src="https://github.com/user-attachments/assets/7322ae6d-d5d0-4a3f-836e-f323c878f775" />
<img width="1167" height="597" alt="image" src="https://github.com/user-attachments/assets/ac96fb76-d83c-477c-9ca3-a040b8955ea6" />
<img width="1163" height="596" alt="image" src="https://github.com/user-attachments/assets/0596e65a-7091-45cd-8870-f4921fb7b097" />
<img width="370" height="108" alt="image" src="https://github.com/user-attachments/assets/0dc545b9-4eb7-4d82-9ac4-115601f1a37f" />

Deskripsi baris kode :

1. `class SongNode:` - Defines a node class to represent individual songs in the linked list.
2. `def __init__(self, title):` - Constructor that initializes a song node with a title.
3. `self.title = title` - Stores the song title in the node.
4. `self.next = None` - Pointer to the next song in the playlist (initially empty).
5. `self.prev = None` - Pointer to the previous song for bidirectional navigation.
6. `class SmartPlayer:` - Main class that manages the music player and playlist.
7. `def __init__(self):` - Initializes the player with empty references.
8. `self.head = None` - Points to the first song in the playlist.
9. `self.tail = None` - Points to the last song in the playlist.
10. `self.current = None` - Tracks which song is currently playing.
11. `def add_song(self, title):` - Method to add a new song to the playlist.
12. `new_song = SongNode(title)` - Creates a new song node with the given title.
13. `if self.head is None:` - Checks if the playlist is empty.
14. `self.head = new_song` - Sets the new song as the first song if playlist is empty.
15. `self.tail = new_song` - Also sets it as the last song.
16. `self.current = new_song` - Sets it as the currently playing song.
17. `return` - Exits the function early when adding to an empty playlist.
18. `self.tail.next = new_song` - Links the current last song to the new song.
19. `new_song.prev = self.tail` - Links the new song back to the previous last song.
20. `self.tail = new_song` - Updates the tail reference to the newly added song.
21. `def now_playing(self):` - Displays the currently playing song.
22. `if self.current:` - Checks if there is a current song playing.
23. `print(f"\nSEDANG DIPUTAR: {self.current.title}")` - Prints the current song's title in Indonesian.
24. `else:` - Executes if no song is currently playing.
25. `print("\nPlaylist masih kosong.")` - Displays a message indicating the playlist is empty.
26. `def play_next(self):` - Moves to the next song in the playlist.
27. `if self.current and self.current.next:` - Checks if there's a current song and a next song available.
28. `self.current = self.current.next` - Updates current to the next song.
29. `print(f"\n⏭️ Beralih ke lagu selanjutnya...")` - Prints a "skip forward" message.
30. `self.now_playing()` - Displays the newly playing song.
31. `else:` - Executes if at the last song or no current song.
32. `print("\n Ini adalah lagu terakhir di playlist. Tidak ada lagu selanjutnya.")` - Informs the user they're at the last song.
33. `def play_prev(self):` - Moves to the previous song in the playlist.
34. `if self.current and self.current.prev:` - Checks if there's a current song and a previous song available.
35. `self.current = self.current.prev` - Updates current to the previous song.
36. `print(f"\n⏮ Beralih ke lagu sebelumnya...")` - Prints a "skip backward" message.
37. `self.now_playing()` - Displays the newly playing song.
38. `else:` - Executes if at the first song or no current song.
39. `print("\n Ini adalah lagu pertama. Tidak ada lagu sebelumnya.")` - Informs the user they're at the first song.
40. `def show_playlist(self):` - Displays all songs in the playlist.
41. `if self.head is None:` - Checks if the playlist is empty.
42. `print("\nPlaylist kosong.")` - Prints an empty playlist message.
43. `return` - Exits the function early if playlist is empty.
44. `print("\n--- DAFTAR PLAYLIST ---")` - Prints a header for the playlist display.
45. `temp = self.head` - Creates a temporary pointer starting at the first song.
46. `nomor = 1` - Initializes a counter for numbering songs.
47. `while temp:` - Loops through all songs in the playlist.
48. `if temp == self.current:` - Checks if the current node is the playing song.
49. `print(f"{nomor}. [▶] {temp.title}")` - Displays the current song with a play indicator.
50. `else:` - Executes for non-current songs.
51. `print(f"{nomor}.     {temp.title}")` - Displays non-current songs without an indicator.
52. `temp = temp.next` - Moves to the next song.
53. `nomor += 1` - Increments the song counter.
54. `print("-----------------------")` - Prints a footer for the playlist display.
55. `if __name__ == "__main__":` - Ensures this code only runs when the script is executed directly.
56. `player = SmartPlayer()` - Creates a new music player instance.
57-59. `player.add_song(...)` - Adds three initial songs to the playlist.
60. `while True:` - Starts an infinite loop for the interactive menu.
61. `player.now_playing()` - Displays the current song before showing the menu.
62-67. `print(...)` - Displays menu options numbered 1-5.
68. `pilihan = input("Pilih aksi (1-5): ")` - Gets the user's menu choice as input.
69. `if pilihan == '1':` - Checks if user wants to add a new song.
70. `judul_lagu = input("Masukkan judul lagu beserta penyanyinya: ")` - Prompts user to enter song title.
71. `player.add_song(judul_lagu)` - Adds the entered song to the playlist.
72. `print(f"Berhasil menambahkan '{judul_lagu}' ke playlist")` - Confirms the song was added.
73. `elif pilihan == '2':` - Checks if user wants to skip to next song.
74. `player.play_next()` - Skips to the next song.
75. `elif pilihan == '3':` - Checks if user wants to skip to previous song.
76. `player.play_prev()` - Skips to the previous song.
77. `elif pilihan == '4':` - Checks if user wants to view the playlist.
78. `player.show_playlist()` - Displays all songs in the playlist.
79. `elif pilihan == '5':` - Checks if user wants to exit the program.
80. `print("Mematikan Musik.")` - Prints a goodbye message.
81. `break` - Exits the infinite loop and ends the program.
82. `else:` - Executes for any invalid menu choice.
83. `print("Pilihan tidak valid.")` - Displays an invalid choice message.
