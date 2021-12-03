import collections as coll
import datetime as dt
import itertools as it
import math
from operator import itemgetter as ig
import pprint as pp
import re
from utils import *
from aocd import get_data, submit

inp = get_data(year=2020, day=9)


def solve1(d, size=25):
    i = ints(d)
    for x in range(size, len(i)):
        possible = False
        for a, b in it.combinations(i[x-size:x], 2):
            if a + b == i[x]:
                possible = True
        if not possible:
            return i[x]


def solve2(d, size=25):
    i = ints(d)
    result = solve1(d, size)
    for x in range(2, len(i)):
        for y in range(len(i) - x):
            if sum(i[y:y+x]) == result:
                return sum(min_max(i[y:y+x]))


s = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
"""
s2 = """"""

print("PART 1")
print("Example Solution:", solve1(s, 5))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve1(inp))
# submit(solve(inp))

print("PART 2")
print("Example Solution:", solve2(s, 5))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve2(inp))
