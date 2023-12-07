from utils import *

inp = get_data(year=2023, day=6)

def hold_time(time, dist):
    return binary_search(lambda x: x * (time - x) > dist, lo=0, hi=time // 2)

def solve1(d):
    return product([time - 2 * hold_time(time, dist) + 1 for time, dist in zip(*map(ints, d.splitlines()))])

def solve2(d):
    time, dist = lmap(lambda line: int("".join(line[1:])), map(alphanumerics, d.splitlines()))
    return time - 2 * hold_time(time, dist) + 1



s = """
Time:      7  15   30
Distance:  9  40  200
""".strip()
s2 = """

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
