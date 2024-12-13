from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

def solve1(d):
    values = sorted(lmap(positive_ints, d.splitlines()))
    sleeptimes = defaultdict(Counter)
    curr = awake = prev = None
    
    for nums in values:
        if len(nums) == 6: 
            curr = nums.pop(5)
            awake = False
        elif not awake:
            sleeptimes[curr].update(range(prev, nums[4]))
        prev = nums[-1]
        awake = not awake
    
    sleepiest = max(sleeptimes, key=lambda x: sum(sleeptimes[x].values()))
    return sleeptimes[sleepiest].most_common(1)[0][0] * sleepiest

def solve2(d):
    values = sorted(lmap(positive_ints, d.splitlines()))
    sleeptimes = defaultdict(Counter)
    curr = awake = prev = None
    
    for nums in values:
        if len(nums) == 6: 
            curr = nums.pop(5)
            awake = False
        elif not awake:
            sleeptimes[curr].update(range(prev, nums[4]))
        prev = nums[-1]
        awake = not awake
    
    sleepiest = max(sleeptimes, key=lambda x: max(sleeptimes[x].values()))
    return sleeptimes[sleepiest].most_common(1)[0][0] * sleepiest


s = """
[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up

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