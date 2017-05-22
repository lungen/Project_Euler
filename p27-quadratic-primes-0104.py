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


def primeIt(n, a, b, i):

    limit = 3

    if a >= limit or b > limit:
        return

    resList = []

    while math.sqrt(n) <= a and math.sqrt(n) <= b:
        for _, ea in enumerate(listOfPrimeNumbers):
            a = ea
            if a < limit:
                for _, eb in enumerate(listOfPrimeNumbers):
                    b = eb
                    if b <= limit:
                        # print("n, a, b", n, a, b)
                        result = n * n + a * n + b
                        if result in listOfPrimeNumbers:
                            resList.append((n, result, a, b, i))
                            #if n in diprime:
                                #diprime[n] = diprime[n], result, a, b, i
                            #else:
                                #diprime[n] = result, a, b, i
                            primeIt(n + 1, a, b, i)
                            #print(i, n, a, b, end=', ')
                            #print(n * n, "+", a * n, "+", b)
                            #n = n + 1
                        i = i + 1
                    else:
                        break
            else:
                break
        n = n + 1

    #print(len(resList))
    return resList


# create list of prime numbers
global listOfPrimeNumbers
listOfPrimeNumbers = sieveOfEratosthenes(1000)

global diPrime
diprime = {}
p = primeIt(0, 0, 0, 1)
print(p)
print(len(p))

#print(diprime.items())
