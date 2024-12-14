from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d, w=101, h=103):
    robots = lmap(ints, d.splitlines())
    points = [((px + (vx * 100)) % w, (py + (vy * 100)) % h) for px, py, vx, vy in robots]
    
    quadrants = [0] * 4
    for x, y in points:
        if x == (w // 2) or y == (h // 2): continue
        quadrants[(x > (w // 2)) + 2 * (y > (h // 2))] += 1
    
    return product(quadrants)

def solve2(d, w=101, h=103):
    robots = lmap(ints, d.splitlines())
    for i in range(10000):
        points = {((px + (vx * i)) % w, (py + (vy * i)) % h) for px, py, vx, vy in robots}
        if len(points) == len(robots): 
            return i

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
    if e1 and s != "": print("Example Solution:", solve1(s, w=11, h=7))
    if ex1: print("Example 2 Solution:", solve1(s2, w=11, h=7))
    if r1: print("Actual Solution:", sol1 := solve1(inp))

    if e2 or ex2 or r2: print("PART 2")
    if e2 and s != "": print("Example Solution:", solve2(s, w=11, h=7))
    if ex2: print("Example 2 Solution:", solve2(s2, w=11, h=7))
    if r2: print("Actual Solution:", sol2 := solve2(inp))
    
    if (one and r1) or (two and r2):
        go = input('Submit? [y/N] ')
        if go == 'y':
            if one and r1: submit(sol1, part=1, year=YEAR, day=DAY)
            if two and r2: submit(sol2, part=2, year=YEAR, day=DAY)