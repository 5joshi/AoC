from utils import *

inp = get_data(year=2021, day=20)

NINE_DELTA = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)] 

def solve1(d, n=2):
    inp = d.split("\n\n")
    mapping = lmap(lambda x: str(int(x == "#")), inp[0])
    grid = dict()
    
    for x, row in enumerate(inp[1].splitlines()):
        for y, cell in enumerate(row):
            grid[(x, y)] = str(int(cell == '#'))
            
    for i in range(n):
        min_row, max_row = min_max(lmap(lambda x: x[0], grid.keys()))
        min_col, max_col = min_max(lmap(lambda x: x[1], grid.keys()))
        new_grid = dict()
        
        for x in range(min_row - 1, max_row + 2):
            for y in range(min_col - 1, max_col + 2):
                neighbors = ""
                
                for delta in NINE_DELTA:
                    neighbor = tadd((x, y), delta)
                    if neighbor in grid:
                        neighbors += str(grid[neighbor])
                    else:
                        neighbors += str(int(i % 2 == 1) * int(mapping[0]))
                
                new_grid[(x, y)] = mapping[int(neighbors, 2)]
                
        grid = new_grid
    
    return Counter(grid.values())['1']

def solve2(d):
    return solve1(d, n=50)


s = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
"""
s2 = """
"""

print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve1(s2))
print("Actual Solution:", solve1(inp))

print("PART 2")
print("Example Solution:", solve2(s))
# print("Example 2 Solution:", solve2(s2))
print("Actual Solution:", solve2(inp))
