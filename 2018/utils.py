# Credits to mcpower for pretty much all of these utils
#region Imports
import abc
import collections
import copy
import datetime
from enum import Enum
import functools as ft
import heapq
import itertools as it
import math
import operator
import random
import re
import sys
import timeit
import typing
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import reduce, lru_cache
from pprint import pprint
from aocd import get_data, submit
from tqdm import tqdm
#endregion

sys.setrecursionlimit(100000)
T = typing.TypeVar("T")

#region parsing
def ints(s: str) -> typing.List[int]:
    return lmap(int, re.findall(r"-?\d+", s))  # thanks mserrano!

def digits(s: str) -> typing.List[int]:
    return lmap(int, re.findall(r"\d", s))

def positive_ints(s: str) -> typing.List[int]:
    return lmap(int, re.findall(r"\d+", s))  # thanks mserrano!

def floats(s: str) -> typing.List[float]:
    return lmap(float, re.findall(r"-?\d+(?:\.\d+)?", s))

def positive_floats(s: str) -> typing.List[float]:
    return lmap(float, re.findall(r"\d+(?:\.\d+)?", s))

def words(s: str) -> typing.List[str]:
    return re.findall(r"[a-zA-Z]+", s)

def alphanumerics(s: str) -> typing.List[str]:
    return re.findall(r"[a-zA-Z0-9]+", s)

def words_and_ints(s: str) -> typing.List[typing.Union[str, int]]:
    return lmap(lambda x: int(x) if (x.isnumeric() or x[0] == '-' and x[1:].isnumeric()) else x, re.findall(r"[a-zA-Z]+|-?\d+", s))
#endregion
#region Strings, lists, dicts
ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def multi_replace(s, replacements):
    for old, new in replacements:
        s = s.replace(old, new)
    return s

def fst(x):
    return x[0]

def snd(x):
    return x[1]

def only(x):
    assert len(x) == 1
    return x[0]

def transpose(*iterables):
    return list(zip(*iterables))

def lmap(func, *iterables):
    return list(map(func, *iterables))

def lzip(*iterables):
    return list(zip(*iterables))

def lfilter(func, *iterables):
    return list(filter(func, *iterables))

def lrange(*args):
    return list(range(*args))

def lsums(*iterables):
    return [sum(elems) for elems in zip(*iterables)]

def ladd(x, y):
    return [x + y for x, y in zip(x, y)]

def lneg(l):
    return [-i for i in l]

def lsub(x, y):
    return [x - y for x, y in zip(x, y)]

def lnorm(l):
    return math.sqrt(sum(i*i for i in l))

def lmul(l, c):
    return [c * i for i in l]

def ldot(x, y):
    return sum(a * b for a, b in zip(x, y))

def tmap(func, *iterables):
    return tuple(map(func, *iterables))

def tzip(*iterables):
    return tuple(zip(*iterables))

def tfilter(func, *iterables):
    return tuple(filter(func, *iterables))

def trange(*args):
    return tuple(range(*args))

def tsums(*iterables):
    return tuple(sum(elems) for elems in zip(*iterables))

def tadd(x, y):
    return tuple(x + y for x, y in zip(x, y))

def tneg(l):
    return tuple(-i for i in l)

def tsub(x, y):
    return tuple(x - y for x, y in zip(x, y))

def tnorm(l):
    return math.sqrt(sum(i*i for i in l))

def tmul(l, c):
    return tuple(c * i for i in l)

def avg(l):
    return sum(l) / len(l)

def median(l):
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2    

def product(l):
    return reduce(operator.mul, l, 1)

def min_max(l):
    return min(l), max(l)

def max_plus_min(l):
    return max(l) + min(l)

def max_minus_min(l):
    return max(l) - min(l)

def partial_sum(l):
    "out[i] == sum(in[:i])"
    out = [0]
    for i in l:
        out.append(out[-1] + i)
    return out

def list_diff(x):
    return [b-a for a, b in zip(x, x[1:])]

def flatten(l):
    return [i for x in l for i in x]

def every_n(l,n):
    return list(zip(*[iter(l)]*n))

def windows(l, n):
    return list(zip(*[l[i:] for i in range(n)]))

