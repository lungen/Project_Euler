"""
Goldbach's other conjecture

  Problem 46
  Difficulty rating: 5%

   It was proposed by Christian Goldbach that every odd composite number can be
   written as the sum of a prime and twice a square.

   9 = 7 + 2×1^2
   15 = 7 + 2×2^2
   21 = 3 + 2×3^2
   25 = 7 + 2×3^2
   27 = 19 + 2×2^2
   33 = 31 + 2×1^2

   It turns out that the conjecture was false.

   What is the smallest odd composite that cannot
   be written as the sum of a prime
   and twice a square?
"""

from _eulertools import isPrime


def makeNumbers(stop=11):
    i = 9
    lim = stop

    while i <= lim:
        if not isPrime(i):
            yield int(i)
        i += 2


def makePrimes(stop=12):
    i = 2
    while i <= stop:
        if isPrime(i):
            yield i
        i += 1


u = 9000
# create odd composite numbers
l = list(makeNumbers(u))

# create prime numbers
pn = list(makePrimes(u))

# add checked prime numbers
reml = []

stop = False

for odd in l:

    i = 0
    while i < len(pn) and not stop:
        # if prime number higher than odd number; break
        if pn[i] >= odd:
            break

        p = 1
        while p <= 40 and not stop:
            # if power number higher than odd number; break
            if 2 * pow(p, 2) >= odd:
                break

            if odd == pn[i] + 2 * pow(p, 2):
                stop = True
                reml.append(odd)  # add checked odd number
                break

            p += 1
        i += 1
    stop = False

# show differences
print(set(l) - set(reml))
