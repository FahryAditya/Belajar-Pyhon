# ============================================
# 🧩 LATIHAN LIST PYTHON
# ============================================
# Tipe Data: LIST
# List adalah kumpulan data yang dapat menyimpan banyak nilai sekaligus.
# Nilainya bisa diubah, dihapus, dan ditambahkan.

# ============================================
# 1️⃣ LIST PUBLIC FIGURE
# ============================================

# 🔹 Proses 1: Membuat list dengan 5 nama public figure
nama_public_figure = ["Rafi Ahmad", "Maudy Ayunda", "Rossa", "Vincent Rompies", "David Beckham"]
print("Data awal public figure:", nama_public_figure)

# 🔹 Proses 2: Menampilkan nama pertama dan terakhir
# akses elemen list dengan indeks [0] dan [-1]
nama_pertama = nama_public_figure[0]
nama_terakhir = nama_public_figure[-1]
print("Nama pertama:", nama_pertama)
print("Nama terakhir:", nama_terakhir)

# 🔹 Proses 3: Mengganti elemen list
# Ganti nama di indeks ke-2 (Rossa) menjadi "Agnes Mo"
nama_public_figure[2] = "Agnes Mo"
print("List setelah diubah:", nama_public_figure)

# 🔹 Proses 4: Menampilkan tipe data
print("Tipe data variabel 'nama_public_figure':", type(nama_public_figure))


# ============================================
# 2️⃣ LIST MAKANAN & DESSERT FAVORIT
# ============================================

# 🔹 Proses 1: Membuat dua list berisi data makanan & dessert
nama_makanan_favorit = ["rendang", "bakso", "mie ayam", "popmie", "steak", "ice cream"]
nama_dessert_favorit = ["pudding", "parfait", "omelete", "crepes", "waffles"]

print("\nData awal:")
print("Makanan favorit:", nama_makanan_favorit)
print("Dessert favorit:", nama_dessert_favorit)

# 🔹 Proses 2: Menambahkan elemen baru
# Tambahkan "chocolate" di awal dan "strawberry" di akhir list dessert
nama_dessert_favorit.insert(0, "chocolate")   # tambah di awal
nama_dessert_favorit.append("strawberry")     # tambah di akhir
print("\nSetelah menambah chocolate & strawberry di dessert:")
print("Dessert favorit:", nama_dessert_favorit)

# 🔹 Proses 3: Memindahkan data antar list
# Hapus 'ice cream' dari makanan dan pindahkan ke dessert
nama_makanan_favorit.remove("ice cream")
nama_dessert_favorit.append("ice cream")

print("\nSetelah memindahkan 'ice cream' ke dessert:")
print("Makanan favorit:", nama_makanan_favorit)
print("Dessert favorit:", nama_dessert_favorit)

# 🔹 Proses 4: Pindahkan 'omelete' dari dessert ke makanan
nama_dessert_favorit.remove("omelete")
nama_makanan_favorit.append("omelete")

print("\nSetelah memindahkan 'omelete' ke makanan:")
print("Makanan favorit:", nama_makanan_favorit)
print("Dessert favorit:", nama_dessert_favorit)

# 🔹 Proses 5: Menampilkan tipe data
print("\nTipe data variabel 'nama_makanan_favorit':", type(nama_makanan_favorit))
print("Tipe data variabel 'nama_dessert_favorit':", type(nama_dessert_favorit))


# ============================================
# 📊 RANGKUMAN PROSES
# ============================================
"""
📘 PENJELASAN LANGKAH DEMI LANGKAH

1️⃣ MEMBUAT DATA LIST
   - nama_public_figure = ["Rafi Ahmad", "Maudy Ayunda", "Rossa", "Vincent Rompies", "David Beckham"]
   - nama_makanan_favorit = ["rendang", "bakso", "mie ayam", "popmie", "steak", "ice cream"]
   - nama_dessert_favorit = ["pudding", "parfait", "omelete", "crepes", "waffles"]

2️⃣ AKSES DATA
   - Gunakan indeks [0] untuk data pertama
   - Gunakan indeks [-1] untuk data terakhir

3️⃣ MENGUBAH DATA
   - nama_public_figure[2] = "Agnes Mo" → mengganti Rossa jadi Agnes Mo

4️⃣ MENAMBAH DATA
   - insert(0, "chocolate") → tambah di awal list
   - append("strawberry") → tambah di akhir list

5️⃣ MENGHAPUS DAN MEMINDAHKAN DATA
   - remove("ice cream") → hapus dari list makanan
   - append("ice cream") → tambahkan ke list dessert

6️⃣ MENAMPILKAN TIPE DATA
   - Semua variabel menggunakan tipe: <class 'list'>

✅ Hasil akhir:
   Makanan favorit: ['rendang', 'bakso', 'mie ayam', 'popmie', 'steak', 'omelete']
   Dessert favorit: ['chocolate', 'pudding', 'parfait', 'crepes', 'waffles', 'strawberry', 'ice cream']
"""
