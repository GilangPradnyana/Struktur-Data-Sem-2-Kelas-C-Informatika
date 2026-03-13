import statistics  # untuk mean (rata-rata)
import matplotlib.pyplot as plt

# =====================================
# 1. Input 10 nilai mahasiswa
# =====================================
nilai = []

print("Masukkan nilai 10 mahasiswa (0-100):")
for i in range(1, 11):
    while True:
        try:
            n = float(input(f"Nilai mahasiswa ke-{i}: "))
            if 0 <= n <= 100:
                nilai.append(n)
                break
            else:
                print("Nilai harus antara 0 sampai 100!")
        except ValueError:
            print("Masukkan angka yang valid!")


# 2 & 3 & 4 - Proses data


# Nilai tertinggi & terendah
nilai_max = max(nilai)
nilai_min = min(nilai)

# Rata-rata
rata_rata = statistics.mean(nilai)
# atau: rata_rata = sum(nilai) / len(nilai)


lulus = sum(1 for n in nilai if n >= 60)
tidak_lulus = 10 - lulus


# Output hasil


print("\n" + "="*50)
print("HASIL PENGELOLAAN NILAI MAHASISWA")
print("="*50)
print(f"Semua nilai       : {nilai}")
print(f"Nilai tertinggi    : {nilai_max}")
print(f"Nilai terendah     : {nilai_min}")
print(f"Rata-rata kelas    : {rata_rata:.2f}")
print(f"Jumlah lulus       : {lulus} orang ({lulus/10*100:.1f}%)")
print(f"Jumlah tidak lulus : {tidak_lulus} orang")
print("="*50 + "\n")

# 5. Grafik nilai tertinggi & terendah + rata-rata

plt.figure(figsize=(8, 5))

# Bar untuk max, min, rata-rata
kategori = ['Terendah', 'Rata-rata', 'Tertinggi']
nilai_grafik = [nilai_min, rata_rata, nilai_max]

bars = plt.bar(kategori, nilai_grafik, color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
plt.ylim(0, 100)
plt.title('Ringkasan Nilai Kelas (Min - Avg - Max)', fontsize=14)
plt.ylabel('Nilai')

# Tambah nilai di atas bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1.5, f'{yval:.1f}',
             ha='center', va='bottom', fontsize=11)

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

