from utils import Grid
from pprint import pprint
from time import time
from utils import avg
import sys

if __name__ == '__main__':
    solutions = []
    for day in range(1, 8):
        if len(sys.argv) == 1:
            exec(f"from day{day:02} import inp, solve1, solve2\npt1 = solve1(inp)\npt2 = solve2(inp)")
            solutions.append((pt1, pt2))  
        elif 'time' in sys.argv[1]:
            samples = 100 if len(sys.argv) == 2 else int(sys.argv[2])
            pt1_times = []
            pt2_times = []
            for _ in range(samples):
                exec(f"from day{day:02} import inp, solve1, solve2")
                start = time()
                exec("solve1(inp)")
                mid = time()
                exec("solve2(inp)")
                end = time()
                pt1_times.append(mid - start)
                pt2_times.append(end - mid)
            solutions.append((f"{avg(pt1_times) * 1000:0.3f}ms", f"{avg(pt2_times) * 1000:0.3f}ms"))
        
    print(f"{'Part 1':>18}{'Part 2':>12}")
    print("-" * 30)
    for idx, (pt1, pt2) in enumerate(solutions):
        print(f"Day {idx+1:02}: {pt1:>10} |{pt2:>10}")