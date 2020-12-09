# region Imports
import collections as coll
import datetime as dt
import itertools as it
import math
from operator import itemgetter as ig
import pprint as pp
import re
import sys
import typing
# endregion

sys.setrecursionlimit(100000)
# Copy a function if you need to modify it.

# region Strings, lists, dicts


def lmap(func, *iterables):
    return list(map(func, *iterables))


def make_grid(*dimensions: typing.List[int], fill=None):
    "Returns a grid such that 'dimensions' is juuust out of bounds."
    if len(dimensions) == 1:
        return [fill for _ in range(dimensions[0])]
    next_down = make_grid(*dimensions[1:], fill=fill)
    return [list(next_down) for _ in range(dimensions[0])]


def min_max(l):
    return min(l), max(l)


def max_plus_min(l):
    return max(l) + min(l)


def max_minus_min(l):
    return max(l) - min(l)


def list_diff(x):
    return [b-a for a, b in zip(x, x[1:])]


def flatten(l):
    return [i for x in l for i in x]


def ints(s: str) -> typing.List[int]:
    return lmap(int, re.findall(r"-?\d+", s))  # thanks mserrano!


def positive_ints(s: str) -> typing.List[int]:
    return lmap(int, re.findall(r"\d+", s))  # thanks mserrano!


def floats(s: str) -> typing.List[float]:
    return lmap(float, re.findall(r"-?\d+(?:\.\d+)?", s))


def positive_floats(s: str) -> typing.List[float]:
    return lmap(float, re.findall(r"\d+(?:\.\d+)?", s))


def words(s: str) -> typing.List[str]:
    return re.findall(r"[a-zA-Z]+", s)


def keyvalues(d):
    return list(d.items())  # keep on forgetting this...
# endregion

# region List/Vector operations


def fst(x):
    return x[0]


def snd(x):
    return x[1]
# endregion
