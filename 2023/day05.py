from utils import *

inp = get_data(year=2023, day=5)

def solve1(d):
    inp = d.split('\n\n')
    seeds = ints(inp[0])
    
    for conversion in inp[1:]:
        conversion = conversion.splitlines()
        new_seeds = seeds.copy()
        for line in conversion[1:]:
            source, destination, length = ints(line)
            for idx, seed in enumerate(seeds):
                if destination <= seed < destination + length:
                    new_seeds[idx] = source + seed - destination
        seeds = new_seeds
        
    return min(seeds)

def solve2(d):
    inp = d.split('\n\n')
    seeds = every_n(ints(inp[0]), 2)
    seeds = [(seed, seed+length) for (seed, length) in seeds]
    min_result = math.inf

    for min_seed, max_seed in seeds:
        seed_ranges = [(min_seed, max_seed)]
        for conversion in inp[1:]:
            conversion = conversion.splitlines()
            converted_ranges = []
            for line in conversion[1:]:
                source, destination, length = ints(line)
                min_dest, max_dest = (destination, destination + length)
                new_ranges = []
                while seed_ranges:
                    start, end = seed_ranges.pop()
                    left = (start, min(min_dest, end))
                    mid = (max(start, min_dest), min(max_dest, end))
                    right = (max(start, max_dest), end)
                    
                    if left[0] < left[1]:
                        new_ranges.append(left)
                    if mid[0] < mid[1]:
                        converted_ranges.append((mid[0] - min_dest + source, mid[1] - min_dest + source))
                    if right[0] < right[1]:
                        new_ranges.append(right)
                        
                seed_ranges = new_ranges
            seed_ranges = converted_ranges + seed_ranges
        min_result = min(min_result, min([x[0] for x in seed_ranges]))
                    
        
    return min_result


s = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
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
