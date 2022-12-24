from utils import *

# inp = get_data(year=2022, day=12)


def solve1(d):
    grid = Grid(lmap(lambda x: list(x), d.splitlines()))
    start = grid.find('S')
    goal = grid.find('E')
    grid[start] = 'a'
    grid[goal] = 'z'
    
    def expand(coord):
        return [(1, neighbor) for neighbor in grid.get_neighbors_coords(coord, GRID_DELTA) if ord(grid[neighbor]) <= (ord(grid[coord]) + 1)]
        
    path = a_star(start, goal, expand)
    return path[0]

def solve2(d):
    grid = Grid(lmap(lambda x: list(x), d.splitlines()))
    S = grid.find('S')
    start = grid.find('E')
    grid[S] = 'a'
    grid[start] = 'z'
    possible_goals = grid.findall('a')
    
    def expand(coord):
        return [neighbor for neighbor in grid.get_neighbors_coords(coord, GRID_DELTA) if ord(grid[neighbor]) >= (ord(grid[coord]) - 1)]
       
    distances, _ = bfs(start, expand)
    return min([distances[goal] for goal in possible_goals if goal in distances])
        

s = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""
s2 = """
"""

print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve1(s2))
# print("Actual Solution:", solve1(inp))

print("PART 2")
print("Example Solution:", solve2(s))
# print("Example 2 Solution:", solve2(s2))
# print("Actual Solution:", solve2(inp))
