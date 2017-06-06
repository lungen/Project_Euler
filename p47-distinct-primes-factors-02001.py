"""
Distinct primes factors
Problem 47
The first two consecutive numbers to have two distinct prime factors are:

    14 = 2 × 7
    15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

        644 = 2² × 7 × 23
        645 = 3 × 5 × 43
        646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors
each. What is the first of these numbers?
"""

import time


def isPrime(x):
    n = abs(int(x))

    if n < 2:
        return False
    if n == 2:
        return True

    # check if even number
    if not n & 1:
        return False

    for i in range(3, int((n ** 0.5)) + 1, 2):
        if not n % i:
            return False

    return True

x0 = time.time()
startTime = time.strftime("%H:%M:%S")
print(startTime)

start = 1000
lim = 1000000
stack = [0, 0]
divs = 0

lp = [x for x in range(1000) if isPrime(x)]
sp = set(lp)

# primfaktorzerlegung
for n in range(start, lim):
    if n in sp:
        continue

    i = 0

    while i < len(lp) and lp[i] <= n:
        r = n % lp[i]
        if r == 0:
            #print(n, " % ", lp[i], " = ", r)
            divs += 1
        i += 1

    if divs == 4:
        if n == stack[0] + 1 and stack[1] + 1 == stack[0]:
            print("bingo: ", stack, n)
            stop = True
            break
        else:
            stack.pop()
            stack.insert(0, n)
            divs = 0

x1 = time.time()
endTime = time.strftime("%H:%M:%S")
print(endTime)
print("Seconds: {0}".format((x1 - x0) / (1000 * 60)))
