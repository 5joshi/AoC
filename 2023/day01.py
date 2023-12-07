from utils import *

inp = get_data(year=2023, day=1)

def solve1(d):
    return sum(nums[0] * 10 + nums[-1] for nums in map(single_ints, d.splitlines()))    

def all_ints(s):
    nums = []
    for idx in range(len(s)):
        if s[idx].isdigit():
            nums.append(int(s[idx]))
            continue
        for num, value in NUMS_TO_INTS.items():
            if s[idx:].startswith(num): 
                nums.append(value)
    return nums

def solve2(d):
    return sum(nums[0] * 10 + nums[-1] for nums in map(all_ints, d.splitlines()))


s = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""
s2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve1(s2))
print("Actual Solution:", solve1(inp))

print("PART 2")
print("Example Solution:", solve2(s2))
# print("Example 2 Solution:", solve2(s2))
print("Actual Solution:", solve2(inp))
