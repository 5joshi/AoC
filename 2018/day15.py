from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

ADJ = [CTD['U'], CTD['L'], CTD['R'], CTD['D']]

class Field:
    def __init__(self, data, atk=3):
        self.grid = s_to_grid(data)
        self.goblins = {c: 200 for c in self.grid.findall("G")}
        self.elves = {c: 200 for c in self.grid.findall("E")}
        self.atk = atk
        
    def order(self):
        return sorted(({*self.goblins.keys()} | {*self.elves.keys()}))
    
    def get_move(self, c):
        if c in self.goblins and "E" in self.grid.get_neighbors_values(c, ADJ): return c
        if c in self.elves and "G" in self.grid.get_neighbors_values(c, ADJ): return c
        
        targets = set()
        
        if c in self.goblins: 
            for e in self.elves.keys(): 
                targets |= {n for n in neighbors(e, ADJ) if self.grid[n] == '.'}
        elif c in self.elves:
            for g in self.goblins.keys(): targets |= {n for n in neighbors(g, ADJ) if self.grid[n] == '.'}
        else:
            raise Exception("No unit at this location")
            
        if not targets: return c
        
        def expand(c):
            return [(1, nc) for nc in neighbors(c, ADJ) if self.grid[nc] == "."]
        
        dists, _ = dijkstra(c, expand, to_func=lambda x: x in targets)
        targets = {t for t in targets if t in dists}
        if not targets: return c
        
        target = min(targets, key=lambda x: (dists[x], x))
        rev, _ = dijkstra(target, expand, to_node=c)
        return min(neighbors(c, ADJ), key=lambda x: (rev.get(x, math.inf), x))
        
    def attack(self, c):
        targets = {n for n in neighbors(c, ADJ) if self.grid[n] not in "#." + self.grid[c]}
        if not targets: return
        
        if c in self.goblins:
            target = min(targets, key=lambda x: (self.elves[x], x))
            self.elves[target] -= 3
            if self.elves[target] <= 0:
                del self.elves[target]
                self.grid[target] = "."
        elif c in self.elves:
            target = min(targets, key=lambda x: (self.goblins[x], x))
            self.goblins[target] -= self.atk
            if self.goblins[target] <= 0:
                del self.goblins[target]
                self.grid[target] = "."
        
    def move(self, c, nc):
        if c in self.goblins:
            self.goblins[nc] = self.goblins[c]
            self.grid[c], self.grid[nc] = ".", "G"
            del self.goblins[c]
        elif c in self.elves:
            self.elves[nc] = self.elves[c]
            self.grid[c], self.grid[nc] = ".", "E"
            del self.elves[c]
        else:
            raise Exception("No unit at this location")
        
    def simulate(self):
        for r in it.count(0):
            # print(self.grid)
            # print(self.goblins)
            # print(self.elves)
            for c in self.order():
                if not self.goblins or not self.elves: 
                    return r * (sum(self.goblins.values()) + sum(self.elves.values()))
                if c not in self.goblins and c not in self.elves: continue

                nc = self.get_move(c)
                if c != nc: self.move(c, nc)
                self.attack(nc)

def solve1(d):
    field = Field(d)
    return field.simulate()
    

def solve2(d):
    elves = d.count("E")
    for i in it.count(4):
        field = Field(d, atk=i)
        result = field.simulate()
        if len(field.elves) == elves: return result


s = """
#######
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#
#######
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