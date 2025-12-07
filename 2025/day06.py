from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    lines = d.splitlines()
    ops = [c for c in lines[-1] if c != ' ']
    lines = lmap(ints, lines[:-1])
    result = 0
    for c in range(len(lines[0])):
        if ops[c] == '+':
            result += sum(line[c] for line in lines)
        else:
            result += math.prod(line[c] for line in lines)
    
    return result

def solve2(d):
    lines = d.splitlines()
    ops = [c for c in lines[-1] if c != ' ']
    result = 0
    
    nums = []
    try:
        for c in range(len(lines[0])):
            num = ''.join([line[-(c + 1)] for line in lines])
            if num.strip() == '': continue
            print(num)
            if num.endswith('+'):
                nums.append(int(num[:-1]))
                print(sum(nums))
                result += sum(nums)
                nums = []
            elif num.endswith('*'):
                nums.append(int(num[:-1]))
                print(product(nums))
                result += product(nums)
                nums = []
            else:
                nums.append(int(num))    
    except:
        pass
    
    
    return result


s = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
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