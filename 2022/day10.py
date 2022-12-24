from utils import *

# inp = get_data(year=2022, day=10)


def solve1(d):
    inp = d.splitlines()
    x = 1
    strengths = [0]
    
    for line in inp:
        strengths.append(len(strengths) * x)
        match line:
            case 'noop': continue
            case default:
                strengths.append(len(strengths) * x)
                x += ints(line)[0]

    return strengths[20] + strengths[60] + strengths[100] + strengths[140] + strengths[180] + strengths[220]

def solve2(d):
    inp = d.splitlines()
    pixels = []
    cycle = x = 1
    
    def tick():
        nonlocal pixels, cycle
        pixels.append(x <= cycle % 40 <= x + 2)
        cycle += 1
    
    for line in inp:
        tick()
        match line:
            case 'noop': continue
            case default:
                tick()
                x += ints(line)[0]
    
    return gridmap(lambda x: '# ' if x else '. ', every_n(pixels, 40))


s = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""
s2 = """
"""

print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve1(s2))
# print("Actual Solution:", solve1(inp))

print("PART 2")
print("Example Solution:") 
print_grid(solve2(s))
# print("Example 2 Solution:", solve2(s2))
# print("Actual Solution:", solve2(inp))
