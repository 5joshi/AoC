from utils import *
import z3

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def tokens(xa, ya, xb, yb, xg, yg):
    A, B = z3.Ints('a b')
    solver = z3.Solver()

    solver.add(xg == A * xa + B * xb, yg == A * ya + B * yb)
    if solver.check() != z3.sat: return 0
    
    model = solver.model()
    return 3 * model[A].as_long() + model[B].as_long()    

def solve1(d):
    return sum(tokens(*ints(p)) for p in d.split("\n\n"))

def solve2(d):
    return sum(tokens(*ab, xg+10000000000000, yg+10000000000000) for *ab, xg, yg in lmap(ints, d.split("\n\n")))



s = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279

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