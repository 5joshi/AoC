from utils import *

YEAR, DAY = ints(__file__)
inp = get_data(year=YEAR, day=DAY)

DOOR = s_to_grid("""789
456
123
 0A""")
 
ROBOT = s_to_grid(""" ^A
<v>""")

def solve1(d):
    codes = d.splitlines()
    result = 0
    
    for code in codes:
        coords = lmap(lambda c: DOOR.find(c), code)
        
        def go(frm, to, door=False):
            if frm == to: return ["A"]
            delta = lsub(to, frm)
            result = ""
            while delta[0] < 0:
                delta[0] += 1
                result += "^"
            while delta[0] > 0:
                delta[0] -= 1
                result += "v"
            while delta[1] < 0:
                delta[1] += 1
                result += "<"
            while delta[1] > 0:
                delta[1] -= 1
                result += ">"
                
            return [result + "A", result[::-1] + "A"]
        
        def check_ext(frm, ext, door=False):
            curr=frm
            for c in ext[:-1]:
                curr=tadd(curr, CTD[c])
                if (door and DOOR[curr]) == " " or (not door and ROBOT[curr] == " "):
                    return False
            return True
        
        paths = {p for p in go(DOOR.find('A'), coords[0]) if check_ext(DOOR.find('A'), p, door=True)}
        for frm, to in windows(coords, 2):
            paths = {path + ext for path in paths for ext in go(frm, to) if check_ext(frm, ext, door=True)}
            
        # print(paths)
        def cost(path):
            result = 0
            for c, nc in windows("A" + path, 2):
                result += dist1(ROBOT.find(c), ROBOT.find(nc))
            return result
        
                
                
            
        for i in range(2):
            new_paths = set()
            # prune paths
            best_cost = min(cost(path) for path in paths)
            paths = {path for path in paths if cost(path) == best_cost}
            # print(paths)
            for path in paths:
                coords = lmap(lambda c: ROBOT.find(c), path)
                curr_paths = {p for p in go(ROBOT.find('A'), coords[0]) if check_ext(ROBOT.find('A'), p)}
                for frm, to in windows(coords, 2):
                    curr_paths = {path + ext for path in curr_paths for ext in go(frm, to) if check_ext(frm, ext)}
                new_paths |= curr_paths
            paths = new_paths
    
        # print(len(min(paths, key=len)), ints(code)[0], min(paths, key=len))
        result += len(min(paths, key=len)) * ints(code)[0]
        
    return result

def solve2(d):
    codes = d.splitlines()
    result = 0
    
    for code in codes:
        coords = lmap(lambda c: DOOR.find(c), code)
        
        def go(frm, to):
            if frm == to: return ["A"]
            delta = lsub(to, frm)
            result = ""
            while delta[0] < 0:
                delta[0] += 1
                result += "^"
            while delta[0] > 0:
                delta[0] -= 1
                result += "v"
            while delta[1] < 0:
                delta[1] += 1
                result += "<"
            while delta[1] > 0:
                delta[1] -= 1
                result += ">"
                
            return [result + "A", result[::-1] + "A"]
        
        def check_ext(frm, ext):
            curr=frm
            for c in ext[:-1]:
                curr=tadd(curr, CTD[c])
                if DOOR[curr] == " ":
                    return False
            return True
        
        paths = {p for p in go(DOOR.find('A'), coords[0]) if check_ext(DOOR.find('A'), p)}
        for frm, to in windows(coords, 2):
            paths = {path + ext for path in paths for ext in go(frm, to) if check_ext(frm, ext)}
            
        # print(paths)
        def cost(path):
            result = 0
            for c, nc in windows("A" + path, 2):
                result += dist1(ROBOT.find(c), ROBOT.find(nc))
            return result
        
        best_cost = min(cost(path) for path in paths)
        paths = {path for path in paths if cost(path) == best_cost}
          
        @lru_cache      
        def go(frm, to):
            if frm == to: return "A"
            if frm == 'v':
                if to == 'A': return "^>A"
                return f"{to}A"
            elif frm == '^':
                if to == 'A': return ">A"
                return f"v{go('v', to)}"
            elif frm == '<':
                if to == 'A': return ">>^A"
                return f">{go('v', to)}"
            elif frm == '>':
                if to == 'A': return "^A"
                return f"<{go('v', to)}"
            
            if to == '^': return "<A"
            elif to == '>': return "vA"
            elif to == 'v': return "<vA"
            return "v<<A"        
            
        # print(paths)
        results = []
        for path in paths:
            pairs = Counter(windows("A" + path, 2))
            for i in range(25):
                new_pairs = Counter()
                for (a, b), count in pairs.items():
                    for pair in windows("A" + go(a, b), 2):
                        new_pairs[pair] += count
                pairs = new_pairs
            # print(code, sum(pairs.values()), ints(code)[0], sum(pairs.values()) * ints(code)[0])
            results.append(sum(pairs.values()) * ints(code)[0])
        # print(results, min(results))
        result += min(results)
        # print(result)
            
            # paths = {"".join(go(a, b) for a, b in windows('A' + path, 2)) for path in paths}
            # for path in paths:
            #     curr_paths = go('A', path[0])
            #     for frm, to in windows(coords, 2):
            #         curr_paths = {path + ext for path in curr_paths for ext in go(frm, to) if check_ext(frm, ext)}
            #     new_paths |= curr_paths
            # paths = new_paths
            # print(paths)
    
        # print(len(min(paths, key=len)), ints(code)[0], min(paths, key=len))
        # result += len(min(paths, key=len)) * ints(code)[0]
        
    return result


s = """
029A
980A
179A
456A
379A
""".strip()
s2 = """
029A
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