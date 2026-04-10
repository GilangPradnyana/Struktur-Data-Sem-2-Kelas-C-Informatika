# StrukturData-Q1-[NIM Anda]-[Nama Anda]-[Kelas Anda]

**Quis 1 Struktur Data: Array dan Linked List**  
**Materi:** Dasar Teori & Implementasi Konseptual

**Nama:** [I PUTU GILANG PRADNYANA]  
**NIM:** [2501010067]  
**Kelas:** [C]

---

### 1. Karakteristik Memori dan Akses Data

Operasi akses elemen pada **Array** dapat dilakukan dalam waktu **konstan O(1)** karena array menyimpan elemen-elemennya secara **kontigu** (berdekatan) di dalam memori.

Alamat memori elemen ke-i dapat dihitung langsung dengan rumus:  
**Alamat = Base Address + (i × ukuran tipe data)**

Komputer hanya perlu menghitung alamat tersebut lalu langsung mengambil data dari lokasi memori tersebut, tanpa perlu melakukan perulangan atau penelusuran.

Sebaliknya, pada **Singly Linked List**, elemen-elemen disimpan di lokasi memori yang **non-kontigu** (tersebar). Setiap node hanya menyimpan data dan pointer ke node berikutnya. Untuk mengakses elemen ke-i, kita harus mulai dari head dan mengikuti pointer sebanyak i kali (traversal). Oleh karena itu, waktu akses rata-rata dan terburuk adalah **O(n)**.

**Ringkasan:**

- Array → Memori kontinu → Akses langsung via indeks (O(1))
- Singly Linked List → Memori non-kontinu → Harus traversal (O(n))

---

### 2. Analisis Efisiensi Operasi Manipulasi

**Linked List** jauh lebih unggul dibandingkan **Array** untuk operasi **penyisipan (insertion)** dan **penghapusan (deletion)** ketika posisi penyisipan/penghapusan sudah diketahui (misalnya kita memiliki pointer langsung ke node tersebut).

**Alasan teoritis:**

- **Array**:
  - Penyisipan/deletion di tengah atau awal memerlukan **shifting** semua elemen setelah posisi tersebut.
  - Kompleksitas waktu: **O(n)** (paling buruk).
  - Ukuran array biasanya tetap (kecuali dynamic array).

- **Linked List** (Singly/Doubly):
  - Hanya perlu mengubah beberapa **pointer** (next/prev).
  - Tidak perlu shifting elemen.
  - Kompleksitas waktu: **O(1)** jika pointer ke posisi sudah ada, atau **O(n)** jika harus mencari posisinya terlebih dahulu.

**Kesimpulan:** Linked List lebih diunggulkan ketika aplikasi sering melakukan banyak operasi insert/delete di posisi acak/tengah, terutama jika ukuran data sering berubah secara dinamis.

---

### 3. Konsep Doubly Linked List

**Struktur anatomi sebuah node** pada Doubly Linked List:

```text
+----------+----------+----------+
|   Prev   |   Data   |   Next   |
+----------+----------+----------+


Setiap node memiliki tiga field:

Data → nilai yang disimpan
Next → pointer ke node berikutnya
Prev → pointer ke node sebelumnya

Dampak keberadaan pointer tambahan (Prev):

Penggunaan memori: Lebih besar dibandingkan Singly Linked List karena setiap node membutuhkan tambahan satu pointer (biasanya 4 atau 8 byte tergantung arsitektur). Sehingga konsumsi memori meningkat sekitar 2x lipat untuk pointer saja.
Fleksibilitas penelusuran:
Memungkinkan traversal dua arah (forward dan backward) dengan mudah.
Penghapusan node menjadi lebih mudah karena kita bisa langsung mengakses node sebelumnya tanpa perlu traversal dari head.
Operasi delete dan insert di tengah lebih efisien dan simpel dibandingkan Singly Linked List.

4. Mekanisme Circular Linked List
Perbedaan utama Circular Linked List dengan Linked List biasa (Linear):

Pada Circular Linked List, pointer next dari node terakhir menunjuk kembali ke node pertama (head), membentuk lingkaran tertutup.
Tidak ada node yang memiliki pointer next bernilai NULL.

Keunggulan teoritis:

Tidak ada "akhir" yang jelas, sehingga penelusuran dapat dilakukan secara terus-menerus.
Lebih mudah untuk implementasi struktur data yang bersifat berulang (circular buffer).

Contoh use case:

Round-Robin Scheduling di sistem operasi (penjadwalan proses CPU secara bergantian).
Playlist musik yang berputar otomatis (setelah lagu terakhir kembali ke lagu pertama).
Implementasi antrian yang bersifat circular (Circular Queue) untuk menghemat memori.


5. Array Dinamis di Python
Python list diimplementasikan secara internal sebagai Dynamic Array (atau Over-allocating Array).
Mekanisme ketika Dynamic Array kehabisan kapasitas saat append():

Python tidak langsung menambah ukuran 1 per 1 (karena akan sangat mahal).
Ketika kapasitas penuh, Python mengalokasikan array baru dengan ukuran yang lebih besar (biasanya 1.125x atau sekitar 25%–50% lebih besar dari ukuran sebelumnya, tergantung implementasi CPython).
Semua elemen dari array lama disalin ke array baru.
Array lama dihapus (garbage collected).
Operasi append() baru kemudian dilakukan pada array yang sudah lebih besar.

Analisis kompleksitas:

Operasi append() rata-rata adalah O(1) (amortized constant time).
Kadang-kadang (saat resizing) menjadi O(n), tetapi karena resizing jarang terjadi, rata-rata tetap efisien.

Strategi over-allocation ini adalah trade-off antara efisiensi waktu dan penggunaan memori.
```
