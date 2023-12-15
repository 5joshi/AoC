from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def h(s):
    start = 0
    for c in s:
        start += ord(c)
        start *= 17
        start %= 256
    return start

def solve1(d):
    lines = d.split(",")
    result = 0
    
    for line in lines:
        result += h(line)
    
    
    return result

        

def solve2(d):
    lines = d.split(",")
    boxes = defaultdict(list)
    result = 0
    

    
    for line in lines:
        s=line
        print(s.split('='))
        if '=' in s:
            b, n = s.split('=')
            hsh = h(b)
            if not any(elem[0] == b for elem in boxes[hsh]):
                boxes[hsh].append((b, int(n)))
            else:
                for idx, elem in enumerate(boxes[hsh]):
                    if elem[0] == b:
                        boxes[hsh][idx] = (b, int(n))
        if '-' in s:
            b = s[:-1]
            hsh = h(b)
            pop_idx = []
            for elem in boxes[hsh]:
                if elem[0] == b:
                    pop_idx.append(elem)
                    
            for elem in reversed(pop_idx):
                boxes[hsh].remove(elem)
        # print(b, line, boxes)
                    
    for i in range(256):
        # print([((i+1), (idx + 1), val[1]) for idx, val in enumerate(boxes[i])])
        result += sum((i+1) * (idx + 1) * val[1] for idx, val in enumerate(boxes[i]))
    print(h('cm'), h('rn'))
    return result


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