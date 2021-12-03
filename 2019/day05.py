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

inp = get_data(year=2019, day=5)


def solve1(d):
    inp = ints(d)
    idx = 0
    
    def get_value(value, mode):
        if mode == "0":
            return inp[value]
        elif mode == "1":
            return value
        
    while inp[idx] != 99:
        opcode = str(inp[idx]).zfill(5)
        if opcode[-2:] == "01":
            pos1, pos2, pos3 = inp[idx+1:idx+4]
            inp[pos3] = get_value(pos1, opcode[-3]) + get_value(pos2, opcode[-4])
            idx += 4
        elif opcode[-2:] == "02":
            pos1, pos2, pos3 = inp[idx+1:idx+4]
            inp[pos3] = get_value(pos1, opcode[-3]) * get_value(pos2, opcode[-4])
            idx += 4
        elif opcode[-2:] == "03":
            pos1 = inp[idx+1]
            inp[pos1] = int(input("Required input..."))
            idx += 2
        elif opcode[-2:] == "04":
            pos1 = inp[idx+1]
            print(get_value(pos1, opcode[-3]))
            idx += 2
    
    return get_value(inp[idx-1], opcode[-3])

def solve2(d):
    inp = ints(d)
    idx = 0
    
    def get_value(value, mode):
        if mode == "0":
            return inp[value]
        elif mode == "1":
            return value
        
    while inp[idx] != 99:
        opcode = str(inp[idx]).zfill(5)
        if opcode[-2:] == "01":
            pos1, pos2, pos3 = inp[idx+1:idx+4]
            inp[pos3] = get_value(pos1, opcode[-3]) + get_value(pos2, opcode[-4])
            idx += 4
        elif opcode[-2:] == "02":
            pos1, pos2, pos3 = inp[idx+1:idx+4]
            inp[pos3] = get_value(pos1, opcode[-3]) * get_value(pos2, opcode[-4])
            idx += 4
        elif opcode[-2:] == "03":
            pos1 = inp[idx+1]
            inp[pos1] = int(input("Required input..."))
            idx += 2
        elif opcode[-2:] == "04":
            pos1 = inp[idx+1]
            print(get_value(pos1, opcode[-3]))
            idx += 2
        elif opcode[-2:] == "05":
            pos1, pos2 = inp[idx+1:idx+3]
            if get_value(pos1, opcode[-3]) != 0:
                idx = get_value(pos2, opcode[-4])
            else:
                idx += 3
        elif opcode[-2:] == "06":
            pos1, pos2 = inp[idx+1:idx+3]
            if get_value(pos1, opcode[-3]) == 0:
                idx = get_value(pos2, opcode[-4])
            else:
                idx += 3
        elif opcode[-2:] == "07":
            pos1, pos2, pos3 = inp[idx+1:idx+4]
            inp[pos3] = get_value(pos1, opcode[-3]) < get_value(pos2, opcode[-4])
            idx += 4
        elif opcode[-2:] == "08":
            pos1, pos2, pos3 = inp[idx+1:idx+4]
            inp[pos3] = get_value(pos1, opcode[-3]) == get_value(pos2, opcode[-4])
            idx += 4
    
    return get_value(inp[idx-1], opcode[-3])


s = """
"""
s2 = """
"""

print("PART 1")
# print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve1(inp))

print("PART 2")
# print("Example Solution:", solve2(s))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve2(inp))
