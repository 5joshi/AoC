from utils import *

# inp = get_data(year=2022, day=14)


def solve1(d):
    inp = d.splitlines()
    stones = set()
    sand = (500, 0)
    result = 0
    
    for line in inp:
        coords = every_n(ints(line), 2)
        for frm, to in windows(coords, 2):      
            stones |= set(map(tuple, line_points(list(frm), list(to))))
            
    deepest = max(stones, key=lambda x: x[1])[1]
    
    while sand[1] < deepest:
        for delta in [(0, 1), (-1, 1), (1, 1)]:
            nxt = tadd(sand, delta)
            if nxt not in stones:
                sand = nxt
                break
        else:
            stones.add(sand)
            result += 1
            sand = (500, 0)
        
    return result

def solve2(d):
    inp = d.splitlines()
    stones = set()
    sand = (500, 0)
    result = 0
    
    for line in inp:
        coords = every_n(ints(line), 2)
        for frm, to in windows(coords, 2):      
            stones |= set(map(tuple, line_points(list(frm), list(to))))
            
    deepest = max(stones, key=lambda x: x[1])[1] + 2
    
    while True:
        for delta in [(0, 1), (-1, 1), (1, 1)]:
            nxt = tadd(sand, delta)
            if nxt not in stones and nxt[1] < deepest:
                sand = nxt
                break
        else:
            stones.add(sand)
            result += 1
            if sand == (500, 0): break
            else: sand = (500, 0)
        
    return result


s = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""
s2 = """
"""

print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve1(s2))
# print("Actual Solution:", solve1(inp))

print("PART 2")
print("Example Solution:", solve2(s))
# print("Example 2 Solution:", solve2(s2))
# print("Actual Solution:", solve2(inp))
