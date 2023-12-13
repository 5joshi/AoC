from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    lines = lmap(ints, d.splitlines())
    neighbors = {frm: [*rest] for frm, *rest in lines}
    
    def reachable(node):
        seen = set()
        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            for neighbor in neighbors[node]:
                dfs(neighbor)
        dfs(node)
        return seen
    
    return sum(0 in reachable(node) for node in neighbors.keys())

def solve2(d):
    lines = lmap(ints, d.splitlines())
    neighbors = {frm: [*rest] for frm, *rest in lines}
    
    def reachable(node):
        seen = set()
        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            for neighbor in neighbors[node]:
                dfs(neighbor)
        dfs(node)
        return seen
    
    return len({frozenset(reachable(node)) for node in neighbors.keys()})


s = """
0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5

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