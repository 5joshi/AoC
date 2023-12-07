from utils import *

inp = get_data(year=2021, day=25)
        
        
def solve1(d):
    lines = d.splitlines()
    result = 0
    right = set()
    down = set()
    
    for x, line in enumerate(lines):
        for y, cell in enumerate(line):
            if cell == '>': 
                right.add((x, y))
            elif cell == 'v':
                down.add((x, y))
            
    height = max(right | down, key=fst)[0]
    width = max(right | down, key=snd)[1]
    
    def move(coords, east=True):
        nonlocal right, down
        
        change = False
        if east: 
            mod = width + 1
            idx = 1
        else: 
            mod = height + 1
            idx = 0
            
        new_coords = set()
        for coord in coords:
            neighbor = list(coord)
            neighbor[idx] = (neighbor[idx] + 1) % mod 
            neighbor = tuple(neighbor)
            if neighbor not in right | down:
                new_coords.add(neighbor)
                change = True
            else:
                new_coords.add(coord)
        
        return new_coords, change                 
      
    change1 = change2 = True     
    while change1 or change2:
        right, change1 = move(right, east=True)
        down, change2 = move(down, east=False)
        result += 1
    return result

def solve2(): 
    return 0

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

