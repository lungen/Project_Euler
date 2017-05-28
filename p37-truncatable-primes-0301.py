"""
Truncatable primes
Problem 37
The number 3797 has an interesting property. Being prime itself,
it is possible to continuously remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable
from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

import _tools


dataSet = set(_tools.load_it("primeList_1million.txt"))
print("len set datalist: ", len(dataSet))


def truncPrimes(primeList):

    l = []
    nok = '014689'
    sum = 0

    for p in primeList:
        if len(l) >= 11:
            break
        if len(p) == 1:
            continue
        if p == 1:
            continue
        if (p[0] in nok) or (p[-1] in nok):
            continue

        found, i = True, 1
        while i < len(p) and found:
            if not p[i:] in primeList:
                found = False
            i += 1

        foundTwo, j = True, len(p)
        while j > 0 and found and foundTwo:
            if not p[:j] in primeList:
                foundTwo = False
            j -= 1

        if found and foundTwo:
            sum += int(p)
            l.append(p)

    return sum


tp = truncPrimes(dataSet)
print(tp)
