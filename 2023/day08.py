from utils import *

inp = get_data(year=2023)

def route_length(route, m, curr = 'AAA', ends = ['ZZZ']):
    for i in it.count(0):
        direction = route[i % len(route)]
        curr = m[curr][direction]
        if curr in ends: return i + 1

def solve1(d):
    route, maps = d.split('\n\n')
    m = {frm: {'L': left, 'R': right} for frm, left, right in lmap(alphanumerics, maps.splitlines())}
    
    return route_length(route, m)
    
def solve2(d):
    route, maps = d.split('\n\n')
    m = {frm: {'L': left, 'R': right} for frm, left, right in lmap(alphanumerics, maps.splitlines())}
    starts, ends = [node for node in m.keys() if re.match('..A', node)], [node for node in m.keys() if re.match('..Z', node)]
    
    return math.lcm(*[route_length(route, m, start, ends) for start in starts])
    


s = """
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
""".strip()
s2 = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)

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
