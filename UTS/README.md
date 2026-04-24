# SISTEM ANTRIAN PRINTER (PRINT QUEUE)

**Project UTS – Struktur Data**  
**Semester Genap 2025/2026**  
**Mata Kuliah:** Struktur Data  
**Tema:** Penerapan Queue dan Stack  
**Studi Kasus:** Sistem Antrian Printer (Print Queue)

---

## 1. Rumusan Masalah dan Solusi

### Rumusan Masalah

1. Bagaimana queue dapat digunakan untuk mengelola antrian dokumen pada sistem printer agar dokumen diproses secara terurut dan adil sesuai prinsip FIFO?
2. Bagaimana implementasi linked list dapat meningkatkan fleksibilitas dan efisiensi dibandingkan array statis dalam pengelolaan antrian printer yang dinamis?
3. Bagaimana sistem antrian printer mampu menyelesaikan masalah nyata pada dunia teknologi, yaitu penumpukan dokumen dan ketidakteraturan urutan pencetakan?

### Solusi yang Ditawarkan

Sistem ini dirancang sebagai **Print Queue Simulator** yang menggunakan **Queue berbasis Linked List**. Setiap dokumen (nama file + jumlah halaman) dimasukkan ke dalam antrian secara FIFO. Sistem menyediakan operasi standar Queue (Enqueue, Dequeue, Peek, Display) sehingga printer dapat memproses dokumen satu per satu sesuai urutan kedatangan. Dengan Linked List, ukuran antrian menjadi dinamis (tidak terbatas) dan hemat memori.

---

## 2. Landasan Teori

Struktur data adalah cara menyimpan dan mengorganisir data agar dapat diakses dan dimanipulasi secara efisien. Menurut Goodrich dkk. (2013), struktur data merupakan fondasi penting dalam pengembangan perangkat lunak karena memengaruhi kinerja algoritma.

Queue adalah struktur data linier yang menerapkan prinsip **FIFO (First In First Out)**, yaitu elemen yang pertama masuk akan keluar pertama kali. Queue banyak digunakan pada sistem antrian seperti printer, antrian pelayanan, dan buffer data. Sebaliknya, Stack menerapkan prinsip **LIFO (Last In First Out)**.

Dalam implementasi Queue, terdapat dua pendekatan utama: menggunakan **Array** (ukuran tetap) dan **Linked List** (ukuran dinamis). Linked List lebih fleksibel karena tidak memerlukan alokasi memori statis di awal dan memungkinkan penambahan serta penghapusan elemen dengan kompleksitas waktu O(1) pada operasi Enqueue dan Dequeue (Cormen et al., 2009).

Referensi ilmiah yang digunakan:

1. Goodrich, M. T., Tamassia, R., & Goldwasser, M. H. (2013). _Data Structures and Algorithms in Python_. Wiley.
2. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). _Introduction to Algorithms_ (3rd ed.). MIT Press.
3. Sedgewick, R., & Wayne, K. (2011). _Algorithms_ (4th ed.). Addison-Wesley.

---

## 3. Desain Sistem dan Implementasi

### Alur Sistem (Input → Proses → Output)

- **Input**: Nama file dokumen dan jumlah halaman yang dimasukkan pengguna.
- **Proses**: Dokumen masuk ke Queue (Enqueue) → Antrian disimpan menggunakan Linked List → Dokumen diproses sesuai FIFO (Dequeue).
- **Output**: Dokumen yang sedang dicetak, daftar antrian lengkap dalam bentuk tabel, dan informasi dokumen berikutnya.

### Desain Sistem (Pseudocode)

```pseudocode
Class PrintQueue:
    front, rear ← null
    ukuran ← 0

    Enqueue(nama, halaman):
        buat node baru
        jika queue kosong:
            front = rear = node baru
        else:
            rear.next = node baru
            rear = node baru
        ukuran += 1

    Dequeue():
        jika queue kosong: return
        cetak dokumen front
        front = front.next
        ukuran -= 1

    Peek(): tampilkan front
    Display(): tampilkan semua node dalam bentuk tabel
```
