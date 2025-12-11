from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)


def solve1(d):
    graph = {head: set(tail) for head, *tail in lmap(words, d.splitlines())}
    
    @cache
    def f(start, end):
        if start == end: return 1
        if start not in graph: return 0
        return sum(f(mid, end) for mid in graph[start])    
    
    return f("you", "out")


def solve2(d):
    graph = {head: set(tail) for head, *tail in lmap(words, d.splitlines())}
    
    @cache
    def f(start, end):
        if start == end: return 1
        if start not in graph: return 0
        return sum(f(mid, end) for mid in graph[start])    
    
    return f("svr", "dac") * f("dac", "fft") * f("fft", "out") + f("svr", "fft") * f("fft", "dac") * f("dac", "out")




s = """
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out


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