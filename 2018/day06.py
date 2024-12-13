from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    points = lmap(ints, d.splitlines())
    (minx, maxx), (miny, maxy) = min_max([x for x, _ in points]), min_max([y for _, y in points])
    
    closest = Counter()
    edges = set()
    for x in range(minx, maxx+1):
        for y in range(miny, maxy+1):
            dists = sorted(points, key=lambda p: dist1(p, (x, y)))
            if dist1((x, y), dists[0]) != dist1((x, y), dists[1]):
                if x == minx or x == maxx or y == miny or y == maxy:
                    edges.add(tuple(dists[0]))
                closest[tuple(dists[0])] += 1
                
    return next(v for k, v in closest.most_common() if k not in edges)

def solve2(d):
    points = lmap(ints, d.splitlines())
    result = 0
    (minx, maxx), (miny, maxy) = min_max([x for x, _ in points]), min_max([y for _, y in points])
    
    for x in range(minx, maxx+1):
        for y in range(miny, maxy+1):
            if sum(dist1((x, y), p) for p in points) < 10000:
                result += 1
                
    return result

s = """
1, 1
1, 6
8, 3
3, 4
5, 5
8, 9

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