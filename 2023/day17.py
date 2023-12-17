from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d, minlen=1, maxlen=3):
    grid = s_to_grid(d).map(int)
    goal = lambda node: node[0] == (grid.nrows - 1, grid.ncols - 1)

    def expand(node):
        (x, y), axis = node
        
        result = []
        upcost = downcost = leftcost = rightcost = 0
        for c in range(1, maxlen + 1):
            if axis == 'horizontal' or axis == 'both':
                if (upc := (x, y - c)) in grid: 
                    upcost += grid[upc]
                    if c >= minlen: result += [(upcost, (upc, 'vertical'))]
                if (downc := (x, y + c)) in grid:
                    downcost += grid[downc]
                    if c >= minlen: result += [(downcost, (downc, 'vertical'))]
            if axis == 'vertical' or axis == 'both':
                if (leftc := (x - c, y)) in grid:
                    leftcost += grid[leftc]
                    if c >= minlen: result += [(leftcost, (leftc, 'horizontal'))]
                if (rightc := (x + c, y)) in grid:
                    rightcost += grid[rightc]
                    if c >= minlen: result += [(rightcost, (rightc, 'horizontal'))]
        return result

    def heuristic(node):
        return dist1(node[0], (grid.nrows - 1, grid.ncols - 1))
    
    return a_star(((0, 0), 'both'), to_func=goal, expand=expand, heuristic=heuristic)[0]
    
def solve2(d):
    return solve1(d, minlen=4, maxlen=10)


s = """
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533


""".strip()
s2 = """
111111111111
999999999991
999999999991
999999999991
999999999991


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