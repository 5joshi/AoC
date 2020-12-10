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

inp = get_data(day=10)


def solve1(d):
    inp = [0] + sorted(ints(d))
    inp.append(inp[-1] + 3)
    inp = list_diff(inp)
    return inp.count(1) * inp.count(3)


def solve2(d):
    inp = sorted(ints(d))
    inp.append(inp[-1] + 3)
    poss = [0] * (inp[-1] + 1)
    poss[0] = 1
    for elem in inp:
        poss[elem] = poss[elem-1] + poss[elem-2] + poss[elem-3]
    return poss[-1]


s = """16
10
15
5
1
11
7
19
6
12
4
"""
s2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""

print("PART 1")
print("Example Solution:", solve1(s))
print("Example 2 Solution:", solve1(s2))
print("Actual Solution:", solve1(inp))
# submit(solve(inp))
print("PART 2")
print("Example Solution:", solve2(s))
print("Example 2 Solution:", solve2(s2))
print("Actual Solution:", solve2(inp))
# submit(solve(inp))
