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

inp = get_data(year=2021, day=9)


def solve1(d):
    grid = lmap(lambda l: [int(x) for x in l], d.splitlines())
    result = 0
    for x, row in enumerate(grid):
        for y, val in enumerate(row):
            if all([val < neighbor for neighbor in get_neighbors(grid, x, y, GRID_DELTA)]):
                result += val + 1
    return result

def solve2(d):
    grid = lmap(lambda l: [int(x) for x in l], d.splitlines())
    basins = []
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if all([val < neighbor for neighbor in get_neighbors(grid, i, j, GRID_DELTA)]):
                to_check = [(i, j)]
                basin = {(i, j)}
                while to_check:
                    x, y = to_check[0]
                    valid_neighbors = {(nx, ny) for (nx, ny) in get_neighbors_coords(grid, x, y, GRID_DELTA) if grid[nx][ny] != 9}
                    to_check.extend([n for n in valid_neighbors if n not in basin])
                    basin.update(valid_neighbors)
                    to_check.pop(0)
                basins.append(len(basin))
    result = math.prod(sorted(basins)[-3:])       
    return result           


s = """2199943210
3987894921
9856789892
8767896789
9899965678
"""
s2 = """
"""

print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve1(s2))
print("Actual Solution:", solve1(inp))

print("PART 2")
print("Example Solution:", solve2(s))
# print("Example 2 Solution:", solve2(s2))
print("Actual Solution:", solve2(inp))
