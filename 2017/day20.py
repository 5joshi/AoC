from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    lines = d.splitlines()
    
    def dist(idx, t=50_000_000):
        p, v, a = every_n(ints(lines[idx]), 3)
        return pdist1(tadd(tadd(p, tmul(v, t)), tmul(a, t ** 2)))
    
    return min(range(len(lines)), key=dist)

def solve2(d):
    lines = d.splitlines()
    particles = {}
    positions = {}
        
    for idx, line in enumerate(lines):
        p, v, a = every_n(ints(line), 3)
        particles[idx] = (p, v, a)
        positions[p] = idx
    
    for _ in range(100):
        for particle, (p, v, a) in particles.items():
            v = tadd(v, a)
            p = tadd(p, v)
            particles[particle] = (p, v, a)
               
        counts = Counter(p for p, v, a in particles.values())
        positions = {p: idx for idx, (p, v, a) in particles.items() if counts[p] == 1}
        particles = {idx: (p, v, a) for idx, (p, v, a) in particles.items() if counts[p] == 1}
            
    return len(particles.keys())


s = """
p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>
""".strip()
s2 = """
p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>
p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>
p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>
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