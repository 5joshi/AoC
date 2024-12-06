from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    grid = s_to_grid(d)
    curr, obstacles = grid.find("^"), set(grid.findall("#"))
    direction = CHAR_TO_DELTA['U']
    visited = set()
    
    while curr in grid:
        visited.add(curr)
        while (nxt := tadd(curr, direction)) in obstacles:
            direction = turn_right(direction)
        curr = nxt
    
    return len(visited)

def solve2(d):
    grid = s_to_grid(d)
    origin, obstacles = grid.find("^"), set(grid.findall("#"))
    visited = set()
    
    def simulate(obstacles=obstacles, curr=origin, direction=CHAR_TO_DELTA['U']):
        nonlocal visited
        visited = set()
        while curr in grid and (curr, direction) not in visited:
            visited.add((curr, direction))
            while (nxt := tadd(curr, direction)) in obstacles:
                direction = turn_right(direction)
            curr = nxt
        return curr in grid
    
    simulate()
    to_check = set(x for x, _ in visited) - {origin}
    
    return sum(simulate({*obstacles, x}) for x in to_check)

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