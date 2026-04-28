Judul Program : Pemutar Musik Sederhana

Deskripsi : Kode Python ini menjalankan sebuah sistem pemutar musik sederhana yang mengatur antrean lagu dengan struktur data Doubly Linked List. Setiap lagu disimpan sebagai simpul yang saling terhubung dua arah melalui kelas SongNode dan SmartPlayer. Ini memungkinkan pengguna dengan mudah menemukan daftar putar. Memasukkan lagu ke akhir daftar, menampilkan status lagu yang sedang diputar, dan melihat seluruh isi playlist secara berurutan adalah beberapa fitur dasar dari kode ini.

<img width="1177" height="596" alt="image" src="https://github.com/user-attachments/assets/7322ae6d-d5d0-4a3f-836e-f323c878f775" />
<img width="1167" height="597" alt="image" src="https://github.com/user-attachments/assets/ac96fb76-d83c-477c-9ca3-a040b8955ea6" />
<img width="1163" height="596" alt="image" src="https://github.com/user-attachments/assets/0596e65a-7091-45cd-8870-f4921fb7b097" />
<img width="370" height="108" alt="image" src="https://github.com/user-attachments/assets/0dc545b9-4eb7-4d82-9ac4-115601f1a37f" />

Deskripsi baris kode :

1. Mendefinisikan kelas node untuk merepresentasikan lagu-lagu individual dalam linked list.
2. Pembangun yang menginisialisasi node lagu dengan sebuah judul.
3. Menyimpan judul lagu di dalam node.
4. Penunjuk ke lagu berikutnya dalam daftar putar (awalnya kosong).
5. Penunjuk ke lagu sebelumnya untuk navigasi dua arah.
6. 
7. Main class yang mengelola pemutar musik dan daftar putar.
8. Menginisialisasi pemain dengan referensi kosong.
9. Menunjuk ke lagu pertama dalam daftar putar.
10. Menunjuk ke lagu terakhir dalam daftar putar.
11. Melacak lagu yang sedang diputar saat ini.
12. 
13. Cara menambahkan lagu baru ke daftar putar.
14. Membuat node lagu baru dengan judul yang diberikan.
15. 
16. Mengecek apakah daftar putar kosong.
17. Menetapkan lagu baru sebagai lagu pertama jika daftar putar kosong.
18. Juga menempatkannya sebagai lagu terakhir.
19. Mengaturnya sebagai lagu yang sedang diputar.
20. Mengakhiri fungsi lebih awal saat menambahkan ke daftar putar kosong.
21. 
22. Menghubungkan lagu terakhir yang diputar dengan lagu baru.
23. Menghubungkan lagu baru kembali ke lagu terakhir sebelumnya.
24. Memperbarui referensi ekor ke lagu yang baru ditambahkan.
25. 
26. Menampilkan lagu yang sedang diputar.
27. Memeriksa apakah ada lagu yang sedang diputar.
28. Menampilkan judul lagu yang sedang diputar.
29. Dieksekusi jika tidak ada lagu yang sedang diputar.
30. Menampilkan pesan yang menunjukkan bahwa daftar putar kosong.
31. 
32. Beralih ke lagu berikutnya dalam daftar putar.
33. Memeriksa apakah ada lagu yang sedang diputar dan lagu berikutnya yang tersedia.
34. Mengupdate lagu saat ini hingga lagu berikutnya.
35. Mencetak pesan "beralih ke lagu selanjutnya".
36. Menampilkan lagu yang baru saja diputar.
37. Akan dieksekusi jika lagu terakhir diputar atau tidak ada lagu yang sedang diputar.
38. Memberi tahu pengguna bahwa mereka sedang mendengarkan lagu terakhir.
39. 
40. Beralih ke lagu sebelumnya dalam playlist.
41. `Memeriksa apakah ada lagu yang sedang diputar dan lagu sebelumnya yang tersedia.
42. `Mengupdate lagu sesuai dengan lagu sebelumnya.
43. Mencetak pesan "Beralih ke lagu sebelumnya...".
44. Menampilkan lagu yang baru saja diputar.
45. Akan dieksekusi jika lagu pertama sedang diputar atau tidak ada lagu yang sedang diputar.
46. Memberi tahu pengguna bahwa mereka sedang berada di lagu pertama.
47. 
48. Menampilkan semua lagu dalam daftar putar.
49. Memeriksa apakah daftar putar kosong.
50. Mencetak pesan bahwa playlist kosong.
51. Mengakhiri fungsi lebih awal jika playlist kosong.
52. 
53. Mencetak header untuk tampilan playlist.
54. Membuat penunjuk sementara yang dimulai dari lagu pertama.
55. Menginisialisasi penghitung untuk menomori lagu.
56. Memutar semua lagu dalam daftar putar secara berulang.
57. Memeriksa apakah node saat ini adalah lagu yang sedang diputar.
58. Menampilkan lagu yang sedang diputar dengan indikator pemutaran.
59. Dieksekusi untuk lagu-lagu yang bukan lagu terbaru.
60. Menampilkan lagu-lagu yang sudah tidak diputar tanpa indikator.
61. Beralih ke lagu berikutnya.
62. Menambah jumlah lagu yang dihitung.
63. Mencetak footer untuk tampilan daftar putar.
64. 
65. Memastikan kode ini hanya berjalan saat skrip dieksekusi secara langsung.
66. Membuat instance pemutar musik baru.
67. 
68. Menambahkan lagu ke Playlist.
69. Menambahkan lagu ke Playlist.
70. Menambahkan lagu ke playlist.
71. 
72. Memulai infinite loop untuk menu interaktif.
73. Menampilkan lagu yang sedang diputar sebelum menampilkan menu.
74. 
75. Menampilkan nama aplikasi.
76. Menampilkan Opsi pertama, yaitu menambah lagu
77. Menampilkan Opsi kedua, yaitu Lagu selanjutnya (next song)
78. Menampilkan Opsi ketiga, yaitu Lagu sebelumnya (previous song)
79. Menampilkan Opsi keempat, yaitu Cek isi Playlist
80. Menampilkan Opsi kelima, yaitu Mematikan musik (end program)
81. 
82. Menerima pilihan menu dari pengguna sebagai input.
83. 
84. Memeriksa apakah pengguna ingin menambahkan lagu baru.
85. Meminta pengguna untuk memasukkan judul lagu.
86. Menambahkan lagu yang dimasukkan ke dalam daftar putar.
87. Memastikan lagu tersebut telah ditambahkan.
88.  Memeriksa apakah pengguna ingin melompati ke lagu berikutnya.
89.  Langsung beralih ke lagu berikutnya.
90.  Memeriksa apakah pengguna ingin melompati ke lagu sebelumnya.
91.  Melompat ke lagu sebelumnya.
92.  Memeriksa apakah pengguna ingin melihat daftar putar.
93.  Menampilkan semua lagu dalam daftar putar.
94.  Memeriksa apakah pengguna ingin keluar dari program.
95.  Mencetak pesan "Mematikan musik"
96.  Keluar dari perulangan tak terbatas dan mengakhiri program.
97.  Dieksekusi untuk setiap pilihan menu yang tidak valid.
98. Menampilkan pesan pilihan tidak valid.

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

Link Presentasi : https://youtu.be/J_E6VLYEvP0
