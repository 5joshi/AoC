from utils import *
from copy import deepcopy

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    grid = s_to_grid(d)
    result = 0
    
    for col in grid.cols():
        row = len(col)
        for idx, elem in enumerate(col):
            if elem == 'O':
                result += row
                row -= 1
            elif elem == '#':
                row = len(col) - idx - 1
        
    return result

def solve2(d):
    grid = Grid(lmap(list, d.splitlines()))
    cycle = []
    seen = set()
    dirs = it.cycle('NWSE')
    
    def roll(grid, direction):
        new_grid = grid
        order = grid.findall('O')
        for old in order if direction in 'NW' else reversed(order):
            new = tadd(old, CHAR_TO_DELTA[direction])
            while new in grid and grid[new] == '.':
                new_grid[new] = 'O'
                new_grid[old] = '.'
                old = new
                new = tadd(new, CHAR_TO_DELTA[direction])
        return new_grid
               
    while str(grid) not in seen:
        seen.add(str(grid))
        cycle.append(str(grid))
        grid = roll(grid, next(dirs))        
    
    frm = cycle.index(str(grid))
    length = len(cycle) - frm
    end = s_to_grid(cycle[frm + (4000000000 - frm) % length])
    return sum([grid.nrows - r for r, c in end.findall('O')])


s = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....

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