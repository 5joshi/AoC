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
    grid = Grid(lmap(lambda l: [int(x) for x in l], d.splitlines()))
    result = 0
    for curr in grid.coords():
        val = grid[curr]
        if all([val < neighbor for neighbor in grid.get_neighbors(curr, GRID_DELTA)]):
            result += val + 1
    return result

def solve2(d):
    grid = Grid(lmap(lambda l: [int(x) for x in l], d.splitlines()))
    basins = []
    for curr in grid.coords():
        val = grid[curr]
        if all([val < neighbor for neighbor in grid.get_neighbors(curr, GRID_DELTA)]):
            to_check = [curr]
            basin = {curr}
            while to_check:
                valid_neighbors = {coord for coord in grid.get_neighbors_coords(to_check[0], GRID_DELTA) if grid[coord] != 9}
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
