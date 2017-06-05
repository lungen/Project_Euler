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


l = list(makeNumbers(111))
print(len(l))

pn = list(makePrimes(111))
print(len(pn), " primes.")

for odd in l:
    for primes in pn:
        if primes >= odd:
            #print("nok primes > odd", odd, primes)
            break
        for p in range(1, 10):
            p = p * p
            if 2 * p >= odd:
                #print("nok 2 * pow > odd", odd, p, p * p)
                break
            
            if odd == primes + 2 * p:
                print("true: ", odd, " = ", primes, " + 2 * ", p)
                l.remove(odd)
                break

