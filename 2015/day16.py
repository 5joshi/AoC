from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

GIFT = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

def solve1(d):    
    for _, idx, *items in lmap(words_and_ints, d.splitlines()):
        if all(GIFT[item] == count for item, count in every_n(items, 2)):
            return idx
    
def solve2(d):
    for _, idx, *items in lmap(words_and_ints, d.splitlines()):
        if all(GIFT[item] == count for item, count in every_n(items, 2) if item not in ['cats', 'trees', 'pomeranians', 'goldfish']) \
            and all(GIFT[item] < count for item, count in every_n(items, 2) if item in ['cats', 'trees']) \
            and all(GIFT[item] > count for item, count in every_n(items, 2) if item in ['pomeranians', 'goldfish']):
            return idx


s = """

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