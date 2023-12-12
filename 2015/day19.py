from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    *rules, _, start = map(words, d.splitlines())
    start = start[0]
    molecules = set()
    for frm, to in rules:
        for idx in range(len(start)):
            if start[idx:idx+len(frm)] == frm:
                molecules.add(start[:idx] + to + start[idx+len(frm):])
        
    return len(molecules)

# https://www.reddit.com/r/adventofcode/comments/3xflz8/comment/cy4etju
def solve2(d):
    *_, goal = d.splitlines()
    return len(re.findall(r"[A-Z]", goal)) - 2 * len(re.findall(r"Rn", goal)) - 2 * len(re.findall(r"Y", goal)) - 1

s = """
e => H
e => O
H => HO
H => OH
O => HH

HOH
""".strip()
s2 = """
e => NAl
e => OMg

NAl
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