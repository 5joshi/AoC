from utils import *

inp = get_data(year=2023)

def solve1(d):
    inp = d.splitlines()
    result = 0
    
    for line in inp:
        line = line.split()
    
    return result

def solve2(d):
    inp = d.splitlines()
    result = 0
        
    for line in inp:
        line = line.split()
    
    return result


s = """

""".strip()
s2 = """

""".strip()

if __name__ == '__main__':
    e1, e2, ex1, ex2, r1, r2 = get_solution_booleans(sys.argv)
            
    if e1 or ex1 or r1: print("PART 1")
    if e1: print("Example Solution:", solve1(s))
    if ex1: print("Example 2 Solution:", solve1(s2))
    if r1: print("Actual Solution:", solve1(inp))

    if e2 or ex2 or r2: print("PART 2")
    if e2: print("Example Solution:", solve2(s))
    if ex2: print("Example 2 Solution:", solve2(s2))
    if r2: print("Actual Solution:", solve2(inp))
