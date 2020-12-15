import collections as coll
import datetime as dt
import itertools as it
import functools as ft
import math
from operator import itemgetter as ig
import pprint as pp
import re
from utils import *
from aocd import get_data, submit

inp = get_data(day=6)


def solve1(d):
    inp = d.split("\n\n")
    result = 0
    for elem in inp:
        elem = elem.splitlines()
        result += len(set("".join(elem)))
    return result


def solve2(d):
    inp = d.split("\n\n")
    result = 0
    for elem in inp:
        elem = elem.splitlines()
        result += len(ft.reduce(lambda a,
                                b: a.intersection(b), map(set, elem)))
    return result


s = """abc

a
b
c

ab
ac

a
a
a
a

b
"""
s2 = """"""

print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve1(inp))
# submit(solve(inp))
print("PART 2")
print("Example Solution:", solve2(s))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve2(inp))
# submit(solve(inp))
