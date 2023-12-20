from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    result = {False: 0, True: 0}
    modules = eval('{"' + multi_replace(d, [('&', ''), ('%', ''), (', ', '", "'), (' -> ', '": ["'), ('\n', '"], "')]) + '"]}')
    flipflops = {module: False for module in re.findall(r'%([a-z]+)', d)}
    conjunctions = {module: {k: False for k, v in modules.items() if module in v} for module in re.findall(r'&([a-z]+)', d)}
        
    q = deque([('broadcaster', False, 'button')] * 1000)
    while q:
        currm, currp, prevm = q.popleft()
        result[currp] += 1
        if currm == 'broadcaster':
            for nextm in modules[currm]:
                q.append((nextm, currp, currm))
        elif currm in flipflops and not currp:
            flipflops[currm] = not flipflops[currm]
            for nextm in modules[currm]:
                q.append((nextm, flipflops[currm], currm))
        elif currm in conjunctions:
            conjunctions[currm][prevm] = currp
            for nextm in modules[currm]:
                q.append((nextm, not all(conjunctions[currm].values()), currm))       
                
    return product(result.values())

def solve2(d):
    modules = eval('{"' + multi_replace(d, [('&', ''), ('%', ''), (', ', '", "'), (' -> ', '": ["'), ('\n', '"], "')]) + '"]}')
    flipflops = {module: False for module in re.findall(r'%([a-z]+)', d)}
    conjunctions = {module: {k: False for k, v in modules.items() if module in v} for module in re.findall(r'&([a-z]+)', d)}
        
    q = deque()
    cycles = {}
    iterations = 0
    while not len(lfilter(lambda x: x > 1, cycles.values())) >= 4:
        if not q: 
            q.append(('broadcaster', False, 'button'))
            iterations += 1
            
        currm, currp, prevm = q.popleft()
        if currm == 'broadcaster':
            for nextm in modules[currm]:
                q.append((nextm, currp, currm))
        elif currm in flipflops and not currp:
            flipflops[currm] = not flipflops[currm]
            for nextm in modules[currm]:
                q.append((nextm, flipflops[currm], currm))
        elif currm in conjunctions:
            conjunctions[currm][prevm] = currp
            for nextm in modules[currm]:
                if (nextp := not all(conjunctions[currm].values())) and currm not in cycles:
                    cycles[currm] = iterations
                q.append((nextm, nextp, currm))       
                
    return math.lcm(*cycles.values())

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
    if ex2: print("Example 2 Solution:", solve2(s2))
    if r2: print("Actual Solution:", sol2 := solve2(inp))
    
    if (one and r1) or (two and r2):
        go = input('Submit? [y/N] ')
        if go == 'y':
            if one and r1: submit(sol1, part=1, year=YEAR, day=DAY)
            if two and r2: submit(sol2, part=2, year=YEAR, day=DAY)