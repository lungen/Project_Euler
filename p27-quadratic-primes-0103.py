# http://mathworld.wolfram.com/Prime-GeneratingPolynomial.html
# http://www.virtualnerd.com/algebra-2/polynomials/equations/factoring-strategies/prime-polynomial-definition


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


def primeIt(limit):

    n = 0
    a = 0
    b = 0
    i = 1

    resList = []

    while math.sqrt(n) <= a and math.sqrt(n) <= b:
        a = 0
        while a < limit:
            b = 0
            while b <= limit:
                result = n * n + a * n + b
                if result in listOfPrimeNumbers:
                    resList.append((result, n, a, b, i))
                    #print(result, end=', ')
                    #print(i, n, a, b, end=', ')
                    #print(n * n, "+", a * n, "+", b)
                    #n = n + 1
                b = b + 1
                i = i + 1
            a = a + 1
        n = n + 1

    #print(len(resList))
    return resList


# create list of prime numbers
global listOfPrimeNumbers
listOfPrimeNumbers = sieveOfEratosthenes(1000)
print(primeIt(5))
