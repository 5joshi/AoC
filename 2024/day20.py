from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def neighbor_dist(c, n):
    return {tadd(c, (dx, dy)) for dx in range(-n, n+1) for dy in range(-n, n+1) if dist1((dx, dy)) <= n}

def solve1(d, n=2):
    grid = s_to_grid(d)
    start, end = grid.find('S'), grid.find('E')
    results = []
    
    def expand(c):
        return [(1, nc) for nc in grid.get_neighbors(c, GRID_DELTA) if grid[nc] != '#']
    
    dists, _ = dijkstra(start, expand=expand)
    real_dist = dists[end]
    rev, _ = dijkstra(end, expand=expand)

    for c in dists:
        for nc in neighbor_dist(c, n):
            if nc not in grid or nc not in rev or grid[nc] == "#": continue
            results.append(real_dist - (dists[c] + rev[nc]) - dist1(c, nc))

    return sum(n >= 100 for n in results)

def solve2(d):
    return solve1(d, 20)


s = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############

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