from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d, n=25):
    counts = Counter(ints(d))
    
    for _ in range(n):
        new_counts = Counter()
        for num, count in counts.items():
            if num == 0: new_counts[1] += count
            elif (d := int(math.log10(num)) + 1) % 2 == 0: 
                new_counts[num // 10 ** (d // 2)] += count
                new_counts[num % 10 ** (d // 2)] += count
            else: new_counts[num * 2024] += count
        counts = new_counts
    
    return sum(counts.values())

def solve2(d):
    return solve1(d, 75)


s = """
125 17""".strip()
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