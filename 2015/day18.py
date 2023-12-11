from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    grid = Grid(lmap(list, d.splitlines()))
    
    for _ in range(100):
        new_points = []
        for coord in grid.coords():
            if grid[coord] == '.' and grid.get_neighbors_values(coord, OCT_DELTA).count('#') == 3:
                new_points.append(coord)
            elif grid[coord] == '#' and grid.get_neighbors_values(coord, OCT_DELTA).count('#') in [2, 3]:
                new_points.append(coord)
        grid = points_to_grid(new_points, sub_min=False, dimensions=(grid.nrows, grid.ncols))
            
    return grid.count('#')

def solve2(d):
    grid = Grid(lmap(list, d.splitlines()))
    for coord in [(0, 0), (0, grid.ncols - 1), (grid.nrows - 1, 0), (grid.nrows - 1, grid.ncols - 1)]:
        grid[coord] = '#'
    
    for _ in range(100):
        new_points = [(0, 0), (0, grid.ncols - 1), (grid.nrows - 1, 0), (grid.nrows - 1, grid.ncols - 1)]
        for coord in grid.coords():
            if grid[coord] == '.' and grid.get_neighbors_values(coord, OCT_DELTA).count('#') == 3:
                new_points.append(coord)
            elif grid[coord] == '#' and grid.get_neighbors_values(coord, OCT_DELTA).count('#') in [2, 3]:
                new_points.append(coord)
        grid = points_to_grid(new_points, sub_min=False, dimensions=(grid.nrows, grid.ncols))
            
    return grid.count('#')


s = """
.#.#.#
...##.
#....#
..#...
#.#..#
####..
""".strip()
s2 = """

""".strip()

if __name__ == '__main__':
    one, two, e1, e2, ex1, ex2, r1, r2 = get_solution_booleans(sys.argv)
            
    if e1 or ex1 or r1: print("PART 1")
    if e1: print("Example Solution:", solve1(s))
    if ex1: print("Example 2 Solution:", solve1(s2))
    if r1: print("Actual Solution:", sol1 := solve1(inp))

    if e2 or ex2 or r2: print("PART 2")
    if e2: print("Example Solution:", solve2(s))
    if ex2: print("Example 2 Solution:", solve2(s2))
    if r2: print("Actual Solution:", sol2 := solve2(inp))
    
    if (one and r1) or (two and r2):
        go = input('Submit? [y/N] ')
        if go == 'y':
            if one and r1: submit(sol1, part=1, year=YEAR, day=DAY)
            if two and r2: submit(sol2, part=2, year=YEAR, day=DAY)