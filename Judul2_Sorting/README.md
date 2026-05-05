Tugas Akhir Judul 2

Program Pengurutan Judul Lagu di Playlist Berdasarkan Alphabet

Program ini bertujuan untuk mengurutkan lagu yang ada di playlist untuk berurut sesuai abjad menggunakan Bubble Sort. Pengguna diminta untuk memasukkan berapa banyak lagu yang diinginkan dalam satu playlist, lalu memasukkan nama lagu ke playlist tersebut. Kemudian, lagu yang sudah dimasukkan ke dalam playlist akan di sortir otomatis menggunakan Bubble Sort, sistem akan membandingkan dua lagu berdasarkan abjad pertama, lalu mengubah posisi lagu tersebut ke tempat yang sesuai, hingga semua lagu tersusun dengan rapih.

<img width="1618" height="2648" alt="code" src="https://github.com/user-attachments/assets/d1da3216-fcc5-407f-a60d-d0a9824f459f" />

1. Mendefinisikan kelas bernama SongNode untuk mewakili lagu-lagu individual dalam daftar putar.
2. Memulai definisi metode init untuk SongNode, yang menginisialisasi node dengan judul.
3. Menetapkan judul yang diberikan ke atribut judul node.
4. Mengatur pointer next ke None, menunjukkan tidak ada node berikutnya pada awalnya.
5. Mengatur pointer prev ke None, menunjukkan tidak ada node sebelumnya pada awalnya.
6. 
7. Mendefinisikan kelas bernama Playlist untuk mengelola koleksi lagu.
8. Memulai definisi metode init untuk Playlist, yang menginisialisasi daftar putar.
9. Mengatur penunjuk kepala ke None, menunjukkan daftar putar kosong di awal.
10. Mengatur penunjuk ekor ke None, menunjukkan daftar putar kosong di awal.
11. 
12. Memulai definisi metode add_song untuk menambahkan lagu baru ke daftar putar.
13. Membuat instance SongNode baru dengan judul yang diberikan.
14. Memeriksa apakah daftar putar kosong (tidak ada node kepala).
15. Jika kosong, mengatur kepala dan ekor ke node baru.
16. Mengembalikan nilai awal jika daftar putar kosong.
17. Mengatur pointer next dari ekor saat ini ke node baru.
18. Mengatur pointer prev dari node baru ke ekor saat ini.
19. Memperbarui ekor ke node baru.
20. -
21. Memulai definisi metode tampilan untuk mencetak daftar putar.      
22. Menginisialisasi penunjuk sementara ke kepala daftar putar.
23. Membuat daftar kosong untuk menyimpan judul lagu.
24. Memulai perulangan untuk menelusuri daftar putar selama masih ada node.
25. Menambahkan judul node saat ini ke daftar lagu.
26. Memindahkan penunjuk sementara ke node berikutnya.
27. Mencetak lagu-lagu yang dipisahkan oleh " -> " jika ada lagu, jika tidak, mencetak "Daftar Putar Kosong".
28. -
29. Memulai definisi fungsi bubble_sort untuk mengurutkan daftar putar secara alfabetis.
30. Memeriksa apakah daftar putar kosong atau hanya berisi satu lagu, dan akan berhenti lebih awal jika demikian.
31. Mengembalikan Fungsi ketika playlist kosong atau berisi satu lagu
32. -
33. Menginisialisasi flag swapped ke True untuk memulai loop pengurutan.
34. Memulai perulangan while yang berlanjut selama pertukaran terjadi.
35. Mengatur ulang flag swapped menjadi False di awal setiap putaran.
36. Mengatur pointer saat ini ke kepala daftar putar.
37. Baris kosong untuk spasi.
38. Memulai perulangan while dalam untuk menelusuri daftar selama ada node berikutnya.
39. Membandingkan judul huruf kecil dari node saat ini dan node berikutnya untuk urutan abjad.
40. Jika tidak berurutan, menukar judul node saat ini dan node berikutnya.
41. Mengatur swapped menjadi True untuk menunjukkan pertukaran telah terjadi.
42. Baris kosong untuk spasi.
43.  Memindahkan pointer saat ini ke node berikutnya.
44. -
45. Memulai definisi fungsi utama untuk menjalankan program.
Memulai blok try untuk menangani potensi kesalahan input.
Meminta pengguna untuk memasukkan jumlah lagu dan mengkonversi input ke bilangan bulat.
Memulai blok except untuk menangkap ValueError jika input bukan angka.
Mencetak pesan kesalahan untuk input yang tidak valid.
Mengembalikan nilai dari fungsi jika input tidak valid.
Membuat instance Playlist baru.
Mencetak prompt untuk memasukkan judul lagu.
Memulai perulangan for untuk mengulangi n kali untuk memasukkan lagu.
Membaca judul lagu dari input pengguna.
Menambahkan judul yang dimasukkan ke playlist.
Mencetak pesan sebelum menampilkan playlist yang belum diurutkan.
Menampilkan playlist saat ini.
Memanggil bubble_sort untuk mengurutkan playlist.
Mencetak pesan sebelum menampilkan playlist yang sudah diurutkan.
Menampilkan playlist yang sudah diurutkan.
Memeriksa apakah skrip dijalankan langsung (tidak diimpor).
Memanggil fungsi utama jika kondisinya benar.
46. 
47. 
48. 
49. 
50. 
51. 
52. 
53. 
54. 
55. 
56. 
57. 
58. 
59. 
60. 
61. 
62. 

Output Program :

<img width="1133" height="244" alt="image" src="https://github.com/user-attachments/assets/c4fbd082-59ba-48f6-9da1-c8736ee9a947" />
