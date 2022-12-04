from utils import *

inp = get_data(year=2022, day=3)


def solve1(d):
    inp = d.splitlines()
    result = 0
    
    for line in inp:
        l1, l2 = set(line[:len(line)//2]), set(line[len(line)//2:])
        common = (l1 & l2).pop()
        result += 26 * common.isupper() + ord(common.lower()) - ord("a") + 1
    
    return result

def solve2(d):
    inp = d.splitlines()
    result = 0
    
    for l1, l2, l3 in every_n(inp, 3):
        common = (set(l1) & set(l2) & set(l3)).pop()
        result += 26 * common.isupper() + ord(common.lower()) - ord("a") + 1

    return result


s = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""
s2 = """
"""

print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve1(s2))
print("Actual Solution:", solve1(inp))

# print("PART 2")
print("Example Solution:", solve2(s))
# # print("Example 2 Solution:", solve2(s2))
print("Actual Solution:", solve2(inp))
