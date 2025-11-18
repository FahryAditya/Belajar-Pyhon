Siswa_SMK_kelas_11 = [
    {"nama": "Rudy",  "umur": 17, "noTelp": "089922331111", "GolDarah": "O"},
    {"nama": "Alex",  "umur": 16, "noTelp": "089612341234", "GolDarah": "A"},
    {"nama": "Fiena", "umur": 16, "noTelp": "087855667744", "GolDarah": "O"},
    {"nama": "Revita","umur": 15, "noTelp": "085552421346", "GolDarah": "B"},
    {"nama": "Levi",  "umur": 15, "noTelp": "091123231456", "GolDarah": "AB"}
]

def find_siswa(nama):
    for siswa in Siswa_SMK_kelas_11:
        if siswa["nama"] == nama:
            return siswa

alex = find_siswa("Alex")
revita = find_siswa("Revita")
rudy = find_siswa("Rudy")
levi = find_siswa("Levi")

temp_no = alex["noTelp"]
alex["noTelp"] = revita["noTelp"]
revita["noTelp"] = temp_no

temp_umur = rudy["umur"]
rudy["umur"] = levi["umur"]
levi["umur"] = temp_umur

for siswa in Siswa_SMK_kelas_11:
    del siswa["GolDarah"]

alamat_mapping = {
    "Rudy":  "Jalan Ahmad Yani no 17 Balikpapan Kota",
    "Alex":  "Jalan Jendral Sudirman no 1 Balikpapan Selatan",
    "Fiena": "Jalan Mulawarman no 11 RT 23 Balikpapan Timur",
    "Revita":"Jalan M.T. Haryono no 54 RT 63 Balikpapan Selatan",
    "Levi":  "Perumahan Bukit Damai Indah Blok AA no 53 RT 12 Balikpapan"
}

for siswa in Siswa_SMK_kelas_11:
    siswa["alamat"] = alamat_mapping[siswa["nama"]]

for siswa in Siswa_SMK_kelas_11:
    print(siswa)
