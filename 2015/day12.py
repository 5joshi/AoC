from utils import *
import json

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    return sum(ints(d))

def solve2(d):
    pop_indices = set()
    for match in re.finditer(r'"red"', d):
        l, r = match.span()
        lcurly = rcurly = lstraight = rstraight = 0
        for r_idx in range(r, len(d)):
            lcurly += (d[r_idx] == '{')
            rcurly += (d[r_idx] == '}')
            lstraight += (d[r_idx] == '[')
            rstraight += (d[r_idx] == ']')
            if lcurly - rcurly < 0 or lstraight - rstraight < 0:
                break
        if lstraight - rstraight < 0:
            continue
        lcurly = rcurly = 0
        for l_idx in range(l, -1, -1):
            lcurly += (d[l_idx] == '{')
            rcurly += (d[l_idx] == '}')
            if rcurly - lcurly < 0:
                break
        pop_indices |= {*range(l_idx, r_idx + 1)}
        
    for idx in reversed(sorted(pop_indices)):
        d = d[:idx] + d[idx + 1:]
        
    return solve1(d)


s = """
[1,{"c":"red","b":2},3]
""".strip()
s2 = """
{"d":"red","e":[1,2,3,4],"f":5}
""".strip()

if __name__ == '__main__':
    one, two, e1, e2, ex1, ex2, r1, r2 = get_solution_booleans(sys.argv)
            
    if e1 or ex1 or r1: print("PART 1")
    if e1: print("Example Solution:", solve1(s))
    if ex1: print("Example 2 Solution:", solve1(s2))
    if r1: print("Actual Solution:", sol1 := solve1(inp))

    if e2 or ex2 or r2: print("PART 2")
    if e2: print("Example Solution:", solve2(s))
    if ex2: print("Example 2 Solution:", solve2(s2))
    if r2: print("Actual Solution:", sol2 := solve2(inp))
    
    if (one and r1) or (two and r2):
        go = input('Submit? [y/N] ')
        if go == 'y':
            if one and r1: submit(sol1, part=1, year=YEAR, day=DAY)
            if two and r2: submit(sol2, part=2, year=YEAR, day=DAY)