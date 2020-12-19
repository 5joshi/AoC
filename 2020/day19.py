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

inp = get_data(day=19)


# THIS DOESNT ACTUALLY SOLVE THE PROBLEM, INSTEAD IT GENERATES A JSON FILE
# WHICH I CAN USE IN MY ALREADY IMPLEMENTED C++ CFG, THEN I SIMPLY PERFORM CYK ALGORITHM ON ALL THE WORDS

def solve(d):
    inp = d.split("\n\n")[0].splitlines()
    cfg = coll.defaultdict(set)
    for line in inp:
        key, rules = line.split(':')
        rules = rules.strip()
        if '|' in line:
            rules = rules.split('|')
        else:
            rules = [rules, ""]
        for rule in rules:
            int_rule = tuple(ints(rule))
            if int_rule:
                cfg[key].add(int_rule)
            elif rule:
                cfg[key].add(tuple(words(rule)))
    file = open("test.json", "w")
    file.write("{\n\t")
    file.write("\"Variables\": " + str(cfg.keys()).replace("dict_keys(",
                                                           "").replace(")", "").replace("'", "\"") + ",\n\t")
    file.write("\"Terminals\": [\"a\", \"b\"],\n\t")
    file.write("\"Productions\": [\n\t\t")
    for key in cfg:
        for rule in cfg[key]:
            file.write("{\"head\": \"" + key + "\", \"body\": " +
                       str(lmap(str, rule)).replace("'", "\"") + "},\n\t\t")
    return


