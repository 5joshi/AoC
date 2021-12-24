from utils import *

inp = get_data(year=2021, day=24)


def solve1(d):
    sections = lmap(lambda x: x.splitlines(), d.split("inp w\n")[1:])
    relevant = lmap(lambda x: (ints(x[4])[0], ints(x[14])[0]), sections)
    depends = dict()
    result = [] 
    z = []
    
    for idx, (x, y) in enumerate(relevant):
        if x >= 10:
            z.append((idx, y))
        elif x < 0:
            other, diff = z.pop()  
            depends[idx] = (other, x + diff)      
            depends[other] = (idx, -(x + diff))

    for num in range(14):
        other, diff = depends[num]
        if other > num:
            result.append(min(9, 9 + diff))
        else:
            result.append(result[other] + diff)

    return "".join([str(x) for x in result])


def solve2(d):
    sections = lmap(lambda x: x.splitlines(), d.split("inp w\n")[1:])
    relevant = lmap(lambda x: (ints(x[4])[0], ints(x[14])[0]), sections)
    depends = dict()
    result = [] 
    z = []
    
    for idx, (x, y) in enumerate(relevant):
        if x >= 10:
            z.append((idx, y))
        elif x < 0:
            other, diff = z.pop()  
            depends[idx] = (other, x + diff)      
            depends[other] = (idx, -(x + diff))

    for num in range(14):
        other, diff = depends[num]
        if other > num:
            result.append(max(1, 1 + diff))
        else:
            result.append(result[other] + diff)

    return "".join([str(x) for x in result])


s = """
"""
s2 = """
"""

print("PART 1")
# print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve1(s2))
print("Actual Solution:", solve1(inp))

print("PART 2")
# print("Example Solution:", solve2(s))
# print("Example 2 Solution:", solve2(s2))
print("Actual Solution:", solve2(inp))
