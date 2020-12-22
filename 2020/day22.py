import collections as coll
import datetime as dt
import functools as ft
import itertools as it
import math
from operator import itemgetter as ig
import pprint as pp
import re
from copy import deepcopy, copy
from utils import *
from functools import reduce
from aocd import get_data, submit

inp = get_data()


def solve1(d):
    p1, p2 = lmap(lambda x: ints(x)[1:], d.split("\n\n"))
    result = 0
    while p1 and p2:
        c1, c2 = p1.pop(0), p2.pop(0)
        if c1 > c2:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)
    for i, c in enumerate(reversed(p1+p2)):
        result += (i+1)*c
    return result


def hash(p):
    n = 0
    for x in p:
        n = (n << 8) + x
    return n


def solve(d):
    player1, player2 = lmap(lambda x: ints(x)[1:], d.split("\n\n"))
    result = 0

    def combat(p1, p2):
        prev_pos = set()
        while p1 and p2 and (hash(p1), hash(p2)) not in prev_pos:
            prev_pos.add((hash(p1), hash(p2)))
            c1, c2 = p1.pop(0), p2.pop(0)
            if len(p1) < c1 or len(p2) < c2:
                if c1 > c2:
                    p1.append(c1)
                    p1.append(c2)
                else:
                    p2.append(c2)
                    p2.append(c1)
            else:
                if combat(p1[:c1], p2[:c2])[0] == 1:
                    p1.append(c1)
                    p1.append(c2)
                else:
                    p2.append(c2)
                    p2.append(c1)
        if (hash(p1), hash(p2)) in prev_pos or not p2:
            return (1, p1)
        else:
            return (2, p2)

    for i, c in enumerate(reversed(combat(player1, player2)[1])):
        result += (i+1)*c
    return result


s = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
"""
s2 = """"""

print("Example Solution:", solve(s))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve(inp))
