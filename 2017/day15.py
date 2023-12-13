from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    v1, v2 = ints(d)
    ones = 2 ** 16 - 1
    
    def A(val):
        while True:
            yield (val := (val * 16807) % 2147483647)
            
    def B(val):
        while True:
            yield (val := (val * 48271) % 2147483647) 
    
    return sum((a & ones) == (b & ones) for a, b in it.islice(zip(A(v1), B(v2)), 40_000_000))

def solve2(d):
    v1, v2 = ints(d)
    ones = 2 ** 16 - 1
    
    def A(val):
        while True:
            yield (val := (val * 16807) % 2147483647)
            
    def B(val):
        while True:
            yield (val := (val * 48271) % 2147483647)
    
    A = filter(lambda x: x % 4 == 0, A(v1))
    B = filter(lambda x: x % 8 == 0, B(v2))
    return sum((a & ones) == (b & ones) for a, b in it.islice(zip(A, B), 5_000_000))


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