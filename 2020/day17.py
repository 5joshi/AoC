import collections as coll
import datetime as dt
import functools as ft
import itertools as it
import math
from operator import itemgetter as ig
from pprint import pprint
import re
from copy import deepcopy
from utils import *
from functools import reduce
from aocd import get_data, submit

inp = get_data(year=2020, day=17)

DELTA_3D = list(filter(
    lambda x: x != (0, 0, 0), it.product([-1, 0, 1], repeat=3)))

DELTA_4D = list(filter(
    lambda x: x != (0, 0, 0, 0), it.product([-1, 0, 1], repeat=4)))


def get_neighbors_count(grid, coord, delta):
    neighbors = 0
    for d in delta:
        curr = tuple(padd(coord, d))
        neighbors += curr in grid
    return neighbors


def solve1(d):
    inp = lmap(list, d.splitlines())
    grid = set()
    for x, row in enumerate(inp):
        for y, col in enumerate(inp[x]):
            if inp[x][y] == "#":
                grid.add((x, y, 0))
    for i in range(6):
        cpy = deepcopy(grid)
        for key in cpy:
            for delta in DELTA_3D + [(0, 0, 0)]:
                curr = tuple(padd(key, delta))
                neighbors = get_neighbors_count(cpy, curr, DELTA_3D)
                if curr in grid and (neighbors < 2 or neighbors > 3):
                    grid.remove(curr)
                elif curr not in grid and neighbors == 3:
                    grid.add(curr)

    return len(grid)


def solve2(d):
    inp = lmap(list, d.splitlines())
    grid = set()
    for x, row in enumerate(inp):
        for y, col in enumerate(inp[x]):
            if inp[x][y] == "#":
                grid.add((x, y, 0, 0))
    for i in range(6):
        cpy = deepcopy(grid)
        for key in cpy:
            for delta in DELTA_4D + [(0, 0, 0, 0)]:
                curr = tuple(padd(key, delta))
                neighbors = get_neighbors_count(cpy, curr, DELTA_4D)
                if curr in grid and (neighbors < 2 or neighbors > 3):
                    grid.remove(curr)
                elif curr not in grid and neighbors == 3:
                    grid.add(curr)

    return len(grid)


s = """
.#.
..#
###
"""
s2 = """"""

print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve1(inp))

print("PART 2")
print("Example Solution:", solve2(s))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve2(inp))