s = """116: 1 18 | 111 47
21: 45 47 | 110 18
20: 2 47 | 76 18
44: 47 47 | 18 18 | 18 47
2: 47 18 | 18 47 | 47 47
113: 51 47 | 35 18
80: 18 22 | 47 44
110: 18 18 | 47 18 | 47 47
1: 22 18 | 112 47
77: 47 7 | 18 113
16: 121 47 | 2 18
66: 91 18 | 58 47
86: 12 18 | 78 47
72: 18 76 | 47 121
46: 47 68 | 18 82
131: 66 18 | 75 47
108: 84 18 | 24 47
27: 22 47 | 110 18
53: 108 18 | 122 47
90: 77 47 | 37 18
6: 18 29 | 47 52
10: 76 18 | 44 47
43: 47 39 | 18 130
106: 18 112 | 47 110
89: 97 47 | 51 18
84: 112 18
91: 74 47 | 110 18
114: 18 47 | 18 18 | 47 18
105: 26 18 | 118 47
18: "b"
19: 2 47 | 22 18
15: 34 47 | 2 18
111: 110 47 | 22 18
94: 47 95 | 18 57
34: 18 18 | 47 47 | 18 47 | 47 18
60: 47 114 | 18 121
62: 44 47 | 45 18
50: 38 47 | 103 18
61: 18 44 | 47 110
87: 112 18 | 112 47
31: 18 49 | 47 25
57: 18 20 | 47 60
103: 18 67 | 47 40
39: 18 45 | 47 22
128: 112 18 | 13 47
5: 45 47 | 44 18
13: 18 18
3: 47 10 | 18 80
11: 42 31
124: 22 18
88: 18 18 | 47 18
54: 32 18 | 129 47
63: 81 18 | 86 47
49: 18 132 | 47 105
102: 10 18 | 120 47
93: 18 44 | 47 34
65: 18 2 | 47 2
132: 83 47 | 14 18
125: 18 43 | 47 71
109: 47 22 | 18 76
117: 18 112 | 47 22
59: 47 22 | 18 13
75: 18 109 | 47 27
4: 47 90 | 18 69
48: 18 65 | 47 115
24: 18 2 | 47 44
42: 47 50 | 18 4
96: 106 47 | 16 18
101: 111 47 | 91 18
58: 47 76 | 18 73
79: 47 73 | 18 22
12: 47 34 | 18 88
25: 33 47 | 55 18
130: 18 114 | 47 44
83: 126 18 | 102 47
45: 47 18
9: 41 18 | 62 47
78: 112 18 | 45 47
14: 3 47 | 85 18
97: 47 45 | 18 22
22: 18 47
41: 18 22 | 47 112
112: 18 47 | 18 18
68: 21 18 | 19 47
121: 47 47 | 18 18
119: 22 47
129: 47 5 | 18 39
30: 73 18 | 2 47
98: 34 18 | 45 47
40: 18 70 | 47 9
7: 64 47 | 79 18
115: 121 47 | 44 18
32: 19 47 | 30 18
73: 18 47 | 47 18
35: 18 76 | 47 45
95: 93 18 | 72 47
52: 28 47 | 124 18
126: 59 18 | 92 47
26: 104 18 | 89 47
81: 47 98 | 18 127
0: 42 11
64: 112 47
71: 47 119 | 18 117
74: 47 47
82: 47 120 | 18 17
56: 74 47 | 88 18
123: 88 47 | 76 18
33: 6 18 | 63 47
104: 80 18 | 128 47
99: 98 18 | 23 47
38: 94 18 | 53 47
36: 47 110 | 18 74
37: 47 48 | 18 101
70: 61 47 | 87 18
55: 47 54 | 18 131
23: 2 47 | 112 18
122: 10 47 | 64 18
120: 88 18 | 112 47
28: 18 112 | 47 73
51: 47 74 | 18 110
17: 47 88 | 18 22
127: 18 73 | 47 45
69: 125 18 | 46 47
92: 2 47 | 114 18
29: 117 18 | 56 47
67: 18 96 | 47 116
85: 18 36 | 47 15
100: 18 123 | 47 12
47: "a"
118: 100 47 | 99 18
76: 47 47 | 47 18"""
s2 = """116: 1 18 | 111 47
21: 45 47 | 110 18
20: 2 47 | 76 18
44: 47 47 | 18 18 | 18 47
2: 47 18 | 18 47 | 47 47
113: 51 47 | 35 18
80: 18 22 | 47 44
110: 18 18 | 47 18 | 47 47
1: 22 18 | 112 47
77: 47 7 | 18 113
16: 121 47 | 2 18
66: 91 18 | 58 47
86: 12 18 | 78 47
72: 18 76 | 47 121
46: 47 68 | 18 82
131: 66 18 | 75 47
108: 84 18 | 24 47
27: 22 47 | 110 18
53: 108 18 | 122 47
90: 77 47 | 37 18
6: 18 29 | 47 52
10: 76 18 | 44 47
43: 47 39 | 18 130
106: 18 112 | 47 110
89: 97 47 | 51 18
84: 112 18
91: 74 47 | 110 18
114: 18 47 | 18 18 | 47 18
105: 26 18 | 118 47
18: "b"
19: 2 47 | 22 18
15: 34 47 | 2 18
111: 110 47 | 22 18
94: 47 95 | 18 57
34: 18 18 | 47 47 | 18 47 | 47 18
60: 47 114 | 18 121
62: 44 47 | 45 18
50: 38 47 | 103 18
61: 18 44 | 47 110
87: 112 18 | 112 47
31: 18 49 | 47 25
57: 18 20 | 47 60
103: 18 67 | 47 40
39: 18 45 | 47 22
128: 112 18 | 13 47
5: 45 47 | 44 18
13: 18 18
3: 47 10 | 18 80
11: 42 31 | 42 99999
124: 22 18
88: 18 18 | 47 18
54: 32 18 | 129 47
63: 81 18 | 86 47
49: 18 132 | 47 105
102: 10 18 | 120 47
93: 18 44 | 47 34
65: 18 2 | 47 2
132: 83 47 | 14 18
125: 18 43 | 47 71
109: 47 22 | 18 76
117: 18 112 | 47 22
59: 47 22 | 18 13
75: 18 109 | 47 27
4: 47 90 | 18 69
48: 18 65 | 47 115
24: 18 2 | 47 44
42: 47 50 | 18 4 | 42 42
96: 106 47 | 16 18
101: 111 47 | 91 18
58: 47 76 | 18 73
79: 47 73 | 18 22
12: 47 34 | 18 88
25: 33 47 | 55 18
130: 18 114 | 47 44
83: 126 18 | 102 47
45: 47 18
9: 41 18 | 62 47
78: 112 18 | 45 47
14: 3 47 | 85 18
97: 47 45 | 18 22
22: 18 47
41: 18 22 | 47 112
112: 18 47 | 18 18
68: 21 18 | 19 47
121: 47 47 | 18 18
119: 22 47
129: 47 5 | 18 39
30: 73 18 | 2 47
98: 34 18 | 45 47
40: 18 70 | 47 9
7: 64 47 | 79 18
115: 121 47 | 44 18
32: 19 47 | 30 18
73: 18 47 | 47 18
35: 18 76 | 47 45
95: 93 18 | 72 47
52: 28 47 | 124 18
126: 59 18 | 92 47
26: 104 18 | 89 47
81: 47 98 | 18 127
0: 42 11
64: 112 47
71: 47 119 | 18 117
74: 47 47
82: 47 120 | 18 17
56: 74 47 | 88 18
123: 88 47 | 76 18
33: 6 18 | 63 47
104: 80 18 | 128 47
99: 98 18 | 23 47
38: 94 18 | 53 47
36: 47 110 | 18 74
37: 47 48 | 18 101
70: 61 47 | 87 18
55: 47 54 | 18 131
23: 2 47 | 112 18
122: 10 47 | 64 18
120: 88 18 | 112 47
28: 18 112 | 47 73
51: 47 74 | 18 110
17: 47 88 | 18 22
127: 18 73 | 47 45
69: 125 18 | 46 47
92: 2 47 | 114 18
29: 117 18 | 56 47
67: 18 96 | 47 116
85: 18 36 | 47 15
100: 18 123 | 47 12
47: "a"
118: 100 47 | 99 18
76: 47 47 | 47 18
99999: 11 31"""


print("Create Part 1 JSON:", solve(s))
print("Create Part 2 JSON:", solve(s2))
# print("Example 2 Solution:", solve(s2))
# print("Actual Solution:", solve(inp))
