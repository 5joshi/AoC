from utils import *

inp = get_data(year=2023, day=2)

def solve1(d):
    inp = lmap(words_and_ints, d.splitlines())
    result = 0
    
    for game in inp:
        colors = defaultdict(int)
        
        for num, color in every_n(game[2:], 2):
            colors[color] = max(colors[color], num)
            
        result += game[1] if (colors['red'] <= 12 and colors['green'] <= 13 and colors['blue'] <= 14) else 0
    
    return result

def solve2(d):
    inp = lmap(words_and_ints, d.splitlines())
    result = 0
    
    for game in inp:
        colors = defaultdict(int)
        
        for num, color in every_n(game[2:], 2):
            colors[color] = max(colors[color], num)
            
        result += reduce(operator.mul, colors.values(), 1)
    
    return result


s = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""".strip()
s2 = """

""".strip()

if __name__ == '__main__':
    e1, e2, ex1, ex2, r1, r2 = get_solution_booleans(sys.argv)
            
    if e1 or ex1 or r1: print("PART 1")
    if e1: print("Example Solution:", solve1(s))
    if ex1: print("Example 2 Solution:", solve1(s2))
    if r1: print("Actual Solution:", solve1(inp))

    if e2 or ex2 or r2: print("PART 2")
    if e2: print("Example Solution:", solve2(s))
    if ex2: print("Example 2 Solution:", solve2(s2))
    if r2: print("Actual Solution:", solve2(inp))
