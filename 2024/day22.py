from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)


def solve1(d):
    result = 0
    for num in ints(d):
        curr = num
        for _ in range(2000):
            curr ^= (curr << 6) 
            curr %= 16777216 
            curr ^= (curr >> 5)
            curr %= 16777216 
            curr ^= (curr << 11) 
            curr %= 16777216       
        result += curr
    return result

def solve2(d):
    values = Counter()
    for num in ints(d):
        curr = num
        lcurr = [curr % 10]
        for _ in range(2000):
            curr ^= (curr << 6) 
            curr %= 16777216 
            curr ^= (curr >> 5)
            curr %= 16777216 
            curr ^= (curr << 11) 
            curr %= 16777216       
            lcurr.append(curr % 10)
        curr_values = Counter()
        for w, v in zip(windows(list_diff(lcurr), 4), lcurr[4:]):
            if w not in curr_values: curr_values[w] = v
        values += curr_values
    return values.most_common(1)[0][1]


s = """
1
10
100
2024


""".strip()
s2 = """
123
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