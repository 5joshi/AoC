from utils import *

inp = get_data(year=2021)

COSTS = {"A": 1, "B": 10, "C": 100, "D": 1000}
TARGETS = {"A": 0, "B": 1, "C": 2, "D": 3}
WAITING_SPOTS = [1, 2, 4, 6, 8, 10, 11]
ROOMS = [tuple((x, y) for x in range(2, 4)) for y in [3, 5, 7, 9]]
NEW_ROOMS = [tuple((x, y) for x in range(2, 6)) for y in [3, 5, 7, 9]]
GOAL = """#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #########
"""
NEW_GOAL = """#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########
"""

def print_state(state, part=1):
    grid = defaultdict(lambda: "#")
    for pos in [(1, x) for x in range(1, 12)] + flatten(ROOMS if part == 1 else NEW_ROOMS):
        grid[pos] = '.'
    for pos, letter in state:
        grid[pos] = letter
    for x in range(5 if part == 1 else 7):
        for y in range(0 if x < 3 else 2, 13 if x < 3 else 11):
            print(grid[(x, y)], end="")
        print("\n" + ("  " if x >= 2 else ""), end="")
    
def print_path(path, part=1):
    for state in path[1]:
        print_state(state, part)
        print()

def state_from_inp(inp):
    state = set()
    for x, line in enumerate(inp.splitlines()):
        for y, c in enumerate(line):
            if c in "ABCD":
                state.add(((x, y), c))
    return frozenset(state)


def solve1(d, rooms=ROOMS, goal=GOAL):
    start = state_from_inp(d)
    goal = state_from_inp(goal)
    
    def new_state(state, letter, start, goal):
        new_state = set(state)
        new_state.remove((start, letter))
        new_state.add((goal, letter))
        return frozenset(new_state)
    
    def cost(letter, start, goal):
        return pdist1(start, goal) * COSTS[letter]
    
    def expand(state):
        nonlocal cost, new_state
        result = []
        occupied = {pos: letter for pos, letter in state}
        # Room to waiting spot
        for room in rooms:
            idx = len(room) - sum([coord in occupied for coord in room])
            if idx == len(room): continue
            highest = room[idx]
            col = highest[1]
            for pos in WAITING_SPOTS:
                if not any([(1, y) in occupied for y in range(min(pos, col), max(pos, col)+1)]):
                    letter = occupied[highest]
                    result.append((cost(letter, highest, (1, pos)), new_state(state, letter, highest, (1, pos)))) 
        # Waiting spot to room   
        for pos in [(1, y) for y in WAITING_SPOTS]:
            if pos not in occupied: continue
            letter = occupied[pos]
            room = rooms[TARGETS[letter]]         
            idx = len(room) - sum([coord in occupied for coord in room]) - 1
            if idx == -1: continue
            lowest = room[idx]
            if sum([(1, y) in occupied for y in range(min(pos[1], lowest[1]), max(pos[1], lowest[1]) + 1)]) == 1:
                if all([occupied[coord] == letter for coord in room[idx+1:]]):
                    result.append((cost(letter, pos, lowest), new_state(state, letter, pos, lowest)))

        return result   
            
    def heuristic(state):
        cost = 0
        for pos, letter in state:
            goal = rooms[TARGETS[letter]]
            if pos not in goal:
                cost += pdist1(pos, goal[0]) * COSTS[letter]
        return cost
            
    path = a_star(start, goal, expand, heuristic)           
    # print_path(path)
    return path[0]

def solve2(d):
    d = "\n".join(d.splitlines()[:3] + ["  #D#C#B#A#  ", "  #D#B#A#C#  "] + d.splitlines()[3:])
    return solve1(d, NEW_ROOMS, NEW_GOAL)


s = """#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
"""
s2 = """#############
#...........#
###A#B#C#D###
  #B#A#C#D#
  #########
"""

print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve1(s2))
print("Actual Solution:", solve1(inp))

print("PART 2")
print("Example Solution:", solve2(s))
# print("Example 2 Solution:", solve2(s2))
print("Actual Solution:", solve2(inp))
