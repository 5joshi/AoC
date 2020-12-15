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

inp = get_data(day=15)


def solve(d, idx):
    inp = ints(d)
    seen = coll.Counter()
    add_next = to_num = -1
    for i, x in enumerate(inp):
        seen[x] = i+1
    while len(inp) < idx:
        if not seen[inp[-1]]:
            num = 0
        else:
            num = len(inp) - seen[inp[-1]]
        seen[to_num] = add_next
        inp.append(num)
        add_next, to_num = len(inp), num
    return inp[idx-1]


s = """1,3,2"""
s2 = """15,5,1,4,7,0"""

print("PART 1")
print("Example Solution:", solve(s, 2020))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve(inp, 2020))
print("PART 2")
print("Example Solution:", solve(s, 30000000))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve(inp, 30000000))
