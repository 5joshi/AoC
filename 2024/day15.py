from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    grid, dirs = d.split("\n\n")
    grid = s_to_grid(grid)
    dirs = lmap(lambda d: CTD[d], flatten(dirs.splitlines()))
    robot = grid.find("@")
    
    for d in dirs:
        np = tadd(robot, d)
        if grid[np] == "#": continue
        if grid[np] == "O":
            nxt = tadd(np, d)
            while grid[nxt] == "O":
                nxt = tadd(nxt, d)
            if grid[nxt] == "#": continue
            grid[nxt] = "O"
                
        grid[np] = "@"
        grid[robot] = "."
        robot = np

    return sum(y + 100 * x for x, y in grid.findall("O"))

def solve2(d):
    grid, dirs = d.split("\n\n")
    grid = s_to_grid(multi_replace(grid, {".": "..", "#": "##", "O": "[]", "@": "@."}))
    dirs = lmap(lambda d: CTD[d], flatten(dirs.splitlines()))
    robot = grid.find("@")
    
    for d in dirs:
        np = tadd(robot, d)
        if grid[np] == "#": continue
        if grid[np] in "[]":
            boxes = {np}
            
            if d in [CTD['<'], CTD['>']]:   
                nxt = tadd(np, d)
                while grid[nxt] in "[]":
                    boxes |= {nxt}
                    nxt = tadd(nxt, d)
                if grid[nxt] == "#": continue
            else:
                curr_row = {np, tadd(np, CTD['<'] if grid[np] == "]" else CTD['>'])}
                pushable = True
                while pushable and curr_row:
                    nxt_row = set()
                    for c in curr_row:
                        nxt = tadd(c, d)
                        if nxt in grid and grid[nxt] == "#":
                            pushable = False
                        elif nxt in grid and grid[nxt] in "[]":
                            nxt_row |= {nxt, tadd(nxt, CTD['<'] if grid[nxt] == "]" else CTD['>'])}
                    boxes |= curr_row
                    curr_row = nxt_row      
                if not pushable: continue        
                 
            boxes = {c: grid[c] for c in boxes}
            for c in boxes.keys():
                grid[c] = "."  
            for c, v in boxes.items():
                grid[tadd(c, d)] = v  
                
        grid[np] = "@"
        grid[robot] = "."
        robot = np
        
    return sum(y + 100 * x for x, y in grid.findall("["))


s = """
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
""".strip()
s2 = """
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^

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