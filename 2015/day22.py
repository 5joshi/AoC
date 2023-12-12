from utils import *
from functools import total_ordering

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)


@total_ordering
class State:
    def __init__(self, hp, mana, boss_hp, boss_dmg, shield=0, poison=0, recharge=0, player_turn=True):
        self.hp = hp
        self.mana = mana
        self.boss_hp = boss_hp
        self.boss_dmg = boss_dmg
        self.shield = shield
        self.poison = poison
        self.recharge = recharge
        self.player_turn = player_turn
        
    def simulate(self, spell=None, p2=False):
        if p2: self.hp -= 1
        
        self.shield = max(self.shield - 1, 0)
        self.poison = max(self.poison - 1, 0)
        self.recharge = max(self.recharge - 1, 0)
        
        if self.player_turn:
            if spell == 'M':
                self.mana -= 53
                self.boss_hp -= 4
            elif spell == 'D':
                self.mana -= 73
                self.boss_hp -= 2
                self.hp += 2
            elif spell == 'S':
                self.mana -= 113
                self.shield = 6
            elif spell == 'P':
                self.mana -= 173
                self.poison = 6
            elif spell == 'R':
                self.mana -= 229
                self.recharge = 5
        else:
            self.hp -= max(self.boss_dmg - (7 if self.shield else 0), 1)

        if self.poison: self.boss_hp -= 3
        if self.recharge: self.mana += 101
        
        self.player_turn = not self.player_turn
        
    def __lt__(self, other):
        return self.boss_hp > other.boss_hp
    
    def __eq__(self, other):
        return self.boss_hp == other.boss_hp
    
    def __hash__(self):
        return hash((self.hp, self.mana, self.boss_hp, self.boss_dmg, self.shield, self.poison, self.recharge, self.player_turn))
    
    def __repr__(self):
        return f"State({self.hp}, {self.mana}, {self.boss_hp}, {self.boss_dmg}, {self.shield}, {self.poison}, {self.recharge}, {self.player_turn})"
                

def solve1(d):
    start = State(50, 500, *ints(d))
    goal = State(50, 500, 0, 0)
    
    def expand(node):
        if node.player_turn:
            result = []
            for spell, cost in zip('MDSPR', [53, 73, 113, 173, 229]):
                new_node = State(*node.__dict__.values())
                new_node.simulate(spell)
                if new_node.hp <= 0 or new_node.mana < 0: continue
                if new_node.boss_hp <= 0: return [(cost, goal)]
                result.append((cost, new_node))
            return result
        else:
            new_node = State(*node.__dict__.values())
            new_node.simulate()
            if new_node.hp <= 0 or new_node.mana < 0: return []
            if new_node.boss_hp <= 0: return [(cost, goal)]
            return [(0, new_node)]
    
    return a_star(start, goal, expand)[0]

def solve2(d):
    start = State(50, 500, *ints(d))
    goal = State(50, 500, 0, 0)
    
    def expand(node):
        if node.player_turn:
            result = []
            for spell, cost in zip('MDSPR', [53, 73, 113, 173, 229]):
                new_node = State(*node.__dict__.values())
                new_node.simulate(spell, p2=True)
                if new_node.hp <= 0 or new_node.mana < 0: continue
                if new_node.boss_hp <= 0: return [(cost, goal)]
                result.append((cost, new_node))
            return result
        else:
            new_node = State(*node.__dict__.values())
            new_node.simulate(p2=True)
            if new_node.hp <= 0 or new_node.mana < 0: return []
            if new_node.boss_hp <= 0: return [(cost, goal)]
            return [(0, new_node)]
    
    return a_star(start, goal, expand)[0]


s = """
13 8
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