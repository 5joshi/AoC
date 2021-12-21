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

inp = get_data(year=2021, day=11)


def solve1(d):
    grid = number_grid(d)
    result = 0
    
    for _ in range(100):
        new_grid = gridmap(lambda x: x + 1, grid)

        flash = True
        while flash:
            flash = False
            for x, row in enumerate(new_grid):
                for y, cell in enumerate(row):
                    if cell > 9:
                        new_grid[x][y] = 0
                        
                        for (nx, ny) in grid_neighbors(grid, x, y, OCT_DELTA):
                            if new_grid[nx][ny] != 0:
                                new_grid[nx][ny] += 1
                                
                        flash = True
                        result += 1
                        
        grid = new_grid
        
    return result

def solve2(d):
    grid = lmap(lambda l: [int(x) for x in l], d.splitlines())
    goal = len(grid) * len(grid[0])
    result = step = 0
    
    while result != goal:
        new_grid = gridmap(lambda x: x + 1, grid)
        step += 1
        result = 0

        flash = True
        while flash:
            flash = False
            for x, row in enumerate(new_grid):
                for y, cell in enumerate(row):
                    if cell > 9:
                        new_grid[x][y] = 0
                        
                        for (nx, ny) in grid_neighbors(grid, x, y, OCT_DELTA):
                            if new_grid[nx][ny] != 0:
                                new_grid[nx][ny] += 1
                                
                        flash = True
                        result += 1
                        
        grid = new_grid
        
    return step


s = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
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
