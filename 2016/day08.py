from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    lines = lmap(words_and_ints, d.splitlines())
    grid = Grid([['.'] * 50 for _ in range(6)])

    for line in lines:
        if line[0] == 'rect':
            grid.set_section((0, 0), (line[3] - 1, line[1] - 1), '#')
        elif line[0] == 'rotate':
            if line[1] == 'row':
                grid.shift_row(line[3], -line[5])
            elif line[1] == 'column':
                grid.shift_col(line[3], -line[5])
    
    return grid.count('#')

def solve2(d):
    lines = lmap(words_and_ints, d.splitlines())
    grid = Grid([['.'] * 50 for _ in range(6)])

    for line in lines:
        if line[0] == 'rect':
            grid.set_section((0, 0), (line[3] - 1, line[1] - 1), '#')
        elif line[0] == 'rotate':
            if line[1] == 'row':
                grid.shift_row(line[3], -line[5])
            elif line[1] == 'column':
                grid.shift_col(line[3], -line[5])
    
    return '\n' + str(grid)


s = """
rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1
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