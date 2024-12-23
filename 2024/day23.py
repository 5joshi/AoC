from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    conns = defaultdict(set)
    result = 0
    for line in d.splitlines():
        a, b = line.split('-')
        conns[a].add(b)
        conns[b].add(a)
        
    keys = set(conns.keys())
    tkeys = {k for k in keys if k.startswith('t')}
    for t, k1, k2 in it.combinations(keys, 3):
        if not any(x in tkeys for x in (t, k1, k2)): continue
        if t == k1 or k1 == k2 or t == k2: continue
        if k1 in conns[t] and k2 in conns[t] and k1 in conns[k2]:
            result += 1
            # print(t, k1, k2)
    return result
    

def solve2(d):
    conns = defaultdict(set)
    result = 0
    for line in d.splitlines():
        a, b = line.split('-')
        conns[a].add(b)
        conns[b].add(a)
        
    keys = set(conns.keys())
    largest_group, largest_len = None, 0
    for k in keys:
        group = {k}
        stack = [k]
        while stack:
            curr = stack.pop()
            for c in conns[curr]:
                if c not in group and all(x in conns[c] for x in group):
                    group.add(c)
                    stack.append(c)
        if len(group) > largest_len:
            largest_group = group
            largest_len = len(group)  
    return sorted(largest_group)


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