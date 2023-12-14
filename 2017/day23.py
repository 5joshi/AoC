from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    lines = lmap(words_and_ints, d.splitlines())
    registers = {c: 0 for c in 'abcdefgh'}
    result = idx = 0
    
    while idx < len(lines):
        instr, *args = lines[idx]
        vals = [registers.get(arg, arg) for arg in args]
        if instr == 'set':
            registers[args[0]] = vals[1]
        elif instr == 'sub':
            registers[args[0]] -= vals[1]
        elif instr == 'mul':
            registers[args[0]] *= vals[1]
            result += 1
        elif instr == 'jnz':
            idx += vals[1] - 1 if vals[0] != 0 else 0
        idx += 1
    
    return result

def step(d, n):
    lines = lmap(words_and_ints, d.splitlines())
    registers = {c: 0 for c in 'abcdefgh'}
    registers['a'] = 1
    result = idx = 0
    
    for _ in range(n):
        instr, *args = lines[idx]
        vals = [registers.get(arg, arg) for arg in args]
        if instr == 'set':
            registers[args[0]] = vals[1]
        elif instr == 'sub':
            registers[args[0]] -= vals[1]
        elif instr == 'mul':
            registers[args[0]] *= vals[1]
            result += 1
        elif instr == 'jnz':
            idx += vals[1] - 1 if vals[0] != 0 else 0
        idx += 1
    
    return registers

def solve2(d):
    regs = step(d, 100)
    
    result = 0
    for x in range(regs['b'], regs['c'] + 1, 17):
        result += any(x % i == 0 for i in range(2, x))
    
    return result


s = """

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