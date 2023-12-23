from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

# TODO: cleanup, (maybe use the polynomial approach)
def solve1(d):
    grid = s_to_grid(d)
    start = grid.find('S')
    
    def expand(node):
        return {c for c, v in grid.get_neighbors_items(node, GRID_DELTA) if v in '.S'}
    
    nodes = set([start])
    for _ in range(64):
        new = set()
        for node in nodes:
            new |= expand(node)
        nodes = new
    return len(nodes)

def solve2(d):
    grid = s_to_grid(d)
    start = grid.find('S')
    result = 0
    
    def expand(node):
        return {c for c, v in grid.get_neighbors_items(node, GRID_DELTA) if v in '.S'}

    def num_reachable(start, steps):
        nodes = set([start])
        for _ in range(steps):
            new_nodes = set()
            for node in nodes:
                new_nodes |= set(expand(node))
            nodes = new_nodes
        return len(nodes)
    
    GRIDS_WIDTH = 26501365 // 131

    # Corners of the diamond, 130 steps left
    for frm in grid.central_edges():
        result += num_reachable(frm, 130)
    
    for frm in grid.corners():
        result += (GRIDS_WIDTH - 1) * num_reachable(frm, 195)
        result += GRIDS_WIDTH * num_reachable(frm, 64)
        
    result += num_reachable(start, 201) * ((GRIDS_WIDTH - 1) ** 2)
    result += num_reachable(start, 200) * (GRIDS_WIDTH ** 2)

    return result


s = """
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........

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