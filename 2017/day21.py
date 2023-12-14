from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

IMAGE = """
.#.
..#
###
""".strip()

def merge_grids(grids):
    assert math.isqrt(len(grids)) ** 2 == len(grids), "Grids must be square"
    rows = []
    for grids in every_n(grids, math.isqrt(len(grids))):
        row = grids[0]
        for grid in grids[1:]:
            row = row.join(grid, right=True)
        rows.append(row)
    result = rows[0]
    for row in rows[1:]:
        result = result.join(row, right=False)
    return result

def solve1(d, iterations=2):
    d = lmap(lambda line: line.replace('/', '\n').split(' => '), d.splitlines())
    grid = s_to_grid(IMAGE)
    rules = {str(g): s_to_grid(v) for k, v in d for g in s_to_grid(k).transformations()}
    for _ in range(iterations):
        split_size = 2 if (grid.nrows % 2 == 0) else 3
        grid = merge_grids([rules[str(grid)] for grid in grid.split(split_size)])
        
    return grid.count('#')

def solve2(d, iterations=18):
    return solve1(d, iterations)


s = """
../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#

""".strip()
s2 = """

""".strip()

if __name__ == '__main__':
    one, two, e1, e2, ex1, ex2, r1, r2 = get_solution_booleans(sys.argv)
            
    if e1 or ex1 or r1: print("PART 1")
    if e1 and s != "": print("Example Solution:", solve1(s, iterations=2))
    if ex1: print("Example 2 Solution:", solve1(s2))
    if r1: print("Actual Solution:", sol1 := solve1(inp))

    if e2 or ex2 or r2: print("PART 2")
    if e2 and s != "": print("Example Solution:", solve2(s, iterations=2))
    if ex2: print("Example 2 Solution:", solve2(s2))
    if r2: print("Actual Solution:", sol2 := solve2(inp))
    
    if (one and r1) or (two and r2):
        go = input('Submit? [y/N] ')
        if go == 'y':
            if one and r1: submit(sol1, part=1, year=YEAR, day=DAY)
            if two and r2: submit(sol2, part=2, year=YEAR, day=DAY)