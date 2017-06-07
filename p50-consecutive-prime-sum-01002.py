"""
The prime 41, can be written as the sum of six consecutive primes:

    41 = 2 + 3 + 5 + 7 + 11 + 13
    This is the longest sum of consecutive primes that adds to a
    prime below one-hundred.

    The longest sum of consecutive primes below one-thousand that
    adds to a prime, contains 21 terms, and is equal to 953.

    Which prime, below one-million, can be written as the sum of
    the most consecutive primes?
"""

from _eulertools import isPrime
import time
import operator


startTime = time.strftime("%H:%M:%S")
print(startTime)

lim = 1000001
suma = 0
lcount = []
d = {}

# create list of primes
lpn = [x for x in range(3, lim, 2) if isPrime(x)]
lpn.insert(0, 2)
print(len(lpn), lpn[-1])

j = 0
while j < len(lpn):

    count = []
    suma = 0
    stop = False
    i = j
    while i < len(lpn) and not stop:
        suma += lpn[i]
        count.append(lpn[i])

        if suma >= lpn[-1]:
            stop = True

        if suma in lpn and lpn[i] != suma:
            lcount.append((suma, len(count)))

            if suma not in d:
                d[suma] = int(len(count))
            else:
                d[suma] = max(d[suma], len(count))
        i += 1

    j += 1

print("len lpn: ", len(lpn))
mx = max(d.items(), key=operator.itemgetter(1))[0]
print("\nPrime: ", mx, "consecutive primes: ", d[mx])


endTime = time.strftime("%H:%M:%S")
print("start: ", startTime, ">>>", endTime)
