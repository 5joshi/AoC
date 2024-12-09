from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def fixed(l):
    for idx, x in enumerate(l):
        if x is None:
            return all(t is None for t in l[idx:])
    return True

def solve1(d):
    disk = list()
    result = 0
    i = 0
    for a, b in every_n(d + "0", 2):
        a, b = int(a), int(b)
        disk += [i] * a
        disk += [None] * b
        i += 1
    # print(disk)
    while not fixed(disk):
        # take the last element that is not none
        i = disk.pop()
        if i is not None:
            idx = disk.index(None)
            disk[idx] = i
    
    for idx, elem in enumerate(disk):
        if elem is not None:
            result += idx * elem
    
    return result

def solve2(d):
    disk = list()
    ends = list()
    result = 0
    i = 0
    for a, b in every_n(d + "0", 2):
        a, b = int(a), int(b)
        disk.append((i, a))
        disk.append((None, b))
        i += 1

    while disk:
        # take the last element that is not none
        val, i = disk.pop()
        if val is not None:
            found = False
            for idx, (v, j) in enumerate(disk):
                if v is None and j >= i:
                    disk[idx] = (val, i)
                    disk.insert(idx+1, (None, j - i))
                    found = True
                    break
            if not found:
                ends.insert(0, (val, i))
            if found: 
                ends.insert(0, (None, i))
        else:
            ends.insert(0, (val, i))
        # print(disk + ends)
    
    disk = disk + ends
    tmp = list()
    for val, i in disk:
        tmp += [val] * i
    for idx, elem in enumerate(tmp):
        if elem is not None:
            result += idx * elem
    
    # print(tmp)
    return result


s = """
2333133121414131402
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