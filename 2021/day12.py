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

inp = get_data(year=2021, day=12)


def solve1(d):
    inp = d.splitlines()
    cave = coll.defaultdict(set)
    
    for line in inp:
        start, end = line.split("-")
        cave[start].add(end)
        cave[end].add(start)
    
    def paths(curr, seen=set()):
        if curr == "end": return 1
        if curr.islower() and curr in seen: return 0
        seen = seen | {curr}
        return sum([paths(nxt, seen) for nxt in cave[curr]])
     
    result = paths("start")
    return result
    

def solve2(d):
    inp = d.splitlines()
    cave = coll.defaultdict(set)
    
    for line in inp:
        start, end = line.split("-")
        cave[start].add(end)
        cave[end].add(start)
    
    def paths(curr, seen=set(), double=False):
        if curr == "end": return 1
        if curr == "start" and seen: return 0
        if curr.islower() and curr in seen: 
            if double: return 0
            else: double = True
        seen = seen | {curr}
        return sum([paths(nxt, seen, double) for nxt in cave[curr]])
     
    result = paths("start")
    return result



s = """start-A
start-b
A-c
A-b
b-d
A-end
b-end
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
