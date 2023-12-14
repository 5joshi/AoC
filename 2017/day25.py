from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    (state, steps), *rest = lmap(lambda b: b.splitlines(), d.split('\n\n'))
    state = words(state)[-1]
    steps = ints(steps)[-1]
    
    idx = 0
    ones = set()
    for _ in range(steps):
        instr = rest[ord(state) - ord('A')]
        write, delta, state = lmap(words_and_ints, instr[2:5] if idx not in ones else instr[6:])
        if write[-1] == 1: ones |= {idx}
        else: ones -= {idx}
        idx += 1 if delta[-1] == 'right' else -1
        state = state[-1]
    
    return len(ones)


s = """
Begin in state A.
Perform a diagnostic checksum after 6 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state B.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.

""".strip()
s2 = """

""".strip()

if __name__ == '__main__':
    one, two, e1, e2, ex1, ex2, r1, r2 = get_solution_booleans(sys.argv)
            
    if e1 or ex1 or r1: print("PART 1")
    if e1 and s != "": print("Example Solution:", solve1(s))
    if ex1: print("Example 2 Solution:", solve1(s2))
    if r1: print("Actual Solution:", sol1 := solve1(inp))
    
    if (one and r1) or (two and r2):
        go = input('Submit? [y/N] ')
        if go == 'y':
            if one and r1: submit(sol1, part=1, year=YEAR, day=DAY)
