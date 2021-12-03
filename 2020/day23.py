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

inp = get_data(year=2020, day=23)

# solved in c++


# def solve(d):
#     inp = lmap(int, d)
#     curr_idx = 0
#     print(inp)
#     for _ in range(100):
#         curr = inp[curr_idx]
#         next_three = inp[]
#     return result


s = """389125467"""
s2 = """"""

print("Example Solution:", solve(s))
# print("Example 2 Solution:", solve(s2))
print("Actual Solution:", solve(inp))
