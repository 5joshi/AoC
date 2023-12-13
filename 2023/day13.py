from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def diffs(ls, idx):
    return sum(sum(x != y for x, y in lzip(a, b)) for a, b in zip(ls[idx:], ls[:idx][::-1]))

def solve1(d, num_diffs=0):
    grids = lmap(s_to_grid, d.split('\n\n'))
    result = 0
    
    for grid in grids:
        result += 100 * (row := next(filter(lambda idx: diffs(grid.rows(), idx) == num_diffs, range(1, grid.nrows)), 0))
        if not row: result += next(filter(lambda idx: diffs(grid.cols(), idx) == num_diffs, range(1, grid.ncols)))
    
    return result

def solve2(d):
    return solve1(d, num_diffs=1)


s = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#

""".strip()
s2 = """
..###..#.
..##...#.
..#.#.##.
...##....
..#..#..#
..#.#####
##..#.#.#
""".strip()

if __name__ == '__main__':
    one, two, e1, e2, ex1, ex2, r1, r2 = get_solution_booleans(sys.argv)
            
    if e1 or ex1 or r1: print("PART 1")
    if e1 and s != "": print("Example Solution:", solve1(s))
    if ex1: print("Example 2 Solution:", solve1(s2))
    if r1: print("Actual Solution:", sol1 := solve1(inp))

    if e2 or ex2 or r2: print("PART 2")
    if e2 and s2 != "": print("Example Solution:", solve2(s))
    if ex2: print("Example 2 Solution:", solve2(s2))
    if r2: print("Actual Solution:", sol2 := solve2(inp))
    
    if (one and r1) or (two and r2):
        go = input('Submit? [y/N] ')
        if go == 'y':
            if one and r1: submit(sol1, part=1, year=YEAR, day=DAY)
            if two and r2: submit(sol2, part=2, year=YEAR, day=DAY)