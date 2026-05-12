def binary_search(nilai_tugas, n, target):
    l = 0
    r = n - 1
    pos = -1
    while l <= r:
        m = l + (r - l) // 2
        print(f"Median: {m}, nilai_tugas: {nilai_tugas[m]}")
        if nilai_tugas[m] == target:
            pos = m
            break
        elif nilai_tugas[m] < target:
            print("Mencari Nilai Tugas di bagian kanan....")
            l = m + 1
        else:
            print("Mencari Nilai Tugas di bagian kiri....")
            r = m - 1
    return pos

def main():
    nilai_tugas = [30, 34, 35, 39, 40, 42, 44, 45, 47, 50, 51, 52, 55, 57, 58, 60, 65, 70, 73, 75, 80, 88, 90, 95, 99]
    n = len(nilai_tugas)
    print(f"Nilai Tugas Satu Semester : {nilai_tugas}")
    while True:
        try:
            target = int(input("Masukkan Nilai Tugas Yang Ingin Anda Cari: "))
            break
        except ValueError:
            print("Input Tidak Valid, Silahkan Masukkan Angka")
    pos = binary_search(nilai_tugas, n, target)
    if pos != -1:
        print(f"Nilai Ditemukan pada indeks ke-{pos}")
    else:
        print("Nilai Yang Dicari Tidak Ditemukan")

if __name__ == "__main__":
    main()