import collections as coll
import datetime as dt
import itertools as it
import math
from operator import itemgetter as ig
import pprint as pp
import re
from utils import *
from aocd import get_data, submit

inp = get_data(year=2020, day=5)


def solve1(d):
    seats = d.replace("F", "0").replace(
        "B", "1").replace("L", "0").replace("R", "1")
    seats = map(lambda a: int(a, 2), seats.splitlines())
    return max(seats)


def solve2(d):
    seats = d.replace("F", "0").replace(
        "B", "1").replace("L", "0").replace("R", "1")
    seats = lmap(lambda a: int(a, 2), seats.splitlines())
    seats.sort()
    for i in range(1, len(seats)):
        if (seats[i] - 2) == seats[i-1]:
            return seats[i] - 1


s = """BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL"""
s2 = """"""

print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve1(inp))
# submit(solve(inp))
print("PART 2")
# print("Example Solution:", solve2(s))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve2(inp))
# submit(solve(inp))
