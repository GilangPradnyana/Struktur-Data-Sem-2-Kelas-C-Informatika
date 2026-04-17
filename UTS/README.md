# Sistem Antrian Printer Menggunakan Queue (Linked List)

**Project UTS Mata Kuliah Struktur Data**  
**Semester Genap 2025/2026**

## Deskripsi Proyek
Proyek ini merupakan implementasi **Sistem Antrian Printer** berbasis **Queue** menggunakan **Linked List**. Sistem ini mensimulasikan proses antrian dokumen yang akan dicetak di laboratorium komputer atau kantor, dengan menerapkan prinsip **FIFO (First In First Out)**.

Pengguna dapat menambahkan dokumen ke antrian, melihat dokumen yang akan dicetak berikutnya, mencetak dokumen (dequeue), serta melihat seluruh daftar antrian saat ini.

## Anggota Kelompok

| Nama Lengkap                  | NIM          | Peran              |
|-------------------------------|--------------|--------------------|
| I Putu Gilang Pradnyana       | 2501010067 | Koordinator / Developer |
| Petrus K Sanexsel Das SA      | 2501010346   | Developer          |


## Fitur yang Diimplementasikan

- **Enqueue** : Menambahkan dokumen baru ke belakang antrian
- **Dequeue** : Mencetak (menghapus) dokumen dari depan antrian
- **Peek**    : Melihat dokumen yang akan dicetak berikutnya tanpa menghapus
- **Display** : Menampilkan seluruh dokumen dalam antrian
- Implementasi menggunakan **Linked List** (bukan Array)

## Teknologi yang Digunakan
- Python 3
- Struktur Data: **Singly Linked List** untuk implementasi Queue
- Prinsip: **FIFO (First In First Out)**

## Cara Menjalankan Program

1. Clone repository ini:
   ```bash
   git clone https://github.com/username/repo-kamu.git 



1. Rumusan Masalah dan Solusi
Rumusan Masalah:

Bagaimana Queue dapat digunakan untuk mengelola antrian dokumen printer secara teratur agar tidak terjadi kekacauan dalam proses pencetakan?
Bagaimana implementasi Linked List pada Queue dapat meningkatkan fleksibilitas dan efisiensi dibandingkan penggunaan array statis dalam mengelola antrian yang dinamis?
Bagaimana sebuah sistem antrian printer mampu menyelesaikan masalah antrian yang tidak teratur, lama menunggu, dan sulitnya melacak dokumen yang sedang diproses di laboratorium komputer?

Solusi yang Ditawarkan:
Sistem Antrian Printer yang dibangun menggunakan struktur data Queue berbasis Linked List menawarkan solusi yang efektif untuk permasalahan di atas. Sistem ini menerapkan prinsip FIFO (First In First Out) sehingga dokumen yang masuk pertama akan dicetak terlebih dahulu. Penggunaan Linked List memungkinkan penambahan dan penghapusan dokumen secara dinamis tanpa batas ukuran tetap, sehingga lebih fleksibel dibandingkan array. Sistem ini juga menyediakan fitur enqueue, dequeue, peek, dan display yang memudahkan pengguna dalam mengelola antrian secara real-time.

2. Landasan Teori
Struktur data merupakan cara untuk mengorganisir, menyimpan, dan mengelola data agar dapat diakses dan dimanipulasi secara efisien. Menurut Cormen et al. (2009), struktur data adalah dasar dari semua algoritma yang efisien karena pemilihan struktur data yang tepat akan sangat memengaruhi kinerja suatu program.
Queue adalah salah satu struktur data linier yang menerapkan konsep FIFO (First In First Out), artinya elemen yang pertama masuk akan menjadi elemen pertama yang keluar. Queue banyak digunakan dalam sistem antrian seperti antrian pelanggan, antrian proses di sistem operasi, dan antrian printer. Dalam implementasi Queue, terdapat dua operasi utama yaitu Enqueue (menambahkan elemen) dan Dequeue (menghapus elemen).
Implementasi Queue dapat dilakukan dengan dua cara utama, yaitu menggunakan Array dan Linked List. Implementasi dengan Array memiliki kelemahan yaitu ukuran yang statis dan memerlukan shifting elemen saat antrian penuh atau kosong. Sedangkan implementasi menggunakan Linked List bersifat dinamis, tidak memerlukan ukuran awal, serta operasi Enqueue dan Dequeue dapat dilakukan dengan kompleksitas waktu O(1) jika pointer rear dan front dikelola dengan baik.
Dalam proyek ini, Queue diimplementasikan menggunakan Singly Linked List karena memberikan fleksibilitas yang tinggi dalam pengelolaan memori dan ukuran antrian yang tidak terbatas, sesuai dengan kebutuhan sistem antrian printer yang dapat berubah-ubah sewaktu-waktu.
Daftar Pustaka (Minimal 3 Sumber):

Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). Introduction to Algorithms (3rd ed.). MIT Press.
Weiss, M. A. (2014). Data Structures and Algorithm Analysis in C++ (4th ed.). Pearson.
Sedgewick, R., & Wayne, K. (2011). Algorithms (4th ed.). Addison-Wesley.

(Kamu boleh mengganti atau menambah sumber sesuai kebutuhan. Jika dosen meminta sumber berbahasa Indonesia, beri tahu saya agar saya ubah.)

3. Desain Sistem dan Implementasi
Diagram Proses Sistem
Alur Sistem Antrian Printer:
textInput:
- Nama File
- Jumlah Halaman
- Nama Pengguna

          ↓

     ENQUEUE
(Menambahkan dokumen ke belakang antrian)

          ↓

     DISPLAY
(Melihat seluruh antrian)

          ↓

     PEEK
(Melihat dokumen berikutnya)

          ↓

     DEQUEUE
(Mencetak dokumen dari depan antrian)

          ↓

     Output:
- Status pencetakan
- Daftar antrian terkini
Pseudocode
textClass Node
    data: nama_file, jumlah_halaman, nama_pengguna
    next: pointer ke node berikutnya

Class PrinterQueue
    front: pointer ke depan antrian
    rear: pointer ke belakang antrian
    size: integer

    Procedure Enqueue(nama_file, jumlah_halaman, nama_pengguna)
        buat node baru
        jika antrian kosong maka
            front = rear = node baru
        else
            rear.next = node baru
            rear = node baru
        size = size + 1

    Procedure Dequeue()
        jika antrian kosong maka return null
        dokumen_dicetak = front
        front = front.next
        jika front == null maka rear = null
        size = size - 1
        return dokumen_dicetak

    Procedure Peek()
        jika antrian kosong maka return null
        return front

    Procedure Display()
        tampilkan semua node dari front sampai null
Implementasi Program
Sistem telah diimplementasikan menggunakan bahasa Python dengan struktur data Singly Linked List. File utama program bernama printer_queue.py. Seluruh operasi utama (Enqueue, Dequeue, Peek, Display) telah berhasil diimplementasikan sesuai dengan teori Queue.

