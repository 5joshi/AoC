from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    rules, pages = lmap(lambda x: lmap(ints, x.splitlines()), d.split("\n\n"))
    result = 0

    rules_dict = defaultdict(set)
    for a, b in rules:
        rules_dict[a].add(b)
    
    for page in pages:
        order = sorted(page, key=lambda x: len(rules_dict[x] & set(page)), reverse=True)
        if page == order: result += page[len(page) // 2]
    
    return result

def solve2(d):
    rules, pages = lmap(lambda x: lmap(ints, x.splitlines()), d.split("\n\n"))
    result = 0

    rules_dict = defaultdict(set)
    for a, b in rules:
        rules_dict[a].add(b)
    
    for page in pages:
        order = sorted(page, key=lambda x: len(rules_dict[x] & set(page)), reverse=True)
        if page != order: result += order[len(order) // 2]
    
    return result


s = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47

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