def binary_search(nilai, n, target):
    l = 0
    r = n - 1
    pos = -1
    while l <= r:
        m = l + (r - l) // 2
        print(f"Median: {m}, nilai: {nilai[m]}")
        if nilai[m] == target:
            pos = m
            break
        elif nilai[m] < target:
            print("Mencari nilai di bagian kanan....")
            l = m + 1
        else:
            print("Mencari nilai di bagian kiri....")
            r = m - 1
    return pos

def main():
    nilai = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 90, 99]
    n = len(nilai)
    print(f"Nilai Yang Tersedia : {nilai}")
    while True:
        try:
            target = int(input("Masukkan nilai yang ingin dicari: "))
            break
        except ValueError:
            print("Invalid Input, Silahkan Masukkan Angka")
    pos = binary_search(nilai, n, target)
    if pos != -1:
        print(f"Ditemukan pada indeks ke-{pos}")
    else:
        print("Nilai tidak ditemukan")

if __name__ == "__main__":
    main()