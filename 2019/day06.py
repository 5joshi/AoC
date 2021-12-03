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
from queue import Queue
from aocd import get_data, submit

inp = get_data(year=2019, day=6)

def solve1(d):
    inp = d.splitlines()
    all_orbits = coll.defaultdict(set)
    for line in inp:
        a, b = line.split(")")
        all_orbits[b].add(a)#.union(all_orbits[a])
    while True:
        before = sum([len(orbits[1]) for orbits in all_orbits.items()])
        for key, items in sorted(all_orbits.items(), key=lambda x: len(x[0])):
            for item in items:
                all_orbits[key] = all_orbits[key].union(all_orbits[item])
        if sum([len(orbits[1]) for orbits in all_orbits.items()]) == before: 
            return before

def solve2(d):
    inp = d.splitlines()
    all_orbits = coll.defaultdict(set)
    for line in inp:
        a, b = line.split(")")
        all_orbits[b].add(a)
        all_orbits[a].add(b)
    return bfs("YOU", lambda x: all_orbits[x], "SAN")[0]["SAN"] - 2        

s = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
"""
s2 = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN
"""

print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve1(s2))
print("Actual Solution:", solve1(inp))

print("PART 2")
print("Example Solution:", solve2(s2))
# print("Example 2 Solution:", solve2(s2))
print("Actual Solution:", solve2(inp))