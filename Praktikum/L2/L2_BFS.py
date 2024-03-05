from collections import deque

# Keadaan awal
initial_state = (0, 0)

# Fungsi untuk mengecek apakah keadaan sudah merupakan goal state
def is_goal_state(state):
    return state[1] == 2

# Algoritma BFS untuk mencari solusi
def bfs(initial_state):
    visited = set()  # Set untuk menyimpan keadaan yang sudah dikunjungi
    index_rules = []
    queue = deque([(initial_state, [], [])])  # Antrian berisi keadaan dan jalur yang sudah dilalui

    while queue:
        state, path, path_rules = queue.popleft()
        visited.add(state)

        if is_goal_state(state):
            return path + [state], path_rules

        for rule in range(1, 9):
            func_rule = rules[rule - 1]
            new_state = func_rule(*state)

            if new_state not in visited:
                queue.append((new_state, path + [state], path_rules + [rule]))

    return None  # Jika tidak ditemukan solusi

rules = [
    lambda x, y : (4, y) if x < 4 else (x, y), # 1
    lambda x, y : (x, 3) if y < 3 else (x, y), # 2
    lambda x, y : (0, y) if x > 0 else (x, y), # 3
    lambda x, y : (x, 0) if y > 0 else (x, y), # 4
    lambda x, y : (4, y - (4-x)) if x + y >= 4 and y > 0 else (x, y), # 5
    lambda x, y : (x - (3-y), 3) if x + y >= 3 and x > 0 else (x, y), # 6
    lambda x, y : (x + y, 0) if x + y <= 4 and y > 0 else (x, y), # 7
    lambda x, y : (0, y + x)  if x + y <= 3 and x > 0 else (x, y), # 8
]

# Cari solusi menggunakan BFS
solution = bfs(initial_state)

# Tampilkan solusi
if solution:
    print("Langkah-langkah untuk mencapai 2 galon air di jerigen y:")
    for step, (state, rule) in enumerate(zip(*solution)):
        print(f"{step}: Atruran ke-{rule}: Langkah {step + 1}: Jerigen x = {state[0]} galon, Jerigen y = {state[1]} galon")
else:
    print("Tidak ditemukan solusi.")
