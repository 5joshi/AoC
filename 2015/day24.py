from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)


def solve1(d):
    weights = tuple(ints(d))
    goal = sum(weights) // 3
    result = []
    
    def sum_to_n(idx, c, n):
        if n == 0: return result.append(c.copy())

        for i in range(idx, len(weights)):
            if weights[i] > n or weights[i] in c:
                continue

            c.append(weights[i])
            sum_to_n(i, c, n - weights[i])
            c.pop()

    sum_to_n(0, [], goal)        
    return product(min(result, key=lambda x: (len(x), product(x))))
    

def solve2(d):
    weights = tuple(ints(d))
    goal = sum(weights) // 4
    result = []
    
    def sum_to_n(idx, c, n):
        if n == 0: return result.append(c.copy())

        for i in range(idx, len(weights)):
            if weights[i] > n or weights[i] in c:
                continue

            c.append(weights[i])
            sum_to_n(i, c, n - weights[i])
            c.pop()

    sum_to_n(0, [], goal)        
    return product(min(result, key=lambda x: (len(x), product(x))))


s = """
1 2 3 4 5 7 8 9 10 11
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