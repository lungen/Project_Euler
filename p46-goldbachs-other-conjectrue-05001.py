# -*- coding: utf-8 -*-

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

import time


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

u = 9000

# create odd composite numbers
l = [i for i in range(9, u + 1, 2) if not isPrime(i)]

# create prime numbers
pn = [i for i in range(2, u + 1) if isPrime(i)]

stop = False
cancel = False

for odd in l:
    cancel = True

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
                cancel = False
                break

            p += 1
        i += 1
    stop = False
    # if odd number is not divisible; CANCEL
    if cancel:
        print("cancel true")
        print("odd nr: ", odd)
        break

end = time.time()
endTime = time.strftime("%H:%M:%S")

print("fin time:", endTime)
print("minutes : ", (end / 60))
