from utils import *

inp = get_data(year=2021, day=14)


def solve1(d):
    x, rules = d.split("\n\n")
    m = dict()
    for rule in rules.splitlines():
        fst, snd = rule.split(" -> ")
        m[fst] = fst[0] + snd + fst[1]
        
    for _ in range(10):
        new_x = x[0]
        for l1, l2 in zip(x, x[1:]):
            new_x += m[l1 + l2][1:]
        x = new_x
        
    count = Counter(x)
    return max_minus_min(count.values())

def solve2(d):
    x, rules = d.split("\n\n")
    m = dict()
    for rule in rules.splitlines():
        fst, snd = rule.split(" -> ")
        m[fst] = fst[0] + snd + fst[1]
        
    bigram_count = Counter([a+b for a,b in zip(x, x[1:])])
    letter_count = Counter(x)
    for _ in range(40):
        new_count = Counter()
        for key, rule in m.items():
            w = bigram_count[key]
            new_count[rule[:2]] += w
            new_count[rule[1:]] += w
            letter_count[rule[1]] += w
        bigram_count = new_count
        
    return max_minus_min(letter_count.values())


s = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""
s2 = """
"""

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
