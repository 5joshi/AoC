# Credits to mcpower for pretty much all of these utils
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


# region Algorithms
def binary_search(f, lo=0, hi=None):
    """
    Returns a value x such that f(x) is true.
    Based on the values of f at lo and hi.
    Assert that f(lo) != f(hi).
    """
    lo_bool = f(lo)
    if hi is None:
        offset = 1
        while f(lo+offset) == lo_bool:
            offset *= 2
        hi = lo + offset
    else:
        assert f(hi) != lo_bool
    best_so_far = lo if lo_bool else hi
    while lo <= hi:
        mid = (hi + lo) // 2
        result = f(mid)
        if result:
            best_so_far = mid
        if result == lo_bool:
            lo = mid + 1
        else:
            hi = mid - 1
    return best_so_far
# endregion


# region List/Vector operations
GRID_DELTA = [[-1, 0], [1, 0], [0, -1], [0, 1]]
OCT_DELTA = [[1, 1], [-1, -1], [1, -1], [-1, 1]] + GRID_DELTA
CHAR_TO_DELTA = {
    "U": [-1, 0],
    "R": [0, 1],
    "D": [1, 0],
    "L": [0, -1],
    "N": [-1, 0],
    "E": [0, 1],
    "S": [1, 0],
    "W": [0, -1],
}
DELTA_TO_UDLR = {
    (-1, 0): "U",
    (0, 1): "R",
    (1, 0): "D",
    (0, -1): "L",
}
DELTA_TO_NESW = {
    (-1, 0): "N",
    (0, 1): "E",
    (1, 0): "S",
    (0, -1): "W",
}


def turn_180(drowcol):
    drow, dcol = drowcol
    return [-drow, -dcol]


def turn_right(drowcol):
    drow, dcol = drowcol
    return [dcol, -drow]


def turn_left(drowcol):
    drow, dcol = drowcol
    return [-dcol, drow]


def get_neighbors(grid, row, col, deltas, fill=None):
    n, m = len(grid), len(grid[0])
    out = []
    for i, j in deltas:
        p_row, p_col = row+i, col+j
        if 0 <= p_row < n and 0 <= p_col < m:
            out.append(grid[p_row][p_col])
        elif fill is not None:
            out.append(fill)
    return out


def fst(x):
    return x[0]


def snd(x):
    return x[1]


def padd(x, y):
    if len(x) == 2:
        return [x[0] + y[0], x[1] + y[1]]
    return [a+b for a, b in zip(x, y)]


def pneg(v):
    if len(v) == 2:
        return [-v[0], -v[1]]
    return [-i for i in v]


def psub(x, y):
    if len(x) == 2:
        return [x[0] - y[0], x[1] - y[1]]
    return [a-b for a, b in zip(x, y)]


def pmul(m: int, v):
    if len(v) == 2:
        return [m * v[0], m * v[1]]
    return [m * i for i in v]


def pdot(x, y):
    if len(x) == 2:
        return x[0] * y[0] + x[1] * y[1]
    return sum(a*b for a, b in zip(x, y))


def pdist1(x, y=None):
    if y is not None:
        x = psub(x, y)
    if len(x) == 2:
        return abs(x[0]) + abs(x[1])
    return sum(map(abs, x))


def pdist2sq(x, y=None):
    if y is not None:
        x = psub(x, y)
    if len(x) == 2:
        return (x[0] * x[0]) + (x[1] * x[1])
    return sum(i*i for i in x)


def pdist2(v):
    return math.sqrt(pdist2sq(v))
# endregion


# region Matrices


def matmat(a, b):
    n, k1 = len(a), len(a[0])
    k2, m = len(b), len(b[0])
    assert k1 == k2
    out = [[None] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            out[i][j] = sum(a[i][k] * b[k][j] for k in range(k1))
    return out


def matvec(a, v):
    return [j for i in matmat(a, [[x] for x in v]) for j in i]


def matexp(a, k):
    n = len(a)
    out = [[int(i == j) for j in range(n)] for i in range(n)]
    while k > 0:
        if k % 2 == 1:
            out = matmat(a, out)
        a = matmat(a, a)
        k //= 2
    return out
# endregion
