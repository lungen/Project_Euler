"""
Pandigital products
Problem 32

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number,
15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.

brute force:
    biggest number: 9 * 8765432 = 1

                    => 9 * 8765432 = 78888888
                    => lim = 10000 => 10 000 * 10 000 = 100 000 000
"""

import itertools

lp = []
# products can be obtained in more than one way
nok = []
suma = 0
s = '123456789'
lim = 10000

p = list(itertools.permutations(s))
pp = ["".join(x) for x in p]
spp = set(pp)

for i in range(1, lim):
    for j in range(1, lim):
        res = i * j
        sres = "".join((str(i), str(j), str(res)))
        if len(sres) > 9:
            break
        if sres in spp:
            if res not in nok:
                lp.append(sres)
                nok.append(res)
                suma += res

print(lp)
print("len lp: ", len(lp))
print("product: ", suma)
