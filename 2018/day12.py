from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d, g=20):
    curr, rules = d.split("\n\n")
    curr = {idx for idx, c in enumerate(curr.split()[-1]) if c == '#'}
    rules = lmap(lambda r: r.split(" => "), rules.splitlines())
    rules = [lmap(lambda x: x == "#", x) for x, c in rules if c == "#"]
    
    for _ in range(g):
        nxt = set()
        for idx in range(min(curr) - 2, max(curr) + 3):
            if [j in curr for j in range(idx - 2, idx + 3)] in rules:
                nxt |= {idx}
        curr = nxt
    
    return sum(curr)

def solve2(d):
    s1, s2 = solve1(d, 1000), solve1(d, 999)
    return (50_000_000_000 - 1000) * (s1 - s2) + s1


s = """
initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #

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