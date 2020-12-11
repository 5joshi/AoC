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


def get_neighbors1(d, x, y):
    a = list()
    if x > 0:
        a.append(d[x-1][y])
        if y > 0:
            a.append(d[x-1][y-1])
        if y < len(d[0])-1:
            a.append(d[x-1][y+1])
    if x < len(d)-1:
        a.append(d[x+1][y])
        if y > 0:
            a.append(d[x+1][y-1])
        if y < len(d[0])-1:
            a.append(d[x+1][y+1])
    if y > 0:
        a.append(d[x][y-1])
    if y < len(d[0])-1:
        a.append(d[x][y+1])
    return a


def solve1(d):
    inp = lmap(list, d.splitlines())
    change = True
    while change:
        change = False
        cpy = deepcopy(inp)
        for x in range(len(inp)):
            for y in range(len(inp[0])):
                if cpy[x][y] == "L" and get_neighbors1(cpy, x, y).count("#") == 0:
                    inp[x][y] = "#"
                    change = True
                elif cpy[x][y] == "#" and get_neighbors1(cpy, x, y).count("#") >= 4:
                    inp[x][y] = "L"
                    change = True
    return sum(map(lambda x: x.count("#"), inp))


def get_neighbors2(d, x, y):
    a = list()
    if x > 0:
        curr = x - 1
        while curr > 0 and d[curr][y] == ".":
            curr -= 1
        a.append(d[curr][y])
        if y > 0:
            curr1 = x - 1
            curr2 = y - 1
            while curr1 > 0 and curr2 > 0 and d[curr1][curr2] == ".":
                curr1 -= 1
                curr2 -= 1
            a.append(d[curr1][curr2])
        if y < len(d[0])-1:
            curr1 = x - 1
            curr2 = y + 1
            while curr1 > 0 and curr2 < (len(d[0])-1) and d[curr1][curr2] == ".":
                curr1 -= 1
                curr2 += 1
            a.append(d[curr1][curr2])
    if x < len(d)-1:
        curr = x + 1
        while curr < len(d)-1 and d[curr][y] == ".":
            curr += 1
        a.append(d[curr][y])
        if y > 0:
            curr1 = x + 1
            curr2 = y - 1
            while curr1 < len(d)-1 and curr2 > 0 and d[curr1][curr2] == ".":
                curr1 += 1
                curr2 -= 1
            a.append(d[curr1][curr2])
        if y < len(d[0])-1:
            curr1 = x + 1
            curr2 = y + 1
            while curr1 < len(d)-1 and curr2 < (len(d[0])-1) and d[curr1][curr2] == ".":
                curr1 += 1
                curr2 += 1
            a.append(d[curr1][curr2])
    if y > 0:
        curr = y - 1
        while curr > 0 and d[x][curr] == ".":
            curr -= 1
        a.append(d[x][curr])
    if y < len(d[0])-1:
        curr = y + 1
        while curr < (len(d[0])-1) and d[x][curr] == ".":
            curr += 1
        a.append(d[x][curr])
    return a


def solve2(d):
    inp = lmap(list, d.splitlines())
    change = True
    while change:
        change = False
        cpy = deepcopy(inp)
        for x in range(len(inp)):
            for y in range(len(inp[0])):
                if cpy[x][y] == "L" and get_neighbors2(cpy, x, y).count("#") == 0:
                    inp[x][y] = "#"
                    change = True
                elif cpy[x][y] == "#" and get_neighbors2(cpy, x, y).count("#") >= 5:
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
