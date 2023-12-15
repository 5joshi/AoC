from utils import *

import hashlib

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    result = ''
    for i in it.count(0):
        h = hashlib.md5((d + str(i)).encode()).hexdigest()
        if '00000' == h[:5]:
            result += h[5]
            if len(result) == 8:
                return result

def solve2(d):
    result = ['X'] * 8
    for i in it.count(0):
        h = hashlib.md5((d + str(i)).encode()).hexdigest()
        if '00000' == h[:5] and h[5].isdigit() and int(h[5]) < 8 and result[int(h[5])] == 'X':
            result[int(h[5])] = h[6]
            print(''.join(result), h[5], h[6])
            if not any(c == 'X' for c in result):
                return ''.join(result)


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