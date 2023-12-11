from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    def isnice(s):
        if any(bad in s for bad in ['ab', 'cd', 'pq', 'xy']): return False
        if sum(s.count(v) for v in 'aeiou') >= 3 and any(c + c in s for c in ALPHABET): return True
        return False
    
    return len(lfilter(isnice, d.splitlines()))

def solve2(d):
    def isnice(s):        
        if any(s.count(a+b) >= 2 for a,b in windows(s, 2)) and any(re.search(f'{c}.{c}', s) for c in ALPHABET): return True
        return False
    
    return len(lfilter(isnice, d.splitlines()))


s = """
xxyxx
""".strip()
s2 = """

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