from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    *gifts, trees = d.split("\n\n")
    sizes = lmap(lambda g: g.count("#"), gifts)
    trees = lmap(ints, trees.splitlines())
    
    return sum(sum(n * sizes[i] for i, n in enumerate(ns[2:])) < (ns[0] * ns[1]) for ns in trees) 


s = """

""".strip()
s2 = """

""".strip()

if __name__ == '__main__':
    one, two, e1, e2, ex1, ex2, r1, r2 = get_solution_booleans(sys.argv)
            
    if e1 or ex1 or r1: print("PART 1")
    if r1: print("Actual Solution:", sol1 := solve1(inp))
