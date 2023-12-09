from utils import *

inp = get_data(year=2023)

def diff_list(l):
    return [l[i] - l[i-1] for i in range(1, len(l))]

def solve1(d):
    inp = d.splitlines()
    result = 0
    
    for line in inp:
        line = ints(line)
        all_diffs = [line]
        diffs = line
        zeros = []
        while not all(map(lambda x: x == 0, diffs)):
            diffs = diff_list(diffs)
            all_diffs.append(diffs)
        
        p = 0
        for idx, l in enumerate(all_diffs[::-1]):
            idx = len(all_diffs) - idx - 1
            p = all_diffs[idx][-1]
            prev = all_diffs[idx-1]
            all_diffs[idx-1].append(prev[-1] + p)
    
        result += all_diffs[0][-1]
    return result

def solve2(d):
    inp = d.splitlines()
    result = 0
    
    for line in inp:
        line = ints(line)
        all_diffs = [line]
        diffs = line
        zeros = []
        while not all(map(lambda x: x == 0, diffs)):
            diffs = diff_list(diffs)
            all_diffs.append(diffs)
        
        p = 0
        for idx, l in enumerate(all_diffs[::-1]):
            idx = len(all_diffs) - idx - 1
            p = all_diffs[idx][0]
            prev = all_diffs[idx-1]
            all_diffs[idx-1].insert(0, prev[0] - p)
    
        result += all_diffs[0][0]
    return result


s = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
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
