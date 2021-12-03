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

inp = get_data(year=2019, day=3)

def intersections(d):
    inp = d.splitlines()
    intersections = []
    grid = coll.defaultdict(bool)
    coord = (0, 0)
    for instr in inp[0].split(','):
        delta = tuple(CHAR_TO_DELTA[instr[0]])
        num = int(instr[1:])
        for _ in range(num):
            coord = tuple(padd(coord, delta))
            grid[coord] = True
    
    coord = (0, 0)        
    for instr in inp[1].split(','):
        delta = tuple(CHAR_TO_DELTA[instr[0]])
        num = int(instr[1:])
        for _ in range(num):
            coord = tuple(padd(coord, delta))
            if grid[coord]: intersections += [coord]   
              
    return intersections

def solve1(d):
    return pdist1(min(intersections(d), key=pdist1))

def solve2(d):
    inp = d.splitlines()
    
    def steps_to_coord(goal, instructions):
        steps = 0
        coord = (0, 0)
        for instr in instructions.split(','):
            delta = tuple(CHAR_TO_DELTA[instr[0]])
            num = int(instr[1:])
            for _ in range(num):
                coord = tuple(padd(coord, delta))
                steps += 1
                if coord == goal:
                    return steps
              
    return min([steps_to_coord(goal, inp[0]) + steps_to_coord(goal, inp[1]) for goal in intersections(d)])


s = """R8,U5,L5,D3
U7,R6,D4,L4
"""
s2 = """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7
"""

print("PART 1")
print("Example Solution:", solve1(s))
print("Example 2 Solution:", solve1(s2))
print("Actual Solution:", solve1(inp))

print("PART 2")
print("Example Solution:", solve2(s))
print("Example 2 Solution:", solve2(s2))
print("Actual Solution:", solve2(inp))
