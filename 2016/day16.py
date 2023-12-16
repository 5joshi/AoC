from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def invert(s):
    return ''.join('1' if c == '0' else '0' for c in s)

def hsh(s, size):
    if len(s) >= size: return s[:size]
    return hsh(s + '0' + invert(s[::-1]), size)

def checksum(s):
    while len(s) % 2 == 0:
        s = ''.join('1' if a == b else '0' for a, b in every_n(s, 2))
    return s

def solve1(d):
    return checksum(hsh(d, 272))

def solve2(d):
    return checksum(hsh(d, 35651584))



s = """
10000
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