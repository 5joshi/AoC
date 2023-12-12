from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

@lru_cache
def count(s, nums):
    s = s.strip('.') + '.'
    if s == '.': return sum(nums) == 0
    if sum(nums) == 0: return '#' not in s
    if sum(nums) > len(s) - 1: return 0

    if s[0] == '#': return count(s[nums[0]+1:], nums[1:]) if re.fullmatch('[?#]+[\.?]', s[:nums[0]+1]) else 0
    return count(s[1:], nums) + count('#' + s[1:], nums)


def solve1(d):
    return sum(count(s, tuple(ints(nums))) for s, nums in map(lambda line: line.split(), d.splitlines()))

def solve2(d):
    return sum(count('?'.join([s] * 5), tuple(ints(nums)*5)) for s, nums in map(lambda line: line.split(), d.splitlines()))



s = """
.??..??...?##. 1,1,3
""".strip()
s2 = """
?###???????? 3,2,1
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