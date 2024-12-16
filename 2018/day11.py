from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)



def solve1(d):
    c = ints(d)[0]
    max_power, idx = 0, None
    
    @lru_cache(None)
    def power(x, y):
        return ((((x + 10) * y + c) * (x + 10)) // 100) % 10 - 5
    
    for x in range(300 - 3):
        for y in range(300 - 3):
            score = sum(power(x + i, y + j) for i in range(3) for j in range(3))
            if score > max_power:
                max_power, idx = score, (x, y)
    
    return idx

def solve2(d):
    c = ints(d)[0]
    max_power, idx = 0, None
    
    @lru_cache(None)
    def power(x, y):
        return ((((x + 10) * y + c) * (x + 10)) // 100) % 10 - 5
    
    for s in range(1, 15):
        for x in range(300 - s):
            for y in range(300 - s):
                score = sum(power(x + i, y + j) for i in range(s) for j in range(s))
                if score > max_power:
                    max_power, idx = score, (x, y, s)
    
    return idx


s = """
42
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