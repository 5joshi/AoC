from utils import *

inp = get_data(year=2022, day=1)


def solve1(d):
    return max([sum(ints(l)) for l in d.split("\n\n")])

def solve2(d):
    return sum(sorted([sum(ints(l)) for l in d.split("\n\n")])[-3:])


s = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""
s2 = """
"""

print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve1(s2))
print("Actual Solution:", solve1(inp))

print("PART 2")
print("Example Solution:", solve2(s))
# # print("Example 2 Solution:", solve2(s2))
print("Actual Solution:", solve2(inp))
