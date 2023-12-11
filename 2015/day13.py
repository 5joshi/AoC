from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    lines = lmap(lambda s: words_and_ints(s.replace('lose ', 'gain -')), d.splitlines())
    attendees = set()
    happiness = {}
    result = 0
    
    for line in lines:
        p1, _, _, units, *_, p2 = line
        happiness[(p1, p2)] = units
        attendees |= {p1, p2}
        
    for permutation in it.permutations(attendees, len(attendees)):
        permutation = list(permutation) + [permutation[0]]
        result = max(result, sum(happiness[(p1, p2)] + happiness[(p2, p1)] for p1, p2 in windows(permutation, 2)))
    
    return result

def solve2(d):
    lines = lmap(lambda s: words_and_ints(s.replace('lose ', 'gain -')), d.splitlines())
    attendees = {"Joshi"}
    happiness = {}
    result = 0
    
    for line in lines:
        p1, _, _, units, *_, p2 = line
        happiness[(p1, p2)] = units
        attendees |= {p1, p2}
        
    for permutation in it.permutations(attendees, len(attendees)):
        permutation = list(permutation) + [permutation[0]]
        result = max(result, sum(happiness.get((p1, p2), 0) + happiness.get((p2, p1), 0) for p1, p2 in windows(permutation, 2)))
    
    return result


s = """
Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.
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