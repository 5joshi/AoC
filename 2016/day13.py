from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    start = (1, 1)
    goal = (31, 39)
    
    def value(x, y):
        return '.' if ((x*x + 3*x + 2*x*y + y + y*y) + int(d)).bit_count() % 2 == 0 else '#'
    
    def expand(node):
        out = []
        for delta in GRID_DELTA:
            new = tadd(node, delta)
            if new[0] >= 0 and new[1] >= 0 and value(*new) == '.':
                out.append(new)
        return out
    
    dists, _ = bfs(start, to_node=goal, expand=expand)        
    return dists[goal]

def solve2(d):
    start = (1, 1)
    goal = (31, 39)
    
    def value(x, y):
        return '.' if ((x*x + 3*x + 2*x*y + y + y*y) + int(d)).bit_count() % 2 == 0 else '#'
    
    def expand(node):
        out = []
        for delta in GRID_DELTA:
            new = tadd(node, delta)
            if new[0] >= 0 and new[1] >= 0 and value(*new) == '.':
                out.append(new)
        return out
    
    dists, _ = bfs(start, to_node=goal, expand=expand, max_dist=50)        
    return len(dists)


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