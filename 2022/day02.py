from utils import *

inp = get_data(year=2022, day=2)


def solve1(d):
    inp = lmap(words, d.splitlines())
    result = 0

    for a, b in inp:
        a = ord(a) - ord("A")
        b = ord(b) - ord("X")
        result += b + 1
        result += (b == a) * 3
        result += (b == (a + 1) % 3) * 6
                
    return result

def solve2(d):
    inp = lmap(words, d.splitlines())
    result = 0

    for a, b in inp:
        a = ord(a) - ord("A")
        match b:
            case 'X': b = (a - 1) % 3
            case 'Y': b = a
            case 'Z': b = (a + 1) % 3
        result += b + 1
        result += (b == a) * 3
        result += (b == (a + 1) % 3) * 6
        
    return result


s = """A Y
B X
C Z
"""
s2 = """
"""

print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve1(s2))
print("Actual Solution:", solve1(inp))

print("PART 2")
print("Example Solution:", solve2(s))
# # print("Example 2 Solution:", solve2(s2))
print("Actual Solution:", solve2(inp))
