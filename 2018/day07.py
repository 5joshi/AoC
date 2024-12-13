from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)


def solve1(d):
    pairs = lmap(lambda w: (w[1], w[7]), map(words, d.splitlines()))
    rules = defaultdict(set)
    inv = defaultdict(set)
    for a, b in pairs: 
        rules[a].add(b)
        inv[b].add(a)
        
    nodes = set(rules.keys()) | set(inv.keys())
    
    q = [x for x in nodes if sum(x in rules[other] for other in nodes) == 0]
    seen = []
    while len(seen) < len(nodes):
        curr = (q := sorted(q)).pop(0)
        if curr in seen: continue
        seen.append(curr)
        q.extend([x for x in rules[curr] if all(n in seen for n in inv[x])])
    
    return "".join(seen)

def solve2(d):
    pairs = lmap(lambda w: (w[1], w[7]), map(words, d.splitlines()))
    rules = defaultdict(set)
    inv = defaultdict(set)
    time = 0
    for a, b in pairs: 
        rules[a].add(b)
        inv[b].add(a)
        
    nodes = set(rules.keys()) | set(inv.keys())
    
    q = [x for x in nodes if sum(x in rules[other] for other in nodes) == 0]
    seen = set()
    workers = []
    while len(seen) < len(nodes) or workers:
        q = sorted(q)
        while q and len(workers) < 5:
            if (curr := q.pop(0)) not in seen and curr not in lmap(fst, workers):
                workers.append([curr, 61 + ord(curr) - ord('A')])

        for worker in workers:
            worker[1] -= 1
            if worker[1] == 0:
                seen |= {worker[0]}
                q.extend([x for x in rules[worker[0]] if all(n in seen for n in inv[x])])   
        workers = [worker for worker in workers if worker[1] > 0]
        time += 1
    
    return time


s = """
Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.

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