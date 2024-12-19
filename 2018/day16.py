from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def addr(curr, a, b, r): return [c if i != r else curr[a] + curr[b] for i, c in enumerate(curr)] 
def addi(curr, a, b, r): return [c if i != r else curr[a] + b for i, c in enumerate(curr)]
def mulr(curr, a, b, r): return [c if i != r else curr[a] * curr[b] for i, c in enumerate(curr)]
def muli(curr, a, b, r): return [c if i != r else curr[a] * b for i, c in enumerate(curr)]
def banr(curr, a, b, r): return [c if i != r else curr[a] & curr[b] for i, c in enumerate(curr)]
def bani(curr, a, b, r): return [c if i != r else curr[a] & b for i, c in enumerate(curr)]
def borr(curr, a, b, r): return [c if i != r else curr[a] | curr[b] for i, c in enumerate(curr)]
def bori(curr, a, b, r): return [c if i != r else curr[a] | b for i, c in enumerate(curr)]
def setr(curr, a, b, r): return [c if i != r else curr[a] for i, c in enumerate(curr)]
def seti(curr, a, b, r): return [c if i != r else a for i, c in enumerate(curr)]
def gtir(curr, a, b, r): return [c if i != r else int(a > curr[b]) for i, c in enumerate(curr)]
def gtri(curr, a, b, r): return [c if i != r else int(curr[a] > b) for i, c in enumerate(curr)]
def gtrr(curr, a, b, r): return [c if i != r else int(curr[a] > curr[b]) for i, c in enumerate(curr)]
def eqir(curr, a, b, r): return [c if i != r else int(a == curr[b]) for i, c in enumerate(curr)]
def eqri(curr, a, b, r): return [c if i != r else int(curr[a] == b) for i, c in enumerate(curr)]
def eqrr(curr, a, b, r): return [c if i != r else int(curr[a] == curr[b]) for i, c in enumerate(curr)]
FUNCS = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

def solve1(d):
    blocks, _ = d.split("\n\n\n\n")
    result = 0
    
    for block in blocks.split("\n\n"):
        curr, (op, a, b, r), nxt = lmap(ints, block.splitlines())
        result += sum(func(curr, a, b, r) == nxt for func in FUNCS) >= 3
    
    return result

def solve2(d):
    blocks, program = d.split("\n\n\n\n")
    opcodes = {i: set(FUNCS) for i in range(16)}
    regs = [0, 0, 0, 0]
        
    for block in blocks.split("\n\n"):
        curr, (op, a, b, r), nxt = lmap(ints, block.splitlines())
        opcodes[op] = {func for func in opcodes[op] if func(curr, a, b, r) == nxt}
        if len(opcodes[op]) == 1:
            for i in {*range(16)} - {op}:
                opcodes[i] -= opcodes[op]
        
    opcodes = {k: v.pop() for k, v in opcodes.items()}    
    for (op, *args) in lmap(ints, program.splitlines()):
        regs = opcodes[op](regs, *args)
    
    return regs[0]


s = """
Before: [3, 2, 1, 1]
9 2 1 2
After:  [3, 2, 2, 1]



1 2 3 4
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