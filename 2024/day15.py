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
        if np not in grid: continue
        if grid[np] == "#": continue
        if grid[np] == "O":
            nxt = tadd(np, d)
            while nxt in grid and grid[nxt] == "O":
                nxt = tadd(nxt, d)
            if nxt in grid and grid[nxt] == ".":
                grid[nxt] = "O"
                grid[np] = "@"
                grid[robot] = "."
                robot = np
        else:
            grid[np] = "@"
            grid[robot] = "."
            robot = np

        # print(grid)  
    
    result = 0
    for x, y in grid.findall("O"):
        result += y + 100 * x
    return result

def solve2(d):
    grid, dirs = d.split("\n\n")
    grid = grid.replace(".", "..").replace("#", "##").replace("O", "[]").replace("@", "@.")
    grid = s_to_grid(grid)
    dirs = lmap(lambda d: CTD[d], flatten(dirs.splitlines()))
    robot = grid.find("@")
    # print(grid)
    for d in dirs:
        np = tadd(robot, d)
        if np not in grid: continue
        if grid[np] == "#": continue
        if grid[np] in "[]":
            if d in [CTD['L'], CTD['R']]:
                nxt = tadd(np, d)
                while nxt in grid and grid[nxt] in '[]':
                    nxt = tadd(nxt, d)
                if nxt in grid and grid[nxt] == ".":
                    while nxt != robot:
                        grid[nxt] = grid[tsub(nxt, d)]
                        nxt = tsub(nxt, d)
                    grid[robot] = "."
                    robot = np
            else:
                boxes = set()
                curr_check = {np}
                if grid[np] == "]":
                    curr_check.add(tadd(np, CTD['L']))
                else:
                    curr_check.add(tadd(np, CTD['R']))
                
                pushable = True
                while pushable and curr_check:
                    nxt_check = set()
                    # print(curr_check    )
                    for c in curr_check:
                        nxt = tadd(c, d)
                        if nxt in grid and grid[nxt] == "#":
                            pushable = False
                        elif nxt in grid and grid[nxt] in "[]":
                            nxt_check.add(nxt)
                            if grid[nxt] == "]":
                                nxt_check.add(tadd(nxt, CTD['L']))
                            else:
                                nxt_check.add(tadd(nxt, CTD['R']))
                    boxes |= curr_check
                    curr_check = nxt_check
                # print(boxes)
                if pushable:
                    vals = {c: grid[c] for c in boxes}
                    for c in boxes:
                        grid[c] = "."
                    for c in boxes:
                        grid[tadd(c, d)] = vals[c]
                    grid[np] = "@"
                    grid[robot] = "."
                    robot = np
                
            
        else:
            grid[np] = "@"
            grid[robot] = "."
            robot = np
    # print(grid)
    
    result = 0
    for x, y in grid.findall("["):
        result += y  + 100 * x
    return result


s = """
#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^

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