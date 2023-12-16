from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d, start=(0, -1), direction='R'):
    grid = Grid(lmap(list, d.splitlines()))
    
    def expand(node):
        coord, direction = node
        nxt = tadd(coord, CTD[direction])
        if nxt not in grid: return []
        val = grid[nxt]
        if (val == '|' and direction in 'LR') or (val == '-' and direction in 'UD'):
            return [(nxt, turn_left(direction)), (nxt, turn_right(direction))]
        if (val == '/' and direction in 'LR') or (val == '\\' and direction in 'UD'):
            return [(nxt, turn_left(direction))]
        if val == '/' or val == '\\':
            return [(nxt, turn_right(direction))]
        return [(nxt, direction)]

    dists, _ = bfs((start, direction), expand)
    return len({c for c, d in dists.keys()}) - 1

def solve2(d):
    grid = Grid(lmap(list, d.splitlines()))
    result = 0
    for r in range(grid.nrows):
        result = max(result, solve1(d, start=(r, -1), direction='R'))
        result = max(result, solve1(d, start=(r, grid.ncols), direction='L'))
    for c in range(grid.ncols):
        result = max(result, solve1(d, start=(-1, c), direction='D'))
        result = max(result, solve1(d, start=(grid.nrows, c), direction='U'))
    return result
    


s = """
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....

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