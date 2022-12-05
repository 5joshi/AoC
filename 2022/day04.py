from utils import *

inp = get_data(year=2022, day=4)


def solve1(d):
    inp = lmap(positive_ints, d.splitlines())
    return sum([(x1 <= y1 <= y2 <= x2) or (y1 <= x1 <= x2 <= y2) for x1, x2, y1, y2 in inp])

def solve2(d):
    inp = lmap(positive_ints, d.splitlines())
    return sum([min(x2, y2) >= max(x1, y1) for x1, x2, y1, y2 in inp])


s = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""
s2 = """
"""

print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve1(s2))
print("Actual Solution:", solve1(inp))

# print("PART 2")
print("Example Solution:", solve2(s))
# # print("Example 2 Solution:", solve2(s2))
print("Actual Solution:", solve2(inp))
