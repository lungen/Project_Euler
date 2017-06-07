# -*- coding: utf-8 -*-

def isPrime(x):
    n = abs(int(x))

    if n < 2:
        return True
    if n == 2:
        return True

    # check if even number
    if not n & 1:
        return False

    for i in range(3, int((n ** 0.5)) + 1, 2):
        if not n % i:
            return False

    return True


import time
import itertools as it


start = time.time()
startTime = time.strftime("%H:%M:%S")

print("go: ", startTime)

lim = 9999
s = 3330

# create permutation
#per = list(itertools.permutations('1234'))
#per = ["".join(x) for x in per]

#print(per)
# create prime numbers 
pn = [i for i in range(1001, lim + 1, 2)  if isPrime(i)]
print(len(pn))
#print(pn)

j = 0
stop = False
while j < len(pn):
    p = list(it.permutations(str(pn[j])))
    p = [int("".join(x)) for x in p]
    p =[x for x in p if x in pn]
    #print(p)
    r = pn[j] + s
    if r in p:
        #print("found: ", pn[j], r)
        rr = pn[j] + 2 * s
        if rr in p:
            print("bingo", pn[j], r, rr)
    j += 1



end = time.time()
endTime = time.strftime("%H:%M:%S")
print("start time: ", startTime)
print("fin time:", endTime) 
print("minutes : ", (end))

