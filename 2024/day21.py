from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

DOOR = s_to_grid("""789
456
123
 0A""")
 
ROBOT = s_to_grid(""" ^A
<v>""")


# def path_from_parents(parents: typing.Dict[T, T], end: T) -> typing.List[T]:
#     """
#     Returns a path from the parents obtained from dijkstra/BFS.
#     """
#     def backtrack(node, path):
#         if not parents[node]:  
#             paths.append(path[::-1])
#             return
#         for parent in parents[node]:
#             backtrack(parent, path + [node])
    
#     paths = []
#     backtrack(end, [])
#     return paths

# def dijkstra(
#     from_node: T,
#     expand: typing.Callable[[T], typing.Iterable[typing.Tuple[int, T]]],
#     heuristic: typing.Optional[typing.Callable[[T], int]] = None,
#     to_node: typing.Optional[T] = None,
#     to_func: typing.Optional[typing.Callable[[T], bool]] = None,
# ) -> typing.Tuple[typing.Dict[T, int], typing.Dict[T, T]]:
#     """
#     Returns (distances, parents).
#     expand is a function that takes a node and returns an iterable of (cost, new_node).
#     heuristic is an optional function that takes a node and returns an estimate of the distance to to_node.
#     heuristic should never overestimate the cost (heuristic = lower bound).
#     Use path_from_parents(parents, node) to get a path.
#     """
#     if heuristic is None:
#         heuristic = lambda _: 0
#     seen = set()  # type: typing.Set[T]
#     g_values = {from_node: 0}  # type: typing.Dict[T, int]
#     parents = {from_node: []}  # type: typing.Dict[T, T]
    
#     # (f, g, n)
#     todo = [(0 + heuristic(from_node), 0, from_node)]  # type: typing.List[typing.Tuple[int, int, T]]

#     while todo:
#         f, g, node = heapq.heappop(todo)

#         assert node in g_values
#         assert g_values[node] <= g

#         if node in seen:
#             continue

#         assert g_values[node] == g
#         if to_node is not None and node == to_node or to_func is not None and to_func(node):
#             break
#         seen.add(node)
#         for cost, new_node in expand(node):
#             new_g = g + cost
#             if new_node not in g_values or new_g < g_values[new_node]:
#                 parents[new_node] = [node]
#                 g_values[new_node] = new_g
#                 heapq.heappush(todo, (new_g + heuristic(new_node), new_g, new_node))
#             elif new_g == g_values[new_node]:
#                 parents[new_node].append(node)
    
#     return (g_values, parents)

# def solve1(d):
#     codes = d.splitlines()
#     result = 0
    
#     for code in codes:
        
#         # node = coord, "presses"
#         def expandk(node):
#             c, p = node
#             return [(1, (nc, p)) for d in GRID_DELTA if (nc := tadd(c, d)) in DOOR] + [(1, (c, p + DOOR[c]))]
    
#         def expandr(node):
#             c, p = node
#             return [(1, (nc, p)) for d in GRID_DELTA if (nc := tadd(c, d)) in ROBOT] + [(1, (c, p + ROBOT[c]))]
            
#         def heuristic(node):
#             # print(node, node[1], code)
#             if not code.startswith(node[1]): return math.inf
#             return 0
            
            
#         start = (DOOR.find('A'), "")
#         dists, parents = dijkstra(start, expandk, to_func=lambda x: x[1] == code, heuristic=heuristic)
#         end = {k for k in dists.keys() if k[1] == code}.pop()
#         paths = [[start] + path for path in path_from_parents(parents, end)]
#         def to_written(paths):
#             written_paths = []
#             for path in paths:
#                 written_path = ""
#                 for node, newnode in windows(path, 2):
#                     if node[0] == newnode[0]:
#                         written_path += "A"
#                     else:
#                         written_path += DELTA_TO_ARROW[tsub(newnode[0], node[0])]
#                 written_paths.append(written_path)
#             return written_paths
        
#         paths = to_written(paths)
#         paths = [p for p in paths if not re.match(r"([^>v]<[^>v])|([>v<]^[>v<])|([^v<]>[^v<])|([^><]v[^><])", p)]
        
#         start = (ROBOT.find('A'), "")
#         for _ in range(2):
#             new_paths = []
#             for code in paths:
#                 dists, parents = dijkstra(start, expandr, to_func=lambda x: x[1] == code, heuristic=heuristic)
#                 end = {k for k in dists.keys() if k[1] == code}.pop()
#                 found_paths = path_from_parents(parents, end)
#                 new_paths.extend(to_written(found_paths))
#             print(new_paths)
#             paths = new_paths
#             paths = [p for p in paths if not re.match(r"([^>v]<[^>v])|([>v<]^[>v<])|([^v<]>[^v<])|([^><]v[^><])", p)]

