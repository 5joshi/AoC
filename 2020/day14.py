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

inp = get_data(year=2020, day=14)


def solve1(d):
    inp = d.splitlines()
    mem = {}
    for line in inp:
        if "mask" in line:
            mask1 = int(line.split()[-1].replace("X", "0"), 2)
            mask2 = int(line.split()[-1].replace("X", "1"), 2)
        else:
            idx, bits = ints(line)
            mem[idx] = (bits & mask2) | mask1
    return sum(mem.values())


def solve2(d):
    inp = d.splitlines()
    mem = {}
    for line in inp:
        if "mask" in line:
            mask = line.split()[-1]
            mask1 = int(mask.replace("X", "0"), 2)
            mask2 = int(mask.replace("0", "1").replace("X", "0"), 2)
        else:
            idx, val = ints(line)
            num = (idx | mask1) & mask2
            x = [i for i, ltr in enumerate(mask[::-1]) if ltr == "X"]
            for i in range(2**len(x)):
                addr = num
                comb = bin(i)[2:].zfill(len(x))
                for bit, power in zip(comb, x):
                    if bit == "1":
                        addr += 2 ** power
                mem[addr] = val
    return sum(mem.values())


s = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
"""
s2 = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
"""
print("PART 1")
print("Example Solution:", solve1(s))
print("Actual Solution:", solve1(inp))
print("PART 2")
print("Example 2 Solution:", solve2(s2))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve2(inp))
