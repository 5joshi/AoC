import collections as coll
import datetime as dt
import itertools as it
import math
from operator import itemgetter as ig
import pprint as pp
import re
from utils import *
from aocd import get_data, submit

inp = get_data(day=8)


def solve1(d):
    inp = d.splitlines()
    curr = acc = 0
    indexes = set()
    while curr not in indexes:
        indexes.add(curr)
        a, b = words(inp[curr])[0], ints(inp[curr])[0]
        if a == "nop":
            curr += 1
        elif a == "jmp":
            curr += b
        elif a == "acc":
            acc += b
            curr += 1
    return acc


def solve2(d):
    inp = d.splitlines()
    for i in range(len(inp)):
        if inp[i][0] == "a":
            continue
        j = inp[:]
        if (j[i][0] == "n"):
            j[i] = j[i].replace("nop", "jmp")
        else:
            j[i] = j[i].replace("jmp", "nop")
        curr = acc = 0
        indexes = set()
        while curr not in indexes and curr < len(j):
            indexes.add(curr)
            a, b = words(j[curr])[0], ints(j[curr])[0]
            if a == "nop":
                curr += 1
            elif a == "jmp":
                curr += b
            elif a == "acc":
                acc += b
                curr += 1
        if curr == len(j):
            return acc


s = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
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
