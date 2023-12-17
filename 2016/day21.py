from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    lines = d.splitlines()
    curr = list('abcdefgh')
    
    for line in lines:
        instruction, *rest = line.split()
        print(instruction, rest)
        if instruction == 'swap':
            if rest[0] == 'position':
                x, y = int(rest[1]), int(rest[4])
            elif rest[0] == 'letter':
                x, y = curr.index(rest[1]), curr.index(rest[4])
            curr[x], curr[y] = curr[y], curr[x]
        elif instruction == 'rotate':
            if rest[0] == 'left':
                x = int(rest[1])
                curr = curr[x:] + curr[:x]
            elif rest[0] == 'right':
                x = int(rest[1])
                curr = curr[-x:] + curr[:-x]
            elif rest[0] == 'based':
                x = rest[-1]
                i = curr.index(x)
                x = (1 + i + (1 if i >= 4 else 0)) % len(curr)
                curr = curr[-x:] + curr[:-x]
        elif instruction == 'reverse':
            x, y = min_max([int(rest[1]), int(rest[-1])])
            curr = curr[:x] + curr[x:y+1][::-1] + curr[y+1:]
        else:
            x, y = int(rest[1]), int(rest[-1])
            val = curr.pop(x)
            curr.insert(y, val)
        print(curr)
    
    return ''.join(curr)

def solve2(d):
    lines = d.splitlines()
    curr = list('decab')
    
    for line in reversed(lines):
        instruction, *rest = line.split()
        print(instruction, rest)
        if instruction == 'swap':
            if rest[0] == 'position':
                x, y = int(rest[1]), int(rest[4])
            elif rest[0] == 'letter':
                x, y = curr.index(rest[1]), curr.index(rest[4])
            curr[x], curr[y] = curr[y], curr[x]
        elif instruction == 'rotate':
            if rest[0] == 'left':
                x = int(rest[1])
                curr = curr[-x:] + curr[:-x]
            elif rest[0] == 'right':
                x = int(rest[1])
                curr = curr[x:] + curr[:x]
            elif rest[0] == 'based':
                x = rest[-1]
                i = curr.index(x)
                x = (1 + i + (1 if i >= 4 else 0)) % len(curr)
                curr = curr[x:] + curr[:x]
        elif instruction == 'reverse':
            x, y = min_max([int(rest[1]), int(rest[-1])])
            curr = curr[:x] + curr[x:y+1][::-1] + curr[y+1:]
        else:
            x, y = int(rest[1]), int(rest[-1])
            val = curr.pop(x)
            curr.insert(y, val)
        print(curr)
    
    return ''.join(curr)


s = """
swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1 step
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d
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