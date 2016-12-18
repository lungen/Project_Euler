# http://stackoverflow.com/questions/8002252/euler-project-18-approach

import pprint

t = """\
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23\
"""

lmax = []

tri = list(reversed([(map(int, line.split(" "))) for line in t.split("\n")]))
"""
for idx, row in enumerate(tri):
    # print(idx, row[idx])
    for x, pos in enumerate(row):
        # print(idx, x, pos, tri[idx][x], row[x])
"""

for idx, row in enumerate(tri[1:], 1):
    # print(row)
    for dx, nr in enumerate(row):
        tri[idx][dx] = (tri[idx][dx] + max(tri[idx - 1][dx], tri[idx - 1][dx + 1]))
        # print(tri[idx][dx] + max(tri[idx - 1][dx], tri[idx - 1][dx + 1]))
        # print(tri[idx - 1][dx], tri[idx - 1][dx + 1])
        # print(max(tri[idx - 1][dx], tri[idx - 1][dx + 1]))
for n in tri:
    print(n)
