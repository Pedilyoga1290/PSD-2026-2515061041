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
21. 
22. 
23. 
24. 
25. 
26. 
27. 
28. -
29. 
30. 
31. 
32. -
33. 
34. 
35. 
36. 
37. 
38. 
39. 
40. 
41. 
42. 
43. 
44. -
45. 
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
