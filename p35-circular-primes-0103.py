"""
Circular primes
Problem 35
The number, 197, is called a circular prime because all
rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13,
17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

import math
import time
import _tools


def sieveOfEratosthenes(n):

    start = time.time()

    l = list(range(2, n + 1))

    for i in range(2, int(math.sqrt(n))):
        if i in l:
            for j in range(2 * i, n + 1, i):
                if j in l:
                    l.remove(j)

    end = time.time()
    result = end - start
    print("time: {0:5f} seconds." .format(result))
    return l


def circularPrimes(start, limit, primeList):
    # circuit primes
    l = []

    for p in primeList[start:]:
        if int(p) <= limit:
            if len(p) == 1:
                l.append(p)
            else:
                i = 0  # rotate 197, 971, 719
                pp = p
                found = True
                while i < len(p) and found:
                    p = str(p[1:]) + str(p[0])
                    if p not in primeList:
                        found = False
                    i += 1
                if found:
                    l.append(pp)
        else:
            break
    return l


#data = sieveOfEratosthenes(1000000)
#_tools.save_it(data, "primeList_100000.txt")
newData = _tools.load_it("primeList_1million.txt")
res = circularPrimes(0, 1000000, newData)
print("\nfin: ", len(res))
