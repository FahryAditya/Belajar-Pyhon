# ================================
# 🧩 EXERCISE LIST PYTHON INTERAKTIF
# ================================

# 📘 Tipe Data yang digunakan: LIST
# List adalah tipe data yang dapat menyimpan banyak nilai dalam satu variabel.
# Elemen di dalam list dapat diubah, dihapus, dan ditambahkan.


# ================================
# 1️⃣ LIST NAMA PUBLIC FIGURE
# ================================

print("=== EXERCISE 1: NAMA PUBLIC FIGURE ===")

# 🔹 Input data dari pengguna
# proses: membuat list kosong, lalu menambahkan elemen dengan append()
nama_public_figure = []   # tipe data list
jumlah = int(input("Berapa jumlah public figure yang ingin kamu masukkan? "))

for i in range(jumlah):
    nama = input(f"Masukkan nama public figure ke-{i+1}: ")
    nama_public_figure.append(nama)

# 🔹 Output awal
print("\n📋 List public figure yang kamu buat:")
print(nama_public_figure)

# 🔹 a. Cetak nama pertama dan terakhir
print("\n➡️ Nama pertama:", nama_public_figure[0])
print("➡️ Nama terakhir:", nama_public_figure[-1])

# 🔹 b. Ganti nama di indeks ke-2 (index 2) dengan "Agnes Mo"
# proses: mengubah elemen list menggunakan indeks
if len(nama_public_figure) > 2:
    nama_public_figure[2] = "Agnes Mo"

# 🔹 c. Tampilkan seluruh isi list setelah diubah
print("\n✅ List setelah diubah:")
print(nama_public_figure)

# 🔹 Tampilkan tipe data
print("\n🔎 Tipe data variabel 'nama_public_figure':", type(nama_public_figure))



# ================================
# 2️⃣ LIST MAKANAN DAN DESSERT FAVORIT
# ================================

print("\n=== EXERCISE 2: MAKANAN & DESSERT FAVORIT ===")

# 🔹 Input makanan favorit
nama_makanan_favorit = []  # tipe data list
jumlah_makanan = int(input("Berapa makanan favorit yang ingin kamu masukkan? "))

for i in range(jumlah_makanan):
    makanan = input(f"Masukkan makanan favorit ke-{i+1}: ")
    nama_makanan_favorit.append(makanan)

# 🔹 Input dessert favorit
nama_dessert_favorit = []  # tipe data list
jumlah_dessert = int(input("\nBerapa dessert favorit yang ingin kamu masukkan? "))

for i in range(jumlah_dessert):
    dessert = input(f"Masukkan dessert favorit ke-{i+1}: ")
    nama_dessert_favorit.append(dessert)

# 🔹 Output sebelum diubah
print("\n📋 Sebelum diubah:")
print("Makanan favorit:", nama_makanan_favorit)
print("Dessert favorit:", nama_dessert_favorit)

# ---------------------------------
# 🔸 PROSES PERUBAHAN DATA
# ---------------------------------

# a. Tambahkan chocolate dan strawberry di awal dan akhir list dessert
# proses: insert() dan append()
nama_dessert_favorit.insert(0, "chocolate")  # menambah di awal
nama_dessert_favorit.append("strawberry")    # menambah di akhir

# b. Hapus 'ice cream' dari list makanan lalu pindahkan ke dessert
# proses: remove() untuk menghapus, append() untuk menambahkan ke list lain
if "ice cream" in nama_makanan_favorit:
    nama_makanan_favorit.remove("ice cream")
    nama_dessert_favorit.append("ice cream")

# c. Hapus 'omelete' dari dessert lalu pindahkan ke makanan
if "omelete" in nama_dessert_favorit:
    nama_dessert_favorit.remove("omelete")
    nama_makanan_favorit.append("omelete")

# ---------------------------------
# 🔹 Output setelah diubah
# ---------------------------------
print("\n✅ Setelah diubah:")
print("Makanan favorit:", nama_makanan_favorit)
print("Dessert favorit:", nama_dessert_favorit)

# 🔹 Tampilkan tipe data variabel
print("\n🔎 Tipe data variabel 'nama_makanan_favorit':", type(nama_makanan_favorit))
print("🔎 Tipe data variabel 'nama_dessert_favorit':", type(nama_dessert_favorit))

# ================================
# 💡 PENJELASAN PROSES
# ================================
"""
1️⃣ Proses input:
   - Menggunakan perulangan for untuk menambahkan data ke dalam list.
   - Setiap input dimasukkan dengan metode append().

2️⃣ Proses manipulasi data:
   - Akses data list pakai indeks, contoh: list[0], list[-1].
   - Ubah isi list dengan assignment langsung, contoh: list[2] = "Agnes Mo".
   - Tambah data pakai append() (akhir) dan insert() (awal).
   - Hapus data pakai remove().
   - Pindah data dengan cara remove() dari satu list, lalu append() ke list lain.

3️⃣ Tipe data:
   - Semua list menggunakan tipe data <class 'list'>.

4️⃣ Output:
   - Ditampilkan dalam bentuk list berisi string (nama, makanan, dessert).
"""
