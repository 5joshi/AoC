from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    robots = lmap(ints, d.splitlines())
    points = defaultdict(set)
    
    for px, py, vx, vy in robots:
        points[(px, py)].add((vx, vy))
    # print(points) 
    (minx, maxx), (miny, maxy) = min_max(lmap(fst, points.keys())), min_max(lmap(snd, points.keys()))
    # minx, maxx = 0, 10
    # miny, maxy = 0, 6
    
    # print(len(points))
    for _ in range(100):
        new_points = defaultdict(set)
        # print(points_to_grid(points.keys(), dimensions=[maxx, maxy]))
        # print(points)
        for p, s in points.items():
            for v in s:
                nx, ny = tadd(p, v)
                if nx < minx:
                    nx += maxx + 1
                elif nx > maxx:
                    nx -= maxx + 1
                if ny < miny:
                    ny += maxy + 1
                elif ny > maxy:
                    ny -= maxy + 1
                new_points[(nx, ny)].add(v)
        points = new_points
    
    print(len(points))
    print(points_to_grid(points.keys()))
    TL = [len(points[(x, y)]) for x, y in points.keys() if minx <= x < minx + (maxx - minx) // 2 and miny <= y < miny + (maxy - miny) // 2]
    TR = [len(points[(x, y)]) for x, y in points.keys() if minx + (maxx - minx) // 2 < x <= maxx and miny <= y < miny + (maxy - miny) // 2]
    BL = [len(points[(x, y)]) for x, y in points.keys() if minx <= x < minx + (maxx - minx) // 2 and miny + (maxy - miny) // 2 < y <= maxy]
    BR = [len(points[(x, y)]) for x, y in points.keys() if minx + (maxx - minx) // 2 < x <= maxx and miny + (maxy - miny) // 2 < y <= maxy]
    print(TL, TR, BL, BR)
    # print(grid, quadrants)
    return product([sum(x) for x in [TL, TR, BL, BR]])

def solve2(d):
    robots = lmap(ints, d.splitlines())
    points = defaultdict(set)
    file = open('day14.txt', 'w')
    
    for px, py, vx, vy in robots:
        points[(px, py)].add((vx, vy))
    # print(points) 
    (minx, maxx), (miny, maxy) = min_max(lmap(fst, points.keys())), min_max(lmap(snd, points.keys()))
    # minx, maxx = 0, 10
    # miny, maxy = 0, 6
    
    # print(len(points))
    for _ in range(101*103):
        new_points = defaultdict(set)
        file.write(str(_))
        file.write('\n')

        file.write(str(points_to_grid(points.keys(), flip=True)))
        file.write('\n\n')
        
        for p, s in points.items():
            for v in s:
                nx, ny = tadd(p, v)
                if nx < minx:
                    nx += maxx + 1
                elif nx > maxx:
                    nx -= maxx + 1
                if ny < miny:
                    ny += maxy + 1
                elif ny > maxy:
                    ny -= maxy + 1
                new_points[(nx, ny)].add(v)
                
            
        points = new_points
    
    print(len(points))
    print(points_to_grid(points.keys(), flip=True))
    TL = [len(points[(x, y)]) for x, y in points.keys() if minx <= x < minx + (maxx - minx) // 2 and miny <= y < miny + (maxy - miny) // 2]
    TR = [len(points[(x, y)]) for x, y in points.keys() if minx + (maxx - minx) // 2 < x <= maxx and miny <= y < miny + (maxy - miny) // 2]
    BL = [len(points[(x, y)]) for x, y in points.keys() if minx <= x < minx + (maxx - minx) // 2 and miny + (maxy - miny) // 2 < y <= maxy]
    BR = [len(points[(x, y)]) for x, y in points.keys() if minx + (maxx - minx) // 2 < x <= maxx and miny + (maxy - miny) // 2 < y <= maxy]
    print(TL, TR, BL, BR)
    file.close()
    return product([sum(x) for x in [TL, TR, BL, BR]])


s = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3

""".strip()
s2 = """
p=2,4 v=2,-3

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