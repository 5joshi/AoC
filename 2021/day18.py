from utils import *

inp = get_data(year=2021, day=18)

def explode(l, parents=[]):
    if isinstance(l, int):
        return False
    if len(parents) < 4:
        return explode(l[0], parents + [(l, 0)]) or explode(l[1], parents + [(l, 1)])
    
    for side in [0, 1]:
        other_side = int(not side)
        for parent, idx in reversed(parents):
            if idx == other_side:
                if isinstance(parent[side], int):
                    parent[side] += l[side]
                else:
                    rightmost = parent[side]
                    while not isinstance(rightmost[other_side], int):
                        rightmost = rightmost[other_side]
                    rightmost[other_side] += l[side]
                break

    parent, idx = parents[-1]
    parent[idx] = 0
    return True
    

def split(l, parents=[]):
    if isinstance(l, list):
        return split(l[0], parents + [(l, 0)]) or split(l[1], parents + [(l, 1)])
    elif l >= 10:
        parent, idx = parents[-1]
        parent[idx] = [l//2, (l+1)//2]
        return True
    else:
        return False

def reduction(l):
    while explode(l) or split(l):
        continue
    return l
        
def magnitude(l):
    if isinstance(l, list):
        return 3 * magnitude(l[0]) + 2 * magnitude(l[1])    
    return l


def solve1(d):
    inp = lmap(eval, d.splitlines())
        
    result = inp[0]
    for line in inp[1:]:
        result = reduction([result, line])    
        
    return magnitude(result)

def solve2(d):
    inp = lmap(eval, d.splitlines())
    result = 0
    
    for f1, f2 in it.combinations(inp, 2):
        result = max(result, magnitude(reduction([deepcopy(f1), deepcopy(f2)])))
        result = max(result, magnitude(reduction([deepcopy(f2), deepcopy(f1)])))

    return result


s = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
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
