# Fakta-fakta
gejala = {
    "batuk": True,
    "demam": True,
    "pilek": True,
    "sakit_tenggorokan": True,
    "bersin": True,
}
# Aturan/ CF Awal
penyakit = {
    "batuk": (["batuk", "sakit_tenggorokan"], [1.0, 0.6]),
    "flu_ringan": (["batuk", "demam", "pilek"], [0.4, 0.6, 0.8]),
    "flu_berat": (
        ["batuk", "demam", "pilek", "sakit_tenggorokan", "bersin"],
        [0.4, 0.6, 0.6, 0.4, 0.8],
    ),
}


# menghitung certainty factor
def hitung_nilai_cf(gejala_cf):
    diagnosa_penyakit = []  # Menyimpan diagnosa untuk setiap penyakit

    for P, (GejalaP, CFP) in penyakit.items():
        cf_kombinasi = 0.0

        for G, cf_user in gejala_cf.items():
            if G in GejalaP:
                for i, gp in enumerate(GejalaP):  # Memperbaiki iterasi
                    if gp == G:
                        cf_gejala = CFP[i] * cf_user

                cf_kombinasi = cf_kombinasi + (1 - cf_kombinasi) * cf_gejala
            else:
                cf_gejala = 0.0

        diagnosa_penyakit.append((P, cf_kombinasi))  # Menyimpan hasil diagnosa

    return diagnosa_penyakit


# Contoh penggunaan
input_user = {
    "batuk": 0.2,
    "demam": 0.6,
    "pilek": 0.8,
    "sakit_tenggorokan": 0.2,
    "bersin": 0.6,
}
daftar_diagnosa = hitung_nilai_cf(input_user)

# Cetak semua hasil diagnosa
print("Hasil Diagnosa:")
penyakit_tertinggi = None
cf_tertinggi = 0.0
for penyakit, cf in daftar_diagnosa:
    print(f"{penyakit}: CF = {cf}")
    if cf > cf_tertinggi:
        cf_tertinggi = cf
        penyakit_tertinggi = penyakit

# Cetak hasil diagnosa akhir (penyakit dengan CF tertinggi)
print("\nHasil Diagnosa Akhir:")
print(f"Penyakit dengan CF Tertinggi: {penyakit_tertinggi}, CF = {cf_tertinggi}")
