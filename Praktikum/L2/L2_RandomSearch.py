import random

def get_input(label, min_num):
    try:
        result =  int(input(f"Goal untuk {label}, default ('n')? "))
        if result >= 0 and result <= min_num:
            return result
        return get_input(label, min_num)
    except ValueError:
        return 'n'

def is_valid(state, goal):
    x, y = state
    gx, gy = goal

    if ((not isinstance(gx, int) and (y == gy))
        or ((x == gx) and not isinstance(gy, int))
        or ((x, y) == (gx, gy))
        or (not isinstance(gx, int) and not isinstance(gy, int))
    ):
        return True

    return False

def recursive_random_search(initial, goal, n=0):
    if is_valid(initial, goal):
        return initial

    func_rule = random.choice(rules)
    proir_initial = initial[:]
    index_rule = rules.index(func_rule) + 1
    initial = func_rule(*initial)

    print(f"{n}: Aturan ke-{index_rule} : {proir_initial} -> {initial}")

    return recursive_random_search(initial, goal, n+1)

def random_search(initial, goal):
    if is_valid(initial, goal):
        return initial

    n = 0
    while True:
        func_rule = random.choice(rules)
        proir_initial = initial[:]
        index_rule = rules.index(func_rule) + 1
        initial = func_rule(*initial)
        print(f"{n}: Aturan ke-{index_rule} : {proir_initial} -> {initial}")

        if is_valid(initial, goal):
            return initial
        n += 1

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

min_x = 4
max_y = 3
gx = get_input("x", min_x)
gy = get_input("y", max_y)
x, y = random_search((0, 0), (gx, gy))
print(f"Akhir: {(x, y)}")
