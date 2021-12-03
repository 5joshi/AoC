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

inp = get_data(year=2020, day=21)


def solve1(d):
    inp = lmap(words, d.splitlines())
    ingredient_count = coll.Counter()
    allergens_map = {}
    for line in inp:
        contains = line.index("contains")
        ingredients = set(line[:contains])
        allergens = line[contains+1:]
        for ingredient in ingredients:
            ingredient_count[ingredient] += 1
        for allergen in allergens:
            if allergen in allergens_map:
                allergens_map[allergen] = allergens_map[allergen].intersection(
                    ingredients)
            else:
                allergens_map[allergen] = ingredients
    for ingredient in flatten(allergens_map.values()):
        ingredient_count[ingredient] = 0
    return sum(ingredient_count.values())


def solve2(d):
    inp = lmap(words, d.splitlines())
    ingredient_count = coll.Counter()
    allergens_map = {}
    for line in inp:
        contains = line.index("contains")
        ingredients = set(line[:contains])
        allergens = line[contains+1:]
        for ingredient in ingredients:
            ingredient_count[ingredient] += 1
        for allergen in allergens:
            if allergen in allergens_map:
                allergens_map[allergen] = allergens_map[allergen].intersection(
                    ingredients)
            else:
                allergens_map[allergen] = ingredients
    used = used_keys = set()
    while (len(used_keys) != len(allergens_map.keys())):
        for key in allergens_map:
            if key in used_keys:
                continue
            allergens_map[key] -= used
            if len(allergens_map[key]) == 1:
                used_keys.add(key)
                used = used.union(allergens_map[key])
    return ",".join([str(allergens_map[key].pop()) for key in sorted(allergens_map.keys())])


s = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
"""
s2 = """"""

print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve1(inp))

print("PART 2")
print("Example Solution:", solve2(s))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve2(inp))
