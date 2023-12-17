from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    grid = s_to_grid(d)
    result = 0
    start = ((0, 0), '')
    goal = (grid.nrows - 1, grid.ncols - 1)
    print(grid)
    def expand(node):
        coord, path = node
        result = []
        # print(coord, path)
        for direction in [turn_left(path[-1]), path[-1], turn_right(path[-1])] if path else 'DR':
            if path == direction * 3: continue
            nxt = tadd(coord, CTD[direction])
            if nxt not in grid: continue
            result.append((int(grid[nxt]), (nxt, path[-2:] + direction)))
        # print(result)
        return result

    # def heuristic(node):
    #     coord, path = node
    #     return dist1(coord, goal)
    
    
    dists, _ = dijkstra(start, to_node=goal, expand=expand)
        
        
    # print(dists)
    
    return min([dist for val, dist in dists.items() if val[0] == goal])

def solve2(d):
    grid = s_to_grid(d)
    result = 0
    start = ((0, 0), '')
    goal = (grid.nrows - 1, grid.ncols - 1)
    print(grid)
    def expand(node):
        coord, path = node
        result = []
        # print(coord, path)
        dirs = path[-1] if path else 'DR'
        if path and path[-4:] == path[-1] * 4:
            # print('hi')
            dirs+=turn_left(path[-1])
            dirs+=turn_right(path[-1])
            # print(dirs)
        for direction in dirs:
            if path and direction == path[-1] and path == direction * 10: continue
            nxt = tadd(coord, CTD[direction])
            if nxt not in grid: continue
            result.append((int(grid[nxt]), (nxt, path[-9:] + direction)))
        # print(result)
        return result

    def heuristic(node):
        coord, path = node
        return dist1(coord, goal)
    
    
    dists, _ = dijkstra(start, to_node=goal, expand=expand, heuristic=heuristic)
    # print(dists)
        
    # print(dists)
    
    return min([(dist, val) for val, dist in dists.items() if val[0] == goal])


s = """
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533


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