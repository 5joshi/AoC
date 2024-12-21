from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

DOOR = s_to_grid("""789
456
123
 0A""")
 
ROBOT = s_to_grid(""" ^A
<v>""")

def kpvalid(frm, p):
    curr = frm
    for c in p:
        curr = tadd(curr, CTD[c])
        if DOOR[curr] == " ": return False
    return True

def kpmove(frm, to):
    frm, to = DOOR.find(frm), DOOR.find(to)
    dx, dy = tsub(to, frm)
    path = abs(dx) * ("v" if dx > 0 else "^") + abs(dy) * (">" if dy > 0 else "<")
    return {p + "A" for p in [path, path[::-1]] if kpvalid(frm, p)}
    
@cache
def rmove(frm, to):
    if frm == to: return "A"
    if frm == 'v':
        if to == 'A': return "^>A"
        return f"{to}A"
    elif frm == '^':
        if to == 'A': return ">A"
        return f"v{rmove('v', to)}"
    elif frm == '<':
        if to == 'A': return ">>^A"
        return f">{rmove('v', to)}"
    elif frm == '>':
        if to == 'A': return "^A"
        return f"<{rmove('v', to)}"
    
    if to == '^': return "<A"
    elif to == '>': return "vA"
    elif to == 'v': return "<vA"
    return "v<<A"   

def solve1(d, n=2):
    result = 0
    
    for code in d.splitlines():
        paths = kpmove('A', code[0])
        for frm, to in windows(code, 2):
            paths = {path + ext for path in paths for ext in kpmove(frm, to)}

        results = []
        for path in paths:
            pairs = Counter(windows("A" + path, 2))
            for _ in range(n):
                new_pairs = Counter()
                for (a, b), count in pairs.items():
                    for pair in windows("A" + rmove(a, b), 2):
                        new_pairs[pair] += count
                pairs = new_pairs
            results.append(sum(pairs.values()))
        
        result += min(results) * ints(code)[0]
        
    return result
        

def solve2(d):
    return solve1(d, n=25)


s = """
029A
980A
179A
456A
379A
""".strip()
s2 = """
029A
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