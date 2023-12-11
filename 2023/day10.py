from utils import *

inp = get_data(year=2023, day=10)

def solve1(d):
    grid = Grid(lmap(list, d.splitlines()))
    start = grid.find("S")
    directions = {pipe: directions for pipe, directions in every_n('S  .  - LR | UD F DR L UR J UL 7 DL'.split(' '), 2)}
    for direction, opposite in zip('UDLR', 'DURL'):
        if opposite in directions[grid[tadd(start, CHAR_TO_DELTA[direction])]]:
            directions['S'] += direction
        
    def expand(coords):
        node = grid[coords]
        deltas = [CHAR_TO_DELTA[direction] for direction in directions[node]]
        return grid.get_neighbors(coords, deltas=deltas)
        
    dists, _ = bfs(start, expand)
    return max(dists.values())

def solve2(d):
    grid = Grid(lmap(list, d.splitlines()))
    start = grid.find("S")
    result = 0
    
    directions = defaultdict(str, {pipe: directions for pipe, directions in every_n('- LR | UD F DR L UR J UL 7 DL'.split(' '), 2)})
    pipes = invert_dict(directions)
    for direction in 'UDLR':
        delta = CHAR_TO_DELTA[direction]
        if DELTA_TO_UDLR[turn_180(delta)] in directions[grid[tadd(start, delta)]]:
            directions['S'] += direction
    grid[start] = pipes[directions['S']]
        
    def expand(coords):
        node = grid[coords]
        deltas = [CHAR_TO_DELTA[direction] for direction in directions[node]]
        return grid.get_neighbors(coords, deltas=deltas)
        
    dists, _ = bfs(start, expand)
    
    for coord in grid.coords():
        if coord not in dists:
            curr = tadd(coord, CHAR_TO_DELTA['R'])    
            num_pipes = 0
            while grid.in_bounds(*curr):
                if curr in dists:
                    num_pipes += int(grid[curr] == '|')
                    num_pipes += 0.5 * int(grid[curr] in 'FJ')
                    num_pipes -= 0.5 * int(grid[curr] in '7L') 
                curr = tadd(curr, CHAR_TO_DELTA[direction])
            result += (num_pipes % 2) == 1 
            
    return result


s = """
..........
.S------7.
.|F----7|.
.||OOOO||.
.||OOOO||.
.|L-7F-J|.
.|II||II|.
.L--JL--J.
..........

""".strip()
s2 = """
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...

""".strip()

if __name__ == '__main__':
    e1, e2, ex1, ex2, r1, r2 = get_solution_booleans(sys.argv)
            
    if e1 or ex1 or r1: print("PART 1")
    if e1: print("Example Solution:", solve1(s))
    if ex1: print("Example 2 Solution:", solve1(s2))
    if r1: print("Actual Solution:", solve1(inp))

    if e2 or ex2 or r2: print("PART 2")
    if e2: print("Example Solution:", solve2(s))
    if ex2: print("Example 2 Solution:", solve2(s2))
    if r2: print("Actual Solution:", solve2(inp))
