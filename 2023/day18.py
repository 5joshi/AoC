from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    lines = d.splitlines()
    curr = (0, 0)
    border_points = set()
    
    for line in lines:
        direction, length, color = line.split()
        
        for _ in range(int(length)):
            curr = tadd(curr, CTD[direction])
            border_points.add(curr)
    
    grid = points_to_grid(border_points)
    start = tadd(grid.find('#'), (1, 1))
    
    seen = set()
    q = deque((start,))
    while q:
        # print(q)
        node = q.popleft()
        if node in seen: continue
        seen.add(node)
        if node not in grid or grid[node] == '#': continue
        grid[node] = '#'
        for n in grid.get_neighbors(node, GRID_DELTA):
            q.append(n)
     
    print(start)
    # flood(start)   
    print(start)
    print(border_points)
    print(grid)
    
    # Write grid to file
    # with open('grid.txt', 'w') as file:
    #     file.write(str(grid))
    
    return grid.count('#')

def solve2(d):
    lines = d.splitlines()
    l = r = result =0 
    border = 0
    curr = (0, 0)
    
    for line in reversed(lines):
        direction, length, color = line.split()
        length = int(length)
        color = color[2:-1]
        length = int(color[:-1], 16)
        direction = ['R', 'D', 'L', 'U'][int(color[-1])]
        x1, y1 = curr
        x2, y2 = tadd(curr, tmul(CTD[direction], length))
        l += x1 * y2
        r += x2 * y1
        # result += dist1(curr, nxt)
        # result += (curr[0] * nxt[1]) - (nxt[0] * curr[1])
        border += length 
        curr = (x2, y2)
    
    
    interior = abs(r - l) // 2 - border // 2 + 1
    
    return border + interior


s = """
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)


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