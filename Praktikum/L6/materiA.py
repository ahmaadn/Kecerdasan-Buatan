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
    cf_penyakit = 0.0
    nm_penyakit = ""

    for P, (GejalaP, CFP) in penyakit.items():
        # Inisialisasi nilai CF kombinasi
        cf_kombinasi = 0.0

        # Hitung CF kombinasi untuk setiap gejala
        for G, cf_user in gejala_cf.items():
            # Hitung CF
            if G in GejalaP:
                for gp in GejalaP:
                    i = 0
                    if gp == G:
                        cf_gejala = CFP[i] * cf_user
                    i = i + 1
            else:
                cf_gejala = 0.0

            # Hitung CF kombinasi
            cf_kombinasi = cf_kombinasi + (1 - cf_kombinasi) * cf_gejala

        # mencari nilai CF Penyakit
        if cf_kombinasi > cf_penyakit:
            cf_penyakit = max(cf_penyakit, cf_kombinasi)
            nm_penyakit = P

    return nm_penyakit, cf_penyakit


# Contoh penggunaan
input_user = {
    "batuk": 0.2,
    "demam": 0.6,
    "pilek": 0.8,
    "sakit_tenggorokan": 0.2,
    "bersin": 0.6,
}
cf = hitung_nilai_cf(input_user)
print("Hasil Diagnosa :", cf)
