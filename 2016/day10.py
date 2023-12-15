from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    lines = d.splitlines()
    values = defaultdict(set)
    to = defaultdict(lambda: [-1, -1])
    order = deque()
    
    for line in lines:
        nums = ints(line)
        line = line.split()
        if len(nums) == 2:
            val, bot = nums
            values[bot].add(val)
            if len(values[bot]) == 2: order.append(bot)
            
        else:
            lo, hi = line[5], line[10]
            if lo == 'bot': to[nums[0]][0] = nums[1]
            if hi == 'bot': to[nums[0]][1] = nums[2]
            
    while order:
        bot = order.popleft()

        if (dep := to[bot][0]) != -1: 
            values[dep].add(min(values[bot]))
            if len(values[dep]) == 2: order.append(dep)
        if (dep := to[bot][1]) != -1:
            values[dep].add(max(values[bot]))
            if len(values[dep]) == 2: order.append(dep)
    
    return [k for k, v in values.items() if v == {17, 61}][0]

def solve2(d):
    lines = d.splitlines()
    values = defaultdict(set)
    to = defaultdict(lambda: [-1, -1])
    order = deque()
    
    for line in lines:
        nums = ints(line)
        line = line.split()
        if len(nums) == 2:
            val, bot = nums
            values[bot].add(val)
            if len(values[bot]) == 2: order.append(bot)
            
        else:
            lo, hi = line[5], line[10]
            to[nums[0]][0] = nums[1] if lo == 'bot' else str(nums[1])
            to[nums[0]][1] = nums[2] if hi == 'bot' else str(nums[2])
            
    while order:
        bot = order.popleft()

        if (dep := to[bot][0]) != -1: 
            values[dep].add(min(values[bot]))
            if len(values[dep]) == 2: order.append(dep)
        if (dep := to[bot][1]) != -1:
            values[dep].add(max(values[bot]))
            if len(values[dep]) == 2: order.append(dep)
    
    return product(values[k].pop() for k in ['0', '1', '2'])


s = """
value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2

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