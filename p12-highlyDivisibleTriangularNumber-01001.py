import math


# https://stackoverflow.com/questions/171765/what-is-the-best-way-to-get-all-the-divisors-of-a-number#171784
def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor


# get nth triangle number, f.e: T(3) = 6
def getTriangleNumber(n):
    return int(((n * (n + 1)) / 2))


#print(list(divisorGenerator(1234)))
print("--> start")
i = 1
while (i != 100000):
    if (len(list(divisorGenerator(getTriangleNumber(i))))) >= 500:
        print("bingo: ", i, getTriangleNumber(i))
        break
    i += 1
print("--> fin: ", i)
