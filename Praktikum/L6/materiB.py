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
    "kulit normal": (
        ["G001", "G002" "G003", "G004", "G005", "G006", "G011"],
        [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
    ),
    "kulit bermiyak": (
        ["G007", "G008", "G009", "G016"],
        [0.8, 0.8, 0.8, 0.8],
    ),
    "kulit kering": (
        ["G001", "G005", "G010", "G011", "G012"],
        [0.6, 0.6, 0.8, 0.6, 0.6],
    ),
    "kulit kombinasi": (
        ["G007", "G014", "G015", "G016", "G017"],
        [0.6, 0.4, 0.6, 0.4, 0.6],
    ),
    "kulit sensitif": (
        ["G012", "G018", "G019", "G020"],
        [0.8, 0.8, 0.8, 0.8],
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
    "GOO5": 0.6,
    "G018": 0.8,
    "G019": 0.8,
    "G019": 0.8,
}
cf = hitung_nilai_cf(input_user)
print("Hasil Diagnosa :", cf)
