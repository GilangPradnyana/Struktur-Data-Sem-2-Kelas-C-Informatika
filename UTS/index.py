# =============================================
# SISTEM ANTRIAN PRINTER (PRINT QUEUE)
# Menggunakan Queue dengan Linked List
# =============================================

class Document:
    def __init__(self, nama_file, jumlah_halaman):
        self.nama_file = nama_file
        self.jumlah_halaman = jumlah_halaman
        self.next = None


class PrintQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.ukuran = 0

    def is_empty(self):
        return self.front is None

    # ENQUEUE - Tambah dokumen ke antrian
    def enqueue(self, nama_file, jumlah_halaman):
        new_doc = Document(nama_file, jumlah_halaman)
        
        if self.is_empty():
            self.front = self.rear = new_doc
        else:
            self.rear.next = new_doc
            self.rear = new_doc
        
        self.ukuran += 1
        print(f"✅ Dokumen '{nama_file}' ({jumlah_halaman} halaman) berhasil ditambahkan ke antrian.")

    # DEQUEUE - Proses/cetak dokumen berikutnya
    def dequeue(self):
        if self.is_empty():
            print("❌ Antrian kosong! Tidak ada dokumen yang bisa dicetak.")
            return
        
        temp = self.front
        print(f"🖨️  Sedang mencetak: '{temp.nama_file}' ({temp.jumlah_halaman} halaman)...")
        
        self.front = self.front.next
        self.ukuran -= 1
        
        if self.front is None:
            self.rear = None

    # PEEK - Lihat dokumen yang akan dicetak berikutnya
    def peek(self):
        if self.is_empty():
            print("❌ Antrian kosong!")
        else:
            print(f"📌 Dokumen berikutnya yang akan dicetak: '{self.front.nama_file}' "
                  f"({self.front.jumlah_halaman} halaman)")

    # DISPLAY - Tampilkan seluruh antrian dalam bentuk TABEL
    def display(self):
        if self.is_empty():
            print("📭 Antrian printer kosong.")
            return
        
        # Kumpulkan semua data dulu untuk menghitung lebar kolom
        data = []
        current = self.front
        nomor = 1
        max_nama = 0
        
        while current:
            nama = current.nama_file
            if len(nama) > max_nama:
                max_nama = len(nama)
            data.append((nomor, nama, current.jumlah_halaman))
            current = current.next
            nomor += 1
        
        # Tentukan lebar kolom
        lebar_nomor = 4
        lebar_nama = max(max_nama, 15)   # minimal 15 karakter
        lebar_halaman = 12
        
        # Garis pemisah
        garis = "+" + "-" * lebar_nomor + "+" + "-" * lebar_nama + "+" + "-" * lebar_halaman + "+"
        
        print("\n" + garis)
        print(f"| {'No':<{lebar_nomor-1}} | {'Nama File':<{lebar_nama}} | {'Jumlah Halaman':<{lebar_halaman-1}} |")
        print(garis)
        
        for no, nama, halaman in data:
            print(f"| {no:<{lebar_nomor-1}} | {nama:<{lebar_nama}} | {halaman:>{lebar_halaman-1}} |")
        
        print(garis)
        print(f"Total dokumen dalam antrian : {self.ukuran}")
        print(garis)

    # Bersihkan memory saat keluar
    def clear(self):
        while not self.is_empty():
            self.dequeue()


# =============================================
# MAIN PROGRAM - MENU
# =============================================
def main():
    printer = PrintQueue()
    
    print("=====================================")
    print("   SISTEM ANTRIAN PRINTER (QUEUE)    ")
    print("=====================================\n")

    while True:
        print("\n=== MENU ===")
        print("1. Tambah Dokumen (Enqueue)")
        print("2. Cetak Dokumen (Dequeue)")
        print("3. Lihat Dokumen Berikutnya (Peek)")
        print("4. Tampilkan Seluruh Antrian (Display)")
        print("5. Keluar")
        
        try:
            pilihan = int(input("Pilih menu (1-5): "))
        except ValueError:
            print("❌ Masukkan angka yang valid!")
            continue

        if pilihan == 1:
            nama_file = input("Masukkan nama file: ")
            try:
                halaman = int(input("Masukkan jumlah halaman: "))
                printer.enqueue(nama_file, halaman)
            except ValueError:
                print("❌ Jumlah halaman harus berupa angka!")
        
        elif pilihan == 2:
            printer.dequeue()
        
        elif pilihan == 3:
            printer.peek()
        
        elif pilihan == 4:
            printer.display()
        
        elif pilihan == 5:
            print("Terima kasih telah menggunakan Sistem Antrian Printer!")
            printer.clear()
            break
        
        else:
            print("❌ Pilihan tidak valid! Silakan pilih 1-5.")

if __name__ == "__main__":
    main()