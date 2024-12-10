from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)


def solve1(d):
    grid = s_to_grid(d).map(int)
    result = 0
    
    for origin in grid.findall(0):
        curr = {origin}
        for i in range(1, 10):
            curr = {nc for c in curr for nc, val in grid.get_neighbors_items(c, GRID_DELTA) if val == i}
        result += len(curr)
        
    return result

def solve2(d):
    grid = s_to_grid(d).map(int)
    result = 0
    
    for origin in grid.findall(0):
        curr = [origin]
        for i in range(1, 10):
            curr = [nc for c in curr for nc, val in grid.get_neighbors_items(c, GRID_DELTA) if val == i]
        result += len(curr)
        
    return result


s = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
""".strip()
s2 = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
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