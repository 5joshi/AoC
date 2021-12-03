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

inp = get_data(year=2020, day=12)


def solve1(d):
    inp = d.splitlines()
    ship = (0, 0)
    dir = (0, 1)
    for line in inp:
        instr = line[0]
        num = int(line[1:])
        if instr in "NESW":
            ship = padd(ship, pmul(num, CHAR_TO_DELTA[instr]))
        elif instr == "L":
            for i in range(num // 90):
                dir = turn_left(dir)
        elif instr == "R":
            for i in range(num // 90):
                dir = turn_right(dir)
        else:
            ship = padd(ship, pmul(num, dir))

    return pdist1(ship)


def solve2(d):
    inp = d.splitlines()
    waypoint = (-1, 10)
    ship = (0, 0)
    for line in inp:
        instr = line[0]
        num = int(line[1:])
        if instr in "NESW":
            waypoint = padd(waypoint, pmul(num, CHAR_TO_DELTA[instr]))
        elif instr == "L":
            for i in range(num // 90):
                waypoint = turn_left(waypoint)
        elif instr == "R":
            for i in range(num // 90):
                waypoint = turn_right(waypoint)
        else:
            ship = padd(ship, pmul(num, waypoint))

    return pdist1(ship)


s = """F10
N3
F7
R90
F11
"""
s2 = """"""

print("PART 1:")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve1(inp))

print("PART 2:")
print("Example Solution:", solve2(s))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve2(inp))
