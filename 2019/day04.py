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

inp = get_data(year=2019, day=4)


def solve1(d):
    lo, hi = map(int, d.split('-'))
    result = 0
    
    def doublenum(password):
        return any([x == y for (x, y) in zip(password, password[1:])])
    
    def increasing(password):
        return all([x <= y for (x, y) in zip(password, password[1:])])
    
    for i in range(lo, hi+1):
        password = str(i).zfill(6)
        if doublenum(password) and increasing(password):
            result += 1
    return result

def solve2(d):
    lo, hi = map(int, d.split('-'))
    result = 0
    
    def doublenum(password):
        return any([x == y and a != x and b != y for (a, x, y, b) in zip(password, password[1:], password[2:], password[3:])])
    
    def increasing(password):
        return all([x <= y for (x, y) in zip(password, password[1:])])
    
    for i in range(lo, hi+1):
        password = "-" + str(i).zfill(6) + "-"
        if doublenum(password) and increasing(password[1:-1]):
            result += 1
    return result


s = """
"""
s2 = """
"""

print("PART 1")
# print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve1(s2))
print("Actual Solution:", solve1(inp))

print("PART 2")
# print("Example Solution:", solve2(s))
# print("Example 2 Solution:", solve2(s2))
print("Actual Solution:", solve2(inp))