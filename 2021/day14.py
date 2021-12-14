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

inp = get_data(year=2021, day=14)


def solve1(d):
    x, rules = d.split("\n\n")
    m = dict()
    for rule in rules.splitlines():
        fst, snd = rule.split(" -> ")
        m[fst] = fst[0] + snd + fst[1]
        
    for _ in range(10):
        new_x = x[0]
        for l1, l2 in zip(x, x[1:]):
            new_x += m[l1 + l2][1:]
        x = new_x
        
    count = coll.Counter(x)
    return max_minus_min(count.values())

def solve2(d):
    x, rules = d.split("\n\n")
    m = dict()
    for rule in rules.splitlines():
        fst, snd = rule.split(" -> ")
        m[fst] = fst[0] + snd + fst[1]
        
    bigram_count = coll.Counter([a+b for a,b in zip(x, x[1:])])
    letter_count = coll.Counter(x)
    for _ in range(40):
        new_count = deepcopy(bigram_count)
        for key, rule in m.items():
            w = bigram_count[key]
            new_count[key] -= w
            new_count[rule[:2]] += w
            new_count[rule[1:]] += w
            letter_count[rule[1]] += w
        bigram_count = new_count
        
    return max_minus_min(letter_count.values())


s = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""
s2 = """
"""

print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve1(s2))
print("Actual Solution:", solve1(inp))

print("PART 2")
print("Example Solution:", solve2(s))
# print("Example 2 Solution:", solve2(s2))
print("Actual Solution:", solve2(inp))
