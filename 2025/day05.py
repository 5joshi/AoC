from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    ranges, nums = d.split("\n\n")
    ranges = lmap(positive_ints, ranges.splitlines())
    nums = ints(nums)
    
    return sum(any(lo <= num <= hi for lo, hi in ranges) for num in nums)

def solve2(d):
    ranges = sorted(lmap(positive_ints, d.split("\n\n")[0].splitlines()))
    new_ranges = [ranges[0]]

    for lo, hi in ranges[1:]:
        if lo <= new_ranges[-1][1]:
            new_ranges[-1][1] = max(new_ranges[-1][1], hi)
        else:
            new_ranges.append([lo, hi])

    return sum(hi - lo + 1 for lo, hi in new_ranges)


s = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32

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