from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    grid = s_to_grid(d)
    result = 0
    for x in grid.findall('X'):
        for delta in OCT_DELTA:
            c2, c3, c4 = tadd(x, delta), tadd(x, tmul(delta, 2)), tadd(x, tmul(delta, 3))
            if c2 in grid and c3 in grid and c4 in grid and grid[c2] + grid[c3] + grid[c4] == "MAS":
                result += 1
    return result

DIAG_DELTA = [(1, 1), (-1, -1), (1, -1), (-1, 1)]

def solve2(d):
    grid = s_to_grid(d)
    result = 0
    for a in grid.findall('A'):
        neighbors = grid.get_neighbors_values(a, DIAG_DELTA)
        result += len(neighbors) == 4 and "".join(neighbors) in ["SMSM", "SMMS", "MSSM", "MSMS"]
    return result


s = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""".strip()
s2 = """
.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
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