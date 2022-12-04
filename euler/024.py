from utils import *

permutations = 1

def descending(num):
    for i in range(len(num)-1):
        if num[i+1] > num[i]:
            return False
    return True

def permute(num):
    if len(num) == 2:
        return num[::-1]
    elif not descending(num[1:]):
        return num[0] + permute(num[1:])
    else:
        nums = sorted(list(num))
        idx = nums.index(num[0]) + 1
        first = nums[idx]
        nums.pop(idx)
        return first + "".join(nums)
        
def solve():
    result = "0123456789"
    for _ in range(1000000 - 1):
        result = permute(result)
    return result

print("Solution:", solve())
