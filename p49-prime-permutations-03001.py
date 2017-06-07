# -*- coding: utf-8 -*-

import time
import itertools as it


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


start = time.time()
startTime = time.strftime("%H:%M:%S")
print("go: ", startTime)

lim = 9999
s = 3330

# create prime numbers
pn = [i for i in range(1001, lim + 1, 2) if isPrime(i)]
print("list of primes: ", len(pn))

# loop through list of primes; make permutations for every prime;
j = 0
stop = False
while j < len(pn):
    # create list ONLY of permutations-primes
    p = set(int("".join(x)) for x in it.permutations(str(pn[j]))
            if int("".join(x)) in pn)

    # check for increasing sequence; if yes; check if is in permutation list
    r = pn[j] + s
    if r in p:
        rr = pn[j] + 2 * s
        if rr in p:
            print("bingo", pn[j], r, rr)
    j += 1

end = time.time()
endTime = time.strftime("%H:%M:%S")
print("start time: ", startTime)
print("fin time:", endTime)
print("ticks : ", end)
