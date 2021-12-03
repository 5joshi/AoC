import collections as coll
import datetime as dt
import itertools as it
import math
from operator import itemgetter as ig
import pprint as pp
import re
from utils import *
from aocd import get_data, submit

inp = get_data(year=2020, day=4)


def solve1(d):
    inp = d.split("\n\n")
    result = 0
    for elem in inp:
        result += len(re.findall("(byr|iyr|eyr|hgt|hcl|ecl|pid):", elem)) == 7
    return result


def solve2(d):
    inp = d.split("\n\n")
    result = 0
    for elem in inp:
        result += len(re.findall(
            "(byr:(19[2-9][0-9]|200[0-2])|iyr:(20(1[0-9]|20))|eyr:(20(2[0-9]|30))|hgt:(1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in)|hcl:(#[a-f0-9]{6})|ecl:(amb|blu|brn|gry|grn|hzl|oth)|pid:([0-9]{9}))(\s|\n|$)", elem)) == 7
    return result


s = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
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
