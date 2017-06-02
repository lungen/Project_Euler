"""
Integer right triangles
Problem 39
If p is the perimeter of a right angle triangle with integral length sides,
 {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""
p = 20
lim = 60
l = []
ll = []


while p <= 130:

    for a in range(1, lim):
        for b in range(1, lim):
            for c in range(1, lim):
                #if a + b + c == p:
                if a + b + c == p:
                    if a * a + b * b == c * c:
                        #print(a, b, c, p)
                        if sorted([a, b, c]) not in l:
                            l.append([p, sorted([a, b, c])])
    p += 1

print(l)
print(len(l))

