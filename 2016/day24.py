from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    grid = s_to_grid(d)
    start = (grid.find('0'), frozenset({'0', '.'}))
    goal = lambda node: len(node[1]) == len(ints(d)) + 1
    
    def expand(node):
        coord, seen = node
        return [(newc, frozenset(seen | {newv})) for newc, newv in grid.get_neighbors_items(coord, GRID_DELTA) if newv != '#']
    
    return bfs_single(start, to_func=goal, expand=expand)[0]

def solve2(d):
    grid = s_to_grid(d)
    result = math.inf
    
    def expand(node):
        return [newc for newc, newv in grid.get_neighbors_items(node, GRID_DELTA) if newv != '#']
    
    dists = {(frm, to): bfs_single(grid.find(str(frm)), to_node=grid.find(str(to)), expand=expand)[0] for frm, to in it.permutations(ints(d), 2)}
    for perm in it.permutations(filter(lambda n: n != 0, ints(d))):
        perm = (0,) + perm + (0,)
        result = min(result, sum([dists[frm, to] for frm, to in windows(perm, 2)]))
        
    return result


s = """
###########
#0.1.....2#
#.#######.#
#4.......3#
###########
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