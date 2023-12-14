from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    lines = d.splitlines()
    grid = Grid([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    curr = grid.middle()
    result = ''
    
    for line in lines:
        for c in line:
            delta = CHAR_TO_DELTA[c]
            nxt = tadd(curr, delta)
            curr = nxt if nxt in grid else curr
        result += str(grid[curr])
    
    return result

def solve2(d):
    lines = d.splitlines()
    grid = Grid([[None, None, 1, None, None], 
                 [None, 2, 3, 4, None], 
                 [5, 6, 7, 8, 9], 
                 [None, 'A', 'B', 'C', None], 
                 [None, None, 'D', None, None]])
    curr = grid.middle()
    result = ''
    
    for line in lines:
        for c in line:
            delta = CHAR_TO_DELTA[c]
            nxt = tadd(curr, delta)
            curr = nxt if nxt in grid and grid[nxt] is not None else curr
        result += str(grid[curr])
    
    return result


s = """

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