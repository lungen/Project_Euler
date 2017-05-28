import math
import time
import _tools


def sieveOfEratosthenes(n):

    start = time.time()

    l = list(range(2, n + 1))

    for i in range(2, int(math.sqrt(n))):
        if i in l:
            for j in range(2 * i, n + 1, i):
                if j in l:
                    l.remove(j)

    end = time.time()
    result = end - start
    print("time: {0:5f} seconds." .format(result))
    return l


data = sieveOfEratosthenes(10000000)
_tools.save_it(data, "primeList_10Mil.txt")
