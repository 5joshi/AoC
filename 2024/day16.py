from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    grid = s_to_grid(d)
    start = (grid.find("S"), CTD["E"])
    end = grid.find("E")
    
    def expand(node):
        p, d = node
        nxt = [(1, (n, d))] if (n := tadd(p, d)) in grid and grid[n] != "#" else []
        return nxt + [(1000, (p, turn_left(d))), (1000, (p, turn_right(d)))]
        
    dists, _ = dijkstra(start, expand=expand, to_func=lambda n: n[0] == end)
    return next(v for k, v in dists.items() if k[0] == end)

def solve2(d):
    grid = s_to_grid(d)
    start = (grid.find("S"), CTD["E"])
    end = grid.find("E")
    
    def expand(node, reverse=False):
        p, d = node
        nxt = [(1, (n, d))] if (n := tadd(p, d) if not reverse else tsub(p, d)) in grid and grid[n] != "#" else []
        return nxt + [(1000, (p, turn_left(d))), (1000, (p, turn_right(d)))]
        
    dists, _ = dijkstra(start, expand=expand)
    end, dist = min([(k, v) for k, v in dists.items() if k[0] == end], key=snd)

    rev, _ = dijkstra(end, expand=lambda n: expand(n, reverse=True))
    return len({k[0] for k in dists.keys() if (dists[k] + rev[k]) == dist})


s = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############

""".strip()
s2 = """
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################

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