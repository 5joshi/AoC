from utils import *

inp = get_data(year=2023)

def solve1(d):
    grid = Grid(lmap(list, d.splitlines()))
    START = grid.find("S")
    directions = {pipe: directions for pipe, directions in every_n('S  .  - LR | UD F DR L UR J UL 7 DL'.split(' '), 2)}
    for direction, opposite in zip('UDLR', 'DURL'):
        if opposite in directions[grid[tadd(START, CHAR_TO_DELTA[direction])]]:
            directions['S'] += direction
        
    def expand(coords):
        node = grid[coords]
        deltas = [CHAR_TO_DELTA[direction] for direction in directions[node]]
        return grid.get_neighbors_coords(coords, deltas=deltas)
        
    dists, _ = bfs(START, expand)
    print(max(dists, key=lambda x: x[1]))
    return max(dists.values())


def possibly_inside(direction, found_pipes):
    num_pipes = 0
    found_pipes = found_pipes[direction]
    if direction in 'LR':
        num_pipes += found_pipes['|']
        num_pipes += 0.5 * abs(found_pipes['F'] - found_pipes['7'])
        num_pipes += 0.5 * abs(found_pipes['J'] - found_pipes['L'])
    elif direction in 'UD':
        num_pipes += found_pipes['-']
        num_pipes += 0.5 * abs(found_pipes['J'] - found_pipes['7'])
        num_pipes += 0.5 * abs(found_pipes['F'] - found_pipes['L'])
        
    return (num_pipes % 2) == 1

def solve2(d):
    grid = Grid(lmap(list, d.splitlines()))
    result = 0
    START = grid.find("S")
    directions = {pipe: directions for pipe, directions in every_n('S  .  - LR | UD F DR L UR J UL 7 DL'.split(' '), 2)}
    for direction, opposite in zip('UDLR', 'DURL'):
        if opposite in directions[grid[tadd(START, CHAR_TO_DELTA[direction])]]:
            directions['S'] += direction
        
    def expand(coords):
        node = grid[coords]
        deltas = [CHAR_TO_DELTA[direction] for direction in directions[node]]
        return grid.get_neighbors_coords(coords, deltas=deltas)
        
    dists, _ = bfs(START, expand)
    
    new_grid = Grid(make_grid(grid.width, grid.height, fill='.'))
    for coord in grid.coords():
        if coord not in dists:
            found_pipes = dict({direction: defaultdict(int) for direction in 'UDLR'})
            for direction in 'UDLR':
                curr = tadd(coord, CHAR_TO_DELTA[direction])    
                while grid.in_bounds(*curr):
                    if curr in dists:
                        found_pipes[direction][grid[curr]] += 1
                    curr = tadd(curr, CHAR_TO_DELTA[direction])
                    
                    
                    
            if any(possibly_inside(direction, found_pipes) for direction in 'UDLR'):
                result += 1
                new_grid[coord] = 'X'
    new_grid.print()
            
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
