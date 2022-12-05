from utils import *

# inp = get_data(year=2022)


def solve1(d):
    stacks, instr = map(lambda x: x.splitlines(), d.split("\n\n"))
    l = [[] for _ in range(ints(stacks[-1])[-1])]
    for line in stacks[:-1]:
        for idx, c in enumerate(line[1::4]):
            if c != ' ':
                l[idx].append(c)
    
    for line in instr:
        amt, frm, to = ints(line)
        for _ in range(amt):
            l[to - 1].insert(0, l[frm - 1].pop(0))
    
    return "".join([s[0] for s in l])

def solve2(d):
    stacks, instr = map(lambda x: x.splitlines(), d.split("\n\n"))
    l = [[] for _ in range(ints(stacks[-1])[-1])]
    for line in stacks[:-1]:
        for idx, c in enumerate(line[1::4]):
            if c != ' ':
                l[idx].append(c)
    
    for line in instr:
        amt, frm, to = ints(line)
        l[to - 1][:0] = l[frm - 1][:amt]
        l[frm - 1] = l[frm - 1][amt:]
    
    return "".join([s[0] for s in l])


s = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""
s2 = """
"""

print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve1(s2))
# print("Actual Solution:", solve1(inp))

# print("PART 2")
print("Example Solution:", solve2(s))
# # print("Example 2 Solution:", solve2(s2))
# print("Actual Solution:", solve2(inp))
