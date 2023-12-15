from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    def decompress(s):
        if s == '':
            return 0
        
        match = re.match(r'\((\d+)x(\d+)\)', s)
        if match:
            substr = s[match.end():match.end() + int(match.group(1))]
            return len(substr) * int(match.group(2)) + decompress(s[match.end() + int(match.group(1)):])
        return 1 + decompress(s[1:])
    
    return sum(map(decompress, d.splitlines()))

def solve2(d):   
    def decompress(s):
        if s == '':
            return 0
        
        match = re.match(r'\((\d+)x(\d+)\)', s)
        if match:
            substr = s[match.end():match.end() + int(match.group(1))]
            return decompress(substr) * int(match.group(2)) + decompress(s[match.end() + int(match.group(1)):])
        return 1 + decompress(s[1:])
    
    return sum(map(decompress, d.splitlines()))


s = """
(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN""".strip()
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