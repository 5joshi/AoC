from utils import *

inp = """Time:        40     92     97     90
Distance:   215   1064   1505   1100
"""

def hold_time(time, dist):
    for hold in range(time):
        remaining = time - hold
        if hold * remaining > dist:
            return hold

def solve1(d):
    return product([time - 2 * hold_time(time, dist) + 1 for time, dist in zip(*map(ints, d.splitlines()))])

def solve2(d):
    time, dist = lmap(lambda line: int("".join(line[1:])), map(alphanumerics, d.splitlines()))
    return time - 2 * hold_time(time, dist) + 1



s = """Time:      7  15   30
Distance:  9  40  200
"""
s2 = """
"""

print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve1(s2))
if inp != "\n":
    print("Actual Solution:", solve1(inp))

print("PART 2")
print("Example Solution:", solve2(s))
# print("Example 2 Solution:", solve2(s2))
if inp != "\n":
    print("Actual Solution:", solve2(inp))
