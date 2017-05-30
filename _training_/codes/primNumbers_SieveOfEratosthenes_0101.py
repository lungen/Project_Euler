
"""
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

Pseudocode
The sieve of Eratosthenes can be expressed in pseudocode, as follows:

 Input: an integer n > 1.

 Let A be an array of Boolean values, indexed by integers 2 to n,
 initially all set to true.

 for i = 2, 3, 4, ..., not exceeding √n:
   if A[i] is true:
     for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n:
       A[j] := false.

Output: all i such that A[i] is true
"""


import math
import time


def sieveOfEratosthenes(n):
    global result

    start = time.time()

    l = list(range(2, n + 1))

    for i in range(2, int(math.sqrt(n))):
        if i in l:
            for j in range(2 * i, n + 1, i):
                if j in l:
                    l.remove(j)

    end = time.time()
    result = end - start
    return l


print("{0}, {1:4f} ms".format(sieveOfEratosthenes(100), result))
