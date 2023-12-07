from utils import *

inp = get_data(year=2023, day=4)

def solve1(d):
    inp = lmap(lambda split: len(set(ints(split[1])).intersection(set(ints(split[2])))), 
               map(lambda line: re.split(r'[:|]', line), d.splitlines())) 
    return sum([(2 ** (matching - 1)) if matching else 0 for matching in inp])

def solve2(d):
    inp = lmap(lambda split: len(set(ints(split[1])).intersection(set(ints(split[2])))), 
               map(lambda line: re.split(r'[:|]', line), d.splitlines())) 
    copies = [0] * len(inp)
    
    for idx, matches in enumerate(inp):
        copies[idx] += 1
        for match in range(matches):
            copies[idx + match + 1] += copies[idx]

    return sum(copies)


s = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
""".strip()
s2 = """

""".strip()

if __name__ == '__main__':
    e1, e2, ex1, ex2, r1, r2 = get_solution_booleans(sys.argv)
            
    if e1 or ex1 or r1: print("PART 1")
    if e1: print("Example Solution:", solve1(s))
    if ex1: print("Example 2 Solution:", solve1(s2))
    if r1: print("Actual Solution:", solve1(inp))

    if e2 or ex2 or r2: print("PART 2")
    if e2: print("Example Solution:", solve2(s))
    if ex2: print("Example 2 Solution:", solve2(s2))
    if r2: print("Actual Solution:", solve2(inp))