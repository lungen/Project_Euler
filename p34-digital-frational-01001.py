#SOLUTION FOUND IN FORUM:
def findFact():
	facts = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
	limit = 362880 * 9
	for i in xrange(0, limit):
		total = 0
		stringI = str(i)
		for j in stringI:
			total += facts[int(j)]
		if (total == i):
			print i


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

