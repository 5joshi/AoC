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
import statistics
from aocd import get_data, submit

inp = get_data(year=2021, day=7)


def solve1(d):
    inp = lmap(int, d.split(','))    
    
    def calc(n):
        return sum([abs(a - n) for a in inp])
            
    # result = calc(min(range(*min_max(inp)), key=calc))
    return calc(int(median(inp)))

def solve2(d):
    inp = lmap(int, d.split(','))
    
    def calc(n):
        return sum([gauss_sum(abs(a - n)) for a in inp])

    result = calc(min(range(*min_max(inp)), key=calc))
    return result


s = """16,1,2,0,4,2,7,1,2,14
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
