from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    lines = lmap(ints, d.splitlines())
    result = 0
    
    for speed, duration, rest in lines:
        dist = ((2503 // (duration + rest) * duration) + min(duration, 2503 % (duration + rest))) * speed
        result = max(result, dist)
        
    
    return result

def solve2(d):
    lines = lmap(ints, d.splitlines())
    points = [0] * len(lines)
    
    for i in range(1, 2504):
        best = 0
        indices = []
        for idx, (speed, duration, rest) in enumerate(lines):
            dist = ((i // (duration + rest) * duration) + min(duration, i % (duration + rest))) * speed
            if dist > best:
                best = dist
                indices = [idx]
            elif dist == best:
                indices.append(idx)
        for idx in indices:
            points[idx] += 1
    
    return max(points)


s = """
Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
""".strip()
s2 = """

""".strip()

if __name__ == '__main__':
    one, two, e1, e2, ex1, ex2, r1, r2 = get_solution_booleans(sys.argv)
            
    if e1 or ex1 or r1: print("PART 1")
    if e1: print("Example Solution:", solve1(s))
    if ex1: print("Example 2 Solution:", solve1(s2))
    if r1: print("Actual Solution:", sol1 := solve1(inp))

    if e2 or ex2 or r2: print("PART 2")
    if e2: print("Example Solution:", solve2(s))
    if ex2: print("Example 2 Solution:", solve2(s2))
    if r2: print("Actual Solution:", sol2 := solve2(inp))
    
    if (one and r1) or (two and r2):
        go = input('Submit? [y/N] ')
        if go == 'y':
            if one and r1: submit(sol1, part=1, year=YEAR, day=DAY)
            if two and r2: submit(sol2, part=2, year=YEAR, day=DAY)