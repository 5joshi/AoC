from utils import *

inp = get_data(year=2023, day=9)

def next_num(nums):
    result = nums[-1]
    while any(nums):
        nums = list_diff(nums)
        result += nums[-1]
    return result

def solve1(d):
    return sum(map(lambda line: next_num(ints(line)), d.splitlines()))


def solve2(d):
    return sum(map(lambda line: next_num(ints(line)[::-1]), d.splitlines()))


s = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
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
