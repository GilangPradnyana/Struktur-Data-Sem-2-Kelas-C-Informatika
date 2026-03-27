# Membuat class Node untuk menyimpan data dan pointer next
class Node:
    def __init__(self, data):
        self.data = data      # Menyimpan nomor antrian pasien
        self.next = None      # Pointer ke node berikutnya


# Membuat class Single Linked List
class SingleLinkedList:
    def __init__(self):
        self.head = None      # Head adalah node pertama (awal antrian)

    # Algoritma Insert di Akhir (Pasien Datang)
    def insert_akhir(self, data):
        new_node = Node(data)     # 1. Buat node baru

        if self.head is None:     # 2. Jika list kosong
            self.head = new_node  #    Node baru menjadi head
            return

        temp = self.head          # 3. Mulai dari head
        while temp.next:          # 4. Loop sampai node terakhir
            temp = temp.next

        temp.next = new_node      # 5. Node terakhir menunjuk ke node baru

    # Algoritma Traversal (Admin Melihat Daftar Antrian)
    def tampilkan(self):
        temp = self.head          # 1. Mulai dari head

        if temp is None:          # 2. Jika list kosong
            print("Antrian kosong")
            return

        print("Daftar Antrian Pasien:")
        while temp:               # 3. Loop sampai node terakhir
            print("Nomor Antrian:", temp.data)  # 4. Tampilkan data
            temp = temp.next      # 5. Pindah ke node berikutnya


# Program Utama (Menu Sistem Antrian)
antrian = SingleLinkedList()      # Membuat objek linked list

while True:
    print("\n=== Sistem Antrian Pasien ===")
    print("1. Tambah Antrian Pasien")
    print("2. Lihat Daftar Antrian")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nomor = input("Masukkan nomor antrian pasien: ")
        antrian.insert_akhir(nomor)   # Memanggil fungsi insert di akhir

    elif pilihan == "2":
        antrian.tampilkan()           # Memanggil fungsi traversal

    elif pilihan == "3":
        print("Program selesai")
        break

    else:
        print("Menu tidak valid")