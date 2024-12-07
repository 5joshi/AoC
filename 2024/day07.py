from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    lines = lmap(ints, d.splitlines())
    result = 0
    
    for total, *nums in lines:        
        outcomes = {nums[0]}
        for num in nums[1:]:
            new_outcomes = set()
            for outcome in outcomes:
                new_outcomes |= {outcome + num, outcome * num}
            outcomes = {x for x in new_outcomes if x <= total}
        result += total * (total in outcomes)
    
    return result

def solve2(d):
    lines = lmap(ints, d.splitlines())
    result = 0
    
    for total, *nums in lines:        
        outcomes = {nums[0]}
        for num in nums[1:]:
            new_outcomes = set()
            for outcome in outcomes:
                new_outcomes |= {outcome + num, outcome * num, int(f"{outcome}{num}")}
            outcomes = {x for x in new_outcomes if x <= total}
        result += total * (total in outcomes)
    
    return result


s = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20

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