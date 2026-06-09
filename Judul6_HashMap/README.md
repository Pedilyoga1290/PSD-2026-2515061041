Sistem Pencarian dan Playlist Lagu menggunakan Hash Map

Sistem ini menggunakan Hash Map Separate Chain untuk mencari lagu, menambah lagu, menghapus lagu dari playlist menggunakan Hash Map.

Source Code :
<img width="1778" height="5726" alt="judul 6" src="https://github.com/user-attachments/assets/60db6ce4-4d59-4281-a0e1-0eccd7722af1" />

Penjelasan kode :

1. Mendefinisikan kelas SongNode yang digunakan sebagai node dalam Doubly Linked List untuk antrean playlist.
2. Memberikan dokumentasi bahwa kelas ini merupakan node baru untuk antrean playlist.
3. Mendefinisikan konstruktor **init** yang menerima parameter title dan artist.
4. Menyimpan judul lagu ke atribut title milik objek.
5. Menyimpan nama artis ke atribut artist milik objek.
6. Menginisialisasi pointer next_song dengan nilai None karena belum ada lagu berikutnya.
7. Menginisialisasi pointer prev_song dengan nilai None karena belum ada lagu sebelumnya.
8. (kosong)
9. (kosong)
10. Mendefinisikan kelas Node yang digunakan untuk Separate Chaining pada Hash Map.
11. Memberikan dokumentasi bahwa kelas ini adalah node asli untuk Separate Chaining di Hash Map.
12. Mendefinisikan konstruktor **init** yang menerima parameter key dan value.
13. Menyimpan kunci hash ke atribut key milik objek.
14. Menyimpan nilai ke atribut value milik objek.
15. Menginisialisasi pointer next dengan nilai None karena belum ada node berikutnya.
16. (kosong)
17. (kosong)
18. Mendefinisikan kelas HashMapSeparateChaining untuk mengelola hash map dan playlist.
19. Mendefinisikan konstruktor **init** dengan ukuran default tabel sebesar 10.
20. Menyimpan ukuran tabel hash ke atribut SIZE.
21. Membuat tabel hash berupa list berisi None sebanyak ukuran SIZE.
22. Menginisialisasi head playlist dengan None karena playlist masih kosong.
23. Menginisialisasi tail playlist dengan None karena playlist masih kosong.
24. (kosong)
25. Mendefinisikan fungsi hash_function untuk menghitung indeks hash dari sebuah key.
26. Menginisialisasi variabel hash_val dengan nilai 0.
27. Melakukan perulangan untuk setiap karakter dalam key.
28. Menambahkan nilai ASCII setiap karakter ke hash_val menggunakan fungsi ord().
29. Mengembalikan indeks hash hasil modulo dengan ukuran tabel SIZE.
30. (kosong)
31. Mendefinisikan fungsi insert untuk menambahkan lagu ke playlist dan hash map.
32. Membuat node lagu baru menggunakan kelas SongNode dengan judul dan artis yang diberikan.
33. (kosong)
34. Memeriksa apakah playlist masih kosong dengan mengecek apakah head bernilai None.
35. Menjadikan lagu baru sebagai head playlist jika playlist masih kosong.
36. Menjadikan lagu baru sebagai tail playlist jika playlist masih kosong.
37. Jika playlist tidak kosong maka masuk ke blok else.
38. Menghubungkan lagu terakhir saat ini ke lagu baru melalui pointer next_song.
39. Menghubungkan lagu baru ke lagu terakhir sebelumnya melalui pointer prev_song.
40. Memperbarui tail playlist menjadi lagu baru.
41. Menghitung indeks hash dari key menggunakan hash_function.
42. Menyimpan node pertama pada indeks hash ke variabel current.
43. Melakukan traversal pada linked list di bucket hash selama current tidak None.
44. Memeriksa apakah key yang sedang dicek sama dengan key yang akan dimasukkan.
45. Jika key sama maka hanya memperbarui nama artis pada lagu yang sudah ada.
46. Menghentikan fungsi insert setelah update dilakukan.
47. Memindahkan current ke node berikutnya dalam bucket hash.
48. Membuat node hash baru menggunakan kelas Node dengan key dan node lagu.
49. Menghubungkan node hash baru ke node pertama lama pada bucket yang sama.
50. Menjadikan node hash baru sebagai kepala bucket pada indeks tersebut.
51. (kosong)
52. Mendefinisikan fungsi search untuk mencari lagu berdasarkan key.
53. Menghitung indeks hash dari key menggunakan hash_function.
54. Menyimpan node pertama pada bucket hash ke variabel current.
55. Melakukan traversal pada linked list bucket selama current tidak None.
56. Memeriksa apakah key pada node saat ini sama dengan key yang dicari.
57. Jika ditemukan maka mengembalikan value berupa SongNode yang terkait.
58. Memindahkan current ke node berikutnya dalam bucket hash.
59. Mengembalikan None jika lagu tidak ditemukan dalam hash map.
60. (kosong)
61. Mendefinisikan fungsi remove_key untuk menghapus lagu dari hash map dan playlist.
62. Menghitung indeks hash dari key menggunakan hash_function.
63. Menyimpan node pertama pada bucket hash ke variabel current.
64. Menginisialisasi variabel prev dengan None untuk menyimpan node sebelumnya.
65. (kosong)
66. Menginisialisasi variabel target_song_node dengan None untuk menyimpan node lagu yang akan dihapus.
67. (kosong)
68. Melakukan traversal pada linked list bucket selama current tidak None.
69. Memeriksa apakah key pada node saat ini sama dengan key yang akan dihapus.
70. Menyimpan SongNode yang terkait ke target_song_node jika key ditemukan.
71. Memeriksa apakah node yang dihapus berada di awal bucket.
72. Jika node di awal bucket maka kepala bucket dipindahkan ke node berikutnya.
73. Jika node bukan di awal bucket maka masuk ke blok else.
74. Menghubungkan node sebelumnya langsung ke node berikutnya untuk menghapus current dari bucket.
75. Menghentikan perulangan setelah node ditemukan dan dihapus dari hash map.
76. Memindahkan prev ke current sebelum melanjutkan traversal.
77. Memindahkan current ke node berikutnya dalam bucket hash.
78. (kosong)
79. Memeriksa apakah target_song_node tetap None yang berarti lagu tidak ditemukan.
80. Mengembalikan False jika lagu tidak ditemukan sehingga tidak ada yang dihapus.
81. (kosong)
82. Memeriksa apakah node lagu yang dihapus memiliki lagu sebelumnya dalam playlist.
83. Jika ada lagu sebelumnya maka pointer next_song lagu sebelumnya diarahkan ke lagu berikutnya.
84. Jika node yang dihapus adalah head playlist maka head dipindahkan ke lagu berikutnya.
85. (kosong)
86. Memeriksa apakah node lagu yang dihapus memiliki lagu berikutnya dalam playlist.
87. Jika ada lagu berikutnya maka pointer prev_song lagu berikutnya diarahkan ke lagu sebelumnya.
88. Jika node yang dihapus adalah tail playlist maka tail dipindahkan ke lagu sebelumnya.
89. (kosong)
90. Mengembalikan True untuk menandakan penghapusan berhasil dilakukan.
91. (kosong)
92. Mendefinisikan fungsi display_hash untuk menampilkan isi hash table.
93. Mencetak judul tampilan isi hash table ke layar.
94. Melakukan perulangan untuk setiap indeks dalam tabel hash.
95. Mencetak nomor indeks hash tanpa pindah baris.
96. Menyimpan node pertama pada bucket indeks saat ini ke variabel current.
97. Melakukan traversal pada linked list bucket selama current tidak None.
98. Mencetak key pada node saat ini diikuti tanda panah tanpa pindah baris.
99. Memindahkan current ke node berikutnya dalam bucket hash.
100. Mencetak NULL untuk menandai akhir linked list pada bucket tersebut.
101. (kosong)
102. Mendefinisikan fungsi display_playlist untuk menampilkan antrean lagu playlist.
103. Mencetak judul tampilan antrean lagu ke layar.
104. Menyimpan head playlist ke variabel current sebagai awal traversal.
105. Melakukan traversal pada doubly linked list selama current tidak None.
106. Mencetak judul lagu dan nama artis dari node saat ini.
107. Memindahkan current ke lagu berikutnya melalui pointer next_song.
108. (kosong)
109. (kosong)
110. Mendefinisikan fungsi main sebagai fungsi utama program.
111. Membuat objek smart_player dari kelas HashMapSeparateChaining dengan ukuran tabel hash 7.
112. (kosong)
113. Menambahkan lagu "Bohemian Rhapsody" dengan artis "Queen" ke sistem.
114. Menambahkan lagu "Shape of You" dengan artis "Ed Sheeran" ke sistem.
115. Menambahkan lagu "Hotel California" dengan artis "Eagles" ke sistem.
116. Menambahkan lagu "Blinding Lights" dengan artis "The Weeknd" ke sistem.
117. Menambahkan lagu "Imagine" dengan artis "John Lennon" ke sistem.
118. (kosong)
119. Menampilkan playlist yang berisi semua lagu yang telah ditambahkan.
120. (kosong)
121. Menampilkan isi hash table yang menyimpan indeks lagu.
122. (kosong)
123. Menyimpan judul lagu yang akan dicari ke variabel cari_judul.
124. Mencari lagu berdasarkan judul dan menyimpan hasilnya ke variabel hasil.
125. (kosong)
126. Memeriksa apakah hasil pencarian tidak None yang berarti lagu ditemukan.
127. Mencetak pesan bahwa pencarian berhasil beserta judul dan artis lagu.
128. (kosong)
129. Memeriksa apakah lagu yang ditemukan memiliki lagu berikutnya dalam playlist.
130. Mencetak judul lagu selanjutnya jika ada.
131. Memeriksa apakah lagu yang ditemukan memiliki lagu sebelumnya dalam playlist.
132. Mencetak judul lagu sebelumnya jika ada.
133. Jika lagu tidak ditemukan maka masuk ke blok else.
134. Mencetak pesan bahwa lagu yang dicari tidak ditemukan di playlist.
135. (kosong)
136. Mencetak pesan bahwa lagu "Shape of You" akan dihapus dari sistem.
137. Menghapus lagu "Shape of You" dari hash map dan playlist.
138. Menampilkan playlist setelah penghapusan dilakukan.
139. (kosong)
140. Memeriksa apakah file dijalankan langsung sebagai program utama.
141. Memanggil fungsi main jika file dijalankan langsung.

Output Program : 

<img width="541" height="473" alt="image" src="https://github.com/user-attachments/assets/04f950d0-5284-4db1-9c55-2b65f7915438" />

Link Presentasi : 
