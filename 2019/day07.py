import collections as coll
import datetime as dt
import functools as ft
import itertools as it
import math
from operator import itemgetter as ig
import pprint as pp
import re
from copy import deepcopy
from utils import *
from functools import reduce
from aocd import get_data, submit

inp = get_data(year=2019, day=7)


def computer(program, inputs):
    inp = ints(program)
    input_idx = 0
    idx = 0
    
    def get_value(value, mode):
        if mode == "0":
            return inp[value]
        elif mode == "1":
            return value
        
    while inp[idx] != 99:
        opcode = str(inp[idx]).zfill(5)
        if opcode[-2:] == "01":
            pos1, pos2, pos3 = inp[idx+1:idx+4]
            inp[pos3] = get_value(pos1, opcode[-3]) + get_value(pos2, opcode[-4])
            idx += 4
        elif opcode[-2:] == "02":
            pos1, pos2, pos3 = inp[idx+1:idx+4]
            inp[pos3] = get_value(pos1, opcode[-3]) * get_value(pos2, opcode[-4])
            idx += 4
        elif opcode[-2:] == "03":
            pos1 = inp[idx+1]
            inp[pos1] = int(inputs[input_idx])
            input_idx += 1
            # inp[pos1] = int(input("Required input..."))
            idx += 2
        elif opcode[-2:] == "04":
            pos1 = inp[idx+1]
            value = get_value(pos1, opcode[-3])
            print(value)
            if value != 0:
                return value
            # print(get_value(pos1, opcode[-3]))
            idx += 2
        elif opcode[-2:] == "05":
            pos1, pos2 = inp[idx+1:idx+3]
            if get_value(pos1, opcode[-3]) != 0:
                idx = get_value(pos2, opcode[-4])
            else:
                idx += 3
        elif opcode[-2:] == "06":
            pos1, pos2 = inp[idx+1:idx+3]
            if get_value(pos1, opcode[-3]) == 0:
                idx = get_value(pos2, opcode[-4])
            else:
                idx += 3
        elif opcode[-2:] == "07":
            pos1, pos2, pos3 = inp[idx+1:idx+4]
            inp[pos3] = get_value(pos1, opcode[-3]) < get_value(pos2, opcode[-4])
            idx += 4
        elif opcode[-2:] == "08":
            pos1, pos2, pos3 = inp[idx+1:idx+4]
            inp[pos3] = get_value(pos1, opcode[-3]) == get_value(pos2, opcode[-4])
            idx += 4
    
    opcode = str(inp[idx-2]).zfill(5)
    if opcode[-2:] == "04":
        return get_value(inp[idx-1], opcode[-3])



def solve1(d):
    def thruster_signal(sequence):
        signal = 0
        for amplifier in sequence:
            # print(amplifier, signal)
            signal = computer(d, [amplifier, signal])
        return signal
       
    best_seq = max(it.permutations(range(5)), key=thruster_signal)        
    return thruster_signal(best_seq), best_seq

def solve2(d):
    def thruster_signal(sequence):
        print(sequence)
        signal = final_signal = 0
        while True:
            for amplifier in sequence:
                signal = computer(d, [amplifier, signal])
                if signal is None: return final_signal
            final_signal = signal
       
    best_seq = max(it.permutations(range(5, 10)), key=thruster_signal)        
    return thruster_signal(best_seq), best_seq


s = """3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0
"""
s2 = """3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0
"""
s3 = """3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5
"""
s4 = """3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10
"""


print("PART 1")
print("Example Solution:", solve1(s))
print("Example 2 Solution:", solve1(s2))
print("Actual Solution:", solve1(inp))

print("PART 2")
print("Example Solution:", solve2(s3))
print("Example 2 Solution:", solve2(s4))
print("Actual Solution:", solve2(inp))