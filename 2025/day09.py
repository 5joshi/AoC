from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    cs = lmap(lambda x: tuple(ints(x)), d.splitlines())
    result = 0
    
    for x, y in it.combinations(cs, 2):
        result = max(result, (abs(x[0] - y[0]) + 1) * (abs(x[1] - y[1]) + 1))
    
    return result

def uirange(a, b):
    return range(min(a, b), max(a, b)+1)

def solve2(d):
    result = 0

    points = []
    rows, cols = set(), set()
    for line in d.splitlines():
        r, c = ints(line)
        points.append((r, c))
        rows.add(r)
        cols.add(c)
    
    row_indices = {r: 2*i for i, r in enumerate(sorted(rows))}
    col_indices = {c: 2*i for i, c in enumerate(sorted(cols))}

    new_points = [(row_indices[r], col_indices[c]) for (r, c) in points]
    boundary = set()
    for (r1, c1), (r2, c2) in windows(new_points + [new_points[0]], 2):
        boundary |= {(r, c) for r in uirange(r1, r2) for c in uirange(c1, c2)}
    
    grid = {(r, c) for r in range(-1, 2*len(rows)+1) for c in range(-1, 2*len(cols)+1)}
    outside = set()
    todo = [(-1, -1)]
    while todo:
        curr = todo.pop()
        if curr in outside: continue
        outside.add(curr)
        for delta in GRID_DELTA:
            new = tadd(curr, delta)
            if new in grid and new not in boundary:
                todo.append(new)
    
    for (ox, x), (oy, y) in it.combinations(zip(points, new_points), 2):
        area = (abs(ox[0] - oy[0]) + 1) * (abs(ox[1] - oy[1]) + 1)
        if all((r, c) not in outside for r in uirange(x[0], y[0]) for c in uirange(x[1], y[1])):
            result = max(result, area)
   
    return result
    

s = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3

""".strip()
s2 = """

""".strip()

if __name__ == '__main__':
    one, two, e1, e2, ex1, ex2, r1, r2 = get_solution_booleans(sys.argv)
            
    if e1 or ex1 or r1: print("PART 1")
    if e1 and s != "": print("Example Solution:", solve1(s))
    if ex1: print("Example 2 Solution:", solve1(s2))
    if r1: print("Actual Solution:", sol1 := solve1(inp))

    if e2 or ex2 or r2: print("PART 2")
    if e2 and s != "": print("Example Solution:", solve2(s))
    if ex2: print("Example 2 Solution:", solve2(s2))
    if r2: print("Actual Solution:", sol2 := solve2(inp))
    
    if (one and r1) or (two and r2):
        go = input('Submit? [y/N] ')
        if go == 'y':
            if one and r1: submit(sol1, part=1, year=YEAR, day=DAY)
            if two and r2: submit(sol2, part=2, year=YEAR, day=DAY)