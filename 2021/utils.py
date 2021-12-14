# Credits to mcpower for pretty much all of these utils
#region Imports
import collections
import copy
import functools as ft
import heapq
import itertools as it
import math
import operator
import re
import sys
import timeit
import typing
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import reduce
from pprint import pprint
from aocd import get_data, submit
#endregion

sys.setrecursionlimit(100000)
T = typing.TypeVar("T")

# Copy a function if you need to modify it.

# region Strings, lists, dicts
def transpose(*iterables):
    return list(zip(*iterables))


def lmap(func, *iterables):
    return list(map(func, *iterables))


def lfilter(func, *iterables):
    return list(filter(func, *iterables))


def make_grid(*dimensions: typing.List[int], fill=None):
    "Returns a grid such that 'dimensions' is juuust out of bounds."
    if len(dimensions) == 1:
        return [fill for _ in range(dimensions[0])]
    next_down = make_grid(*dimensions[1:], fill=fill)
    return [list(next_down) for _ in range(dimensions[0])]


def gridmap(func, grid):
    return [lmap(func, row) for row in grid]


def number_grid(inp):
    return lmap(lambda l: [int(x) for x in l], inp.splitlines())


def print_gridmap(grid: typing.Set[typing.Tuple[int, int]] | typing.Dict[typing.Tuple[int, int], T], fill=" ", rows=False):
    print(gridmap_to_str(grid, fill, rows))


def gridmap_to_str(grid: typing.Set[typing.Tuple[int, int]] | typing.Dict[typing.Tuple[int, int], T], fill=" ", rows=False):
    left, right = min_max([y for (_, y) in grid])
    up, down = min_max([x for (x, _) in grid])
    maxrow = max(len(str(up)), len(str(down)))
    result = "\n" 
    if isinstance(grid, set):
        for y in range(left, right+1):
            result += (str(y).rjust(maxrow+1) + ": ") * rows
            result += " ".join(["#" if (x, y) in grid else fill for x in range(up, down+1)]) + "\n"
    elif isinstance(grid, dict):
        for y in range(left, right+1):
            result += (str(y).rjust(maxrow+1) + ": ") * rows
            result += " ".join([str(grid[(x, y)]) if (x, y) in grid else fill for x in range(up, down+1)]) + "\n"
    return result


def avg(l):
    return sum(l) / len(l)


def median(l):
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2


def gauss_sum(n):
    return (n * (n + 1)) // 2


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
# endregion


#region Algorithms
class RepeatingSequence:
    def __init__(self, generator, to_hashable=lambda x: x):
        """
        generator should yield the things in the sequence.
        to_hashable should be used if things aren't nicely hashable.
        """
        self.index_to_result = []
        self.hashable_to_index = dict()
        for i, result in enumerate(generator):
            self.index_to_result.append(result)
            hashable = to_hashable(result)
            if hashable in self.hashable_to_index:
                break
            else:
                self.hashable_to_index[hashable] = i
        else:
            raise Exception("generator terminated without repeat")
        self.cycle_begin = self.hashable_to_index[hashable]
        self.cycle_end = i
        self.cycle_length = self.cycle_end - self.cycle_begin

        self.first_repeated_result = self.index_to_result[self.cycle_begin]
        self.second_repeated_result = self.index_to_result[self.cycle_end]
    
    def cycle_number(self, index):
        """
        Returns which 0-indexed cycle index appears in.
        cycle_number(cycle_begin) is the first index to return 0,
        cycle_number(cycle_end)   is the first index to return 1,
        and so on.
        """
        if index < self.cycle_begin:
            print("WARNING: Index is before cycle!!")
            return 0
        return (index - self.cycle_begin) // self.cycle_length

    def __getitem__(self, index):
        """
        Gets an item in the sequence.
        If index >= cycle_length, returns the items from the first occurrence
        of the cycle.
        Use first_repeated_result and second_repeated_result if needed.
        """
        if index < 0:
            raise Exception("index can't be negative")
        if index < self.cycle_begin:
            return self.index_to_result[index]
        cycle_offset = (index - self.cycle_begin) % self.cycle_length
        return self.index_to_result[self.cycle_begin + cycle_offset]

