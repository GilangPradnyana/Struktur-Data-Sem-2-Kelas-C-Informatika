# StrukturData-Q1-[2501010067]- [I PUTU GILANG PRADNYANA]- [C]

**Quis 1 Struktur Data: Array dan Linked List**  
**Materi:** Dasar Teori & Implementasi Konseptual

**Nama:** [I PUTU GILANG PRADNYANA]  
**NIM:** [2501010067]  
**Kelas:** [C]

---

### 1. Karakteristik Memori dan Akses Data

Operasi akses elemen pada **Array** dapat dilakukan dalam waktu **konstan O(1)** karena semua elemen array disimpan secara **kontigu** (berurutan dan berdekatan) di dalam memori.

Alamat memori suatu elemen dapat dihitung langsung menggunakan rumus:  
**Alamat = Base Address + (indeks × ukuran tipe data)**

Sehingga komputer dapat langsung melompat ke lokasi memori tersebut tanpa harus menelusuri elemen lain.

Sedangkan pada **Singly Linked List**, elemen-elemen disimpan di lokasi memori yang **non-kontigu** (tersebar di berbagai tempat). Setiap node hanya memiliki pointer ke node berikutnya. Untuk mengakses elemen ke-i, kita harus mulai dari head dan mengikuti pointer satu per satu (traversal). Oleh karena itu, waktu akses adalah **O(n)**.

**Kesimpulan:**

- Array → memori kontinu → akses langsung via indeks (O(1))
- Singly Linked List → memori non-kontinu → harus traversal (O(n))

---

### 2. Analisis Efisiensi Operasi Manipulasi

**Linked List** lebih diunggulkan dibandingkan **Array** untuk operasi **penyisipan (insertion)** dan **penghapusan (deletion)** ketika posisi yang diinginkan sudah diketahui (kita memiliki pointer ke node tersebut).

**Alasan teoritis:**

- Pada **Array**, penyisipan atau penghapusan di tengah/awal memerlukan **shifting** semua elemen setelah posisi tersebut agar tetap kontigu. Kompleksitas waktu: **O(n)**.
- Pada **Linked List**, kita hanya perlu mengubah beberapa pointer (`next`/`prev`). Tidak ada proses shifting elemen. Jika pointer ke posisi sudah tersedia, kompleksitas waktu menjadi **O(1)**.

Oleh karena itu, Linked List sangat efisien untuk aplikasi yang sering melakukan insert dan delete di posisi acak atau tengah daftar, terutama ketika ukuran data sering berubah secara dinamis.

---

### 3. Konsep Doubly Linked List

**Struktur anatomi sebuah node** pada Doubly Linked List terdiri dari tiga bagian:

- **Prev** : pointer ke node sebelumnya
- **Data** : nilai yang disimpan
- **Next** : pointer ke node berikutnya

**Dampak pointer tambahan (Prev):**

- **Penggunaan memori**: Lebih besar dibandingkan Singly Linked List karena setiap node membutuhkan satu pointer tambahan (biasanya +4 atau +8 byte). Konsumsi memori meningkat sekitar dua kali lipat hanya untuk pointer saja.
- **Fleksibilitas penelusuran**: Memungkinkan traversal **dua arah** (maju dan mundur) dengan mudah. Operasi penghapusan dan penyisipan di tengah menjadi lebih sederhana dan efisien karena kita bisa langsung mengakses node sebelumnya tanpa harus traversal dari head.

---

### 4. Mekanisme Circular Linked List

**Perbedaan utama** Circular Linked List dengan Linked List biasa adalah:

Pada Circular Linked List, pointer `next` dari node **terakhir** menunjuk kembali ke node **pertama** (head), sehingga membentuk sebuah **lingkaran tertutup**. Tidak ada pointer yang bernilai `NULL`.

**Contoh use case:**
Struktur ini sangat efektif digunakan pada **Round-Robin Scheduling** di sistem operasi, di mana proses CPU dijadwalkan secara bergantian secara terus-menerus. Selain itu, cocok juga untuk implementasi **playlist musik** yang otomatis berulang (setelah lagu terakhir kembali ke lagu pertama).

---

### 5. Array Dinamis di Python

Python `list` diimplementasikan secara internal sebagai **Dynamic Array** (over-allocating array).

**Mekanisme saat Dynamic Array kehabisan kapasitas saat operasi `append()`:**

1. Python mengalokasikan **array baru** dengan ukuran yang lebih besar (biasanya sekitar 1.125x atau bertambah 25%–50% dari ukuran sebelumnya).
2. Semua elemen dari array lama **disalin** ke array baru.
3. Array lama dihapus dari memori.
4. Operasi `append()` kemudian dilakukan pada array yang sudah lebih besar.

Meskipun sesekali operasi ini membutuhkan waktu **O(n)** (saat resizing), secara keseluruhan `append()` memiliki kompleksitas **amortized O(1)** karena operasi resizing jarang terjadi.

---

**Catatan:**  
Jawaban di atas telah difokuskan pada konsep dasar struktur data serta analisis kompleksitas waktu dan ruang sesuai instruksi quis.

Repository ini dibuat untuk memenuhi tugas Quis 1 Struktur Data.
