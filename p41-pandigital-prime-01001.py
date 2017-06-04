import itertools


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


s = '7654321'

pn = list(itertools.permutations(s))
pp = ["".join(x) for x in pn]
for i in pp:
    #print(i)
    if isPrime(int(i)):
        print("prime: ", i)
        break
    
