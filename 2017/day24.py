from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    num_to_part = defaultdict(set)
    for x, y in lmap(ints, d.splitlines()):
        num_to_part[x].add(y)
        num_to_part[y].add(x)
    
    def best(bridge):
        used = set(windows(bridge, 2))
        options = [part for part in num_to_part[bridge[-1]] if (bridge[-1], part) not in used and (part, bridge[-1]) not in used]
        if not options:
            return sum(bridge) + sum(bridge[1:-1])
        return max(best(bridge + [option]) for option in options)
        
    return best([0])

def solve2(d):
    num_to_part = defaultdict(set)
    for x, y in lmap(ints, d.splitlines()):
        num_to_part[x].add(y)
        num_to_part[y].add(x)
    
    def best(bridge):
        used = set(windows(bridge, 2))
        options = [part for part in num_to_part[bridge[-1]] if (bridge[-1], part) not in used and (part, bridge[-1]) not in used]
        if not options:
            return (len(bridge), sum(bridge) + sum(bridge[1:-1]))
        return max(best(bridge + [option]) for option in options)
        
    return best([0])[1]


s = """
0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10
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