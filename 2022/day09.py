from utils import *

# inp = get_data(year=2022, day=9)


def solve1(d):
    inp = d.splitlines()
    visited = set()
    tail = head = (0, 0)

    for line in inp:
        direction, dist = line.split(' ')
        direction = CHAR_TO_DELTA[direction]
        dist = int(dist)
        
        for _ in range(dist):
            # print(line[0], head, tail)
            head = tadd(head, direction)
            if any(x > 1 for x in map(abs, tsub(head, tail))):
                tail_direction = tnorm(tsub(head, tail))
                tail = tadd(tail, tail_direction)
            visited.add(tail)

       
    # print_grid(points_to_grid(list(visited), flip=False))   
    return len(visited)

def solve2(d):
    inp = d.splitlines()
    visited = set()
    rope = [(0, 0) for _ in range(10)]

    for line in inp:
        direction, dist = line.split(' ')
        direction = CHAR_TO_DELTA[direction]
        dist = int(dist)
        
        for _ in range(dist):
            # print(line[0], head, tail)
            rope[0] = tadd(rope[0], direction)
            for idx in range(1, 10):
                if any(x > 1 for x in map(abs, tsub(rope[idx-1], rope[idx]))):
                    tail_direction = tnorm(tsub(rope[idx-1], rope[idx]))
                    rope[idx] = tadd(rope[idx], tail_direction)
            visited.add(rope[-1])

    return len(visited)

s = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""
s2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""

print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve1(s2))
# print("Actual Solution:", solve1(inp))

print("PART 2")
print("Example Solution:", solve2(s))
print("Example 2 Solution:", solve2(s2))
# print("Actual Solution:", solve2(inp))
