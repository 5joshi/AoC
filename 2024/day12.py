from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    grid = s_to_grid(d)
    result = 0
    
    for coord in grid.coords():
        if grid[coord] == ".": continue
        same = {coord}
        todo = {coord}
        ref = grid[coord]
        grid[coord] = "."
        while todo:
            c = todo.pop()
            for nc, val in grid.get_neighbors_items(c, GRID_DELTA):
                if val == ref and nc not in same:
                    grid[nc] = "."
                    same.add(nc)
                    todo.add(nc)
        area = len(same)
        perimeter = 0
        for c in same:
            for nc, _ in grid.get_neighbors_items(c, GRID_DELTA, ""):
                if nc not in same:
                    perimeter += 1
        result += area * perimeter
        print(ref, area, perimeter)
        # print(grid)
    
    
    return result

def solve2(d):
    grid = s_to_grid(d)
    result = 0
    
    for coord in grid.coords():
        if grid[coord] == ".": continue
        same = {coord}
        todo = {coord}
        ref = grid[coord]
        grid[coord] = "."
        while todo:
            c = todo.pop()
            for nc, val in grid.get_neighbors_items(c, GRID_DELTA):
                if val == ref and nc not in same:
                    grid[nc] = "."
                    same.add(nc)
                    todo.add(nc)
        area = len(same)
        sides = set()
        for c in same:
            for nc, _ in grid.get_neighbors_items(c, GRID_DELTA, ""):
                if nc not in same:
                    sides.add((c, DELTA_TO_UDLR[tsub(nc, c)]))
        # print([d for c, d in sides if c == (1, 0)])
        dir_to_coords = {d: set() for d in "UDLR"}
        for c, d in sides:
            dir_to_coords[d].add(c)
            
        sides_count = 0

        # print(sides_count, dir_to_coords['U'])
        for x in set(x for x, _ in dir_to_coords['U']):
            tmp_ys = list_diff(sorted(list(y for x2, y in dir_to_coords['U'] if x2 == x)))
            sides_count += 1
            for d in tmp_ys:
                if d > 1: sides_count += 1
        # print(sides_count)

        for x in set(x for x, _ in dir_to_coords['D']):
            tmp_ys = list_diff(sorted(list(y for x2, y in dir_to_coords['D'] if x2 == x)))
            sides_count += 1
            for d in tmp_ys:
                if d > 1: sides_count += 1
        # print(sides_count)

        for y in set(y for _, y in dir_to_coords['L']):
            tmp_xs = list_diff(sorted(list(x for x, y2 in dir_to_coords['L'] if y2 == y)))
            sides_count += 1
            for d in tmp_xs:
                if d > 1: sides_count += 1
        # print(sides_count)

        for y in set(y for _, y in dir_to_coords['R']):
            tmp_xs = list_diff(sorted(list(x for x, y2 in dir_to_coords['R'] if y2 == y)))
            sides_count += 1
            for d in tmp_xs:
                if d > 1: sides_count += 1
        # print(ref, area, sides_count)
        result += area * sides_count
        # print(ref, area, perimeter)
        # print(grid)
    
    
    return result


s = """
EEEEE
EXXXX
EEEEE
EXXXX
EEEEE


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