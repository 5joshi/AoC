import collections as coll
import datetime as dt
import functools as ft
import itertools as it
import math
from operator import itemgetter as ig
import pprint
import re
from copy import deepcopy
from utils import *
from functools import reduce
from aocd import get_data, submit

inp = get_data(day=11)


def solve1(d):
    inp = lmap(list, d.splitlines())
    change = True
    while change:
        change = False
        cpy = deepcopy(inp)
        for x in range(len(inp)):
            for y in range(len(inp[0])):
                neighbors = get_neighbors(cpy, x, y, OCT_DELTA)
                if cpy[x][y] == "L" and neighbors.count("#") == 0:
                    inp[x][y] = "#"
                    change = True
                elif cpy[x][y] == "#" and neighbors.count("#") >= 4:
                    inp[x][y] = "L"
                    change = True
    return sum(map(lambda x: x.count("#"), inp))


def get_neighbors2(grid, row, col, deltas):
    n, m = len(grid), len(grid[0])
    out = []
    for i, j in deltas:
        p_row, p_col = row+i, col+j
        while 0 <= p_row < n and 0 <= p_col < m and grid[p_row][p_col] == ".":
            p_row += i
            p_col += j
        if 0 <= p_row < n and 0 <= p_col < m:
            out.append(grid[p_row][p_col])
    return out


def solve2(d):
    inp = lmap(list, d.splitlines())
    change = True
    while change:
        change = False
        cpy = deepcopy(inp)
        for x in range(len(inp)):
            for y in range(len(inp[0])):
                neighbors = get_neighbors2(cpy, x, y, OCT_DELTA)
                if cpy[x][y] == "L" and neighbors.count("#") == 0:
                    inp[x][y] = "#"
                    change = True
                elif cpy[x][y] == "#" and neighbors.count("#") >= 5:
                    inp[x][y] = "L"
                    change = True
    return sum(map(lambda x: x.count("#"), inp))


s = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""
s2 = """"""

print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve1(inp))
# submit(solve(inp))
print("Example Solution:", solve2(s))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve2(inp))
# submit(solve(inp))
