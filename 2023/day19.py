from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

# TODO: cleanup
def solve1(d):
    start, end = d.split('\n\n')
    workflows = {}
    total = 0
    
    for line in start.splitlines():
        frm, to = line.split('{')
        workflows[frm] = []
        for instruction in to[:-1].split(','):
            workflows[frm].append(instruction.split(':'))
    
    for line in end.splitlines():
        workflow = 'in'
        values = {var: value for var, value in every_n(words_and_ints(line), 2)}
        while workflow != 'A' and workflow != 'R':
            for instruction in workflows[workflow]:
                if len(instruction) == 2:
                    condition, result = instruction
                    condition = re.sub(r'([a-z]+)', r'values["\1"]', condition)
                    if eval(condition):
                        workflow = result
                        break
                else:
                    workflow = instruction[0]
                    break
        if workflow == 'A':
            total += sum(ints(line))
    
    return total

def solve2(d):
    start, end = d.split('\n\n')
    workflows = {}
    total = 0
    
    for line in start.splitlines():
        frm, to = line.split('{')
        workflows[frm] = []
        for instruction in to[:-1].split(','):
            workflows[frm].append(instruction.split(':'))
    
    def possibilities(workflow, idx, ranges):
        if workflow == 'A':
            return product(rng[1] - rng[0] + 1 for rng in ranges.values())
        if workflow == 'R':
            return 0
        
        instruction = workflows[workflow][idx]
        if len(instruction) == 2:
            condition, result = instruction
            var, sign, *rest = condition
            rest = ''.join(rest)
            curr_min, curr_max = ranges[var]
            if (int(rest) <= curr_min and sign == '<') or (int(rest) >= curr_max and sign == '>'):
                return 0
            elif curr_min < int(rest) < curr_max:
                true_ranges = ranges.copy()
                false_ranges = ranges.copy()
                if sign == '<':
                    true_ranges[var] = (curr_min, int(rest)-1)
                    false_ranges[var] = (int(rest), curr_max)
                else:
                    true_ranges[var] = (int(rest)+1, curr_max)
                    false_ranges[var] = (curr_min, int(rest))
                return possibilities(result, 0, true_ranges) + possibilities(workflow, idx + 1, false_ranges)
            else:
                return possibilities(result, 0, ranges)
                
        else:
            return possibilities(instruction[0], 0, ranges)
        
        
    return possibilities('in', 0, {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)})


s = """
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
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