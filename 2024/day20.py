from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def neighbor_dist(c, n):
    return {tadd(c, (dx, dy)) for dx in range(-n, n+1) for dy in range(-n, n+1) if dist1((dx, dy)) <= n}

def solve1(d):
    grid = s_to_grid(d)
    start = grid.find('S')
    end = grid.find('E')
    
    def expand(node):
        return [(1, n) for n in neighbors(node, GRID_DELTA) if n in grid and grid[n] != '#']
    
    dists, _ = dijkstra(start, expand=expand)
    real = dists[end]
    rev, _ = dijkstra(end, expand=expand)
    results = []

    for c in dists:
        for nc in neighbor_dist(c, 2):
            if nc not in grid or nc not in rev or grid[nc] == "#": continue
            
            results.append(shortcut := (real - (dists[c] + rev[nc]) - dist1(c, nc)))

    return sum(n >= 100 for n in results)
        

# def solve1(d):
#     grid = s_to_grid(d)
#     start = grid.find('S')
#     end = grid.find('E')
    
#     def expand2(node):
#         p, c = node
#         if c == (-1, -1):
#             return [(n, (n if grid[n] == "#" else (-1, -1))) for n in neighbors(p, GRID_DELTA) if n in grid]
#         return [(n, c) for n in neighbors(c, GRID_DELTA) if n in grid and grid[n] != "#"]
    
#     dists, _ = bfs((start, (-1, -1)), expand=expand2)
    
#     print({dist for dist in dists if dist[0] == end})


def solve2(d):
    grid = s_to_grid(d)
    start = grid.find('S')
    end = grid.find('E')
    
    def expand(node):
        return [(1, n) for n in neighbors(node, GRID_DELTA) if n in grid and grid[n] != '#']
    
    dists, _ = dijkstra(start, expand=expand)
    real = dists[end]
    rev, _ = dijkstra(end, expand=expand)
    results = []

    for c in dists:
        for nc in neighbor_dist(c, 20):
            if nc not in grid or nc not in rev or grid[nc] == "#": continue
            
            results.append(shortcut := (real - (dists[c] + rev[nc]) - dist1(c, nc)))

    return sum(n >= 100 for n in results)


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