def keyvalues(d):
    return list(d.items())

def make_hashable(l):
    if isinstance(l, list):
        return tuple(map(make_hashable, l))
    if isinstance(l, dict):
        l = set(l.items())
    if isinstance(l, set):
        return frozenset(map(make_hashable, l))
    return l

def invert_dict(d, single=True):
    out = {}
    if single:
        for k, v in d.items():
            v = make_hashable(v)
            if v in out:
                print("[invert_dict] WARNING WARNING: duplicate key", v)
            out[v] = k
    else:
        for k, v in d.items():
            v = make_hashable(v)
            out.setdefault(v, []).append(k)
    return out
#endregion
#region numbers
def gauss_sum(n):
    return (n * (n + 1)) // 2

def signum(n: int) -> int:
    if n > 0:
        return 1
    elif n == 0:
        return 0
    else:
        return -1
    
def primes(n):
    """Returns a set of primes from 2 to n (inclusive)"""
    sieve = set(range(2, n+1))
    while sieve:
        prime = min(sieve)
        yield prime
        sieve -= set(range(prime, n+1, prime))

def is_prime(n):
    """Checks if n is prime."""
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    # since all primes > 3 are of the form 6n ± 1
    # start with f=5 (which is prime)
    # and test f, f+2 for being prime
    # then loop by 6. 
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f+2) == 0: return False
        f += 6
    return True   

