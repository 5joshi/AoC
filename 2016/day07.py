from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    lines = d.splitlines()
    result = 0
    
    for line in lines:
        abbas = re.findall('(\w)(\w)\\2\\1', line)
        bad = re.findall('\[\w*(\w)(\w)\\2\\1\w*\]', line)
        if (not bad or all(a == b for a, b in bad)) and any(a != b for a, b in abbas):
            result += 1
    
    return result

def solve2(d):
    lines = d.splitlines()
    result = 0
        
    for line in lines:
        ababab = re.findall('(?=(\w)(?!\\1)(\w)\\1(?:\w|\[\w*\])*\[\w*\\2\\1\\2\w*\])', line)
        bababa = re.findall('(?=\[\w*(\w)(?!\\1)(\w)\\1\w*\](?:\w|\[\w*\])*\\2\\1\\2)', line)
        if len(ababab) + len(bababa) > 0:
            result += 1
    
    return result


s = """
aba[bab]xyz
xyx[xyx]xyx
aaa[kek]eke
zazbz[bzb]cdb
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