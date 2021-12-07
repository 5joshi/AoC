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

inp = get_data(year=2021, day=2)


def solve1(d):
    inp = d.splitlines()
    horizontal = depth = 0
    for line in inp:
        action, num = line.split()
        num = int(num)
        match action:
            case "up":
                depth -= num
            case "down":
                depth += num
            case "forward":
                horizontal += num 
        # if action[0] == "u":
        #     depth -= num
        # elif action[1] == "d":
        #     depth += num
        # else:
        #     horizontal += num
    return horizontal * depth

def solve2(d):
    inp = d.splitlines()
    horizontal = depth = aim = 0
    for line in inp:
        action, num = line.split()
        num = int(num)
        match action:
            case "up":
                aim -= num
            case "down":
                aim += num
            case "forward":
                horizontal += num 
                depth += aim * num
        # if action[0] == "u":
        #     aim -= num
        # elif action[1] == "d":
        #     aim += num
        # else:
        #     horizontal += num 
        #     depth += aim * num
    return horizontal * depth


s = """forward 5
down 5
forward 8
up 3
down 8
forward 2
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
