from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d, start=(0,-1), start_dir=CHAR_TO_DELTA['R']):
    grid = Grid(lmap(list, d.splitlines()))
    seen = set()
    
    to_check = deque([(start, start_dir)])
    while to_check:
        coord, direction = to_check.popleft()
        if (coord, direction) in seen: continue
        seen.add((coord, direction))
        # print(to_check)
        nxt_c = tadd(coord, direction)
        # print(nxt, nxt_c, "\n", grid)
        if nxt_c not in grid: continue
        nxt = grid[nxt_c]

        if nxt == '|' and direction in (CHAR_TO_DELTA['E'], CHAR_TO_DELTA['W']):
            to_check.append((nxt_c, CHAR_TO_DELTA['N']))
            to_check.append((nxt_c, CHAR_TO_DELTA['S']))
        elif nxt == '-' and direction in (CHAR_TO_DELTA['N'], CHAR_TO_DELTA['S']):
            to_check.append((nxt_c, CHAR_TO_DELTA['E']))
            to_check.append((nxt_c, CHAR_TO_DELTA['W']))
        elif nxt == '/' and direction in (CHAR_TO_DELTA['L'], CHAR_TO_DELTA['R']):
            to_check.append((nxt_c, turn_left(direction)))
        elif nxt == '/':
            to_check.append((nxt_c, turn_right(direction)))
        elif nxt == '\\' and direction in (CHAR_TO_DELTA['L'], CHAR_TO_DELTA['R']):
            to_check.append((nxt_c, turn_right(direction)))
        elif nxt == '\\':
            to_check.append((nxt_c, turn_left(direction)))
        else:
            to_check.append((nxt_c, direction))
    
    # for c in {c for c, d in seen}:
    #     # print(c)
    #     grid[c] = '#'    
    # print(grid)
    return len({c for c, d in seen}) - 1
    # return len(grid.findall('#')) - 1

def solve2(d):
    grid = Grid(lmap(list, d.splitlines()))
    result = 0
    for c in range(grid.ncols):
        result = max(result, solve1(d, start=(-1, c), start_dir=CHAR_TO_DELTA['S']))
    for c in range(grid.ncols):
        result = max(result, solve1(d, start=(grid.nrows, c), start_dir=CHAR_TO_DELTA['N']))
    for c in range(grid.nrows):
        result = max(result, solve1(d, start=(c, -1), start_dir=CHAR_TO_DELTA['E']))
    for c in range(grid.nrows):
        result = max(result, solve1(d, start=(c, grid.ncols), start_dir=CHAR_TO_DELTA['W']))
    return result
    


s = """
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....

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