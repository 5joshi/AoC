from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def parse(nums):
    c, d = nums[:2]
    nums = nums[2:]
    result = 0
    vals = []
    
    for _ in range(c):
        data, val, nums = parse(nums)
        result += data
        vals.append(val)
        
    result += (val := sum(nums[:d]))
    if c == 0:
        return (result, val, nums[d:])
    return (result, sum(vals[i-1] for i in nums[:d] if 0 < i <= len(vals)), nums[d:])

def solve1(d):
    return parse(ints(d))[0]
    
def solve2(d):
    return parse(ints(d))[1]


s = """
2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
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