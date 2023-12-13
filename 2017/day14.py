from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def knot_hash(d):
    nums = lrange(256)
    lengths = lmap(ord, d.strip()) + [17, 31, 73, 47, 23]
    curr = skip = 0
    
    for l in lengths * 64:
        indices = [i % len(nums) for i in range(curr, curr+l)]
        new_nums = nums.copy()
        for old, new in zip(indices, reversed(indices)):
            new_nums[old] = nums[new]
        nums = new_nums
        curr += l + skip
        skip += 1
    
    return ''.join(map(lambda s: f"{reduce(operator.xor, s, 0):08b}", every_n(nums, 16)))

def solve1(d):
    return sum(Counter(knot_hash(f'{d}-{idx}'))['1'] for idx in range(128))


def solve2(d):
    grid = Grid([list(knot_hash(f'{d}-{idx}')) for idx in range(128)])
    result = 0
    
    while (c := grid.find('1')):
        result += 1
        grid[c] = '0'
        check = {*grid.get_neighbors(c, GRID_DELTA)}
        while check:
            curr = check.pop()
            if grid[curr] == '1':
                grid[curr] = '0'
                check |= {*grid.get_neighbors(curr, GRID_DELTA)}

    return result


s = """
flqrgnkx
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