Sistem Manajemen Persediaan Barang Menggunakan Binary Search Tree

Sistem ini menyimpan data persediaan barang menggunakan Binary Search Tree berdasarkan ID yang disimpan oleh pengguna. Penguna dapat menambah barang, mengecek barang, sortir barang menggunakan fungsi Inorder, mengupdate stok barang, menghitung berapa banyak barang yang tersedia, dan menjumlahkan seluruh stok barang.

<img width="1848" height="7360" alt="judul5" src="https://github.com/user-attachments/assets/0cf490c0-deda-4bd2-8b9a-3bf4b2cf15a7" />

Penjelasan Source Code :

1. Mendefinisikan kelas Node untuk menyimpan data barang dalam BST.
2. Membuat constructor untuk menginisialisasi atribut node.
3. Menyimpan ID barang ke dalam atribut objek.
4. Menyimpan nama barang ke dalam atribut objek.
5. Menyimpan jumlah stok barang ke dalam atribut objek.
6. Menginisialisasi child kiri dengan nilai kosong.
7. Menginisialisasi child kanan dengan nilai kosong.
8. (kosong)
9. Mendefinisikan kelas BSTInv sebagai Binary Search Tree inventaris.
10. Membuat constructor untuk BSTInv.
11. Menginisialisasi root tree dengan nilai kosong.
12. (kosong)
13. Membuat fungsi untuk menambahkan node baru ke BST.
14. Mengecek apakah root masih kosong.
15. Membuat node baru jika root kosong.
16. Mengecek apakah ID barang lebih kecil dari root.
17. Menambahkan node ke subtree kiri secara rekursif.
18. Mengecek apakah ID barang lebih besar dari root.
19. Menambahkan node ke subtree kanan secara rekursif.
20. Menangani kondisi jika ID barang sudah ada.
21. Menampilkan pesan peringatan jika ID barang duplikat.
22. Mengembalikan root setelah proses insert selesai.
23. (kosong)
24. Membuat fungsi insert utama untuk pengguna.
25. Memasukkan node baru ke dalam BST melalui root utama.
26. (kosong)
27. Membuat fungsi pencarian node berdasarkan ID barang.
28. Mengecek apakah node saat ini kosong.
29. Mengembalikan None jika barang tidak ditemukan.
30. Mengecek apakah ID barang sesuai dengan node saat ini.
31. Mengembalikan node jika barang ditemukan.
32. Mengecek apakah ID barang lebih kecil dari node saat ini.
33. Mencari barang pada subtree kiri secara rekursif.
34. Mencari barang pada subtree kanan secara rekursif.
35. (kosong)
36. Membuat fungsi untuk menghapus node dari BST.
37. Mengecek apakah node saat ini kosong.
38. Mengembalikan None jika node tidak ditemukan.
39. Mengecek apakah key lebih kecil dari ID node.
40. Menghapus node pada subtree kiri secara rekursif.
41. Mengecek apakah key lebih besar dari ID node.
42. Menghapus node pada subtree kanan secara rekursif.
43. Menjalankan proses penghapusan jika node ditemukan.
44. Mengecek apakah node tidak memiliki child.
45. Menghapus node daun dengan mengembalikan None.
46. Mengecek apakah node hanya memiliki child kanan.
47. Menggantikan node dengan child kanan.
48. Mengecek apakah node hanya memiliki child kiri.
49. Menggantikan node dengan child kiri.
50. Menangani kondisi jika node memiliki dua child.
51. Mencari successor terkecil dari subtree kanan.
52. Mengganti ID barang dengan data successor.
53. Mengganti nama barang dengan data successor.
54. Mengganti stok barang dengan data successor.
55. Menghapus node successor dari subtree kanan.
56. Mengembalikan root setelah proses delete selesai.
57. (kosong)
58. Membuat fungsi delete utama untuk pengguna.
59. Menghapus node dari root utama BST.
60. (kosong)
61. Membuat fungsi untuk mencari node dengan nilai terkecil.
62. Menyimpan root awal ke variabel current.
63. Melakukan perulangan selama child kiri masih ada.
64. Memindahkan current ke child kiri.
65. Mengembalikan node terkecil yang ditemukan.
66. (kosong)
67. Membuat fungsi pencarian barang utama.
68. Memanggil fungsi pencarian mulai dari root utama.
69. (kosong)
70. Membuat fungsi untuk memperbarui stok barang.
71. Mencari node barang berdasarkan ID.
72. Mengecek apakah barang ditemukan.
73. Mengecek apakah hasil perubahan stok menjadi negatif.
74. Menampilkan pesan gagal jika stok menjadi minus.
75. Menjalankan proses update jika stok valid.
76. Menambahkan perubahan jumlah stok ke stok lama.
77. Menampilkan pesan sukses setelah stok diperbarui.
78. Menangani kondisi jika barang tidak ditemukan.
79. Menampilkan pesan gagal karena barang tidak ada.
80. (kosong)
81. Membuat fungsi traversal inorder untuk menampilkan data barang.
82. Mengecek apakah node kosong.
83. Menghentikan fungsi jika node kosong.
84. Menampilkan subtree kiri terlebih dahulu secara rekursif.
85. Menampilkan data barang dalam format tabel.
86. Menampilkan subtree kanan secara rekursif.
87. (kosong)
88. Membuat fungsi untuk menghitung jumlah jenis barang.
89. Mengecek apakah node kosong.
90. Mengembalikan 0 jika node kosong.
91. Menghitung total node pada subtree kiri dan kanan.
92. (kosong)
93. Membuat fungsi untuk menghitung total stok barang.
94. Mengecek apakah node kosong.
95. Mengembalikan 0 jika node kosong.
96. Menjumlahkan stok node dengan subtree kiri dan kanan.
97. (kosong)
98. (kosong)
99. Mendefinisikan fungsi utama program.
100. Membuat objek BST inventaris bernama gudang.
101. (kosong)
102. Menambahkan data barang Laptop ke BST.
103. Menambahkan data barang Mouse ke BST.
104. Menambahkan data barang Keyboard ke BST.
105. (kosong)
106. Menginisialisasi variabel pilihan menu dengan nilai 0.
107. Membuat perulangan selama pengguna belum memilih keluar.
108. Menampilkan judul menu sistem.
109. Menampilkan opsi tambah barang baru.
110. Menampilkan opsi cari data barang.
111. Menampilkan opsi tampilkan semua barang.
112. Menampilkan opsi update stok barang.
113. Menampilkan opsi laporan jumlah jenis barang.
114. Menampilkan opsi laporan total stok barang.
115. Menampilkan opsi hapus barang.
116. Menampilkan opsi keluar program.
117. (kosong)
118. Memulai blok penanganan error input.
119. Meminta pengguna memilih menu dan mengubah input menjadi integer.
120. Menangani error jika input bukan angka.
121. Menampilkan pesan kesalahan input.
122. Melanjutkan perulangan menu berikutnya.
123. (kosong)
124. Mengecek apakah pengguna memilih menu 1.
125. Memulai blok penanganan error input barang.
126. Meminta input ID barang dari pengguna.
127. Meminta input nama barang dari pengguna.
128. Meminta input jumlah stok barang.
129. Menambahkan barang baru ke BST.
130. Menampilkan pesan sukses penambahan barang.
131. Menangani error jika input tidak valid.
132. Menampilkan pesan kesalahan input angka.
133. (kosong)
134. Mengecek apakah pengguna memilih menu 2.
135. Memulai blok penanganan error pencarian barang.
136. Meminta input ID barang yang dicari.
137. Mencari barang berdasarkan ID.
138. Mengecek apakah barang ditemukan.
139. Menampilkan judul hasil pencarian.
140. Menampilkan ID barang yang ditemukan.
141. Menampilkan nama barang yang ditemukan.
142. Menampilkan jumlah stok barang yang ditemukan.
143. Menampilkan garis penutup hasil pencarian.
144. Menangani kondisi jika barang tidak ditemukan.
145. Menampilkan pesan bahwa barang tidak ada dalam sistem.
146. Menangani error jika input ID tidak valid.
147. Menampilkan pesan kesalahan input angka.
148. (kosong)
149. Mengecek apakah pengguna memilih menu 3.
150. Menampilkan judul daftar barang gudang.
151. Menampilkan semua barang menggunakan traversal inorder.
152. Menampilkan garis penutup daftar barang.
153. (kosong)
154. Mengecek apakah pengguna memilih menu 4.
155. Memulai blok penanganan error update stok.
156. Meminta input ID barang.
157. Menampilkan petunjuk penggunaan angka positif dan negatif.
158. Meminta input jumlah perubahan stok.
159. Memperbarui stok barang sesuai perubahan.
160. Menangani error jika input tidak valid.
161. Menampilkan pesan kesalahan input angka.
162. (kosong)
163. Mengecek apakah pengguna memilih menu 5.
164. Menghitung jumlah jenis barang di BST.
165. Menampilkan total jenis barang di gudang.
166. (kosong)
167. Mengecek apakah pengguna memilih menu 6.
168. Menghitung total keseluruhan stok barang.
169. Menampilkan total stok fisik barang di gudang.
170. (kosong)
171. Mengecek apakah pengguna memilih menu 7.
172. Memulai blok penanganan error penghapusan barang.
173. Meminta input ID barang yang akan dihapus.
174. Menghapus barang dari BST.
175. Menampilkan pesan sukses penghapusan barang.
176. Menangani error jika input tidak valid.
177. Menampilkan pesan kesalahan input angka.
178. (kosong)
179. Mengecek apakah pengguna memilih menu 8.
180. Menampilkan pesan penutupan sistem.
181. Menangani pilihan menu yang tidak tersedia.
182. Menampilkan pesan bahwa pilihan tidak valid.
183. (kosong)
184. (kosong)
185. Mengecek apakah file dijalankan sebagai program utama.
186. Menjalankan fungsi main untuk memulai program.