def solve1(d):
    codes = d.splitlines()
    result = 0
    
    for code in codes:
        coords = lmap(lambda c: DOOR.find(c), code)
        
        def go(frm, to, door=False):
            if frm == to: return ["A"]
            delta = lsub(to, frm)
            result = ""
            while delta[0] < 0:
                delta[0] += 1
                result += "^"
            while delta[0] > 0:
                delta[0] -= 1
                result += "v"
            while delta[1] < 0:
                delta[1] += 1
                result += "<"
            while delta[1] > 0:
                delta[1] -= 1
                result += ">"
                
            return [result + "A", result[::-1] + "A"]
        
        def check_ext(frm, ext, door=False):
            curr=frm
            for c in ext[:-1]:
                curr=tadd(curr, CTD[c])
                if (door and DOOR[curr]) == " " or (not door and ROBOT[curr] == " "):
                    return False
            return True
        
        paths = {p for p in go(DOOR.find('A'), coords[0]) if check_ext(DOOR.find('A'), p, door=True)}
        for frm, to in windows(coords, 2):
            paths = {path + ext for path in paths for ext in go(frm, to) if check_ext(frm, ext, door=True)}
            
        # print(paths)
        def cost(path):
            result = 0
            for c, nc in windows("A" + path, 2):
                result += dist1(ROBOT.find(c), ROBOT.find(nc))
            return result
        
                
                
            
        for i in range(2):
            new_paths = set()
            # prune paths
            best_cost = min(cost(path) for path in paths)
            paths = {path for path in paths if cost(path) == best_cost}
            # print(paths)
            for path in paths:
                coords = lmap(lambda c: ROBOT.find(c), path)
                curr_paths = {p for p in go(ROBOT.find('A'), coords[0]) if check_ext(ROBOT.find('A'), p)}
                for frm, to in windows(coords, 2):
                    curr_paths = {path + ext for path in curr_paths for ext in go(frm, to) if check_ext(frm, ext)}
                new_paths |= curr_paths
            paths = new_paths
    
        # print(len(min(paths, key=len)), ints(code)[0], min(paths, key=len))
        result += len(min(paths, key=len)) * ints(code)[0]
        
    return result

def solve2(d):
    codes = d.splitlines()
    result = 0
    
    for code in codes:
        coords = lmap(lambda c: DOOR.find(c), code)
        
        def go(frm, to):
            if frm == to: return ["A"]
            delta = lsub(to, frm)
            result = ""
            while delta[0] < 0:
                delta[0] += 1
                result += "^"
            while delta[0] > 0:
                delta[0] -= 1
                result += "v"
            while delta[1] < 0:
                delta[1] += 1
                result += "<"
            while delta[1] > 0:
                delta[1] -= 1
                result += ">"
                
            return [result + "A", result[::-1] + "A"]
        
        def check_ext(frm, ext):
            curr=frm
            for c in ext[:-1]:
                curr=tadd(curr, CTD[c])
                if DOOR[curr] == " ":
                    return False
            return True
        
        paths = {p for p in go(DOOR.find('A'), coords[0]) if check_ext(DOOR.find('A'), p)}
        for frm, to in windows(coords, 2):
            paths = {path + ext for path in paths for ext in go(frm, to) if check_ext(frm, ext)}
            
        # print(paths)
        def cost(path):
            result = 0
            for c, nc in windows("A" + path, 2):
                result += dist1(ROBOT.find(c), ROBOT.find(nc))
            return result
        
        best_cost = min(cost(path) for path in paths)
        paths = {path for path in paths if cost(path) == best_cost}
          
        @lru_cache      
        def go(frm, to):
            if frm == to: return "A"
            if frm == 'v':
                if to == 'A': return ">^A"
                return f"{to}A"
            elif frm == '^':
                if to == 'A': return ">A"
                return f"v{go('v', to)}"
            elif frm == '<':
                if to == 'A': return ">>^A"
                return f">{go('v', to)}"
            elif frm == '>':
                if to == 'A': return "^A"
                return f"<{go('v', to)}"
            
            if to == '^': return "<A"
            elif to == '>': return "vA"
            elif to == 'v': return "<vA"
            return "v<<A"        
            
        print(paths)
        for i in tqdm(range(25)):

            
            paths = {"".join(go(a, b) for a, b in windows('A' + path, 2)) for path in paths}
            # for path in paths:
            #     curr_paths = go('A', path[0])
            #     for frm, to in windows(coords, 2):
            #         curr_paths = {path + ext for path in curr_paths for ext in go(frm, to) if check_ext(frm, ext)}
            #     new_paths |= curr_paths
            # paths = new_paths
            # print(paths)
    
        print(len(min(paths, key=len)), ints(code)[0], min(paths, key=len))
        result += len(min(paths, key=len)) * ints(code)[0]
        
    return result


s = """
029A
980A
179A
456A
379A
""".strip()
s2 = """
029A
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