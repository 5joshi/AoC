from utils import *

inp = get_data(year=2023)

def solve1(d):
    grid = Grid(lmap(list, d.splitlines()))    
    empty_rows = []
    empty_cols = []
    for idx in range(grid.nrows):
        if all([elem == '.' for elem in grid.cols()[idx]]):
            empty_cols.append(idx)
        if all([elem == '.' for elem in grid.rows()[idx]]):
            empty_rows.append(idx)
    
    galaxies = grid.findall('#')
    def dist(g1, g2):
        return pdist1(g1, g2) + len(set(range(*sorted((g1[0], g2[0])))) & set(empty_rows)) + len(set(range(*sorted((g1[1], g2[1])))) & set(empty_cols))
    
    return sum([dist(g1, g2) for g1, g2 in it.combinations(galaxies, 2)])

def solve2(d):
    grid = Grid(lmap(list, d.splitlines()))    
    empty_rows = []
    empty_cols = []
    for idx in range(grid.nrows):
        if all([elem == '.' for elem in grid.cols()[idx]]):
            empty_cols.append(idx)
        if all([elem == '.' for elem in grid.rows()[idx]]):
            empty_rows.append(idx)
    
    galaxies = grid.findall('#')
    def dist(g1, g2):
        return pdist1(g1, g2) + 999999 * (len(set(range(*sorted((g1[0], g2[0])))) & set(empty_rows)) + len(set(range(*sorted((g1[1], g2[1])))) & set(empty_cols)))
    
    return sum([dist(g1, g2) for g1, g2 in it.combinations(galaxies, 2)])


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
