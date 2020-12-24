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

inp = get_data(day=24)

CHAR_TO_HEX_DELTA = {
    "ne": [-1, 0.5],
    "nw": [-1, -0.5],
    "e": [0, 1],
    "se": [1, 0.5],
    "sw": [1, -0.5],
    "w": [0, -1],
}

HEX_DELTA = [(-1, 0.5), (-1, -0.5), (0, 1), (1, 0.5), (1, -0.5), (0, -1)]


def solve1(d):
    inp = d.splitlines()
    grid = coll.defaultdict(lambda: False)
    for line in inp:
        line = list(line)
        i = 0
        while i < len(line):
            if line[i] == "n" or line[i] == "s":
                line[i:i+2] = [''.join(line[i:i+2])]
            i += 1
        currPos = (0, 0)
        for dir in line:
            currPos = tuple(padd(currPos, CHAR_TO_HEX_DELTA[dir]))
        grid[currPos] = not grid[currPos]
    return sum(grid.values())


def count_hex_neighbors(location, grid):
    result = 0
    for dir in HEX_DELTA:
        result += tuple(padd(location, dir)) in grid
    return result


def solve2(d):
    inp = d.splitlines()
    grid = set()
    for line in inp:
        line = list(line)
        i = 0
        while i < len(line):
            if line[i] == "n" or line[i] == "s":
                line[i:i+2] = [''.join(line[i:i+2])]
            i += 1
        currPos = (0, 0)
        for dir in line:
            currPos = tuple(padd(currPos, CHAR_TO_HEX_DELTA[dir]))
        if currPos in grid:
            grid.remove(currPos)
        else:
            grid.add(currPos)
    for _ in range(100):
        cpy = deepcopy(grid)
        for elem in cpy:
            for dir in HEX_DELTA + [(0, 0)]:
                curr = tuple(padd(elem, dir))
                neighbors = count_hex_neighbors(curr, cpy)
                if curr not in grid and neighbors == 2:
                    grid.add(curr)
                elif curr in grid and (neighbors == 0 or neighbors > 2):
                    grid.remove(curr)
    return len(grid)


s = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
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
