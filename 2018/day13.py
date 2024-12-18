from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    grid = s_to_grid(d, fill=" ")
    carts = {c: (CTD[grid[c]], 0) for c in grid.findall_regex(r"[<>^v]")}
    grid.map(lambda x: x if x not in "<>^v" else "|" if x in "^v" else "-", inplace=True)

    for _ in it.count(0):
        new_carts = dict()
        for c in sorted(carts):
            d, t = carts[c]
            nc = tadd(c, d)
            if c in new_carts: return f"{c[1]},{c[0]}"
            if nc in new_carts: return f"{nc[1]},{nc[0]}"
            if grid[nc] in "-|" or (grid[nc] == "+" and t == 1):
                new_carts[nc] = (d, (t + (grid[nc] == "+")) % 3)
            elif (grid[nc] == "/" and d[0] != 0) or (grid[nc] == "\\" and d[1] != 0) or (grid[nc] == "+" and t == 2):
                new_carts[nc] = (turn_right(d), (t + (grid[nc] == "+")) % 3)
            elif (grid[nc] == "/" and d[1] != 0) or (grid[nc] == "\\" and d[0] != 0) or (grid[nc] == "+" and t == 0):
                new_carts[nc] = (turn_left(d), (t + (grid[nc] == "+")) % 3)
        carts = new_carts           
    
def solve2(d):
    grid = s_to_grid(d, fill=" ")
    carts = {c: (CTD[grid[c]], 0) for c in grid.findall_regex(r"[<>^v]")}
    grid.map(lambda x: x if x not in "<>^v" else "|" if x in "^v" else "-", inplace=True)

    for _ in it.count(0):
        new_carts = dict()
        for c in sorted(carts):
            d, t = carts[c]
            nc = tadd(c, d)
            if c in new_carts: 
                del new_carts[c]
            elif nc in new_carts: 
                del new_carts[nc]
            elif grid[nc] in "-|" or (grid[nc] == "+" and t == 1):
                new_carts[nc] = (d, (t + (grid[nc] == "+")) % 3)
            elif (grid[nc] == "/" and d[0] != 0) or (grid[nc] == "\\" and d[1] != 0) or (grid[nc] == "+" and t == 2):
                new_carts[nc] = (turn_right(d), (t + (grid[nc] == "+")) % 3)
            elif (grid[nc] == "/" and d[1] != 0) or (grid[nc] == "\\" and d[0] != 0) or (grid[nc] == "+" and t == 0):
                new_carts[nc] = (turn_left(d), (t + (grid[nc] == "+")) % 3)
        carts = new_carts
        if len(carts) == 1: 
            x, y = carts.popitem()[0]
            return f"{y},{x}"


s = r"""
/>-<\  
|   |  
| /<+-\
| | | v
\>+</ |
  |   ^
  \<->/ 
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