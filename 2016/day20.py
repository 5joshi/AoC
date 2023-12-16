from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    ranges = [(lo, hi) for lo, hi in every_n(positive_ints(d), 2)]
    excluded = []
    
    for lo, hi in ranges:
        for idx, (xlo, xhi) in enumerate(excluded):
            if lo <= xlo - 1 <= hi or lo <= xhi + 1 <= hi:
                excluded[idx] = (min(lo, xlo), max(hi, xhi))
                break
        else: 
            excluded.append((lo, hi))

    return next(filter(lambda w: w[0][1] + 1 != w[1][0], windows(sorted(excluded), 2)))[0][1] + 1

def solve2(d):
    ranges = [(lo, hi) for lo, hi in every_n(positive_ints(d), 2)]
    ranges.append((2**32, 2**32))
    result = curr = 0
    
    for lo, hi in sorted(ranges):
        if lo <= curr <= hi:
            curr = hi + 1
        elif curr < lo:
            result += lo - curr
            curr = hi + 1

    return result


s = """
5-8
0-2
4-7
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