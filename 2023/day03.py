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


s = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
s2 = """
"""

print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve1(s2))
print("Actual Solution:", solve1(inp))

print("PART 2")
print("Example Solution:", solve2(s))
# print("Example 2 Solution:", solve2(s2))
print("Actual Solution:", solve2(inp))
