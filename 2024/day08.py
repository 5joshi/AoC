from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    grid = s_to_grid(d)
    values = set(flatten(grid.grid)) - {'.'}
    mappings = {value: grid.findall(value) for value in values}
    result = 0
    
    for coord in grid.coords():
        found = False
        for value, coords in mappings.items():
            for a, b in it.permutations(coords, 2):
                if dist1(coord, a) == (2 * dist1(coord, b)) and tsub(b, a) == tsub(coord, b):
                    result += 1
                    found = True
                    break
            if found: break
    
    print(grid)
    return result

def solve2(d):
    grid = s_to_grid(d)
    values = set(flatten(grid.grid)) - {'.'}
    mappings = {value: grid.findall(value) for value in values}
    result = 0
    found = set()
    

    for value, coords in mappings.items():
        for a, b in it.permutations(coords, 2):
            delta = tsub(b, a)
            found |= {tadd(a, tmul(delta, c)) for c in range(-100, 100)}
    
    found = {point for point in found if point in grid}
    for point in found:
        grid[point] = '#'
    print(grid)
    return len(found)


s = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............

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