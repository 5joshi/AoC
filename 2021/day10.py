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

inp = get_data(year=2021, day=10)


def solve1(d):
    inp = d.splitlines()
    mapping =  {")": 3, "]": 57, "}": 1197, ">": 25137}
    result = 0

    for line in inp:
        while True:
            new_line = line.replace("()", "").replace("<>", "").replace("[]", "").replace("{}", "")
            if line == new_line:
                break
            line = new_line
        corrupt = [c2 for c1, c2 in zip(line, line[1:]) if c1 in "([{<" and c2 in ")]}>"]
        if corrupt: result += mapping[corrupt[-1]]
    return result

def solve2(d):
    inp = d.splitlines()
    scores = []

    for line in inp:
        score = 0
        while True:
            new_line = line.replace("()", "").replace("<>", "").replace("[]", "").replace("{}", "")
            if line == new_line:
                break
            line = new_line
        if any([closing in line for closing in ")]}>"]): continue

        score = line[::-1].replace("(", "1").replace("[", "2").replace("{", "3").replace("<", "4")
        scores.append(int(score, 5))

    return sorted(scores)[len(scores) // 2]


s = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""
s2 = """{([(<{}[<>[]}>{[]{[(<()>
"""

print("PART 1")
print("Example Solution:", solve1(s2))
# print("Example 2 Solution:", solve1(s2))
print("Actual Solution:", solve1(inp))

print("PART 2")
print("Example Solution:", solve2(s))
# print("Example 2 Solution:", solve2(s2))
print("Actual Solution:", solve2(inp))