def divisors(n, prime=False):
    """
    Returns a set of divisors of n
    """
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0 and (not prime or is_prime(i)):
            result.add(i)
            if not prime:
                result.add(n//i)
    if prime and is_prime(n): 
        result.add(n)
    return result

def prime_factors(n):
    """
    Returns a list of prime factors of n (with repetitions)
    """
    factors = []
    for factor in divisors(n, prime=True):
        while n % factor == 0:
            factors.append(factor)
            n //= factor
    return factors
#endregion
#region algorithms
def bisect(f, lo=0, hi=None, eps=1e-9):
    """
    Returns a value x such that f(x) is true.
    Based on the values of f at lo and hi.
    Returns the first float x such that f(x) is true within eps.
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
    while hi - lo > eps:
        mid = (hi + lo) / 2
        if f(mid) == lo_bool:
            lo = mid
        else:
            hi = mid
    if lo_bool:
        return lo
    else:
        return hi

def binary_search(f, lo=0, hi=None):
    """
    Returns a value x such that f(x) is true.
    Based on the values of f at lo and hi.
    Returns the first integer x such that f(x) is true.
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
#endregion
#region graphs
def topsort(out_edges: typing.Dict[T, typing.List[T]]) -> typing.List[T]:
    """
    Returns a list containing topological sort of the nodes.
    out_edges is a dict mapping a node to a list of nodes it points to.
    """
    temp = set()  # type: typing.Set[T]
    seen = set()  # type: typing.Set[T]
    out = []

    def dfs(n):
        nonlocal temp,seen,out
        if n in seen:
            return
        if n in temp:
            raise Exception("not a DAG")
        temp.add(n)
        if n in out_edges:
            for other in out_edges[n]:
                dfs(other)
        temp.remove(n)
        seen.add(n)
        out.append(n)
    
    for n in out_edges:
        dfs(n)
    out.reverse()
    return out

def path_from_parents(parents: typing.Dict[T, T], end: T) -> typing.List[T]:
    """
    Returns a path from the parents obtained from dijkstra/BFS.
    """
    out = [end]
    while out[-1] in parents:
        out.append(parents[out[-1]])
    out.reverse()
    return out

def dijkstra(
    from_node: T,
    expand: typing.Callable[[T], typing.Iterable[typing.Tuple[int, T]]],
    heuristic: typing.Optional[typing.Callable[[T], int]] = None,
    to_node: typing.Optional[T] = None,
    to_func: typing.Optional[typing.Callable[[T], bool]] = None,
) -> typing.Tuple[typing.Dict[T, int], typing.Dict[T, T]]:
    """
    Returns (distances, parents).
    expand is a function that takes a node and returns an iterable of (cost, new_node).
    heuristic is an optional function that takes a node and returns an estimate of the distance to to_node.
    heuristic should never overestimate the cost (heuristic = lower bound).
    Use path_from_parents(parents, node) to get a path.
    """
    if heuristic is None:
        heuristic = lambda _: 0
    seen = set()  # type: typing.Set[T]
    g_values = {from_node: 0}  # type: typing.Dict[T, int]
    parents = {}  # type: typing.Dict[T, T]
    
    # (f, g, n)
    todo = [(0 + heuristic(from_node), 0, from_node)]  # type: typing.List[typing.Tuple[int, int, T]]

    while todo:
        f, g, node = heapq.heappop(todo)

        assert node in g_values
        assert g_values[node] <= g

        if node in seen:
            continue

        assert g_values[node] == g
        if to_node is not None and node == to_node or to_func is not None and to_func(node):
            break
        seen.add(node)
        for cost, new_node in expand(node):
            new_g = g + cost
            if new_node not in g_values or new_g < g_values[new_node]:
                parents[new_node] = node
                g_values[new_node] = new_g
                heapq.heappush(todo, (new_g + heuristic(new_node), new_g, new_node))
    
    return (g_values, parents)

def a_star(
    from_node: T,
    expand: typing.Callable[[T], typing.Iterable[typing.Tuple[int, T]]],
    heuristic: typing.Optional[typing.Callable[[T], int]] = None,
    to_node: typing.Optional[T] = None,
    to_func: typing.Optional[typing.Callable[[T], bool]] = None,
) -> typing.Tuple[int, typing.List[T]]:
    """
    Returns the (distance, path) from from_node to to_node using dijkstra.
    expand is a function that takes a node and returns an iterable of (cost, new_node).
    heuristic is an optional function that takes a node and returns an estimate of the distance to to_node.
    heuristic should never overestimate the cost (heuristic = lower bound).
    """
    g_values, parents = dijkstra(from_node, to_node=to_node, expand=expand, heuristic=heuristic, to_func=to_func)
    if to_node is None and to_func is None: 
        raise Exception("must specify to_node or to_func")
    if to_node:
        if to_node not in g_values:
            raise Exception("couldn't reach to_node")
        return (g_values[to_node], path_from_parents(parents, to_node))
    else:
        check = [(g, n) for n, g in g_values.items() if to_func(n)]
        if not check:
            raise Exception("couldn't reach to_node")
        best = check[0]
        return (best[0], path_from_parents(parents, best[1]))


def bfs(
    from_node: T,
    expand: typing.Callable[[T], typing.Iterable[T]],
    to_node: typing.Optional[T] = None,
    to_func: typing.Optional[typing.Callable[[T], bool]] = None,
) -> typing.Tuple[typing.Dict[T, int], typing.Dict[T, T]]:
    """
    Returns (distances, parents).
    expand is a function that takes a node and returns an iterable of new_nodes.
    Use path_from_parents(parents, node) to get a path.
    """
    g_values = {from_node: 0}  # type: typing.Tuple[typing.Dict[T, int]]
    parents = {}  # type: typing.Dict[T, T]
    todo = [from_node]  # type: typing.List[T]
    dist = 0

    while todo:
        new_todo = []
        dist += 1
        for node in todo:
            for new_node in expand(node):
                if new_node not in g_values:
                    new_todo.append(new_node)
                    parents[new_node] = node
                    g_values[new_node] = dist
        todo = new_todo
        if (to_node is not None and to_node in g_values) or (to_func is not None and any(to_func(node) for node in g_values)):
            break
    
    return (g_values, parents)

def bfs_single(
    from_node: T,
    expand: typing.Callable[[T], typing.Iterable[T]],
    to_node: typing.Optional[T] = None,
    to_func: typing.Optional[typing.Callable[[T], bool]] = None,
) -> typing.Tuple[int, typing.List[T]]:
    """
    Returns the (distance, path) from from_node to to_node using bfs.
    expand is a function that takes a node and returns an iterable of new_nodes.
    """
    g_values, parents = bfs(from_node, to_node=to_node, expand=expand)
    if to_node is None and to_func is None: 
        raise Exception("must specify to_node or to_func")
    if to_node:
        if to_node not in g_values:
            raise Exception("couldn't reach to_node")
        return (g_values[to_node], path_from_parents(parents, to_node))
    else:
        check = [(g, n) for n, g in g_values.items() if to_func(n)]
        if not check:
            raise Exception("couldn't reach to_node")
        best = check[0]
        return (best[0], path_from_parents(parents, best[1]))
#endregion
#region distances
BLANK = object()

def hamming_distance(a, b) -> int:
    """
    Returns the hamming distance between a and b.
    This is the number of positions where a and b differ.
    """
    return sum(i is BLANK or j is BLANK or i != j for i, j in it.zip_longest(a, b, fillvalue=BLANK))

def edit_distance(a, b) -> int:
    """
    Returns the levenstein distance between a and b.
    This is the minimum number of insertions, deletions, and substitutions to turn a into b.
    """
    n = len(a)
    m = len(b)
    dp = [[None] * (m+1) for _ in range(n+1)]
    dp[n][m] = 0
    def aux(i, j):
        assert 0 <= i <= n and 0 <= j <= m
        if dp[i][j] is not None:
            return dp[i][j]
        if i == n:
            dp[i][j] = 1 + aux(i, j+1)
        elif j == m:
            dp[i][j] = 1 + aux(i+1, j)
        else:
            dp[i][j] = min((a[i] != b[j]) + aux(i+1, j+1), 1 + aux(i+1, j), 1 + aux(i, j+1))
        return dp[i][j]
    return aux(0, 0)

def dist1(x, y=None):
    """
    Returns the manhattan distance between x and y.
    This is the sum of the absolute values of the differences of the coordinates.
    """
    if y is not None:
        x = tsub(x, y)
    return sum(map(abs, x))

def dist2sq(x, y=None):
    """
    Returns the squared euclidean distance between x and y.
    This is the sum of the squares of the differences of the coordinates.
    If y is None, this is the squared distance from the origin.
    """
    if y is not None:
        x = tsub(x, y)
    return sum(i*i for i in x)

def dist2(x, y=None):
    """
    Returns the euclidean distance between x and y.
    If y is None, this is the distance from the origin.
    """
    return math.sqrt(dist2sq(x, y))
#endregion
#region Data structures
class UnionFind:
    # n: int
    # parents: List[Optional[int]]
    # ranks: List[int]
    # num_sets: int

    def __init__(self, n: int) -> None:
        self.n = n
        self.parents = [None] * n
        self.ranks = [1] * n
        self.num_sets = n
    
    def find(self, i: int) -> int:
        p = self.parents[i]
        if p is None:
            return i
        p = self.find(p)
        self.parents[i] = p
        return p
    
    def in_same_set(self, i: int, j: int) -> bool:
        return self.find(i) == self.find(j)
    
    def merge(self, i: int, j: int) -> None:
        i = self.find(i)
        j = self.find(j)

        if i == j:
            return
        
        i_rank = self.ranks[i]
        j_rank = self.ranks[j]

        if i_rank < j_rank:
            self.parents[i] = j
        elif i_rank > j_rank:
            self.parents[j] = i
        else:
            self.parents[j] = i
            self.ranks[i] += 1
        self.num_sets -= 1
#endregion
#region matrices
GRID_DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]

