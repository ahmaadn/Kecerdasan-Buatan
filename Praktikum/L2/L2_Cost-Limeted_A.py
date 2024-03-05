import heapq


def cost_limited_a(awal, tujuan, cost_limited=1000):
    antrian = []  #
    heapq.heappush(antrian, (0, awal)) # niiai f untuk `awal` adalah 0
    explorasi = {awal: None} # node yang telah melakukkan explorasi
    g_explorasi = {awal: 0} # nilai g untuk setiap node yang telah melakukan explorasi
    
    while antrian:
        # mancari nili f terkecil dari sebuah antrian
        f, titik = heapq.heappop(antrian)

        # cek jiak `titik` sama dengan `tujuan`
        if titik == tujuan:
            return explorasi

        # kerena menerapkan cost-limited, maka nilai `f` harus lebih kecil dari `cost_limited`
        # pencarian akan dihentikan jika nilai `f` lebih besar dari `cost_limited`.
        if f > cost_limited:
            return None

        # lakukan iterasi setiap titik yang saling terhubung.
        for titi_baru, jarak in graph[titik].items():
            new_g = g_explorasi[titik] + jarak

            # cek setiap titik baru apakah sebuah tujuan
            if titi_baru == tujuan:
                g_explorasi[titi_baru] = new_g
                explorasi[titi_baru] = titik
                return explorasi

            # cek jika titik baru mempunyai nilai g atau
            # titik baru mempunyai niai g yang lebih kecil dengan nilai g sebelumnya
            if titi_baru not in g_explorasi or new_g < g_explorasi[titi_baru]:

                # simpan nilai g untuk titik baru
                g_explorasi[titi_baru] = new_g
                new_h = heuristic[titi_baru]
                new_f = new_g + new_h

                # melakukan pembatasan niai f
                if new_f > cost_limited:
                    continue

                # simpan titik baru ke antrian dengan nilai f
                heapq.heappush(antrian, (new_f, titi_baru))

                # simpan untuk titik baru yang telah melakukan explorasi
                explorasi[titi_baru] = titik

def print_jalan(tujuan, jalan):
    # mencari titik besarkan informasi yang telah 
    path = []
    titik = tujuan
    while titik != None:
        path.append(titik)
        titik = jalan[titik]
    path.reverse()
    
    print(" -> ".join(path))


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

# heuristic = perkiraan biaya dari titk ke goal
heuristic = {
    'asahan': 0,
    "balige": 250,
    "parapat": 245,
    "raya": 230,
    "siantar": 145,
    "tebing": 120,
    "perdagangan": 85,
    "sipirok": 78,
    "tanjung": 81,
    "binjai": 100,
    "medan": 88,
    "kisaran": 66,
}

awal = 'parapat'
tujuan = 'asahan'
cost = 300

result = cost_limited_a(awal, tujuan, cost)

if result:
    print("jalanan terpendek dari {} ke {}")
    print_jalan("asahan", result)
else:
    print("Jalanan terpendek tidak di temukan")
