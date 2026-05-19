Program Stacking Buku Dalam Rak Buku

Kode ini berfungsi untuk menumpuk suatu buku ke dalam rak buku menggunakan program stack, pengguna diminta untuk memasukkan nama buku, lalu buku tersebut akan dimasukkan ke rak paling bawah (push), dan seterusnya. Pengguna dapat mengambil buku dengan menggunakan fungsi pop agar mengambil buku yang terakhir kali dimasukkan ke rak buku. Pengguna dapat melihat buku yang terakhir kali dimasukkan ke rak menggunakan fungsi peek. Dan pengguna dapat melihat seluruh isi buku (dari buku pertama yang dimasukkan hingga buku yang terakhir kali dimasukkan) menggunakan fungsi display

Source Code :
<img width="1526" height="2838" alt="judul4" src="https://github.com/user-attachments/assets/99c7bbcc-b4b3-40ba-b761-dbe64e1b3217" />

Penjelasan kode :

1. Mendefinisikan kelas Stack untuk merepresentasikan tumpukan buku.
2. Mendefinisikan metode konstruktor __init__ untuk Stack.
3. Menginisialisasi daftar kosong self.books untuk menyimpan isi tumpukan.
4. 
5. Mendefinisikan metode is_empty untuk memeriksa apakah tumpukan tidak memiliki buku.
6. Mengembalikan True jika self.books memiliki panjang nol, jika tidak False.
7. 
8. Mendefinisikan metode push yang menerima buku untuk ditambahkan ke tumpukan.
9. Menambahkan buku yang diberikan ke daftar self.books.
10. Mencetak pesan yang menunjukkan buku telah ditempatkan ke dalam rak.
11. 
12. Mendefinisikan metode pop untuk menghapus dan mengembalikan buku teratas.
13. Memeriksa apakah tumpukan kosong dengan memanggil is_empty.
14. Jika kosong, mengembalikan string yang memberi tahu pemanggil bahwa rak kosong dan tidak ada buku yang dapat diambil.
15. Jika tidak, menghapus item terakhir dari self.books dan menyimpannya di book_taken.
16. Mencetak pesan bahwa buku yang dihapus telah dikeluarkan dari rak.
17. Mengembalikan buku yang dihapus yang disimpan di book_taken.
18. 
19. Mendefinisikan metode peek untuk melihat buku teratas tanpa mengeluarkannya.
20. Jika tumpukan kosong, mengembalikan string yang menunjukkan tidak ada buku untuk dilihat.
21. Mengembalikan elemen terakhir dari self.books dan menampilkan pesan buku kosong
22. 
23. Mengembalikan elemen terakhir dari self.books
24.
25. Mendefinisikan metode size untuk melaporkan berapa banyak buku yang ada di tumpukan.
26. Mengembalikan panjang self.books sebagai ukuran tumpukan.
27.
28. Mendefinisikan metode display untuk mencetak isi tumpukan saat ini.
29. Mencetak daftar self.books yang diberi label sebagai isi rak dari bawah ke atas.
30. 
31. Mendefinisikan fungsi utama yang menjalankan antarmuka baris perintah untuk tumpukan.
32. Membuat instance Stack baru dan menetapkannya ke stack.
33. Menginisialisasi variabel kontrol pilihan ke 0 untuk memasuki loop menu.
34. Memulai loop while yang berlanjut hingga pilihan sama dengan 5 (opsi keluar).
35. Mencetak baris header untuk menu aplikasi.
36. Mencetak opsi menu untuk mendorong buku ke tumpukan.
37. Mencetak opsi menu untuk mengeluarkan buku teratas dari tumpukan.
38. Mencetak opsi menu untuk mengintip buku teratas.
39. Mencetak opsi menu untuk menampilkan semua buku di rak.
40. Mencetak opsi menu untuk keluar dari program.
41. 
42. Memulai blok try untuk mengurai input pengguna dengan aman.
43. Membaca input pengguna, mengonversinya ke bilangan bulat, dan menyimpannya di pilihan.
44. Memulai blok except ValueError untuk menangkap konversi bilangan bulat yang tidak valid.
45. Mencetak pesan kesalahan yang meminta angka antara 1 dan 5 ketika input tidak valid.
46. Fungsi ini terus memulai ulang loop setelah input yang tidak valid.
47. 
48. Memeriksa apakah pilihan yang dipilih sama dengan 1 untuk melakukan operasi push.
49. Meminta pengguna untuk memasukkan nama buku dan menyimpannya di book.
50. Memanggil stack.push(book) untuk menambahkan buku yang dimasukkan ke dalam tumpukan.
51. Memeriksa apakah pilihan sama dengan 2 untuk melakukan operasi pop.
52. Memanggil stack.pop() untuk menghapus dan mencetak buku teratas.
53. Memeriksa apakah pilihan sama dengan 3 untuk melakukan operasi peek.
54. Memanggil stack.peek() dan menyimpan hasilnya di top_book.
55. Membandingkan top_book dengan pesan sentinel kosong untuk menentukan apakah buku yang valid telah dikembalikan.
56. Jika buku teratas yang valid ada, mencetak judulnya yang diberi label sebagai buku teratas.
57. Jika tidak ada buku yang bisa di peek
58. mencetak pesan kosong yang dikembalikan oleh peek untuk memberi tahu pengguna.
59. Memeriksa apakah pilihan sama dengan 4 untuk menampilkan isi tumpukan.
60. Memanggil stack.display() untuk mencetak buku-buku yang ada di rak saat ini.
61. Memeriksa apakah pilihan sama dengan 5 untuk menangani opsi keluar.
62. Mencetak pesan perpisahan sebelum keluar dari program.
63. Menangani pilihan angka tidak valid lainnya yang bukan dalam rentang 1–5.
64. Mencetak pesan yang memberi tahu pengguna bahwa pilihan tersebut tidak valid dan untuk memilih antara 1 dan 5.
65. 
66. Memeriksa apakah skrip dijalankan sebagai program utama.
67. Memanggil fungsi main() untuk memulai aplikasi interaktif.

Output program : 

<img width="705" height="487" alt="image" src="https://github.com/user-attachments/assets/f0e5a4ea-7970-49dc-b33b-f6ae528244d2" />

Penjelasan output : 

Pengguna diminta untuk memasukkan angka antara 1 sampai 5. Apabila pengguna memilih nomor 1, pengguna akan diminta untuk memasukkan nama buku untuk dimasukkan ke dalam rak buku, dan buku tersebut dimasukkan ke bagian bawah rak buku. Apabila pengguna memilih nomor 2, pengguna dapat mengambil buku yang terakhir kali dimasukkan, kalau rak kosong dan pengguna tetap memilih nomor 2, akan keluar pesan "Rak buku Kosong, Tidak ada buku yang bisa diambil." Apabila pengguna memilih nomor 3, pengguna dapat melihat buku yang terakhir kali dimasukkan. Apabila pengguna memilih nomor 4, pengguna dapat melihat semua isi buku, berurutan dari bawah hingga atas. dan terakhir, pengguna dapat keluar dengan memilih nomor 5.

Link Presentasi : https://youtu.be/b1UjlVjHbP8
