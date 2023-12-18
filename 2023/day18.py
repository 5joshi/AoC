from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    lines = lmap(alphanumerics, d.splitlines())
    area = border = 0
    curr = (0, 0)
    
    for direction, length, _ in lines:        
        x1, y1 = curr
        x2, y2 = tadd(curr, tmul(CTD[direction], int(length)))
        
        area += (y1 + y2) * (x1 - x2)
        border += int(length) 
        curr = (x2, y2)
    
    inside = (abs(area) - border) // 2 + 1
    return border + inside

def solve2(d):
    lines = lmap(alphanumerics, d.splitlines())
    area = border = 0
    curr = (0, 0)
    
    for _, _, color in lines:
        length = int(color[:-1], 16)
        direction = "RDLU"[int(color[-1])]
        
        x1, y1 = curr
        x2, y2 = tadd(curr, tmul(CTD[direction], length))
        
        area += (y1 + y2) * (x1 - x2)
        border += length 
        curr = (x2, y2)
    
    inside = (abs(area) - border) // 2 + 1
    return border + inside


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