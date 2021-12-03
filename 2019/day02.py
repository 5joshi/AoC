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

inp = get_data(year=2019, day=2)


def solve1(d, noun=12, verb=2):
    inp = ints(d)
    if noun and verb:
        inp[1] = noun
        inp[2] = verb
    idx = 0
    while inp[idx] != 99:
        if inp[idx] == 1:
            inp[inp[idx+3]] = inp[inp[idx+1]] + inp[inp[idx+2]]
        elif inp[idx] == 2:
            inp[inp[idx+3]] = inp[inp[idx+1]] * inp[inp[idx+2]]
        idx += 4
    return inp[0]

def solve2(d):
    for noun, verb in it.product(range(100), repeat=2):
        if solve1(d, noun, verb) == 19690720:
            return 100 * noun + verb


s = """1,9,10,3,2,3,11,0,99,30,40,50
"""
s2 = """
"""

print("PART 1")
print("Example Solution:", solve1(s, None, None))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve1(inp))

print("PART 2")
# print("Example Solution:", solve2(s))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve2(inp))
