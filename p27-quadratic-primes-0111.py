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


def primresult(n, a):
    while n < a:
        result = n * n + n + a
        print(result, end=', ')
        n = n + 1


def primeRunner(n=0, a=1):
    # n² + an + b
    # n² + n + 41

    l = []
    lim = 50
    maxi = []

    #while math.sqrt(n) <= a and math.sqrt <= b:
    while n < a:
        while a < lim:
            result = n * n + n + a
            while result in listOfPrimeNumbers:
                l.append(result)
                n = n + 1
                result = n * n + n + a
            else:
                if len(l) > len(maxi):
                    maxi = l[:]
                    #maxi.append(("n: ", n))
                    maxi.insert(0, ("n, a", n, a))
                l = []
                a = a + 1
                n = 0
        n = n + 1

    return maxi


global listOfPrimeNumbers
listOfPrimeNumbers = sieveOfEratosthenes(1000)

print(primeRunner())
print("\nlen: ", len(primeRunner()))
