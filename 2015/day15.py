from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    lines = lmap(ints, d.splitlines())
    
    def calc_score(teaspoons):
        scores = (0, 0, 0, 0, 0)
        for idx, tsp in enumerate(teaspoons):
            scores = tadd(scores, tmul(lines[idx], tsp))
        if any(x <= 0 for x in scores): return 0
        return product(scores[:-1])
    
    return max(calc_score(teaspoons) for teaspoons in it.product(range(101), repeat=len(lines)) if sum(teaspoons) == 100)

def solve2(d):
    lines = lmap(ints, d.splitlines())
    
    def calc_score(teaspoons):
        scores = (0, 0, 0, 0, 0)
        for idx, tsp in enumerate(teaspoons):
            scores = tadd(scores, tmul(lines[idx], tsp))
        if any(x <= 0 for x in scores) or scores[-1] != 500: return 0
        return product(scores[:-1])
    
    return max(calc_score(teaspoons) for teaspoons in it.product(range(101), repeat=len(lines)) if sum(teaspoons) == 100)


s = """
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3

""".strip()
s2 = """

""".strip()

if __name__ == '__main__':
    one, two, e1, e2, ex1, ex2, r1, r2 = get_solution_booleans(sys.argv)
            
    if e1 or ex1 or r1: print("PART 1")
    if e1: print("Example Solution:", solve1(s))
    if ex1: print("Example 2 Solution:", solve1(s2))
    if r1: print("Actual Solution:", sol1 := solve1(inp))

    if e2 or ex2 or r2: print("PART 2")
    if e2: print("Example Solution:", solve2(s))
    if ex2: print("Example 2 Solution:", solve2(s2))
    if r2: print("Actual Solution:", sol2 := solve2(inp))
    
    if (one and r1) or (two and r2):
        go = input('Submit? [y/N] ')
        if go == 'y':
            if one and r1: submit(sol1, part=1, year=YEAR, day=DAY)
            if two and r2: submit(sol2, part=2, year=YEAR, day=DAY)