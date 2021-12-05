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

inp = get_data(year=2021, day=5)


def solve1(d):
    grid = coll.defaultdict(int)
    inp = d.splitlines()
    
    for line in inp:
        x1, y1, x2, y2 = ints(line)
        if not (x1 == x2 or y1 == y2): continue
        delta = ((x1!=x2) * (-1) ** (x2<x1), (y1!=y2) * (-1) ** (y2<y1))
        
        while (x1, y1) != tuple(padd((x2, y2), delta)):
            grid[(x1, y1)] += 1
            (x1, y1) = padd((x1, y1), delta)
    
    result = sum([num >= 2 for _, num in grid.items()])
    return result

def solve2(d):
    grid = coll.defaultdict(int)
    inp = d.splitlines()
    
    for line in inp:
        x1, y1, x2, y2 = ints(line)
        delta = ((x1!=x2) * (-1) ** (x2<x1), (y1!=y2) * (-1) ** (y2<y1))
            
        while (x1, y1) != tuple(padd((x2, y2), delta)):
            grid[(x1, y1)] += 1
            (x1, y1) = padd((x1, y1), delta)
    
    result = sum([num >= 2 for _, num in grid.items()])
    return result


s = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
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
