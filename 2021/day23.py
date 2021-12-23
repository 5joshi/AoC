from utils import *

inp = get_data(year=2021)

COSTS = {"A": 1, "B": 10, "C": 100, "D": 1000}
WAITING_SPOTS = [1, 2, 4, 6, 8, 10, 11]
ROOMS = [((2, 3), (3, 3)), ((2, 5), (3, 5)), ((2, 7), (3, 7)), ((2, 9), (3, 9))]
NEW_ROOMS = [((2, 3), (3, 3), (4, 3), (5, 3)), ((2, 5), (3, 5), (4, 5), (5, 5)), ((2, 7), (3, 7), (4, 7), (5, 7)), ((2, 9), (3, 9), (4, 9), (5, 9))]
LETTER_GOAL = {"A": 0, "B": 1, "C": 2, "D": 3}
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

def print_state(state):
    print_out = defaultdict(lambda: "#")
    for pos in [(1, x) for x in range(1, 12)]:
        print_out[pos] = '.'
    for top, bottom in ROOMS:
        print_out[top] = "."
        print_out[bottom] = "."
    for pos, letter in state:
        print_out[pos] = letter
    for x in range(7):
        for y in range(13):
            print(print_out[(x, y)], end="")
        print()
    

def state_from_inp(inp):
    state = set()
    for x, line in enumerate(inp.splitlines()):
        for y, c in enumerate(line):
            if c in "ABCD":
                state.add(((x, y), c))
    return frozenset(state)

def solve1(d):
    start = state_from_inp(d)
    goal = state_from_inp(GOAL)
    
    def new_state(state, letter, start, goal):
        new_state = set(state)
        new_state.remove((start, letter))
        new_state.add((goal, letter))
        return frozenset(new_state)
    
    def move_cost(letter, start, goal):
        # print(start, goal)
        return pdist1(start, goal) * COSTS[letter]
    
    def expand(state):
        nonlocal move_cost, new_state
        result = []
        
        occupied = {pos: letter for pos, letter in state}
        for top, bottom in ROOMS:
            col = top[1]
            if top in occupied:
                for pos in WAITING_SPOTS:
                    if not any([(1, y) in occupied for y in range(min(pos, col), max(pos, col)+1)]):
                        letter = occupied[top]
                        result.append((move_cost(letter, top, (1, pos)), new_state(state, letter, top, (1, pos))))
            elif bottom in occupied:
                for pos in WAITING_SPOTS:
                    if not any([(1, y) in occupied for y in range(min(pos, col), max(pos, col)+1)]):
                        letter = occupied[bottom]
                        result.append((move_cost(letter, bottom, (1, pos)), new_state(state, letter, bottom, (1, pos))))   
            
        for pos, letter in occupied.items():
            if pos in [(1, y) for y in WAITING_SPOTS]:
                top, bottom = ROOMS[LETTER_GOAL[letter]]
                col1 = pos[1]
                col2 = top[1]
                if sum([(1, y) in occupied for y in range(min(col1, col2), max(col1, col2)+1)]) == 1:
                    if top not in occupied and bottom not in occupied:
                        result.append((move_cost(letter, pos, bottom), new_state(state, letter, pos, bottom)))
                    elif top not in occupied and occupied[bottom] == letter:
                        result.append((move_cost(letter, pos, top), new_state(state, letter, pos, top)))

        return result
    
    # for cost, state in expand(start):
    #     print(cost)
    #     print_state(state)        
            
    path = a_star(start, goal, expand)        
    print(path)
    for state in path[1]:
        print_state(state)
        print()
    return path[0]

