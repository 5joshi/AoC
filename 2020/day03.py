import collections as coll
import datetime as dt
import itertools as it
import math
from operator import itemgetter as ig
import pprint as pp
import re
from utils import *
from aocd import get_data, submit

inp = get_data(day=3)


def solve1(d):
    inp = d.splitlines()
    curr = result = 0
    for i in range(len(inp)):
        if inp[i][curr] == "#":
            result += 1
        curr = (curr + 3) % len(inp[0])
    return result


def solve2(d):
    inp = d.splitlines()
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    end_result = 1
    for slope in slopes:
        curr = result = 0
        for i in range(0, len(inp), slope[1]):
            if inp[i][curr] == "#":
                result += 1
            curr = (curr + slope[0]) % len(inp[0])
        end_result *= result
    return end_result


s = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""
s2 = """"""

print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve1(inp))
# submit(solve(inp))
print("PART 2")
print("Example Solution:", solve2(s))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve2(inp))
# submit(solve(inp))
