from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    grid = s_to_grid(d)
    agent = grid.find("^")
    direction = CHAR_TO_DELTA['U']
    result = 0
    
    while agent in grid:
        grid[agent] = "X"
        nxt = tadd(agent, direction)
        if nxt not in grid: break
        if grid[nxt] == "#":
            direction = turn_right(direction)
            nxt = tadd(agent, direction)
        agent = nxt
    
    return grid.count("X")

def solve2(d):
    grid = s_to_grid(d)
    origin = grid.find("^")
    visited = set()
    result = 0
    
    def simulate(grid):
        nonlocal visited
        agent = origin
        direction = CHAR_TO_DELTA['U']
        visited = set()
        
        while (agent, direction) not in visited:
            visited.add((agent, direction))
            nxt = tadd(agent, direction)
            if nxt not in grid: return False
            while grid[nxt] == "#":
                direction = turn_right(direction)
                nxt = tadd(agent, direction)
            if nxt not in grid: return False
            agent = nxt
        
        return agent in grid
    
    simulate(grid)
    to_check = set(x for x, _ in visited) - {origin}
    
    valid = set()
    for idx, coord in enumerate(to_check):
        grid[coord] = "#"
        if simulate(grid): valid.add(coord)
        grid[coord] = "."
        
    for x, y in sorted(list(valid)):
        print(f"{x},{y}")

s = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...

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