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


startTime = time.strftime("%H:%M:%S")
print(startTime)

d = {}
start = 1000
lim = 1000000

lp = [x for x in range(1000) if isPrime(x)]
print(len(lp))

sp = set(lp)

# primfaktorzerlegung
for n in range(start, lim):
    if n in sp:
        continue

    i = 0
    stop = False

    while i < len(lp):  # and not stop:
        r = n % lp[i]
        if r == 0:
            #print(m, " % ", lp[i], " = ", r)
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
        i += 1

print(len(d))

lf = sorted([k for k, v in d.items() if v == 4])
print(len(lf))

for idx, ele in enumerate(lf[:-4]):
    if lf[idx] == lf[idx + 1] - 1 and lf[idx] == lf[idx + 2] - 2 \
       and lf[idx] == lf[idx + 3] - 3:
        print("bingo!", lf[idx], lf[idx + 1], lf[idx + 2], lf[idx + 3])

endTime = time.strftime("%H:%M:%S")
print(endTime)
