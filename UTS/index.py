# =====================================================
# SISTEM ANTRIAN PRINTER - Menggunakan Queue + Linked List
# Project UTS Struktur Data - Semester Genap 2025/2026
# Studi Kasus: Sistem Antrian Printer di Laboratorium Komputer
# =====================================================


class Node:
    """
    Kelas Node untuk Linked List.
    Setiap node merepresentasikan satu dokumen print.
    """
    def __init__(self, nama_file, jumlah_halaman, nama_pengguna):
        self.nama_file = nama_file          # Nama file yang akan dicetak
        self.jumlah_halaman = jumlah_halaman  # Jumlah halaman
        self.nama_pengguna = nama_pengguna    # Nama mahasiswa / pengguna
        self.next = None                    # Pointer ke dokumen berikutnya


class PrinterQueue:
    """
    Kelas utama untuk mengelola Antrian Printer menggunakan Queue (Linked List).
    Mengikuti prinsip FIFO (First In First Out).
    """
    
    def __init__(self):
        self.front = None   # Depan antrian (akan dilayani pertama)
        self.rear = None    # Belakang antrian (tempat menambah dokumen baru)
        self.size = 0       # Jumlah dokumen dalam antrian

    def is_empty(self):
        """Cek apakah antrian kosong"""
        return self.front is None

    def enqueue(self, nama_file, jumlah_halaman, nama_pengguna):
        """
        Menambahkan dokumen baru ke belakang antrian (Enqueue).
        Operasi ini O(1) karena kita menyimpan pointer rear.
        """
        new_node = Node(nama_file, jumlah_halaman, nama_pengguna)
        
        if self.is_empty():
            # Jika antrian kosong, front dan rear menunjuk ke node yang sama
            self.front = new_node
            self.rear = new_node
        else:
            # Tambahkan di belakang
            self.rear.next = new_node
            self.rear = new_node
        
        self.size += 1
        print(f"✓ Dokumen '{nama_file}' dari {nama_pengguna} berhasil masuk antrian.")

    def dequeue(self):
        """
        Mengambil dan menghapus dokumen dari depan antrian (Dequeue).
        Dokumen ini yang sedang dicetak.
        Operasi ini O(1).
        """
        if self.is_empty():
            print("❌ Antrian printer kosong! Tidak ada dokumen yang bisa dicetak.")
            return None
        
        printed_doc = self.front
        self.front = self.front.next
        
        # Jika setelah dequeue antrian menjadi kosong
        if self.front is None:
            self.rear = None
        
        self.size -= 1
        
        print(f"🖨️  Sedang mencetak: {printed_doc.nama_file} "
              f"({printed_doc.jumlah_halaman} halaman) - {printed_doc.nama_pengguna}")
        
        return printed_doc

    def peek(self):
        """
        Melihat dokumen di depan antrian tanpa menghapusnya (Peek).
        """
        if self.is_empty():
            print("❌ Antrian kosong.")
            return None
        
        print(f"📄 Dokumen berikutnya yang akan dicetak: "
              f"{self.front.nama_file} ({self.front.jumlah_halaman} halaman) "
              f"- {self.front.nama_pengguna}")
        return self.front

    def display(self):
        """
        Menampilkan semua dokumen dalam antrian saat ini.
        """
        if self.is_empty():
            print("📭 Antrian printer saat ini kosong.")
            return
        
        print("\n" + "="*60)
        print("             DAFTAR ANTRIAN PRINTER SAAT INI")
        print("="*60)
        print(f"{'No':<3} {'Pengguna':<15} {'File':<20} {'Halaman':<8}")
        print("-"*60)
        
        current = self.front
        count = 1
        while current:
            print(f"{count:<3} {current.nama_pengguna:<15} "
                  f"{current.nama_file:<20} {current.jumlah_halaman:<8}")
            current = current.next
            count += 1
        
        print(f"\nTotal dokumen dalam antrian: {self.size}")
        print("="*60)
