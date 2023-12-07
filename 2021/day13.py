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

inp = get_data(year=2021, day=13)


def solve1(d):
    coords, folds = lmap(lambda x: x.splitlines(), d.split("\n\n"))
    grid = set()
    
    for coord in coords:
        grid.add(tuple(ints(coord)))
    
    for fold in folds[:1]:
        axis, num = fold.split()[-1].split("=")
        axis = int(axis == "y")
        num = int(num)
        new_grid = set()
        
        for coord in lmap(list, grid):
            if coord[axis] > num:
                coord[axis] = (num * 2) - coord[axis]
            new_grid.add(tuple(coord))
                
        grid = new_grid

    return len(grid)

def solve2(d):
    coords, folds = lmap(lambda x: x.splitlines(), d.split("\n\n"))
    grid = set()
    
    def grid_str(grid):
        result = "\n"
        l = max([y for (_, y) in grid]) + 1
        w = max([x for (x, _) in grid]) + 1
        for y in range(l):
            result += " ".join(["#" if (x, y) in grid else " " for x in range(w)]) + "\n"
        return result
    
    for coord in coords:
        grid.add(tuple(ints(coord)))
    
    for fold in folds:
        axis, num = fold.split()[-1].split("=")
        axis = int(axis == "y")
        num = int(num)
        new_grid = set()
        
        for coord in lmap(list, grid):
            if coord[axis] > num:
                coord[axis] = (num * 2) - coord[axis]
            new_grid.add(tuple(coord))
                
        grid = new_grid

    result = grid_str(grid)
    return result


s = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
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
