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

inp = get_data(year=2020, day=18)


def solve1(d):
    return eval("+".join([line.count("*")*"("+line.replace("(", line.count("*")*"(").replace(")", line.count("*")*")").replace("*", ")*") for line in d.splitlines()]))


def solve2(d):
    return eval("+".join(["("+line.replace("(", "((").replace(")", "))").replace("*", ")*(")+")" for line in d.splitlines()]))


s = """((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"""
s2 = """"""

print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve1(inp))
print("PART 2")
print("Example Solution:", solve2(s))
# print("Example 2 Solution:", solve2(s2))
print("Actual Solution:", solve2(inp))
