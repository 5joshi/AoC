from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    lines = d.split(', ')
    delta = CHAR_TO_DELTA['U']
    curr = (0, 0)
    
    seen = set()
    for instr in lines:
        seen.add(curr)
        if instr[0] == 'R':
            delta = turn_right(delta)
        else:
            delta = turn_left(delta)
        curr = tmul(tadd(curr, delta), int(instr[1:]))

    return pdist1(curr)

def solve2(d):
    lines = d.split(', ')
    delta = CHAR_TO_DELTA['U']
    curr = (0, 0)
    
    seen = set(curr)
    for instr in lines:
        if instr[0] == 'R':
            delta = turn_right(delta)
        else:
            delta = turn_left(delta)
        for i in range(int(instr[1:])):
            curr = tadd(curr, delta)
            if curr in seen: return pdist1(curr)
            else: seen.add(curr)


s = """
R8, R4, R4, R8""".strip()
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