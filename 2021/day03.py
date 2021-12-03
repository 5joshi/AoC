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

inp = get_data(year=2021, day=3)


def common(idx, l):
    result = coll.Counter([s[idx] for s in l]).most_common()
    if len(result) == 2 and result[0][1] == result[1][1] and result[0][0] == "0":
        result.reverse()
    return result

def solve1(d):
    inp = d.splitlines()
    size = len(inp[0])
    gamma = int("".join([common(i, inp)[0][0] for i in range(size)]), 2)
    epsilon = int("".join([common(i, inp)[1][0] for i in range(size)]), 2)
    return gamma * epsilon

def solve2(d):
    inp = d.splitlines()
    nums1 = nums2 = inp
    idx1 = idx2 = 0
    while len(nums1) > 1:
        comm = common(idx1, nums1)[0][0]
        nums1 = list(filter(lambda n: n[idx1] == comm, nums1))
        idx1 += 1
    while len(nums2) > 1:
        comm = common(idx2, nums2)[0][0]
        nums2 = list(filter(lambda n: n[idx2] != comm, nums2))
        idx2 += 1   
    oxygen = int(nums1[0], 2) 
    co2 = int(nums2[0], 2)   
    return oxygen * co2


s = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""
s2 = """
"""

print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve1(inp))

print("PART 2")
print("Example Solution:", solve2(s))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve2(inp))
