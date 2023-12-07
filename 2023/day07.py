from utils import *

inp = get_data(year=2023, day=7)

def hand_tier(hand):
    counter = Counter(hand)
    counts = [counter[x] for x in counter if x != 1]
    if counts.count(2) == 2:
        return 2.5 + counter[1]
    if (3 in counts and 2 in counts):
        return 3.5
    return max(counts + [0]) + counter[1]
        
CARDS_TO_NUMS = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

def solve1(d, cards_to_nums=CARDS_TO_NUMS):
    inp = lmap(lambda l: l.split(), d.splitlines())
    ranks = []
    
    for hand, bid in inp:
        hand = [int(x) if x.isdigit() else cards_to_nums[x] for x in hand]
        value = "".join([f"{x:>02}" for x in hand])
        ranks.append((hand_tier(hand), int(value), int(bid)))
    
    return sum([(rank + 1) * bid for rank, (_, _, bid) in enumerate(sorted(ranks))])

def solve2(d):
    return solve1(d, cards_to_nums={"T": 10, "J": 1, "Q": 12, "K": 13, "A": 14})


s = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""
s2 = """32JJ4 1
32J22 1
33J22 1
JJ332 1
"""

print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve1(s2))
print("Actual Solution:", solve1(inp))

print("PART 2")
print("Example Solution:", solve2(s))
# print("Example 2 Solution:", solve2(s2))
print("Actual Solution:", solve2(inp))
