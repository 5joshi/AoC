from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    nodes = lmap(ints, d.splitlines()[2:])
    nodes = [(x, y, used, avail) for x, y, _, used, avail, _ in nodes]    
    
    return sum([c[0][2] != 0 and c[0][2] <= c[1][3] for c in it.permutations(nodes, 2)])

def solve2(d):
    grid = lmap(ints, d.splitlines()[2:])
    grid = {(x, y): ('#' if used > 100 else 'E' if used == 0 else '.') for x, y, _, used, _, _ in grid}
    grid = map_to_grid(grid)
    start = (0, 0)
    empty = grid.find('E')
    goal = (grid.nrows - 1, 0)

    def expand(node):
        return [new for new in grid.get_neighbors(node, GRID_DELTA) if grid[new] != '#']
    
    empty_to_goal = bfs_single(empty, to_node=goal, expand=expand)[0]
    goal_to_start = bfs_single(goal, to_node=start, expand=expand)[0]
    return empty_to_goal + 5 * (goal_to_start - 1)


s = """
root@ebhq-gridcenter# df -h
Filesystem            Size  Used  Avail  Use%
/dev/grid/node-x0-y0   10T    8T     2T   80%
/dev/grid/node-x0-y1   11T    6T     5T   54%
/dev/grid/node-x0-y2   32T   28T     4T   87%
/dev/grid/node-x1-y0    9T    7T     2T   77%
/dev/grid/node-x1-y1    8T    0T     8T    0%
/dev/grid/node-x1-y2   11T    7T     4T   63%
/dev/grid/node-x2-y0   10T    6T     4T   60%
/dev/grid/node-x2-y1    9T    8T     1T   88%
/dev/grid/node-x2-y2    9T    6T     3T   66%

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