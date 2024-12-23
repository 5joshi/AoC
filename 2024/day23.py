from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    result = 0
    conns = defaultdict(set)
    for a, b in every_n(words(d), 2):
        conns[a].add(b)
        conns[b].add(a)
        
    for k1, k2, k3 in it.combinations(conns.keys(), 3):
        if not any(k.startswith('t') for k in (k1, k2, k3)): continue
        if k1 in conns[k2] and k2 in conns[k3] and k1 in conns[k3]: result += 1

    return result
    

def solve2(d):
    conns = defaultdict(set)
    for a, b in every_n(words(d), 2):
        conns[a].add(b)
        conns[b].add(a)
        
    best, lbest = None, 0
    for k in conns.keys():
        seen, todo = {k}, [k]
        while todo:
            curr = todo.pop()
            for c in conns[curr]:
                if c not in seen and all(x in conns[c] for x in seen):
                    seen.add(c)
                    todo.append(c)
                    
        if len(seen) > lbest:
            best, lbest = seen, len(seen)
            
    return ','.join(sorted(best))


s = """
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn

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