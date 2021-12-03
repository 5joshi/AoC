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

inp = get_data(day=1)


def solve1(d):
    inp = ints(d)
    result = sum([inp[i+1] > inp[i] for i in range(len(inp) - 1)])
    return result

def solve2(d):
    inp = ints(d)
    result = sum([sum(inp[i+1:i+4]) > sum(inp[i:i+3]) for i in range(len(inp) - 3)])
    return result


s = """
199
200
208
210
200
207
240
269
260
263
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
