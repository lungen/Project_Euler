"""
http://mathforum.org/library/drmath/view/54367.html

"""


def divid(n):

    import math

    l = []

    for i in range(1, math.floor(math.sqrt(n)) + 1):
        if not n % i:
            l.extend(map(int, (i, n/i)))

    l = sorted(l)
    print(l)

    suma = 0
    # for idx, k in enumerate(sorted(l)):
    for k in range(len(l) - 1):
        print(l[k])
        suma += l[k]

    print("Sum of divisors of {0} = {1}".format(n, suma))
    print("When the sum of proper dividors equals n, the number is perfect")



divid(48)
