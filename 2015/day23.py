from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    lines = lmap(words_and_ints, d.splitlines())
    variables = defaultdict(int)
    idx = 0
    
    while 0 <= idx < len(lines):
        line = lines[idx]
        if line[0] == 'hlf': variables[line[1]] //= 2
        elif line[0] == 'tpl': variables[line[1]] *= 3
        elif line[0] == 'inc': variables[line[1]] += 1
        elif line[0] == 'jmp': idx += line[1] - 1
        elif line[0] == 'jie' and variables[line[1]] % 2 == 0: idx += line[2] - 1
        elif line[0] == 'jio' and variables[line[1]] == 1: idx += line[2] - 1
        idx += 1

    return variables['b']

def solve2(d):
    lines = lmap(words_and_ints, d.splitlines())
    variables = defaultdict(int, {'a': 1})
    idx = 0
    
    while 0 <= idx < len(lines):
        line = lines[idx]
        if line[0] == 'hlf': variables[line[1]] //= 2
        elif line[0] == 'tpl': variables[line[1]] *= 3
        elif line[0] == 'inc': variables[line[1]] += 1
        elif line[0] == 'jmp': idx += line[1] - 1
        elif line[0] == 'jie' and variables[line[1]] % 2 == 0: idx += line[2] - 1
        elif line[0] == 'jio' and variables[line[1]] == 1: idx += line[2] - 1
        idx += 1

    return variables['b']


s = """
inc a
jio a, +2
tpl a
inc a
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