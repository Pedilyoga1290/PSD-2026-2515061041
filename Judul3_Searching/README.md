Program Pencarian Nilai Tugas Satu Semester

Program ini mencari nilai tugas selama satu semester menggunakan binary search, dengan cara memasukkan nilai yang ingin dicari, lalu sistem akan mencari niai yang cocok dengan mencari median dari indeks, hal ini dilakukan terus menerus sampai nilai yang dicari ditemukan.

<img width="2128" height="1660" alt="image" src="https://github.com/user-attachments/assets/97503062-c8b9-45ce-836d-ab3014adb87a" />

Penjelasan Kode :

1. Mendefinisikan fungsi binary_search dengan parameter untuk daftar skor, panjangnya, dan nilai target.
2. Mengatur indeks batas kiri ke nol.
3. Mengatur indeks batas kanan ke posisi valid terakhir.
4. Menginisialisasi hasil posisi ke -1 untuk menunjukkan tidak ditemukan.
5. Memulai perulangan yang berlanjut selama interval pencarian valid.
6. Menghitung indeks titik tengah antara kiri dan kanan.
7. Mencetak titik tengah saat ini dan skornya untuk penelusuran.
8. Memeriksa apakah skor titik tengah cocok dengan target.
9. Menyimpan indeks titik tengah sebagai posisi yang ditemukan.
10. Keluar dari perulangan lebih awal karena target ditemukan.
11. Jika tidak, memeriksa apakah skor titik tengah kurang dari target.
12. Mencetak pesan yang menunjukkan pencarian akan berpindah ke bagian kanan.
13. Memindahkan batas kiri ke satu posisi setelah titik tengah.
14. Jika tidak, menangani kasus di mana skor titik tengah lebih besar dari target.
15. Mencetak pesan yang menunjukkan pencarian akan berpindah ke bagian kiri.
16. Memindahkan batas kanan ke satu posisi sebelum titik tengah.
17. Mengembalikan posisi yang ditemukan atau -1 jika tidak ditemukan.
18. -
19. Mendefinisikan fungsi main.
20. Membuat daftar nilai tugas semester yang diurutkan.
21. Menghitung jumlah nilai dalam daftar.
22. Mencetak seluruh daftar nilai.
23. Memulai perulangan untuk meminta input yang valid dari pengguna.
24. Memulai blok untuk menangkap input yang tidak valid.
25. Membaca input dari pengguna dan mengonversinya menjadi bilangan bulat.
26. Keluar dari perulangan input ketika angka yang valid telah dimasukkan.
27. Menangani kasus di mana konversi input gagal.
28. Mencetak pesan kesalahan yang memberi tahu pengguna untuk memasukkan angka.
29. Memanggil fungsi pencarian biner dengan daftar nilai, panjangnya, dan target.
30. Memeriksa apakah posisi yang dikembalikan menunjukkan keberhasilan.
31. Mencetak pesan dengan indeks yang ditemukan ketika nilai tersebut ada.
32. Memeriksa apakah posisi yang dikembalikan bukanlah data yang dimasukkan
33. Mencetak pesan yang menyatakan bahwa nilai tersebut tidak ditemukan.
34. -
35. Memeriksa apakah skrip dijalankan sebagai program utama.
36. Memanggil main untuk memulai eksekusi.

<img width="990" height="585" alt="image" src="https://github.com/user-attachments/assets/7ad3a424-4581-434d-b6cb-d6fb8dfda64e" />

Penjelasan Output :

Pertama, sistem akan menampilkan nilai yang sudah tersedia dan mengurut, lalu, pengguna diminta untuk mengisi nilai yang akan dicari, lalu, sistem akan mencari nilai tengah atau median dari data nilai sampai nilai yang pengguna masukkan ketemu, dan akan ditmpilkan prosesnya dan nilai tersebut ditemukan di indeks ke berapa. Apabila user memasukkan angka yang tidak ada di data, sistem tetap mencari median dari data tersebut, namun di akhir proses, sistem akan mengeluarkan pesan "Nilai Yang Dicari Tidak Ditemukan".

Link Presentasi :