OCT_DELTA = [(1, 1), (-1, -1), (1, -1), (-1, 1)] + GRID_DELTA

HEX_DELTA = {
    'n': (0, 1, -1),
    'ne': (1, 0, -1),
    'se': (1, -1, 0),
    's': (0, -1, 1),
    'sw': (-1, 0, 1),
    'nw': (-1, 1, 0),
}

CHAR_TO_DELTA = {
    ">": (0, 1),
    "<": (0, -1),
    "^": (-1, 0),
    "v": (1, 0),
    "U": (-1, 0),
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1),
    "N": (-1, 0),
    "E": (0, 1),
    "S": (1, 0),
    "W": (0, -1),
    "NE": (-1, 1),
    "SE": (1, 1),
    "NW": (-1, -1),
    "SW": (1, -1),
    "UR": (-1, 1),
    "DR": (1, 1),
    "UL": (-1, -1),
    "DL": (1, -1),
    "RU": (-1, 1),
    "RD": (1, 1),
    "LU": (-1, -1),
    "LD": (1, -1),
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

def best_delta(x, y=(0, 0), deltas=OCT_DELTA, dist=dist1):
    """
    Returns the delta in deltas that leads to the shortest path (minimizes dist(x + delta, y)).
    """
    return min(deltas, key=lambda delta: dist(tadd(x, delta), y))

