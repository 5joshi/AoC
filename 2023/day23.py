from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    grid = s_to_grid(d)
    start = (grid.find('.'), frozenset())
    
    def expand(node):
        coord, seen = node
        ret = []
        deltas = GRID_DELTA
        if grid[coord] in '>v<^':
            deltas = [CTD[grid[coord]]]
        for n, item in grid.get_neighbors_items(coord, deltas):
            if item in '.>v^<' and n not in seen:
                ret.append((n, frozenset(seen | {n})))
        return ret
    
    result = 0
    dists, _ = bfs(start, expand)
    for (coord, path), dist in dists.items():
        if coord == (grid.nrows - 1, grid.ncols - 2):
            # print(coord, dist)
            # test = points_to_grid(path)
            # print(test)
            result = max(result, dist)
    return result

def solve2(d):
    grid = s_to_grid(d)
    start = grid.find('.')
    graph = defaultdict(set)
    q = deque()
    q.append(start)
    
    def expand(node):
        coord, seen = node
        # print(node)
        return [(c, frozenset(seen | {c})) for c, item in grid.get_neighbors_items(coord, GRID_DELTA) if item in '.>v^<' and c not in seen]

    def graph_expand(node):
        coord, seen = node
        return [(cost, (c, frozenset(seen | {c}))) for c, cost in graph[coord] if c not in seen]
    
    while q:
        node = q.popleft()
        if node in graph: continue
        for n, seen in expand((node, {node})):
            cost = 1
            while len(nxt := expand((n, seen))) == 1:
                n, seen = nxt[0]
                cost += 1
            graph[node].add((n, cost))
            q.append(n)

    print(graph)
        
    q = deque()
    q.append(((start, {start}), 0))
    result = 0
    while q:
        (coord, seen), length = q.popleft()
        if coord == (grid.nrows - 1, grid.ncols - 2):
            if length > result:
                result = length
                print(result)
            # result = max(result, length)
            # print(length, result)
            
        for cost, n in graph_expand((coord, seen)):
            q.append((n, length + cost))
        
    # dists, _ = dijkstra(start, graph_expand)
    # print(dists)
    # print(max(dists.items(), key=lambda x: x[1]))
        
    
    # q = []
    # q.append(start)
    # sols = set()
    # while q:
    #     # q.sort(key=lambda x: len(x[1]), reverse=True)
    #     # print(q)
    #     coord, seen = q.pop(0)
    #     result = 0
    #     if coord == (grid.nrows - 1, grid.ncols - 2):
    #         sols.add(len(seen))
    #         print(len(seen), max(sols))
    #     for n, item in grid.get_neighbors_items(coord, GRID_DELTA):
    #         if item in '.>v^<' and n not in seen:
    #             # result = max(result, try_paths((n, frozenset(seen | {n}))) + 1)
    #             q.append((n, frozenset(seen | {n})))
    #             # if res := try_paths((n, frozenset(seen | {n}))):
    #             #     return res
    
    return result


s = """
#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#

""".strip()
s2 = """

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