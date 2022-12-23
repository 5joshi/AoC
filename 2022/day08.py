from utils import *

# inp = get_data(year=2022, day=8)


def solve1(d):
    heights = Grid(number_grid(d))
    size = heights.rows
    
    result = 0
    
    for (x, y) in heights.coords():
        if x in [0, size - 1] or y in [0, size - 1]: 
            result += 1
        else:
            curr_height = heights[(x, y)]
            row = heights.get_row(x)
            col = heights.get_col(y)
        
            if all([height < curr_height for height in row[:y]]) or \
                all([height < curr_height for height in row[y+1:]]) or \
                all([height < curr_height for height in col[:x]]) or \
                all([height < curr_height for height in col[x+1:]]):
                result += 1
        
    return result

def solve2(d):
    heights = Grid(number_grid(d))
    max_score = 0
    
    for (x, y) in heights.coords():
        curr_height = heights[(x, y)]
        curr_score = 1
        row = heights.get_row(x)
        col = heights.get_col(y)
    
        left = row[:y][::-1]
        right = row[y+1:]
        up = col[:x][::-1]
        down = col[x+1:]
        
        for l in (left, right, up, down):
            temp_score = 0
            for height in l:
                if height < curr_height:
                    temp_score += 1
                else:
                    temp_score += 1
                    break
            curr_score *= temp_score
        max_score = max(curr_score, max_score)
                
    return max_score


s = """30373
25512
65332
33549
35390
"""
s2 = """
"""

print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve1(s2))
# print("Actual Solution:", solve1(inp))

print("PART 2")
print("Example Solution:", solve2(s))
# print("Example 2 Solution:", solve2(s2))
# print("Actual Solution:", solve2(inp))
