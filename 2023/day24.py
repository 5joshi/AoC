from utils import *
import numpy as np
import z3

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    points = [eval(f'({line.replace(" @ ", "), (")})') for line in d.splitlines()]
    LO, HI = 200000000000000, 400000000000000
    result = 0

    for ((p1, v1), (p2, v2)) in it.combinations(points, 2):
        if (v1[0] / v2[0]) == (v1[1] / v2[1]): continue
        
        A = np.array([[v1[0], -v2[0]], [v1[1], -v2[1]]])
        b = np.array([p2[0] - p1[0], p2[1] - p1[1]])
        x = np.linalg.solve(A, b)
        if min(x) < 0: continue
        
        newx, newy, _ = tadd(tmul(v1, x[0]), p1)
        if LO <= newx <= HI and LO <= newy <= HI:
            result += 1

    return result

def solve2(d):
    points = [eval(f'({line.replace(" @ ", "), (")})') for line in d.splitlines()]

    solver = z3.Solver()
    X, Y, Z, VX, VY, VZ, *times = z3.Reals('x y z vx vy vz t1 t2 t3')
    for t, ((x, y, z), (vx, vy, vz)) in zip(times, points[:3]):
        solver.add((t * (VX - vx)) == x - X)
        solver.add((t * (VY - vy)) == y - Y)
        solver.add((t * (VZ - vz)) == z - Z)
        
    solver.check()
    solution = solver.model()
    return eval(str(solution[X] + solution[Y] + solution[Z]))


s = """
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3

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