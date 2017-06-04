"""
Integer right triangles
Problem 39
If p is the perimeter of a right angle triangle with integral length sides,
 {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""
import math
import operator

lim = 555
d = {}

for i in range(1, lim):
    for j in range(1, lim):
        c = math.sqrt(pow(i, 2) + pow(j, 2))
        if c.is_integer():
            p = i + j + c
            if p not in d:
                d[p] = 1
            else:
                d[p] += 1

# https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
mx = max(d.items(), key=operator.itemgetter(1))[0]
print("p: ", mx, " with solutions: ",  d[mx])
