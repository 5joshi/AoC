from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    regs, steps = d.split("\n\n")
    regs = dict(lmap(lambda x: (x.split()[1][:-1], ints(x)[0]), regs.splitlines()))
    steps = ints(steps)
    idx = 0
    result = list()
    
    while 0 <= idx < len(steps) - 1:
        op, val = steps[idx], steps[idx + 1]
        combo = regs[k] if (k := chr(val - 4 + ord('A'))) in regs else val
        if op == 0:
            regs['A'] = regs['A'] // (2 ** combo)
        elif op == 1:
            regs['B'] ^= val
        elif op == 2:
            regs['B'] = combo % 8
        elif op == 3:
            if regs['A'] != 0 and idx != val:
                idx = val 
                continue
        elif op == 4:
            regs['B'] ^= regs['C']
        elif op == 5:
            result.append(combo % 8)
        elif op == 6:
            regs['B'] = regs['A'] // (2 ** combo)
        elif op == 7:
            regs['C'] = regs['A'] // (2 ** combo)
        idx += 2
    return ",".join(lmap(str, result))
    


def solve2(d):
    target = ints(d)[3:]
    def solve(a):
        result = []
        while a != 0:
            result.append((((a % 8) ^ 3) ^ a >> ((a % 8) ^ 5)) % 8)
            a //= 8
        return result
    
    curr = [0]
    for idx in range(1, len(target) + 1):
        curr = [i * 8 + j for i in curr for j in range(8) if solve(i * 8 + j) == target[-idx:]]
    return curr[0]

s = """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0


""".strip()
s2 = """
Register A: 33024962
Register B: 0
Register C: 0

Program: 2,4,1,3,7,5,1,5,0,3,4,2,5,5,3,0
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