from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

class State:
    def __init__(self, floors, elevator=0):
        self.floors = floors
        self.elevator = elevator
        self.steps = 0
        
    def expand(self):
        for i in range(1, min(len(self.floors[self.elevator]) + 1, 3)):
            for c in it.combinations(self.floors[self.elevator], i):
                for d in [-1, 1]:
                    if (self.elevator + d) < 0 or (self.elevator + d) >= len(self.floors):
                        continue
                    new_floors = deepcopy(self.floors)
                    new_floors[self.elevator + d].extend(c)
                    new_floors[self.elevator] = [x for x in self.floors[self.elevator] if x not in c]
                    new_state = State(new_floors, self.elevator + d)
                    if new_state.valid():
                        yield new_state

    def valid(self):
        for floor in self.floors:
            chips = [x for x in floor if x[1] == 'M']
            for chip in chips:
                if (chip[0], 'G') not in floor and any([x[1] == 'G' for x in floor]):
                    return False
        return True
    
    def __repr__(self):
        result = "\n"
        idx = 4
        for floor in reversed(self.floors):
            result += f"Floor {idx}: "
            items = ""
            for element, typ in floor:
                if typ == 'G' and (element, 'M') in floor:
                    result += "match "
                elif typ == 'G':
                    items = f"G " + items
                elif typ == 'M' and (element, 'G') not in floor:
                    items += f" M" 
            result += items + ('<----' if idx - 1 == self.elevator else '') + '\n'
                
            # result += f"Floor {idx}: {str(sorted(floor))} {'<---' if idx - 1 == self.elevator else ''}\n"
            idx -= 1
        return result
    
    def __hash__(self):
        return hash(str(self))
    
    def __eq__(self, other):
        return str(self) == str(other)
    
    def __lt__(self, other):
        return sum(len(x) * (4 - idx) for idx, x in enumerate(self.floors)) < sum(len(x) * (4 - idx) for idx, x in enumerate(other.floors))

def solve1(d):
    lines = d.splitlines()
    floors = []
    
    for line in lines:
        floor = []
        for match in re.findall('(\w+) generator', line):
            floor.append((match, 'G'))
        for match in re.findall('(\w+)-compatible microchip', line):
            floor.append((match, 'M'))
        floors.append(floor)
        
    def expand(state):
        for new in state.expand():
            yield new
    
    goal = State([[], [], [], flatten(floors)], 3)
    dists, _ = bfs(State(floors), expand, goal)
    return dists[goal]

def solve2(d):
    lines = d.splitlines()
    floors = []
    
    for line in lines:
        floor = []
        for match in re.findall('(\w+) generator', line):
            floor.append((match, 'G'))
        for match in re.findall('(\w+)-compatible microchip', line):
            floor.append((match, 'M'))
        floors.append(floor)
        
    floors[0].extend([('elerium', 'G'), ('elerium', 'M'), ('dilithium', 'G'), ('dilithium', 'M')])

    def expand(state):
        for new in state.expand():
            yield (1, new)
            
    goal = State([[], [], [], flatten(floors)], 3)
    result, _ = a_star(from_node=State(floors), expand=expand, to_node=goal)
    return result


s = """
The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant.

""".strip()
s2 = """

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