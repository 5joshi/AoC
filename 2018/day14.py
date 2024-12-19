from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    target = int(d)
    scores = [3, 7]
    a, b = 0, 1
    
    while len(scores) < target + 10:
        scores += lmap(int, list(str(scores[a] + scores[b])))
        a = (a + scores[a] + 1) % len(scores)
        b = (b + scores[b] + 1) % len(scores)
    
    return "".join(lmap(str, scores[target:target+10]))

def solve2(d):
    target = d
    scores = "37"
    a, b = 0, 1
    
    while target not in scores[-len(target)-1:]:
        scores += str(int(scores[a]) + int(scores[b]))
        a = (a + int(scores[a]) + 1) % len(scores)
        b = (b + int(scores[b]) + 1) % len(scores)
    
    return scores.index(target)


s = """
51589
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