def bisect(f, lo=0, hi=None, eps=1e-9):
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

# Graphs
def topsort(out_edges: typing.Dict[T, typing.List[T]]) -> typing.List[T]:
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
) -> typing.Tuple[typing.Dict[T, int], typing.Dict[T, T]]:
    """
    Returns (distances, parents).
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
        if to_node is not None and node == to_node:
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
    to_node: T,
    expand: typing.Callable[[T], typing.Iterable[typing.Tuple[int, T]]],
    heuristic: typing.Optional[typing.Callable[[T], int]] = None,
) -> typing.Tuple[int, typing.List[T]]:
    g_values, parents = dijkstra(from_node, to_node=to_node, expand=expand, heuristic=heuristic)
    if to_node not in g_values:
        raise Exception("couldn't reach to_node")
    return (g_values[to_node], path_from_parents(parents, to_node))


def bfs(
    from_node: T,
    expand: typing.Callable[[T], typing.Iterable[T]],
    to_node: typing.Optional[T] = None
) -> typing.Tuple[typing.Dict[T, int], typing.Dict[T, T]]:
    """
    Returns (distances, parents).
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
        if to_node is not None and to_node in g_values:
            break
    
    return (g_values, parents)

def bfs_single(
    from_node: T,
    to_node: T,
    expand: typing.Callable[[T], typing.Iterable[T]],
) -> typing.Tuple[int, typing.List[T]]:
    g_values, parents = bfs(from_node, to_node=to_node, expand=expand)
    if to_node not in g_values:
        raise Exception("couldn't reach to_node")
    return (g_values[to_node], path_from_parents(parents, to_node))

# Distances
BLANK = object()
def hamming_distance(a, b) -> int:
    return sum(i is BLANK or j is BLANK or i != j for i, j in itertools.zip_longest(a, b, fillvalue=BLANK))


def edit_distance(a, b) -> int:
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
#endregion

#region Data Structures
class Linked(typing.Generic[T], typing.Iterable[T]):
    """
    Represents a node in a doubly linked lists.
    Can also be interpreted as a list itself.
    Consider this to be first in the list.
    """
    # item: T
    # forward: "Linked[T]"
    # backward: "Linked[T]"
    def __init__(self, item: T) -> None:
        self.item = item
        self.forward = self
        self.backward = self
    
    @property
    def val(self): return self.item
    @property
    def after(self): return self.forward
    @property
    def before(self): return self.backward

    def _join(self, other: "Linked[T]") -> None:
        self.forward = other
        other.backward = self
    
    def concat(self, other: "Linked[T]") -> None:
        """
        Concatenates other AFTER THE END OF THE LIST,
        i.e. before this current node.
        """
        first_self = self
        last_self = self.backward

        first_other = other
        last_other = other.backward
        # self ++ other
        # consider last_self and first_other
        last_self._join(first_other)
        last_other._join(first_self)
    
    def concat_immediate(self, other: "Linked[T]") -> None:
        """
        Concatenates other IN THE "SECOND" INDEX OF THE LIST
        i.e. after this current node.
        """
        self.forward.concat(other)
    
    def append(self, val: T) -> None:
        """
        Appends an item AFTER THE END OF THE LIST,
        i.e. before this current node.
        """
        self.concat(Linked(val))
    
    def append_immediate(self, val: T) -> None:
        """
        Appends an item IN THE "SECOND" INDEX OF THE LIST
        i.e. after this current node.
        """
        self.concat_immediate(Linked(val))
    
    def pop(self, n: int = 1) -> None:
        """
        Pops this node, as well as n others, off from the "parent list"
        into its own list.
        """
        assert n > 0
        first_self = self
        last_self = self.move(n-1)

        first_other = last_self.forward
        last_other = first_self.backward
        
        last_other._join(first_other)
        last_self._join(first_self)
    
    def pop_after(self, after: int, n: int = 1) -> None:
        """
        Pops the node n nodes after this node, as well as n others, into its
        own list.
        Returns the node n nodes after this node (in its new list).
        """
        to_return = self.move(after)
        to_return.pop(n)  # music
        return to_return

    def delete(self) -> None:
        """
        Deletes this node from the "parent list" into its own list.
        """
        self.pop()
    
    def delete_other(self, n: int) -> None:
        """
        Deletes a node n nodes forward, or backwards if n is negative.
        """
        to_delete = self.move(n)
        if to_delete is self:
            raise Exception("can't delete self")
        to_delete.delete()
        del to_delete
    
    def move(self, n: int) -> "Linked[T]":
        """
        Move n nodes forward, or backwards if n is negative.
        """
        out = self
        if n >= 0:
            for _ in range(n):
                out = out.forward
        else:
            for _ in range(-n):
                out = out.backward
        return out
    
    def iterate_nodes_inf(self) -> typing.Iterator["Linked[T]"]:
        cur = self
        while True:
            yield cur
            cur = cur.forward
    
    def iterate_nodes(self, count=1) -> typing.Iterator["Linked[T]"]:
        for node in self.iterate_nodes_inf():
            if node is self:
                count -= 1
                if count < 0:
                    break
            yield node
    
    def iterate_inf(self) -> typing.Iterator[T]:
        return map(lambda node: node.item, self.iterate_nodes_inf())
    
    def iterate(self, count=1) -> typing.Iterator[T]:
        return map(lambda node: node.item, self.iterate_nodes(count))
    
    def to_list(self):
        return list(self.iterate())
    
    def check_correctness(self) -> None:
        assert self.forward.backward is self
        assert self.backward.forward is self
    
    def check_correctness_deep(self) -> None:
        for node in self.iterate_nodes():
            node.check_correctness()
    
    def __iter__(self) -> typing.Iterator[T]:
        return self.iterate()
    
    def __repr__(self) -> str:
        return "Linked({})".format(self.to_list())

    @classmethod
    def from_list(cls, l: typing.Iterable[T]) -> "Linked[T]":
        it = iter(l)
        out = cls(next(it))
        for i in it:
            out.concat(cls(i))
        return out


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


