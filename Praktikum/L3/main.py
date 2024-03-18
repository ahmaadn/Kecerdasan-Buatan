
# jarak tempuh / menit
# ketua : ahmad nur
# anggota 1 : yoga
# anggota 2 : dimas
# anggota 3 : ramadhan
# 1 menit == 350 meter
import random
import math


def rute_acak(awal, tujuan):
    titik = awal
    rute = [titik]

    # mendapatkan semua jalan yang harus di kunjungi
    kunjungan = list(graph.keys())
    
    # mengeluarkan titik awal dan tujuan
    kunjungan.pop(kunjungan.index(titik))
    kunjungan.pop(kunjungan.index(tujuan))

    while True:
        rute_baru = list(graph[titik].keys())
        titik_baru = random.choice(rute_baru)
        
        # titik yang dipilih sudah pernah dikunjungi        
        if titik_baru not in kunjungan:
            continue

        # menambahkan titik yang baru saja dikunjungi
        rute.append(titik_baru)
        kunjungan.pop(kunjungan.index(titik_baru))

        # semua kunujungan telah dikunjungi
        if not kunjungan:
            break

    rute.append(tujuan)
    return rute

def hitung_nilai_rute(rute):
    cost = 0
    for n in range(len(rute)-1):
        titik = rute[n]         # titik ke n 
        next_titik = rute[n+1]  # titik selanjutnya dari n

        # dapatkan jumlah rumah makan
        jml_makan = jumlah_rumah_makan[titik][next_titik]
        jarak = graph[titik][next_titik]
        
        # hitung total waktu yang ditempuh        
        cost += jarak + (jml_makan * 5)

    return cost

def simulated_analing(awal, tujuan, max_iterasi, suhu, alpha):
    """fungsi untuk mencari solusi rute terbaik menggunakan simulated analing
    """

    # tetapkan solusi terbaik untuk saat ini
    solusi_terbaik = rute_acak(awal, tujuan)
    rute_sekarang = solusi_terbaik

    # lakukan itersi sebanyak `max_iterasi`
    for i in range(max_iterasi):

        # dapatkan rute baru untuk setiap iterasi
        rute_baru = rute_acak(awal, tujuan)
        
        # delta panjang panjang rute 
        delta_panjang_jalur = hitung_nilai_rute(rute_baru) - hitung_nilai_rute(rute_sekarang)

        # cek jika delta pakna 
        if delta_panjang_jalur < 0:
            rute_sekarang = rute_baru
        else:
            # rumus simulated_analing
            p = random.random()
            if p < math.exp(-delta_panjang_jalur / suhu):
                rute_sekarang = rute_baru

        # cek jika rute sekarang lebih baik dari solusi terbaik
        if hitung_nilai_rute(rute_sekarang) < hitung_nilai_rute(solusi_terbaik):
            solusi_terbaik = rute_sekarang
        
        # debug
        print("")
        print(f"iter {i+1}")
        print(" -> ".join(rute_sekarang))
        print(f"Durasi perjalanan (menit): {hitung_nilai_rute(rute_sekarang)}")
    
        suhu *= alpha

    return rute_sekarang

graph = {
    'Kampus ITG': {"Rumah ketua": 29, 'anggota 1': 13, 'anggota 2': 21, 'anggota 3': 51},
    'Rumah ketua': {"Kampus ITG": 29, 'anggota 1': 38, 'anggota 2': 45, 'anggota 3': 78},
    "anggota 1": {'Kampus ITG': 13, 'Rumah ketua': 38, 'anggota 2': 10, 'anggota 3': 57},
    'anggota 2': {'Kampus ITG': 21, 'anggota 1': 10, 'rumah ketua': 45, 'anggota 3': 64},
    'anggota 3': {'Kampus ITG': 51, 'anggota 1': 57, 'anggota 2': 64, 'rumah ketua': 78}
}

# dari ketua ke setiap anggota
jumlah_rumah_makan = {
    'Kampus ITG': {"Rumah ketua": 50, 'anggota 1': 10, 'anggota 2': 13, 'anggota 3': 35},
    'Rumah ketua': {"Kampus ITG": 50, 'anggota 1': 24, 'anggota 2': 27, 'anggota 3': 83},
    "anggota 1": {'Kampus ITG': 10, 'Rumah ketua': 24, 'anggota 2': 3, 'anggota 3': 44},
    'anggota 2': {'Kampus ITG': 13, 'anggota 1': 3, 'rumah ketua': 27, 'anggota 3': 47},
    'anggota 3': {'Kampus ITG': 35, 'anggota 1': 44, 'anggota 2': 47, 'rumah ketua': 83}
}


awal = 'Rumah ketua'
tujuan = 'Kampus ITG'

rute = simulated_analing(awal, tujuan, 10, 100, 0.9)
print()
print()
print(f"Rute terbaik dari {awal} le {tujuan} adalah: ")
print(" -> ".join(rute))
print(f"Durasi perjalanan (menit): {hitung_nilai_rute(rute)}")