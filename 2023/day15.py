from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def h(s):
    return reduce(lambda acc, c: ((acc + ord(c)) * 17) % 256, s, 0)

def solve1(d):
    return sum(map(h, d.split(',')))

def solve2(d):
    boxes = {i: [] for i in range(256)}
    
    for s in d.split(","):
        if '=' in s:
            label, n = s.split('=')
            box = h(label)
            for idx, (l2, _) in enumerate(boxes[box]):
                if label == l2:
                    boxes[box][idx] = (label, int(n))
                    break
            else:
                boxes[box].append((label, int(n)))
        else:
            label = s[:-1]
            box = h(label)
            boxes[box] = lfilter(lambda v: v[0] != label, boxes[box])
                    
    return sum(sum((box + 1) * (idx + 1) * n for idx, (_, n) in enumerate(boxes[box])) for box in range(256))


s = """
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
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