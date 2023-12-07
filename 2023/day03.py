from utils import *

inp = get_data(year=2023, day=3)

def solve1(d):
    grid = Grid(lmap(list, d.splitlines()))
    nums = positive_ints(d)
    indices = flatten([[idx] * len(str(num)) for idx, num in enumerate(nums)])
    valid_indices = set()
    
    for idx, coord in zip(indices, grid.findall_regex(r"\d")):
        if any(map(lambda x: x not in '.0123456789', grid.get_neighbors(coord, OCT_DELTA))):
            valid_indices.add(idx)
    
    return sum([nums[idx] for idx in valid_indices])

def solve2(d):
    grid = Grid(lmap(list, d.splitlines()))
    nums = positive_ints(d)
    indices = flatten([[idx] * len(str(num)) for idx, num in enumerate(nums)])
    gears = defaultdict(set)
    
    for idx, coord in zip(indices, grid.findall_regex(r"\d")):
        for gear_coord in filter(lambda x: grid[x] == '*', grid.get_neighbors_coords(coord, OCT_DELTA)):
            gears[gear_coord] |= {idx}
    
    return sum([product([nums[idx] for idx in indices]) for indices in gears.values() if len(nums) > 1])


s = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".strip()
s2 = """

""".strip()

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