from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    grid = s_to_grid(d).map(int)
    start = ((0, 0), 'DR', 0)
    goal = lambda node: node[0] == (grid.nrows - 1, grid.ncols - 1)

    def expand(node):
        coord, direction, length = node
        
        dirs = direction if length < 2 else ''
        if len(direction) == 1: dirs += (turn_left(direction) + turn_right(direction))
        
        return [(grid[newc], (newc, newd, length + 1 if newd == direction else 0)) \
            for newd in dirs if (newc := tadd(coord, CTD[newd])) in grid]

    def heuristic(node):
        return dist1(node[0], (grid.nrows - 1, grid.ncols - 1))
    
    dist, _ = a_star(start, to_func=goal, expand=expand, heuristic=heuristic)
    return dist

def solve2(d):
    grid = s_to_grid(d).map(int)
    start = ((0, 0), 'DR', 0)
    goal = lambda node: node[0] == (grid.nrows - 1, grid.ncols - 1)

    def expand(node):
        coord, direction, length = node
        
        dirs = direction if length < 9 else ''
        if len(direction) == 1 and length >= 3: dirs += (turn_left(direction) + turn_right(direction))
        
        return [(grid[newc], (newc, newd, length + 1 if newd == direction else 0)) \
            for newd in dirs if (newc := tadd(coord, CTD[newd])) in grid]

    def heuristic(node):
        return dist1(node[0], (grid.nrows - 1, grid.ncols - 1))
    
    dist, _ = a_star(start, to_func=goal, expand=expand, heuristic=heuristic)
    return dist


s = """
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533


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