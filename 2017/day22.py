from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    grid = s_to_grid(d)
    curr, delta = grid.middle(), CHAR_TO_DELTA['U']
    infected = set(grid.findall('#'))
    result = 0
    
    for _ in range(10000):
        delta = turn_right(delta) if curr in infected else turn_left(delta)
        if curr in infected: 
            infected.remove(curr)
        else: 
            result += 1
            infected.add(curr)
        curr = tadd(curr, delta)
    
    return result

def solve2(d):
    grid = s_to_grid(d)
    curr, delta = grid.middle(), CHAR_TO_DELTA['U']
    nodes = defaultdict(lambda: 'C', {c: 'I' for c in grid.findall('#')})
    cycle = {frm: to for frm, to in zip('CWIF', 'WIFC')}
    result = 0
    
    for _ in range(10000000):
        if nodes[curr] == 'C': delta = turn_left(delta)
        elif nodes[curr] == 'I': delta = turn_right(delta)
        elif nodes[curr] == 'F': delta = turn_180(delta)
        
        if nodes[curr] == 'W': result += 1
        nodes[curr] = cycle[nodes[curr]]
        curr = tadd(curr, delta)
    
    return result


s = """
..#
#..
...
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