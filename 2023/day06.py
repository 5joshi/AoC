from utils import *

inp = """Time:        40     92     97     90
Distance:   215   1064   1505   1100
"""


def solve1(d):
    times, distances = lmap(ints, d.splitlines())
    result = 1
    
    for time, dist in zip(times, distances):
        left = 0
        right = 0
        for i in range(time):
            speed = i
            left = time - i
            if speed * left > dist:
                left = i
                break
        for i in range(time, 0, -1):
            speed = i
            right = time - i
            if speed * right > dist:
                right = i
                break
        print(left, right)
        result *= right - left + 1
    
    return result

def solve2(d):
    times, distances = lmap(ints, d.splitlines())
    times = [str(x) for x in times]
    distances = [str(x) for x in distances]
    time = int("".join(times))
    dist = int("".join(distances))
    result = 1
    
    left = 0
    right = 0
    for i in range(time):
        speed = i
        left = time - i
        if speed * left > dist:
            left = i
            break
    for i in range(time, 0, -1):
        speed = i
        right = time - i
        if speed * right > dist:
            right = i
            break
    print(left, right)
    result *= right - left + 1
    
    return result


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