Output dari Program : 

Pilihan 1 :

<img width="312" height="246" alt="image" src="https://github.com/user-attachments/assets/caa24c76-9f60-4b67-8b5d-9e26bfe0955f" />

Pilihan 2 :

<img width="322" height="295" alt="image" src="https://github.com/user-attachments/assets/048f5214-a01f-4699-a7de-6e1fbc8452af" />

Pilihan 3 :

<img width="367" height="293" alt="image" src="https://github.com/user-attachments/assets/5e7aa953-27e9-4879-8227-43cffa297230" />

Pilihan 4 :

<img width="533" height="242" alt="image" src="https://github.com/user-attachments/assets/29c76428-2ef1-4b90-a324-b00ddf089407" />

Pilihan 5 :

<img width="338" height="190" alt="image" src="https://github.com/user-attachments/assets/2e01c791-1281-4f43-8018-17db53b5bb7e" />

Pilihan 6 :

<img width="412" height="188" alt="image" src="https://github.com/user-attachments/assets/18bec90c-2333-45b8-8abd-ff00780bd45e" />

Pilihan 7 :

<img width="292" height="208" alt="image" src="https://github.com/user-attachments/assets/2179b689-90ae-4e15-9fca-9d91a6947281" />

Pilihan 8 :

<img width="308" height="203" alt="image" src="https://github.com/user-attachments/assets/fe679401-ce11-4513-92e9-b31219fc0ee9" />

Link Presentasi : https://youtu.be/qO4FXQT2JJA
