import math


#d = {'1': 1, '2': 2, '3': 6, '4': 24, '5': 120}
l = []
ll = []
d = {}
res = 0
suma = 0

for i in range(0, 10):
    d[str(i)] = math.factorial(i)

#for i in range(10, 100000001):
for i in range(10, 100001):
    ll = []
    res = 0
    for s in str(i):
        #ll.append((i, res, d[str(s)]))
        res += int(d[str(s)])
        if res > i:
            break
        #print(ll)
    if i == res:
            l.append(i)
            suma += i

print(l)