def turn_180(drowcol):
    """
    Given a delta, returns the delta that is 180 degrees rotated.
    """
    if isinstance(drowcol, str):
        delta = CHAR_TO_DELTA[drowcol]
        if drowcol in 'UDLR': return DELTA_TO_UDLR[turn_180(delta)]
        if drowcol in 'NESW': return DELTA_TO_NESW[turn_180(delta)]
        assert False, f'unknown direction passed ({drowcol})'
    drow, dcol = drowcol
    return (-drow, -dcol)

def turn_right(drowcol):
    """
    Given a delta, returns the delta that is 90 degrees rotated clockwise.
    """
    if isinstance(drowcol, str):
        delta = CHAR_TO_DELTA[drowcol]
        if drowcol in 'UDLR': return DELTA_TO_UDLR[turn_right(delta)]
        if drowcol in 'NESW': return DELTA_TO_NESW[turn_right(delta)]
        assert False, f'unknown direction passed ({drowcol})'
    drow, dcol = drowcol
    return (dcol, -drow)

def turn_left(drowcol):
    """
    Given a delta, returns the delta that is 90 degrees rotated counterclockwise.
    """
    if isinstance(drowcol, str):
        delta = CHAR_TO_DELTA[drowcol]
        if drowcol in 'UDLR': return DELTA_TO_UDLR[turn_left(delta)]
        if drowcol in 'NESW': return DELTA_TO_NESW[turn_left(delta)]
        assert False, f'unknown direction passed ({drowcol})'
    drow, dcol = drowcol
    return (-dcol, drow)

def dimensions(grid):
    """
    Returns the dimensions of a grid of any dimensions.
    """
    out = []
    while isinstance(grid, list):
        out.append(len(grid))
        grid = grid[0]
    return out

def neighbors(dimensions, coord, deltas) -> typing.List[typing.Tuple[int]]:
    """
    Returns the neighbors of coords in a grid of any dimensions.
    """
    out = []
    for delta in deltas:
        new_coord = tadd(coord, delta)
        if all(0 <= c < c_max for c, c_max in zip(new_coord, dimensions)):
            out.append(new_coord)
    return out

def lget(l, i):
    """
    Gets the element at coordinate i in a list of any dimensions.
    """
    if len(l) == 2: return l[i[0]][i[1]]
    for index in i: l = l[index]
    return l

def lset(l, i, v):
    """
    Sets the element at coordinate i to v in a list of any dimensions.
    """
    if len(l) == 2:
        l[i[0]][i[1]] = v
        return
    for index in i[:-1]: l = l[index]
    l[i[-1]] = v
    
