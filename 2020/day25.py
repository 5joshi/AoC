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

inp = get_data(day=25)


def get_loop_size(target, subject=7):
    loops = 0
    result = 1
    while result != target:
        loops += 1
        result = result * subject % 20201227
    return loops


def solve1(d):
    card, door = ints(d)
    card_loops = get_loop_size(card)
    door_loops = get_loop_size(door)
    result = 1
    for i in range(card_loops):
        result = result * door % 20201227
    return result


s = """5764801
17807724"""
s2 = """"""

print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve1(inp))