def solve2(d):
    d = "\n".join(d.splitlines()[:3] + ["  #D#C#B#A#  ", "  #D#B#A#C#  "] + d.splitlines()[3:])
    print(d)
    start = state_from_inp(d)
    goal = state_from_inp(NEW_GOAL)
    
    def new_state(state, letter, start, goal):
        new_state = set(state)
        new_state.remove((start, letter))
        new_state.add((goal, letter))
        return frozenset(new_state)
    
    def move_cost(letter, start, goal):
        # print(start, goal)
        return pdist1(start, goal) * COSTS[letter]
    
    def expand(state):
        nonlocal move_cost, new_state
        result = []
        
        occupied = {pos: letter for pos, letter in state}
        for top, midtop, midbottom, bottom in NEW_ROOMS:
            col = top[1]
            if top in occupied:
                for pos in WAITING_SPOTS:
                    if not any([(1, y) in occupied for y in range(min(pos, col), max(pos, col)+1)]):
                        letter = occupied[top]
                        result.append((move_cost(letter, top, (1, pos)), new_state(state, letter, top, (1, pos))))
            elif midtop in occupied:
                for pos in WAITING_SPOTS:
                    if not any([(1, y) in occupied for y in range(min(pos, col), max(pos, col)+1)]):
                        letter = occupied[midtop]
                        result.append((move_cost(letter, midtop, (1, pos)), new_state(state, letter, midtop, (1, pos))))   
            elif midbottom in occupied:
                for pos in WAITING_SPOTS:
                    if not any([(1, y) in occupied for y in range(min(pos, col), max(pos, col)+1)]):
                        letter = occupied[midbottom]
                        result.append((move_cost(letter, midbottom, (1, pos)), new_state(state, letter, midbottom, (1, pos))))   
            elif bottom in occupied:
                for pos in WAITING_SPOTS:
                    if not any([(1, y) in occupied for y in range(min(pos, col), max(pos, col)+1)]):
                        letter = occupied[bottom]
                        result.append((move_cost(letter, bottom, (1, pos)), new_state(state, letter, bottom, (1, pos))))   
            
        for pos, letter in occupied.items():
            if pos in [(1, y) for y in WAITING_SPOTS]:
                top, midtop, midbottom, bottom = NEW_ROOMS[LETTER_GOAL[letter]]
                col1 = pos[1]
                col2 = top[1]
                # print(top, midtop, midbottom, bottom)
                # print_state(state)
                # print([cell not in occupied for cell in [top, midtop, midbottom, bottom]])
                # print([occupied[cell] if cell in occupied else " - " for cell in [top, midtop, midbottom, bottom]])
                if sum([(1, y) in occupied for y in range(min(col1, col2), max(col1, col2)+1)]) == 1:
                    if all([cell not in occupied for cell in [top, midtop, midbottom, bottom]]):
                        result.append((move_cost(letter, pos, bottom), new_state(state, letter, pos, bottom)))
                    elif all([cell not in occupied for cell in [top, midtop, midbottom]]):
                        if occupied[bottom] == letter:
                            result.append((move_cost(letter, pos, midbottom), new_state(state, letter, pos, midbottom)))
                    elif all([cell not in occupied for cell in [top, midtop]]):
                        if all([cell in occupied and occupied[cell] == letter for cell in [midbottom, bottom]]):
                            result.append((move_cost(letter, pos, midtop), new_state(state, letter, pos, midtop)))
                    elif top not in occupied:
                        if all([cell in occupied and occupied[cell] == letter for cell in [midtop, midbottom, bottom]]):
                            result.append((move_cost(letter, pos, top), new_state(state, letter, pos, top)))

        return result
    
    # for cost, state in expand(start):
    #     print(cost)
    #     print_state(state)        
            
    path = a_star(start, goal, expand)        
    print(path)
    for state in path[1]:
        print_state(state)
        print()
    return path[0]


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
# print("Example Solution:", solve1(s))
# # print("Example 2 Solution:", solve1(s2))
# print("Actual Solution:", solve1(inp))

print("PART 2")
print("Example Solution:", solve2(s))
# print("Example 2 Solution:", solve2(s2))
print("Actual Solution:", solve2(inp))
