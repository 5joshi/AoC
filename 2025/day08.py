from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    boxes = lmap(ints, d.splitlines())
    best = 5000000000000
    pair = (None, None)
    
    circuits = []
    dists = []

    for x, y in it.combinations(boxes, 2):
        dists.append((dist2(x, y), tuple(x), tuple(y)))
    for d, x, y in sorted(dists)[:1000]:
        changes = set()
        for i, c in enumerate(circuits):
            if x in c: 
                circuits[i].add(y)
                changes.add(i)
            elif y in c: 
                circuits[i].add(x)
                changes.add(i)
        if not changes: 
            circuits.append({x, y})
        elif len(changes) > 1:
            merged = set()
            for i in sorted(changes, reverse=True):
                merged |= {*circuits[i]}
                circuits.pop(i)
            circuits.append(merged)
        
        
    return product(len(c) for c in sorted(circuits, key=len, reverse=True)[:3])

def solve2(d):
    boxes = lmap(ints, d.splitlines())
    best = 5000000000000
    pair = (None, None)
    
    circuits = []
    dists = []

    for x, y in it.combinations(boxes, 2):
        dists.append((dist2(x, y), tuple(x), tuple(y)))
    for d, x, y in sorted(dists):
        changes = set()
        for i, c in enumerate(circuits):
            if x in c: 
                circuits[i].add(y)
                changes.add(i)
            elif y in c: 
                circuits[i].add(x)
                changes.add(i)
        if not changes: 
            circuits.append({x, y})
        elif len(changes) > 1:
            merged = set()
            for i in sorted(changes, reverse=True):
                merged |= {*circuits[i]}
                circuits.pop(i)
            circuits.append(merged)
        
        if len(circuits[0]) == len(boxes):
            return x[0] * y[0]
        
    

s = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689

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