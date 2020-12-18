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

inp = get_data(day=18)


def solve1(d):
    inp = d.splitlines()
    result = 0
    for line in inp:
        count = line.count("*")
        result += eval(count*"("+line.replace("(", count *
                                              "(").replace(")", count*")").replace(" *", ") *"))
    return result


def solve2(d):
    inp = d.splitlines()
    result = 0
    for line in inp:
        result += eval("("+line.replace("(",
                                        "((").replace(")", "))").replace(" * ", ")*(")+")")
    return result


s = """((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"""
s2 = """"""

print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve1(inp))
print("PART 2")
print("Example Solution:", solve2(s))
print("Example 2 Solution:", solve2(s2))
print("Actual Solution:", solve2(inp))
