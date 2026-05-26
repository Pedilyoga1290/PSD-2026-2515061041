class Node:
    def __init__(self, id_barang, nama_barang, stok):
        self.id_barang = id_barang
        self.nama_barang = nama_barang
        self.stok = stok
        self.left = None
        self.right = None

class BSTInv:
    def __init__(self):
        self.root = None

    def insert_node(self, root, id_barang, nama_barang, stok):
        if root is None:
            return Node(id_barang, nama_barang, stok)
        if id_barang < root.id_barang:
            root.left = self.insert_node(root.left, id_barang, nama_barang, stok)
        elif id_barang > root.id_barang:
            root.right = self.insert_node(root.right, id_barang, nama_barang, stok)
        else:
            print(f"Peringatan: Barang dengan ID {id_barang} sudah ada!")
        return root

    def insert(self, id_barang, nama_barang, stok):
        self.root = self.insert_node(self.root, id_barang, nama_barang, stok)

    def search_node(self, root, id_barang):
        if root is None:
            return None
        if root.id_barang == id_barang:
            return root
        if id_barang < root.id_barang:
            return self.search_node(root.left, id_barang)
        return self.search_node(root.right, id_barang)

    def delete_node(self, root, key):
        if root is None:
            return None
        if key < root.id_barang:
            root.left = self.delete_node(root.left, key)
        elif key > root.id_barang:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                successor = self.find_min_node(root.right)
                root.id_barang = successor.id_barang
                root.nama_barang = successor.nama_barang
                root.stok = successor.stok
                root.right = self.delete_node(root.right, successor.id_barang)
        return root

    def delete(self, key):
        self.root = self.delete_node(self.root, key)

    def find_min_node(self, root):
        current = root
        while current is not None and current.left is not None:
            current = current.left
        return current
        
    def search(self, id_barang):
        return self.search_node(self.root, id_barang)
    
    def update_stok(self, id_barang, jumlah_perubahan):
        node = self.search(id_barang)
        if node:
            if node.stok + jumlah_perubahan < 0:
                print("Gagal: Stok tidak boleh minus!")
            else:
                node.stok += jumlah_perubahan
                print(f"Sukses: Stok {node.nama_barang} diperbarui menjadi {node.stok}.")
        else:
            print("Gagal: Barang tidak ditemukan!")

    def inorder_display(self, root):
        if root is None:
            return
        self.inorder_display(root.left)
        print(f"| ID: {root.id_barang:<5} | Nama: {root.nama_barang:<15} | Stok: {root.stok:<5} |")
        self.inorder_display(root.right)

    def count_jenis_barang(self, root):
        if root is None:
            return 0
        return 1 + self.count_jenis_barang(root.left) + self.count_jenis_barang(root.right)

    def sum_total_stok(self, root):
        if root is None:
            return 0
        return root.stok + self.sum_total_stok(root.left) + self.sum_total_stok(root.right)


def main():
    gudang = BSTInv()
    
    gudang.insert(105, "Laptop", 12)
    gudang.insert(102, "Mouse", 50)
    gudang.insert(108, "Keyboard", 30)

    pilih = 0
    while pilih != 8:
        print("\n=== SISTEM MANAJEMEN PERSEDIAAN BARANG ===")
        print("1. Tambah Barang Baru")
        print("2. Cari Data Barang")
        print("3. Tampilkan Semua Barang (Urut ID)")
        print("4. Update Stok Barang (Masuk/Keluar)")
        print("5. Laporan Jumlah Jenis Barang")
        print("6. Laporan Total Keseluruhan Stok")
        print("7. Hapus Barang")
        print("8. Keluar")
        
        try:
            pilih = int(input("Pilih menu (1-8): "))
        except ValueError:
            print("Input tidak valid, masukkan angka!")
            continue
            
        if pilih == 1:
            try:
                id_brg = int(input("Masukkan ID Barang (Angka): "))
                nama = input("Masukkan Nama Barang: ")
                stok = int(input("Masukkan Jumlah Stok: "))
                gudang.insert(id_brg, nama, stok)
                print("Barang berhasil ditambahkan!")
            except ValueError:
                print("Input stok/ID harus berupa angka!")
                
        elif pilih == 2:
            try:
                id_brg = int(input("Masukkan ID Barang yang dicari: "))
                hasil = gudang.search(id_brg)
                if hasil:
                    print("\n--- Data Ditemukan ---")
                    print(f"ID Barang   : {hasil.id_barang}")
                    print(f"Nama Barang : {hasil.nama_barang}")
                    print(f"Sisa Stok   : {hasil.stok}")
                    print("----------------------")
                else:
                    print("Barang tidak ditemukan dalam sistem.")
            except ValueError:
                print("Input ID harus berupa angka!")
                
        elif pilih == 3:
            print("\n--- Daftar Barang di Gudang ---")
            gudang.inorder_display(gudang.root)
            print("-------------------------------")
            
        elif pilih == 4:
            try:
                id_brg = int(input("Masukkan ID Barang: "))
                print("Gunakan angka positif untuk barang MASUK, negatif (-) untuk barang KELUAR.")
                perubahan = int(input("Jumlah perubahan stok: "))
                gudang.update_stok(id_brg, perubahan)
            except ValueError:
                print("Input harus berupa angka!")
                
        elif pilih == 5:
            total_jenis = gudang.count_jenis_barang(gudang.root)
            print(f"Total terdapat {total_jenis} jenis barang (SKU) di gudang.")
            
        elif pilih == 6:
            total_stok = gudang.sum_total_stok(gudang.root)
            print(f"Total fisik keseluruhan barang di gudang adalah {total_stok} unit.")   

        elif pilih == 7:
            try:
                id_brg = int(input("Masukkan ID Barang yang akan dihapus: "))
                gudang.delete(id_brg)
                print(f"Barang dengan ID {id_brg} berhasil dihapus.")
            except ValueError:
                print("Input harus berupa angka!")
                
        elif pilih == 8:
            print("Sistem ditutup. Terima kasih!")
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()