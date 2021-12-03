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

inp = get_data(year=2020, day=13)


def solve1(d):
    inp = ints(d)
    time = inp[0]
    m = inp[1]
    mn = 0
    for elem in inp[1:]:
        if (elem - (time % elem)) < m:
            m = (elem - (time % elem))
            mn = elem
    return m * mn


def solve2(d):
    inp = ints(d.replace("x", "1"))[1:]
    N = math.prod(inp)
    inp = list(filter(lambda x: x[1] != 1, enumerate(inp)))
    inp = lmap(lambda a: (a[1], (a[1] - a[0]) % a[1], N // a[1]), inp)
    return sum(map(lambda x: x[1] * x[2] * pow(x[2], -1, x[0]), inp)) % N


s = """939
7,13,x,x,59,x,31,19
"""
s2 = """121
1789,37,47,1889"""
s3 = """1313
17,x,13,19"""

print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve(s2))
# print("Example 3 Solution:", solve1(s3))
print("Actual Solution:", solve1(inp))
print("PART 2")
print("Example Solution:", solve2(s))
print("Example 2 Solution:", solve2(s2))
print("Example 3 Solution:", solve2(s3))
print("Actual Solution:", solve2(inp))