def spiral(size=None, start=(0, 0)):
    """
    Get coordinates of spiral of given size. (size = number of points including origin)
    """
    curr = start
    directions = it.cycle(CHAR_TO_DELTA[d] for d in 'RULD')
    steps = map(lambda c: c//2, it.count(2))
    curr_dir = next(directions)
    curr_steps = next(steps)

    def step():
        nonlocal curr, curr_dir, curr_steps
        if curr_steps == 0:
            curr_dir = next(directions)
            curr_steps = next(steps)
        curr = tadd(curr, curr_dir)
        curr_steps -= 1

    yield start
    while size is None:
        step()
        yield curr    
    else:
        for _ in range(size-1):
            step()
            yield curr    
    
def make_grid(*dimensions: typing.List[int], fill=None):
    "Returns a grid such that 'dimensions' is juuust out of bounds."
    if len(dimensions) == 1:
        return [fill for _ in range(dimensions[0])]
    next_down = make_grid(*dimensions[1:], fill=fill)
    result = [list(next_down) for _ in range(dimensions[0])]
    return Grid(result) if len(dimensions) == 2 else result
    
def points_sub_min(points):
    m = [min(p[i] for p in points) for i in range(len(points[0]))]
    return [tsub(p, m) for p in points]

def points_to_grid(points, sub_min=True, flip=False, hit='#', fill='.', dimensions=None):
    """
    Converts a list of points to a grid.
    """
    if not isinstance(points, list):
        points = list(points)
    if sub_min:
        points = points_sub_min(points)
    if flip:
        points = [(y, x) for x, y in points]
    if dimensions:
        grid = make_grid(*dimensions, fill=fill)
    else:
        grid = make_grid(max(map(fst, points))+1, max(map(snd, points))+1, fill=fill)
    for x, y in points:
        grid[(x, y)] = hit
    return grid

def map_to_grid(d, sub_min=True, flip=False, fill='.'):
    """
    Converts a dictionary of points to a grid.
    """
    points = [*d.keys()]
    if sub_min:
        new_points = points_sub_min(points)
        d = {new: d[old] for old, new in zip(points, new_points)}
        points = new_points
    if flip:
        d = {(y, x): v for (x, y), v in d.items()}
        points = [(y, x) for x, y in points]
    grid = make_grid(max(map(fst, points))+1, max(map(snd, points))+1, fill=fill)
    for x, y in points:
        grid[(x, y)] = d[(x, y)]
    return grid

def s_to_grid(s, flip=False):
    """
    Converts a string to a grid.
    """
    grid = map(list, s.splitlines())
    if flip: grid = transpose(*grid)
    return Grid([*grid])

class Grid(typing.Generic[T]):
    """2D only!!!"""
    def __init__(self, grid: typing.List[typing.List[T]]) -> None:
        self.grid = grid
        self.width = self.nrows = len(self.grid)
        self.height = self.ncols = len(self.grid[0])
        
    def copy(self):
        return Grid(deepcopy(self.grid))
    
    def coords(self) -> typing.List[typing.List[int]]:
        return [(r, c) for r in range(self.nrows) for c in range(self.ncols)]
    
    def get_row(self, row: int):
        assert 0 <= row < self.nrows, f"row {row} is OOB"
        return self.grid[row]
        
    def get_col(self, col: int):
        assert 0 <= col < self.ncols, f"row {col} is OOB"
        return transpose(*self.grid)[col]
    
    def set_row(self, row: int, new_row: typing.List[T]):
        assert 0 <= row < self.nrows, f"row {row} is OOB"
        assert len(new_row) == self.ncols, f"new_row {new_row} is wrong length"
        self.grid[row] = new_row
        
    def set_col(self, col: int, new_col: typing.List[T]):
        assert 0 <= col < self.ncols, f"col {col} is OOB"
        assert len(new_col) == self.nrows, f"new_col {new_col} is wrong length"
        for r in range(self.nrows):
            self.grid[r][col] = new_col[r]
            
    def shift_row(self, row: int, amount: int):
        assert 0 <= row < self.nrows, f"row {row} is OOB"
        self.grid[row] = self.grid[row][amount:] + self.grid[row][:amount]
        
    def shift_col(self, col: int, amount: int):
        assert 0 <= col < self.ncols, f"col {col} is OOB"
        new_col = self.get_col(col)
        new_col = new_col[amount:] + new_col[:amount]
        self.set_col(col, new_col)
    
    def rows(self):
        return self.grid
    
    def cols(self):
        return transpose(*self.grid)
    
    def in_bounds(self, row: int, col: int) -> bool:
        return 0 <= row < self.nrows and 0 <= col < self.ncols
    
    def find(self, item: T) -> typing.Tuple[int, int]:
        for c in self.coords():
            if self[c] == item:
                return c
    
    def findall(self, item: T) -> typing.Tuple[int, int]:
        result = []
        for c in self.coords():
            if self[c] == item:
                result.append(c)
        return result
    
    def findall_regex(self, regex) -> typing.Tuple[int, int]:
        result = []
        for c in self.coords():
            if re.match(regex, self[c]):
                result.append(c)
        return result
    
    def findall_func(self, func) -> typing.Tuple[int, int]:
        result = []
        for c in self.coords():
            if func(self[c]):
                result.append(c)
        return result
    
    def count(self, item: T) -> int:
        return sum([row.count(item) for row in self.grid])
    
    def points_map(self, func, points: typing.List[typing.Tuple[int, int]]):
        for p in points:
            assert self.in_bounds(*p), f"cannot map point {p} as it is not in the grid"
            self.grid[p] = func(self.grid[p])
            
    def section_map(self, func, top_left: typing.Tuple[int, int], bottom_right: typing.Tuple[int, int]):
        for r in range(top_left[0], bottom_right[0]+1):
            for c in range(top_left[1], bottom_right[1]+1):
                self.grid[r][c] = func(self.grid[r][c])
            
    def get_neighbors(self, coord, deltas):
        out = []
        for delta in deltas:
            p_row, p_col = tadd(coord, delta)
            if self.in_bounds(p_row, p_col):
                out.append((p_row, p_col))
        return out
    
    def get_neighbors_items(self, coord, deltas, fill=None):
        """
        coord, value
        """
        out = []
        for delta in deltas:
            p_row, p_col = tadd(coord, delta)
            if self.in_bounds(p_row, p_col):
                out.append(((p_row, p_col), self[(p_row, p_col)]))
            elif fill is not None:
                out.append(((p_row, p_col), fill))
        return out

    def get_neighbors_values(self, coord, deltas, fill=None):
        out = []
        for delta in deltas:
            p_row, p_col = tadd(coord, delta)
            if self.in_bounds(p_row, p_col):
                out.append(self[(p_row, p_col)])
            elif fill is not None:
                out.append(fill)
        return out
    
    def middle(self):
        assert self.nrows % 2 == 1 and self.ncols % 2 == 1, "grid is not odd dimensions"
        return (self.nrows//2, self.ncols//2)
    
    def join(self, other, right=True):
        if right:
            return Grid([row + other_row for row, other_row in zip(self.grid, other.grid)])
        else:
            return Grid([*self.grid, *other.grid])
    
    def section(self, top_left, bottom_right):
        return Grid([row[top_left[1]:bottom_right[1]+1] for row in self.grid[top_left[0]:bottom_right[0]+1]])
    
    def set_section(self, top_left, bottom_right, new_grid):
        assert len(new_grid) == bottom_right[0] - top_left[0] + 1, "new_grid has wrong number of rows"
        assert len(new_grid[0]) == bottom_right[1] - top_left[1] + 1, "new_grid has wrong number of cols"
        for r in range(top_left[0], bottom_right[0]+1):
            for c in range(top_left[1], bottom_right[1]+1):
                self.grid[r][c] = new_grid[r-top_left[0]][c-top_left[1]]
    
    
    def split(self, n_rows, n_cols=None):
        if n_cols is None: n_cols = n_rows
        assert self.nrows % n_rows == 0
        assert self.ncols % n_cols == 0
        return [self.section((r*n_rows, c*n_cols), ((r+1)*n_rows-1, (c+1)*n_cols-1)) for r in range(self.nrows//n_rows) for c in range(self.ncols//n_cols)]
    
    def rotations(self):
        return [self, self.rotate_right(), self.rotate_180(), self.rotate_left()]
    
    def flips(self):
        return [self, self.flip_horizontal(), self.flip_vertical()]
    
    def transformations(self):
        return [self, self.rotate_right(), self.rotate_180(), self.rotate_left(), (flipped := self.flip_horizontal()), flipped.rotate_right(), flipped.rotate_180(), flipped.rotate_left()]
    
    def rotate(self, inplace=False):
        self.rotate_right(inplace=inplace)
    
    def rotate_right(self, inplace=False):
        if inplace:
            self.grid = list(zip(*self.grid[::-1]))
        else:
            return Grid(list(zip(*self.grid[::-1])))
    
    def rotate_left(self, inplace=False):
        if inplace:
            self.grid = list(zip(*self.grid))[::-1]
        else:
            return Grid(list(zip(*self.grid))[::-1])
        
    def rotate_180(self, inplace=False):
        if inplace:
            self.grid = [row[::-1] for row in self.grid[::-1]]
        else:
            return Grid([row[::-1] for row in self.grid[::-1]])
        
    def flip_horizontal(self, inplace=False):
        if inplace:
            self.grid = [row[::-1] for row in self.grid]
        else:
            return Grid([row[::-1] for row in self.grid])
        
    def flip_vertical(self, inplace=False):
        if inplace:
            self.grid = self.grid[::-1]
        else:
            return Grid(self.grid[::-1])
    
    def map(self, func, inplace=False):
        if inplace:
            self.grid = [lmap(func, row) for row in self.grid]
        else:
            return Grid([lmap(func, row) for row in self.grid])
        
    def sum(self):
        return sum([sum(row) for row in self.grid])
    
    def max(self, key=None):
        return max([max(row, key=key) for row in self.grid], key=key)
    
    def min(self, key=None):
        return min([min(row, key=key) for row in self.grid], key=key)
    
    def __add__(self, other):
        if isinstance(other, Grid):
            return Grid([ladd(row, other_row) for row, other_row in zip(self.grid, other.grid)])
        else:
            return Grid([ladd(row, [other] * len(row)) for row in self.grid])
        
    def __sub__(self, other):
        if isinstance(other, Grid):
            return Grid([lsub(row, other_row) for row, other_row in zip(self.grid, other.grid)])
        else:
            return Grid([lsub(row, [other] * len(row)) for row in self.grid])
        
    def __mul__(self, other):
        if isinstance(other, Grid):
            return Grid(matmat(self.grid, other.grid))
        elif isinstance(other, list):
            return Grid(matvec(self.grid, other))
        else:
            return Grid([lmul(row, [other] * len(row)) for row in self.grid])
        
    def __pow__(self, other):
        assert isinstance(other, int)
        return Grid(matexp(self.grid, other))
            
    def __contains__(self, item: typing.Union[typing.Tuple[int, int], typing.List[int], T]) -> bool:
        if isinstance(item, tuple):
            return self.in_bounds(*item)
        else:
            return any([item in row for row in self.grid])
        
    def __iter__(self):
        """
        Iterating over a grid gives you (coord, value) pairs.
        """
        for coord in self.coords():
            yield coord, self[coord]
    
    def __getitem__(self, coord: typing.Union[typing.Tuple[int, int], typing.List[int]]) -> T:
        return self.grid[coord[0]][coord[1]]
    
    def __setitem__(self, coord: typing.Union[typing.Tuple[int, int], typing.List[int]], value) -> T:
        self.grid[coord[0]][coord[1]] = value
        
    def __len__(self):
        return self.nrows
    
    def print(self, sep='', fill=' '):
        max_len = len(str(self.max(key=lambda x: len(str(x)))))
        print("\n".join([sep.join([str(item).rjust(max_len, fill) for item in line]) for line in self.grid]))
    
    def __repr__(self):
        max_len = len(str(self.max(key=lambda x: len(str(x)))))
        return "\n".join([''.join([str(item).rjust(max_len, ' ') for item in line]) for line in self.grid])
    
    def __lt__(self, other):
        return self
    
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
#endregion
#region aliases
Matrix = Grid
cumsum = partial_sum
tdot = ldot
CTD = CHAR_TO_DELTA
GD = GRID_DELTA
OD = OCT_DELTA
#endregion
#region running
def get_solution_booleans(argv):
    one = two = False
    e1 = e2 = ex1 = ex2 = r1 = r2 = True
    ex1 = ex2 = False
    if len(argv) > 1:
        e1 = e2 = ex1 = ex2 = r1 = r2 = False
        if '1' in argv[1]: 
            one = True
            if '1' == argv[1]: e1 = r1 = True
            if 'a' in argv[1]: e1 = ex1 = r1 = True
            if 'r' in argv[1] or 's' in argv[1]: r1 = True
            if 'e' in argv[1]: e1 = True
            if 'x' in argv[1]: ex1 = True
        elif '2' in argv[1]:
            two = True
            if '2' == argv[1]: e2 = r2 = True
            if 'a' in argv[1]: e2 = ex2 = r2 = True
            if 'r' in argv[1] or 's' in argv[1]: r2 = True
            if 'e' in argv[1]: e2 = True
            if 'x' in argv[1]: ex2 = True
    return one, two, e1, e2, ex1, ex2, r1, r2
#endregion
