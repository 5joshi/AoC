from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

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
                if new_node == ((15, 4), (0, -1)):
                    print(node, frozenset((node,)))
                parents[new_node] = frozenset((node,))
                g_values[new_node] = new_g
                heapq.heappush(todo, (new_g + heuristic(new_node), new_g, new_node))
            elif new_g == g_values[new_node]:
                if new_node == ((15, 4), (0, -1)):
                    print(node, frozenset({*parents[new_node], node}))
                parents[new_node] = frozenset({*parents[new_node], node})
    
    return (g_values, parents)

def solve1(d):
    grid = s_to_grid(d)
    start = grid.find("S")
    end = grid.find("E")
    
    def expand(node):
        p, d = node
        results = [(1000, (p, turn_left(d))), (1000, (p, turn_right(d)))]
        if tadd(p, d) in grid and grid[tadd(p, d)] != "#":
            results.append((1, (tadd(p, d), d)))
        return results
        
    dists, parents = dijkstra((start, CTD['E']), expand=expand, to_func=lambda n: n[0] == end)
    return {k[0]: v for k, v in dists.items()}[end]

def path_from_parents(parents: typing.Dict[T, T], end: T) -> typing.List[T]:
    """
    Returns a path from the parents obtained from dijkstra/BFS.
    """
    out = [end]
    seen = {end}
    q = [end]
    print(parents)
    while q:
        curr = q.pop(0)
        print(curr)
        if curr not in parents: continue
        for p in parents[curr]:
            if p not in seen:
                q.append(p)
                seen.add(p)
            
    out.reverse()
    return seen

def solve2(d):
    grid = s_to_grid(d)
    start = grid.find("S")
    end = grid.find("E")
    
    def expand(node):
        p, d = node
        results = [(1000, (p, turn_left(d))), (1000, (p, turn_right(d)))]
        if tadd(p, d) in grid and grid[tadd(p, d)] != "#":
            results.append((1, (tadd(p, d), d)))
        return results
        
    dists, parents = dijkstra((start, CTD['E']), expand=expand, to_func=lambda n: n[0] == end)
    k = [k for k, v in dists.items() if k[0] == end][0]
    
    seen = {k}
    q = [k]
    # pprint(parents)
    while q:
        curr = q.pop(0)
        # print(curr, parents[curr])
        if curr not in parents: continue
        for p in parents[curr]:
            if p not in seen:
                q.append(p)
                seen.add(p)
    
    pprint(seen)
    print(points_to_grid([x[0] for x in seen]))
    return len(set([x[0] for x in seen]))
    pprint(parents)
    # path = path_from_parents(parents, k)
    # points = set() 
    # print(path)
    # print([x[0] for x in path])
    # print(points_to_grid([x[0] for x in path]))
    # return len([path])
    # return {k[0]: v for k, v in dists.items()}[end]


s = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############

""".strip()
s2 = """
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################

""".strip()

if __name__ == '__main__':
    one, two, e1, e2, ex1, ex2, r1, r2 = get_solution_booleans(sys.argv)
            
    if e1 or ex1 or r1: print("PART 1")
    if e1 and s != "": print("Example Solution:", solve1(s))
    if ex1: print("Example 2 Solution:", solve1(s2))
    if r1: print("Actual Solution:", sol1 := solve1(inp))

    if e2 or ex2 or r2: print("PART 2")
    if e2 and s != "": print("Example Solution:", solve2(s))
    if ex2: print("Example 2 Solution:", solve2(s2))
    if r2: print("Actual Solution:", sol2 := solve2(inp))
    
    if (one and r1) or (two and r2):
        go = input('Submit? [y/N] ')
        if go == 'y':
            if one and r1: submit(sol1, part=1, year=YEAR, day=DAY)
            if two and r2: submit(sol2, part=2, year=YEAR, day=DAY)