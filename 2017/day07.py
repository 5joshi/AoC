from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    lines = lmap(words_and_ints, d.splitlines())
    names = set()
    tower = {}
    
    for name, _, *rest in lines:
        names.add(name)
        for child in rest:
            tower[child] = name
                
    return next(key for key in names if key not in tower.keys())

def solve2(d):
    lines = lmap(words_and_ints, d.splitlines())
    weights = {}
    tower = {}
    
    for name, weight, *rest in lines:
        weights[name] = weight
        for child in rest:
            tower[child] = name
                
    def real_weight(name):
        if name not in tower:
            return weights[name]
        return weights[name] + sum(map(real_weight, tower[name]))
                
    tower = invert_dict(tower, single=False)
    for name in reversed(topsort(tower)):   
        if name in tower:
            child_weights = [real_weight(child) for child in tower[name]]
            if sum(list_diff(child_weights)) != 0:
                lo, hi = min_max(child_weights)
                return next(weights[child] + lo - hi for child in tower[name] if real_weight(child) == hi)
    


s = """
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)

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