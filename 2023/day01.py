from utils import *

inp = get_data(year=2023, day=1)

NUMS_TO_INTS = {num: idx for idx, num in enumerate('zero one two three four five six seven eight nine'.split())}

def solve1(d):
    return sum(nums[0] * 10 + nums[-1] for nums in map(single_ints, d.splitlines()))    

def all_ints(s):
    matches = re.findall(f'(?=(\d|{"|".join(NUMS_TO_INTS.keys())}))', s)
    return [int(NUMS_TO_INTS.get(match, match)) for match in matches]

def solve2(d):
    return sum(nums[0] * 10 + nums[-1] for nums in map(all_ints, d.splitlines()))


s = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
""".strip()
s2 = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
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
