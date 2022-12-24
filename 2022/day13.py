from utils import *

# inp = get_data(year=2022, day=13)

def compare(l1, l2):
    if isinstance(l1, int) and isinstance(l2, int):
        if l1 < l2: return True
        elif l1 > l2: return False
        else: return None
    elif isinstance(l1, int):
        l1 = [l1]
    elif isinstance(l2, int):
        l2 = [l2]
    
    for x, y in zip(l1, l2):
        result = compare(x, y)
        if result is not None: 
            return result
    
    if len(l1) < len(l2): return True
    elif len(l1) > len(l2): return False
    else: return None
        


def solve1(d):
    inp = lmap(lambda x: x.splitlines(), d.split("\n\n"))
    orders = [compare(eval(l1), eval(l2)) for l1, l2 in inp]
    return sum([idx + 1 for idx, correct in enumerate(orders) if correct])

def solve2(d):
    packets = [[[2]], [[6]]]
    for line in d.splitlines():
        if line:
            packets.append(eval(line))
            
    packets.sort(key=ft.cmp_to_key(lambda x, y: -1 if compare(x, y) else 1))
    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


s = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
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
