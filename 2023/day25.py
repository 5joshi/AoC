from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    lines = lmap(words, d.splitlines())
    graph = defaultdict(list)
    
    for frm, *rest in lines:
        for to in rest:
            graph[frm].append(to)
            graph[to].append(frm)
    
    while True:
        new_g = {k: v.copy() for k, v in graph.items()}
        size = {k: 1 for k in new_g}
        while len(new_g) > 2:
            new = random.choice(list(new_g.keys()))
            old = random.choice(new_g[new])

            size[new] += size[old]
            for x in new_g[old]:
                if x != new:
                    new_g[x].append(new)
                    new_g[new].append(x)
                new_g[x].remove(old)
            del new_g[old]
            del size[old]
            assert not any(old in v for v in new_g.values()), new_g

        if any(len(v) == 3 for v in new_g.values()): 
            return product(size.values())

s = """
jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr

""".strip()
s2 = """

""".strip()

if __name__ == '__main__':
    one, two, e1, e2, ex1, ex2, r1, r2 = get_solution_booleans(sys.argv)
            
    if e1 or ex1 or r1: print("PART 1")
    if e1 and s != "": print("Example Solution:", solve1(s))
    if ex1: print("Example 2 Solution:", solve1(s2))
    if r1: print("Actual Solution:", sol1 := solve1(inp))
    
    if (one and r1) or (two and r2):
        go = input('Submit? [y/N] ')
        if go == 'y':
            if one and r1: submit(sol1, part=1, year=YEAR, day=DAY)