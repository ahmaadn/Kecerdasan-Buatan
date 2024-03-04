import random
import copy

def get_input(label):
    try:
        return int(input(f"Goal untuk {label}, default ('n')? "))
    except ValueError:
        return 'n'

def is_valid(state, goal):
    x, y = state
    gx, gy = goal

    if ((not isinstance(gx, int) and y == gy) 
        or (gx == x and not isinstance(gy, int)) 
        or ((x, y) == (gx, gy))
        or (not isinstance(gx, int) and not isinstance(gy, int))
    ):
        return True

    return False

def recursife_random_search(initial, goal, n=0):
    if is_valid(initial, goal):
            return initial
    
    func_rule = random.choice(rules)
    proir_initial = copy.copy(initial)
    index_rule = rules.index(func_rule) + 1
    initial = func_rule(*initial)
    
    print(f"{n}: Aturan ke-{index_rule} : {proir_initial} -> {initial}")
    
    return recursife_random_search(initial, goal, n+1)

def random_search(initial, goal):
    if is_valid(initial, goal):
        return initial
    n = 1
    while True:
        func_rule = random.choice(rules)
        proir_initial = copy.copy(initial)
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

gx = get_input("x")
gy = get_input("y")
x, y = recursife_random_search((0, 0), (gx, gy))
