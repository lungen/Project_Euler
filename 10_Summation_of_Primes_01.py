# -*- coding: utf-8 -*-
"""
Summation of primes
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def start(lim=2000000):

    pzl = [2]
    Rest = []
    suma = 2

    for i in xrange(3, lim):
        for e, v in enumerate(pzl):
            if not i % v:
                Rest.append(False)
                break
            else:
                Rest.append(True)
                continue

        if False not in Rest:
            pzl.append(i)
            suma += i

        Rest = []

    return suma


print(start())
