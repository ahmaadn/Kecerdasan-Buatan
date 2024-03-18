import random
import math

def rute_acak(awal, tujuan):
    """fungsi untuk mencari jalur acak dan jumlah jarak"""
    
    # jumalah rute yang tersedia
    n = len(graph.keys())
    
    while True:
        jalur = awal
        rute = [jalur]

        # lakukan iterasi sebanyak n
        for _ in range(n):
            # mendapkan rute baru bedasarkan dengan jalur saat ini
            rute_baru = list(graph[jalur].keys())
            jalur_baru = random.choice(rute_baru)

            if jalur_baru in rute:
                continue

            jalur = jalur_baru
            rute.append(jalur_baru)

        # cek jika akhir dari rute adakah tujuan
        if rute[-1] == tujuan:
            return rute

def hitung_panjang_rute(rute):
    """fungsi untuk menghitung panjang rute
    """

    cost = 0
    for n in range(len(rute)-1):
        cost += graph[rute[n]][rute[n+1]]
    return cost

def simulated_analing(awal, tujuan, max_iterasi, suhu, alpha):
    """fungsi untuk mencari solusi rute terbaik menggunakan simulated analing
    """
    
    # tetapkan solusi terbaik untuk saat ini
    solusi_terbaik = rute_acak(awal, tujuan)
    rute_sekarang = solusi_terbaik

    # lakukan itersi sebanyak `max_iterasi`
    for _ in range(max_iterasi):
        
        # dapatkan rute baru untuk setiap iterasi
        rute_baru = rute_acak(awal, tujuan)
        
        # delta panjang panjang rute 
        delta_panjang_jalur = hitung_panjang_rute(rute_baru) - hitung_panjang_rute(rute_sekarang)

        # cek jika delta pakna 
        if delta_panjang_jalur < 0:
            rute_sekarang = rute_baru
        else:
            # rumus simulated_analing
            p = random.random()
            if p < math.exp(-delta_panjang_jalur / suhu):
                rute_sekarang = rute_baru

        # cek jika rute sekarang lebih baik dari solusi terbaik
        if hitung_panjang_rute(rute_sekarang) < hitung_panjang_rute(solusi_terbaik):
            solusi_terbaik = rute_sekarang
    
        suhu *= alpha

    return solusi_terbaik

def get_input(label, valid=None, default=None, res=str):
    """Mendapatkan input dari user"""
    try:
        result = res(input(label))
        if valid and result in valid or not valid and result:
            return result
    except ValueError:
        pass
    
    if default:
        return default

    return get_input(label, valid, default, res)

graph = {
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

awal = get_input("Awal tujuan default ('parapat')? ", valid=list(graph.keys()), default='parapat')
tujuan = get_input("Awal tujuan default ('asahan')? ", valid=list(graph.keys()), default='asahan')
max_iteration = get_input("input max iterasi: default (1000)? ", default=1000, res=int) # type: ignore
suhu = get_input("input suhu: default (100) ? ", default=100, res=int) # type: ignore
alpha = get_input("input alpha:  default (0.9) ? ", default=0.9, res=float) # type: ignore

rute = simulated_analing(awal, tujuan, max_iteration, suhu, alpha)
print("\n\n")
print(f"Rute terbaik dari {awal} le {tujuan} adalah: ")
print(" -> ".join(rute))
print(f"Dengan panjang jalan : {hitung_panjang_rute(rute)}")