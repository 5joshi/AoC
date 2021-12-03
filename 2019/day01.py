import collections as coll
import datetime as dt
import functools as ft
import itertools as it
import math
from operator import itemgetter as ig
import pprint as pp
import re
from copy import deepcopy
from utils import *
from functools import reduce
from aocd import get_data, submit

inp = get_data(year=2019, day=1)


def solve1(d):
    inp = ints(d)
    return sum([n // 3 - 2 for n in inp])

def solve2(d):
    inp = ints(d)
    result = 0
    for n in inp:
        while n > 0:
            n = n // 3 - 2 
            result += max(0, n)
    return result


s = """12
"""
s2 = """100756
"""

print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve1(inp))

print("PART 2")
print("Example Solution:", solve2(s))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve2(inp))
