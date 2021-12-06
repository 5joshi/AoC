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

inp = get_data(year=2021, day=6)


def solve1(d):
    inp = ints(d)
    counter = coll.Counter(inp)
    for _ in range(80):
        new_counter = coll.Counter()
        for key, item in counter.items():
            if key == 0:
                new_counter[6] += item
                new_counter[8] += item
            else:
                new_counter[key-1] += item
        counter = new_counter
    result = sum(counter.values())
    return result

def solve2(d):
    inp = ints(d)
    counter = coll.Counter(inp)
    for _ in range(256):
        new_counter = coll.Counter()
        for key, item in counter.items():
            if key == 0:
                new_counter[6] += item
                new_counter[8] += item
            else:
                new_counter[key-1] += item
        counter = new_counter
    result = sum(counter.values())
    return result


s = """3,4,3,1,2
"""
s2 = """
"""

print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve1(s2))
print("Actual Solution:", solve1(inp))

print("PART 2")
print("Example Solution:", solve2(s))
# print("Example 2 Solution:", solve2(s2))
print("Actual Solution:", solve2(inp))
