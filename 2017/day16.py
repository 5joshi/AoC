from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    moves = d.split(',')
    programs = lrange(16)
    for move in moves:
        if move[0] == 's':
            i = ints(move)[0]
            programs = programs[-i:] + programs[:-i]
        else:
            i, j = map(lambda c: programs.index(ord(c) - ord('a')), move[1:].split('/')) if move[0] == 'p' else ints(move)
            programs[i], programs[j] = programs[j], programs[i]

    
    return ''.join(map(lambda i: chr(i + ord('a')), programs))

def solve2(d):
    moves = d.split(',')
    programs = lrange(16)
    cycle = [tuple(programs)]
    seen = set()
    seen.add(tuple(programs))
    
    for i in range(1_000_000_000):
        for move in moves:
            if move[0] == 's':
                i = ints(move)[0]
                programs = programs[-i:] + programs[:-i]
            else:
                i, j = map(lambda c: programs.index(ord(c) - ord('a')), move[1:].split('/')) if move[0] == 'p' else ints(move)
                programs[i], programs[j] = programs[j], programs[i]
                
        if tuple(programs) in seen: break
        
        seen.add(tuple(programs))
        cycle.append(tuple(programs))
    
    return ''.join(map(lambda i: chr(i + ord('a')), cycle[1_000_000_000 % len(cycle)]))


s = """
s1,x3/4,pe/b
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