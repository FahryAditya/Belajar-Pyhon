barang = {
    "kode": "B01",
    "nama_barang": "Kabel",
    "stok": 100,
    "lokasi": {"rak": "A1", "baris": 2}
}

# =========================
# A. Menampilkan lokasi barang
# =========================
nama = barang["nama_barang"]
rak = barang["lokasi"]["rak"]
baris = barang["lokasi"]["baris"]

print(f"Lokasi {nama} ada di Rak {rak} baris ke {baris}\n")

# =========================
# B. Update stok & menampilkan pesan
# =========================
pesanan = 3
barang["stok"] -= pesanan  # stok dikurangi pesanan
nama_upper = barang["nama_barang"].upper()

print(f"Selamat! Barang {nama_upper} anda sebanyak {pesanan} buah telah berhasil terjual.\n")
print(f"Sisa stok di Gudang adalah {barang['stok']}\n")

# =========================
# C. Update kode barang
# =========================
barang["kode"] = "A01"

# =========================
# FINAL DATA SETELAH UPDATE
# =========================
print("===== FINAL DATA SETELAH UPDATE =====")
print(f"Kode Barang  : {barang['kode']}")
print(f"Nama Barang  : {barang['nama_barang']}")
print(f"Stok Barang  : {barang['stok']}")
print(f"Lokasi Rak   : {barang['lokasi']['rak']}")
print(f"Baris Rak    : {barang['lokasi']['baris']}")