# region List/Vector operations
GRID_DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]
OCT_DELTA = [(1, 1), (-1, -1), (1, -1), (-1, 1)] + GRID_DELTA
CHAR_TO_DELTA = {
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

# delta to go from p1 to p2
def get_delta(p1, p2):
    return [(p1[0]!=p2[0]) * (-1) ** (p2[0]<p1[0]), (p1[1]!=p2[1]) * (-1) ** (p2[1]<p1[1])]


def signum(n: int) -> int:
    if n > 0:
        return 1
    elif n == 0:
        return 0
    else:
        return -1
    

def turn_180(drowcol):
    drow, dcol = drowcol
    return [-drow, -dcol]


def turn_right(drowcol):
    drow, dcol = drowcol
    return [dcol, -drow]


def turn_left(drowcol):
    drow, dcol = drowcol
    return [-dcol, drow]


def get_neighbors_coords(grid, row, col, deltas):
    n, m = len(grid), len(grid[0])
    out = []
    for i, j in deltas:
        p_row, p_col = row+i, col+j
        if 0 <= p_row < n and 0 <= p_col < m:
            out.append((p_row, p_col))
    return out


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


def lget(l, i):
    if len(l) == 2: return l[i[0]][i[1]]
    for index in i: l = l[index]
    return l


def lset(l, i, v):
    if len(l) == 2:
        l[i[0]][i[1]] = v
        return
    for index in i[:-1]: l = l[index]
    l[i[-1]] = v
    
    
def points_sub_min(points):
    m = [min(p[i] for p in points) for i in range(len(points[0]))]
    return [psub(p, m) for p in points]


def points_to_grid(points, sub_min=True, flip=True):
    if sub_min:
        points = points_sub_min(points)
    if not flip:
        points = [(y, x) for x, y in points]
    grid = make_grid(max(map(snd, points))+1, max(map(fst, points))+1, '.')
    for x, y in points:
        grid[y][x] = '#'
    return grid


def print_grid(grid):
    for line in grid:
        print(*line, sep="")


def fst(x):
    return x[0]


def snd(x):
    return x[1]


def padd(x, y):
    if isinstance(x, tuple) and isinstance(y, tuple):
        return (a+b for a, b in zip(x, y))
    return [a+b for a, b in zip(x, y)]


def pneg(v):
    if isinstance(v, tuple):
        return (-i for i in v)
    return [-i for i in v]


def psub(x, y):
    if isinstance(x, tuple) and isinstance(y, tuple):
        return (a-b for a, b in zip(x, y))
    return [a-b for a, b in zip(x, y)]


def pmul(m: int, v):
    if isinstance(v, tuple):
        return (m * i for i in v)
    return [m * i for i in v]


def pdot(x, y):
    return sum(a*b for a, b in zip(x, y))


def pdist1(x, y=None):
    if y is not None:
        x = psub(x, y)
    return sum(map(abs, x))


def pdist2sq(x, y=None):
    if y is not None:
        x = psub(x, y)
    return sum(i*i for i in x)


def pdist2(v):
    return math.sqrt(pdist2sq(v))


def pdistinf(x, y=None):
    if y is not None: x = psub(x, y)
    return max(map(abs, x))

# points needed to go from p1 to p2
def line_points(p1, p2):
    dist = psub(p1, p2)
    assert 0 in dist or dist[0] == dist[1], "Can't draw straight line"
    result = [p1]
    delta = get_delta(p1, p2)
    while result[-1] != p2:
        result.append(padd(result[-1], delta))
    return result

# points needed to go delta * distance from p1
def line_from(p1, delta, distance):
    return line_points(p1, padd(p1, pmul(distance, delta)))
    
# endregion


# region Matrices

class Grid(typing.Generic[T]):
    """2D only!!!"""
    def __init__(self, grid: typing.List[typing.List[T]]) -> None:
        self.grid = grid
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
    
    def coords(self) -> typing.List[typing.List[int]]:
        return [(r, c) for r in range(self.rows) for c in range(self.cols)]
    
    def get_row(self, row: int):
        assert 0 <= row < self.rows, f"row {row} is OOB"
        return self.grid[row]
        
    def get_col(self, col: int):
        assert 0 <= col < self.cols, f"row {col} is OOB"
        return transpose(self.grid)[col]
    
    def rows(self):
        return self.grid
    
    def cols(self):
        return transpose(self.grid)
    
    def in_bounds(self, row: int, col: int) -> bool:
        return 0 <= row < self.rows and 0 <= col < self.cols
    
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
    
    def count(self, item: T) -> int:
        return sum([row.count(item) for row in self.grid])
    
    def points_map(self, func, points: typing.List[typing.Tuple[int, int]]):
        for p in points:
            assert self.in_bounds(*p), f"cannot map point {p} as it is not in the grid"
            self.grid[p] = func(self.grid[p])
    
    def map(self, func):
        self.grid = [lmap(func, row) for row in self.grid]
        
    def sum(self):
        return sum([row for row in self.grid])
    
    def __contains__(self, item: typing.Tuple[int, int] | typing.List[int] | T) -> bool:
        if isinstance(item, T):
            return any([item in row for row in self.grid])
        else:
            return self.in_bounds(*item)
    
    def __getitem__(self, coord: typing.Tuple[int, int] | typing.List[int]) -> T:
        return self.grid[coord[0]][coord[1]]
    
    def print(self, sep=""):
        print("\n".join([sep.join([str(item) for item in line]) for line in self.grid]))
    
    def __repr__(self):
        return "\n".join(["".join([str(item) for item in line]) for line in self.grid])
    

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


imports = """import collections as coll
import datetime as dt
import itertools as it
import math
from operator import itemgetter as ig
import pprint as pp
import re
import sys
import typing
"""
def time(day, part):
    time = timeit.timeit(stmt=f"solve{part}(inp)", setup=f"{imports}\nfrom day{day} import solve{part}, inp\n", number=100) / 100
    print(f"Time taken: {time}s -- {time * 1000}ms -- {time * 1000 * 1000}µs")
    