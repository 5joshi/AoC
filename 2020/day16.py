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

inp = get_data()


def solve1(d):
    inp = d.split("\n\n")
    ranges = []
    result = 0
    for line in inp[0].splitlines():
        a = positive_ints(line)
        ranges.append((a[0], a[1], a[2], a[3]))
    for line in inp[2].splitlines():
        a = ints(line)
        for num in a:
            found = False
            for rng in ranges:
                if rng[0] <= num <= rng[1] or rng[2] <= num <= rng[3]:
                    found = True
                    break
            if not found:
                result += num
    return result


def solve2(d):
    inp = d.split("\n\n")
    ranges = []
    nums = []
    notes = {}
    for line in inp[0].splitlines():
        a = positive_ints(line)
        ranges.append((a[0], a[1], a[2], a[3], line[0:line.find(":")]))
        nums.append([])
    rule_count = len(ranges)
    for line in inp[2].splitlines():
        a = ints(line)
        c = 0
        for num in a:
            for rng in ranges:
                if rng[0] <= num <= rng[1] or rng[2] <= num <= rng[3]:
                    c += 1
                    break
        if c == rule_count:
            for i in range(len(a)):
                nums[i].append(a[i])
    for i in range(len(nums)):
        l = nums[i]
        for rng in ranges:
            found = True
            for num in l:
                if not (rng[0] <= num <= rng[1] or rng[2] <= num <= rng[3]):
                    found = False
                    break
            if found:
                if rng[4] not in notes.keys():
                    notes[rng[4]] = set()
                notes[rng[4]].add(i)
    result = 1
    notes = dict(sorted(notes.items(), key=lambda item: len(item[1])))
    my_ticket = ints(inp[1])
    last_used = set()
    for key in notes:
        rule_num = (notes[key] - last_used).pop()
        if "departure" in key:
            result *= my_ticket[rule_num]
        last_used = notes[key]

    return result


s = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
"""
s2 = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
"""


print("PART 1")
print("Example Solution:", solve1(s))
print("Actual Solution:", solve1(inp))
print("PART 2")
print("Actual Solution:", solve2(inp))
