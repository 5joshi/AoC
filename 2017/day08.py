from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    d = re.sub(r'(^|\n|if )(\w+)', r'\1variables["\2"]', d)
    d = multi_replace(d, [('\n', ' else 0\n'), ('inc', '+='), ('dec', '-=')]) + ' else 0'
    variables = defaultdict(int)
    exec(d)
    
    return max(variables.values())

def solve2(d):
    d = re.sub(r'(^|\n|if )(\w+)', r'\1variables["\2"]', d)
    d = multi_replace(d, [('\n', ' else 0\n'), ('inc', '+='), ('dec', '-=')]) + ' else 0'
    variables = defaultdict(int)
    result = 0
    
    for line in d.splitlines():
        exec(line)
        result = max(result, max(variables.values()))
    
    return result


s = """
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
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