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

inp = get_data(year=2021, day=4)


class BingoBoard():
    def __init__(self, inp):
        self.board = ints(inp)
        self.grid = [False for _ in range(len(self.board))]

    def get(self, x, y):
        return self.board[x*5 + y]
        
    def get_bool(self, x, y):
        return self.grid[x*5 + y]

    def mark(self, num):
        for idx, number in enumerate(self.board):
            if number == num:
                self.grid[idx] = True
        
    def bingo(self):
        for x in range(5):
            if all([self.get_bool(x, y) for y in range(5)]):
                return True
            if all([self.get_bool(y, x) for y in range(5)]):
                return True
        return False
            

def solve1(d):
    inp = d.split("\n\n")
    nums = ints(inp[0])
    boards = {BingoBoard(s) for s in inp[1:]}
    
    def play_bingo(nums, boards):
        for num in nums:
            for board in boards:
                board.mark(num)
                if board.bingo():
                    return (board, num)
         
    winner, num = play_bingo(nums, boards)
    unmarked = sum([num for (num, marked) in zip(winner.board, winner.grid) if not marked])

    return unmarked * num

def solve2(d):
    inp = d.split("\n\n")
    nums = ints(inp[0])
    boards = {BingoBoard(s) for s in inp[1:]}
    
    def play_bingo(nums, boards):
        winners = []
        for num in nums:
            for board in boards:
                if board in winners: continue
                board.mark(num)
                if board.bingo(): winners += [board]
            if len(winners) == len(boards):
                return (winners[-1], num)
         
    winner, num = play_bingo(nums, boards)
    unmarked = sum([num for (num, marked) in zip(winner.board, winner.grid) if not marked])

    return unmarked * num


s = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""
s2 = """
"""

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
