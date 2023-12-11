from utils import *

inp = get_data(year=2023)

def solve1(d):
    grid = Grid(lmap(list, d.splitlines()))
    result = 0
    
    col_indices = []
    for col in range(grid.ncols):
        if all([row[col] == '.' for row in grid.rows()]):
            col_indices.append(col)
            
    row_indices = []
    for idx, row in enumerate(grid.rows()):
        if all([elem == '.' for elem in row]):
            row_indices.append(idx)
    
    galaxies = grid.findall('#')
    for pair in it.combinations(galaxies, 2):
        dist = pdist1(pair[0], pair[1]) + len([col for col in col_indices if (pair[0][1] < col < pair[1][1] or pair[1][1] < col < pair[0][1])]) +  len([row for row in row_indices if (pair[0][0] < row < pair[1][0] or pair[1][0] < row < pair[0][0])])
        result += dist
        # print(pair, dist)
    # pair = galaxies[0], galaxies[6]
    # dist = pdist1(pair[0], pair[1]) + len([col for col in col_indices if pair[0][1] < col < pair[1][1]]) + len([row for row in row_indices if pair[0][0] < row < pair[1][0]])
    # print(row_indices, col_indices)
    # print(dist,len([col for col in col_indices if pair[0][1] < col < pair[1][1]]), len([row for row in row_indices if pair[0][0] < row < pair[1][0]]) )
    return result

def solve2(d):
    grid = Grid(lmap(list, d.splitlines()))
    result = 0
    
    col_indices = []
    for col in range(grid.ncols):
        if all([row[col] == '.' for row in grid.rows()]):
            col_indices.append(col)
            
    row_indices = []
    for idx, row in enumerate(grid.rows()):
        if all([elem == '.' for elem in row]):
            row_indices.append(idx)
    
    galaxies = grid.findall('#')
    for pair in it.combinations(galaxies, 2):
        dist = pdist1(pair[0], pair[1]) + 999999 * len([col for col in col_indices if (pair[0][1] < col < pair[1][1] or pair[1][1] < col < pair[0][1])]) + 999999 * len([row for row in row_indices if (pair[0][0] < row < pair[1][0] or pair[1][0] < row < pair[0][0])])
        result += dist
        # print(pair, dist)
    # pair = galaxies[0], galaxies[6]
    # dist = pdist1(pair[0], pair[1]) + len([col for col in col_indices if pair[0][1] < col < pair[1][1]]) + len([row for row in row_indices if pair[0][0] < row < pair[1][0]])
    # print(row_indices, col_indices)
    # print(dist,len([col for col in col_indices if pair[0][1] < col < pair[1][1]]), len([row for row in row_indices if pair[0][0] < row < pair[1][0]]) )
    return result


s = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
""".strip()
s2 = """

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
