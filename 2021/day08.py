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

inp = get_data(year=2021, day=8)

def solve1(d):
    inp = d.splitlines()
    result = 0
    
    for line in inp:
        line = line.split("|")
        data, output = map(lambda x: x.split(), line)
        result += sum([len(num) in [2, 3, 4, 7] for num in output])

    return result

def solve2(d):
    inp = d.splitlines()
    result = 0

    for line in inp:
        line = line.split("|")
        data, output = map(lambda x: x.split(), line)
        data = sorted(data, key=len)
        mapping = coll.defaultdict(str)
        
        mapping[1] = frozenset(data[0])
        mapping[7] = frozenset(data[1])
        mapping[4] = frozenset(data[2])     
        mapping[8] = frozenset(data[9])
                
        for num in data[6:9]:
            if mapping[4].issubset(set(num)):
                mapping[9] = frozenset(num)
            elif mapping[1].issubset(set(num)):
                mapping[0] = frozenset(num)
            else:
                mapping[6] = frozenset(num)
        
        for num in data[3:6]:
            if mapping[6].issuperset(set(num)):
                mapping[5] = frozenset(num)
            elif mapping[9].issuperset(set(num)):
                mapping[3] = frozenset(num)
            else:
                mapping[2] = frozenset(num)

        inverse_mapping = invert_dict(mapping)
        output = ''.join([str(inverse_mapping[frozenset(num)]) for num in output])
        result += int(output)

    return result


s = """acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
"""
s2 = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""

print("PART 1")
print("Example Solution:", solve1(s))
print("Example 2 Solution:", solve1(s2))
print("Actual Solution:", solve1(inp))

print("PART 2")
print("Example Solution:", solve2(s))
print("Example 2 Solution:", solve2(s2))
print("Actual Solution:", solve2(inp))
