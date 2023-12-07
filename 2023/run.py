from utils import Grid
from pprint import pprint
from time import time
from utils import avg
import sys

CURR_DAY = 7

if __name__ == '__main__':
    solutions = []
    time_idx = sys.argv.index('time') if 'time' in sys.argv else len(sys.argv)
    days = [int(x) for x in sys.argv[1:time_idx] if x.isnumeric()]
    if not days: days = range(1, CURR_DAY + 1)
    inp_name = 's' if 'ex' in sys.argv else 'inp'
    
    
    for day in days:
        if 'time' not in sys.argv:
            exec(f"from day{day:02} import {inp_name}, solve1, solve2\npt1 = solve1({inp_name})\npt2 = solve2({inp_name})")
            solutions.append((day, pt1, pt2))  
        elif 'time' in sys.argv:
            samples = 100 if len(sys.argv) == time_idx + 1 else int(sys.argv[-1])
            pt1_times = []
            pt2_times = []
            for _ in range(samples):
                exec(f"from day{day:02} import {inp_name}, solve1, solve2")
                start = time()
                exec(f"solve1({inp_name})")
                mid = time()
                exec(f"solve2({inp_name})")
                end = time()
                pt1_times.append(mid - start)
                pt2_times.append(end - mid)
            solutions.append((day, f"{avg(pt1_times) * 1000:0.3f}ms", f"{avg(pt2_times) * 1000:0.3f}ms"))
        
    print(f"{'Part 1':>18}{'Part 2':>12}")
    print("-" * 30)
    for day, pt1, pt2 in solutions:
        print(f"Day {day:02}: {pt1:>10} |{pt2:>10}")