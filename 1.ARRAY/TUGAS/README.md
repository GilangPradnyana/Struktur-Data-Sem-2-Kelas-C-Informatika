# Sistem Pengelolaan Nilai Mahasiswa Sederhana

Program Python sederhana untuk mengelola nilai 10 mahasiswa menggunakan **array** (list di Python). Program ini mencakup input nilai, perhitungan statistik dasar, dan visualisasi grafik menggunakan matplotlib.

1. Penjelasan Konsep Array

**Array** adalah struktur data yang digunakan untuk menyimpan kumpulan elemen dengan **tipe data yang sama** dalam lokasi memori yang berurutan . Dalam Python, array paling umum diimplementasikan menggunakan tipe data **list**.

Dalam program ini, saya menggunakan **list** (`nilai = []`) sebagai array satu dimensi untuk menyimpan nilai mahasiswa. Karakteristik utama yang dimanfaatkan:

- Dinamis → bisa menambah elemen dengan `.append()` 
- Diakses dengan indeks → `nilai[0]`, `nilai[3]`
- Iterasi mudah→ bisa menggunakan `for n in nilai:` 
- Built-in functions → `max()`, `min()`, `sum()`, `len()` 

Kelebihan penggunaan list sebagai array di program ini:
- Mudah ditambah/dibaca
- Mendukung operasi statistik sederhana tanpa library tambahan (kecuali rata-rata)
- Cocok untuk data jumlah kecil hingga sedang 

Kekurangan (jika skalanya besar):
- Operasi pencarian max/min/rata-rata tetap O(n)
- Tidak se-efisien array statis di bahasa seperti C/C++ untuk akses sangat cepat

## 2. Screenshot Hasil Eksekusi



### Input nilai
![Input nilai mahasiswa](assets/input-nilai.png)

### Output teks di terminal
![Hasil output teks](assets/output-teks.png)

### Grafik bar (Min – Avg – Max)
![Grafik ringkasan nilai](assets/grafik-bar-min-avg-max.png)


## 3. Analisis Kompleksitas

| Operasi                        | Metode yang digunakan              | Kompleksitas Waktu | Kompleksitas Ruang | Keterangan                                      |
|--------------------------------|-------------------------------------|----------------------|----------------------|--------------------------------------------------|
| Input 10 nilai                 | loop + `append`                     | O(1)                | O(n)                | n = 10 (konstan)                                 |
| Mencari nilai maksimum         | `max(nilai)`                        | O(n)                | O(1)                | Harus scan seluruh elemen                        |
| Mencari nilai minimum          | `min(nilai)`                        | O(n)                | O(1)                | Sama seperti max                                 |
| Menghitung rata-rata           | `statistics.mean()`                 | O(n)                | O(1)                | Memerlukan penjumlahan semua elemen              |
| Menghitung jumlah mahasiswa lulus | generator expression + `sum()`   | O(n)                | O(1)                | Linear scan                                      |
| Menampilkan output teks        | `print()`                           | O(n)                | O(1)                | —                                                |
| Membuat grafik bar             | matplotlib (rendering)              | O(1) untuk data kecil | O(1)              | Kompleksitas dominan di rendering, bukan data    |
| **Keseluruhan program**        | —                                   | **O(n)**            | **O(n)**            | n = 10 → praktis konstan                         |

**Kesimpulan**: Program sangat efisien untuk skala kecil (10 mahasiswa). Jika jumlah mahasiswa menjadi jutaan, saya bisa optimasi dengan struktur data yang lebih baik (misal heap untuk max/min cepat), tapi untuk kasus ini sudah sangat memadai.

4. Refleksi Pembelajaran

Melalui proyek ini saya belajar beberapa hal penting:

1. **Pemahaman array/list di Python**  
   List sangat fleksibel dan powerful untuk pemula, tapi saya  menyadari batasannya jika data sangat besar.

2. Input validation  
   Menggunakan `try-except` dan loop `while` untuk memastikan input valid sangat penting agar program tidak crash.

3. Pemisahan logika  
   Memisahkan bagian input, proses, output, dan visualisasi membuat kode lebih mudah dibaca dan dimodifikasi.

4. Visualisasi data  
   Grafik sederhana dengan matplotlib membantu memahami distribusi nilai jauh lebih cepat dibandingkan hanya angka.

5. Kesadaran kompleksitas  
   Meskipun n kecil, saya mulai terbiasa berpikir tentang Big-O bahkan pada program sederhana.

Hal yang ingin saya tingkatkan di proyek selanjutnya:
- Membuat input jumlah mahasiswa menjadi dinamis (bukan fix 10)
- Menyimpan data ke file (CSV/JSON)
- Menambahkan fitur pencarian mahasiswa berdasarkan nilai tertentu
- Mengimplementasikan max/min tanpa fungsi built-in (loop manual) untuk latihan lebih dalam

  
Dibuat oleh: I Putu Gilang Pradnyana:2501010067 
---
