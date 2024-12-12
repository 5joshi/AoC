from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def perimeter(coords, deltas=GRID_DELTA):
    return sum(sum(nc not in coords for nc in neighbors(c, deltas)) for c in coords)

def sides(coords, deltas=GRID_DELTA):
    result = perimeter(coords, deltas)
    for c in {nc for c in coords for nc in neighbors(c, deltas)}:
        x1, x2, x3, x4 = c, tadd(c, CTD["L"]), tadd(c, CTD["UL"]), tadd(c, CTD["U"])
        result -= ((x1 in coords) != (x3 in coords)) and ((x2 in coords) != (x4 in coords))
    return result

def solve1(d):
    grid = s_to_grid(d)
    result = 0
    
    while c := grid.find_func(lambda x: x != "."):
        group = grid.floodfill(c, GRID_DELTA, ".")
        result += len(group) * perimeter(group)
    
    return result

def solve2(d):
    grid = s_to_grid(d)
    result = 0

    while c := grid.find_func(lambda x: x != "."):
        group = grid.floodfill(c, GRID_DELTA, ".")
        result += len(group) * sides(group)
    
    return result


s = """
EEEEE
EXXXX
EEEEE
EXXXX
EEEEE




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