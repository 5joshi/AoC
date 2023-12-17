from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d, eggs=7):
    lines = lmap(words_and_ints, d.splitlines())
    registers = {c: 0 for c in 'abcd'}
    registers['a'] = eggs
    idx = 0
    
    while 0 <= idx < len(lines):
        instr, *args = lines[idx]
        vals = [registers.get(arg, arg) for arg in args]
        if instr == 'cpy':
            if isinstance(args[1], int): continue
            registers[args[1]] = vals[0]
        elif instr == 'inc':
            registers[args[0]] += 1
        elif instr == 'dec':
            registers[args[0]] -= 1
        elif instr == 'jnz':
            idx += vals[1] - 1 if vals[0] != 0 else 0
        elif instr == 'tgl':
            if 0 <= idx + vals[0] < len(lines):
                if len(lines[idx + vals[0]]) == 2:
                    lines[idx + vals[0]][0] = 'dec' if lines[idx + vals[0]][0] == 'inc' else 'inc'
                else:
                    lines[idx + vals[0]][0] = 'cpy' if lines[idx + vals[0]][0] == 'jnz' else 'jnz'
        idx += 1
    
    return registers['a']

def solve2(d, eggs=12):
    const = product(ints(d)[-4:-2])
    return math.factorial(eggs) + const


s = """
cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a

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