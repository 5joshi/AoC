from utils import *
import hashlib

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    start, goal = (0, 0), (3, 3)
    grid = points_to_grid([start, goal])
    todo = deque([(start, '')])
    
    while todo:
        coord, path = todo.popleft()
        h = hashlib.md5((d + path).encode()).hexdigest()[:4]
        for c, direction in zip(h, 'UDLR'):
            if c not in 'bcdef': continue
            nxt = tadd(coord, CHAR_TO_DELTA[direction])
            if nxt not in grid: continue
            if nxt == goal: return path + direction
            todo.append((nxt, path + direction))
    

def solve2(d):
    start, goal = (0, 0), (3, 3)
    grid = points_to_grid([start, goal])
    todo = deque([(start, '')])
    dists = set()
    
    while todo:
        coord, path = todo.popleft()
        h = hashlib.md5((d + path).encode()).hexdigest()[:4]
        for c, direction in zip(h, 'UDLR'):
            if c not in 'bcdef': continue
            nxt = tadd(coord, CHAR_TO_DELTA[direction])
            if nxt not in grid: continue
            if nxt == goal: dists.add(len(path + direction))
            else: todo.append((nxt, path + direction))
            
    return max(dists)


s = """
ihgpwlah
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