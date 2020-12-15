import collections as coll
import datetime as dt
import itertools as it
import math
from operator import itemgetter as ig
import pprint as pp
import re
from utils import *
from aocd import get_data, submit

inp = get_data(day=7)


def solve1(d):
    inp = d.splitlines()
    fitsIn = set()
    toCheck = list()
    toCheck.append("shiny gold")
    while toCheck:
        curr = toCheck[0]
        for line in inp:
            if curr in line[1:]:
                toCheck.append(words(line)[0] + " " + words(line)[1])
                fitsIn.add(words(line)[0] + " " + words(line)[1])
        toCheck.pop(0)
    return len(fitsIn)


def solve2(d):
    inp = dict()
    for line in d.splitlines():
        line = re.sub("bags?", "", line)
        w, i = words(line), ints(line)
        colors = lmap(lambda x: x[0] + " " + x[1], zip(w[3::2], w[4::2]))
        inp[w[0] + " " + w[1]] = list(zip(i, colors))

    def count(color):
        result = 0
        for elem in inp[color]:
            result += elem[0] + elem[0] * count(elem[1])
        return result

    return count("shiny gold")


s = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""
s2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
"""

print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve1(inp))
# submit(solve(inp))
print("PART 2")
print("Example Solution:", solve2(s))
print("Example 2 Solution:", solve2(s2))
print("Actual Solution:", solve2(inp))
# submit(solve(inp))
