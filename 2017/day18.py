from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    lines = lmap(words_and_ints, d.splitlines())
    registers = defaultdict(int)
    result = idx = 0
    
    while result == 0:
        instr, *args = lines[idx]
        vals = [registers.get(arg, arg) for arg in args]
        if instr == 'snd':
            registers['snd'] = vals[0]
        elif instr == 'set':
            registers[args[0]] = vals[1]
        elif instr == 'add':
            registers[args[0]] += vals[1]
        elif instr == 'mul':
            registers[args[0]] *= vals[1]
        elif instr == 'mod':
            registers[args[0]] %= vals[1]
        elif instr == 'rcv':
            result = registers['snd'] if vals[0] != 0 else 0
        elif instr == 'jgz':
            idx += vals[1] - 1 if vals[0] > 0 else 0
        idx += 1
    
    return result

def solve2(d):
    lines = lmap(words_and_ints, d.splitlines())
    regs1 = defaultdict(int)
    regs2 = defaultdict(int, {'p': 1})
    result1 = idx1 = 0
    result2 = idx2 = 0
        
    def step(lines, idx, registers, received, sent, result):  
        instr, *args = lines[idx]
        vals = [registers.get(arg, arg) for arg in args]
        if instr == 'snd':
            result += 1
            sent.append(vals[0])
        elif instr == 'set':
            registers[args[0]] = vals[1]
        elif instr == 'add':
            registers[args[0]] += vals[1]
        elif instr == 'mul':
            registers[args[0]] *= vals[1]
        elif instr == 'mod':
            registers[args[0]] %= vals[1]
        elif instr == 'rcv':
            if len(received) > 0: registers[args[0]] = received.pop(0)
            else: return result, idx, True
        elif instr == 'jgz':
            idx += vals[1] - 1 if vals[0] > 0 else 0
        return result, idx + 1, False
        
    sent1 = []
    sent2 = []
    while True:
        result1, idx1, stuck1 = step(lines, idx1, regs1, received=sent2, sent=sent1, result=result1)
        result2, idx2, stuck2 = step(lines, idx2, regs2, received=sent1, sent=sent2, result=result2)
        if stuck1 and stuck2: break
    
    return result2


s = """
snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d

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