Judul Program : Pemutar Musik Sederhana

Deskripsi : Kode Python ini menjalankan sebuah sistem pemutar musik sederhana yang mengatur antrean lagu dengan struktur data Doubly Linked List. Setiap lagu disimpan sebagai simpul yang saling terhubung dua arah melalui kelas SongNode dan SmartPlayer. Ini memungkinkan pengguna dengan mudah menemukan daftar putar. Memasukkan lagu ke akhir daftar, menampilkan status lagu yang sedang diputar, dan melihat seluruh isi playlist secara berurutan adalah beberapa fitur dasar dari kode ini.

<img width="1177" height="596" alt="image" src="https://github.com/user-attachments/assets/7322ae6d-d5d0-4a3f-836e-f323c878f775" />
<img width="1167" height="597" alt="image" src="https://github.com/user-attachments/assets/ac96fb76-d83c-477c-9ca3-a040b8955ea6" />
<img width="1163" height="596" alt="image" src="https://github.com/user-attachments/assets/0596e65a-7091-45cd-8870-f4921fb7b097" />
<img width="370" height="108" alt="image" src="https://github.com/user-attachments/assets/0dc545b9-4eb7-4d82-9ac4-115601f1a37f" />

Deskripsi baris kode :

1. `class SongNode:` - Mendefinisikan kelas node untuk merepresentasikan lagu-lagu individual dalam linked list.
2. `def __init__(self, title):` - Pembangun yang menginisialisasi node lagu dengan sebuah judul.
3. `self.title = title` - Menyimpan judul lagu di dalam node.
4. `self.next = None` - Penunjuk ke lagu berikutnya dalam daftar putar (awalnya kosong).
5. `self.prev = None` - Penunjuk ke lagu sebelumnya untuk navigasi dua arah.
6. `class SmartPlayer:` - Main class yang mengelola pemutar musik dan daftar putar.
7. `def __init__(self):` - Menginisialisasi pemain dengan referensi kosong.
8. `self.head = None` - Menunjuk ke lagu pertama dalam daftar putar.
9. `self.tail = None` - Menunjuk ke lagu terakhir dalam daftar putar.
10. `self.current = None` - Melacak lagu yang sedang diputar saat ini.
11. `def add_song(self, title):` - Cara menambahkan lagu baru ke daftar putar.
12. `new_song = SongNode(title)` - Membuat node lagu baru dengan judul yang diberikan.
13. `if self.head is None:` - Mengecek apakah daftar putar kosong.
14. `self.head = new_song` - Menetapkan lagu baru sebagai lagu pertama jika daftar putar kosong.
15. `self.tail = new_song` - Juga menempatkannya sebagai lagu terakhir.
16. `self.current = new_song` - Mengaturnya sebagai lagu yang sedang diputar.
17. `return` -Mengakhiri fungsi lebih awal saat menambahkan ke daftar putar kosong.
18. `self.tail.next = new_song` - Menghubungkan lagu terakhir yang diputar dengan lagu baru.
19. `new_song.prev = self.tail` - Menghubungkan lagu baru kembali ke lagu terakhir sebelumnya.
20. `self.tail = new_song` - Memperbarui referensi ekor ke lagu yang baru ditambahkan.
21. `def now_playing(self):` - Menampilkan lagu yang sedang diputar.
22. `if self.current:` - Memeriksa apakah ada lagu yang sedang diputar.
23. `print(f"\nSEDANG DIPUTAR: {self.current.title}")` - Menampilkan judul lagu yang sedang diputar dalam bahasa Indonesia.
24. `else:` - Dieksekusi jika tidak ada lagu yang sedang diputar.
25. `print("\nPlaylist masih kosong.")` - Menampilkan pesan yang menunjukkan bahwa daftar putar kosong.
26. `def play_next(self):` -Beralih ke lagu berikutnya dalam daftar putar.
27. `if self.current and self.current.next:` - Memeriksa apakah ada lagu yang sedang diputar dan lagu berikutnya yang tersedia.
28. `self.current = self.current.next` - Mengupdate lagu saat ini hingga lagu berikutnya.
29. `print(f"\n⏭️ Beralih ke lagu selanjutnya...")` - Mencetak pesan "beralih ke lagu selanjutnya".
30. `self.now_playing()` - Menampilkan lagu yang baru saja diputar.
31. `else:` - Akan dieksekusi jika lagu terakhir diputar atau tidak ada lagu yang sedang diputar.
32. `print("\n Ini adalah lagu terakhir di playlist. Tidak ada lagu selanjutnya.")` - Memberi tahu pengguna bahwa mereka sedang mendengarkan lagu terakhir.
33. `def play_prev(self):` - Beralih ke lagu sebelumnya dalam playlist.
34. `if self.current and self.current.prev:` - Memeriksa apakah ada lagu yang sedang diputar dan lagu sebelumnya yang tersedia.
35. `self.current = self.current.prev` - Mengupdate lagu sesuai dengan lagu sebelumnya.
36. `print(f"\n⏮ Beralih ke lagu sebelumnya...")` - Mencetak pesan "Beralih ke lagu sebelumnya...".
37. `self.now_playing()` - Menampilkan lagu yang baru saja diputar.
38. `else:` - Akan dieksekusi jika lagu pertama sedang diputar atau tidak ada lagu yang sedang diputar.
39. `print("\n Ini adalah lagu pertama. Tidak ada lagu sebelumnya.")` - Memberi tahu pengguna bahwa mereka sedang berada di lagu pertama.
40. `def show_playlist(self):` - Menampilkan semua lagu dalam daftar putar.
41. `if self.head is None:` - Memeriksa apakah daftar putar kosong.
42. `print("\nPlaylist kosong.")` - Mencetak pesan bahwa playlist kosong.
43. `return` - Mengakhiri fungsi lebih awal jika playlist kosong.
44. `print("\n--- DAFTAR PLAYLIST ---")` - Mencetak header untuk tampilan playlist.
45. `temp = self.head` - Membuat penunjuk sementara yang dimulai dari lagu pertama.
46. `nomor = 1` - Menginisialisasi penghitung untuk menomori lagu.
47. `while temp:` - Memutar semua lagu dalam daftar putar secara berulang.
48. `if temp == self.current:` - Memeriksa apakah node saat ini adalah lagu yang sedang diputar.
49. `print(f"{nomor}. [▶] {temp.title}")` - Menampilkan lagu yang sedang diputar dengan indikator pemutaran.
50. `else:` - Dieksekusi untuk lagu-lagu yang bukan lagu terbaru.
51. `print(f"{nomor}.     {temp.title}")` - Menampilkan lagu-lagu yang sudah tidak diputar tanpa indikator.
52. `temp = temp.next` - Beralih ke lagu berikutnya.
53. `nomor += 1` - Menambah jumlah lagu yang dihitung.
54. `print("-----------------------")` - Mencetak footer untuk tampilan daftar putar.
55. `if __name__ == "__main__":` - Memastikan kode ini hanya berjalan saat skrip dieksekusi secara langsung.
56. `player = SmartPlayer()` - Membuat instance pemutar musik baru.
57-59. `player.add_song(...)` - Menambahkan tiga lagu awal ke daftar putar.
60. `while True:` - Memulai infinite loop untuk menu interaktif.
61. `player.now_playing()` - Menampilkan lagu yang sedang diputar sebelum menampilkan menu.
62-67. `print(...)` - Menampilkan pilihan menu bernomor 1-5.
68. `pilihan = input("Pilih aksi (1-5): ")` - Menerima pilihan menu dari pengguna sebagai input.
69. `if pilihan == '1':` - Memeriksa apakah pengguna ingin menambahkan lagu baru.
70. `judul_lagu = input("Masukkan judul lagu beserta penyanyinya: ")` -Meminta pengguna untuk memasukkan judul lagu.
71. `player.add_song(judul_lagu)` - Menambahkan lagu yang dimasukkan ke dalam daftar putar.
72. `print(f"Berhasil menambahkan '{judul_lagu}' ke playlist")` - Memastikan lagu tersebut telah ditambahkan.
73. `elif pilihan == '2':` - Memeriksa apakah pengguna ingin melompati ke lagu berikutnya.
74. `player.play_next()` - Langsung beralih ke lagu berikutnya.
75. `elif pilihan == '3':` - Memeriksa apakah pengguna ingin melompati ke lagu sebelumnya.
76. `player.play_prev()` - Melompat ke lagu sebelumnya.
77. `elif pilihan == '4':` - Memeriksa apakah pengguna ingin melihat daftar putar.
78. `player.show_playlist()` - Menampilkan semua lagu dalam daftar putar.
79. `elif pilihan == '5':` - Memeriksa apakah pengguna ingin keluar dari program.
80. `print("Mematikan Musik.")` - Mencetak pesan perpisahan.
81. `break` - Keluar dari perulangan tak terbatas dan mengakhiri program.
82. `else:` - Dieksekusi untuk setiap pilihan menu yang tidak valid.
83. `print("Pilihan tidak valid.")` - Menampilkan pesan pilihan tidak valid.

