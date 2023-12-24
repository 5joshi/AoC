from utils import *
import numpy as np
import z3

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    lines = d.splitlines()
    points = []
    # LO, HI = 7, 27
    LO, HI = 200000000000000, 400000000000000
    result = 0
    
    for line in lines:
        pos, vel = line.split('@')
        points.append((ints(pos), ints(vel)))

    for comb in it.combinations(points, 2):
        (p1, v1), (p2, v2) = comb
        p1 = p1[:2]
        p2 = p2[:2]
        v1 = v1[:2]
        v2 = v2[:2]
        # delta = best_delta(p1, p2)
        # delta2 = best_delta((0, 0), v1)
        # if delta == delta2:
        x1, y1 = p1
        x2, y2 = p2
        vx1, vy1 = v1
        vx2, vy2 = v2
        A = np.array([[vx1, -vx2], [vy1, -vy2]])
        b = np.array([x2 - x1, y2 - y1])
        try:
            x = np.linalg.solve(A, b)
            if any(v < 0 for v in x):
                continue
        except np.linalg.LinAlgError:
            continue
        newx, newy = tadd(tmul(v1, x[0]), p1)
        if LO <= newx <= HI and LO <= newy <= HI:
            # print(x, p1, p2, v1, v2, (newx, newy))
            result += 1
            # mul1 = max(min(abs((LO - x1) / vx1), abs((LO - y1) / vy1)), 0)
            # mul2 = max(min(abs((LO - x2) / vx2), abs((LO - y2) / vy2)), 0)
            # new1 = tadd(tmul(v1, mul1), p1)
            # new2 = tadd(tmul(v2, mul2), p2)
            # print(mul1, mul2, new1, new2)
            # bottom_delta = best_delta(new1, new2)
            # mul1 = max(min((HI - x1) / vx1, (HI - y1) / vy1), 0)
            # mul2 = max(min((HI - x2) / vx2, (HI - y2) / vy2), 0)
            # new1 = tadd(tmul(v1, mul1), p1)
            # new2 = tadd(tmul(v2, mul2), p2)
            # print((HI - x2) / vx2, (HI - y2) / vy2)
            # print(mul1, mul2, new1, new2)
            # top_delta = best_delta(new1, new2)
            # print(delta, bottom_delta, top_delta)
            # if top_delta != bottom_delta:
                # print(comb)
                # print(delta, bottom_delta, top_delta)
                # print(new1, new2)
                # print()
                # result += 1
            
        # x1, y1, z1 = p1
        # x2, y2, z2 = p2
        # vx1, vy1, vz1 = v1
        # vx2, vy2, vz2 = v2
        # time =  -(x1*vx1 - vx1*x2 - (x1 - x2)*vx2 + y1*vy1 - vy1*y2 - (y1 - y2)*vy2) / (vx1**2 - 2*vx1*vx2 + vx2**2 + vy1**2 - 2*vy1*vy2 + vy2**2)
        # time = -((x1 - x2) * (vx1 - vx2) + (y1 - y2) * (vy1 - vy2)) / ((vx1 - vx2)**2 + (vy1 - vy2)**2)
        # new1 = tadd(tmul(v1, time), p1)
        # new2 = tadd(tmul(v2, time), p2)
        # print(time, new1, new2)
        
    
    return result

def solve2(d):
    lines = d.splitlines()
    points = []
    result = 0
    
    for line in lines:
        pos, vel = line.split('@')
        points.append((ints(pos), ints(vel)))

    solver = z3.Solver()
    X, Y, Z, VX, VY, VZ = z3.Reals('x y z vx vy vz')
    times = z3.Reals('t1 t2 t3')
    for t, point in zip(times, points[:3]):
        (x, y, z), (vx, vy, vz) = point
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