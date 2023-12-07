from utils import *

inp = get_data(year=2021, day=17)


def solve1(d):
    _, _, ymin, ymax = ints(d)

    def simulate(dy):
        max_height = y = 0
        
        while True:
            y += dy
            dy -= 1
            max_height = max(max_height, y)
            if ymin <= y <= ymax:
                return max_height 
            elif y < ymin:
                return 0      
            
    dy_max = max(abs(ymin), abs(ymax))             
    for dy in range(dy_max, 0, -1):
        if height := simulate(dy): 
            return height

def solve2(d):
    xmin, xmax, ymin, ymax = ints(d)
    
    result = 0

    def simulate(dx, dy):
        max_height = x = y = 0
        while True:
            (x, y) = (x + dx, y + dy)
            (dx, dy) = (dx - signum(dx), dy - 1)
            max_height = max(max_height, y)
            if xmin <= x <= xmax and ymin <= y <= ymax:
                return True
            elif y < ymin or x > xmax or (x < xmin and dx == 0):
                return False
    
    sign = signum(xmax)
    dx_max = xmax
    dx_min = min([x for x in range(xmax // 2) if xmin <= gauss_sum(abs(x)) * sign <= xmax])    
    dy_max = max(abs(ymin), abs(ymax))    
    dy_min = -dy_max   
    for x in range(dx_min, dx_max + sign, sign):
        for y in range(dy_min, dy_max+1):
            result += int(simulate(x, y))
    
    return result


s = """target area: x=20..30, y=-10..-5
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
