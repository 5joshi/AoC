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

if __name__ == '__main__':
    e1, e2, ex1, ex2, r1, r2 = get_solution_booleans(sys.argv)
            
    if e1 or ex1 or r1: print("PART 1")
    if e1: print("Example Solution:", solve1(s))
    if ex1: print("Example 2 Solution:", solve1(s2))
    if r1: print("Actual Solution:", solve1(inp))

    if e2 or ex2 or r2: print("PART 2")
    if e2: print("Example Solution:", solve2(s))
    if ex2: print("Example 2 Solution:", solve2(s2))
    if r2: print("Actual Solution:", solve2(inp))
