from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d, n=1024, x=70):
    grid = points_to_grid(every_n(ints(d), 2)[:n])
    start, end = (0, 0), (x, x)
    
    def expand(c):
        return [(1, n) for n, v in grid.get_neighbors_items(c, GRID_DELTA, '#') if v != "#"]
    
    dists, _ = dijkstra(start, expand=expand, to_node=end)
    return dists[end]
    
def solve2(d, n=1024, x=70):
    coords = every_n(ints(d), 2)
    start, end = (0, 0), (x, x)
    
    def expand(c):
        return [(1, n) for n, v in grid.get_neighbors_items(c, GRID_DELTA, '#') if v != "#"]
    
    grid = points_to_grid(coords[:n])
    dists, parents = dijkstra(start, expand=expand, to_node=end)
    path = path_from_parents(parents, end)
    for x in range(n, len(coords)):
        if coords[x] not in path: continue
        grid = points_to_grid(coords[:x+1])
        dists, parents = dijkstra(start, expand=expand, to_node=end)
        if end not in dists: return ",".join(map(str, coords[x]))
        path = path_from_parents(parents, end)
    


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