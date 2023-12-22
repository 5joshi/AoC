from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    lines = lmap(ints, d.splitlines())
    bricks = []
    taken = set()
    UP = (0, 0, 1)
    DOWN = (0, 0, -1)
    
    for line in lines:
        frm, to = every_n(line, 3)
        bricks.append((frm, to))

    idx = 0
    for frm, to in sorted(bricks, key=lambda x: x[0][2]):
        diff = lsub(to, frm)
        print(frm, to)

        delta = tuple(c // max(map(abs, diff + [1])) for c in diff)
        brick_coords = {frm, to}
        while frm != to:
            frm = tadd(frm, delta)
            brick_coords.add(frm)
            
        while all(tadd(brick, DOWN) not in taken for brick in brick_coords) and all(tadd(brick, DOWN)[2] >= 1 for brick in brick_coords):
            brick_coords = {tadd(brick, DOWN) for brick in brick_coords}
        # print(frm, to, brick_coords, taken, [tadd(brick, DOWN) not in taken for brick in brick_coords])
        bricks[idx] = (brick_coords)
        # print(bricks[idx])
        taken |= brick_coords  
        idx += 1

    result = 0
    supports = defaultdict(set)
    supported_by = defaultdict(set)
    for i, brick in enumerate(bricks):
        under = {tadd(b, DOWN) for b in brick}
        above = {tadd(b, UP) for b in brick}
        dep = 0
        indep = 0
        for j, other in enumerate(bricks):
            if brick == other: continue
            if len(under & other) >= 1:
                supported_by[i].add(j)
            if len(above & other) >= 1:
                supports[i].add(j)
    
    for i in range(len(bricks)):
        print(i, supports[i], supported_by[i])

        if len(supports[i]) == 0 or all(len(supported_by[j]) > 1 for j in supports[i]):

            result += 1
    return result

def solve2(d):
    lines = lmap(ints, d.splitlines())
    bricks = []
    taken = set()
    UP = (0, 0, 1)
    DOWN = (0, 0, -1)
    
    for line in lines:
        frm, to = every_n(line, 3)
        bricks.append((frm, to))

    idx = 0
    for frm, to in sorted(bricks, key=lambda x: x[0][2]):
        diff = lsub(to, frm)
        print(frm, to)

        delta = tuple(c // max(map(abs, diff + [1])) for c in diff)
        brick_coords = {frm, to}
        while frm != to:
            frm = tadd(frm, delta)
            brick_coords.add(frm)
            
        while all(tadd(brick, DOWN) not in taken for brick in brick_coords) and all(tadd(brick, DOWN)[2] >= 1 for brick in brick_coords):
            brick_coords = {tadd(brick, DOWN) for brick in brick_coords}
        # print(frm, to, brick_coords, taken, [tadd(brick, DOWN) not in taken for brick in brick_coords])
        bricks[idx] = (brick_coords)
        # print(bricks[idx])
        taken |= brick_coords  
        idx += 1

    result = 0
    supports = defaultdict(set)
    supported_by = defaultdict(set)
    for i, brick in enumerate(bricks):
        under = {tadd(b, DOWN) for b in brick}
        above = {tadd(b, UP) for b in brick}
        for j, other in enumerate(bricks):
            if brick == other: continue
            if len(under & other) >= 1:
                supported_by[i].add(j)
            if len(above & other) >= 1:
                supports[i].add(j)
    
    for i in range(len(bricks)):
        if not (len(supports[i]) == 0 or all(len(supported_by[j]) > 1 for j in supports[i])):
            supporting = set(j for j in supports[i] if len(supported_by[j]) == 1)
            to_check = set()
            for j in supporting:
                to_check |= supports[j]
            while to_check:
                j = to_check.pop()
                if all(k in supporting for k in supported_by[j]):
                    supporting.add(j)
                to_check |= supports[j]
            print(i, supporting)
            result += len(supporting)
    return result



s = """
1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
""".strip()
s2 = """
1,1,1~1,1,1
1,1,2~1,1,2
1,2,1~1,2,2
1,1,3~1,2,3
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