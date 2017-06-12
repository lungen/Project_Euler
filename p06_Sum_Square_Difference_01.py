# -*- coding: utf-8 -*-
"""
The sum of the squares of the first ten natural numbers is,

1² + 2² + ... + 10² = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)² = 55² = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""
# A: 25164150


def suma_of_squares(n=10):
    suma, sumb = 0, 0
    for x in xrange(1, n+1):
        suma += x * x
        sumb += x
    return (sumb * sumb) - suma

sos = suma_of_squares(100)
print(sos)
