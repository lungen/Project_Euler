# -*- coding: utf-8 -*-
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
# A: 31875000, a, b, c = 200, 375, 425


def start(lim=1000):
    for a in xrange(1, lim):
        for b in xrange(a+1, lim):
            for c in xrange(b+1, lim):
                if a < b < c:
                    if a*a + b*b == c*c:
                        if a + b + c == 1000:
                            print("THATS IT: ", a, b, c, (a + b + c))
                            print("\na² + b² = c²", a*a, b*b, c*c)
                            print("product of abc: ", a*b*c)
                            return a*b*c

f = start()
