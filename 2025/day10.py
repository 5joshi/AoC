from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    lines = d.splitlines()
    result = 0
    
    for line in lines:
        to = tuple([c == '#' for c in line.split()[0][1:-1]])
        options = line.split()[1:-1]
        options = lmap(ints, options)
        
        def expand(state):
            out = []
            for option in options:
                new_state = list(state)
                for idx in option:
                    new_state[idx] = not new_state[idx]
                out.append((1, tuple(new_state)))
            return out
    
        result += a_star(tuple([False] * len(to)), expand, to_node=to)[0]
            
    
    return result

from z3 import *

def solve2(d):
    lines = d.splitlines()
    result = 0
    
    for line in lines:
        target = tuple(ints(line.split()[-1]))
        buttons = lmap(ints, line.split()[1:-1])
        
        solver = Optimize()
        button_vars = [Int(f'button_{i}') for i in range(len(buttons))]
        
        for b in button_vars:
            solver.add(b >= 0)
        
        for idx, target_num in enumerate(target):
            relevant_buttons = []
            for button_idx, button in enumerate(buttons):
                if idx in button:
                    relevant_buttons.append(button_vars[button_idx])
            solver.add(Sum(relevant_buttons) == target_num)
        
        solver.minimize(Sum(button_vars))
        if solver.check() == sat:
            model = solver.model()
            result += sum([model.evaluate(b).as_long() for b in button_vars])
            
    return result

s = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}

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