from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d, n=1024, x=70):
    coords = every_n(ints(d), 2)[:n]
    start = (0, 0)
    end = (x, x)
    grid = points_to_grid(coords)
    print(grid)
    def expand(c):
        r = []
        for neighbor in GRID_DELTA:
            new = tadd(c, neighbor)
            if new in grid and grid[new] != "#":
                r.append((1, new))
        return r
    dists, _ = dijkstra(start, expand=expand,to_node=end)
    # print(dists)
    return dists[end]
    
    # return result

def solve2(d, n=1024, x=70):
    start = (0, 0)
    end = (x, x)
    points = every_n(ints(d), 2)
    result = n
    
    while True:
        curr = points[:result]
        grid = points_to_grid(curr)
        def expand(c):
            r = []
            for neighbor in GRID_DELTA:
                new = tadd(c, neighbor)
                if new in grid and grid[new] != "#":
                    r.append((1, new))
            return r
        dists, _ = dijkstra(start, expand=expand,to_node=end)
        if end not in dists:
            return points[result-1]
        result += 1


s = """
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0

""".strip()
s2 = """

""".strip()

if __name__ == '__main__':
    one, two, e1, e2, ex1, ex2, r1, r2 = get_solution_booleans(sys.argv)
            
    if e1 or ex1 or r1: print("PART 1")
    if e1 and s != "": print("Example Solution:", solve1(s, n=12, x=6))
    if ex1: print("Example 2 Solution:", solve1(s2))
    if r1: print("Actual Solution:", sol1 := solve1(inp))

    if e2 or ex2 or r2: print("PART 2")
    if e2 and s != "": print("Example Solution:", solve2(s, n=12, x=6))
    if ex2: print("Example 2 Solution:", solve2(s2))
    if r2: print("Actual Solution:", sol2 := solve2(inp))
    
    if (one and r1) or (two and r2):
        go = input('Submit? [y/N] ')
        if go == 'y':
            if one and r1: submit(sol1, part=1, year=YEAR, day=DAY)
            if two and r2: submit(sol2, part=2, year=YEAR, day=DAY)