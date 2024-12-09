from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    disk = list(((idx // 2 if idx % 2 == 0 else None), int(n)) for idx, n in enumerate(d)) 
    while any(val is None for val, _ in disk[:-1]):
        val, n = disk.pop()
        if val is None: continue
        while n > 0:
            idx, space = next(((idx, n) for idx, (val, n) in enumerate(disk) if val is None), (None, n))
            if idx is None:
                disk.append((val, n))
            elif n >= space:
                disk[idx] = (val, space)
            else:
                disk[idx] = (val, n)
                disk.insert(idx + 1, (None, space - n))
            n -= space
    return list(it.accumulate(disk, lambda x, y: (x[0] + (sum(range(x[1], x[1] + y[1])) * y[0] if y[0] else 0), x[1] + y[1]), initial=(0, 0)))[-1][0]
        
def solve2(d):
    disk = list(((idx // 2 if idx % 2 == 0 else None), int(n)) for idx, n in enumerate(d)) 
    end = list()
    while any(val is None for val, _ in disk[:-1]):
        val, n = disk.pop()
        idx, space = next(((idx, m) for idx, (val, m) in enumerate(disk) if val is None and m >= n), (None, None))
        end.insert(0, (None if idx else val, n))
        if val and idx:
            disk[idx] = (val, n)
            if n != space: disk.insert(idx + 1, (None, space - n))
    return list(it.accumulate(disk + end, lambda x, y: (x[0] + (sum(range(x[1], x[1] + y[1])) * y[0] if y[0] else 0), x[1] + y[1]), initial=(0, 0)))[-1][0]


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