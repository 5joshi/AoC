from utils import *

inp = get_data(year=2023)

def solve1(d):
    instr, dirs = d.split('\n\n')
    dirs = lmap(words, dirs.splitlines())
    m = dict()
    result = 0
    
    for frm, left, right in dirs:
        m[(frm, 'L')] = left
        m[(frm, 'R')] = right
    
    i = 0
    curr = 'AAA'
    while True:
        curr_i = instr[i % len(instr)]
        curr = m[(curr, curr_i)]
        if curr == 'ZZZ':
            break
        i += 1 
    
    return i + 1

def solve2(d):
    instr, dirs = d.split('\n\n')
    dirs = lmap(alphanumerics, dirs.splitlines())
    m = dict()
    
    

def solve2(d):
    instr, dirs = d.split('\n\n')
    dirs = lmap(alphanumerics, dirs.splitlines())
    m = dict()
    result = 0
    
    for frm, left, right in dirs:
        m[(frm, 'L')] = left
        m[(frm, 'R')] = right
    
    i = 0
    curr = []
    converges = []
    for key in m:
        # print(key)
        if key[0][2] == 'A':
            curr.append(key)
    while curr:
        new_curr = []
        curr_i = instr[i % len(instr)]
        
        for item in curr:
            if len(item) == 2: item = item[0]
            new = m[(item, curr_i)]
            new_curr.append((new, curr_i))
        bs = lmap(lambda x: x[0][2] == 'Z', new_curr)
        pop_indices = []
        for idx, b in enumerate(bs):
            if b: converges.append(i+1)
            if b: pop_indices.append(idx)
        for elem in reversed(pop_indices):
            new_curr.pop(elem)
        curr = new_curr
        i += 1 
    
    print(converges)
    return math.lcm(*converges)


s = """
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
""".strip()
s2 = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)

""".strip()

if __name__ == '__main__':
    e1, e2, ex1, ex2, r1, r2 = get_solution_booleans(sys.argv)
            
    if e1 or ex1 or r1: print("PART 1")
    if e1: print("Example Solution:", solve1(s))
    if ex1: print("Example 2 Solution:", solve1(s2))
    if r1: print("Actual Solution:", solve1(inp))

    if e2 or ex2 or r2: print("PART 2")
    if e2: print("Example Solution:", solve2(s))
    if ex2: print("Example 2 Solution:", solve2(s2))
    if r2: print("Actual Solution:", solve2(inp))
