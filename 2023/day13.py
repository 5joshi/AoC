from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    grids = lmap(lambda section: Grid(lmap(list, section.splitlines())), d.split('\n\n'))
    mirr_rows = mirr_cols = 0
    
    for grid in grids:
        cols = grid.cols()
        for idx in range(grid.ncols):
            col_found = False
            # length = min(idx, grid.nrows-idx)
            after = cols[idx:]
            before = cols[:idx][::-1]
            if len(before) and all(a == b for a, b in lzip(before, after)): 
                col_found = True
                mirr_cols += idx
                break
        if not col_found:
            rows = grid.rows()
            for idx in range(grid.nrows):
                after = rows[idx:]
                before = rows[:idx][::-1]
                if len(before) and all(a == b for a, b in lzip(before, after)): 
                    row_found = True
                    mirr_rows += idx
                    break
        if not col_found and not row_found:     
            print(grid, idx, col_found)

    
    return mirr_cols + 100 * mirr_rows

def solve2(d):
    grids = lmap(lambda section: Grid(lmap(list, section.splitlines())), d.split('\n\n'))
    mirr_rows = mirr_cols = 0
    
    for grid in grids:
        cols = grid.cols()
        for idx in range(grid.ncols):
            col_found = False
            # length = min(idx, grid.nrows-idx)
            after = cols[idx:]
            before = cols[:idx][::-1]
            if len(before) and sum(sum(x != y for x, y in lzip(a, b)) for a, b in lzip(before, after)) == 1: 
                col_found = True
                mirr_cols += idx
                break
        if not col_found:
            rows = grid.rows()
            for idx in range(grid.nrows):
                after = rows[idx:]
                before = rows[:idx][::-1]
                if len(before) and sum(sum(x != y for x, y in lzip(a, b)) for a, b in lzip(before, after)) == 1: 
                    row_found = True
                    mirr_rows += idx
                    break
        print(grid, idx, col_found)

    
    return mirr_cols + 100 * mirr_rows


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