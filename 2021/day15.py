from re import S
from utils import *

inp = get_data(year=2021, day=15)


def solve1(d):
    grid = number_grid(d)
    rows, cols = dimensions(grid)
    
    def expand(coord):
        return [(grid[x][y], (x, y)) for x, y in grid_neighbors(grid, *coord, GRID_DELTA)]
        
    path = a_star((0, 0), (rows-1, cols-1), expand)
    return path[0]

def solve2(d):
    grid = number_grid(d)
    rows, cols = dimensions(grid)
    
    def modified_neighbors(grid, row, col, deltas):
        out = []
        for i, j in deltas:
            p_row, p_col = row+i, col+j
            if 0 <= p_row < (rows * 5) and 0 <= p_col < (cols * 5):
                value = (((grid[p_row % rows][p_col % cols] + (p_row // rows) + (p_col // cols)) - 1) % 9) + 1
                out.append((value, (p_row, p_col)))
        return out
    
    def expand(coord):
        return modified_neighbors(grid, coord[0], coord[1], GRID_DELTA)
    
    path = a_star((0, 0), (rows*5 - 1, cols*5 - 1), expand)
    return path[0]


s = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""
s2 = """8
"""

# print("PART 1")
# print("Example Solution:", solve1(s))
# # print("Example 2 Solution:", solve1(s2))
# print("Actual Solution:", solve1(inp))

# print("PART 2")
# print("Example Solution:", solve2(s))
# # print("Example 2 Solution:", solve2(s2))
# print("Actual Solution:", solve2(inp))
if __name__ == "__main__":
    time(15, 2, amount=1)