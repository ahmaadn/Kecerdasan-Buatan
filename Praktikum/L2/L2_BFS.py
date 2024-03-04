from collections import deque

# Fungsi untuk menghasilkan keadaan baru berdasarkan aturan produksi
def apply_rule(state, rule):
    x, y = state
    if rule == 1:
        return (4, y)
    elif rule == 2:
        return (x, 3)
    elif rule == 3:
        return (0, y)
    elif rule == 4:
        return (x, 0)
    elif rule == 5:
        return (4, y - (4-x))
    elif rule == 6:
        return (x - (3-y), 3)
    elif rule == 7:
        return (x+y, 0)
    elif rule == 8:
        return (0, y+x)

# Fungsi untuk mengecek apakah keadaan sudah merupakan goal state
def is_goal_state(state):
    return state[1] == 2

# Algoritma BFS untuk mencari solusi
def bfs(initial_state):
    visited = set()  # Set untuk menyimpan keadaan yang sudah dikunjungi
    queue = deque([(initial_state, [])])  # Antrian berisi keadaan dan jalur yang sudah dilalui

    while queue:
        state, path = queue.popleft()
        visited.add(state)

        if is_goal_state(state):
            return path + [state]

        for rule in range(1, 9):
            new_state = apply_rule(state, rule)
            if new_state not in visited:
                queue.append((new_state, path + [state]))

    return None  # Jika tidak ditemukan solusi

# Keadaan awal
initial_state = (0, 0)

# Cari solusi menggunakan BFS
solution = bfs(initial_state)

# Tampilkan solusi
if solution:
    print("Langkah-langkah untuk mencapai 2 galon air di jerigen B:")
    for step, state in enumerate(solution):
        print(f"Langkah {step + 1}: Jerigen A = {state[0]} galon, Jerigen B = {state[1]} galon")
else:
    print("Tidak ditemukan solusi.")
