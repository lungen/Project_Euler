
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


def primeRunner(n=0, a=-999, b=-1000):
    # n² + an + b
    # n² + n + 41

    l = []
    maxi = []
    lim = 1000

    while n < abs(b):
        while abs(a) < lim:
            while abs(b) <= lim:
                result = n * n + a * n + b
                while abs(result) in listOfPrimeNumbers:
                    l.append(result)
                    n = n + 1
                    result = n * n + a * n + b
                else:
                    if len(l) > len(maxi):
                        maxi = l[:]
                        maxi.insert(0, ("n, a, b", n, a, b))
                    l = []
                    b = b + 1
                    while not abs(b) in listOfPrimeNumbers:
                        b = b + 1
                    n = 0
            a = a + 1
            while not a % 2:
                a = a + 1
            b = 0
        n = n + 1
        a = 0

    print("len: ", len(maxi))
    return maxi


global listOfPrimeNumbers
listOfPrimeNumbers = sieveOfEratosthenes(10000)

print(primeRunner())
