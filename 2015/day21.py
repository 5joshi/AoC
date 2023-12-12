from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

ITEMS = """
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
"""

def solve1(d):
    hp, dmg, armor = ints(d)
    weapons, armors, rings = lmap(lambda x: [nums[-3:] for l in x.splitlines() if len((nums := ints(l)))], ITEMS.split('\n\n'))
    armors.append([0, 0, 0])
    rings.append([0, 0, 0])
    
    for option in sorted(it.product(weapons, armors, rings, rings), key=lambda c: sum(x[0] for x in c)):
        if len(option) == 4 and option[2] == option[3]: continue
        
        out_dmg = max(sum(x[1] for x in option) - armor, 1)
        in_dmg = max(dmg - sum(x[2] for x in option), 1)
        
        player_turns = (hp + out_dmg - 1) // out_dmg
        boss_turns = (100 + in_dmg - 1) // in_dmg
        
        if player_turns <= boss_turns:
            return sum(x[0] for x in option)

def solve2(d):
    hp, dmg, armor = ints(d)
    weapons, armors, rings = lmap(lambda x: [nums[-3:] for l in x.splitlines() if len((nums := ints(l)))], ITEMS.split('\n\n'))
    armors.append([0, 0, 0])
    rings.append([0, 0, 0])
    
    for option in sorted(it.product(weapons, armors, rings, rings), key=lambda c: sum(x[0] for x in c), reverse=True):
        if len(option) == 4 and option[2] == option[3]: continue
        
        out_dmg = max(sum(x[1] for x in option) - armor, 1)
        in_dmg = max(dmg - sum(x[2] for x in option), 1)
        
        player_turns = (hp + out_dmg - 1) // out_dmg
        boss_turns = (100 + in_dmg - 1) // in_dmg
        
        if player_turns > boss_turns:
            return sum(x[0] for x in option)


s = """

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
    if e2 and s2 != "": print("Example Solution:", solve2(s))
    if ex2: print("Example 2 Solution:", solve2(s2))
    if r2: print("Actual Solution:", sol2 := solve2(inp))
    
    if (one and r1) or (two and r2):
        go = input('Submit? [y/N] ')
        if go == 'y':
            if one and r1: submit(sol1, part=1, year=YEAR, day=DAY)
            if two and r2: submit(sol2, part=2, year=YEAR, day=DAY)