from utils import *

# inp = get_data(year=2022, day=11)

class Monkey:
    def __init__(self, info):
        monkey, items, operation, test, if_true, if_false = info.splitlines()
        self.id = ints(monkey)[0]
        self.items = ints(items)
        self.operation = lambda old: eval(operation.split(' = ')[1])
        self.divisible_num = ints(test)[0]
        self.test = lambda x: x % self.divisible_num == 0
        self.if_true = ints(if_true)[0]
        self.if_false = ints(if_false)[0]
        self.inspect_count = 0
        
    def give(self, item):
        self.items.append(item)
        
    def inspect(self, monkeys, lcm):
        self.inspect_count += 1
        
        item = self.items.pop(0)
        item = self.operation(item)
        
        if lcm is None: item //= 3
        else: item %= lcm
        result = self.test(item)

        if result: monkeys[self.if_true].give(item)
        else: monkeys[self.if_false].give(item)
        
    def inspect_all(self, monkeys, lcm=None):
        while self.items:
            self.inspect(monkeys, lcm)

def solve1(d):
    monkeys = lmap(lambda info: Monkey(info), d.split("\n\n"))
    
    for _ in range(20):
        for monkey in monkeys:
            monkey.inspect_all(monkeys)
        
    most_active = sorted([monkey.inspect_count for monkey in monkeys])    
    return most_active[-1] * most_active[-2]

def solve2(d):
    monkeys = lmap(lambda info: Monkey(info), d.split("\n\n"))
    lcm = math.lcm(*[monkey.divisible_num for monkey in monkeys])

    for _ in range(10000):
        for monkey in monkeys:
            monkey.inspect_all(monkeys, lcm=lcm)
        
    most_active = sorted([monkey.inspect_count for monkey in monkeys])    
    return most_active[-1] * most_active[-2]


s = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
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
