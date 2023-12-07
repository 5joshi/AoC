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
