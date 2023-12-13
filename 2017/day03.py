from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def make_spiral(size, func=lambda c, points: len(points) + 1):   
    """
    func = function that takes coordinate & points of the current spiral
    Creates a spiral of given size in which each cell is the result of func applied to the cell's coordinates and the previous cells.
    """
    curr = (0, 0)
    points = {curr: func(curr, {})}
    directions = it.cycle(CHAR_TO_DELTA[d] for d in 'RULD')
    steps = map(lambda c: c//2, it.count(2))
    curr_dir = next(directions)
    curr_steps = next(steps)

    for _ in range(size-1):
        if curr_steps == 0:
            curr_dir = next(directions)
            curr_steps = next(steps)
        curr = tadd(curr, curr_dir)
        points[curr] = func(curr, points)
        curr_steps -= 1
    
    return points

def solve1(d):
    return sum(map(abs, invert_dict(make_spiral(int(d)))[int(d)]))

def solve2(d):
    def value(c, points):
        return 1 if c == (0,0) else sum(points.get(tadd(c, d), 0) for d in OCT_DELTA)
    
    return next(filter(lambda x: x > int(d), make_spiral(1000, value).values()))


s = """
1024
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
    if e2 and s2 != "": print("Example Solution:", solve2(s))
    if ex2: print("Example 2 Solution:", solve2(s2))
    if r2: print("Actual Solution:", sol2 := solve2(inp))
    
    if (one and r1) or (two and r2):
        go = input('Submit? [y/N] ')
        if go == 'y':
            if one and r1: submit(sol1, part=1, year=YEAR, day=DAY)
            if two and r2: submit(sol2, part=2, year=YEAR, day=DAY)