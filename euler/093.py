from utils import *

def num_consecutive(nums):
    curr = 1
    while curr in nums:
        curr += 1
    return curr - 1
        
@lru_cache(maxsize=None)
def perform_operations(num1, num2):
    nums = {num1 + num2, num1 * num2}
    nums.add(num1 - num2 if num1 >= num2 else num2 - num1)
    if num2 != 0: nums.add(num1 / num2)
    if num1 != 0: nums.add(num2 / num1)
    return nums
        
def solve():
    best_result = (0, None, None)

    for a, b, c, d in combinations(range(1, 10), 4):
        result = set()
        for x_a, x_b, x_c, x_d in permutations([a, b, c, d]):
            for num1 in perform_operations(x_a, x_b):
                for num2 in perform_operations(num1, x_c):
                    for num3 in perform_operations(num2, x_d):
                        result.add(num3)
                                
        curr_result = num_consecutive(result)   
        if curr_result >= best_result[0]:
            best_result = (curr_result, (a, b, c, d), sorted([int(x) for x in result if x == int(x)]))
                    
    return best_result 
                    
solution = solve()
print(solution)
print("Solution:", "".join([str(x) for x in solution[1]]))
