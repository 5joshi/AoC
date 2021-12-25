from utils import *

inp = get_data(year=2021, day=25)


def solve1(d):
    lines = d.splitlines()
    result = 0
    grid = defaultdict(lambda: '.')
    for x, line in enumerate(lines):
        for y, cell in enumerate(line):
            if cell in '>v': grid[(x, y)] = cell
            
    height = max(grid.keys(), key=fst)[0]
    width = max(grid.keys(), key=snd)[1]
    
    def move(grid, right=True):
        change = False
        if right: 
            symbol = '>'
            mod = width + 1
            idx = 1
        else: 
            symbol = 'v'
            mod = height + 1
            idx = 0
            
        new_grid = deepcopy(grid)
        for x in range(height+1):
            for y in range(width+1):
                if grid[(x, y)] == symbol:
                    neighbor = [x, y]
                    neighbor[idx] = (neighbor[idx] + 1) % mod 
                    neighbor = tuple(neighbor)
                    if grid[neighbor] == '.':
                        new_grid[neighbor] = symbol
                        new_grid[(x, y)] = '.'
                        change = True
        
        return new_grid, change                 
      
    change1 = change2 = True                        
    while change1 or change2:
        grid, change1 = move(grid, right=True)
        grid, change2 = move(grid, right=False)
        result += 1
    return result


s = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>
"""
s2 = """
"""

print("PART 1")
print("Example Solution:", solve1(s))

# print("Example 2 Solution:", solve1(s2))
print("Actual Solution:", solve1(inp))

