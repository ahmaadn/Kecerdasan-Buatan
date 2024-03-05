import random
import math

def hitung_panjang_jalur(rute, jarak):
    panjang_jalur = 0
    for i in range(len(rute) - 1):
        kota_awal = rute[i]
        kota_tujuan = rute[i + 1]
        if kota_awal in jarak and kota_tujuan in jarak[kota_awal]:
            panjang_jalur += jarak[kota_awal][kota_tujuan]
        else:
            # handle jika kota tidak ditemukan dalam kamus jarak
            print("Error: Tidak ditemukan jarak antara", kota_awal, "dan", kota_tujuan)
            return float('inf')  # mengembalikan nilai tak terhingga sebagai penanda kesalahan
    return panjang_jalur

def rute_acak(kota):
    rute = kota[:]
    random.shuffle(rute)
    return rute

def rute_perubahan(rute):
    rute_baru = rute[:]
    titik1 = random.randint(0, len(rute) - 1)
    titik2 = random.randint(0, len(rute) - 1)
    rute_baru[titik1], rute_baru[titik2] = rute_baru[titik2], rute_baru[titik1]
    return rute_baru

def simulated_annealing(jarak, suhu_awal, suhu_akhir, alpha):
    kota = list(jarak.keys())
    rute_sekarang = rute_acak(kota)
    panjang_jalur_sekarang = hitung_panjang_jalur(rute_sekarang, jarak)

    while suhu_awal > suhu_akhir:
        rute_baru = rute_perubahan(rute_sekarang)
        panjang_jalur_baru = hitung_panjang_jalur(rute_baru, jarak)

        delta_panjang_jalur = panjang_jalur_baru - panjang_jalur_sekarang
        if delta_panjang_jalur < 0 or random.random() < math.exp(-delta_panjang_jalur / suhu_awal):
            rute_sekarang = rute_baru
            panjang_jalur_sekarang = panjang_jalur_baru

        suhu_awal *= alpha

    return rute_sekarang, panjang_jalur_sekarang

# Contoh kasus: jarak antar kota
jarak_antar_kota = {
    'balige': {'tebing': 209, "siantar": 133, "parapat": 80},
    'tebing': {'balige': 209, "binjai": 98, "medan": 78, "perdagangan": 53, "siantar": 100},
    'siantar': {'balige': 133, 'tebing': 100, 'perdagangan': 59, 'raya': 101, 'parapat': 126},
    'parapat': {'balige': 80, 'siantar': 126, 'raya': 38},
    'binjai': {'tebing': 98, 'medan': 21},
    'perdagangan': {'tebing': 53, 'medan': 126, 'asahan': 86, 'sipirok': 49, 'raya': 166, 'siantar': 59},
    'raya': {'siantar': 101, 'perdagangan': 166, 'sipirok': 143, 'parapat': 38},
    'medan': {'binjai': 21, 'asahan': 88, 'perdagangan': 126, 'tebing': 78},
    'asahan': {'medan': 88, 'kisaran': 66, 'tanjung': 81, 'sipirok': 78, 'perdagangan': 86},
    'sipirok': {'asahan': 78, 'tanjung': 23, 'raya': 143, 'perdagangan': 49},
    'kisaran': {'asahan': 66, 'tanjung': 118},
    'tanjung': {'asahan': 81, 'kisaran': 118, 'sipirok': 23}
}

# Parameter Simulated Annealing
suhu_awal = 1000
suhu_akhir = 0.01
alpha = 0.99

# Panggil algoritma Simulated Annealing
rute_optimal, panjang_jalur_optimal = simulated_annealing(jarak_antar_kota, suhu_awal, suhu_akhir, alpha)

print("Rute Optimal:", rute_optimal)
print("Panjang Jalur Optimal:", panjang_jalur_optimal)
