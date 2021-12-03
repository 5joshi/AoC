import collections as coll
import datetime as dt
import itertools as it
import math
from operator import itemgetter as ig
import pprint as pp
import re
from utils import *
from aocd import get_data

inp = get_data(year=2020, day=1)


def solve1(d):
    nums = ints(d)
    for a, b in it.combinations(nums, 2):
        if a+b == 2020:
            return a*b


def solve2(d):
    nums = ints(d)
    for a, b, c in it.combinations(nums, 3):
        if a+b+c == 2020:
            return a*b*c


s = """
1721
979
366
299
675
1456

"""
s2 = """

"""

print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve1(inp))
print("PART 2")
print("Example Solution:", solve2(s))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve2(inp))
