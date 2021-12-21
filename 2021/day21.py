from utils import *

inp = get_data(year=2021, day=21)


def solve1(d):
    _, p1, _, p2 = ints(d)
    positions = [p1, p2]
    scores = [0, 0]
    roll = 6
    
    while not any([score >= 1000 for score in scores]):
        positions[roll % 2] = ((positions[roll % 2] + roll - 1) % 10) + 1
        scores[roll % 2] += positions[roll % 2]
        roll += 9
     
    return min(scores) * (roll // 3 - 2)   


def solve2(d):
    _, p1, _, p2 = ints(d)
    p1_score = p2_score = 0
    
    possibs = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
    
    @ft.lru_cache(maxsize=None)
    def wins(p1, p1_score, p2, p2_score, player=0):
        if p1_score >= 21:
            return (1, 0)
        elif p2_score >= 21:
            return (0, 1)
        
        result = (0, 0)
        for roll in range(3, 10):
            if player == 0:
                new_p1 = ((p1 + roll - 1) % 10) + 1
                tmp = wins(new_p1, p1_score + new_p1, p2, p2_score, 1)
            else:
                new_p2 = ((p2 + roll - 1) % 10) + 1
                tmp = wins(p1, p1_score, new_p2, p2_score + new_p2, 0)
                
            tmp = tmul(possibs[roll], tmp)
            result = tadd(result, tmp)
                
        return result
            
    result = wins(p1, p1_score, p2, p2_score)
    return max(result)


s = """Player 1 starting position: 4
Player 2 starting position: 8
"""
s2 = """
"""

print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve1(s2))
print("Actual Solution:", solve1(inp))

print("PART 2")
print("Example Solution:", solve2(s))
# print("Example 2 Solution:", solve2(s2))
print("Actual Solution:", solve2(inp))
