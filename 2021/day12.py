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
    
    idx = 0         
    paths = [["start"]]
    while idx != len(paths):
        path = paths[idx]
        if path[-1] == "end": 
            idx += 1
        else:
            for nxt in cave[path[-1]]:
                if not (nxt.islower() and nxt in path): 
                    paths.append(path + [nxt])
            paths.pop(idx)
    
    result = len(paths)
    return result
    

def solve2(d):
    inp = d.splitlines()
    cave = coll.defaultdict(set)
    
    for line in inp:
        start, end = line.split("-")
        if end != "start": cave[start].add(end)
        if start != "start": cave[end].add(start)
    lower = {key for key in cave.keys() if key.islower() and key not in ["start", "end"]}

    idx = 0         
    paths = [["start"]]
    while idx != len(paths):
        path = paths[idx]
        if path[-1] == "end": 
            idx += 1
        else:
            for nxt in cave[path[-1]]:
                if not (nxt.islower() and nxt in path) or not any([path.count(key) >= 2 for key in lower]): 
                    paths.append(path + [nxt])
            paths.pop(idx)
    
    result = len(paths)
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
