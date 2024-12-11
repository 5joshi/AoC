from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    nums = ints(d)
    result = 0
    
    for _ in range(25):
        new_nums = list()
        for idx, num in enumerate(nums):
            if num == 0: new_nums.append(1)
            elif len(str(num)) % 2 == 0: 
                temp = str(num)
                left = temp[:len(temp) // 2]
                right = temp[len(temp) // 2:]
                new_nums += [int(left), int(right)] 
            else:
                new_nums.append(num * 2024)
        nums = new_nums
    
    return len(nums)

def solve2(d):
    nums = Counter(ints(d))
    result = 0
    
    for _ in range(75):
        new_nums = Counter()
        for num, count in nums.items():
            if num == 0: new_nums[1] += count
            elif len(str(num)) % 2 == 0: 
                temp = str(num)
                left = temp[:len(temp) // 2]
                right = temp[len(temp) // 2:]
                new_nums[int(left)] += count
                new_nums[int(right)] += count
            else:
                new_nums[num * 2024] += count
        nums = new_nums
    
    print(len(nums.items()))
    return sum(nums.values())


s = """
125 17""".strip()
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