from utils import *
import hashlib

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    keys = 0
    for i in it.count(0):
        h = hashlib.md5((d + str(i)).encode()).hexdigest()
        match = re.search(r'(.)\1\1', h)
        if match:
            for j in range(i + 1, i + 1001):
                if re.search(match.group(1) * 5, hashlib.md5((d + str(j)).encode()).hexdigest()):
                    keys += 1
                    if keys == 64: return i

def new_hash(s):
    for _ in range(2017):
        s = hashlib.md5(s.encode()).hexdigest()
    return s

def solve2(d):
    keys = set()
    threes = {}
    fives = {}
    for i in it.count(0):
        h = new_hash(d + str(i))
        match = re.search(r'(.)\1\1', h)
        threes[i] = match.group(1) if match else None
        fives[i] = set(re.findall(r'(.)\1\1\1\1', h))
        if fives[i]:
            for j in range(max(0, i - 1000), i):
                if threes[j] and threes[j] in fives[i]:
                    keys.add(j)
                    if len(keys) == 64: return j


s = """
abc
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