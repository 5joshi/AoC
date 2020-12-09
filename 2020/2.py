import collections as coll
import datetime as dt
import itertools as it
import math
from operator import itemgetter as ig
import pprint as pp
import re
from utils import *
from aocd import get_data

inp = get_data(day=2)


def solve1(d):
    result = 0
    for elem in d.splitlines():
        lo, hi = positive_ints(elem)
        char, word = words(elem)
        result += (lo <= word.count(char) <= hi)
    return result


def solve2(d):
    result = 0
    for elem in d.splitlines():
        lo, hi = positive_ints(elem)
        char, word = words(elem)
        result += (((word[lo-1] == char) + (word[hi-1] == char)) == 1)
    return result


s = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""
s2 = """"""
print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve1(inp))
print("PART 2")
print("Example Solution:", solve2(s))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve2(inp))