Output Program :

<img width="1308" height="646" alt="image" src="https://github.com/user-attachments/assets/ae55a049-4ec0-46d5-bef0-3e08b493e61c" />
<img width="1302" height="559" alt="image" src="https://github.com/user-attachments/assets/b2b7876f-e36a-4275-8a39-6368eb3dc4a7" />


Penjelasan Output :

Saat program dijalankan, sistem secara otomatis menambahkan tiga lagu ke dalam playlist melalui fungsi add_song:
Bohemian Rhapsody - Queen (sebagai head atau lagu pertama).
Metallica - For Whom The Bell Tolls.
Tame Impala - Let It Happen (sebagai tail atau lagu terakhir).

Program ini menggunakan looping (while True), jadinya program akan terus berjalan hingga pengguna menginput angka 5 di menu

A. Tampilan "Now Playing"
Setiap kali menu muncul, program akan memanggil now_playing().
Output: SEDANG DIPUTAR: [Judul Lagu]
Secara default, saat baru dinyalakan, lagu pertama yang muncul adalah "Bohemian Rhapsody".
B. Opsi 1: Tambah Lagu Baru
Jika pengguna menginput angka 1 di menu, Lagu baru ditambahkan di akhir daftar (tail) dan menambahkan '[Judul]' ke playlist
C. Opsi 2 & 3: Navigasi (Next & Prev)
Berfungsi sebagai pointer untuk traverse forward dan traverse backward
Next: Jika ada lagu setelahnya, penunjuk current berpindah ke next. Jika di lagu terakhir, muncul pesan: "Ini adalah lagu terakhir di playlist."
Prev: Jika ada lagu sebelumnya, penunjuk current berpindah ke prev. Jika di lagu pertama, muncul pesan: "Ini adalah lagu pertama."
D. Opsi 4: Lihat Daftar Playlist
Fungsi show_playlist() mencetak semua lagu yang ada di memori.
Indikator Khusus: Lagu yang sedang dipilih (node current) akan ditandai dengan simbol [▶]. Output dari opsi 4 akan terlihat sebagai berikut :
--- DAFTAR PLAYLIST ---
1. [▶] Bohemian Rhapsody - Queen
2.      Metallica - For Whom The Bell Tolls
3.      Tame Impala - Let It Happen
-----------------------
E. Opsi 5: Matikan Musik
Output: Mematikan Musik.
Berfungsi untuk menghentikan perulangan dan menutup program.
