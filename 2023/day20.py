from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    lines = d.splitlines()
    result = 0
    broadcaster = {}
    flipflops = {}
    flipflop_states = {}
    conjunc = {}
    conjunc_last = {}
    lows = highs = 0
    for line in lines:
        frm, to = line.split(' -> ')
        to = to.split(', ')
        if frm == 'broadcaster':
            broadcaster[(frm)] = to
        elif frm[0] == '%':
            flipflops[(frm[1:])] = to
            flipflop_states[(frm[1:])] = 'off'
        elif frm[0] == '&':
            conjunc[(frm[1:])] = to
            conjunc_last[(frm[1:])] = {}
    
    for key, values in broadcaster.items():
        for value in values:
            if value in conjunc:
                conjunc_last[value][key] = 'low'
    for key, values in flipflops.items():
        for value in values:
            if value in conjunc:
                conjunc_last[value][key] = 'low'
    for key, values in conjunc.items():
        for value in values:
            if value in conjunc:
                conjunc_last[value][key] = 'low'
        
    q = deque()
    for _ in range(1000): q.append(('broadcaster', 'low', 'button'))
    while q:
        currm, currp, prevm = q.popleft()
        if currp == 'low': lows += 1
        elif currp == 'high': highs += 1
        if currm == 'broadcaster':
            for nextm in broadcaster[currm]:
                q.append((nextm, currp, currm))
        elif currm in flipflops and currp == 'low':
            flipflop_states[currm] = 'on' if flipflop_states[currm] == 'off' else 'off'
            for nextm in flipflops[currm]:
                q.append((nextm, 'high' if flipflop_states[currm] == 'on' else 'low', currm))
        elif currm in conjunc:
            conjunc_last[currm][prevm] = currp
            if all(value == 'high' for value in conjunc_last[currm].values()):
                for nextm in conjunc[currm]:
                    q.append((nextm, 'low', currm))
            else:
                for nextm in conjunc[currm]:
                    q.append((nextm, 'high', currm))            
            
    return lows * highs

def solve2(d):
    lines = d.splitlines()
    result = 0
    broadcaster = {}
    flipflops = {}
    flipflop_states = {}
    conjunc = {}
    conjunc_last = {}
    lows = highs = 0
    for line in lines:
        frm, to = line.split(' -> ')
        to = to.split(', ')
        if frm == 'broadcaster':
            broadcaster[(frm)] = to
        elif frm[0] == '%':
            flipflops[(frm[1:])] = to
            flipflop_states[(frm[1:])] = 'off'
        elif frm[0] == '&':
            conjunc[(frm[1:])] = to
            conjunc_last[(frm[1:])] = {}
    
    for key, values in broadcaster.items():
        for value in values:
            if value in conjunc:
                conjunc_last[value][key] = 'low'
    for key, values in flipflops.items():
        for value in values:
            if value in conjunc:
                conjunc_last[value][key] = 'low'
    for key, values in conjunc.items():
        for value in values:
            if value in conjunc:
                conjunc_last[value][key] = 'low'
        
    conjunc_ons = {}
    conjunc_offs = {}
    q = deque()
    iterations = 0  
    while iterations < 100000:
        iterations += 1
        q.append(('broadcaster', 'low', 'button'))
        if iterations % 100000 == 0: print(conjunc_offs)
        # if iterations % 100000 == 0: 
        #     print(iterations, conjunc_last)
        # print([(key, [*value.values()].count('high'), len(value.values())) for key, value in conjunc_last.items()])
        # print(conjunc_last)
        # print([(key, [*value.values()].count('high'), len(value.values())) for key, value in conjunc_last.items()])
        while q:
            currm, currp, prevm = q.popleft()
            if currm == 'rx' and currp == 'low': return iterations
            if currm == 'broadcaster':
                for nextm in broadcaster[currm]:
                    q.append((nextm, currp, currm))
            elif currm in flipflops and currp == 'low':
                flipflop_states[currm] = 'on' if flipflop_states[currm] == 'off' else 'off'
                for nextm in flipflops[currm]:
                    q.append((nextm, 'high' if flipflop_states[currm] == 'on' else 'low', currm))
            elif currm in conjunc:
                conjunc_last[currm][prevm] = currp
                if all(value == 'high' for value in conjunc_last[currm].values()):
                    if currm not in conjunc_ons: conjunc_ons[currm] = iterations
                    for nextm in conjunc[currm]:
                        q.append((nextm, 'low', currm))
                else:
                    if currm not in conjunc_offs: conjunc_offs[currm] = iterations
                    for nextm in conjunc[currm]:
                        q.append((nextm, 'high', currm))            
    return math.lcm(*conjunc_offs.values())

s = """
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a

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