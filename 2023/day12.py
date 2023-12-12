from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    lines = d.splitlines()
    result = 0
    
    for line in lines:
        s, nums = line.split()
        qs = line.count('?')
        possibilities = it.product('#.', repeat=qs)
        for possib in possibilities:
            s2 = ""
            idx = 0
            for c in s:
                if c != '?':
                    s2 += c
                else:
                    s2 += possib[idx]
                    idx += 1
                    
            lens = [len(list(g)) for k, g in it.groupby(s2) if k == '#']
            # print(s2, lens)
            if lens == ints(nums):
                result += 1

    
    return result



    # print(s, nums)

@lru_cache
def possibs(s, nums):
    # print(s, nums)
    if nums[0] == 0:
        if s[0] == '#':
            return 0 
        elif s[0] == '?':
            return possibs(s[1:], nums[1:])
        nums = nums[1:]
    if nums == ():
        # print(s, nums)

        if s.count('#') == 0:
            return 1
        else:
            return 0
    elif s.count('?') + s.count('#') < sum(nums):
        return 0
    elif s.count('?') + s.count('#') == sum(nums):
        tmp = tmap(len, re.split(r'\.+', s.strip('.')))
        print(s, nums, tmp, tmp == nums)
        if tmp == nums:
            return 1
        else:
            return 0
    else:
        if s[0] == '?':
            result = possibs(s[1:], nums) + possibs(s[1:], (nums[0] - 1,) + nums[1:])
            # return possibs(s[1:], nums) + possibs(s[1:], (nums[0] - 1,) + nums[1:])          
        elif s[0] == '#':
            result = possibs(s[1:], (nums[0] - 1,) + nums[1:])  
            # return possibs(s[1:], (nums[0] - 1,) + nums[1:])       
        else:
            result = possibs(s[1:], nums)
            # return possibs(s[1:], nums)   
        if result == 1:
            
            print(s, nums)
        return result
    
@lru_cache(maxsize=None)
def possibs(s, nums, block=False):
    left = sum(nums)

    
    
    if s == '':
        return left == 0
    if left == 0:
        return not '#' in s
    
    if s[0] == '#':
        if nums[0] == 0 and block:
            return 0
        return possibs(s[1:], (nums[0] - 1,) + nums[1:], True)
    
    if s[0] == '.':
        if nums[0] > 0 and block:
            return 0
        return possibs(s[1:], nums[1:] if nums[0] == 0 else nums, False)
    
    if nums[0] == 0 and block:
        return possibs(s[1:], nums[1:], False)
    if block:
        return possibs(s[1:], (nums[0] - 1,) + nums[1:], True)
    return possibs(s[1:], (nums[0] - 1,) + nums[1:], True) + possibs(s[1:], nums, False)
        


def solve2(d):
    lines = d.splitlines()
    result = 0
    
    for line in lines:
        s, nums = line.split()
        s = '?'.join([s] * 5)
        nums = ints(nums) * 5
        result += possibs(s, tuple(nums))

    return result


s = """
.??..??...?##. 1,1,3
""".strip()
s2 = """
?###???????? 3,2,1
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